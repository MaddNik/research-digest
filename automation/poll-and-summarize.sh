#!/usr/bin/env bash
# Poll open "summary-request" GitHub issues and run summarize-anything on each.
# Invoked by cron during the weekday run slot. Uses the existing headless `claude`
# (subscription login, no Anthropic API) and the existing GitHub PAT via curl
# (no `gh` dependency). The Stop hook (sync-summaries.sh) auto-publishes + pushes
# when claude exits, so this script never publishes itself.
#
# Usage gate: skips when the cached Claude 5h/7d usage is >= 95% (cache written by
# ~/.claude/statusline.py). If a run still hits the limit, the issue is left queued
# and retried in the next slot.
set -uo pipefail

export HOME=/home/nik
export PATH="/home/nik/.local/bin:/home/nik/.npm-global/bin:/usr/local/bin:/usr/bin:/bin"

REPO="/home/nik/research-digest"
OWNER="MaddNik"
GH_REPO="$OWNER/research-digest"
API="https://api.github.com/repos/$GH_REPO"
PAGES_BASE="https://maddnik.github.io/research-digest/summaries"
RM="/home/nik/research-material"
CACHE="$HOME/.claude/rate-limits-cache.json"
PROMPT="$REPO/automation/summarize-request-prompt.md"
LOGDIR="$REPO/automation/logs"
LOCK="$REPO/automation/.poll.lock"
USAGE_MAX=95
RETRY_CAP=2
# Model for headless deep-summary generation.
MODEL=opus

TOKEN="$(cat "$HOME/.gh_pat" 2>/dev/null)"
[ -n "$TOKEN" ] || TOKEN="$(sed -n 's#https://[^:]*:\([^@]*\)@github.com#\1#p' "$HOME/.git-credentials" 2>/dev/null | head -1)"

# --- GitHub REST helpers (curl + PAT) --------------------------------------
api()  { curl -fsS  -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github+json" "$@"; }
apiq() { curl -fsS -o /dev/null -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github+json" "$@"; }
jbody(){ python3 -c 'import json,sys;print(json.dumps({"body":sys.argv[1]}))' "$1"; }

add_label()    { apiq -X POST  -d "{\"labels\":[\"$2\"]}" "$API/issues/$1/labels" 2>/dev/null || true; }
remove_label() { curl -s -o /dev/null -X DELETE -H "Authorization: token $TOKEN" "$API/issues/$1/labels/$2" 2>/dev/null || true; }
comment()      { api -X POST -d "$(jbody "$2")" "$API/issues/$1/comments" >/dev/null 2>&1 || true; }
close_issue()  { apiq -X PATCH -d '{"state":"closed"}' "$API/issues/$1" 2>/dev/null || true; }

mkdir -p "$LOGDIR"
TS="$(date +%Y-%m-%d_%H%M%S)"
LOG="$LOGDIR/poll-$TS.log"

# --- single-instance lock (skip if another poller is running) ---
exec 9>"$LOCK"
if ! flock -n 9; then
  echo "another poller is running; exiting" >>"$LOG"
  exit 0
fi

cd "$REPO" || exit 1

{
  echo "=== poll $TS ==="
  if [ -z "$TOKEN" ]; then echo "no GitHub token found; exiting"; exit 1; fi
  git pull --rebase --autostash 2>&1 || echo "(pull failed, continuing)"

  # --- usage gate -------------------------------------------------------------
  GATE="$(python3 - "$CACHE" "$USAGE_MAX" <<'PY'
import json, sys, time
path, umax = sys.argv[1], float(sys.argv[2])
try:
    d = json.load(open(path))
except Exception:
    print("STALE -1 -1"); raise SystemExit
age = time.time() - float(d.get("written_at") or 0)
rl = d.get("rate_limits") or {}
def pct(k):
    v = (rl.get(k) or {}).get("used_percentage")
    try: return float(v)
    except (TypeError, ValueError): return -1.0
h5, d7 = pct("five_hour"), pct("seven_day")
if age > 1800:        print("STALE %.0f %.0f" % (h5, d7))
elif h5 >= umax or d7 >= umax: print("SKIP %.0f %.0f" % (h5, d7))
else:                 print("RUN %.0f %.0f" % (h5, d7))
PY
)"
  echo "usage gate: $GATE"
  if [ "${GATE%% *}" = "SKIP" ]; then echo "no headroom (>= ${USAGE_MAX}%); exiting"; exit 0; fi
  # STALE or RUN both proceed (STALE relies on the limit-error safety net).

  # --- fetch all open summary requests (any creator) -------------------------
  ROWS="$(api "$API/issues?state=open&labels=summary-request&per_page=50" \
          | python3 -c '
import sys, json, base64
for it in json.load(sys.stdin):
    if it.get("pull_request"): continue
    num = it["number"]
    labels = ",".join(l["name"] for l in it.get("labels", []))
    body = base64.b64encode((it.get("body") or "").encode()).decode()
    print("%s\t%s\t%s" % (num, labels, body))
')"

  if [ -z "$ROWS" ]; then echo "no open summary requests"; exit 0; fi

  printf '%s\n' "$ROWS" | while IFS=$'\t' read -r NUM LABELS BODY64; do
    [ -n "$NUM" ] || continue
    case ",$LABELS," in
      *,summarizing,*|*,summarized,*) echo "skip #$NUM (labels: $LABELS)"; continue ;;
    esac

    BODY="$(printf '%s' "$BODY64" | base64 -d 2>/dev/null)"
    SRC="$(printf '%s\n' "$BODY" | grep -ioE 'https?://[^ )"<>]+' | head -1)"
    LEVEL="$(printf '%s\n' "$BODY" | grep -ioE '\b(deep|full|page)\b' | head -1)"; LEVEL="${LEVEL:-deep}"
    CAT="$(printf '%s\n' "$BODY" | grep -ioE 'Photonics|PQC|FHE|Cryptography|Hardware Security|Other' | head -1)"; CAT="${CAT:-Other}"

    if [ -z "$SRC" ]; then
      echo "#$NUM has no source URL"
      comment "$NUM" "Could not find a source URL in this request. Please edit the issue to include a valid link."
      add_label "$NUM" needs-info
      continue
    fi

    # --- dedupe: if a summary for this arXiv id already exists, relink + close --
    ARXIV="$(printf '%s' "$SRC" | grep -oiE '[0-9]{4}\.[0-9]{4,5}' | head -1)"
    if [ -n "$ARXIV" ]; then
      EXIST_URL="$(python3 - "$REPO/_data/summaries.yml" "$ARXIV" <<'PY'
import sys, re
path, arx = sys.argv[1], sys.argv[2]
url = ""
try:
    for line in open(path):
        m = re.match(r'\s*url:\s*"([^"]+)"', line)
        if m: url = m.group(1)
        if "source_url" in line and arx in line:
            print(url); break
except Exception:
    pass
PY
)"
      if [ -n "$EXIST_URL" ]; then
        echo "#$NUM already summarized (arXiv $ARXIV) -> $EXIST_URL"
        comment "$NUM" "A deep summary already exists: https://maddnik.github.io/research-digest${EXIST_URL}"
        add_label "$NUM" summarized
        close_issue "$NUM"
        continue
      fi
    fi

    echo "--- processing #$NUM  src=$SRC  level=$LEVEL  cat=$CAT"
    add_label "$NUM" summarizing
    BEFORE="$(find "$RM" -maxdepth 3 -name summary.html 2>/dev/null | sort -u)"

    PROMPT_TEXT="$(SRC="$SRC" LEVEL="$LEVEL" CAT="$CAT" envsubst '${SRC} ${LEVEL} ${CAT}' < "$PROMPT")"
    OUT="$(claude -p "$PROMPT_TEXT" --model "$MODEL" --dangerously-skip-permissions --output-format text < /dev/null 2>&1)"
    RC=$?
    printf '%s\n' "$OUT"

    git pull --rebase --autostash 2>&1 || true   # Stop hook published during the run

    if printf '%s' "$OUT" | grep -qiE 'usage limit|resets at|5-hour limit|hit your limit'; then
      echo "#$NUM limit-blocked; requeueing for next slot"
      remove_label "$NUM" summarizing
      break
    fi

    AFTER="$(find "$RM" -maxdepth 3 -name summary.html 2>/dev/null | sort -u)"
    NEW_DIR="$(comm -13 <(printf '%s\n' "$BEFORE") <(printf '%s\n' "$AFTER") | head -1)"

    if [ "$RC" -eq 0 ] && [ -n "$NEW_DIR" ]; then
      SLUG="$(basename "$(dirname "$NEW_DIR")")"
      echo "#$NUM done -> $SLUG"
      comment "$NUM" "Deep summary published: ${PAGES_BASE}/${SLUG}/ (live after the next Pages build)."
      add_label "$NUM" summarized
      remove_label "$NUM" summarizing
      close_issue "$NUM"
    else
      echo "#$NUM produced no summary (rc=$RC)"
      FAILS="$(api "$API/issues/$NUM/comments" 2>/dev/null | python3 -c 'import sys,json;print(sum(1 for c in json.load(sys.stdin) if "did not produce a summary" in (c.get("body") or "")))' 2>/dev/null || echo 0)"
      comment "$NUM" "Automated summarization did not produce a summary (exit $RC). Leaving open for retry."
      remove_label "$NUM" summarizing
      add_label "$NUM" summary-failed
      if [ "${FAILS:-0}" -ge "$RETRY_CAP" ]; then add_label "$NUM" needs-info; echo "#$NUM hit retry cap"; fi
    fi
  done

  echo "=== done ==="
} >>"$LOG" 2>&1

ls -1t "$LOGDIR"/poll-*.log 2>/dev/null | tail -n +13 | xargs -r rm -f
