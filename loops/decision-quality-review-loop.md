# Decision Quality Review Loop

`decision-quality-review-loop` reviews the quality of prior research or portfolio decisions after an outcome window.

It is not a performance report by itself. Its goal is to separate thesis correctness, process quality, timing, market pricing, beta, luck and execution constraints.

## Loop Input

- `decision_id`
- `research_object`
- `review_date`
- `original_decision_date`
- `outcome_window`
- `original_thesis_refs`
- `outcome_data`
  required for outcome claims; examples: price return, relative return, financial result, event result, thesis variable realization
- `position_context`
  optional; required for execution or position-size conclusions

## States

### `load-original-record`

Load:

- original thesis ledger
- expectation map
- decision log
- actionability bridge
- evidence log
- position review or portfolio review if relevant

Do not rewrite the original decision with hindsight. Record what was knowable at the original date.

### `define-outcome-window`

State:

- start and end date
- expected thesis validation event
- market benchmark or peer set if used
- relevant price, financial or operating outcomes
- unavailable data or calculation gaps

### `attribute-outcome`

Separate:

- thesis variable realization
- market beta
- sector or factor move
- multiple expansion or contraction
- estimate revision
- risk premium change
- timing
- execution constraint
- unrelated luck

If attribution depends on returns, peer comparison, factor movement or valuation math, run the quant dependency gate or mark `calculation_gap`.

### `score-decision-quality`

Assess:

- evidence quality at decision time
- reasoning quality
- claim weighting
- time horizon match
- valuation and expectation anchor
- disconfirming evidence handling
- sizing discipline if position context exists
- refresh discipline
- path-fit discipline: whether the original decision required enduring a cycle,
  whether that burden was stated, and whether the later outcome came from thesis
  validity, market beta, timing, or simply surviving the pain path
- stage discipline: whether the original setup was only `watch_only`, a valid
  `left_side_candidate`, or genuinely `confirmed_participation`

Use postmortem error categories from [../architecture/thesis-system.md](../architecture/thesis-system.md) and add a methodology update candidate when a process error is found.

### `package`

Output:

- `decision-quality-review.md`
- updated `postmortem.md` if the decision belongs to a thesis object
- updated `thesis-scorecard.csv` when confidence calibration changes
- methodology update candidate if needed

## Exit Criteria

- Original decision and outcome window are stated.
- Facts available then and facts known now are separated.
- Outcome attribution is supported or downgraded.
- Process error, market-pricing error and execution constraint are not conflated.
- Methodology changes trace to a specific failure mode.
- Step 4.5 critical interaction asks one natural-language question that selects the next methodology fix, missing outcome evidence, or follow-up review target.

## Stop Rules

- If original records are missing, create a reconstruction note and mark confidence `low`.
- If outcome data is missing, do not score decision quality beyond process audit.
- If the review depends on portfolio execution but no position context exists, do not infer execution quality.
