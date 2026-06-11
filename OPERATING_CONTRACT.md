# Mira Operating Contract

This is the one-screen contract an agent should read before loading heavier Mira references.

Use it to save context. Load detailed loops, skills and templates only when the current step requires them.

## Core Contract

Mira is a research protocol, not an adviser or trade bot.

Every formal output must:

- preserve the minimum interaction quality bar in [data/interaction-kernel.md](data/interaction-kernel.md)
- identify `research_object`, `market_scope`, `time_boundary` and available sources
- run intent intake first: split compound prompts into `primary_intent` / `secondary_intents`, declare running assumptions, and emit a depth-scaled routing card before formal analysis
- run [loops/analysis-routing.md](loops/analysis-routing.md) before formal analysis
- route via the machine index first: read [data/routing-index.csv](data/routing-index.csv) (`task_mode` → one `primary_loop_or_skill` + trigger + `load_gate`), then load only that one loop/skill body; do not front-load the whole analysis-routing.md
- choose `depth_mode`: `quick_map`, `standard` or `deep_dive`
- when it improves the question, apply at most two [question expansion lenses](data/question-expansion-lenses.md) before source or calculation budget is spent
- when the prompt is time-sensitive (`today`, `now`, `latest`, intraday market
  reaction, or similar), run [data/live-data-source-policy.md](data/live-data-source-policy.md)
  before judging the move; search or live-source lookup is required unless the
  answer is only a stable definition
- after choosing depth, run the information-value / knowability check; allow `irreducible_uncertainty` as an honest terminal instead of over-researching
- separate `facts`, `inferences` and `judgments`, and label each material judgment with `judgment_confidence` and a `reversal_condition`
- keep every durable conclusion tied to an evidence log or explicit source note
- keep user-specific views, holdings, watchlists and preferences in gitignored
  `private/` state by default; tracked Mira files are product state
- record `private_state_action` when an output creates, continues, updates,
  promotes or waives a reusable user view
- route newly supplied files, public API pulls, vendor exports and portfolio
  data through [data/ingestion-layer.md](data/ingestion-layer.md) before using
  them as evidence or calculations
- label evidence posture with [data/evidence-posture-taxonomy.md](data/evidence-posture-taxonomy.md) when creating new evidence logs
- assign a package/actionability readiness level using [data/research-readiness-gate.md](data/research-readiness-gate.md)
- scale visible fields using [data/output-surface-matrix.md](data/output-surface-matrix.md), so `quick_map` remains light without dropping required discipline
- include `stale_after`, `must_refresh_if` or equivalent refresh conditions
- run the `critical_interaction_step` before handoff: decide whether this
  workflow needs blocking clarification, progressive follow-up, workflow
  handoff, follow-up answer continuation, or an explicit waiver
- end with 1-3 route-bound, object-specific progressive follow-up prompts when
  they can improve research boundary, evidence quality, readiness, thesis
  state, actionability boundary or next-route selection
- never silently omit the interaction step: if no question or handoff is useful,
  state `followup_prompt_mode=none` and a route-specific waiver reason
- downgrade conclusions when evidence quality is weak
- avoid autonomous trade instructions; use research actions only
- for buy, sell, add, trim, chase, dip-buying or event participation prompts,
  run [data/marginal-buyer-payoff-bridge.md](data/marginal-buyer-payoff-bridge.md)
  before actionability risk control, so the answer states the next marginal
  buyer or seller, payoff source, repricing trigger and priced-in status
- apply [data/actionability-risk-control.md](data/actionability-risk-control.md) before any participation, add, trim, chase or event-trade framing
- load [data/instrument-strategy-gate.md](data/instrument-strategy-gate.md) only when the user explicitly asks about options, short selling, hedges, pair trades, margin, leverage or other instruments

Onboarding and Help prompts are not formal research outputs. If the user sends
an empty first prompt, `hi Mira`, `你好 Mira`, `Mira mode`, `Mira help`, `怎么用
Mira`, `Mira 能做什么` or `start here`, return a concise [START_HERE.md](START_HERE.md)
summary before running research routing. If the user already gives a concrete
research task, skip onboarding and route the task normally.

## Lazy Loading Map

| task step | read only this first | load next only if needed |
| --- | --- | --- |
| Wake word / identity | [MIRA.md](MIRA.md) | [START_HERE.md](START_HERE.md) for user prompt examples |
| Onboarding / Help | [START_HERE.md](START_HERE.md) | [AGENT_QUICKSTART.md](AGENT_QUICKSTART.md) only for execution details |
| Mira self-update | run `scripts/mira_update.sh`; use `--help` only for options | [AGENT_QUICKSTART.md](AGENT_QUICKSTART.md) update section |
| Route selection (which loop/skill) | [data/routing-index.csv](data/routing-index.csv) — `task_mode` → one loop/skill | only the matched `primary_loop_or_skill` body |
| Any formal task | [data/interaction-kernel.md](data/interaction-kernel.md) | [loops/analysis-routing.md](loops/analysis-routing.md) for route detail, then selected loop |
| Intent intake / decision pressure | [loops/analysis-routing.md](loops/analysis-routing.md) Step 0 / 0.5 | [data/actionability-risk-control.md](data/actionability-risk-control.md) when decision pressure is medium/high |
| Question expansion | [data/question-expansion-lenses.md](data/question-expansion-lenses.md) | only when comparison, scale shift, trend or anomaly framing improves the current route |
| Live / time-sensitive market data | [data/live-data-source-policy.md](data/live-data-source-policy.md) | [data/public-source-targets.md](data/public-source-targets.md) Live Market Snapshot Targets and market default pack |
| Daily / weekly market briefing | [loops/market-briefing-loop.md](loops/market-briefing-loop.md) | [templates/market-briefing-package/](templates/market-briefing-package/) and live-data policy for current markets |
| Continue / save user view | [loops/view-continuity-loop.md](loops/view-continuity-loop.md) | `private/research/<OBJECT>/` and `private/views/view-register.csv` only when relevant |
| First-pass single equity | [loops/research-loop.md](loops/research-loop.md) | thesis horizon, framework and overlay references |
| Research report interpretation | [skills/research-report-interpretation/SKILL.md](skills/research-report-interpretation/SKILL.md) | [data/ingestion-layer.md](data/ingestion-layer.md), [templates/research-report-interpretation-package/](templates/research-report-interpretation-package/) and restricted source note when the report is user-provided, paid or licensed |
| Thesis update / expectation change | [loops/thesis-update-loop.md](loops/thesis-update-loop.md) | thesis ledger, expectation map and decision-log templates |
| Event or earnings delta | [loops/event-delta-loop.md](loops/event-delta-loop.md) | earnings skill and event-delta template |
| SEC fact supplement | [skills/sec-filing-analysis/SKILL.md](skills/sec-filing-analysis/SKILL.md) | [templates/sec-supplement-source-note.csv](templates/sec-supplement-source-note.csv) |
| SEC filing deep dive | [skills/sec-filing-analysis/SKILL.md](skills/sec-filing-analysis/SKILL.md) | [templates/sec-filing-analysis-package/](templates/sec-filing-analysis-package/) |
| PM / research book review | [loops/portfolio-review-loop.md](loops/portfolio-review-loop.md) | portfolio register template and research index |
| Single position review | [loops/position-review-loop.md](loops/position-review-loop.md) | [templates/portfolio-system/position-review.md](templates/portfolio-system/position-review.md) and position register |
| Real portfolio construction review | [loops/portfolio-construction-review-loop.md](loops/portfolio-construction-review-loop.md) | portfolio exposure review and position register |
| Decision quality review | [loops/decision-quality-review-loop.md](loops/decision-quality-review-loop.md) | postmortem and thesis scorecard |
| Source routing | [data/source-taxonomy.md](data/source-taxonomy.md) | [data/source-coverage-matrix.csv](data/source-coverage-matrix.csv) |
| Market default pack (after `market_scope` is set) | [data/market-default-packs.csv](data/market-default-packs.csv) | [data/public-source-targets.md](data/public-source-targets.md) Market Default Packs |
| Data / tool ingestion | [data/ingestion-layer.md](data/ingestion-layer.md) | [templates/ingestion-layer/](templates/ingestion-layer/) when retaining user material, public API output, vendor data or portfolio exports |
| Evidence logging | [data/evidence-log-schema.md](data/evidence-log-schema.md) | [data/claim-taxonomy.md](data/claim-taxonomy.md) and [data/evidence-posture-taxonomy.md](data/evidence-posture-taxonomy.md) |
| Numeric / calculation gate | [skills/data-analysis-quality-gate/SKILL.md](skills/data-analysis-quality-gate/SKILL.md) | [templates/data-requirement-brief.md](templates/data-requirement-brief.md) and [templates/calculation-ledger.csv](templates/calculation-ledger.csv) |
| Marginal buyer / payoff lens | [data/marginal-buyer-payoff-bridge.md](data/marginal-buyer-payoff-bridge.md) | [data/actionability-risk-control.md](data/actionability-risk-control.md) and actionability bridge template when participation language appears |
| Actionability / participation risk control | [data/actionability-risk-control.md](data/actionability-risk-control.md) | [templates/actionability-system/actionability-bridge.md](templates/actionability-system/actionability-bridge.md), position or portfolio loop if real holdings are provided |
| Instrument strategy gate | [data/instrument-strategy-gate.md](data/instrument-strategy-gate.md) | [templates/actionability-system/instrument-strategy-gate.md](templates/actionability-system/instrument-strategy-gate.md), option chain / borrow / hedge data only if needed |
| Readiness / handoff | [data/research-readiness-gate.md](data/research-readiness-gate.md) | [data/handoff-contracts.md](data/handoff-contracts.md) and [templates/research-package/research-package-manifest.json](templates/research-package/research-package-manifest.json) |
| State/action tokens | [data/controlled-vocabulary.md](data/controlled-vocabulary.md) | task-specific template |
| Output surface / verbosity | [data/output-surface-matrix.md](data/output-surface-matrix.md) | [data/interaction-kernel.md](data/interaction-kernel.md) for non-negotiable checks |
| Final self-check | [templates/delivery-checklist.md](templates/delivery-checklist.md) | [data/output-surface-matrix.md](data/output-surface-matrix.md) when deciding what must be visible |

Do not load all `private/`, all `memory/`, all `skills/` or all cases at startup.
Retrieve only the files required by the routed task. If private and tracked
memory both exist for the same object, prefer the object-specific private state
for continuity and use tracked memory only as product context or examples.

## Depth Defaults

| depth_mode | use when | default cost control |
| --- | --- | --- |
| `quick_map` | fast read, early triage, unclear source boundary | read only the most relevant sources; output routing card, core judgment, source notes, refresh triggers and light progressive follow-up unless explicitly waived |
| `standard` | normal research package, earnings package, monitoring update, daily/weekly market briefing | load only routed loop / skill plus triggered references; output required package artifacts |
| `deep_dive` | long-term thesis, complex valuation, SEC deep dive, PM / methodology review | allow extra sources and artifacts only when each one improves evidence quality, actionability, or refresh conditions |

For visible output requirements by depth, use
[data/output-surface-matrix.md](data/output-surface-matrix.md). Do not make
short answers heavy by exposing every internal field, and do not make short
answers weak by dropping refresh, evidence or follow-up discipline.
The visible surfaces are only `quick_map`, `standard` and `deep_dive`;
`quick_answer` is an interaction shape that renders through one of those depth
surfaces.

If the user does not specify depth, infer it from the requested output. "看一下" defaults to `quick_map`; "研究 X" defaults to `standard`; "深挖 / 完整 / 方法验证 / PM review" defaults to `deep_dive`.

## Role Defaults

| user role | default path | default output |
| --- | --- | --- |
| Research analyst | `analysis-routing` -> `research-loop` or relevant skill | research package, evidence log, thesis objects if durable |
| Trader | `analysis-routing` -> thesis/event update -> actionability bridge | research action, invalidation, risk/reward frame, next catalyst |
| Portfolio manager | `portfolio-review-loop`, `position-review-loop` or `portfolio-construction-review-loop` depending on data | thesis board, position review, exposure/crowding notes, follow-up list |

If the user does not name a role, infer it from the requested output. A request for "能不能买", "能不能卖", "能不能动", "能不能冲", "目标价到了还能不能买", "跌下来能不能接", or a 预期差 question paired with an action ask ("预期差兑现了还能不能加/冲"), is trader-facing and must load the marginal buyer / payoff lens before the actionability risk-control policy; a bare 预期差 / variant-perception question ("预期差在哪") is research-facing — route to the variant-perception lens or thesis update with `decision_pressure` typically `none`; a request for "用期权怎么玩", "怎么对冲", "能不能做空", "pair trade" or "结构化一点" is trader-facing and must also load the instrument strategy gate; a request for "哪些 thesis 需要看" is PM-facing; a request for "review 我的仓位" is position-review-facing; a request for "研究 X" is analyst-facing.

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
- participation framing lacks confirmation and invalidation conditions
- instrument framing lacks objective, risk budget, access, data status or named failure modes
- the case is past `stale_after` and the user wants live use
- a live-use answer cannot establish `quote_time` / `publish_time` or source
  freshness for the market-pricing claim
- facts, inferences and judgments cannot be separated
- `readiness_level` cannot be upgraded past `working_view` without resolving named evidence, calculation or freshness gaps
- the user asks for position-size or portfolio conclusions without holdings, weights, mandate or risk budget
- an actionability, position-review or portfolio task did not emit `decision_pressure`, or emitted medium/high pressure without a disconfirmation check
- the dominant variable is unknowable now and deeper research will not change the conclusion (`irreducible_uncertainty`)

When stopped, return `source_gap`, `watch_only`, `no_action`, `needs_refresh` or `irreducible_uncertainty` instead of forcing a stronger conclusion. Use [data/controlled-vocabulary.md](data/controlled-vocabulary.md) for machine-facing state/action tokens.
