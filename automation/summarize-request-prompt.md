You are running non-interactively (headless) in /home/nik/research-digest, which
is authenticated to push to GitHub. Style rules: no em dashes, no emojis, recreate
all mathematics as proper LaTeX, put all code/pseudocode in code blocks.

Task: produce ONE summary for a single source, then exit. Do NOT commit or push
anything yourself. There is no web-search tool; only fetch URLs you're given or
that appear as links on a page you've already fetched.

- Source URL: ${SRC}
- Requested level: ${LEVEL}
- Site category (one of Photonics, PQC, FHE, Cryptography, Hardware Security, Other): ${CAT}

This reproduces the summarize-anything skill's pipeline directly (no skill-loading
mechanism is available here, so the relevant steps are inlined below). A separate
CLI at `/home/nik/.claude/skills/summarize-anything/scripts/cli.py` still does the
PDF/image parsing and final HTML rendering; run every `python -m scripts.cli ...`
command below with `cwd` explicitly set to
`/home/nik/.claude/skills/summarize-anything/` (the bash tool otherwise defaults to
this repo's root, and the CLI resolves relative paths under its own directory,
which silently breaks figure paths if you don't pass absolute paths for every
job/file argument).

## 0. PROBE
Run (cwd = the skill directory above): `python -m scripts.cli probe`. If `ready`
comes back false, continue in text-only mode: skip figure extraction, describe
any figures in words, and note this in your final report.

## 1. DETECT
Run: `python -m scripts.cli detect "${SRC}"`. Use the returned `kind` to pick the
ACQUIRE branch below. If `kind` is `unknown`, report the format is unsupported and
stop (do not write anything under research-material).

## 2. Choose the category and job directory
List existing categories: `bash: ls ~/research-material`. Choose a topical
kebab-case `<category>` folder by the source's TOPIC, not by the site category
above. Map loosely: FHE topics to an existing `fhe*`/`tfhe*` folder if one clearly
fits; Photonics to a `photonics-*` folder; PQC or Cryptography to a `pqc-*` or
`crypto-*` folder; Hardware Security to a `hardware-security-*` folder.

If the best-fitting folder already exists AND already holds other material,
create a NEW dedicated folder instead of merging into it (this is the headless
default; do not ask, since nobody can answer).

Form the job path `~/research-material/<category>/<slug>-<YYYY-MM-DD>/` with an
`assets/` subdirectory, where `<slug>` is a lowercased, hyphenated slug from the
source's title. Use the absolute form of this path (expand `~`) for every command
below.

## 3. ACQUIRE - build a source bundle (ordered text + asset manifest)
Branch on the `kind` from step 1:
- **pdf**: first `fetch_url` the source URL with `mode: "download"` and an
  absolute `dest_path` under the job directory (e.g. `<job>/source.pdf`), then
  run (cwd = the skill directory): `python -m scripts.cli parse-pdf "<absolute
  path to source.pdf>" "<absolute job path>/assets"`. If the returned `subtype`
  is `image-only`, you have no native vision tool here: fall back to text-only
  mode for this source (report this in the final message; do not fabricate a
  description of pages you cannot read). Use the returned `assets` list as
  candidate figures.
- **web**: the DETECT script only recognizes URLs literally ending in `.pdf`
  as `kind: pdf`; an arXiv abstract page (`arxiv.org/abs/...`) or an IACR
  ePrint page (`eprint.iacr.org/YYYY/NNNN`) both come back as `kind: web`
  even though a full-text PDF exists. **If the URL is an arXiv or IACR
  ePrint page, you MUST still acquire the actual PDF, not just the abstract
  page text** - an abstract alone is nowhere near enough to write a grounded
  summary, and filling in details from your own training knowledge instead
  of the fetched source is exactly the hallucination this task exists to
  prevent. Build the PDF URL yourself (arXiv: replace `/abs/` with `/pdf/`
  in the URL, or append `.pdf`; ePrint: append `.pdf` to the abstract URL),
  `fetch_url` it with `mode: "download"` to `<job>/source.pdf`, then follow
  the **pdf** branch above (`parse-pdf`, etc.) on that file. Only fall back
  to abstract-only text, with an explicit note in your final report that you
  could not get the full text, if the PDF genuinely isn't fetchable (e.g. a
  paywall or a block you can't get past). For any other kind of `web` source
  (a blog post, a documentation page, etc.) `fetch_url` the URL with
  `mode: "text"` directly.
- **text**: `fetch_url` the URL with `mode: "text"`, or `read_file` if it's
  already local.
- **repo** (a GitHub URL): `bash: git clone --depth 1 <url> <job>/repo`, then
  `read_file` the README and key source/config files, and detect the primary
  language(s). Any diagrams/screenshots already committed under paths like
  `docs/` or `assets/` are candidate figures; copy the ones you use into
  `<job>/assets` with `bash`. Delete `<job>/repo` when done.
- **image**: `fetch_url` with `mode: "download"` to a local path. You have no
  native vision tool here; report the figure by filename/context only, note the
  limitation, and continue with whatever surrounding text is available.
- **office** (`.docx`/`.pptx`/`.xlsx`): `fetch_url` with `mode: "download"`, then
  attempt to extract text with `bash` (e.g. a Python one-liner using a library
  already installed, if any). If you cannot extract usable text, report that this
  format is not supported here and stop.
- **notion**: no Notion connector is available here; report that Notion sources
  are unsupported in this environment and stop.

**Save the combined extracted text you gathered in this step** (concatenated PDF
page text, or the fetched page text, or the repo README/file contents, in
whatever order you used them to build the outline) to `<job>/raw_source.txt`
with `write_file`, verbatim, before moving on. This is required for every source
you actually summarize, not optional; it is used afterward to double-check the
summary against the source.

## 4. STRUCTURE and SUMMARIZE
Build an outline (sections, key points, candidate figures ranked by importance)
directly from the source bundle, then write the summary at level ${LEVEL} from
that outline. For very long sources, work through the text in your own passes
rather than delegating to a sub-agent (no sub-agent dispatch mechanism exists
here). Ground the summary only in the source; verify the title, authors, and
venue against what you fetched. Obey these formatting rules exactly, they are
non-negotiable:
- **Equations**: recreate every mathematical expression properly in LaTeX,
  `$...$` inline or `$$...$$` for display. Never leave ASCII pseudo-notation like
  `n^2` or `O(n log n)` in prose; write `$n^2$` and `$O(n \log n)$`.
- **Code and pseudocode**: always in a fenced code block, never a run-on
  paragraph. Preserve indentation.
- **Completeness**: cover every key result, definition, parameter, and step; at
  `deep` level especially, add another section rather than drop material; never
  truncate a section mid-thought.
- **Algorithms appendix (always)**: end the summary with a final section titled
  "Algorithms" containing every algorithm from the source as a self-contained
  pseudocode listing in a code block. If the source has none, say so briefly
  instead of omitting the section.

Never fabricate a figure; skip with a note instead. Never pad to reach a length;
shorter than the source always wins.

## 5. ASSEMBLE
Write `<job>/content.json` with `write_file`, using exactly this shape:
```json
{
  "title": "<source title>",
  "source_type": "<e.g. PDF (text-layer) | GitHub repo | web page>",
  "publisher": "<venue/repository, e.g. arXiv | IACR ePrint 2026/1234 | IEEE TC>",
  "source_url": "${SRC}",
  "level": "${LEVEL}",
  "verified": false,
  "tags": ["<keywords>"],
  "sections": [{"heading": "...", "body_html": "<p>...</p>", "figures": ["<job>/assets/<file>"]}]
}
```
Set `verified` to `false` here regardless of level; for `deep`-level requests,
the harness runs an automatic adversarial check after you finish and updates
this field itself, so do not attempt to verify or edit it yourself. Add
`"concepts"` to `tags` when the summary covers foundational/background material.
Then run (cwd = the skill directory): `python -m scripts.cli build-html
"<absolute job path>/content.json" "<absolute job path>/summary.html"`.

## 6. Do not publish
Do NOT commit or push. A separate Stop hook publishes and pushes automatically
once you exit.

## 7. Report
End your final message with these lines, in this order, so they can be parsed
by the calling script:
```
Summary saved: ~/research-material/<category>/<slug>-<date>/summary.html
  Source: <source_type>  |  Level: ${LEVEL}  |  Category: <category>
  Sections: <N>  |  Figures embedded: <N>  |  Verified: pending
JOB_DIR: <absolute path to the job directory>
```
If PROBE fell back to text-only, add a line noting figure extraction was
unavailable. The `JOB_DIR:` line is required exactly as shown (no extra text on
that line) whenever you created a job directory, even if the summary is
incomplete or degraded, so the harness can find `content.json` and
`raw_source.txt` afterward.
