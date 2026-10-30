---
name: start
description: Entry point for the harness. Learns what the person is building, matches it to a shape, picks the blocks, and runs them in order. Use when someone says "use the harness" or describes a project they want to build.
---

# start

## Why
So the person builds only what their project needs.

## Choose

Ask in one message:
1. What are you building, in a sentence or two?
2. Where will you use it: in a browser, by text, or both?
3. Does it need to do things on its own, like on a schedule or when a message arrives?

Then match a shape:

| Signals | Shape | Blocks |
|---|---|---|
| Browser only, nothing on its own | Web app | foundation, publish |
| By text, acts on its own | Texting agent | foundation, models, always-on, messaging |
| Browser, acts on its own | Agent with a dashboard | foundation, models, always-on, publish |
| Both | Full assistant | all |

`map` is always included. Add `models` to any shape where the app writes, summarizes, or decides with AI (for example, "AI makes my weekly menu").

## Build

1. Say back the shape and blocks in plain words with a rough time for each, and the defaults (Netlify, iMessage, Claude). Offer swaps.
2. **Your turn:** confirm or change.
3. Write `harness.config.json` from `harness.config.example.json`.
4. Start `MAP.md` (see `map`).
5. Show the tracker (see `status`) so the person sees the whole road before the first step. Tell them they can say "status" anytime.
6. Run blocks in order: foundation, publish, models, always-on, messaging. Show the tracker as each block starts and as its Prove passes.

## Prove
- Agent: `harness.config.json` and `MAP.md` exist and list the chosen blocks.
- Person: hears the plan back and agrees.

If they're not on a Mac and want iMessage, explain iMessage needs a Mac and offer Telegram.
