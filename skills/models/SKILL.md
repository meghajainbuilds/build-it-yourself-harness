---
name: models
description: Chooses and connects the AI for the project, both the model the app calls (Claude by default, or OpenAI, Gemini, or an open-source model) and the coding agent that runs always-on work (Claude Code or Codex). Use when the project uses AI.
---

# models

## Why
Your project can think: write a menu, summarize, decide. You can switch to another AI later by changing one setting.

## Choose

**The model your app calls**

> **Default: Claude** (Anthropic). Say "ok" to keep it.
> **Other options:** GPT (OpenAI), Gemini (Google), or an open-source model like Llama that runs free on your own Mac through Ollama.

**The agent that runs on its own** (only with `always-on`)

> **Default: Claude Code.** Say "ok" to keep it.
> **Other options:** Codex (OpenAI), or any command you choose.

## Build

**App model.**
1. Create one file, `lib/ai` (in the app's language), with a single `ask(prompt)` function. It reads `AI_PROVIDER` and `AI_MODEL` and calls that provider. Every AI call in the app goes through it.
2. Add `AI_PROVIDER`, `AI_MODEL`, and the matching key name to `.env.example`.
3. Keys come from the provider's site, where the person's billing lives:
   - **Your turn:** create an API key at console.anthropic.com (or platform.openai.com, or aistudio.google.com) and set a monthly spending limit there.
   - **Your turn:** paste the key into `.env`. You read it from there.
   - Open-source path: `brew install ollama`, `ollama pull llama3.2`, set `AI_PROVIDER=ollama`. No key, no cost.
4. If the app calls the AI from the server, set the key on the host yourself (`netlify env:set ANTHROPIC_API_KEY ...` read from `.env`). Keep it out of browser code.

**Agent command.** Write `models.agent_command` in `harness.config.json`: `claude` runs `claude -p "<message>"`, `codex` runs `codex exec "<message>"`. Check it with `which`, and if missing, **Your turn:** install it and sign in.

## Prove
- Agent: `ask("Reply with OK")` returns OK; the agent command answers "Say hello in three words."
- Person: uses the app's AI feature once and sees a real answer.
