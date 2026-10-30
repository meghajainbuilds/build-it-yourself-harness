# Harness for Personal Projects: agent instructions

You're building a personal project with someone. This repo gives you blocks, each in `skills/<name>/SKILL.md`. Always begin with `skills/start/SKILL.md`.

## Every block has four parts

- **Why**: tell the person in one line what this block adds.
- **Choose**: offer the options, recommend the default, respect `harness.config.json`.
- **Build**: do the work yourself. Pause at each **Your turn** and wait.
- **Prove**: run the agent test, then ask the person to see the result. Don't start the next block until both pass.

## Your turn means

Only the person signs in, enters codes, approves access, handles billing, or pastes secrets (into `.env` or a settings page, never into chat). Say exactly what to click, on a Mac, then wait.

## Always

- Plain words. Define a technical term in a short phrase the first time.
- Ask before anything that sends, deletes, spends, or changes account settings.
- Keep `MAP.md` current (see `skills/map`). It's how the next agent finds its way.
- Use a browser tool if you have one to open dashboards and confirm settings saved.
