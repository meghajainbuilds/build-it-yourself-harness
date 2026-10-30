---
name: messaging
description: Lets the person text their agent and get replies. iMessage on a Mac is the default, with Telegram as the option that works anywhere. Use when the project should talk to someone through text messages.
---

# Messaging: text your agent

**Result:** you text a number or email you own, your agent reads it, thinks, and texts back. Only approved senders get answers.

## Default: iMessage (Mac only)

The bridge in `templates/imessage-bridge/` does three things:
1. Reads new incoming texts from the Messages database on the Mac
2. Passes each approved text to your agent command (`claude` or `codex`)
3. Sends the agent's reply back through the Messages app

### Person does

1. **Pick the account the agent texts from.** Best: a separate Apple ID signed in to Messages on the always-on Mac, so your own texts aren't mixed in. Simplest: your own Apple ID, and the bridge only answers people on the allowlist.
2. **Grant Full Disk Access** so the bridge can read Messages: System Settings, Privacy & Security, Full Disk Access, click +, and add the Python app the agent names (and Terminal if testing by hand).
3. **Allow automation** the first time it sends: macOS asks if it can control Messages. Click OK.

### Agent does

1. Copy `templates/imessage-bridge/` into the project as `bridge/`.
2. Create `bridge/config.json` from `config.example.json`:
   - `allowed_senders`: phone numbers in `+1XXXXXXXXXX` format, or Apple ID emails. **Required.** The bridge refuses to start if it's empty.
   - `agent_command`: from `harness.config.json`, `models.agent_command`
   - `project_dir`: where the agent runs, so it reads the project's AGENTS.md
3. Run `python3 bridge/bridge.py --check` and fix anything it flags.
4. Test by hand: run `python3 bridge/bridge.py` in Terminal, have the person text "hi" from an allowed number, watch the reply arrive, then press Control+C.
5. Then install it as always-on (see `always-on` block).

**Check:** text "What's 2+2?" from an allowed phone and get a reply within about a minute. Text from a number not on the list and get no reply.

### Things to know

- Replies come from whichever Apple ID is signed in to Messages on that Mac.
- The bridge saves the last message it handled in `bridge/state.json`, so it never replays old texts after a restart.
- Newer macOS versions store some message text in a coded field. The bridge decodes the common case. If a text arrives empty in the log, update to the newest bridge.

## Option: Telegram (any computer or cloud)

1. Person messages @BotFather in Telegram, sends `/newbot`, and copies the token **into `.env` as `TELEGRAM_BOT_TOKEN`**, not into chat.
2. Agent writes a small bot loop that long polls `getUpdates`, checks the sender's user ID against an allowlist, runs the agent command, and replies with `sendMessage`.
3. Run it under the `always-on` block.

## Update HARNESS.md

Record the channel, the sending account (not passwords), the allowlist size, and the test result.
