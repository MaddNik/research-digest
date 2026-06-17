#!/usr/bin/env bash
# Monthly conferences updater - invoked by cron once a month.
# Runs the headless Claude CLI to research upcoming semiconductor/photonics
# conferences and refresh _data/conferences.yml.
set -uo pipefail

export HOME=/home/nik
export PATH="/home/nik/.npm-global/bin:/usr/local/bin:/usr/bin:/bin"

REPO="/home/nik/research-digest"
LOGDIR="$REPO/automation/logs"
mkdir -p "$LOGDIR"
TS="$(date +%Y-%m-%d_%H%M%S)"
LOG="$LOGDIR/conferences-$TS.log"

cd "$REPO" || { echo "repo not found" >&2; exit 1; }

{
  echo "=== Conferences update $TS ==="
  git pull --rebase --autostash 2>&1 || echo "(pull failed, continuing)"

  claude -p "$(cat "$REPO/automation/conferences-prompt.md")" \
    --dangerously-skip-permissions \
    --output-format text

  echo "=== exit code: $? ==="
  echo "=== latest commit ==="
  git log -1 --oneline 2>&1
} >"$LOG" 2>&1

# Keep only the 12 most recent conference logs
ls -1t "$LOGDIR"/conferences-*.log 2>/dev/null | tail -n +13 | xargs -r rm -f
