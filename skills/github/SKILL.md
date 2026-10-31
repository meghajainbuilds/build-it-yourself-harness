---
name: github
description: First block of every build. Creates the person's project as its own GitHub repository, with history, a safe .gitignore, and CHECKLIST.md. Use right after start confirms the plan.
---

# github

## Why
Your project lives on GitHub from minute one. Every change is saved, and any agent can pick it up later.

## Choose

> **Default: a private GitHub repo.** Say "ok" to keep it.
> **Other options:** a public repo, if you want to share the code.

## Build

**Tools on the Mac.** Check each, install what's missing:
- `git --version`. Missing: `xcode-select --install`.
- `brew --version`. Missing: give the one-line installer from brew.sh and wait.
- `gh --version`. Missing: `brew install gh`.

**Account.** Run `gh auth status`. If signed out:
1. **Your turn:** create a free account at github.com/signup if you have none, and turn on two-factor sign-in.
2. Run `gh auth login --web`. **Your turn:** enter the code shown and approve in the browser.

**Repo.** From the project folder:
```
mkdir -p ~/Projects/<project> && cd ~/Projects/<project>
git init -b main
```
Write `.gitignore` (`.env`, `.env.*`, `!.env.example`, `node_modules/`, `.DS_Store`, `logs/`, `bridge/config.json`, `bridge/state.json`).
Create `CHECKLIST.md` (see `checklist`) and a one-paragraph `README.md` about their idea.
```
git add -A && git commit -m "Start <project>"
gh repo create <project> --private --source=. --push
```

## Prove
- Agent: `gh repo view` returns the repo; `git status` is clean; `.env` is absent from the repo.
- Person: opens the repo link and sees README and CHECKLIST.
