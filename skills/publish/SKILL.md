---
name: publish
description: Puts the project on the web with Netlify (default), Vercel, or Cloudflare, connected to GitHub so every push updates the site, and adds Google sign-in through Supabase. Use when the person will use their project in a browser.
---

# publish

## Why
Your app gets its own web address, updates itself every time you save code to GitHub, and knows who is signed in.

## Choose

> **Default: Netlify** (free plan). Works with any framework. Say "ok" to keep it.
> **Other options:** Vercel (best fit for Next.js apps), Cloudflare Pages (lowest cost at high traffic).

> **Sign-in default: Google.** Say "ok" to keep it.
> **Other options:** email magic links (Supabase sends a sign-in link), GitHub sign-in.

## Build

**App.** If no app exists, create the smallest version of their idea: a home page, sign in, and one screen that saves and shows one record from the database. Vite + React for Netlify or Cloudflare, Next.js for Vercel. Run the production build and fix every error.

**Host (Netlify).**
1. `which netlify`. Missing: `npm install -g netlify-cli`.
2. `netlify login`. **Your turn:** approve in the browser.
3. `netlify init` to create the site and connect it to this GitHub repo with automatic deploys. **Your turn:** approve Netlify's access to this one repo when GitHub asks.
4. Set the public variables yourself: `netlify env:set VITE_SUPABASE_URL ...` and `netlify env:set VITE_SUPABASE_ANON_KEY ...` (use the framework's prefix).
5. Push to GitHub and watch the deploy finish.

For Vercel, use `vercel login`, `vercel link`, `vercel env add`, and `vercel git connect`. For Cloudflare, use `wrangler login` and `wrangler pages project create`.

**Google sign-in.** OAuth is the handshake that lets someone sign in with Google without your app ever seeing their password. The person goes from your app to Google, Google sends them to Supabase, and Supabase sends them back to your app. Each stop needs the next address registered.

1. Your callback address is `https://<ref>.supabase.co/auth/v1/callback`.
2. Google requires a person to create the sign-in client. If you have a browser tool, open console.cloud.google.com and fill in each screen, pausing for sign-in. **Your turn** for: signing in to Google, and clicking Create. The settings:
   - New project named after their app
   - Google Auth Platform: External, Testing, their email as a test user
   - Clients, Create client, Web application, with the callback address above as the redirect
3. **Your turn:** paste the Client ID and Client secret into `.env` as `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`. Read them from `.env` yourself; keep them out of chat.
4. Turn on Google in Supabase and set the return addresses through the Supabase Management API, using the token from `supabase login`: enable the Google provider with the ID and secret, set the site URL to the live address, and add the live address and `http://localhost:5173` to the allowed redirects.
5. Add sign-in, sign-out, and session handling to the app. Request basic profile only. Push.

## Prove
- Agent: the deploy succeeded; the live address returns the home page; a signed-out request reads zero private rows.
- Person: signs in on the live site, saves something, refreshes and still sees it, then opens a private window and sees no private data.
