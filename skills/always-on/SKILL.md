---
name: always-on
description: Keeps the project's agent running when the laptop is closed, on a Mac that stays awake (default) or a cloud server, with restart on crash, logs, and daily schedules. Use when the project acts on its own.
---

# always-on

## Why
Your agent works while you don't: answers texts, runs the morning summary, watches for things.

## Choose

| Where | Cost | Best when |
|---|---|---|
| Mac (default) | $0 on a Mac you own | Using iMessage; a spare Mac or one that stays plugged in |
| Cloud | about $5 to $20 a month | No spare Mac; using Telegram |

## Build (Mac)

macOS can start a program at login and restart it if it stops, using a LaunchAgent (a small settings file in your Library folder).

1. **Your turn:** System Settings, Energy (on a laptop: Battery, Options). Turn on "Prevent automatic sleeping when the display is off" and "Wake for network access." Stay signed in to the Mac.
2. `mkdir -p logs`
3. Copy `templates/imessage-bridge/com.harness.agent.plist` into the project. Replace `__PROJECT_DIR__`, `__PYTHON__` (`which python3`), and `__HOME__` (`echo $HOME`).
4. Install and start:
   ```
   cp com.harness.agent.plist ~/Library/LaunchAgents/
   launchctl load ~/Library/LaunchAgents/com.harness.agent.plist
   ```
5. Write the controls into `MAP.md`:
   - Status: `launchctl list | grep harness`
   - Logs: `tail -f logs/agent.log`
   - Stop: `launchctl unload ~/Library/LaunchAgents/com.harness.agent.plist`

**Schedules:** add entries to `schedules` in `bridge/config.json` with a time and a prompt file in `prompts/`. Prompts live in GitHub, so they're versioned.

## Build (cloud)
Pick a host that keeps one process running and restarts it (Railway, Fly.io, or Render; check current free tiers). Add a `Dockerfile`, set secrets in the host's dashboard, turn on restart. Pair with Telegram in `messaging`.

## Prove
- Agent: status shows running; the log shows "bridge running."
- Person: restarts the Mac, signs in, touches nothing, and status still shows running.
