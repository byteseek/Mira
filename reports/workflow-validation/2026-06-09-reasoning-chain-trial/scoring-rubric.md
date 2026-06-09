# Scoring Rubric (pre-registered)

- trial: reasoning-chain optimization, multi-arm ablation
- locked: 2026-06-09, **before** any treatment card is written and before any run.
- principle: score **reasoning quality, not the final direction**. A model that pattern-matches
  "I recognize this case → downgrade" can get the direction right while scoring low here.

## Fixed prompt (identical across all arms and cases)

> 你是一名研究分析师。仅依据所提供的 research packet 事实和你当前加载的研究协议，对该研究对象做一次 `first_pass_research` 判断。给出：核心结论；它现在是 `actionable` 还是 `watch_only`（写出具体 action state）；关键依据；**市场共识是什么、你哪里可能不同**；**什么单一证据会推翻你的判断**；刷新 / 失效条件。只用 packet 里的事实；缺的当作 `source_gap`，不要编造，也不要假设公司后续结果。

The agent additionally receives: the arm's assembled Mira contract + one packet (`case_a/b/c`). Nothing else.

## Dimensions

### Three KEY dimensions (decisive; reasoning-focused)

**`consensus_proxy_quality`** — did it characterize what the market expects, concretely?
- 1 — no consensus stated, or only "market is bullish/optimistic" with no referent.
- 2 — asserts a consensus exists but ties it to no proxy (sell-side / positioning / price-implied) and no number.
- 3 — states a consensus qualitatively, tied to ≥1 named proxy, but not to a specific number/expectation.
- 4 — states a **specific** consensus expectation (a number or event the market is implicitly forecasting) grounded in the packet facts.
- 5 — triangulates ≥2 proxies into a concrete, falsifiable statement of what the market is paying for, and names the **specific variable** the view diverges on.

**`falsification_point`** — did it name the single observation that would flip the view?
- 1 — none.
- 2 — vague "if fundamentals deteriorate", no variable or threshold.
- 3 — names a relevant variable to watch, but no direction/threshold that flips the conclusion.
- 4 — names a specific observable (variable + direction) that would invalidate the thesis, tied to a refresh/kill condition.
- 5 — specific, threshold-/event-bound observable **and** states which way the conclusion moves, wired to `must_refresh_if` / `kill_criteria` / `reversal_condition`.

**`downgrade_timing`** — right action state, justified from the dated facts? (for `case_c`, "correctly does NOT over-downgrade")
- 1 — wrong action state (actionable on a/b; broken-thesis downgrade on c) with no defensible basis.
- 2 — right-ish direction but justification not derivable from the dated facts ("these stories end badly").
- 3 — defensible action state, loose justification (recites bullish facts, hand-waves the caution).
- 4 — **correct** action state with a basis traceable to the dated facts.
  - a/b correct = `watch_only` pending normalized demand / value capture.
  - c correct = `no_action` / `watch` quality-compounder (see `case_c-answer-key.md`).
- 5 — correct action state + explicitly derives it from the specific at-cutoff facts (shock-attribution + margin/inventory/valuation heat for a/b; durable non-shock platform + priced-in for c) + states what later evidence flips it.

### Eight reused dimensions (no-regression guards)

Score 1–5 using `cases/*/workflow-scorecard.csv` as anchor reference:
`source_quality`, `lens_coverage`, `conflict_detection`, `valuation_expectations`,
`refresh_conditions`, `decision_impact`, `cost_efficiency`, `institutional_readiness`.

## Pre-registered win rule

An intervention/arm is kept only if **all** hold:

1. **No regression**: treatment **median ≥ control median** on every one of the 11 dimensions (3 key + 8 reused), over `case_a` + `case_b`.
2. **Real gain**: **≥1 of the 3 KEY dims improves by ≥1 point in median** (treatment vs control), over `case_a` + `case_b`.
3. **Floor**: treatment **worst-case (min across runs)** on each KEY dim is **≥ control's median** for that dim — a high-variance treatment that sometimes reasons worse is rejected.
4. **Reverse control**: on `case_c`, treatment produces **no erroneous downgrade** (per `case_c-answer-key.md`) in **any** run.
5. **Harness regression red lines** (from the plan): `evals/BASELINE` stays 12/12; net hot-path field count ≤ control.

Any failure → that arm/intervention is **reverted**, and the negative result is recorded in `methodology-delta.md`.

## Attribution (because all three ship together)

- Arm 1 / 2 / 3 (single interventions) vs Arm 0 isolate each intervention's main effect on the KEY dims.
- Arm 4 (all three) is the shipped combination; compare to the best single arm to check for interaction / redundancy.

## Grader protocol (blind)

- Grader receives each transcript labeled only by an opaque `run_id`; the **arm and intervention are stripped** (mapping held in `arm-manifest.lock.csv`, not shown to the grader).
- Grader scores all 11 dims by the anchors above; for the 3 KEY dims, a second blind pass (shuffled order) checks intra-rater consistency. Material disagreement (≥2 points) is re-read and reconciled with a one-line note.
- The grader is instructed to score the **reasoning shown**, and to explicitly **not** reward a correct final action that lacks a derived consensus, mechanism, or falsification point.

## N and matrix

Per `arm-manifest.protocol.csv`: `case_a`/`case_b` run Arm 0–4; `case_c` runs Arm 0/1/2/4; N = 2–3 per cell.
