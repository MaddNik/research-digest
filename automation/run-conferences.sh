#!/usr/bin/env bash
# Monthly conferences updater - invoked by cron once a month.
# Runs a custom OpenRouter tool-calling harness (automation/openrouter_agent.py)
# to research upcoming semiconductor/photonics conferences and refresh
# _data/conferences.yml. Billed per-token via ~/.openrouter_api_key.
set -uo pipefail

export HOME=/home/nik
export PATH="/home/nik/.local/bin:/home/nik/.npm-global/bin:/usr/local/bin:/usr/bin:/bin"

REPO="/home/nik/research-digest"
LOGDIR="$REPO/automation/logs"
LOCK="$REPO/automation/.run-conferences.lock"
mkdir -p "$LOGDIR"
TS="$(date +%Y-%m-%d_%H%M%S)"
LOG="$LOGDIR/conferences-$TS.log"

cd "$REPO" || { echo "repo not found" >&2; exit 1; }

# --- single-instance lock (skip if another conferences run is still in progress) ---
exec 9>"$LOCK"
if ! flock -n 9; then
  echo "$(date): another run-conferences.sh is still running; exiting" >>"$LOG"
  exit 0
fi

{
  echo "=== Conferences update $TS ==="

  if ! command -v python3 >/dev/null 2>&1; then
    echo "FATAL: python3 not found in PATH ($PATH)"
    exit 127
  fi
  if [ ! -s "$HOME/.openrouter_api_key" ]; then
    echo "FATAL: $HOME/.openrouter_api_key is missing or empty"
    exit 127
  fi
  export OPENROUTER_API_KEY="$(cat "$HOME/.openrouter_api_key")"

  git pull --rebase --autostash 2>&1 || echo "(pull failed, continuing)"

  python3 "$REPO/automation/openrouter_agent.py" \
    --prompt-file "$REPO/automation/conferences-prompt.md" \
    --model "${OPENROUTER_MODEL:-anthropic/claude-sonnet-5}" \
    --max-cost-usd "${OPENROUTER_MAX_COST_CONFERENCES:-8}"
  # Rollback fallback (kept for one cycle, then delete): the previous
  # subscription-based invocation via Claude Code's CLI.
  # claude -p "$(cat "$REPO/automation/conferences-prompt.md")" \
  #   --model sonnet --dangerously-skip-permissions --output-format text

  echo "=== exit code: $? ==="
  echo "=== latest commit ==="
  git log -1 --oneline 2>&1
} >"$LOG" 2>&1

# Keep only the 12 most recent conference logs
ls -1t "$LOGDIR"/conferences-*.log 2>/dev/null | tail -n +13 | xargs -r rm -f
