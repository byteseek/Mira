# Mira Routing Card

**One-line assumption bar (standard depth):** Reading this as a first-pass single-equity research package on AAPL, US listing, directional-to-medium-term horizon, as of 2026-06-05, with no live network/market data available this turn. Correct me if the horizon or scope is off.

| field | value |
| --- | --- |
| `interaction_mode` | `routed_research` |
| `primary_intent` | first-pass single-equity research package on AAPL |
| `secondary_intents` | none stated |
| `execution_order` | single intent |
| `scope_confirmation_required` | no |
| `task_mode` | `first_pass_research` |
| `research_object` | `single_equity` — Apple Inc. (AAPL) |
| `market_scope` | US equities (`listing_market` = US, `price_discovery_venue` = NASDAQ) |
| `time_boundary` | `2Q_8Q_or_FY1_FY2` → `medium_term_revision` (default for "standard research"; see follow-up) |
| `output_language` | `en` (matches your message) |
| `evidence_languages` | `[en]` |
| `depth_mode` | `standard` |
| `source_budget` | constrained: **no live access this turn**; relying on the prior tracked case `cases/aapl-2026-04/` (L1 filing + L1 results + L5 market context) |
| `ingestion_route` | `none` (no new files/API/exports supplied) |
| `information_value` | `high` (a refreshed package would materially change the valuation/actionability conclusion) |
| `knowability_status` | `partially_knowable` — business-model and last-reported facts are knowable from the prior case; **current price, valuation multiple, and consensus revisions are `unknowable_now` without live data** |
| `depth_override_reason` | the dominant "as of today" variable (current price/valuation/estimate revisions) cannot be settled this turn, so the package is delivered at `working_view` / `needs_refresh`, not full `research_ready` |
| `decision_pressure` | `none` (research request, no buy/add/trim/chase framing) |
| `framing_risk` | `none` |
| `disconfirmation_required` | no |
| `quant_dependency` | `high` (valuation, growth, margin) → `calculation_gate` = `required` but **`calculation_gap`**: live inputs unavailable this turn |
| `private_state_action` | `waive` (no prior user view referenced; no save requested) |
| `routing_carryover` | `none` (fresh object this session) |
| `primary_skill_or_loop` | `loops/research-loop.md` → `skills/equity-research-core/` |
| `horizon_bucket` | `medium_term_revision` |
| `selected_framework` | `large-mega` |
| `framework_basis` | mega-cap; price set by institutional allocation, multi-quarter earnings path, discount rate, capital return — single events only matter if they reshape the multi-year cash-flow curve |
| `framework_mismatch_risk` | treating a single product-cycle/event read (e.g. foldable timing) as if it rewrites the long-term curve, when for AAPL it is marginal unless it shifts the FY revision path |
| `selected_overlays` | `macro` (rates/discount-rate sensitivity), `supply-chain` (tariff/gross-margin) |
| `overlay_basis` | both are named risk vectors in the FY2025 10-K and affect the medium-term margin/valuation path |
| `selected_lenses` | `variant-perception` (core debate is expectations-vs-quality, not quality itself) |
| `routing_mismatch_risk` | mistaking a stale prior case for a live, decision-ready read |
| `readiness_level` | `needs_refresh` / `working_view` |
| `readiness_basis` | prior AAPL case is **past `stale_after`** (next results or 2026-07-13) and no live price/valuation/consensus is available; durable actionability blocked |
| `followup_prompt_mode` | `standard` |

---

# AAPL — Standard Research Package (working_view, needs_refresh)

> **Data-availability gate (read first).** I have no network or live market access this turn, and the workspace's prior AAPL case (`cases/aapl-2026-04/`, cutoff 2026-04-14, financials through fiscal Q1 2026) is **past its `stale_after`**. Per the contract's stop rules, I will not invent a current price, multiple, or consensus. This package is anchored to the **verified prior facts** and is delivered at `working_view` / `needs_refresh` — usable for framing the debate, **not** for live actionability.

## Facts (verified / disclosed, from tracked evidence log)

- **Business model:** Apple is an installed-base-driven hardware+services platform, not a single-product hardware company. Source: FY2025 Form 10-K (`L1`, verified, 2025-10-31). [`sec_apple_10k_2025`]
- **Last reported results (fiscal Q1 2026, ended 2025-12-27):** revenue ~$143.8B (+16% YoY), EPS $2.84 (+19% YoY), operating cash flow ~$54B; iPhone and Services both strong. Source: Apple newsroom Q1 FY2026 release (`L1`, disclosed, 2026-01-29). [`apple_q1_2026_results`]
- **Disclosed risk:** the FY2025 10-K cites tariffs and trade measures as possible supply-chain and gross-margin headwinds. Source: FY2025 10-K (`L1`, verified). [`sec_apple_10k_2025`]
- **Last logged market context (NOT current):** close, market cap, PE and 52-week range were captured at 2026-04-13 from FinanceCharts (`L5`, estimated). This is **stale** and must not be used as today's pricing. [`financecharts_aapl_summary`]

## Inferences

- Apple still meets the definition of a high-quality, capital-returning mega-cap platform: the Q1 FY2026 print shows the ecosystem (devices + Services) compounding rather than a one-off hardware spike.
- Because pricing is institutional-allocation-driven, the medium-term direction depends on the **FY revision path and discount rate**, not on any single product event. Foldable-iPhone timing or a discrete AI-feature launch matters only if it changes the multi-quarter revenue/margin curve.
- The unresolved debate is a **valuation/expectations** question (`variant-perception`), not a business-quality question: "is the quality already in the price?" — and that cannot be answered without current price + multiple + consensus revisions.

## Judgments

**J1 — Business quality remains intact as a mega-cap core asset.**
- `judgment_confidence`: `medium`
- `confidence_basis`: rests on `L1` filing + `L1` last results; both high-authority but the latest is the Q1 FY2026 print (older now).
- `base_rate_anchor`: established mega-cap platforms rarely see quality break in a single quarter absent a margin/Services shock.
- `reversal_condition`: next results show Services or gross-margin deterioration, or a material tariff/regulatory hit to the margin path.

**J2 — As-of-today actionability cannot be established (`no_action` / `needs_refresh`).**
- `judgment_confidence`: `high` (about the data gap itself, not a market call)
- `confidence_basis`: prior case is past `stale_after`; no live price, valuation anchor, or consensus revisions this turn → `calculation_gap` + `source_gap`.
- `reversal_condition`: a refresh supplying current price, a rebuilt base/bull/bear valuation table, and current consensus estimates would lift readiness toward `research_ready` / `actionable_with_caveats`.

## Valuation & Expectation Quant

- `current_valuation_anchor`: **`source_gap`** — no live multiple/price this turn.
- `calculation_gate`: `required` → **`calculation_gap`** (live inputs unavailable; not waived by choice, blocked by access).
- `base / bull / bear`: framed qualitatively only — base = quality compounder continues with no clear multiple-expansion edge; bull = stronger Services/iPhone revisions or risk-premium compression; bear = margin pressure, product-cycle disappointment, or multiple reset. **No numeric scenario math** without refreshed inputs.

## Refresh Conditions

- `stale_after`: this working view is stale immediately for live pricing; treat as superseded by Apple's **next quarterly results / guidance update**.
- `must_refresh_if`: (1) next earnings or guidance lands; (2) a current price, multiple and rebuilt valuation table become available; (3) current sell-side consensus / estimate-revision data becomes accessible; (4) a material tariff / gross-margin or capital-allocation policy change is disclosed.
- `kill_criteria` (for J1): confirmed Services or gross-margin deterioration in reported results, or a major regulatory/tariff hit that resets the margin path.

## Source Notes

- Evidence drawn from tracked golden case `cases/aapl-2026-04/evidence-log.csv` (claim-level). Highest-authority rows: `sec_apple_10k_2025` (L1), `apple_q1_2026_results` (L1). Market-context row `financecharts_aapl_summary` (L5) is **stale (2026-04-13)** and excluded from any current conclusion.
- No new sources ingested this turn; `ingestion_artifacts` = `waived`.

---

## Progressive Follow-Up

1. Should I refresh this into a live, decision-ready AAPL package by pulling current price, a rebuilt base/bull/bear valuation table, and current consensus estimates (requires network access next turn)?
   - route_binding: `data_tool_ingestion_gate` + `skills/data-analysis-quality-gate` + `calculation_gate`
   - object_anchor: AAPL current PE / market cap vs. fiscal Q1 FY2026 results and FY revision path
   - decision_impact: `readiness_level` (`needs_refresh` → `research_ready` / `actionable_with_caveats`) and `calculation_depth`

2. Is your horizon the **next 1–2 quarters' revision path** (FY1/FY2 estimate moves) or the **multi-year platform/cash-flow thesis (>1y)**?
   - route_binding: `time_boundary` + `thesis-horizon-routing` (+ `long-term-thesis-loop` if >1y)
   - object_anchor: AAPL Services/iPhone revision cadence vs. long-run installed-base monetization and capital return
   - decision_impact: `boundary` + `selected_framework` weighting and `evidence_path`

3. Of the named risks, which should the package stress-test first — **tariff/gross-margin** (supply-chain overlay), **product-cycle/AI execution** (e.g. foldable timing), or **multiple reset** (macro/discount-rate overlay)?
   - route_binding: `overlay-routing` (`supply-chain` / `macro`) + `variant-perception` lens
   - object_anchor: AAPL gross-margin sensitivity and Services durability as the disconfirming variables
   - decision_impact: `evidence_path` + `refresh_condition` (sharpens `kill_criteria`)
