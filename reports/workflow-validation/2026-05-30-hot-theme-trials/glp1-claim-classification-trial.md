# GLP-1 Claim Classification Trial

- as_of: 2026-05-30
- task_mode: `methodology_review` + `thesis_system_update`
- research_object: next-generation GLP-1 / metabolic drugs
- market_scope: global obesity / diabetes medicines, public-equity evidence focused on LLY and NVO
- time_boundary: current commercial and regulatory setup as of 2026-05-30; 2026-2028 commercial evidence window
- primary_skill_or_loop: `llm-claim-classification` via `data/claim-taxonomy.md`
- workflows_under_test: `analysis-routing`, `llm-claim-classification`, `institutional-research-quality-gate`, `institutional-thesis-system`
- source_boundary: evidence rows in `evidence-log.csv`; no valuation or prescription-data model yet
- output_status: claim-classification trial, not a full investment memo
- not_investment_advice: true

## Routing Result

This should not start as a single-company investment memo. The right first pass is claim classification because the GLP-1 topic mixes different evidence types:

- reported sales
- company capacity commentary
- FDA approval and label constraints
- company guidance
- clinical/commercial forecasts
- market-share and reimbursement assumptions

Without classification, the workflow would likely convert "oral GLP-1 approved" into an overbroad thesis about adoption, pricing power or share shift.

## Core Question

Which GLP-1 claims are already facts, which are formal guidance, which are company claims, and which are still assumptions requiring validation?

## Claim Map

See [glp1-claim-classification.csv](glp1-claim-classification.csv).

The important split:

| layer | high-authority claim | what it can support | what it cannot support |
| --- | --- | --- | --- |
| regulatory fact | FDA approval / label | event delta; possible market expansion path | actual adoption, reimbursement or persistence |
| reported metric | LLY/NVO Q1 sales | current commercial momentum | future share or margin durability |
| guidance | company 2026 outlook | expectation map input | realized demand |
| company claim | capacity and demand commentary | follow-up questions | independent proof |
| assumption | oral GLP-1 expands market | scenario design | thesis-level conclusion |
| interpretation | pricing/reimbursement risk | risk frame | settled economics |

## Facts

- Lilly and Novo have current reported GLP-1 franchise evidence from Q1 2026 materials.
- FDA approval and label information are higher-authority regulatory facts than company marketing narrative.
- Label constraints and safety language are binding inputs for adoption assumptions.

## Inferences

- Oral GLP-1 can be a major commercial variable, but the approval fact only opens the adoption pathway. It does not prove volume, net price, payer coverage, persistence or margin.
- The first-order variable is not simply "more GLP-1 demand." It is the conversion from clinical/regulatory access into profitable, durable treated-patient growth.
- For public equities, the sharper question is whether the market already prices leader durability, next-gen pipeline optionality and competitive pressure.

## Trial Judgment

The theme passes reality basis and first-order-variable checks at the category level, but does not yet pass thesis upgrade.

Current state should be `claim_map_first`. Next work should build an expectation map for LLY/NVO and then decide whether any company-level thesis needs updating.

## Quality Gate

| gate | result |
| --- | --- |
| `reality_basis` | pass for current sales and regulatory facts; partial for future adoption assumptions |
| `first_order_variable` | pass after compression: profitable durable treated-patient growth, not just drug approval |
| `decision_increment` | partial pass: supports an expectation-map update and watchlist priority, not a stock action |
| `disconfirmation_path` | partial pass: needs prescription trends, payer access, discontinuation, net pricing and comparative data |

## Workflow Review

### What Worked

- `llm-claim-classification` is useful here because it prevents approval, guidance and assumptions from collapsing into one bullish thesis.
- The quality gate changed the conclusion from "oral GLP-1 expands market" to "approval creates a pathway; adoption economics remain unproven."
- The thesis-system path is appropriate only after building expectation maps for LLY and NVO.

### What Failed Or Is Missing

- The current evidence set lacks prescription data, payer coverage, net price, discontinuation and real-world adherence.
- Peer comparison is too high-level; it needs exact segment sales, volume/price mix and launch-curve data.
- The workflow needs a compact biopharma evidence bridge: `approval -> label -> access -> adoption -> persistence -> economics`.

## Proposed Workflow Patch Candidate

Name: `clinical_commercial_bridge`

Use when a healthcare theme moves from clinical/regulatory evidence toward commercial equity conclusions.

Required fields:

- regulatory status
- label / endpoint constraint
- patient population
- access / reimbursement
- adoption and persistence
- supply capacity
- price / margin conversion
- competitive standard of care
- disconfirmation metric

Do not adopt yet. Trial it on GLP-1 first, then on another healthcare or medtech theme.

## Next Work

1. Build LLY/NVO expectation maps using current consensus or market-implied assumptions.
2. Add prescription, payer and net-price evidence if available.
3. Decide whether GLP-1 should become a thesis-system update case or remain a claim-classification trial.

## Refresh Policy

- stale_after: 2026-06-30
- must_refresh_if:
  - FDA label, safety, approval status or indication changes
  - LLY or NVO updates guidance, supply, capacity or launch timing
  - prescription, payer or net pricing evidence diverges from company commentary
  - comparative clinical data changes the expected standard of care
  - market pricing changes enough to alter the expectation map

