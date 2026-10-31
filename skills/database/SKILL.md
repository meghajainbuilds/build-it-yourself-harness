---
name: database
description: Gives the project a Supabase database, created and configured by the agent through the Supabase command line after one sign-in, with access rules on every private table. Use after github in every build.
---

# database

## Why
Your project remembers things, on any device, and only the right people see them.

## Choose

> **Default: Supabase** (free plan). A hosted database with sign-in and access rules built in. Say "ok" to keep it.
> **Other options:** Neon or any Postgres host, if you already use one.

## Build

**Tool.** `which supabase`. Missing: `brew install supabase/tap/supabase`.

**Account.**
1. **Your turn:** if you have no account, sign up at supabase.com with GitHub.
2. Run `supabase login`. **Your turn:** approve in the browser.

**Project.** You do all of this:
1. `supabase orgs list` to get the organization ID. If they have none, **Your turn:** create one on the free plan in the dashboard.
2. Generate a database password: `openssl rand -base64 24`. Write it to `.env` as `SUPABASE_DB_PASSWORD`. Tell them to copy it from `.env` into their password manager.
3. Create the project, in the region closest to them:
   ```
   supabase projects create <project> --org-id <id> --region us-west-1 --db-password "$SUPABASE_DB_PASSWORD"
   ```
4. Wait until it reports ready, then `supabase projects api-keys --project-ref <ref>`.
5. Write `SUPABASE_URL` (`https://<ref>.supabase.co`) and the publishable or anon key to `.env`. Add the names, without values, to `.env.example`. Keep the secret and service role keys out of app code.
6. `supabase init`, then `supabase link --project-ref <ref> -p "$SUPABASE_DB_PASSWORD"`.

**Tables.** Write the first migration in `supabase/migrations/` for their project. Every table holding private data gets row level security, meaning rules inside the database that decide who can see each row:
```sql
create table if not exists recipes (
  id uuid primary key default gen_random_uuid(),
  owner uuid not null default auth.uid(),
  title text not null,
  created_at timestamptz default now()
);
alter table recipes enable row level security;
create policy "owner reads"   on recipes for select using (owner = auth.uid());
create policy "owner writes"  on recipes for insert with check (owner = auth.uid());
create policy "owner updates" on recipes for update using (owner = auth.uid());
```
Apply it: `supabase db push`.

Commit and push. Tick the database items in `CHECKLIST.md`.

## Prove
- Agent: `supabase db push --dry-run` reports nothing pending; a request to the table with only the public key and no sign-in returns zero rows.
- Person: opens the Supabase dashboard, sees the project and its tables, each marked as protected.
