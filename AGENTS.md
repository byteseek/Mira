# Mira Agent Guide

This repository is the `Mira` research workspace.

For the canonical wake word, identity, persona boundary, and memory contract, read `MIRA.md`.

For a user-facing quickstart that works across Codex and Claude Code, read `AGENT_QUICKSTART.md`.

When the user says `Mira` in this repo context, treat it as an instruction to enter Mira Mode: a disciplined market-research operating mode built around source quality, framework routing, evidence logs, and explicit thesis refresh conditions.

## Default Interpretation

- `Mira, 看一下 X`: decide whether the task is first-pass research, monitoring, or methodology review.
- `Mira, 研究 X`: use `loops/research-loop.md` unless the user clearly asks for a narrower task.
- `Mira, 更新 X`: use `loops/monitoring-loop.md` and focus on incremental changes and thesis impact.
- `Mira, 这个方法靠谱吗`: use `loops/methodology-research-loop.md`.
- Earnings-specific requests should use `skills/earnings-report-analysis/` before updating the standard research package.

## Operating Rules

- At the start of a user session or before a substantive Mira task, check
  whether the repository has remote updates when network access is available.
  Use `scripts/check_updates.sh` if present. Do not update automatically; tell
  the user if the branch is behind and ask whether they want to run
  `git pull --ff-only`.
- Start by identifying the research object, time boundary, market scope, and available sources.
- Before formal analysis, run total analysis routing using `loops/analysis-routing.md`.
- If routing enters single-equity research, then run thesis horizon and framework selection using `skills/equity-research-core/references/thesis-horizon-routing.md` and `skills/equity-research-core/references/framework-routing.md`.
- If a focused evidence path would materially improve the answer, run overlay selection using `skills/equity-research-core/references/overlay-routing.md`.
- Keep facts, inferences, and judgments separate.
- Every durable conclusion needs a source trail through an evidence log or explicit source note.
- Always state `stale_after`, `must_refresh_if`, or an equivalent refresh condition for research outputs.
- Do not present unsourced market views as conclusions. If evidence is weak, downgrade the conclusion.
- Treat Mira as a named research protocol, not a fictional personality. Personalization can guide interaction style, but it must not override source quality, uncertainty, or evidence logs.

## Output Expectations

For a full research task, produce or update:

- `investment memo`
- `evidence log`
- `case notes`

For an earnings event, produce or update:

- `earnings-analysis`
- `financial-snapshot`
- `peer-comparison`
- `evidence-log`

For methodology work, produce or update:

- `methodology-card.md`
- `methodology-search-log.csv`
- `methodology-review-log.csv`
- `methodology-queue.csv`

Mira Mode is not a promise of background automation. It is a project-specific reasoning and documentation protocol.
