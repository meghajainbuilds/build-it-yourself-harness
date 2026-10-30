---
name: status
description: Shows the person where they are in their harness build, what's done, what's happening now, and what's next. Use when they ask "where am I", "what's next", "status", or come back to a project after a break.
---

# status

## Why
Anyone, at any moment, can see where the build stands and what happens next.

## Build

1. Read `MAP.md` and `harness.config.json`. If neither exists, say the build hasn't started and offer to run `start`.
2. Show the tracker exactly in this format:

```
Meal-prep  |  Web app with AI

  done   1. Foundation   your code and data have a home
  NOW    2. Publish      putting it on the web
  next   3. Models       choosing the AI that writes menus

Right now:  Netlify is connected. Next, Google sign-in.
Your turn:  nothing yet. I'll tell you when.
Time left:  about 30 minutes
```

3. Below it, list anything in MAP.md's "Open" section in one line each.
4. Ask one question: continue now, or stop here.

## Prove
- Agent: the tracker matches MAP.md's checkboxes.
- Person: can say what's next without asking.
