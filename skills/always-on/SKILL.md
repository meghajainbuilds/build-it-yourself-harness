---
name: always-on
description: Keeps an agent running when the laptop is closed, on a Mac that stays awake (default) or a cloud server. Sets up auto restart, schedules, and logs. Use when the project must answer messages or run on a schedule.
---

# Always-on: an agent that doesn't sleep

**Result:** a background process that starts on its own, restarts if it crashes, keeps a log, and can run tasks on a schedule.

## Pick where it runs

Read `always_on.where` in `harness.config.json`.

| Where | Cost | Pick it when |
|---|---|---|
| **mac** (default) | $0 if you own one | Using iMessage, or you have a Mac that stays plugged in |
| **cloud** | about $5 to $20 a month | No spare Mac, or using Telegram/SMS instead of iMessage |

iMessage needs a Mac. A Mac mini or an old MacBook that stays plugged in works well.

## Mac setup

macOS has a built-in way to keep programs running, called a LaunchAgent (a small settings file that tells the Mac to start your program at login and restart it if it stops).

**Person does:**
1. System Settings, Energy (or Battery, Options on a laptop): turn on **Prevent automatic sleeping when the display is off** and **Wake for network access**.
2. Stays signed in to the Mac. LaunchAgents run only while the user is logged in.

**Agent does:**
1. Copy `templates/imessage-bridge/com.harness.agent.plist` to the project and replace the placeholders (`__PROJECT_DIR__`, `__PYTHON__`, `__HOME__`) with real paths. Find Python with `which python3` and the home folder with `echo $HOME`. Run `mkdir -p logs` in the project.
2. Install it:
   ```
   cp com.harness.agent.plist ~/Library/LaunchAgents/
   launchctl load ~/Library/LaunchAgents/com.harness.agent.plist
   ```
3. Show how to check it:
   ```
   launchctl list | grep harness
   tail -f logs/agent.log
   ```
4. To stop it: `launchctl unload ~/Library/LaunchAgents/com.harness.agent.plist`

**Check:** restart the Mac, sign in, and confirm `launchctl list | grep harness` shows it running without doing anything.

## Scheduled tasks

For "every morning at 7" style tasks, add a second LaunchAgent with `StartCalendarInterval`, or put a `schedules` list in the bridge config (see `templates/imessage-bridge/README.md`). Keep scheduled prompts in files under `prompts/` so they live in GitHub.

## Cloud setup

If `where` is `cloud`: pick a host that runs a long running process and restarts it (Railway, Fly.io, or Render; check current free tiers). Package the agent loop with a `Dockerfile`, set secrets in the host's dashboard, and turn on auto restart. Use the `messaging` block with Telegram or SMS, since iMessage can't run in the cloud.

**Check:** close the laptop, send a test message, and get a reply.

## Update HARNESS.md

Record where it runs, how to start, stop and view logs, and any schedules.
