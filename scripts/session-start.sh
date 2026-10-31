#!/bin/bash
# Build It Yourself Harness: loads where the build left off when a session opens.
# Prints nothing for folders that aren't harness projects.

DIR="${CLAUDE_PROJECT_DIR:-$PWD}"
cd "$DIR" 2>/dev/null || exit 0

[ -f CHECKLIST.md ] || exit 0

echo "This folder is a Build It Yourself Harness project. Context from earlier sessions is below."
echo "Open by following the resume block: show the tracker, then one line on where we left off and what's next, then ask if the person is ready to continue."
echo

if [ -f SESSION-NOTES.md ]; then
  echo "===== SESSION-NOTES.md ====="
  head -n 120 SESSION-NOTES.md
  echo
fi

echo "===== CHECKLIST.md ====="
head -n 150 CHECKLIST.md

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo
  echo "===== Recent commits ====="
  git log --oneline -n 8 2>/dev/null
  CHANGES=$(git status --porcelain 2>/dev/null | head -n 20)
  if [ -n "$CHANGES" ]; then
    echo
    echo "===== Uncommitted changes (work in progress from last session) ====="
    echo "$CHANGES"
  fi
fi

exit 0
