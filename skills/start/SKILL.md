---
name: start
description: Begin here. Asks what the person wants to build, picks the harness blocks they need (foundation, publish, always-on, messaging, models), confirms, and runs them in order. Use when someone says "use the harness", "set up my project", or describes an idea they want to build.
---

# Start: pick the blocks

## 1. Ask three questions (one message)

1. What do you want to build? One or two sentences is enough.
2. Should it keep running when your laptop is closed, like sending you a morning summary or answering texts?
3. How do you want to use it: a web page, text messages, or both?

Also note which coding agent they're in (Claude Code or Codex) and whether they're on a Mac.

## 2. Pick the blocks

| If they said | Add |
|---|---|
| Anything | `foundation`, `handoff` |
| Web page, dashboard, sign-in, or other people using it | `publish` |
| Keep running, scheduled, "every morning", "watch for" | `always-on` |
| Text it, it texts me | `messaging` |
| It calls an AI inside the app | `models` |

Common recipes:
- Web app: foundation, publish
- Always-on agent you text: foundation, always-on, messaging, models
- Always-on agent with web: foundation, always-on, publish, models

## 3. Confirm in plain words

Example:

> You're building a texting assistant that checks your calendar each morning. You'll need:
> 1. **Foundation**: a home for your code and saved data (about 20 minutes)
> 2. **Always-on**: keeps it running on your Mac (about 15 minutes)
> 3. **Messaging**: iMessage, so you text it like a person (about 20 minutes)
> 4. **Models**: picks which AI does the thinking (about 5 minutes)
>
> Sound right? Want to swap anything (Vercel instead of Netlify, Telegram instead of iMessage)?

Wait for a yes.

## 4. Save choices and run

1. Copy `harness.config.example.json` to the project as `harness.config.json` and fill in their choices.
2. Create `HARNESS.md` using `skills/handoff`.
3. Run each block's skill in this order: foundation, publish, models, always-on, messaging, handoff.
4. After each block, show its check and confirm it passed before moving on.

## Rules

- Don't add blocks they didn't ask for. Mention optional ones once at the end.
- If they're not on a Mac and chose iMessage, explain that iMessage needs a Mac and offer Telegram.
