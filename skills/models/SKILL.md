---
name: models
description: Lets the person choose which AI does the thinking, both the coding agent that runs the always-on loop (Claude Code or Codex) and the model called from inside the app. Use when the project calls an AI or runs an agent.
---

# Models: choose your AI

There are two separate choices. Explain both in one short message.

## 1. The agent that runs your always-on loop

This is what the iMessage bridge calls when a text arrives. Set `models.agent_command` in `harness.config.json`.

| Value | What runs | Needs |
|---|---|---|
| `claude` | `claude -p "<message>"` | Claude Code installed and signed in |
| `codex` | `codex exec "<message>"` | Codex CLI installed and signed in |
| anything else | your own command; the message is passed as the last argument | your command prints the reply |

Check it works: run the command once with "Say hello in five words" and confirm it prints a reply.

## 2. The model inside your app

If the app calls an AI directly (for example, a summary button), keep the provider in one place so it's easy to swap.

**Agent does:**
1. Add to `.env.example` (no values):
   ```
   AI_PROVIDER=anthropic
   AI_MODEL=
   ANTHROPIC_API_KEY=
   OPENAI_API_KEY=
   ```
2. Create one file, `lib/ai.(js|ts|py)`, with a single `ask(prompt)` function that reads `AI_PROVIDER` and calls the right provider. Nothing else in the app calls a provider directly.
3. Optional: if they want many models behind one key, suggest a router service like OpenRouter. Mention it once.

**Person does:** creates the API key on the provider's site and pastes it into `.env` themselves. Sets a monthly spending limit there.

**Check:** run `ask("Reply with OK")` and see "OK".

## Update HARNESS.md

Record the agent command, app provider, and model name. No keys.
