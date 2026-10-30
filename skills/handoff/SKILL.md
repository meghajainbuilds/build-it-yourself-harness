---
name: handoff
description: Keeps HARNESS.md, a setup log in the person's project, current so any agent or session can pick up without this chat. Use at the start of setup, after each block, and at the end.
---

# Handoff: a log any agent can read

Create `HARNESS.md` in the project root at the start, update it after every block, and push it to GitHub.

## Template

```markdown
# Setup log

Project: <name>
Built with: Harness for Personal Projects
Coding agent: <Claude Code or Codex>
Last updated: <date>

## Blocks
| Block | Status | Notes |
|---|---|---|
| Foundation | done / in progress / blocked | |
| Publish | | |
| Models | | |
| Always-on | | |
| Messaging | | |

## Where things live
- Code: <GitHub URL>
- Database: <Supabase project URL>
- Live site: <URL>
- Always-on: <mac or cloud host>, start/stop/log commands
- Messaging: <channel>, <sending account>

## Settings (names only, never values)
- SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY, ...

## Checks run
- <date> <what was tested> <result>

## Blocked or not yet verified
- ...

## How to back up data
- Supabase: Database, Backups, or run `pg_dump` with the connection string from the person's password manager.
```

## Rules

- Never write secret values here. This file goes to GitHub.
- Be honest in "Blocked or not yet verified." A future agent trusts this file.
- At the end of setup, read it back to the person in three lines: what works, what's left, what to try first.
