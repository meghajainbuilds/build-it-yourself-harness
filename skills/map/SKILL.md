---
name: map
description: Keeps MAP.md, a living map of the project, so any agent or session can pick up cold. Use at the start, after every block, and whenever something changes.
---

# map

## Why
The next agent, in Claude Code, Codex, or a fresh chat, knows exactly where everything is.

## Build

Create `MAP.md` at the project root. Update it after every block and push it.

```markdown
# Project map: <name>

**What it is:** <one sentence>
**Shape:** <web app / texting agent / agent with a dashboard / full assistant>
**Agent:** <claude or codex>   **Updated:** <date>

## Blocks
- [x] foundation: <GitHub URL>, <Supabase project URL>
- [ ] publish: <host>, <live URL>
- [ ] models: agent <command>, app <provider and model>
- [ ] always-on: <mac or cloud>
- [ ] messaging: <channel>, <sending account>, <N> approved senders

## Controls
- Start / stop / status / logs: <commands>

## Settings (names only)
- SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY, ...

## Proven
- <date>: <what was tested>, <passed or failed>

## Open
- <anything blocked, untested, or decided later>
```

## Prove
- Agent: no secret values appear in `MAP.md` (search for `key`, `secret`, `token`, `password` and confirm only names).
- Person: at the end, reads three lines back from you: what works, what's open, what to try first.
