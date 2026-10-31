---
name: resume
description: Continues a build from an earlier session. Reads SESSION-NOTES.md, CHECKLIST.md, and recent commits, shows the tracker and where things left off, and picks up at the exact step. Use when a session opens in a harness project, when the person says "continue" or "where were we", or runs /build-it:resume.
---

# resume

## Why
Each session starts with the full picture, so you spend your time building.

## Build

1. Read `SESSION-NOTES.md`, `CHECKLIST.md`, and `harness.config.json`. In Claude Code, the plugin loads these automatically when the session opens. In Codex or any other agent, read them yourself first.
2. Check for uncommitted changes (`git status`). If there are any, they're work from the last session; mention them in one line.
3. Run `git pull` so the folder matches GitHub, in case the person worked on another computer.
4. Show the tracker (see `status`), then:

```
Last time:  finished the Database; Netlify site created.
Next:       Google sign-in client, about 5 minutes, needs your Google login.
Open:       How many meals per week should the menu plan?

Ready to continue?
```

5. On their yes, continue from the exact step in "In progress."
6. If the notes and the checklist disagree, trust what you can verify (the live site, the database, GitHub), fix the notes, and say what you corrected.

## Prove
- Agent: the next step named matches "Next step" in the notes.
- Person: recognizes where they left off without re-explaining.
