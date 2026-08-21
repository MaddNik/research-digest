#!/usr/bin/env bash
# Stale-run failsafe - invoked by cron once a day.
# Compares each job's last known success against its expected cadence and,
# if something is overdue, opens/updates a single tracking GitHub issue
# (label "automation-health") so it's visible without digging through logs.
set -uo pipefail

export HOME=/home/nik
export PATH="/home/nik/.local/bin:/home/nik/.npm-global/bin:/usr/local/bin:/usr/bin:/bin"

REPO="/home/nik/research-digest"
LOGDIR="$REPO/automation/logs"
OWNER="MaddNik"
GH_REPO="$OWNER/research-digest"
API="https://api.github.com/repos/$GH_REPO"
LABEL="automation-health"

TOKEN="$(cat "$HOME/.gh_pat" 2>/dev/null)"
[ -n "$TOKEN" ] || TOKEN="$(sed -n 's#https://[^:]*:\([^@]*\)@github.com#\1#p' "$HOME/.git-credentials" 2>/dev/null | head -1)"

api()  { curl -fsS  -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github+json" "$@"; }
apiq() { curl -fsS -o /dev/null -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github+json" "$@"; }
jbody(){ python3 -c 'import json,sys;print(json.dumps({"body":sys.argv[1]}))' "$1"; }

cd "$REPO" || exit 1

now_epoch="$(date +%s)"
age_days() { # age_days <git-log-args...>
  local ts
  ts="$(git log -1 --format=%ct "$@" 2>/dev/null)"
  [ -n "$ts" ] || { echo "-1"; return; }
  echo $(( (now_epoch - ts) / 86400 ))
}

PROBLEMS=()

# Weekly digest: fires every Friday - 8 days gives a 1-day grace window.
w_age="$(age_days --grep='^Research Tracker papers,')"
if [ "$w_age" -ge 0 ] && [ "$w_age" -gt 8 ]; then
  PROBLEMS+=("Weekly papers digest: last successful commit was $w_age days ago (expected every 7 days). Check automation/logs/run-*.log for FATAL/error lines.")
elif [ "$w_age" -lt 0 ]; then
  PROBLEMS+=("Weekly papers digest: no \"Research Tracker papers, ...\" commit found in history at all.")
fi

# Conferences: fires the 1st of each month - 35 days gives grace for short months.
c_age="$(age_days --grep='^Update conferences,')"
if [ "$c_age" -ge 0 ] && [ "$c_age" -gt 35 ]; then
  PROBLEMS+=("Conferences update: last successful commit was $c_age days ago (expected monthly). Check automation/logs/conferences-*.log for FATAL/error lines.")
elif [ "$c_age" -lt 0 ]; then
  PROBLEMS+=("Conferences update: no \"Update conferences, ...\" commit found in history at all.")
fi

# Poll-and-summarize: fires many times a day - if cron stopped invoking it at
# all, no poll-*.log gets written even on an early exit, since the log file
# is created before any real work starts. Absence for 24h+ means cron itself
# isn't running the script, not just "nothing to do".
newest_poll_log="$(ls -1t "$LOGDIR"/poll-*.log 2>/dev/null | head -1)"
if [ -n "$newest_poll_log" ]; then
  p_age_hours=$(( (now_epoch - $(stat -c %Y "$newest_poll_log")) / 3600 ))
  if [ "$p_age_hours" -gt 24 ]; then
    PROBLEMS+=("Deep-summary poller: no poll-and-summarize.sh log written in the last $p_age_hours hours (expected every 5-30 min during its cron windows). Cron may not be firing at all - check \`crontab -l\` and \`systemctl status cron\`.")
  fi
else
  PROBLEMS+=("Deep-summary poller: no poll-*.log file exists at all under automation/logs/.")
fi

if [ -z "$TOKEN" ]; then
  echo "no GitHub token found; cannot report health (problems found: ${#PROBLEMS[@]})" >&2
  exit 1
fi

EXISTING="$(api "$API/issues?state=open&labels=$LABEL&per_page=1" 2>/dev/null | python3 -c 'import sys,json;d=json.load(sys.stdin);print(d[0]["number"] if d else "")' 2>/dev/null)"

if [ "${#PROBLEMS[@]}" -eq 0 ]; then
  # All clear - close the tracking issue if one is open from a prior incident.
  if [ -n "$EXISTING" ]; then
    api -X POST -d "$(jbody "All automation jobs are within their expected cadence again as of $(date -u +%Y-%m-%dT%H:%M:%SZ).")" "$API/issues/$EXISTING/comments" >/dev/null 2>&1 || true
    apiq -X PATCH -d '{"state":"closed"}' "$API/issues/$EXISTING" 2>/dev/null || true
  fi
  exit 0
fi

BODY="Automation health check found the following overdue job(s) as of $(date -u +%Y-%m-%dT%H:%M:%SZ):\n\n"
for p in "${PROBLEMS[@]}"; do BODY="${BODY}- ${p}\n"; done

if [ -n "$EXISTING" ]; then
  api -X POST -d "$(jbody "$(printf '%b' "$BODY")")" "$API/issues/$EXISTING/comments" >/dev/null 2>&1 || true
else
  PAYLOAD="$(python3 -c 'import json,sys;print(json.dumps({"title":"Automation health warning","body":sys.argv[1],"labels":["automation-health"]}))' "$(printf '%b' "$BODY")")"
  api -X POST -d "$PAYLOAD" "$API/issues" >/dev/null 2>&1 || true
fi
