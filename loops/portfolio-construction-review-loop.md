# Portfolio Construction Review Loop

`portfolio-construction-review-loop` reviews a user-provided portfolio or research book for concentration, duplicated bets, factor/theme overlap, catalyst crowding and thesis conflicts.

It does not replace a PMS, risk model or investment committee. It produces research-backed portfolio construction notes and position-review priorities.

## Loop Input

- `book_scope`
- `review_date`
- `market_scope`
- `portfolio_context`
  required for real portfolio conclusions; examples: holdings, weights, cash, mandate, risk budget, benchmark, liquidity limits
- `research_objects`
- `thesis_refs`
- `constraints`
  optional; examples: max single-name weight, max theme exposure, no derivatives, tax constraints

## States

### `define-book`

Classify the review:

- `research_book`: no real positions; use thesis exposure only
- `real_portfolio`: holdings or weights are provided
- `mixed`: some real holdings plus watchlist objects

If the whole book is `research_book` and the user is asking for a PM-style
multi-thesis review rather than structure/exposure analysis, reroute to
`portfolio_review` ([portfolio-review-loop.md](portfolio-review-loop.md))
instead of continuing here.

If holdings or weights are absent, do not infer position size.

### `load-thesis-and-position-registers`

Read:

- private thesis index first when user continuity matters:
  `private/views/view-register.csv` or `private/research/INDEX.md`
- private position register if provided, usually under `private/portfolio/`
- private portfolio register if provided, usually under `private/portfolio/`
- [../memory/research/INDEX.md](../memory/research/INDEX.md) only as product context, public example or fallback
- thesis ledgers only when the index is stale, insufficient or in the review set

Reconcile state, stale status and action tokens against [../data/controlled-vocabulary.md](../data/controlled-vocabulary.md).

### `map-exposures`

Classify each object by:

- theme
- factor
- macro driver
- valuation regime
- catalyst
- liquidity
- thesis state
- evidence quality
- position weight if provided
- position sizing context if provided

### `detect-portfolio-risks`

Identify:

- single-name concentration
- theme concentration
- factor concentration
- macro dependency
- same-catalyst crowding
- duplicate exposure
- liquidity concentration
- thesis conflict
- stale high-impact positions
- high conviction with weak evidence

Any concentration claim must list the exact objects and, if numeric, the calculation basis.

### `prioritize-position-reviews`

Rank follow-up by:

- stale or near-stale thesis
- large position with weak evidence
- large position near catalyst
- duplicate exposure without clear reason
- contradicted thesis
- missing valuation anchor
- missing postmortem
- unresolved source or calculation gap

### `package`

Output:

- `portfolio-construction-review.md`
- `portfolio-exposure-review.csv`
- position-review queue
- stale thesis list
- catalyst calendar
- concentration and duplicate-bet notes
- actionability boundary

## Exit Criteria

- `decision_pressure` is emitted (even if `none`), with a disconfirmation check when medium/high, per `analysis-routing.md` Step 0.5 (this route is `load_gate=on_hit_decision_support`).
- Review scope is classified as `research_book`, `real_portfolio` or `mixed`.
- Every portfolio-level claim lists the objects behind it.
- Real portfolio conclusions use user-provided weights or explicitly state `no_position_data`.
- Numeric concentration or risk claims have a calculation note or are marked `calculation_gap`.
- Follow-up queue is sorted by research or portfolio-review urgency.

## Stop Rules

- If the user asks for portfolio advice without holdings, mandate or risk budget, return a research-book view only.
- If a material holding has stale thesis data, mark it `needs_refresh` before drawing a strong conclusion.
- If multiple holdings share a hidden exposure but evidence is weak, mark as `source_gap` and schedule follow-up.
