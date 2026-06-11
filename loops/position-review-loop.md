# Position Review Loop

`position-review-loop` is for reviewing a user-provided real position against the current Mira thesis, evidence quality, price context and portfolio constraints.

It is not an autonomous trading system. It can produce position-management implications and review actions, but it must not generate orders, exact share quantities, or unconfirmed trade instructions.

## Loop Input

- `position_id`
- `research_object`
- `review_date`
- `market_scope`
- `time_boundary`
- `position_context`
  required for position-level conclusions; examples: current weight, cost basis, entry thesis, holding period, mandate, liquidity constraint, tax/accounting constraint
- `thesis_refs`
  thesis ledger, case package, expectation map, event delta or explicit source notes
- `portfolio_context`
  optional; use only if the user provides it
- `constraints`
  optional; examples: max single-name weight, risk budget, liquidity, no new capital, hedging unavailable

## States

### `define-position`

Define the review boundary:

- current holding or proposed holding
- position size if provided
- cost basis or entry price if provided
- original thesis and entry rationale
- review date
- whether this is research-only or tied to a user-provided real portfolio

If the user does not provide real position data, mark `position_data_status = no_position_data` and return research-only implications.

### `load-current-thesis`

Load the current private thesis package first when the position belongs to the
user's private book:

- thesis ledger
- expectation map
- latest event delta
- decision log
- actionability bridge
- evidence log or explicit source note

Default private locations:

- `private/research/<OBJECT>/thesis-ledger.md`
- `private/research/<OBJECT>/expectation-map.csv`
- `private/research/<OBJECT>/working-view.md`
- `private/portfolio/position-register.csv`

Use tracked `memory/research/<OBJECT>/` or case packages only as public product
context, examples, or fallback when private state does not exist.

If the thesis is stale, mark `position_review_action = needs_refresh` before making any stronger position-level judgment.

### `compare-thesis-to-price`

Separate:

- facts: current disclosure, price, valuation, event timing and position data
- inferences: what appears priced in, what changed since entry, what evidence strengthened or weakened
- judgments: whether position size still matches thesis quality, downside path and time boundary

For buy, sell, add, trim or exit questions, also run
[../data/marginal-buyer-payoff-bridge.md](../data/marginal-buyer-payoff-bridge.md)
before action implication. The position review must distinguish remaining
payoff source from position-size or risk-budget fit.

If valuation, return, drawdown, exposure, concentration or risk budget claims are material, run the quant dependency gate or mark `calculation_gap`.

### `size-vs-evidence-check`

Assess whether the position is aligned with:

- thesis state and evidence quality
- conviction and disconfirming evidence
- downside path and invalidation conditions
- liquidity and volatility
- catalyst timing
- portfolio concentration
- correlation or duplicate exposure

Use [../data/controlled-vocabulary.md](../data/controlled-vocabulary.md) `position_sizing_context` tokens. Do not invent new machine-facing sizing labels.

### `action-implication`

Return a research-bound action implication:

- `research_only`
- `hold_review`
- `add_only_if_confirmed`
- `trim_review`
- `exit_review`
- `risk_cap_review`
- `needs_refresh`
- `no_action`

This is not an executed trade. If the user asks for exact trade execution, state that Mira requires explicit portfolio constraints, user confirmation and any applicable PMS or brokerage rules.

### `package`

Output:

- `position-review.md`
- updated `position-register.csv` if maintaining a portfolio file
- updated `decision-log.csv` if a research action changed
- required research follow-up list and refresh triggers

## Exit Criteria

- `decision_pressure` is emitted (even if `none`), with a disconfirmation check when medium/high, per `analysis-routing.md` Step 0.5 (this route is `load_gate=on_hit_decision_support`).
- Buy/sell/add/trim prompts include the marginal buyer / payoff bridge before
  position-management implication.
- Real position data is either provided or explicitly marked `no_position_data`.
- Thesis state, stale status and source trail are stated before action implication.
- Any sizing or risk conclusion is tied to position data and, when numeric, to a reproducible calculation.
- Position-management implication stays separate from trade execution.
- `stale_after` and `must_refresh_if` are present.
- Step 4.5 critical interaction asks one natural-language question that obtains the missing position context, verifies the disconfirming variable, or confirms the next research action.

## Stop Rules

- If no position data is provided, do not make position-size conclusions; return research-only implications.
- If the thesis is stale, return `needs_refresh` before `hold_review`, `add_only_if_confirmed`, `trim_review` or `exit_review`.
- If the user asks for precise order size without constraints, ask for mandate, current weight, risk limit, liquidity and confirmation workflow.
- If evidence and position data conflict but sources are weak, downgrade to `risk_cap_review` or `needs_refresh`.
