---
name: publish
description: Puts the app on the web with Netlify (default), Vercel, or Cloudflare, and adds Google sign-in through Supabase. Use when the project needs a web page, dashboard, or sign-in.
---

# Publish: your app at a web address

**Result:** a live URL that updates every time code is pushed to GitHub, with "Sign in with Google."

## Pick a host

Read `publish.host` in `harness.config.json`.

| Host | Pick it when |
|---|---|
| **Netlify** (default) | Any framework, simplest start |
| **Vercel** | The app uses Next.js |
| **Cloudflare** | Lots of traffic or lowest cost matters |

All three have free plans and deploy from GitHub automatically. Neither Netlify nor Vercel runs things in the background; use the `always-on` block for that.

## Build a minimal app

If no app exists yet, create a minimal one: a landing page, a sign-in button, and a page that saves and reads one note from Supabase. Use Vite + React for Netlify or Cloudflare, Next.js for Vercel. Run the build locally and fix errors before deploying.

## Connect the host

**Person does:** signs up with GitHub on the host, picks Free, and authorizes access to this one repo.

**Agent does:** gives the exact build command, output folder, and environment variables (`SUPABASE_URL`, `SUPABASE_PUBLISHABLE_KEY`, plus the framework's public prefix if needed, like `VITE_` or `NEXT_PUBLIC_`). Fills them in through the browser if available.

**Check:** the person opens the `.netlify.app`, `.vercel.app`, or `.pages.dev` address and sees the landing page.

## Google sign-in

OAuth is how someone signs in with Google without giving your app their Google password.

Two addresses must match:
- Google sends people back to **Supabase** (callback URL from Supabase, Authentication, Sign In / Providers, Google)
- Supabase sends people back to **your app** (Authentication, URL Configuration)

**Person does, in Google Cloud Console:**
1. Create a project, open Google Auth Platform, finish setup, choose External, stay in Testing, and add their email as a test user.
2. Clients, Create client, Web application. Paste Supabase's callback URL as an authorized redirect URI.
3. Copy the Client ID and Client secret **directly into Supabase's Google provider settings**. Not into chat.

**Agent does:** sets Supabase's Site URL to the live address, adds redirect URLs, and wires up sign-in, sign-out, and session handling. Requests only basic profile info.

**Check:** sign in on the live site, save a note, refresh, and the note is still there. Open a private window and confirm the note isn't visible when signed out.

## Update HARNESS.md

Add the host, live URL, Google Cloud project name, and test results.
