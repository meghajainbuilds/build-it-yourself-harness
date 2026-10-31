---
name: messaging
description: Lets the person text their agent and get replies, through iMessage on a Mac (default) or Telegram anywhere. Only approved senders get answers. Use when the project should talk by text.
---

# messaging

## Why
You reach your project from the app already on your phone.

## Choose

> **Default: iMessage**, through a Mac with Messages signed in. Say "ok" to keep it.
> **Other options:** Telegram (works on any computer or cloud server), SMS through Twilio (paid).

For iMessage, the agent replies from whichever Apple ID is signed in to Messages on that Mac. A separate Apple ID keeps your own texts apart. Your own Apple ID works too, since the bridge answers approved senders only.

## Build (iMessage)

The bridge in `templates/imessage-bridge/` reads new texts on the Mac (read only), passes approved ones to the agent from `models`, and replies through Messages.

1. Copy it into the project: `mkdir -p bridge && cp templates/imessage-bridge/* bridge/`.
2. Ask which phone numbers or Apple ID emails may text it. Write `bridge/config.json` with `allowed_senders` (`+1XXXXXXXXXX` format), `agent_command`, and `project_dir`.
3. **Your turn:** System Settings, Privacy & Security, Full Disk Access, click +, add Terminal (and later the Python app the LaunchAgent uses). This lets the bridge read Messages.
4. Run `python3 bridge/bridge.py --check` and fix anything it reports.
5. Run `python3 bridge/bridge.py`. **Your turn:** text "hi" from an approved phone. On the first reply, macOS asks to let Terminal control Messages; click OK. Press Control+C when you see the reply.
6. Hand it to `always-on`.

## Build (Telegram)
1. **Your turn:** in Telegram, message @BotFather, send `/newbot`, and paste the token into `.env` as `TELEGRAM_BOT_TOKEN`.
2. Write a bot loop that polls for new messages, checks the sender against an allowlist, runs the agent command, and replies.

## Prove
- Agent: `--check` reports all good.
- Person: texts "What's 2+2?" from an approved phone and gets an answer; a text from an unapproved number gets no reply.
