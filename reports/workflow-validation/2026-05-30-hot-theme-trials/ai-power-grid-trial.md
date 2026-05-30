# AI Power / Data-Center Grid Bottleneck Trial

- as_of: 2026-05-30
- task_mode: `methodology_review` + `industry_concept`
- research_object: AI power / data-center grid bottleneck
- market_scope: global theme, US-listed evidence first
- time_boundary: 2026-2028 setup, with current source boundary as of 2026-05-30
- primary_skill_or_loop: `industry-concept-analysis` with `macro-regime-analysis` overlay
- workflows_under_test: `analysis-routing`, `industry-concept-analysis`, `macro-regime-analysis`, `institutional-research-quality-gate`
- source_boundary: evidence rows in `evidence-log.csv`; no utility-level company memo yet
- output_status: compact trial note, not a full investment memo
- not_investment_advice: true

## Routing Result

This should not start as a single-equity memo. The right first pass is an industry/macro bottleneck map because the investable question is not "AI demand exists"; it is where power availability, interconnection, generation mix, grid capex and rate treatment create binding constraints or profit pools.

## One-Page Industry Map

| field | current trial view |
| --- | --- |
| one-line definition | Data-center AI load is becoming a localized electricity, grid and interconnection constraint rather than only a server/GPU deployment question. |
| first-order variable | speed and cost of deliverable power relative to data-center load commitments |
| core bottleneck | local grid connection, generation availability, transmission queue, cooling, permitting and who pays for network upgrades |
| profit-pool candidates | utilities with load growth and constructive rate base treatment; independent power/generation; electrical equipment; cooling; grid services; behind-the-meter or dedicated power providers |
| false-positive risk | assuming every utility, power producer or electrical equipment stock benefits equally from AI power demand |
| evidence needed before stock handoff | regional load queue, utility capex plan, allowed ROE/rate treatment, contracted data-center load, generation procurement, customer concentration and financing burden |
| likely route after map | split into `utility_rate_base`, `merchant_power`, `electrical_equipment`, `cooling`, and `data-center_operator_power_risk` subcases |

## Facts

- IEA source notes support the claim that AI and data centers are large enough to matter for electricity demand, but forecast ranges are scenario-dependent.
- Microsoft FY26 Q3 evidence supports the claim that AI/cloud infrastructure demand and capacity constraints remain live at hyperscaler level.
- EIA and regulatory source notes support keeping the analysis regional: load growth and grid constraint are not uniform across the US.

## Inferences

- The most useful first workflow branch is not "AI beneficiaries"; it is "where is power physically and economically deliverable?"
- Company-level work should come after a regional bottleneck map. Without that, single-name conclusions risk being a generic AI power basket.
- The best early evidence path is utility/regional data, not sell-side theme language.

## Trial Judgment

The theme passes the reality-basis gate but does not yet pass stock-level decision readiness.

Current state should be `watch / map-first`, not thesis upgrade. Mira can justify a focused research action: build a regional bottleneck and profit-pool map, then hand off only the strongest subsegments to single-equity research.

## Quality Gate

| gate | result |
| --- | --- |
| `reality_basis` | pass for theme-level bottleneck; source trail includes IEA/EIA/regulatory/company evidence |
| `first_order_variable` | pass after compression: deliverable power speed/cost, not broad AI demand |
| `decision_increment` | partial pass: supports research prioritization and stock-handoff design, not a buy/sell judgment |
| `disconfirmation_path` | partial pass: needs specific metrics such as interconnection queue easing, lower power procurement cost, weaker hyperscaler capex or utility commission pushback |

## Workflow Review

### What Worked

- `analysis-routing` correctly kept this out of single-equity research at the start.
- `industry-concept-analysis` forced the value-chain/profit-pool split.
- `institutional-research-quality-gate` improved the conclusion by downgrading "AI power winners" into a map-first research action.

### What Failed Or Is Missing

- The current evidence log is still too macro. It needs regional utility filings, interconnection queues and rate-case evidence before any stock-level conclusion.
- `macro-regime-analysis` needs a tighter template for "large load -> grid constraint -> allowed return / merchant price / equipment order" transmission.
- Source quality is good for theme selection but not yet sufficient for durable company-level conclusions.

## Proposed Workflow Patch Candidate

Add a lightweight `regional_bottleneck_check` to industry concept work when the theme depends on physical infrastructure.

Required fields:

- geography of constraint
- local demand source
- capacity/interconnection timeline
- who funds the bottleneck relief
- pricing or allowed-return mechanism
- company exposure purity
- disconfirmation metric

Do not adopt this patch yet. Trial it first on AI power, then later on another infrastructure theme.

## Next Work

1. Build the AI power regional map: PJM / Virginia, ERCOT, Georgia/Southeast, Arizona, Ireland/EU as candidates.
2. Create a company handoff list only after regional bottlenecks are mapped.
3. Review whether `regional_bottleneck_check` belongs in `industry-concept-analysis` or only as an overlay.

## Refresh Policy

- stale_after: 2026-06-30
- must_refresh_if:
  - hyperscaler capex guidance changes materially
  - EIA/IEA/FERC or grid-operator data changes load-growth framing
  - a major utility commission rejects data-center cost recovery
  - large data-center projects are delayed or cancelled due to power availability
  - regional power prices or interconnection queues move enough to change the bottleneck map

