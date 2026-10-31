---
name: pause
description: Saves where the build stands so the next session continues smoothly. Writes SESSION-NOTES.md, updates CHECKLIST.md, and commits both to GitHub. Use when the person says "pause", "stop here", "that's it for today", or runs /build-it:pause, and after every block finishes.
---

# pause

## Why
You can stop anytime. Next session, your agent picks up exactly where you left off, on any computer.

## Build

1. Update `SESSION-NOTES.md` at the project root. Keep the top section current and add one line to the history:

```markdown
# Where we left off

**Updated:** <date and time>
**Last finished:** Database. Recipes and menus tables are live with access rules.
**In progress:** Publish. Netlify site created and connected to GitHub; Google sign-in is next.
**Next step:** Create the Google sign-in client (about 5 minutes, needs your Google login).

## Decisions
- Hosting: Netlify (default kept)
- AI: Claude, model claude-sonnet-5-5
- Prep sessions only for now; house manager access later

## Open questions
- How many meals per week should the menu plan?

## What you said you want next
- Ingredient list grouped by store section

## History
- <date>: GitHub and Database done
- <date>: Publish started
```

   Record decisions with a short reason when one was given. Record the exact point inside a step, so the next session starts there. Keep secret values out.
2. Tick finished items in `CHECKLIST.md`.
3. Commit and push:
   ```
   git add -A && git commit -m "Pause: <one-line summary>" && git push
   ```
4. Tell the person in three lines: what's done, what's next, and how to continue ("Open Claude Code in this folder. I'll pick up from here.").

## Prove
- Agent: `git status` is clean and the latest commit is on GitHub.
- Person: reads the three lines and knows where things stand.
