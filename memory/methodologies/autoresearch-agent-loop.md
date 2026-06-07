# Methodology Card: AutoResearch Agent Loop

- status: trial
- role: meta-research-production-loop + quality-gate enhancer
- last_updated: 2026-06-07
- source_bucket: mixed (`practitioner`, `engineering`, `academic-workflow`, `derived_internal`)
- source_quality: medium
- credibility_score: medium
- credibility_basis: Deli Chen's AutoResearch materials provide a concrete research-production workflow and public paper-writing skill group; Karpathy and GitHub provide a separate measurable-engineering optimization loop. Credibility is capped at medium because Mira has not run a live trial, the full Deli AutoResearch system has not been audited as a reproducible framework here, and automatic self-review scores are not equivalent to independent peer review.
- search_coverage: low-medium
- search_gaps: Need direct inspection of any full Deli AutoResearch framework release if published, broader critique or replication attempts, and one Mira trial on a real research package before protocol adoption.
- comparison_baseline: existing Mira methodology loop, evidence log, readiness gate, delivery checklist and ad hoc iterative drafting
- empirical_validation_mode: trial -> internal dry run + live research-package trial + false-positive audit
- follow_through_plan: Test on one methodology card upgrade, one long-form research package, and one quant or evidence-classification experiment.

## Core Idea

`autoresearch-agent-loop` turns research or engineering work into an explicit iteration system:

1. Define the objective and scope boundary.
2. Define measurable or reviewable quality gates before work begins.
3. Run an agent loop that proposes changes, executes the allowed task, records results and keeps only improvements.
4. Route weaknesses back to the right sub-skill instead of asking for vague "make it better" revisions.
5. Stop when marginal improvement fades, budget is exhausted, or independent review finds the metric is no longer aligned with real quality.

The useful Mira adaptation is not autonomous research or automatic conviction. It is a bounded quality-improvement loop for research artifacts, methodology design, evidence classification and reproducible quantitative experiments.

## Reverse-Engineered From

- Deli Chen's `Deli AutoResearch` materials, especially the public scientific-paper workflow and skill group.
- Deli AutoResearch paper examples covering literature review, experiment design, simulated peer review and paper writing.
- Karpathy's `autoresearch` prototype, which uses a measurable experiment loop for code and training optimization.
- GitHub's `awesome-copilot` `autoresearch` skill, which generalizes the idea into metric-defined coding experiments.
- Mira's existing methodology loop, evidence logs and readiness gates.

## Search Paths Used

- `DeepSeek expert autoresearch`
- `DeepSeek 专家 autoresearch`
- `Deli Chen AutoResearch DeepSeek`
- `Deli AutoResearch Papers`
- `Scientific Paper Writing Skill Group autoresearch`
- `Karpathy autoresearch`
- `GitHub awesome-copilot autoresearch skill`

## Use When

- A Mira method, report, evidence classifier, prompt pack or quant workflow can be improved through repeated bounded iterations.
- The desired improvement can be measured by a metric, rubric, reviewer scorecard, source coverage gate or reproducible test.
- Weaknesses can be routed to a specific sub-skill: literature/source coverage, structure, experiment design, figures/tables, peer review, evidence logging or calculation quality.
- The task benefits from preserving failed attempts and their reasons.

## Avoid When

- The output is a one-off factual answer or quick market triage.
- The task lacks a measurable or reviewable gate.
- The agent can alter the evaluation script, source boundary or acceptance metric.
- The research question is open-ended judgment where deeper iteration would mostly create synthetic confidence.
- The user needs a decision-bound market answer and live-data freshness is the binding constraint.

## Applies To

- Methodology cards and methodology upgrades.
- Long-form research packages.
- Evidence-log quality improvements.
- Prompt, skill and loop design.
- Quant experiments with fixed metrics.
- Internal reviewer simulations and release-readiness dry runs.

## Core Question

Can this research artifact be improved through a bounded, logged, falsifiable iteration loop without letting the agent optimize the score at the expense of real evidence quality?

## Required Inputs

- `objective`
- `scope_boundary`
- `allowed_files_or_artifacts`
- `frozen_evaluation_or_review_rubric`
- `baseline_result`
- `iteration_budget`
- `acceptance_metric`
- `rollback_rule`
- `human_or_independent_review_gate` when conclusions or public release readiness are at stake

## Primary Signal

The method is working if iterations produce observable improvement in source coverage, citation verification, facts / inferences / judgments separation, falsification conditions, unsupported-claim count, calculation reproducibility or reviewer-to-repair routing.

## Why It Works

Mira already has quality gates, but many improvements still happen as unlogged drafting. AutoResearch-style loops force baseline comparison, frozen evaluation, iteration records, rollback and routed repair paths.

## Failure Mode

- Metric hacking: the agent optimizes the visible score while real research quality worsens.
- Self-review inflation: simulated peer review scores are treated as independent validation.
- Source laundering: weak or stale sources are made to look formal through better formatting.
- Scope drift: each iteration expands the task until the original question is lost.
- Evaluation contamination: the agent edits tests, rubrics or source boundaries to pass.
- Process bloat: simple Mira tasks become unnecessarily heavy.

## Evidence Cost

medium

The setup cost is higher than a normal quick map because it needs a baseline, rubric, iteration log and review path. It becomes cost-efficient only when the artifact will be reused or when quality failures would be expensive.

## Speed Vs Depth

Starts slow, then compounds. Use the lightweight version for method cards or prompt packs; use the full loop only for public-grade reports, release candidates, quant experiments or workflow changes that could affect many future research outputs.

## Comparison To Existing Methods

Relative to `methodology-research-loop`, this method adds an iterative execution layer. The existing loop defines how to collect, score and queue a method; AutoResearch-style looping defines how to improve a candidate artifact under a frozen evaluation protocol.

Relative to `institutional-research-quality-gate`, this is heavier and more operational. The quality gate asks four final-pass questions; AutoResearch loops create a repeated improvement path and evidence trail.

Relative to `delivery-checklist`, this is not a checklist. It is a controlled experiment loop for improving the artifact until the checklist or rubric stops moving.

## Follow-Through Criteria

- Did the loop improve output quality versus a single-pass baseline?
- Did failed iterations reveal useful failure modes?
- Did reviewer criticism route cleanly to a specific repair skill?
- Did the final output avoid overstating confidence from self-review?
- Did the loop stay inside the original scope and budget?

## Trial Design

### Trial 1: Methodology Card Upgrade

- target: upgrade one existing `trial` methodology card
- baseline: current card plus search log
- evaluation: source coverage, failure-mode clarity, trial design quality and adoption-boundary discipline
- expected increment: cleaner search gaps and better falsification conditions

### Trial 2: Long-Form Research Package

- target: one `standard` or `deep_dive` research package
- baseline: first complete draft
- evaluation: evidence-log completeness, unsupported-claim count, source quality, refresh conditions and thesis-state clarity
- expected increment: fewer weak conclusions and clearer evidence-to-judgment mapping

### Trial 3: Quant Or Classification Experiment

- target: evidence claim classifier, source classifier, or small backtest-like workflow
- baseline: fixed metric and held-out examples
- evaluation: frozen test, iteration log, rollback rule and no evaluation-script edits
- expected increment: measurable improvement without metric leakage

## Falsification Conditions

- It cannot improve a methodology card or research package versus one careful manual pass.
- It mainly increases process text without improving evidence quality.
- The agent repeatedly optimizes the rubric while missing real source or logic weaknesses.
- Self-review scores diverge from human or independent reviewer feedback.
- The loop encourages automatic thesis confidence, actionability or trading instructions.

## Adoption Decision

Current judgment: `trial`.

Do not patch Mira's core operating contract yet. Use this as an optional methodology loop for reusable artifacts and measurable experiments. Upgrade only after at least two real Mira trials and one independent or human-reviewed comparison show better quality without unacceptable process drag.

## Source Notes

- Deli Chen homepage and DeepSeek affiliation note: https://victorchen96.github.io/index.html
- Deli AutoResearch paper examples: https://victorchen96.github.io/auto_research/paper.html
- Deli Scientific Paper Writing Skill Group: https://victorchen96.github.io/auto_research/skill/paper-writing.html
- Karpathy AutoResearch prototype: https://github.com/karpathy/autoresearch
- GitHub `awesome-copilot` AutoResearch skill: https://raw.githubusercontent.com/github/awesome-copilot/main/skills/autoresearch/SKILL.md
- GitHub Copilot skill safety documentation: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills

## Refresh Conditions

- stale_after: 2026-07-07
- must_refresh_if: Deli publishes the full AutoResearch framework, GitHub changes the `autoresearch` skill materially, Karpathy updates the prototype into a broader release, or a Mira trial shows the loop improves or harms artifact quality.
