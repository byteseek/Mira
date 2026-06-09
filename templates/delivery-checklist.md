# Mira Delivery Checklist

Use this before handing off a formal research output.

## Required

- [ ] Interaction kernel passed: the non-negotiable checks in `data/interaction-kernel.md` ran before choosing visible output.
- [ ] Final strong-habit gate passed: evidence strength, refresh condition and progressive follow-up were all checked together before handoff.
- [ ] Visible fields were scaled using `data/output-surface-matrix.md`; short outputs did not expose unnecessary package fields or omit required discipline.
- [ ] The task was routed through `analysis-routing` or the route was explicitly waived with a reason.
- [ ] Intent intake ran: compound prompts were split into `primary_intent` / `secondary_intents`, running assumptions were declared, and the routing card was scaled to `depth_mode`.
- [ ] On actionability / position / portfolio routes, `decision_pressure` is emitted (even if `none`), with a disconfirmation check when pressure is medium/high.
- [ ] `research_object`, `market_scope`, `time_boundary` and source boundary are stated.
- [ ] Time-sensitive market answers ran `data/live-data-source-policy.md`: fresh
  lookup/search was performed or explicitly waived as a stable definition;
  `quote_time` / `publish_time`, `live_freshness_status`,
  `cross_check_status` and `stale_after` are present or the answer is
  downgraded.
- [ ] `output_language` is stated on formal output (defaults to `interaction_language`; `quick_answer` may inherit implicitly); `evidence_languages` is declared when evidence spans more than one language.
- [ ] After `market_scope` is set, the matching `data/market-default-packs.csv` pack (sources, calendar, currency, accounting standard, translation caveats) was applied; local-disclosure gaps were downgraded per `coverage_gap_action`.
- [ ] Localization: human-facing labels are rendered in `output_language` via `data/localization-glossary.csv`; machine tokens, schema field names and file names were NOT translated.
- [ ] `depth_mode` is stated, and artifacts match `quick_map`, `standard` or `deep_dive`.
- [ ] Information value and knowability were checked; if a dominant variable is unknowable, depth was overridden and `irreducible_uncertainty` / `unknowable_now` stated instead of over-researching.
- [ ] Facts, inferences and judgments are separated.
- [ ] Each material judgment states `judgment_confidence`, `confidence_basis` and `reversal_condition` (and `base_rate_anchor` when a reference class applies).
- [ ] Every durable conclusion has an evidence-log row or explicit source note.
- [ ] Newly supplied files, API pulls, vendor exports or portfolio data have an
  ingestion artifact or an explicit ingestion waiver.
- [ ] New evidence logs use the v1.2 schema (posture fields + `source_language` / `translation_basis`), or explicitly state why a legacy v1 / v1.1 schema is being used.
- [ ] Non-English primary sources record `source_language` and `translation_basis`; judgment-bearing translated quotes keep `original_excerpt=` in `notes` (claim_text stays a single verifiable claim).
- [ ] Formal case packages include `research-package-manifest.json` with hero artifacts, support artifacts, readiness, source scope and refresh conditions.
- [ ] `readiness_level`, `readiness_basis` and `blocking_gaps` are stated before any actionability conclusion.
- [ ] Numeric conclusions were routed through `data-analysis-quality-gate` or explicitly waived with a reason.
- [ ] Derived calculations have a `calculation-ledger` row or explicit formula note.
- [ ] Numeric claims that affect thesis/actionability were cross-checked, or downgraded to `calculation_gap`, `source_gap`, `watch_only`, `needs_refresh` or equivalent.
- [ ] No unresolved `{{ placeholder }}` remains.
- [ ] `stale_after`, `must_refresh_if` or equivalent refresh condition is present.
- [ ] Progressive follow-up is complete: either 1-3 route-bound, object-specific questions are present, or `followup_prompt_mode=none` has a concrete waiver reason.
- [ ] Progressive follow-up has rung progression: standard/deep_dive/decision-grade outputs do not stop at boundary/data hygiene when pricing variables, consensus, falsification or next-route questions are available.
- [ ] For `quick_map`, follow-up was not silently omitted: 1 light follow-up is present unless the user explicitly requested no follow-up, the task is mechanical, or the next step is uniquely determined.
- [ ] Weak evidence is downgraded to `source_gap`, `watch_only`, `needs_refresh` or equivalent.
- [ ] Cross-skill handoffs preserve source IDs, evidence categories, freshness/conflict status and named gaps.
- [ ] Output states `not_investment_advice` or an equivalent boundary.

## Single-Equity Additions

- [ ] `horizon_bucket`, `selected_framework` and `selected_overlays` are stated.
- [ ] Framework mismatch risk is stated.
- [ ] Valuation and expectation quant is present or explicitly waived.
- [ ] Actionability bridge is present or explicitly waived.
- [ ] Actionability uses only [../data/controlled-vocabulary.md](../data/controlled-vocabulary.md) research-action tokens.

## SEC Additions

- [ ] SEC use is routed as `sec_supplement` or `sec_filing_deep_dive`.
- [ ] Filing claims record CIK, accession number, form type, filing date, report period and section or exhibit.
- [ ] Companyfacts claims record CIK, taxonomy, tag, unit, period and frame if available.
- [ ] Missing filing sections or unavailable 10-Q/10-K details are marked as `source_gap`.
- [ ] Filing conflicts with release, market data or prior Mira work are escalated to filing deep dive, event delta or thesis update.

## Thesis System Additions

- [ ] Thesis ledger has current thesis, supporting claims, key assumptions, variant view, disconfirming evidence and state.
- [ ] Expectation map states consensus proxy, Mira view, price-in status and next check.
- [ ] Decision log records basis, risk and required follow-up.
- [ ] Event deltas state pre-event setup, actual disclosure, delta vs expectation and thesis impact.
- [ ] Postmortem is required when an outcome invalidates a prior judgment or exposes a process error.

## PM / Portfolio Additions

- [ ] Thesis register or portfolio register is updated when multiple research objects are discussed.
- [ ] Theme, factor, liquidity, macro or single-name concentration is called out when relevant.
- [ ] No research action is represented as an executed trade or portfolio instruction.
- [ ] Position-level conclusions use user-provided holdings, weights, cost basis or constraints; otherwise `position_data_status` is `no_position_data` or `research_only`.
- [ ] `position_review_action` and `position_sizing_context` use controlled-vocabulary tokens.
- [ ] Numeric exposure, concentration, return or risk claims have a calculation note or are downgraded to `calculation_gap`.
- [ ] Duplicate-bet or concentration claims list the exact objects behind the claim.
- [ ] Decision-quality reviews separate what was knowable at the original decision date from hindsight evidence.
