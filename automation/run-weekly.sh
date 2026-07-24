#!/usr/bin/env bash
# Weekly Frontier Digest runner - invoked by cron every Friday.
# Runs the headless Claude Code CLI to research, verify, and publish the digest.
set -uo pipefail

export HOME=/home/nik
export PATH="/home/nik/.local/bin:/home/nik/.npm-global/bin:/usr/local/bin:/usr/bin:/bin"

REPO="/home/nik/research-digest"
LOGDIR="$REPO/automation/logs"
mkdir -p "$LOGDIR"
TS="$(date +%Y-%m-%d_%H%M%S)"
LOG="$LOGDIR/run-$TS.log"

cd "$REPO" || { echo "repo not found" >&2; exit 1; }

{
  echo "=== Frontier Digest run $TS ==="
  git pull --rebase --autostash 2>&1 || echo "(pull failed, continuing)"

  claude -p "$(cat "$REPO/automation/local-run-prompt.md")" \
    --model sonnet \
    --dangerously-skip-permissions \
    --output-format text

  echo "=== exit code: $? ==="
  echo "=== latest commit ==="
  git log -1 --oneline 2>&1
} >"$LOG" 2>&1

# Keep only the 12 most recent logs
ls -1t "$LOGDIR"/run-*.log 2>/dev/null | tail -n +13 | xargs -r rm -f
