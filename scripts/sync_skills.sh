#!/usr/bin/env bash
# Mirror the canonical skills (.agents/skills, read by Codex) to .claude/skills (read by Claude Code).
# Edit skills only under .agents/skills, then run this script and commit both copies.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf .claude/skills
mkdir -p .claude
cp -R .agents/skills .claude/skills
echo "Synced .agents/skills -> .claude/skills"
