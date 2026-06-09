# Mira Instructions For Claude Code

This repository is the `Mira` market-research workspace.

When working in Claude Code, follow the same project protocol as Codex.
Do not duplicate the rules manually; use the root files as the source of truth:

1. Read [MIRA_BOOTSTRAP.md](MIRA_BOOTSTRAP.md) for the minimum entry gate and visible route signal.
2. Read [AGENTS.md](AGENTS.md) for the operating rules.
3. Read [MIRA.md](MIRA.md) for the wake word, identity contract, persona boundary, and memory rules.
4. Read [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md) for the one-screen lazy-loading contract.
5. Read [START_HERE.md](START_HERE.md) when the user asks how to start, what Mira covers, or wants prompt examples.
6. Read [AGENT_QUICKSTART.md](AGENT_QUICKSTART.md) for agent execution details, routing, output locations, and required evidence discipline.
7. When the user says `Mira`, enter Mira Mode.

Minimum execution rules:

- On an empty first prompt, `hi Mira`, `你好 Mira`, `Mira mode`, or an
  onboarding request, return a concise `START_HERE.md` summary before any
  research workflow.
- If the first prompt is already a concrete research task, do not block with
  onboarding; route the task and optionally mention `Mira help`.
- For `update mira` / Mira self-update requests, run `scripts/mira_update.sh`
  directly.
- For `Mira help`, `怎么用 Mira`, `Mira 能做什么` or `start here`, return the
  layered user-facing entry card from `START_HERE.md`.
- For `standard` / `deep_dive` research, run `scripts/check_updates.sh` once
  (local-first by default, with a 24h remote TTL); `quick_map` / 看一下 tasks
  skip it. A blocked fetch degrades to local refs and is reported — never
  elevate sandbox permissions for a freshness check. Then route the task with
  `loops/analysis-routing.md`.
- Keep facts, inferences, judgments, evidence trails, and refresh conditions
  explicit.
- Use position, portfolio, instrument, and trade-action framing only within the
  gates named in `OPERATING_CONTRACT.md`.

Mira Mode is a research and documentation protocol, not a promise of background automation.
