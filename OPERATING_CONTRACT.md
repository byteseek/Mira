# Mira Operating Contract

This is the one-screen contract an agent should read before loading heavier Mira references.

Use it to save context. Load detailed loops, skills and templates only when the current step requires them.

## Core Contract

Mira is a research protocol, not an adviser or trade bot.

Every formal output must:

- identify `research_object`, `market_scope`, `time_boundary` and available sources
- run [loops/analysis-routing.md](loops/analysis-routing.md) before formal analysis
- choose `depth_mode`: `quick_map`, `standard` or `deep_dive`
- separate `facts`, `inferences` and `judgments`
- keep every durable conclusion tied to an evidence log or explicit source note
- include `stale_after`, `must_refresh_if` or equivalent refresh conditions
- downgrade conclusions when evidence quality is weak
- avoid autonomous trade instructions; use research actions only

## Lazy Loading Map

| task step | read only this first | load next only if needed |
| --- | --- | --- |
| Wake word / identity | [MIRA.md](MIRA.md) | [AGENT_QUICKSTART.md](AGENT_QUICKSTART.md) for prompts |
| Any formal task | [loops/analysis-routing.md](loops/analysis-routing.md) | selected loop from routing |
| First-pass single equity | [loops/research-loop.md](loops/research-loop.md) | thesis horizon, framework and overlay references |
| Thesis update / expectation change | [loops/thesis-update-loop.md](loops/thesis-update-loop.md) | thesis ledger, expectation map and decision-log templates |
| Event or earnings delta | [loops/event-delta-loop.md](loops/event-delta-loop.md) | earnings skill and event-delta template |
| SEC fact supplement | [skills/sec-filing-analysis/SKILL.md](skills/sec-filing-analysis/SKILL.md) | [templates/sec-supplement-source-note.csv](templates/sec-supplement-source-note.csv) |
| SEC filing deep dive | [skills/sec-filing-analysis/SKILL.md](skills/sec-filing-analysis/SKILL.md) | [templates/sec-filing-analysis-package/](templates/sec-filing-analysis-package/) |
| PM / book review | [loops/portfolio-review-loop.md](loops/portfolio-review-loop.md) | portfolio register template and research index |
| Source routing | [data/source-taxonomy.md](data/source-taxonomy.md) | [data/source-coverage-matrix.csv](data/source-coverage-matrix.csv) |
| Evidence logging | [data/evidence-log-schema.md](data/evidence-log-schema.md) | [data/claim-taxonomy.md](data/claim-taxonomy.md) |
| Numeric / calculation gate | [skills/data-analysis-quality-gate/SKILL.md](skills/data-analysis-quality-gate/SKILL.md) | [templates/data-requirement-brief.md](templates/data-requirement-brief.md) and [templates/calculation-ledger.csv](templates/calculation-ledger.csv) |
| State/action tokens | [data/controlled-vocabulary.md](data/controlled-vocabulary.md) | task-specific template |
| Final self-check | [templates/delivery-checklist.md](templates/delivery-checklist.md) | task-specific quality bar |

Do not load all `memory/`, all `skills/` or all cases at startup. Retrieve only the files required by the routed task.

## Depth Defaults

| depth_mode | use when | default cost control |
| --- | --- | --- |
| `quick_map` | fast read, early triage, unclear source boundary | read only the most relevant sources; output routing card, core judgment, source notes and refresh triggers |
| `standard` | normal research package, earnings package, monitoring update | load only routed loop / skill plus triggered references; output required package artifacts |
| `deep_dive` | long-term thesis, complex valuation, SEC deep dive, PM / methodology review | allow extra sources and artifacts only when each one improves evidence quality, actionability, or refresh conditions |

If the user does not specify depth, infer it from the requested output. "看一下" defaults to `quick_map`; "研究 X" defaults to `standard`; "深挖 / 完整 / 方法验证 / PM review" defaults to `deep_dive`.

## Role Defaults

| user role | default path | default output |
| --- | --- | --- |
| Research analyst | `analysis-routing` -> `research-loop` or relevant skill | research package, evidence log, thesis objects if durable |
| Trader | `analysis-routing` -> thesis/event update -> actionability bridge | research action, invalidation, risk/reward frame, next catalyst |
| Portfolio manager | `portfolio-review-loop` plus thesis index | thesis board, exposure/crowding notes, follow-up list |

If the user does not name a role, infer it from the requested output. A request for "能不能动" or "预期差" is trader-facing; a request for "哪些 thesis 需要看" is PM-facing; a request for "研究 X" is analyst-facing.

## Golden Examples

Use these as few-shot examples before old cases:

- [cases/aapl-2026-04/](cases/aapl-2026-04/): single-equity golden case with memo, canonical evidence log, expectation map, thesis ledger, decision log and actionability bridge.
- [cases/nvts-2026-05/](cases/nvts-2026-05/): earnings/event case with peer verification, event impact framing and actionability bridge.

Legacy cases may be useful as historical artifacts, but do not copy their old evidence-log shape.

## Stop Rules

Stop or downgrade when:

- the key conclusion rests only on L4/L6, sentiment, opinion or rumor
- consensus proxy cannot be stated at variable level
- valuation anchor is missing for an actionability claim
- the case is past `stale_after` and the user wants live use
- facts, inferences and judgments cannot be separated

When stopped, return `source_gap`, `watch_only`, `no_action` or `needs_refresh` instead of forcing a stronger conclusion. Use [data/controlled-vocabulary.md](data/controlled-vocabulary.md) for machine-facing state/action tokens.
