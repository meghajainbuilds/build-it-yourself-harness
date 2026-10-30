---
name: models
description: Sets which AI does the thinking, both the agent behind always-on and messaging (Claude Code, Codex, or any command) and the model the app calls. Use when the project runs an agent or calls an AI.
---

# models

## Why
You're never locked into one AI company. Swap with one setting.

## Choose

**The agent** that answers messages and runs schedules. Set `models.agent_command`:

| Value | Runs | Needs |
|---|---|---|
| `claude` (default) | `claude -p "<message>"` | Claude Code installed and signed in |
| `codex` | `codex exec "<message>"` | Codex CLI installed and signed in |
| your own command | message passed as the last argument | prints the reply |

**The model inside the app**, if the app calls an AI directly: set `AI_PROVIDER` and `AI_MODEL`.

## Build
1. Confirm the agent command exists (`which claude` or `which codex`). If not, **Your turn:** install it and sign in.
2. If the app calls an AI, create one file, `lib/ai`, with one `ask(prompt)` function that reads `AI_PROVIDER`. Nothing else in the app talks to a provider directly.
3. Add `AI_PROVIDER`, `AI_MODEL`, and the key names to `.env.example`.
4. **Your turn:** create the API key on the provider's site, paste it into `.env`, and set a monthly spending cap there.

## Prove
- Agent: the agent command replies to "Say ok"; `ask("Say ok")` returns ok.
- Person: changes `AI_PROVIDER` and sees it still answers.
