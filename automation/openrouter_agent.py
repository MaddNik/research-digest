#!/usr/bin/env python3
"""Tool-calling harness that replaces `claude -p ... --dangerously-skip-permissions`
for headless automation, billed via an OpenRouter API key instead of the
Claude subscription's usage window. Stdlib-only, no new pip dependency.

Exit codes: 0 success, 1 API/config error, 2 hit --max-iterations without a
natural stop.
"""
import argparse
import html as html_mod
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "anthropic/claude-sonnet-5"
MAX_ITERATIONS = 40
BASH_TIMEOUT = 180
FETCH_TIMEOUT = 60
API_TIMEOUT = 180
MAX_TOOL_OUTPUT = 20000  # chars; longer tool output is truncated


def load_api_key():
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not key:
        print("FATAL: OPENROUTER_API_KEY is not set", file=sys.stderr)
        sys.exit(1)
    return key


def truncate(text, limit=MAX_TOOL_OUTPUT):
    if len(text) <= limit:
        return text
    return text[:limit] + f"\n...[truncated, {len(text) - limit} more chars]"


def _require_absolute(path):
    p = Path(path)
    if not p.is_absolute():
        return None
    return p


# ---- tool implementations ----

def tool_bash(command, cwd=None, timeout=BASH_TIMEOUT):
    cwd = cwd or str(REPO_ROOT)
    try:
        proc = subprocess.run(
            ["bash", "-c", command],
            cwd=cwd,
            timeout=timeout,
            capture_output=True,
            text=True,
        )
        out = f"exit_code: {proc.returncode}\nstdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
        return truncate(out)
    except subprocess.TimeoutExpired:
        return f"ERROR: command timed out after {timeout}s"
    except Exception as e:
        return f"ERROR: {e}"


def tool_read_file(path):
    p = _require_absolute(path)
    if p is None:
        return f"ERROR: path must be absolute, got: {path}"
    if not p.exists():
        return f"ERROR: file not found: {path}"
    try:
        return truncate(p.read_text(errors="replace"))
    except Exception as e:
        return f"ERROR: {e}"


def tool_write_file(path, content):
    p = _require_absolute(path)
    if p is None:
        return f"ERROR: path must be absolute, got: {path}"
    try:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        return f"OK: wrote {len(content)} chars to {path}"
    except Exception as e:
        return f"ERROR: {e}"


def tool_edit_file(path, old_string, new_string):
    p = _require_absolute(path)
    if p is None:
        return f"ERROR: path must be absolute, got: {path}"
    if not p.exists():
        return f"ERROR: file not found: {path}"
    try:
        text = p.read_text()
    except Exception as e:
        return f"ERROR: {e}"
    count = text.count(old_string)
    if count == 0:
        return "ERROR: old_string not found in file"
    if count > 1:
        return f"ERROR: old_string matches {count} times, must match exactly once"
    p.write_text(text.replace(old_string, new_string, 1))
    return f"OK: replaced 1 occurrence in {path}"


def _strip_html(raw_html):
    text = re.sub(r"(?is)<(script|style)\b.*?</\1\s*>", "", raw_html)
    text = re.sub(r"(?s)<!--.*?-->", "", text)
    text = re.sub(r"(?is)<br\s*/?>", "\n", text)
    text = re.sub(r"(?is)</p\s*>", "\n\n", text)
    text = re.sub(r"(?is)<[^>]+>", "", text)
    text = html_mod.unescape(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def tool_fetch_url(url, mode="text", dest_path=None):
    req = urllib.request.Request(
        url, headers={"User-Agent": "Mozilla/5.0 (research-tracker-automation)"}
    )
    try:
        with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
            content_type = resp.headers.get("Content-Type", "")
            data = resp.read()
    except urllib.error.HTTPError as e:
        return f"ERROR: HTTP {e.code} fetching {url}"
    except Exception as e:
        return f"ERROR: {e}"

    if mode == "download":
        if not dest_path:
            return "ERROR: mode=download requires dest_path"
        p = _require_absolute(dest_path)
        if p is None:
            return f"ERROR: dest_path must be absolute, got: {dest_path}"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
        return f"OK: downloaded {len(data)} bytes to {dest_path} (content-type: {content_type})"

    is_binary_type = any(
        marker in content_type.lower()
        for marker in ("application/pdf", "application/octet-stream", "image/", "application/zip")
    )
    looks_binary = b"\x00" in data[:2000]
    if is_binary_type or looks_binary:
        return (
            f"ERROR: response looks binary (content-type: {content_type}, "
            f"{len(data)} bytes). Use mode=\"download\" with a dest_path instead "
            "of mode=\"text\" for this URL."
        )

    text = data.decode("utf-8", errors="replace")
    if "html" in content_type.lower():
        text = _strip_html(text)
    return truncate(text)


TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "bash",
            "description": "Run a bash command. cwd defaults to the repo root.",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {"type": "string"},
                    "cwd": {"type": "string", "description": "Absolute working directory (optional)"},
                    "timeout": {"type": "integer", "description": "Seconds (optional)"},
                },
                "required": ["command"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a file. path must be absolute.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Create or overwrite a file. path must be absolute.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "edit_file",
            "description": (
                "Replace exactly one occurrence of old_string with new_string in a "
                "file. Fails if old_string matches zero or more than one time."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "old_string": {"type": "string"},
                    "new_string": {"type": "string"},
                },
                "required": ["path", "old_string", "new_string"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "fetch_url",
            "description": (
                "Fetch a URL. mode=text (default) returns readable text with HTML "
                "stripped. mode=download streams raw bytes to dest_path (absolute "
                "path, required for download mode) - use this for PDFs and other "
                "binary files before processing them with bash."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {"type": "string"},
                    "mode": {"type": "string", "enum": ["text", "download"]},
                    "dest_path": {"type": "string"},
                },
                "required": ["url"],
            },
        },
    },
]

TOOL_DISPATCH = {
    "bash": tool_bash,
    "read_file": tool_read_file,
    "write_file": tool_write_file,
    "edit_file": tool_edit_file,
    "fetch_url": tool_fetch_url,
}


def call_openrouter(messages, model, tools=None, tool_choice=None, response_format=None, max_retries=5):
    api_key = load_api_key()
    body = {"model": model, "messages": messages}
    if tools:
        body["tools"] = tools
    if tool_choice:
        body["tool_choice"] = tool_choice
    if response_format:
        body["response_format"] = response_format

    data = json.dumps(body).encode("utf-8")
    delay = 2
    for attempt in range(max_retries):
        req = urllib.request.Request(
            OPENROUTER_URL,
            data=data,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://maddnik.github.io/research-digest",
                "X-Title": "research-digest-automation",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=API_TIMEOUT) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            if (e.code == 429 or e.code >= 500) and attempt < max_retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            print(f"FATAL: OpenRouter HTTP {e.code}: {err_body}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            print(f"FATAL: OpenRouter request failed: {e}", file=sys.stderr)
            sys.exit(1)
    print("FATAL: exhausted retries calling OpenRouter", file=sys.stderr)
    sys.exit(1)


def run_agent_loop(system_prompt, user_prompt, model, max_iterations=MAX_ITERATIONS, debug_log=None):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    def log(entry):
        if debug_log:
            with open(debug_log, "a") as f:
                f.write(json.dumps(entry) + "\n")

    for _ in range(max_iterations):
        resp = call_openrouter(messages, model, tools=TOOLS_SCHEMA, tool_choice="auto")
        msg = resp["choices"][0]["message"]
        messages.append(msg)
        log({"role": "assistant", "content": msg.get("content"), "tool_calls": msg.get("tool_calls")})

        tool_calls = msg.get("tool_calls")
        if not tool_calls:
            return msg.get("content") or ""

        for tc in tool_calls:
            fn = tc["function"]
            name = fn["name"]
            try:
                args = json.loads(fn.get("arguments") or "{}")
            except json.JSONDecodeError as e:
                result = f"ERROR: invalid JSON arguments: {e}"
            else:
                impl = TOOL_DISPATCH.get(name)
                if not impl:
                    result = f"ERROR: unknown tool {name}"
                else:
                    try:
                        result = impl(**args)
                    except TypeError as e:
                        result = f"ERROR: bad arguments for {name}: {e}"
                    except Exception as e:
                        result = f"ERROR: {name} raised: {e}"
            log({"role": "tool_call", "name": name, "arguments": fn.get("arguments"), "result": result})
            messages.append({"role": "tool", "tool_call_id": tc["id"], "content": result})

    print(f"HARNESS: hit max_iterations ({max_iterations}) without natural completion", file=sys.stderr)
    sys.exit(2)


def verify_summary(source_text, draft_json_text, model):
    """Deep-summary adversarial check, replacing SKILL.md's Agent-tool subagent call."""
    system = (
        "You are an adversarial summary verifier with zero tolerance for unsupported "
        "claims and zero tolerance for missed key content. Compare the DRAFT summary "
        "JSON against the SOURCE text. Respond with ONLY a JSON object of this exact "
        'shape: {"hallucinations": [{"claim": "...", "why": "not supported by source"}], '
        '"omissions": [{"missing": "...", "where_in_source": "..."}], "ok": true|false}. '
        '"ok" is true only if there are no hallucinations and no significant omissions.'
    )
    user = (
        f"SOURCE:\n{truncate(source_text, 150000)}\n\n"
        f"DRAFT SUMMARY JSON:\n{truncate(draft_json_text, 40000)}"
    )
    resp = call_openrouter(
        [{"role": "system", "content": system}, {"role": "user", "content": user}],
        model,
        response_format={"type": "json_object"},
    )
    text = resp["choices"][0]["message"].get("content") or ""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", text, re.S)
        if m:
            try:
                return json.loads(m.group(0))
            except json.JSONDecodeError:
                pass
        print(f"WARNING: verify_summary could not parse model output as JSON: {text[:500]}", file=sys.stderr)
        return {"hallucinations": [], "omissions": [], "ok": False}


def run_verify_if_deep(result_text, var_map, model):
    """If --var LEVEL=deep was passed, look for a `JOB_DIR: <path>` line in the
    final report, and if the job directory has both content.json and
    raw_source.txt, run the adversarial VERIFY step and update content.json's
    "verified" field in place."""
    if var_map.get("LEVEL") != "deep":
        return result_text

    m = re.search(r"^JOB_DIR:\s*(.+)$", result_text, re.M)
    if not m:
        return result_text + "\n\nVERIFY: skipped (no JOB_DIR line in the final report)"

    job_dir = Path(m.group(1).strip())
    content_path = job_dir / "content.json"
    source_path = job_dir / "raw_source.txt"
    if not content_path.exists() or not source_path.exists():
        return result_text + (
            f"\n\nVERIFY: skipped (content.json or raw_source.txt missing under {job_dir})"
        )

    try:
        content = json.loads(content_path.read_text())
        source_text = source_path.read_text()
        verdict = verify_summary(source_text, json.dumps(content), model)
        content["verified"] = bool(verdict.get("ok"))
        content_path.write_text(json.dumps(content, indent=2))
        return result_text + (
            f"\n\nVERIFY: ok={verdict.get('ok')} "
            f"hallucinations={len(verdict.get('hallucinations', []))} "
            f"omissions={len(verdict.get('omissions', []))}"
        )
    except Exception as e:
        return result_text + f"\n\nVERIFY: failed to run ({e})"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt-file", required=True)
    parser.add_argument("--system-prompt-file")
    parser.add_argument("--model", default=os.environ.get("OPENROUTER_MODEL", DEFAULT_MODEL))
    parser.add_argument("--var", action="append", default=[], metavar="KEY=VALUE")
    parser.add_argument("--max-iterations", type=int, default=MAX_ITERATIONS)
    parser.add_argument("--debug-log", help="Append a JSONL trace of every assistant/tool turn to this file")
    args = parser.parse_args()

    prompt_text = Path(args.prompt_file).read_text()

    var_map = {}
    for item in args.var:
        if "=" not in item:
            print(f"FATAL: --var must be KEY=VALUE, got: {item}", file=sys.stderr)
            sys.exit(1)
        k, v = item.split("=", 1)
        var_map[k] = v
    # Literal ${KEY} substitution rather than string.Template: these prompt
    # files are full of literal LaTeX `$...$` delimiters, which
    # Template.substitute() rejects as invalid placeholders.
    for k, v in var_map.items():
        prompt_text = prompt_text.replace("${%s}" % k, v)

    system_prompt_path = (
        Path(args.system_prompt_file)
        if args.system_prompt_file
        else Path(__file__).parent / "harness-system-prompt.md"
    )
    system_prompt = system_prompt_path.read_text()

    result = run_agent_loop(system_prompt, prompt_text, args.model, args.max_iterations, debug_log=args.debug_log)
    result = run_verify_if_deep(result, var_map, args.model)
    print(result)


if __name__ == "__main__":
    main()
