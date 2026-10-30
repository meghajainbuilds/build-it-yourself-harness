---
name: messaging
description: Lets the person text their agent and get replies, through iMessage on a Mac (default) or Telegram anywhere. Only approved senders are answered. Use when the project should talk by text.
---

# messaging

## Why
The most natural interface is the one already on your phone.

## Choose

| Channel | Needs | Notes |
|---|---|---|
| iMessage (default) | A Mac with Messages signed in | Replies come from that Apple ID |
| Telegram | Any computer or cloud | A free bot token |

For iMessage, decide which Apple ID the agent texts from. A separate Apple ID is cleanest. Your own works too, since only approved senders get answers.

## Build (iMessage)

`templates/imessage-bridge/` reads new texts on the Mac (read only), passes approved ones to the agent from `models`, and sends the reply through Messages.

1. Copy it into the project as `bridge/`.
2. Create `bridge/config.json` from the example. Fill `allowed_senders` (`+1XXXXXXXXXX` or Apple ID emails; the bridge won't start without at least one), `agent_command`, and `project_dir`.
3. **Your turn:** System Settings, Privacy & Security, Full Disk Access, click +, add the app running Python (Terminal while testing). This lets the bridge read Messages.
4. Run `python3 bridge/bridge.py --check` and fix anything it flags.
5. Run `python3 bridge/bridge.py`. **Your turn:** text it from an approved phone. The first reply triggers a macOS prompt to let it control Messages; click OK. Press Control+C when done.
6. Hand it to `always-on`.

## Build (Telegram)
1. **Your turn:** message @BotFather, send `/newbot`, and paste the token into `.env` as `TELEGRAM_BOT_TOKEN`.
2. Write a bot loop that polls for updates, checks the sender's ID against an allowlist, runs the agent command, and replies.

## Prove
- Agent: `--check` reports all good.
- Person: texts "What's 2+2?" from an approved phone and gets an answer; texts from an unapproved number and gets nothing.
