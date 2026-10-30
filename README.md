# Harness for Personal Projects

Pick what you're building. Your coding agent sets up only the parts you need.

Works in **Claude Code** and **OpenAI Codex**. Use any model.

---

## Why this exists

Most people with an idea stall on setup, not on the idea. Accounts, hosting, sign-in, keeping something running, getting it to text you back.

This harness turns that setup into building blocks. You tell your agent what you want to make. It proposes the blocks, you confirm, and it walks you through each one. You handle sign-ins and billing. The agent handles the rest.

Inspired by Rose Yao's [Set Up Once. Start Building.](https://roseyao.com/agents/get-started) guide. This harness takes the same idea and makes it modular, so it fits any project, including agents that stay on and message you.

## The blocks

| Block | What it gives you | Default | Swap for |
|---|---|---|---|
| **Foundation** | A home for code and saved data | GitHub + Supabase | Any Postgres host |
| **Publish** | Your app at a web address, with sign-in | Netlify + Google sign-in | Vercel, Cloudflare |
| **Always-on** | An agent that keeps running when your laptop lid is closed | A Mac that stays awake | A cloud server |
| **Messaging** | Text your agent, and it texts you back | iMessage | Telegram, SMS |
| **Models** | Choose which AI does the thinking | Claude | OpenAI, Gemini, others |
| **Handoff** | A setup log so any agent can pick up where you left off | Always on | |

## Recipes

Recipes are blocks bundled for common projects.

| You want to build | Blocks |
|---|---|
| A web app | Foundation + Publish |
| An always-on agent you text | Foundation + Always-on + Messaging |
| An always-on agent with a web dashboard | Foundation + Always-on + Publish |
| A personal assistant | Foundation + Always-on + Messaging + Publish |

## Install

**Claude Code**

```
/plugin marketplace add YOUR_GITHUB/personal-projects-harness
/plugin install personal-projects-harness
```

**Codex, or any agent that reads Agent Skills**

```
npx skills add YOUR_GITHUB/personal-projects-harness
```

Or clone the repo and open it in your agent. `AGENTS.md` tells it what to do.

## Start

Open an empty project folder in your agent and say:

> Use the harness. I want to build: [your idea].

The `start` skill asks a few questions, picks your blocks, and runs them in order. Each step tells you what you do, what the agent takes over, and how to check it worked.

## Budget

| Item | Monthly cost |
|---|---|
| AI coding plan (Claude or ChatGPT) | about $20 to $100 |
| GitHub, Supabase, Netlify free plans | $0 |
| Always-on on a Mac you already own | $0 |
| Always-on on a cloud server | about $5 to $20 |

Check each provider's pricing page. Prices change.

## Safety defaults

- Secrets never go in chat or in GitHub. They live in a local `.env` file or the provider's settings.
- Private data is protected in the database, not just hidden in the app.
- The iMessage bridge only answers phone numbers or emails you approve.
- The agent never sends a message, deletes data, or spends money without asking you first.

## Requirements

- A laptop (the iMessage block needs a Mac)
- A Claude or ChatGPT plan with a coding agent
- A Google account and a password manager

## License

MIT
