# Blind Packet Build Log

- trial: reasoning-chain optimization, multi-arm ablation
- build_date: 2026-06-09
- purpose: document how `case_a/b/c` blind packets were sanitized from the source cases,
  so a reviewer can confirm there is **no post-cutoff data and no answer/verdict leakage**.
- packets graded against: `cases/pton-.../failure-backtest.md` (case_a), `cases/tdoc-.../failure-backtest.md` (case_b), `case_c-answer-key.md` (case_c). **Graders see answer keys; test-blind generation agents never do.**

## Two leakage channels (handled separately)

1. **Framing / verdict leakage** — the source files are explicitly retrospective
   (`failure-backtest`, `postmortem`, `collapse`, `impairment`, `would downgrade`,
   `hardware acquisition engine broke`, `Postmortem severity evidence`, etc.). This is the
   strongest tell and is **fully removable**: every packet strips the `notes` column, all
   retrospective lexicon, and all post-cutoff rows.
2. **Identity leakage** — these are famous cases; a knowledgeable model may still infer the
   company from the facts themselves. Anonymization only **partially** mitigates this. It is
   **not** relied on alone — see "Why identity leakage does not sink the experiment" below.

## What was stripped (all cases)

- ticker, company name, product/brand names (kept only a generic business descriptor)
- all URLs, SEC CIK numbers, `source_id`s, file paths
- the `notes` column (carried retrospective/verdict language)
- 2026-05-30 retrieval/`source_date` traces on historical rows (kept the **event** `as_of_date`)
- all Mira-derived L6 retrospective valuations (gave the **raw L1/L4 inputs** instead, so the
  agent must compute — this also exercises the quant-trap intervention)

## What was retained (all cases)

- `authority_level` (L1/L4/L5) and document type — **required** so the agent can weigh
  L1 filing vs L4 market-pricing vs L5 aggregator (per reviewer note: stripping source grade
  would unfairly damage reasoning quality)
- exact reported numbers, period labels, and event dates
- `claim_type` distinctions (reported_metric vs forecast/pro-forma vs market_pricing vs rumor)
- period-true disclosures that happen to be analytically load-bearing (e.g. the issuer's own
  COVID stay-at-home attribution in case_a fact 1 — this is a *contemporaneous filing fact*,
  not hindsight)

## Per-case cutoff and exclusions

### `case_a` (source: pton failure-backtest)
- cutoff: `as_of_date ≤ 2021-06-30` (FY2021 annual filing = peak-narrative moment, before any deterioration signal).
- **included** (sanitized): FY2020 + FY2021 issuer metrics, FY2021 hardware gross margin 29.0%, FY2021 year-end inventory $937.1M, capital structure (Dec 2020), peak price + year-end-2020 market cap.
- **excluded as post-cutoff / collapse / postmortem**: Q2-FY2022 hardware revenue decline & 6.4% margin (2021-12-31); Dec-2021 inventory $1.541B and Jun-2022 $1.105B (kept only the Jun-2021 $937.1M); all FY2022 10-K rows (revenue −30.5%, −11.3% margin, −$2.8B net loss, −$2.4B FCF); goodwill reset; 2021 year-end market-cap collapse value; Q2-FY2022 transcript; L6 consensus-reconstruction and L6 peak-valuation calc.
- design intent: at this cutoff a naive reader sees "subs 2.33M, churn 0.61%, engagement up, revenue $4.0B (+100%+)" → bullish; a disciplined reader sees COVID-attributed demand + 29% volume-dependent hardware margin + inventory building + ~$52B cap on $4B revenue → watch-only pending normalized hardware demand. **This is the discrimination point.**

### `case_b` (source: tdoc failure-backtest)
- cutoff: `as_of_date ≤ 2021-12-31` (FY2021 release, before the Q2-2022 impairment).
- **included** (sanitized): Q3-2020 shock growth, 2020 merger announcement + pro-forma claim, 2020/2021 revenue, Q4-2021 deceleration, shares, capital structure (Dec 2020), peak price, year-end-2020 market cap, FY2021-call 2022 guidance.
- **excluded as post-cutoff / collapse / postmortem**: 2022 revenue $2.407B; the $13.66B 2022 net loss (row bundled the 2021 $429M loss with it — whole row dropped to avoid the tell); goodwill $14.5B→$1.07B impairment; Q2-2022 $3.0B and 9-month $9.6B impairment charges; L6 2026 valuations.
- design intent: explosive COVID growth + a big acquisition narrative + ~$29–45B valuation, but shock-source demand, decelerating, and zero cross-sell/ROIC evidence → watch-only pending normalized demand and acquisition value capture.

### `case_c` (source: aapl golden case) — reverse control, should **not** downgrade
- cutoff: 2026-04-14 (full case; no truncation — it is a current-era quality compounder).
- **included** (sanitized): FY2025 filing + tariff risk factor, fiscal-Q1-2026 results (rev $143.8B +16%, EPS +19%, OCF ≈$54B), capital-return capacity, L5 market data (flagged stale), L4 technical read, L4 foldable-delay rumor.
- **excluded**: none for outcome reasons; only identifiers stripped.
- design intent: no demand shock, durable platform. Correct answer = quality compounder, valuation mostly priced-in, `no_action` / `watch` — **not** a broken-thesis downgrade. Catches any arm that downgrades on recognized-risk reflex.

## Why identity leakage does not sink the experiment

- **Ablation holds it constant.** The same packet + model feeds every arm. Whatever the model
  recognizes, it recognizes equally in Arm 0 and Arm 4, so recognition largely **cancels in the
  control-vs-treatment delta**. We measure the *intervention* effect, not absolute accuracy.
- **The rubric scores reasoning, not the final direction.** A model that pattern-matches
  "I recognize this, it crashed → downgrade" gets the direction but **scores low on
  `consensus_proxy_quality`, `falsification_point` and `downgrade_timing`** because it never
  articulates the consensus, the mechanism, or derives the timing from the dated facts.
- **`case_c` catches recognition-reflex.** A model that downgrades whatever it recognizes as
  risky will wrongly downgrade `case_c` and fail the reverse control.

## Residual recognizability (honest record)

- `case_a`: moderate — connected-fitness hardware + subscription + COVID + ~$167 ATH may suggest a specific 2020–21 name.
- `case_b`: moderate — telehealth + 2020 chronic-care merger + ~$294 ATH may suggest a specific name.
- `case_c`: **high** — 2.5B+ installed base + services + foldable rumor is hard to disguise. Accepted because, for the reverse control, recognition does not hand over a *wrong* answer.

## Leakage self-check

Automated grep of `packets/*.md` for the retrospective lexicon and leftover identifiers — result recorded in `leakage-check.txt` in this directory.
