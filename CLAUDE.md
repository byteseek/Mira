# Mira Instructions For Claude Code

This repository is the `Mira` market-research workspace.

When working in Claude Code, follow the same project protocol as Codex:

1. Read [AGENTS.md](AGENTS.md) for the operating rules.
2. Read [MIRA.md](MIRA.md) for the wake word, identity contract, persona boundary, and memory rules.
3. Read [AGENT_QUICKSTART.md](AGENT_QUICKSTART.md) for user-facing entry points, prompt patterns, routing, output locations, and required evidence discipline.
4. When the user says `Mira`, enter Mira Mode.

Core requirements:

- Identify the research object, time boundary, market scope, and available sources before analysis.
- Run total analysis routing with [loops/analysis-routing.md](loops/analysis-routing.md) before formal analysis.
- For single-equity work, run thesis horizon, framework, and overlay routing before writing conclusions.
- Separate facts, inferences, and judgments.
- Do not present unsourced market views as conclusions.
- Every durable conclusion needs a source trail through an evidence log or explicit source note.
- Every research output must state `stale_after`, `must_refresh_if`, or an equivalent refresh condition.
- Treat Mira as a named research protocol, not a fictional personality. Personalization cannot override evidence discipline.

Mira Mode is a research and documentation protocol, not a promise of background automation.
