# Research Readiness Gate

Mira separates whether a research package is complete from whether its
conclusion is usable for action.

Use this gate before assigning a research action, publishing a package, or
carrying a conclusion into another loop.

## Readiness Levels

| readiness_level | meaning | minimum bar |
| --- | --- | --- |
| `draft` | Work in progress. Useful for scoping, not conclusion-bearing. | Research object, time boundary and source plan are clear. |
| `working_view` | A provisional view for discussion or follow-up. | Material claims are logged; weak evidence is labeled; refresh condition exists. |
| `research_ready` | A durable research package for internal use. | Durable conclusions tie to evidence; quant gate is satisfied or waived with downgrade; conflicts are handled. |
| `actionable_with_caveats` | Research can inform a watch, event setup or risk context. | Current evidence, valuation or expectation anchor, invalidation path and risk caveats are explicit. |
| `watch_only` | Interesting but not enough for actionability. | Source, calculation, valuation, freshness or thesis gap prevents stronger action. |
| `not_actionable` | Do not use for action. | Core evidence is missing, stale, contradicted, unsupported, or outside the requested time boundary. |
| `needs_refresh` | Prior work may be useful but is stale for the current use. | Refresh triggers are known and must be checked before reuse. |

## Required Checks

Before upgrading above `working_view`, record:

- `research_object`
- `market_scope`
- `time_boundary`
- `source_scope`
- `evidence_log_status`
- `quant_gate_status`
- `readiness_level`
- `readiness_basis`
- `blocking_gaps`
- `stale_after`
- `must_refresh_if`

## Blocking Gaps

Default to `watch_only`, `not_actionable` or `needs_refresh` when any material
conclusion depends on:

- unsupported `assumption`, `inference`, `estimate` or `weak_signal`
- missing calculation ledger for a material derived number
- unresolved source conflict
- stale market data, filings, guidance, estimate revisions or macro releases
- unclear consensus proxy or valuation anchor for an actionability claim
- left-side participation claim without a named reversal variable, observation
  window, further-drawdown test and invalidation path
- thesis requiring cycle endurance without a path-fit note, observable refresh
  variables and evidence for waiting through the cycle
- market pricing treated as fundamental validation

## Handoff Rule

When a package feeds another loop or skill, pass the `readiness_level` and
`blocking_gaps` with the handoff. Downstream work must not upgrade readiness
unless it resolves the specific gaps.
