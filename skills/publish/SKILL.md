---
name: publish
description: Puts the project on the web with Netlify, Vercel, or Cloudflare, and adds Google sign-in through Supabase. Use when the project needs a browser interface or sign-in.
---

# publish

## Why
Your project gets a web address, updates itself when you push code, and knows who's using it.

## Choose

| Host | Best when |
|---|---|
| Netlify (default) | Any framework, quickest start |
| Vercel | Built with Next.js |
| Cloudflare | Cost and speed at scale matter most |

All deploy from GitHub on every push and have free plans. None of them keep a process running; that's the `always-on` block.

## Build

**App**
1. If there's no app yet, make the smallest one: a home page, sign in, and save and show one item from Supabase. Vite + React for Netlify or Cloudflare, Next.js for Vercel.
2. Build it locally and fix every error first.

**Host**
1. **Your turn:** sign up on the host with GitHub, Free plan, and give it access to this one repo.
2. Set the build command, output folder, and public variables (`SUPABASE_URL`, `SUPABASE_PUBLISHABLE_KEY`, with the framework's prefix if needed).

**Google sign-in**

OAuth lets people sign in with Google without your app ever seeing their password. It's a round trip: the app sends people to Google, Google returns them to Supabase, Supabase returns them to the app. Each hop needs its address registered.

1. Read Supabase's Google callback address (Authentication, Sign In / Providers, Google).
2. **Your turn:** in console.cloud.google.com, create a project, set up Google Auth Platform as External in Testing, add yourself as a test user, then create a Web client with Supabase's callback as the redirect.
3. **Your turn:** paste the Client ID and secret straight into Supabase's Google settings. Not into chat.
4. In Supabase URL Configuration, set the Site URL to the live address and add it to Redirect URLs.
5. Add sign-in, sign-out, and session handling. Ask Google for basic profile only.

## Prove
- Agent: production build passes; live URL returns the home page; a signed-out request can't read items.
- Person: signs in on the live site, saves an item, refreshes, still sees it; opens a private window and sees nothing private.
