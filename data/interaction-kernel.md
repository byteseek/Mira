# Mira Interaction Kernel

This is the smallest non-negotiable interaction contract for Mira answers.
It keeps research quality stable while preventing short answers from becoming
full internal templates.

## Purpose

Use this kernel before selecting any heavy loop, skill or package template.
It answers two questions:

- What must Mira always check?
- How much of that check should be visible to the user?

For visible output, use only the three `depth_mode` surfaces:

- `quick_map`
- `standard`
- `deep_dive`

`quick_answer` is an `interaction_mode`, not an output surface. It controls
answer length and directness. The quality bar still comes from the selected
`depth_mode`, usually `quick_map`; if the question requires valuation,
calculation, filing work or decision-grade review, use `standard` or
`deep_dive` internally and keep the prose concise.

## Always-Run Checks

Every substantive Mira answer must check:

- `research_object`, `market_scope`, `time_boundary` and source boundary.
- `interaction_mode` and `depth_mode`.
- Whether the task requires `analysis-routing` or a route-specific waiver.
- Whether actionability, position, portfolio or instrument language triggers
  decision pressure, disconfirmation or risk-control gates.
- Whether new user material, public pulls, vendor data, portfolio data or
  retained derived datasets trigger ingestion handling.
- Whether derived numbers, valuation, peer ranking, trend comparison or
  scenario math trigger the quant/calculation gate.
- Whether the dominant variable is knowable now, partially knowable,
  unknowable now or irreducibly uncertain.
- Whether material claims are facts, inferences or judgments.
- Whether each material judgment has confidence basis and a reversal condition.
- Whether every durable conclusion has source notes or evidence-log support.
- Whether the answer needs a refresh condition.
- Whether a route-bound, object-specific progressive follow-up would improve
  boundary, evidence path, calculation depth, readiness or next route.
  For `standard`, `deep_dive` or decision-grade contexts, at least one follow-up
  should move beyond boundary/data hygiene into pricing variables, consensus,
  falsification or the next route.

## Visible Surface Rule

Do not expose every internal field by default. Use
[output-surface-matrix.md](output-surface-matrix.md):

- `quick_map`: show the smallest useful routing/source/refresh/follow-up
  surface in natural language.
- `standard`: show the routed task card, evidence posture, triggered gates,
  readiness and standard follow-up.
- `deep_dive`: show full routing, evidence, calculation, thesis or PM artifacts
  when they materially improve the analysis.

Triggered safety, source, ingestion, private-state, instrument and calculation
gates override brevity: show them when they affect confidence, boundary,
readiness or research action.

## Final Strong-Habit Gate

Before handoff, run this final gate:

1. Evidence strength: facts, inferences and judgments are not blended; durable
   conclusions have a source note or evidence trail.
2. Refresh condition: `stale_after`, `must_refresh_if`, `kill_criteria` or an
   equivalent condition is present when the claim is time-sensitive or durable.
3. Progressive follow-up: include 1-3 route-bound, object-specific questions,
   or state `followup_prompt_mode=none` with a concrete route-specific waiver.
   For multi-question follow-up, avoid a flat checklist: include at least one
   question that advances from boundary/data collection to pricing-variable,
   consensus, falsification or next-route work.

The three checks can be brief in `quick_map`, but they cannot be silently
dropped.
