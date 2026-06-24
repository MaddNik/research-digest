#!/usr/bin/env bash
# Publish new/updated summaries from /home/nik/research-material into the site
# and push. Safe to run repeatedly (commits only when summaries changed).
# Wired to run automatically via a Claude Code Stop hook.
set -uo pipefail

export HOME=/home/nik
export PATH="/home/nik/.npm-global/bin:/usr/local/bin:/usr/bin:/bin"

REPO="/home/nik/research-digest"
cd "$REPO" || exit 0
[ -d /home/nik/research-material ] || exit 0

python3 "$REPO/automation/publish-summaries.py" || exit 0

git add summaries _data/summaries.yml 2>/dev/null
if ! git diff --cached --quiet 2>/dev/null; then
  git pull --rebase --autostash -q origin main 2>/dev/null || true
  git commit -q -m "Publish summaries, $(date +%Y-%m-%d)"
  git push -q origin main 2>/dev/null || true
fi
