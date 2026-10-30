---
name: foundation
description: Sets up a GitHub repository for the code and a Supabase database for saved data, with access rules from day one. Use as the first block for any harness project.
---

# Foundation: a home for code and data

**Result:** a private GitHub repo with the project, and a Supabase project the app can save to.

## GitHub

**Person does:** signs up at github.com/signup, picks Free, turns on two-factor sign-in, saves recovery codes.

**Agent does:**
1. Check `git` is installed (`git --version`). On a Mac, if missing, run `xcode-select --install`.
2. Check the GitHub CLI (`gh --version`). If missing on a Mac: `brew install gh`. If Homebrew is missing, give the install line from brew.sh.
3. Run `gh auth login` and let the person finish in the browser.
4. Create the repo: `gh repo create <project> --private --source=. --push`.
5. Add `.gitignore` with `.env` in it before the first commit.

**Check:** the person opens the repo URL and sees the files.

## Supabase

Supabase is a hosted database that also handles sign-in and access rules.

**Person does:** signs up at supabase.com with GitHub, picks Free, creates a project, generates a database password and saves it in their password manager, picks the closest region.

**Agent does:**
1. Ask for the Project URL and publishable key (Settings, then API Keys). These are safe in app code.
2. Write them to `.env`:
   ```
   SUPABASE_URL=...
   SUPABASE_PUBLISHABLE_KEY=...
   ```
3. Never ask for the database password or secret key in chat. If a secret is needed later, the person pastes it into `.env` themselves.
4. Create `supabase/schema.sql` with the first table. Every table with private data gets row level security (rules in the database that decide who can read or change each row):
   ```sql
   create table if not exists notes (
     id uuid primary key default gen_random_uuid(),
     owner uuid not null default auth.uid(),
     body text,
     created_at timestamptz default now()
   );
   alter table notes enable row level security;
   create policy "owner reads" on notes for select using (owner = auth.uid());
   create policy "owner writes" on notes for insert with check (owner = auth.uid());
   ```
5. Have the person paste it into the Supabase SQL Editor and run it, or run it through the browser if you have one.

**Check:** the `notes` table appears in Supabase's Table Editor with a lock icon showing access rules are on.

## Update HARNESS.md

Add the repo URL, Supabase project URL, and variable names (never values).
