# Long-Term Workflow Validation Program

- task_mode: methodology_review + live_case_trial_design
- research_object: `long-term-integrated-thesis` workflow
- market_scope: public equity themes and public-company read-throughs, primarily US-listed names with room for HK/A-share follow-up
- time_boundary: 2026-05-30 snapshot; thesis horizon is 3-5 years
- research_cutoff_date: 2026-05-30
- as_of: 2026-05-30
- primary_skill_or_loop: `loops/methodology-research-loop.md`
- linked_methodology_case: `cases/long-term-methodology-2026-05-30/`
- validation_status: iteration_01_in_progress
- not_investment_advice: true

## Objective

Pick current high-attention market themes, run the candidate workflow against them, and use the failures to improve the workflow until it is suitable for sharing with institutional colleagues.

This project treats the workflow as a hypothesis. It is not adopted until it survives repeated live and historical cases.

## Selected Trial Themes

The first four themes were chosen because they are currently market-relevant, have public-company expressions, and stress different parts of the six-lens workflow.

1. `ai_power_and_data_center_infrastructure`
   Tests macro/economy, industry structure, capital cycle, supply-chain bottlenecks and valuation expectations.
2. `enterprise_ai_agents_and_software_monetization`
   Tests product reality, customer value, adoption evidence, margin impact and valuation expectations.
3. `glp1_metabolic_health_and_consumer_readthrough`
   Tests consumer demand, product reality, health-care economics, behavioral substitution and cross-sector read-through.
4. `humanoid_robotics_and_physical_ai`
   Tests theme-to-company mapping, product maturity, evidence availability and the risk of investing in a hot concept before public-company value capture is clear.
5. `nuclear_smr_and_ai_power`
   Tests power-market contracts, regulation, interconnection, project delivery, capital cycle and the risk of mistaking AI electricity demand for public-company value capture.
6. `stablecoins_tokenized_cash_and_payment_networks`
   Tests reserve economics, rate sensitivity, distribution costs, redemption liquidity, regulatory status, AML/BSA obligations and payment-network value capture.
7. `defense_autonomy_drones_and_counter_uas`
   Tests government procurement, funded program status, contract quality, program-of-record path, delivery, compliance, allied sales and margin risk.

## Why These Themes

The set is intentionally mixed:

- infrastructure theme: strong capex visibility, hard-asset constraints, valuation risk
- software/product theme: high product uncertainty, high expectation risk
- consumer/health theme: strong product-market evidence but complex payer, behavior and downstream effects
- frontier theme: high narrative heat, weak public-company purity, large evidence gaps
- regulated power theme: real demand signal, but value capture depends on contract economics, regulatory approvals, grid treatment, COD and valuation burden
- regulated fintech theme: real adoption and regulatory momentum, but value capture depends on reserve yield, partner economics, compliance cost, redemption liquidity and actual payment usage
- defense procurement theme: real policy urgency, but value capture depends on funded programs, contract type, delivery, compliance and margin quality

If the workflow works only on one of these, it is not institution-grade.

## Source Trail

- BlackRock 2026 outlook / megatrends and AI infrastructure framing: https://www.blackrock.com/corporate/insights/blackrock-investment-institute/outlook
- Goldman Sachs Asset Management 2026 thematic / megatrend framing: https://am.gs.com/en-us/advisors/insights/article/2026-investment-outlook
- Morgan Stanley AI and humanoid robotics research hub: https://www.morganstanley.com/ideas/artificial-intelligence-investing
- IEA electricity and data-center demand coverage: https://www.iea.org/reports/electricity-2024
- McKinsey technology trends and gen AI adoption coverage: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-top-trends-in-tech
- Eli Lilly obesity / tirzepatide investor materials: https://investor.lilly.com/
- Novo Nordisk obesity care investor materials: https://www.novonordisk.com/investors.html
- FDA GLP-1 / obesity-drug source path: https://www.fda.gov/

## Iteration Discipline

Each iteration must record:

- themes tested
- why the theme was selected
- source quality
- six-lens result
- weakest lens
- workflow defect exposed
- proposed workflow patch
- next case to test the patch

## Current Iterations

- `iteration-01-assessment.md`
  Direction-level trial across four hot themes. Result: method useful but not public-grade; exposed P0 handoff and valuation defects.
- `../humanoid-robotics-2026-05-value-capture-screen/`
  Humanoid robotics / physical AI value-capture screen. Result: `industry_map_first`; public-market expressions are mostly enabling layers, adjacent automation or pre-revenue options rather than clean humanoid pure plays.
- `iteration-02-ai-power-handoff.md`
  Partial live trial on AI power / data-center infrastructure. Result: `theme_to_company_handoff` proved necessary; next best full single-company trial is likely `ETN` or `VRT`, not a blanket AI-power conclusion.
- `../etn-2026-05-long-term-workflow-trial/`
  First single-company trial. Result: ETN passes value-capture handoff but stays `watch_only_pending_expectation_map`; the workflow needs a standard expectation map, backlog quality sub-lens and acquisition-driven value-capture guardrail.
- `../vrt-2026-05-long-term-workflow-trial/`
  High-purity contrast trial. Result: VRT has stronger AI-infrastructure purity than ETN and stronger current growth, but valuation heat is higher; the workflow needs `purity_vs_expectation_burden` scoring and cash-flow quality checks.
- `../crm-2026-05-product-workflow-trial/`
  Product-reality trial for enterprise AI agents. Result: CRM has stronger-than-narrative Agentforce evidence, but product metrics still require a monetization bridge to retention, pricing, organic revenue acceleration and margin conversion.
- `../tdoc-2020-2022-failure-backtest/`
  First historical failure backtest. Result: current workflow would have downgraded TDOC before the 2022 impairment if `pull_forward_vs_structural_demand`, `product_monetization_map`, acquisition value-capture and valuation expectation patches existed.
- `../pton-2020-2022-failure-backtest/`
  Second historical failure backtest. Result: current workflow would have downgraded PTON by Q2 FY2022 if `pull_forward_vs_structural_demand` and `hardware_subscription_mix_check` existed; the case added inventory/capacity commitment and hardware gross-margin stop rules.
- `iteration-07-pton-backtest.md`
  Validation summary for the PTON historical failure backtest and the resulting hardware/subscription patch.
- `../lly-2026-05-glp1-workflow-dry-run/`
  Fourth full live single-company trial and first fresh-case dry run using the candidate public workflow pack. Result: LLY passes direct GLP-1 value-capture handoff, but stays `watch_only_pending_payer_access_and_expectation_map_refresh`; the dry run added a payer-access / net-price overlay.
- `iteration-08-lly-public-pack-dry-run.md`
  Validation summary for the LLY fresh-case dry run and the resulting payer-access / net-price patch.
- `../lly-2026-05-glp1-workflow-dry-run/source-gap-refresh-2026-05-30.md`
  Process refresh for LLY. Result: FDA verification gap closed, payer-access gap partially closed with Lilly/CVS/CMS sources, but this does not count as the required true post-memo follow-through refresh.
- `public-workflow-pack/reviewer-dry-run-2026-05-30.md`
  Internal reviewer simulation. Result: public pack had incomplete overlay/template coverage and outdated decision labels; fixed in README, fill guide, checklist and templates. This does not count as external independent analyst review.
- `historical-source-cleanup-2026-05-30.md`
  Historical source cleanup for TDOC and PTON. Result: peak-price / market-cap reconstruction improved; later upgrades added near-peak EV and transcript support, while consensus support remains open.
- `ordinary-vs-workflow-comparison.md`
  Internal comparison against ordinary research output. Result: workflow changed actionability, downgrade timing or stock-selection readiness in every completed validation case.
- `expectation-map-data-availability-audit.md`
  Valuation data availability audit. Result: CRM is the G05 public-grade candidate after adding historical EV/FCF / forward P/E and MarketScreener FY2 FCF forecast.
- `g05-expectation-map-upgrade-2026-05-30.md`
  G05 upgrade. Result: CRM historical EV/FCF and forward P/E are improved with StockAnalysis ratio history; superseded by the FY2 FCF source upgrade.
- `g05-crm-unavailable-data-exception-review.md` and `g05-crm-source-attempts.csv`
  G05 exception packet. Result: source attempts and reviewer decision rubric were prepared; packet is now a fallback audit trail after MarketScreener FY2 FCF source discovery.
- `g05-fy2-fcf-source-upgrade-2026-05-30.md`
  G05 source upgrade. Result: MarketScreener FY2028 FCF forecast closes the FY2 FCF gap for internal gate tracking; reviewer still needs to challenge source definitions under G06.
- `public-workflow-pack/external-reviewer-brief.md`
  External reviewer handoff packet. Result: reviewer assignment, scorecard, blind-review instructions and G05 exception task are ready, but not yet completed by an independent reviewer.
- `g06-external-review-handoff-2026-05-30.md`
  G06 handoff. Result: reviewer return template, intake checklist and G06 clearing rule are explicit; no independent reviewer has completed them yet.
- `follow-through-refresh-playbook.md`
  Follow-through refresh execution guide. Result: trigger tracker and refresh template are ready, but no later material event has been refreshed yet.
- `../../scripts/validate_follow_through_trigger_tracker.py`
  G04 trigger tracker validator. Result: CRM_2026 is machine-checked as the highest-priority later-event candidate with concrete trigger metrics and source requirements.
- `g04-follow-through-event-watch-calendar.csv` and `../../scripts/validate_g04_event_watch_calendar.py`
  G04 event-watch calendar. Result: ETN, VRT, CRM and LLY have official-source monitoring rows; LLY has one scheduled future event; no row clears G04 without a completed validated refresh.
- `g04-later-event-candidate-screen.csv` and `../../scripts/validate_g04_later_event_candidate_screen.py`
  G04 later-event candidate screen. Result: ETN, VRT and CRM have no later event available; LLY has one scheduled future event, but no event is selected for refresh and G04 remains blocked until official post-cutoff materials pass materiality screening.
- `../../scripts/build_follow_through_packet.py`
  G04 follow-through packet builder. Result: CRM_2026 remains the default highest-priority export, while ETN_2026, VRT_2026 and LLY_2026 can be exported with explicit `--case-id` overrides after a later material event; the packet includes the later-event candidate screen and validator, and this does not clear G04 without completed refresh evidence.
- `../../scripts/validate_follow_through_packet_matrix.py`
  G04 follow-through packet matrix validator. Result: ETN_2026, VRT_2026, CRM_2026 and LLY_2026 all temporarily export packets with required control files, including later-event candidate controls, so the next true follow-through can use whichever live case receives a qualifying later event first.
- `../../scripts/build_institutional_release_packet.py`
  Final institutional release packet builder. Result: export is refused until `scripts/validate_long_term_release.py --require-external-ready` exits 0; dry-run still checks 40 required export paths so future final packets cannot silently omit theme-selection, practice-falsification, methodology iteration trace, multi-lens coverage, objective/goal completion audits, release verification command manifest, external action queue, reviewer selection rubric, colleague-acceptance return, G04/G06 controls.
- `g04-follow-through-handoff-2026-05-30.md`, `g04-follow-through-intake-checklist.csv`, `g04-follow-through-execution-tracker.csv`, `crm-g04-follow-through-assignment.md`
  G04 execution packet. Result: four live case candidates are ready and waiting for later events, with CRM kept as the default first export; execution rows cross-check trigger tracker and event calendar state; G04 remains blocked until a later material event is refreshed and validated.
- `g01-external-method-source-audit.csv` and `g01-external-method-source-upgrade-2026-05-30.md`
  G01 external method-source upgrade. Result: public Asian/Chinese practitioner and institutional long-horizon sources improve method-source coverage; G01 remains `partial_pass_improved` pending external reviewer acceptance.
- `../../scripts/validate_g01_external_method_scan.py`
  G01 source-scan validator. Result: checks the upgraded source audit, Chinese/practitioner/institutional coverage and the memo boundary that this is not `pass_external`.
- `public-release-decision.md`
  Release decision memo. Result: internal candidate is ready for reviewer assignment, but final external release is not ready.
- `public-release-gate-tracker.csv`
  Gate tracker. Result: G05 is cleared for internal gate tracking; G04 true follow-through and G06 external reviewer remain blocking.
- `public-handoff-manifest.md`
  Handoff manifest. Result: specifies what to send to external reviewer and what to keep internal unless requested.
- `external-reviewer-bundle-manifest.csv`
  Reviewer bundle manifest. Result: required reviewer send/no-send files are explicit and validated by `scripts/validate_long_term_release.py`.
- `../../scripts/build_external_review_packet.py`
  Reviewer packet export builder. Result: the G06 reviewer packet can be dry-run checked or exported from `send_to_reviewer=yes` manifest rows without including internal do-not-send files.
- `../../scripts/validate_external_review_dispatch_packet.py`
  Reviewer dispatch packet validator. Result: a temporary real export is audited against the manifest and assignment tracker, proving the G06 packet is dispatch-ready while still not assigned and not completed.
- `g06-dispatch-readiness-checklist.csv` and `../../scripts/validate_g06_dispatch_readiness.py`
  G06 dispatch readiness checklist. Result: nine pre-assignment controls pass, including reviewer independence screening, candidate-screen readiness, practice-falsification packet coverage and methodology-iteration traceability coverage, while actual reviewer assignment and reviewer return remain external pending blockers.
- `practice-falsification-audit.csv` and `../../scripts/validate_practice_falsification_audit.py`
  Practice falsification audit. Result: eight methodology claims are mapped to 39 validated case links, explicit rejection tests, actionability/source-gap deltas and G04/G06 release boundaries, preventing theory-only claims from entering the release package.
- `methodology-iteration-trace-audit.csv` and `../../scripts/validate_methodology_iteration_trace_audit.py`
  Methodology iteration trace audit. Result: 12 workflow iterations map case failures to patch artifacts, validation commands, decision effects and G04/G06 release boundaries, preventing method changes from being justified by vague memory or theory-only claims.
- `goal-completion-audit.csv` and `../../scripts/validate_goal_completion_audit.py`
  Goal completion audit. Result: the original objective is mapped to ten proof components; the validator executes each non-recursive proof command; seven are internally proved and three remain externally blocked by G04, G06 and final release.
- `release-verification-command-manifest.csv` and `../../scripts/validate_release_verification_command_manifest.py`
  Release verification command manifest. Result: ten non-recursive release verification commands are machine-readable, executable, mirrored in the operator runbook and include current expected failures for external-ready and institutional-packet export blockers.
- `trial-theme-matrix.csv` and `../../scripts/validate_trial_theme_matrix.py`
  Theme-selection audit. Result: seven recent hot directions are linked to validation cases, evidence logs and source IDs before they can count as selected themes.
- `final-release-cutover-checklist.csv` and `external-release-go-no-go-template.md`
  Final release cutover package. Result: future `ready_external_release` requires completed checklist, go/no-go memo and passing validator.
- `../../scripts/validate_go_no_go_evidence_coverage.py`
  Go/no-go evidence coverage validator. Result: all 11 external-release gates map to 15 final go/no-go evidence rows plus matching cutover validator checks, so future gate changes cannot silently bypass final signoff evidence.
- `../../scripts/validate_public_release_freshness.py`
  Public release freshness validator. Result: 15 public/reviewer-facing materials have concrete non-stale `stale_after` dates and observable `must_refresh_if` triggers, while 4 templates preserve refresh fields for future signed returns.
- `../../scripts/validate_final_release_cutover.py`
  Final release cutover validator. Result: current cutover state is machine-checked as not ready, with 13 pending rows and no dated signed go/no-go memo; placeholder-filled or premature `decision: go` dated memos are rejected.
- `institutional-colleague-acceptance-checklist.csv` and `../../scripts/validate_institutional_colleague_acceptance.py`
  Institutional colleague acceptance validator. Result: nine colleague adoption checks plus a return memo template are prepared, but `acceptance_ready: false` until an actual institutional colleague pilot and memo exist after external-ready gates clear. Any dated acceptance memo is chained through `../../scripts/validate_institutional_colleague_acceptance_return.py`, so memo-content failures cannot be bypassed by file presence.
- `public-workflow-pack/external-review-request.md`
  Reviewer request memo. Result: external reviewer assignment language, independence boundary and required returns are standardized.
- `g06-reviewer-assignment-tracker.csv` and `../../scripts/validate_external_review_assignment_tracker.py`
  G06 assignment tracker. Result: reviewer assignment state is machine-checked as ready-to-assign, not assigned and not completed; it cross-checks independence-screen reviewer-naming / attestation rows and the reviewer candidate screen.
- `g06-reviewer-candidate-screen.csv` and `../../scripts/validate_g06_reviewer_candidate_screen.py`
  G06 candidate screen. Result: candidate-level conflict, authorship, incentive, capability and source-boundary checks are ready before assignment across three required reviewer profiles; no reviewer is selected and G06 remains blocked.
- `g06-reviewer-selection-rubric.csv` and `../../scripts/validate_g06_reviewer_selection_rubric.py`
  G06 reviewer selection rubric. Result: 11 required external-release decisions are mapped to reviewer profiles, scorecard dimensions and evidence paths before assignment; this does not clear G06.
- `../../loops/long-term-thesis-loop.md`
  Operational loop. Result: the validated trial checklist has been promoted into a formal internal-candidate loop for 3-5 year multi-lens thesis work; it is not final external-release methodology until G04 and G06 clear. G05 is internally cleared but remains subject to G06 source challenge.
- `release-qa-report-2026-05-30.md`
  Release QA report. Result: `scripts/run_long_term_release_checks.py` confirms the package is internally consistent, externally not ready, hard-blocked by G04/G06, clean across source-linked theme selection, public release freshness, practice-falsification validation, methodology-iteration trace validation, multi-lens coverage validation, public workflow pack overlay/source-trail/source-boundary validation, non-recursive ten-case validation, G01 source-scan validation, external-review packet validation, G06 assignment tracker validation, G06 reviewer candidate screen validation, G06 reviewer selection rubric validation, G06 reviewer independence screen validation, reviewer-packet export dry-run, dispatch audit and dispatch-readiness validation, external action queue validation, G04 trigger tracker validation, G04 event-watch calendar validation, G04 later-event candidate screen validation, G04 follow-through packet dry-run, four-case G04 packet matrix export audit, institutional-release bundle validation, institutional-colleague acceptance validation, expected institutional release packet export refusal, release verification command manifest validation, go/no-go evidence coverage validation, objective-readiness validation, goal-completion audit validation, ten case repo checks and 28 release-control CSV shape checks.
- `objective-readiness-audit.csv` and `../../scripts/validate_objective_readiness.py`
  Objective completion audit. Result: the original user objective is mapped to concrete proof standards; the validator executes each non-recursive proof command; 7 requirements are internally met and 3 remain blocking, so the project cannot be called complete until G04, G06 and final external release clear.
- `../nuclear-ai-power-2026-05-value-capture-screen/`
  Nuclear / SMR / AI power value-capture screen. Result: broad theme routes to `industry_map_first`; existing nuclear generators, fuel suppliers and listed SMR developers require expectation maps plus a new power-contract/regulatory overlay before any single-equity actionability.
- `../stablecoin-payments-2026-05-value-capture-screen/`
  Stablecoin / tokenized cash / payment network value-capture screen. Result: broad theme routes to `industry_map_first_with_single_equity_candidates`; issuers, distribution partners, card networks and wallets require expectation maps plus a new stablecoin reserve/regulatory overlay before any single-equity actionability.
- `../defense-autonomy-drones-2026-05-value-capture-screen/`
  Defense autonomy / drones / counter-UAS value-capture screen. Result: broad theme routes to `industry_map_first_with_single_equity_candidates`; AVAV, KTOS, PLTR and primes require expectation maps plus a new government procurement/program overlay before any single-equity actionability.
- `cross-case-validation-matrix.csv`, `overlay-coverage-audit.csv` and `cross-case-validation-summary.md`
  Cross-case synthesis. Result: every validation case now maps to an ordinary-research failure mode, workflow decision, reusable overlay/patch, public-release caveat and refresh trigger; every triggered overlay has a coverage audit row.
- `historical-backtest-source-archive-audit.csv` and `historical-backtest-publication-standard.md`
  Historical source gate. Result: TDOC/PTON evidence gaps are row-level publication gates instead of loose caveats.
- `historical-valuation-source-upgrade-2026-05-30.md`
  Historical valuation source upgrade. Result: TDOC/PTON now have filing-backed near-peak EV bridges, but consensus gaps still block external public-grade example use.
- `historical-transcript-source-upgrade-2026-05-30.md`
  Historical transcript source upgrade. Result: TDOC/PTON now have transcript support for downgrade timing, but consensus gaps still block external public-grade example use.
- `historical-consensus-source-attempts.csv` and `historical-consensus-unavailable-data-exception-2026-05-30.md`
  Historical consensus exception. Result: public source attempts are documented and the remaining consensus gap is now a reviewer-decision item, not an undefined missing-data problem.

## Public-Grade Bar

Before sharing with institutional colleagues, the workflow must show:

- at least 4 live theme/company tests
- at least 2 historical failure backtests
- at least 1 postmortem or follow-through refresh
- a clear comparison against ordinary Mira research-loop output
- no unresolved P0 defect in lens routing, evidence quality, valuation expectations or refresh conditions

## Candidate Public Workflow Pack

The first compressed candidate pack lives in `public-workflow-pack/`.

It includes:

- analyst-facing workflow
- fill guide
- source appendix
- analyst checklist
- operator runbook
- template inventory

Current status: internal candidate. It has now survived one fresh-case dry run on LLY, one LLY source-gap refresh, one internal reviewer simulation, one historical source-cleanup pass, one ordinary-vs-workflow comparison, one expectation-map data availability audit, humanoid robotics, nuclear/AI power, stablecoin/tokenized payment and defense-autonomy theme screens, promotion into `loops/long-term-thesis-loop.md`, a command-level release QA suite across ten cases, a G01 public-source coverage upgrade and a G05 FY2 FCF source upgrade. It also has external reviewer, follow-through refresh, operator runbook and release-gate packets ready. It still needs a true post-memo follow-through refresh example and completed external independent reviewer dry run before being treated as share-ready.

## Refresh Conditions

- stale_after: 2026-06-30 for theme selection
- stale_after: 2026-08-30 for workflow design
- must_refresh_if: market leadership changes, a selected theme loses relevance, or trial cases reveal a missing lens or recurring false precision in valuation expectations
