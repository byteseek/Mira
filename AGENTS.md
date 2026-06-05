# Mira Agent Guide

This repository is the `Mira` research workspace. Mira is a named research
protocol, not a fictional personality, adviser, trade bot, or background
automation promise.

## Read Order

1. `MIRA.md` for the wake word, identity boundary, and memory contract.
2. `OPERATING_CONTRACT.md` for the one-screen lazy-loading map.
3. `START_HERE.md` when the user asks how to start, what Mira covers, or wants prompt examples.
4. `AGENT_QUICKSTART.md` only when agent execution details, output locations, or extended examples are needed.

## Fast Paths

| user intent | do this |
| --- | --- |
| empty first prompt, `hi Mira`, `你好 Mira`, `Mira mode`, or onboarding request | Return a concise `START_HERE.md` summary before any research workflow. |
| `update mira`, `Mira self-update`, `从 GitHub 拉最新 Mira` | Run `scripts/mira_update.sh`. Do not run `scripts/check_updates.sh` first. |
| `Mira help`, `怎么用 Mira`, `Mira 能做什么`, `start here` | Return the layered Start Here card from `START_HERE.md`; keep it user-facing and concise. |
| start a substantive Mira research task | Run `scripts/check_updates.sh` when network access is available; report if behind, but do not update unless the user asks. |
| `Mira, 看一下 X` | Treat as `quick_map`; route first, then answer with source notes and refresh triggers. |
| time-sensitive market question (`今天`, `现在`, `目前`, `latest`, intraday, premarket, after-hours, crash/pullback) | Run `data/live-data-source-policy.md`; search or refresh live sources before judging, and show quote/publish time plus freshness caveat. |
| `Mira, 研究 X` | Use `loops/research-loop.md` unless routing selects a narrower path. |
| `Mira, 更新 X` | Use `loops/monitoring-loop.md`; focus on incremental evidence and thesis impact. |
| earnings, guidance, or transcript work | Use `skills/earnings-report-analysis/` before updating a standard research package. |
| methodology reliability | Use `loops/methodology-research-loop.md`. |
| PM, position, portfolio, or decision review | Use the matching review loop from `OPERATING_CONTRACT.md`. |

If a user already provides a concrete research task as the first prompt, do not
block with onboarding. Route and answer the task, optionally adding one short
line that `Mira help` shows the full prompt menu.

## Research Rules

- Start by identifying `research_object`, `market_scope`, `time_boundary`, and
  available sources.
- Before formal analysis, run `loops/analysis-routing.md`.
- For time-sensitive market questions, run `data/live-data-source-policy.md`
  before judging the move; do not answer from memory or stale market data.
- Use `quick_map`, `standard`, or `deep_dive` to control depth. Do not let a
  quick look become a full package unless the user asks.
- For single-equity research, run thesis horizon and framework routing; add
  overlay routing only when it materially improves the evidence path.
- Use the quant dependency gate when conclusions rely on derived numbers,
  valuation math, peer ranking, or time-series comparisons.
- Keep facts, inferences, and judgments separate.
- Tie every durable conclusion to an evidence log or explicit source note.
- Keep user-specific views, watchlists, preferences, holdings, weights, and
  portfolio constraints in gitignored `private/` state by default. Tracked Mira
  files are product state unless the user explicitly asks to contribute a
  de-identified example or method.
- State `stale_after`, `must_refresh_if`, or an equivalent refresh condition.
- Downgrade conclusions when source quality, freshness, or calculation support
  is weak.
- Do not present position-size or portfolio-construction conclusions without
  user-provided holdings, weights, mandate, and risk budget.
- Use research actions only; never present autonomous trade execution.

## Expected Artifacts

| task | required outputs |
| --- | --- |
| full research | `investment-memo.md`, `evidence-log.csv`, `case-notes.md` |
| earnings event | `earnings-analysis`, `financial-snapshot`, `peer-comparison`, `evidence-log` |
| methodology work | `methodology-card.md`, search/review logs, queue update |
| position or portfolio review | review file, register or exposure file, follow-up queue, refresh conditions |
