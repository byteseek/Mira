# Module Map

This document keeps the module, loop, skill, case and extension map that used to make the root README too heavy.

Use [README.md](../README.md) as the project entry point and [OPERATING_CONTRACT.md](../OPERATING_CONTRACT.md) as the one-screen agent contract.

## Main Directories

| Directory | Purpose |
| --- | --- |
| [agents/](../agents/) | Agent orchestration rules. |
| [architecture/](../architecture/) | System design notes such as Thesis System and app skeleton. |
| [cases/](../cases/) | Historical examples and workflow validation cases. |
| [data/](../data/) | Source, claim, evidence, readiness and vocabulary protocols. |
| [docs/](./) | Reader-facing support docs that do not belong in the root README. |
| [examples/](../examples/) | Case reading order and public-example boundaries. |
| [loops/](../loops/) | Task loops for research, monitoring, thesis updates, event deltas and reviews. |
| [memory/](../memory/) | Wiki-style slow-variable memory and adopted methodology notes. |
| [reports/](../reports/) | Validation reports and workflow trial records. |
| [skills/](../skills/) | Reusable analysis capabilities. |
| [templates/](../templates/) | Package templates and delivery checklists. |

## Loops

| Loop | Use Case | File |
| --- | --- | --- |
| Analysis routing | First step before formal analysis | [loops/analysis-routing.md](../loops/analysis-routing.md) |
| Investment research | First coverage, topic research or thesis rebuild | [loops/research-loop.md](../loops/research-loop.md) |
| Monitoring | Incremental update and thesis impact check | [loops/monitoring-loop.md](../loops/monitoring-loop.md) |
| Methodology research | Evaluate research methods for trial/adoption/retirement | [loops/methodology-research-loop.md](../loops/methodology-research-loop.md) |
| Thesis update | Update thesis state, expectation map and decision log | [loops/thesis-update-loop.md](../loops/thesis-update-loop.md) |
| Event delta | Compare pre-event setup with actual disclosure or market event | [loops/event-delta-loop.md](../loops/event-delta-loop.md) |
| PM research book review | Review multiple theses from a research-book perspective | [loops/portfolio-review-loop.md](../loops/portfolio-review-loop.md) |
| Position review | Review a user-provided single real position | [loops/position-review-loop.md](../loops/position-review-loop.md) |
| Portfolio construction review | Review user-provided holdings, exposures and constraints | [loops/portfolio-construction-review-loop.md](../loops/portfolio-construction-review-loop.md) |
| Decision quality review | Review historical research decisions and process quality | [loops/decision-quality-review-loop.md](../loops/decision-quality-review-loop.md) |

## Skills

| Skill | Purpose |
| --- | --- |
| [skills/equity-research-core/](../skills/equity-research-core/) | Core single-equity research, framework routing and overlay selection. |
| [skills/industry-concept-analysis/](../skills/industry-concept-analysis/) | Industry, technology and supply-chain concept analysis before stock handoff. |
| [skills/earnings-report-analysis/](../skills/earnings-report-analysis/) | Earnings disclosure, call, guidance, peer comparison and thesis impact. |
| [skills/sec-filing-analysis/](../skills/sec-filing-analysis/) | SEC supplement and filing deep dive provenance. |
| [skills/macro-economic-analysis/](../skills/macro-economic-analysis/) | Macro variables and asset-pricing transmission. |
| [skills/commodity-cycle-analysis/](../skills/commodity-cycle-analysis/) | Commodity cycle analysis where supply/demand and pricing cycles dominate. |
| [skills/etf-listing-discovery/](../skills/etf-listing-discovery/) | New, pending or recently announced ETF discovery. |
| [skills/etf-listing-analysis/](../skills/etf-listing-analysis/) | ETF listing structure, exposure and follow-up analysis. |
| [skills/data-analysis-quality-gate/](../skills/data-analysis-quality-gate/) | Gate for derived numbers, comparisons, valuation math, time-series checks and peer ranking. |

## Equity Research Frameworks And Overlays

Single-equity work should run:

- [thesis-horizon-routing.md](../skills/equity-research-core/references/thesis-horizon-routing.md)
- [framework-routing.md](../skills/equity-research-core/references/framework-routing.md)
- [overlay-routing.md](../skills/equity-research-core/references/overlay-routing.md), when a focused evidence path can materially improve the answer

Default framework references include:

- [micro-small](../skills/equity-research-core/references/micro-small.md)
- [mid-cap](../skills/equity-research-core/references/mid-cap.md)
- [large-mega](../skills/equity-research-core/references/large-mega.md)

Overlay references include:

- [supply-chain](../skills/equity-research-core/references/supply-chain-overlay.md)
- [macro](../skills/equity-research-core/references/macro-overlay.md)
- [commodity](../skills/equity-research-core/references/commodity-overlay.md)
- [strategic-catalyst](../skills/equity-research-core/references/strategic-catalyst-overlay.md)
- [valuation-expectation](../skills/equity-research-core/references/valuation-expectation-overlay.md)

## Data Layer

[data/](../data/) defines:

- source schemas, taxonomy, registry and source policy
- data and tool ingestion contracts for public APIs, user material and
  authorized providers
- source coverage and time policy
- claim taxonomy and evidence posture
- readiness gates, handoff contracts and controlled vocabulary

Key files:

- [data/evidence-log-schema.md](../data/evidence-log-schema.md)
- [data/ingestion-layer.md](../data/ingestion-layer.md)
- [data/source-taxonomy.md](../data/source-taxonomy.md)
- [data/claim-taxonomy.md](../data/claim-taxonomy.md)
- [data/research-readiness-gate.md](../data/research-readiness-gate.md)
- [data/controlled-vocabulary.md](../data/controlled-vocabulary.md)

## Agent And Memory

[agents/research-orchestrator.md](../agents/research-orchestrator.md) is the current primary orchestrator. It clarifies the research question and time boundary, checks source protocol, runs the routed loop or skill, downgrades weak-evidence conclusions and decides what can be written to memory.

[memory/](../memory/) uses a wiki-style structure:

- `research/`: durable research result chains.
- `methodologies/`: methodology queue, trials, adopted methods and retired methods.
- `playbooks/`: market experience patterns.
- `skills/`: skill-level method notes.

Memory rules: [memory/MEMORY-RULES.md](../memory/MEMORY-RULES.md).

## Canonical Examples

Prefer these examples before older cases:

- [cases/aapl-2026-04/](../cases/aapl-2026-04/): standard single-equity package with memo, evidence log, expectation map, thesis ledger, decision log and actionability bridge.
- [cases/nvts-2026-05/](../cases/nvts-2026-05/): earnings/event package with peer verification, supply-chain note and actionability bridge.
- [cases/abf-2026-05/](../cases/abf-2026-05/): industry concept package.
- [cases/etf-discovery-2026-05-09/](../cases/etf-discovery-2026-05-09/): ETF discovery example.
- [cases/etf-listing-analysis-2026-05-09/](../cases/etf-listing-analysis-2026-05-09/): ETF listing analysis example.

Case reading order and boundaries: [examples/README.md](../examples/README.md). All public cases are historical examples, not investment advice.

## Open Source Notes

- License: [Apache-2.0](../LICENSE)
- Contribution guide: [CONTRIBUTING.md](../CONTRIBUTING.md)
- Security policy: [SECURITY.md](../SECURITY.md)
- Data/source policy: [DATA_POLICY.md](../DATA_POLICY.md)

Minimum expectations for open-source contributions:

- Real cases need an `evidence-log.csv`.
- Real cases need time boundaries and refresh conditions.
- Real security, privacy and redistribution limits are governed by [DATA_POLICY.md](../DATA_POLICY.md).
- Evidence-weak conclusions must be downgraded rather than written as facts.

## Current Boundaries

Mira is not:

- an automated scraping platform
- a trading execution system
- a full multi-agent scheduling system
- a complete quantitative backtesting engine
- a promise to archive every methodology source automatically

Current docs and templates focus on Markdown/CSV research packages, routed analysis loops, evidence logs, refresh conditions and reusable methodology memory.

## Extension Backlog

This backlog is not a release commitment.

- Strengthen industry-specific metrics in `earnings-report-analysis`.
- Add frameworks such as `cyclical`, `turnaround` and `compounder`.
- Add overlays such as `channel-check` and `peer-benchmark`.
- Validate `macro-regime-analysis` on more real cases before promoting it from `trial` to `adopted`.
- Validate `industry-concept-analysis` on more real cases such as GPU, HBM, memory and CPO.
- Connect methodology scoring to case validation.
- Validate `llm-claim-classification` on more real cases before promoting it from `trial` to `adopted`.
- Add methodology review logs and longer follow-through records.
- Add methodology query expansion and search automation.
- Split `equity-research-core` into narrower thematic skills when complexity justifies it.
- Split `research-orchestrator` into multiple monitors and specialty agents when orchestration complexity justifies it.
- Add a more detailed A-share local data source registry and public target set.
- Add monitoring-loop log templates.
