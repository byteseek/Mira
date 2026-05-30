# Methodology Card: Institutional Research Quality Gate

- status: trial
- role: quality-gate
- last_updated: 2026-05-30
- source_bucket: mixed (`institutional`, `practitioner`, `first_principles`, `derived_internal`)
- source_quality: medium-high
- credibility_score: medium-high
- credibility_basis: CFA standards support reasonable basis, fact/opinion separation and research records; expectations investing supports price-implied expectations and decision relevance; Oakmark supports thesis challenge and retrospective; Mira already has evidence logs, refresh conditions and thesis state machinery
- search_coverage: medium
- search_gaps: More buy-side internal investment committee checklists, portfolio-manager decision journals and failed-thesis postmortems would improve confidence
- comparison_baseline: existing Mira evidence discipline plus delivery checklist
- empirical_validation_mode: trial -> apply to live research outputs and review whether it reduces weak conclusions without adding workflow drag
- follow_through_plan: Use as a final self-check in the next 3-5 formal Mira outputs before deciding whether to patch `OPERATING_CONTRACT.md` or keep it as a methodology note

## Core Idea

Mira should not add another long checklist. The useful upgrade is a small quality gate that forces each important judgment to pass four questions:

1. `reality_basis`: Is the judgment supported by observable facts, operating data, market outcomes or source-traced evidence, rather than document rhetoric, stale memory or narrative?
2. `first_order_variable`: Does it address the variable that can actually move value, expectations, cash flow, competitive position, risk exposure or thesis state?
3. `decision_increment`: Would it change thesis state, research action, watch priority, risk framing, refresh condition or follow-up work?
4. `disconfirmation_path`: What fact, metric, event or market/operating result would prove the judgment wrong or force a reassessment?

The gate translates the user's preferred research standard into Mira's existing protocol:

- `institutional + practical` -> decision increment and ability to survive professional challenge.
- `fundamental + correctness` -> first-order variable discipline.
- `practice as test of truth` -> reality basis and disconfirmation path.

## Use When

- Before upgrading a conclusion to thesis-level judgment.
- Before writing `judgment`, `thesis_state`, `research_action` or `actionability_bridge`.
- When a draft output feels comprehensive but may be mostly background.
- When evidence is present but the link to decision, value driver or invalidation is unclear.

## Avoid When

- The user asks for a lightweight factual lookup.
- The output is a raw evidence log or source inventory with no durable conclusion.
- The same point is already captured more specifically by `claim-taxonomy`, `variant-perception`, `thesis-horizon-routing` or an event-specific skill.

## Applies To

- Single-equity research packages.
- Monitoring updates and thesis-system updates.
- Earnings and event delta reviews.
- PM or multi-thesis reviews where background facts can easily crowd out decision-relevant judgment.

## Core Question

Is this conclusion reality-grounded, focused on the first-order variable, decision-relevant and explicitly falsifiable?

## Required Inputs

- research object, market scope and time boundary
- source notes or evidence log
- current thesis or target output type
- claimed conclusion or judgment to test
- likely research action or follow-up path

## Primary Signal

The gate is working if it causes weak conclusions to be downgraded, compressed or moved to background, while leaving strong conclusions easier to challenge and refresh.

## Why It Works

Mira already has many strong mechanisms: evidence log, claim taxonomy, thesis horizon routing, variant perception, actionability bridge and refresh conditions. The missing piece is a short pre-upgrade question set that decides whether a conclusion deserves thesis-level status at all.

This method should therefore act as a compression layer, not a new workflow branch.

## Failure Mode

- It becomes a repeated checklist pasted into every memo.
- It duplicates existing evidence-log or delivery-checklist fields.
- It blocks useful exploratory thinking too early.
- It over-demands market proof for questions that are still in discovery mode.
- It turns every conclusion into a trading-action question, violating Mira's research boundary.

## Evidence Cost

low

The method mostly uses evidence already gathered by other Mira loops. It should not require new data collection unless the four questions reveal a source gap.

## Speed Vs Depth

fast

It should be usable as a 30-90 second final pass. If it takes longer, the method is probably too complex or the output needs a more specific loop.

## Comparison To Existing Methods

Relative to `delivery-checklist`, this is narrower: it checks whether the judgment is worth making, not whether the package is complete.

Relative to `claim-taxonomy`, this is later in the chain: claim taxonomy classifies evidence; the quality gate tests conclusion strength.

Relative to `variant-perception`, this is broader and lighter: variant perception focuses on market expectations; the quality gate applies to any durable research judgment.

Relative to `institutional-thesis-system`, this is smaller: thesis system maintains stateful objects; the quality gate decides whether a conclusion should be promoted into that system.

## Trial Design

- Apply to next 3-5 formal Mira outputs that contain thesis-level judgments.
- For each output, record whether the gate caused:
  - downgrade from thesis to watch/background
  - clearer first-order variable
  - better refresh or invalidation condition
  - shorter output with less repeated process text
- Review after at least two real cases and one monitoring or event update.

## Falsification Conditions

- It mostly repeats fields already required by `OPERATING_CONTRACT.md` and `templates/delivery-checklist.md`.
- It makes simple tasks noticeably slower.
- It does not improve downgrade decisions or conclusion clarity in at least two real cases.
- It encourages overconfident actionability instead of better research boundaries.

## Adoption Decision

Current judgment: `trial`.

Do not patch the core operating contract yet. Keep this as a trial methodology until live cases show it improves output quality without adding complexity.

## Source Notes

- CFA Institute Standard V(A) Diligence and Reasonable Basis: https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-a
- CFA Institute Standard V(B) Communication with Clients and Prospective Clients: https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-b
- CFA Institute Standard V(C) Record Retention: https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-c
- Expectations Investing overview: https://www.expectationsinvesting.com/about-expectations-investing
- Oakmark decision process article: https://oakmark.com/news-insights/decide-like-an-athlete/
- Bridgewater All Weather Story: https://www.bridgewater.com/research-and-insights/the-all-weather-story

