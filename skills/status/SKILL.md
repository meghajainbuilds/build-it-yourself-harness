---
name: status
description: Shows the tracker, where the build stands, what's happening now, and what's next, read from CHECKLIST.md. Use when the person says "status", "where am I", "what's next", or returns after a break, and at each block change during a build.
---

# status

## Why
You always know where you are on the road from idea to working project.

## Build

1. Read `CHECKLIST.md` and `harness.config.json`. If neither exists, say the build hasn't begun and offer `/build-it:start`.
2. Show the tracker in this format, one line per block this project uses, with what each block is:

```
Meal-prep  |  a web app with AI

  done   1. GitHub      your code and its history
  done   2. Database    where your recipes and menus are saved
  NOW    3. Publish     your app on the web, with sign-in
  next   4. Models      the AI that writes your menus

Right now:  Netlify is connected. Next, Google sign-in.
Your turn:  nothing yet. I'll tell you when.
```

3. List any "Open" items from `CHECKLIST.md`, one line each.
4. Ask: keep going, or stop here?

## Prove
- Agent: the tracker matches the ticks in `CHECKLIST.md`.
- Person: can say what's next without asking.
