# Build It Yourself Harness

**The focus is on your idea. The harness takes care of the setup.**

Every project runs on a few core accounts: GitHub keeps your code, a database saves your data, a host puts it on the web, and an AI model does the thinking. The harness explains each one, helps you choose what fits your comfort level, and sets them up for you through their command line tools and APIs.

Works in Claude Code and OpenAI Codex, with any AI model.

---

## What the harness does for you

- **Creates your project on GitHub first**, so your work is saved from the start
- **Sets up each account for you** through its command line or API, after you sign in once
- **Recommends a default at every step** and names the other options, so you choose quickly
- **Writes and tests the code**, and proves each step works before moving on
- **Shows a tracker** of where you are, and **saves a checklist** in your repo
- **Remembers between sessions**, so each session picks up where the last one stopped

## What you do

- Sign in to each account and enter verification codes
- Approve access, like letting Netlify read your GitHub repo
- Handle billing and set spending limits
- Decide what to build

## The core accounts

| Account | What it does | Default | Other options |
|---|---|---|---|
| **GitHub** | Keeps your code and every change | Private repo | Public repo |
| **Database** | Saves your data and controls who sees it | Supabase | Neon, any Postgres |
| **Host** | Puts your app on the web | Netlify | Vercel, Cloudflare |
| **Sign-in** | Lets people log in to your app | Google | Email link, GitHub |
| **AI model** | The thinking inside your app | Claude | GPT, Gemini, an open-source model on your Mac |
| **Always-on** | Keeps your agent running with the laptop closed | Your Mac | A cloud server |
| **Messaging** | Lets you text your agent | iMessage | Telegram, SMS |

You set up only the accounts your project needs.

## Walk through it

Here is the path, using Meal-prep (a web app where AI plans the weekly menu and saves a recipe box) as the example.

**1. Install the harness.** In Claude Code:
```
/plugin marketplace add YOUR_GITHUB/build-it-yourself-harness
/plugin install build-it@build-it-yourself-harness
```

**2. Start.** Make a folder and open Claude Code there:
```
mkdir -p ~/Projects/meal-prep && cd ~/Projects/meal-prep
claude
```
Then type:
```
/build-it:start
```

**3. Describe your idea.** The harness asks one question: *What do you want to build?* You answer in your own words.

**4. See the plan.** You get a list of the accounts you'll need, the time it takes, the cost, what you'll be asked to approve, and the defaults. You say "ok" or swap anything.

**5. Your project goes on GitHub.** The harness creates the repo and a `CHECKLIST.md` inside it.

**6. Sign in once per account.** The harness creates the database, the tables, the website, and the connections between them. It pauses only when it needs you.

**7. Follow the tracker.**
```
Meal-prep  |  a web app with AI

  done   1. GitHub      your code and its history
  done   2. Database    where your recipes and menus are saved
  NOW    3. Publish     your app on the web, with sign-in
  next   4. Models      the AI that writes your menus
```
Say **status** anytime to see it.

**8. Pause anytime.** Say **pause**. The harness saves `SESSION-NOTES.md` with what's done, what's in progress, your decisions, and the next step, then commits it to GitHub.

**9. Pick up where you left off.** Open Claude Code in the project folder, on any computer. The harness loads your notes automatically and opens with:
```
Last time:  finished the Database; Netlify site created.
Next:       Google sign-in, about 5 minutes.
Ready to continue?
```

**10. Your app is live.** Every step has been tested, and the checklist in your repo records what was set up and where it lives.

## Shapes

| You're building | Blocks |
|---|---|
| A web app | GitHub, Database, Publish |
| A web app with AI | GitHub, Database, Publish, Models |
| A texting agent | GitHub, Database, Models, Always-on, Messaging |
| An agent with a web page | GitHub, Database, Publish, Models, Always-on |
| A full assistant | All of them |

## What it costs

| Item | Cost |
|---|---|
| AI coding plan (Claude Pro, or Claude Max for heavy building) | $20, or $100 to $200 a month |
| GitHub, Supabase, Netlify | $0 on free plans |
| AI usage inside your app | a few dollars a month for personal use, with a limit you set |
| When you outgrow free plans | Netlify Personal about $9, Supabase Pro $25 a month |
| Always-on in the cloud (optional) | about $5 to $20 a month |
| Your own domain name (optional) | about $10 to $20 a year |

Most personal projects run on the coding plan plus a few dollars of AI usage. Prices as of October 2026; check each provider's pricing page.

## Requirements

- A Mac for iMessage and the always-on Mac setup; other blocks work on any computer
- Claude Code or Codex, signed in
- A Google account
- A password manager

## Using Codex

```
npx skills add YOUR_GITHUB/build-it-yourself-harness
```
Open your project folder in Codex and say: *Start the build-it harness.* `AGENTS.md` gives Codex the same instructions Claude Code uses.

## Ground rules

1. Secret values live in `.env` on your computer or in each provider's settings. They stay out of chat and out of GitHub.
2. Private data is protected by rules inside the database.
3. Messaging answers only the people you approve.
4. Anything that sends, deletes, or spends asks you first.

## Acknowledgments

Thanks to Rose Yao, whose guide [Set Up Once. Start Building.](https://roseyao.com/agents/get-started) showed how much setup a coding agent can carry for a beginner, and sparked the idea for this harness.

## License

MIT
