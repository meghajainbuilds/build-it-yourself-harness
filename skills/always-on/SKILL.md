---
name: always-on
description: Keeps the project's agent running when the laptop is closed, on a Mac that stays awake (default) or a cloud server, with automatic restart, logs, and daily schedules. Use when the project acts on its own.
---

# always-on

## Why
Your agent keeps working while you're away: answering texts, sending the morning summary, watching for things.

## Choose

> **Default: a Mac that stays awake.** $0 on a Mac you own, and required for iMessage. Say "ok" to keep it.
> **Other options:** a cloud server such as Railway, Fly.io, or Render (about $5 to $20 a month), paired with Telegram.

## Build (Mac)

macOS restarts a program automatically through a LaunchAgent, a small settings file in your Library folder that says "start this at login and restart it if it stops."

1. **Your turn:** System Settings, Energy (on a laptop: Battery, Options). Turn on "Prevent automatic sleeping when the display is off" and "Wake for network access." Stay signed in to the Mac.
2. You do the rest:
   ```
   mkdir -p logs ~/Library/LaunchAgents
   ```
   Copy `templates/imessage-bridge/com.harness.agent.plist`, fill in `__PROJECT_DIR__`, `__PYTHON__` (from `which python3`), and `__HOME__` (from `echo $HOME`), then:
   ```
   cp com.harness.agent.plist ~/Library/LaunchAgents/
   launchctl load ~/Library/LaunchAgents/com.harness.agent.plist
   ```
3. Record the controls in `CHECKLIST.md`:
   - Status: `launchctl list | grep harness`
   - Logs: `tail -f logs/agent.log`
   - Stop: `launchctl unload ~/Library/LaunchAgents/com.harness.agent.plist`

**Schedules.** Add entries to `schedules` in `bridge/config.json`, each with a time and a prompt file in `prompts/`. Prompts live in GitHub with the rest of the project.

## Build (cloud)
Add a `Dockerfile` for the agent loop. Use the host's command line (for Railway: `railway login`, `railway init`, `railway variables set`, `railway up`). **Your turn:** sign in once and approve billing. Turn on automatic restart.

## Prove
- Agent: status shows the process running; the log shows "bridge running."
- Person: restarts the Mac, signs in, touches nothing, and status still shows running.
