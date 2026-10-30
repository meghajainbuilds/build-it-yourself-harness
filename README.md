# Harness for Personal Projects

Tell your coding agent what you're building. The harness gives it the right parts, in the right order, and proves each one works before moving on.

Runs in **Claude Code** and **OpenAI Codex**. Any model.

---

## The idea

A harness is everything around the idea: where the code lives, where data is saved, how people reach it, how it keeps running, how it talks to you. It's the same handful of parts every time, and it's where most personal projects stall.

This repo packages those parts as **blocks**. Your agent picks the blocks your project needs, builds them with you, and proves each one works. You only step in for the things an agent shouldn't do alone: signing in, approving access, paying.

## Blocks

| Block | Gives your project | Default | Also supports |
|---|---|---|---|
| `foundation` | Version history and a database | GitHub + Supabase | Any Postgres |
| `publish` | A web address and sign-in | Netlify + Google | Vercel, Cloudflare |
| `models` | Your choice of AI | Claude | Codex, OpenAI, Gemini, others |
| `always-on` | Keeps running with your laptop closed | A Mac that stays awake | A cloud server |
| `messaging` | Text it, it texts back | iMessage | Telegram |
| `map` | A living map of your project for the next agent | Always included | |

## Shapes

Most projects are one of these shapes. The `start` block recognizes them.

| Shape | Blocks |
|---|---|
| **Web app** | foundation, publish |
| **Texting agent** | foundation, models, always-on, messaging |
| **Agent with a dashboard** | foundation, models, always-on, publish |
| **Full assistant** | all of them |

## Install

**Claude Code**
```
/plugin marketplace add YOUR_GITHUB/personal-projects-harness
/plugin install personal-projects-harness
```

**Codex and other agents**
```
npx skills add YOUR_GITHUB/personal-projects-harness
```

## Use

In an empty folder, tell your agent:

```
Use the harness. I'm building [your idea].
```

## How every block works

| Part | What happens |
|---|---|
| **Why** | One line on what this block adds |
| **Choose** | Options, with a default, so you can swap pieces |
| **Build** | The agent does the work and stops at **Your turn** for anything only you should do |
| **Prove** | A test the agent runs and one you can see yourself. No block is done until both pass. |

## Ground rules

1. Secrets live in `.env` or a provider's settings page. Never in chat, never in GitHub.
2. Private data is locked in the database itself, not just hidden on screen.
3. Messaging answers only people you approve.
4. Anything that sends, deletes, or spends asks you first.

## What it costs

Free tiers cover the starting setup. Plan on your AI coding subscription, plus about $5 to $20 a month if you run always-on in the cloud instead of on a Mac. Check provider pricing pages; prices change.

## License

MIT
