---
name: start
description: Starts a Build It Yourself build. Asks what the person wants to build, picks the blocks, shows what they'll need and what you'll ask permission for, then runs the blocks in order, beginning with GitHub. Use when someone runs /build-it:start or describes a project they want to build.
---

# start

## Why
The person sees the whole plan, what it takes, and what they'll be asked to approve before anything happens.

## 1. Ask

Open with:

> What do you want to build? A sentence or two is plenty.

Then, only if their answer leaves it unclear, ask:
- Will you use it in a browser, by text message, or both?
- Should it do things on its own, like on a schedule or when a message arrives?
- Does it use AI to write, summarize, or decide something?

Also note: Mac or other computer, and Claude Code or Codex.

## 2. Pick the blocks

| Block | Add when |
|---|---|
| `github` | Always, and always first |
| `database` | Always |
| `publish` | They use it in a browser |
| `models` | It uses AI to write, summarize, or decide |
| `always-on` | It acts on its own |
| `messaging` | They want to text it |
| `checklist`, `status` | Always |

Name the shape in plain words: a web app, a web app with AI, a texting agent, an agent with a web page, or a full assistant.

## 3. Show what they'll need

One message, tailored to the blocks you picked. Example for a web app with AI:

> **Meal-prep: a web app with AI**
>
> **What you'll need**
> - [ ] A GitHub account (free). Keeps your code and its history.
> - [ ] A Supabase account (free). Saves your recipes and menus.
> - [ ] A Netlify account (free). Puts your app on the web.
> - [ ] A Google account. Lets you sign in to your app.
> - [ ] An Anthropic API key, with a spending limit. Lets your app ask Claude for menus.
> - [ ] Your password manager open.
>
> **Time:** about 90 minutes. **Cost:** $0 for accounts, plus a few dollars a month of AI usage.
>
> **What I'll ask you to approve**
> - Signing in to GitHub, Supabase, and Netlify once each in your browser
> - Letting Netlify read this one GitHub repo
> - Creating a Google sign-in client for your app
> - Pasting your API key into a private file on your Mac
>
> **What I do on my own after you sign in**
> - Create the GitHub repo, the database, the tables, and the website
> - Connect everything and test it
>
> **What I never do without asking**
> - Spend money, send messages, delete anything, or change account settings
>
> **Defaults:** Netlify for hosting, Claude for AI. Say "ok" to keep them, or name a swap (Vercel, Cloudflare, OpenAI, Gemini, an open-source model).

Wait for their yes.

## 4. Set up and go

1. Write `harness.config.json` from `harness.config.example.json` with their choices.
2. Run `github`. It creates the repo and `CHECKLIST.md` (see `checklist`).
3. Show the tracker (see `status`) and tell them they can say "status" anytime.
4. Run the remaining blocks in order: database, publish, models, always-on, messaging. After each block, run `pause` to save progress.
5. Tell them once: "You can stop anytime by saying pause. Next session, I'll pick up where we left off."

If `CHECKLIST.md` already exists in the folder, this is a returning build: run `resume` instead.

## Prove
- Agent: `harness.config.json` lists the chosen blocks; the repo exists on GitHub with `CHECKLIST.md`.
- Person: confirmed the plan, and can see the repo on github.com.

If they're on a computer other than a Mac and want text messaging, explain that iMessage needs a Mac and offer Telegram.
