# Portfolio Review Loop

`portfolio-review-loop` is for PM-facing review of multiple Mira theses.

It is not a portfolio management system and does not produce trade orders. It turns single-name thesis objects into a book-level research view: what is active, stale, crowded, correlated, over-dependent on one theme, or missing follow-up.

If the user provides real holdings, weights, cost basis, mandate or risk budget, first decide whether the task should use:

- [position-review-loop.md](position-review-loop.md) for one position
- [portfolio-construction-review-loop.md](portfolio-construction-review-loop.md) for a real or mixed portfolio

Keep this loop for research-book reviews when real position data is absent or intentionally out of scope.

## Loop Input

- `book_scope`
- `research_objects`
- `review_date`
- `market_scope`
- `portfolio_context`
  optional; use only if the user provides it; if it contains real holdings or weights, consider `portfolio-construction-review-loop`
- `constraints`
  optional; examples: liquidity, mandate, risk budget, no live positions

## States

### `define-book`

Define the review boundary:

- active thesis set
- watchlist set
- excluded objects
- review date
- whether this is research-only or tied to a user-provided portfolio context

### `load-thesis-index`

Read the private thesis index first when it exists and the task is tied to the
user's prior views:

- `private/views/view-register.csv`
- `private/research/INDEX.md`, if the user maintains one

Use [../memory/research/INDEX.md](../memory/research/INDEX.md) only as product
context, a public example, or a fallback when no private research state exists.

Only load individual thesis ledgers when the index is insufficient, stale, or the object is part of the current review set.

Before using the index as a PM view, reconcile each included row against its primary thesis ledger or case package:

- state token matches [../data/controlled-vocabulary.md](../data/controlled-vocabulary.md)
- stale status is consistent with the referenced ledger/case
- actionability token is controlled vocabulary, with any nuance in notes
- event-based stale conditions are marked `needs_refresh` or `stale` when the event has already occurred

### `classify-exposures`

Classify each thesis by:

- theme
- horizon
- thesis state
- conviction
- actionability
- next catalyst
- stale status
- primary risk driver
- evidence quality

If real portfolio positions are not provided, use `research_exposure_only`.

### `detect-clusters`

Identify book-level risks:

- single theme concentration
- same catalyst across multiple objects
- common macro factor
- common funding/liquidity risk
- same supplier/customer chain
- crowded narrative or consensus proxy overlap

Do not infer position size unless the user provides it.

### `prioritize-follow-up`

Rank research maintenance by:

- stale or near-stale thesis
- high-conviction thesis with weak evidence
- near catalyst
- high actionability but missing valuation anchor
- contradicted or unresolved evidence
- missing postmortem after outcome

### `package`

Output a PM-facing review:

- `portfolio_register.csv` or updated thesis index
- book-level exposure notes
- stale thesis list
- catalyst calendar
- follow-up queue
- actionability boundary

Run `python3 scripts/validate_repo.py` after updating tracked [../memory/research/INDEX.md](../memory/research/INDEX.md), because the validator checks index state/action tokens and date-like stale cells.

Do not run repo validation solely because user-private `private/` state changed.

## Exit Criteria

- Every included thesis has a state, horizon, stale condition and primary reference.
- Any cluster or concentration claim is tied to listed objects.
- Research actions remain separate from trade instructions.
- If real position data is provided, routing either remains explicitly research-only or escalates to the position/portfolio construction loops.
- Stale or source-gap items are marked before any stronger conclusion.
- Follow-up list is sorted by research urgency.
- Step 4.5 critical interaction asks one natural-language question that chooses the next review object, missing portfolio context, or follow-up queue priority.

## Stop Rules

- If no thesis index or thesis ledgers exist, create a draft register from available case files and mark confidence `low`.
- If the user asks for portfolio advice without providing positions or mandate, return a research-only view and ask for the missing portfolio context before any position-level conclusion.
- If evidence is stale, use `needs_refresh` instead of upgrading conviction.
