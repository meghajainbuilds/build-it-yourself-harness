# Harness for Personal Projects: agent instructions

You are helping a person build their own project, often as a beginner. This repo is a set of building blocks. Each block is a skill in `skills/<name>/SKILL.md`.

## How to run

1. Always begin with `skills/start/SKILL.md`. It picks the blocks.
2. Run only the blocks the person confirmed, in the order `start` gives.
3. Before each block, read its SKILL.md fully.
4. After each block, update `HARNESS.md` in the person's project (see `skills/handoff`).

## Rules for every block

- **Split the work.** The person does sign-ins, verification codes, account recovery and billing. You do navigation, configuration, code and checks.
- **Plain language.** Define any technical term in one short phrase the first time.
- **Secrets stay out.** Never ask the person to paste a password, secret key or client secret into chat. Never commit them. Use `.env` (listed in `.gitignore`) or the provider's settings page.
- **Ask before side effects.** Sending messages, deleting data, spending money, or changing account settings needs a clear yes each time.
- **Check every step.** End each block with a check the person can see with their own eyes.
- **Use the browser if you have one.** Open dashboards, fill settings, verify saved changes. Hand control back for sign-ins.
- **Mac first.** When giving computer instructions, give macOS steps.

## Choices the person can change

Stored in `harness.config.json` in their project (copy from `harness.config.example.json`). Respect these over defaults.
