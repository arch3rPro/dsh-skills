#!/usr/bin/env bash
# Symlink every skill into the local harness skill directories so a git pull
# keeps installed skills current. Re-run after adding, removing, or renaming a skill.
# Portable: works with macOS bash 3.2 + BSD find (no mapfile, no find -printf).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGETS=( "$HOME/.claude/skills" "$HOME/.agents/skills" )

# Collect the directory of every SKILL.md (the -name filter already scopes to skill dirs).
SKILL_DIRS=()
while IFS= read -r f; do
  [ -n "$f" ] && SKILL_DIRS+=( "$(dirname "$f")" )
done < <(find "$ROOT/skills" -name SKILL.md -type f)

for dir in "${SKILL_DIRS[@]}"; do
  name="$(basename "$dir")"
  for target in "${TARGETS[@]}"; do
    [ -d "$target" ] || mkdir -p "$target"
    ln -sfn "$dir" "$target/$name"
    echo "linked $target/$name"
  done
done
