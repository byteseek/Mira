# Iteration Log

## 2026-05-30: Round 1 Scaffold

### Routing

- task_mode: `methodology_review` plus `discovery_or_screening`
- research_object: hot-theme practical trials for Mira workflow validation
- market_scope: global public-market research, US-listed evidence first
- time_boundary: 2026-05-30 through first validation review on 2026-06-30
- primary_skill_or_loop: `loops/methodology-research-loop.md`
- expected_output_package: theme register, evidence log, workflow evaluation rubric and iteration log

### What Changed

- Created a Round 1 hot-theme sample pool.
- Added a source-traced evidence log for theme selection.
- Added a workflow evaluation rubric that ties each trial to a pass/fail signal.
- Kept the new `institutional-research-quality-gate` in trial status; did not promote it to core protocol.

### Initial Reverse Assessment

The current Mira workflow is strong on evidence discipline and routing, but still needs live proof on three points:

1. Can it stay compact when a topic is hot and information-rich?
2. Can it downgrade strong narratives before they become pseudo-theses?
3. Can it produce a reviewable artifact that an institutional colleague can challenge without reading the whole repository?

### Next Trial

Started with `ai_power_grid`.

Reason:

- It has recent official data.
- It tests industry, macro and company evidence together.
- It is popular enough to tempt generic AI commentary.
- It gives the quality gate a clean first-order-variable test: power availability, grid connection, generation mix and capex timing relative to data-center demand.

### First Trial Result

- file: `ai-power-grid-trial.md`
- result: `map_first`
- workflow finding: `analysis-routing` and the quality gate prevented premature single-stock conclusions.
- downgrade: broad "AI power winners" was downgraded to a regional bottleneck mapping task.
- proposed patch candidate: `regional_bottleneck_check` for physical-infrastructure themes.
- evidence gap: utility filings, interconnection queue data, rate-case treatment and regional power-market evidence.

## 2026-05-30: AI Power Regional Map Iteration

### Added Outputs

- `ai-power-regional-bottleneck-map.csv`
- `ai-power-company-handoff.csv`
- `ai-power-workflow-review.md`

### Reverse Assessment

The added regional map improved the workflow in one important way: it stopped the handoff list from becoming a generic AI-power basket. The candidates are now tied to distinct exposure paths:

- regulated utility rate base and cost recovery
- Texas transmission and merchant-power sensitivity
- Southeast resource planning and PSC approval
- Arizona growth with weaker source trail
- equipment and grid-services order conversion

### Workflow Finding

`regional_bottleneck_check` looks useful, but should remain a patch candidate. It belongs as a compact overlay to `industry-concept-analysis` for physical-infrastructure themes, not as a new standalone loop.

### Next Validation Choice

Option A: deepen AI power into one single-equity sample, likely `D`, `SO`, `ETN`, `PWR` or `VRT`.

Option B: run GLP-1 claim classification next to test whether the same quality gate works in clinical/regulatory/commercial evidence instead of infrastructure evidence.

## 2026-05-30: GLP-1 Claim Classification Trial

### Added Outputs

- `glp1-claim-classification-trial.md`
- `glp1-claim-classification.csv`

### Reverse Assessment

The GLP-1 sample validated a different part of Mira than AI power. The main risk was not geographic overgeneralization; it was claim-type collapse:

- FDA approval could be mistaken for adoption.
- Label constraints could be ignored in favor of commercial narrative.
- company guidance could be mistaken for realized demand.
- oral GLP-1 market expansion could be upgraded from assumption to thesis.

`llm-claim-classification` worked as a useful guardrail by separating facts, reported metrics, guidance, company claims, assumptions and interpretations.

### Workflow Finding

The quality gate still helped outside infrastructure, but it needed a healthcare-specific bridge. The proposed patch candidate is `clinical_commercial_bridge`:

- regulatory status
- label / endpoint constraint
- patient population
- access / reimbursement
- adoption and persistence
- supply capacity
- price / margin conversion
- competitive standard of care
- disconfirmation metric

This should remain a patch candidate until tested on at least one more healthcare/medtech case.

### Next Validation Choice

Option A: deepen AI power into one single-equity sample from `ai-power-company-handoff.csv`.

Option B: deepen GLP-1 into LLY/NVO expectation maps and decide whether it should become a thesis-system update case.

Option C: run a third contrasting theme, likely stablecoins, to test regulatory-plumbing evidence.

## 2026-05-30: GLP-1 Expectation Map Iteration

### Added Outputs

- `glp1-expectation-map.csv`
- `glp1-expectation-map-review.md`

### Reverse Assessment

The second GLP-1 iteration showed that claim classification is necessary but not sufficient. The workflow also needs to ask whether the classified facts are already embedded in expectations.

The expectation map downgraded several potential overclaims:

- reported product growth is real, but likely partly or mostly visible
- oral GLP-1 approval is real, but adoption economics remain unproven
- company guidance is useful, but not market-expectation proof
- competitive share shift is plausible, but needs prescription, payer and consensus evidence

### Workflow Finding

`institutional-thesis-system` should not automatically start just because a theme has strong facts. It should start only when the expectation map can tie new evidence to thesis state or market expectation change.

For GLP-1, current state remains `watch / expectation_map_needed`, not thesis upgrade.

### Next Validation Choice

Option A: continue GLP-1 into consensus/valuation snapshot for LLY and NVO.

Option B: switch to stablecoins to test regulatory-plumbing evidence and issuer-economics workflow.

Option C: deepen AI power into one single-equity sample from the existing handoff list.

## 2026-05-30: Stablecoin Regulatory Plumbing Trial

### Added Outputs

- `stablecoin-regulatory-plumbing-trial.md`
- `stablecoin-regulatory-plumbing-map.csv`
- `stablecoin-company-handoff.csv`

### Reverse Assessment

The stablecoin sample tested a third evidence structure: financial regulation and issuer economics. The main workflow risk was law-to-winner overreach:

- legal framework becomes mistaken for adoption
- permitted issuer status becomes mistaken for competitive winner
- reserve requirements become mistaken for economics without rate and cost assumptions
- distribution access becomes mistaken for actual payment volume

The workflow forced a better chain:

`law enacted -> eligible issuer rules -> reserve requirements -> distribution access -> circulation growth -> reserve yield / revenue share / compliance costs -> issuer cash flow`

### Workflow Finding

`macro-regime-analysis` needs a compact regulatory-to-economics bridge for financial plumbing themes. The proposed patch candidate is `regulatory_economics_bridge`.

Current state remains `regulatory_map_first`, not stock-level thesis.

### Next Validation Choice

Option A: build CRCL issuer-economics snapshot from SEC filings and Q1 2026 results.

Option B: compare V/MA payment-network exposure against direct issuer economics.

Option C: pause new cases and produce a public-facing validation summary for internal review before deciding which workflow patches deserve deeper trials.

## 2026-05-30: CRCL Issuer Economics Snapshot

### Added Outputs

- `crcl-issuer-economics-snapshot.md`
- `crcl-issuer-economics-bridge.csv`

### Reverse Assessment

This was the first single-equity handoff from the validation package. It tested whether the stablecoin regulatory map could produce company-level economics instead of a theme-driven stock thesis.

The workflow worked at the first-pass level:

- CRCL was selected because it has direct issuer economics.
- The analysis focused on USDC circulation, reserve income, distribution costs, net income, adjusted EBITDA and valuation snapshot.
- The quality gate downgraded the output to `issuer_economics_watch` instead of a thesis upgrade.

### Workflow Finding

`regulatory_economics_bridge` passed its first company-level test, but remains a trial candidate. It still needs:

- a rate/circulation/distribution-cost scenario table
- live valuation and consensus refresh
- peer comparison against COIN or payment-network exposure

### Next Validation Choice

Option A: deepen CRCL into scenario/valuation snapshot.

Option B: test `regional_bottleneck_check` with an AI power single-equity sample.

Option C: test `clinical_commercial_bridge` with LLY/NVO consensus and valuation.

## 2026-05-30: CRCL Scenario / Valuation Sanity Check

### Added Outputs

- `crcl-scenario-valuation-check.md`
- `crcl-scenario-table.csv`

### Reverse Assessment

The CRCL scenario check closed one of the publication gaps: the validation package now has at least one explicit market-pricing sanity check.

The key workflow improvement was that the single-equity sample did not stop at "CRCL has real issuer economics." It asked what the current market value appears to require:

- continued USDC circulation growth
- favorable reserve yield
- improved distribution-cost leverage
- durable adjusted EBITDA margin

### Workflow Finding

`regulatory_economics_bridge` is increasingly useful, but still not adopted. The CRCL case now validates the bridge from:

`law -> issuer economics -> market-pricing sanity check`

But it still lacks:

- consensus estimate table
- enterprise value / diluted share count
- peer comparison against COIN or payment networks
- second independent regulatory-financial case

### Next Validation Choice

Option A: add CRCL consensus/estimate snapshot and peer comparison.

Option B: switch to GLP-1 consensus/valuation snapshot to test another domain.

Option C: pause case generation and write the public-facing README, explicitly marking remaining gaps.

## 2026-05-30: CRCL Consensus / Peer Snapshot

### Added Outputs

- `crcl-consensus-peer-snapshot.md`
- `crcl-consensus-peer-snapshot.csv`

### Reverse Assessment

The CRCL consensus/peer step moved the market-pricing check from a simple market-cap sanity check to a weak but explicit expectation proxy.

The workflow improved in three ways:

- CRCL now has an analyst/forecast proxy rather than only company filings.
- COIN is correctly treated as an adjacent distribution/ecosystem peer, not a clean issuer comp.
- The conclusion still stops at `issuer_economics_watch` because primary consensus, EV and diluted-share reconciliation remain incomplete.

### Workflow Finding

`variant-perception` can run at proxy level, but it should not generate an actionability claim from secondary forecast pages alone.

The readiness checklist now passes market-pricing sanity check, but final publication still fails because no patch candidate has a second independent case and source-link QA is incomplete.

### Next Validation Choice

Option A: test `regulatory_economics_bridge` on a second regulatory-financial case.

Option B: test `clinical_commercial_bridge` on a second healthcare or medtech case.

Option C: test `regional_bottleneck_check` on a second infrastructure/logistics case.

### Review Trigger

After the first case, update this log with:

- workflow used
- output length before/after quality gate
- conclusion downgraded or upgraded
- evidence gaps
- proposed workflow patch

### Completion Boundary

This goal is not complete until multiple real cases have been run, reviewed and iterated into a package that can be handed to institutional colleagues without relying on private context.
