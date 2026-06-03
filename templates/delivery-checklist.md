# Mira Delivery Checklist

Use this before handing off a formal research output.

## Required

- [ ] The task was routed through `analysis-routing` or the route was explicitly waived with a reason.
- [ ] `research_object`, `market_scope`, `time_boundary` and source boundary are stated.
- [ ] Facts, inferences and judgments are separated.
- [ ] Every durable conclusion has an evidence-log row or explicit source note.
- [ ] Numeric conclusions were routed through `data-analysis-quality-gate` or explicitly waived with a reason.
- [ ] Derived calculations have a `calculation-ledger` row or explicit formula note.
- [ ] Numeric claims that affect thesis/actionability were cross-checked, or downgraded to `calculation_gap`, `source_gap`, `watch_only`, `needs_refresh` or equivalent.
- [ ] No unresolved `{{ placeholder }}` remains.
- [ ] `stale_after`, `must_refresh_if` or equivalent refresh condition is present.
- [ ] Weak evidence is downgraded to `source_gap`, `watch_only`, `needs_refresh` or equivalent.
- [ ] Output states `not_investment_advice` or an equivalent boundary.

## Single-Equity Additions

- [ ] `horizon_bucket`, `selected_framework` and `selected_overlays` are stated.
- [ ] Framework mismatch risk is stated.
- [ ] Valuation and expectation quant is present or explicitly waived.
- [ ] Actionability bridge is present or explicitly waived.
- [ ] Actionability uses only [../data/controlled-vocabulary.md](../data/controlled-vocabulary.md) research-action tokens.

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
