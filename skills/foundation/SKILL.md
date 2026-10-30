---
name: foundation
description: Gives the project version history on GitHub and a Supabase database with access rules from the first table. Use first for any harness project.
---

# foundation

## Why
Your work is never lost, and your project can remember things.

## Choose
- Code: GitHub (default). Private repo unless the person wants it public.
- Data: Supabase (default), a hosted database with sign-in and access rules built in. Any Postgres host works if they prefer.

## Build

**Tools on the Mac**
1. Check `git --version`. If missing: `xcode-select --install`.
2. Check `gh --version`. If missing: `brew install gh` (if Homebrew is missing, use the one-line installer at brew.sh).

**GitHub**
1. **Your turn:** create a free account at github.com and turn on two-factor sign-in.
2. Run `gh auth login`. **Your turn:** finish in the browser.
3. Add `.gitignore` with `.env` in it.
4. `gh repo create <project> --private --source=. --push`

**Supabase**
1. **Your turn:** sign up at supabase.com with GitHub, create a project on the Free plan near you, and save the database password in your password manager.
2. **Your turn:** from Settings, API Keys, share the Project URL and publishable key. Both are safe to share; the secret key is not.
3. Write them to `.env` as `SUPABASE_URL` and `SUPABASE_PUBLISHABLE_KEY`, and add the names (no values) to `.env.example`.
4. Create `supabase/schema.sql`. Every table holding private data gets row level security (database rules for who sees each row). Starter:
   ```sql
   create table if not exists items (
     id uuid primary key default gen_random_uuid(),
     owner uuid not null default auth.uid(),
     body text,
     created_at timestamptz default now()
   );
   alter table items enable row level security;
   create policy "own rows read"  on items for select using (owner = auth.uid());
   create policy "own rows write" on items for insert with check (owner = auth.uid());
   ```
5. Run it in the Supabase SQL Editor (through the browser, or **Your turn:** paste and run).

## Prove
- Agent: `git log` shows a commit on GitHub; `.env` is not in the repo; a request to the table without signing in returns no rows.
- Person: sees the repo on github.com, and the `items` table in Supabase marked as protected.
