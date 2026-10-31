---
name: checklist
description: Keeps CHECKLIST.md in the person's GitHub repo, the saved record of what they need, what they approved, each block's status, where everything lives, and what was tested. Use when github creates the repo and after every block.
---

# checklist

## Why
Your setup is written down in your repo. You, or any agent later, can see what's done and where everything lives.

## Build

`github` creates `CHECKLIST.md`. Tick items as they finish, then commit and push after every block.

```markdown
# <Project> setup checklist

**What it is:** <one sentence>
**Shape:** <web app with AI, texting agent, ...>
**Built with:** Build It Yourself Harness, in <Claude Code or Codex>

## What you need
- [x] GitHub account
- [ ] Supabase account
- [ ] Netlify account
- [ ] Google account for sign-in
- [ ] Anthropic API key with a spending limit

## What you approved
- <date>: signed in to GitHub, approved repo creation
- <date>: ...

## Blocks
- [x] 1. GitHub: your code and its history
- [ ] 2. Database: where your data is saved
- [ ] 3. Publish: your app on the web, with sign-in
- [ ] 4. Models: the AI your app uses
- [ ] 5. Always-on: keeps running with the laptop closed
- [ ] 6. Messaging: text your agent

## Where everything lives
- Code: <GitHub link>
- Database: <Supabase project link>
- Live app: <address>
- Settings names (values stay in .env): SUPABASE_URL, ...
- Controls: <start, stop, status, logs>

## Tested
- <date>: <what was tested>, <passed or failed>

## Open
- <anything blocked, untested, or decided later>
```

List only the blocks this project uses, numbered in order.

## Prove
- Agent: searches `CHECKLIST.md` for `key`, `secret`, `token`, `password` and finds names only, no values; the ticks match the tracker.
- Person: at the end, hears three lines: what works, what's open, what to try first.
