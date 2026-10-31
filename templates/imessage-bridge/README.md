# iMessage bridge

Text your agent from your phone. It reads, thinks, and texts back.

## How it works

1. Every few seconds, reads new incoming texts from the Messages database on this Mac (read only)
2. Answers only the people listed in `allowed_senders`
3. Passes the text to your agent command (`claude`, `codex`, or your own)
4. Sends the reply through the Messages app
5. Runs any `schedules` once a day at their time

Standard library Python only. Nothing to install.

## Set up

```
mkdir -p logs prompts
cp bridge/config.example.json bridge/config.json   # then edit it
python3 bridge/bridge.py --check
```

`--check` confirms the Messages database is readable and your agent command replies. If the database isn't readable, give Full Disk Access to the app running Python: System Settings, Privacy & Security, Full Disk Access, click +.

Test by hand:

```
python3 bridge/bridge.py
```

Text it from an allowed phone. Press Control+C to stop. Then install the LaunchAgent so it runs on its own (see the `always-on` skill).

## Config

| Key | Meaning |
|---|---|
| `allowed_senders` | Phones (`+1XXXXXXXXXX`) or Apple ID emails it will answer. Required. |
| `agent_command` | `claude`, `codex`, or any command that takes the message as its last argument and prints a reply |
| `project_dir` | Folder the agent runs in, so it reads that project's AGENTS.md |
| `schedules` | Daily prompts: `time` (24 hour, local), `prompt_file`, `send_to` (must be allowed) |

## Limits

- Mac only, and the Mac must stay awake and signed in.
- Text only. Photos and attachments are skipped.
- Group chats are answered only if the sender is allowed, and the reply goes to that sender directly.
- `state.json` remembers the last message handled. Delete it to start fresh from "now."
