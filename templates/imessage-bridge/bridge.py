#!/usr/bin/env python3
"""
iMessage bridge for Harness for Personal Projects.

Reads new incoming iMessages on this Mac, sends approved ones to your coding
agent (Claude Code, Codex, or any command), and texts the reply back.
Also runs scheduled prompts (for example, a 7am summary).

Python standard library only. macOS only.

Usage:
  python3 bridge.py            run forever (what the LaunchAgent does)
  python3 bridge.py --check    test config, Messages access, and agent command
  python3 bridge.py --send +12065550100 "hello"   send one test text
"""

import json
import os
import shlex
import sqlite3
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONFIG_PATH = HERE / "config.json"
STATE_PATH = HERE / "state.json"
CHAT_DB = Path.home() / "Library" / "Messages" / "chat.db"

PRESETS = {
    "claude": ["claude", "-p"],
    "codex": ["codex", "exec"],
}

DEFAULT_INSTRUCTIONS = (
    "You are replying to a text message. Answer in plain text, no markdown, "
    "under 600 characters unless the person asks for more. "
    "Do not send messages, delete data, or spend money; describe what you "
    "would do and ask for a yes instead."
)


def log(msg):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{stamp}] {msg}", flush=True)


def load_json(path, default):
    try:
        return json.loads(Path(path).read_text())
    except FileNotFoundError:
        return default


def save_state(state):
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2))
    tmp.replace(STATE_PATH)


def normalize(handle):
    h = handle.strip().lower().replace(" ", "").replace("-", "")
    h = h.replace("(", "").replace(")", "")
    return h


def load_config():
    cfg = load_json(CONFIG_PATH, None)
    if cfg is None:
        sys.exit(f"Missing {CONFIG_PATH}. Copy config.example.json to config.json.")
    allowed = [normalize(a) for a in cfg.get("allowed_senders", []) if a.strip()]
    if not allowed:
        sys.exit("allowed_senders is empty. Add at least one phone or email. "
                 "The bridge will not answer everyone.")
    cfg["_allowed"] = set(allowed)
    cfg.setdefault("agent_command", "claude")
    cfg.setdefault("project_dir", str(HERE.parent))
    cfg.setdefault("poll_seconds", 5)
    cfg.setdefault("agent_timeout_seconds", 300)
    cfg.setdefault("instructions", DEFAULT_INSTRUCTIONS)
    cfg.setdefault("schedules", [])
    return cfg


# ---------- reading Messages ----------

def open_db():
    # Read only, so the bridge can never change your messages.
    uri = f"file:{CHAT_DB}?mode=ro"
    return sqlite3.connect(uri, uri=True, timeout=5)


def decode_attributed_body(blob):
    """Newer macOS stores some text only in attributedBody. Pull the string out."""
    if not blob:
        return None
    try:
        idx = blob.find(b"NSString")
        if idx < 0:
            return None
        rest = blob[idx + len(b"NSString"):]
        plus = rest.find(b"\x2b")
        if plus < 0:
            return None
        length = rest[plus + 1]
        start = plus + 2
        if length == 0x81:
            length = int.from_bytes(rest[plus + 2:plus + 4], "little")
            start = plus + 4
        elif length == 0x82:
            length = int.from_bytes(rest[plus + 2:plus + 5], "little")
            start = plus + 5
        return rest[start:start + length].decode("utf-8", errors="ignore") or None
    except Exception:
        return None


def max_rowid(conn):
    row = conn.execute("SELECT MAX(ROWID) FROM message").fetchone()
    return row[0] or 0


def new_messages(conn, after_rowid):
    rows = conn.execute(
        """
        SELECT m.ROWID, m.text, m.attributedBody, h.id
        FROM message m
        JOIN handle h ON m.handle_id = h.ROWID
        WHERE m.ROWID > ? AND m.is_from_me = 0
        ORDER BY m.ROWID ASC
        """,
        (after_rowid,),
    ).fetchall()
    out = []
    for rowid, text, body, sender in rows:
        text = text or decode_attributed_body(body)
        out.append((rowid, sender, text))
    return out


# ---------- sending Messages ----------

SEND_SCRIPT = """
on run argv
  set targetHandle to item 1 of argv
  set msg to item 2 of argv
  tell application "Messages"
    set svc to 1st account whose service type = iMessage
    send msg to participant targetHandle of svc
  end tell
end run
"""


def send_imessage(handle, text):
    chunks = [text[i:i + 1500] for i in range(0, len(text), 1500)] or [""]
    for chunk in chunks:
        subprocess.run(["osascript", "-e", SEND_SCRIPT, handle, chunk],
                       check=True, capture_output=True, timeout=30)


# ---------- calling the agent ----------

def agent_argv(cfg):
    cmd = cfg["agent_command"]
    if cmd in PRESETS:
        return list(PRESETS[cmd])
    return shlex.split(cmd)


def ask_agent(cfg, prompt):
    argv = agent_argv(cfg) + [prompt]
    try:
        result = subprocess.run(argv, cwd=cfg["project_dir"], capture_output=True,
                                text=True, timeout=cfg["agent_timeout_seconds"])
    except FileNotFoundError:
        return f"Setup problem: '{argv[0]}' is not installed or not on PATH."
    except subprocess.TimeoutExpired:
        return "That took too long. Try a shorter request."
    reply = (result.stdout or "").strip()
    if result.returncode != 0 or not reply:
        log(f"agent error {result.returncode}: {(result.stderr or '')[:500]}")
        return reply or "Something went wrong on my side. Check the bridge log."
    return reply


def build_prompt(cfg, sender, text):
    return f"{cfg['instructions']}\n\nMessage from {sender}:\n{text}"


# ---------- schedules ----------

def run_schedules(cfg, state):
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    ran = state.setdefault("schedules_ran", {})
    for job in cfg["schedules"]:
        name = job.get("name") or job.get("time")
        if now.strftime("%H:%M") < job["time"] or ran.get(name) == today:
            continue
        send_to = job["send_to"]
        if normalize(send_to) not in cfg["_allowed"]:
            log(f"schedule {name}: {send_to} is not in allowed_senders, skipped")
            ran[name] = today
            continue
        prompt_path = Path(cfg["project_dir"]) / job["prompt_file"]
        try:
            prompt = prompt_path.read_text()
        except FileNotFoundError:
            log(f"schedule {name}: missing {prompt_path}")
            ran[name] = today
            continue
        log(f"schedule {name}: running")
        reply = ask_agent(cfg, f"{cfg['instructions']}\n\n{prompt}")
        send_imessage(send_to, reply)
        ran[name] = today
        save_state(state)


# ---------- main ----------

def check(cfg):
    ok = True
    print(f"Config: {CONFIG_PATH}")
    print(f"Allowed senders: {len(cfg['_allowed'])}")
    try:
        conn = open_db()
        print(f"Messages database: readable, latest message id {max_rowid(conn)}")
    except Exception as e:
        ok = False
        print(f"Messages database: NOT readable ({e}).\n"
              "  Fix: System Settings > Privacy & Security > Full Disk Access, "
              "add the Python or Terminal app running this.")
    reply = ask_agent(cfg, "Reply with exactly: bridge ok")
    print(f"Agent ({cfg['agent_command']}): {reply[:200]}")
    if "bridge ok" not in reply.lower():
        ok = False
    print("All good." if ok else "Fix the items above, then run --check again.")
    return ok


def run(cfg):
    state = load_json(STATE_PATH, {})
    conn = open_db()
    if "last_rowid" not in state:
        # First run: start from now so old texts are never replayed.
        state["last_rowid"] = max_rowid(conn)
        save_state(state)
    log(f"bridge running, {len(cfg['_allowed'])} allowed senders, "
        f"agent '{cfg['agent_command']}'")
    while True:
        try:
            for rowid, sender, text in new_messages(conn, state["last_rowid"]):
                state["last_rowid"] = rowid
                save_state(state)
                if normalize(sender) not in cfg["_allowed"]:
                    continue
                if not text:
                    log(f"from {sender}: empty or attachment only, skipped")
                    continue
                log(f"from {sender}: {text[:80]}")
                reply = ask_agent(cfg, build_prompt(cfg, sender, text))
                send_imessage(sender, reply)
                log(f"replied to {sender}: {reply[:80]}")
            run_schedules(cfg, state)
        except sqlite3.OperationalError as e:
            log(f"database busy or moved ({e}), reconnecting")
            time.sleep(2)
            conn = open_db()
        except Exception as e:
            log(f"error: {e}")
        time.sleep(cfg["poll_seconds"])


def main():
    cfg = load_config()
    args = sys.argv[1:]
    if args[:1] == ["--check"]:
        sys.exit(0 if check(cfg) else 1)
    if args[:1] == ["--send"] and len(args) == 3:
        if normalize(args[1]) not in cfg["_allowed"]:
            sys.exit("That handle is not in allowed_senders.")
        send_imessage(args[1], args[2])
        print("Sent.")
        return
    if args:
        sys.exit(__doc__)
    run(cfg)


if __name__ == "__main__":
    main()
