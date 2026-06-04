# Mira Instructions For Claude Code

This repository is the `Mira` market-research workspace.

When working in Claude Code, follow the same project protocol as Codex.
Do not duplicate the rules manually; use the root files as the source of truth:

1. Read [AGENTS.md](AGENTS.md) for the operating rules.
2. Read [MIRA.md](MIRA.md) for the wake word, identity contract, persona boundary, and memory rules.
3. Read [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md) for the one-screen lazy-loading contract.
4. Read [AGENT_QUICKSTART.md](AGENT_QUICKSTART.md) for user-facing entry points, prompt patterns, routing, output locations, and required evidence discipline.
5. When the user says `Mira`, enter Mira Mode.

Minimum execution rules:

- For `update mira` / Mira self-update requests, run `scripts/mira_update.sh`
  directly.
- Before substantive research, run `scripts/check_updates.sh` when network
  access is available, then route the task with `loops/analysis-routing.md`.
- Keep facts, inferences, judgments, evidence trails, and refresh conditions
  explicit.
- Use position, portfolio, instrument, and trade-action framing only within the
  gates named in `OPERATING_CONTRACT.md`.

Mira Mode is a research and documentation protocol, not a promise of background automation.
