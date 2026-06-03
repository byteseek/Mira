# Mira

[English](README.md) | [中文](README.zh.md)

Agent-native investment research workspace for evidence-tracked, refreshable investment theses.

Mira is a research workspace for AI agents and research users. It is designed to turn multi-source material into traceable, reviewable and refreshable investment judgment, rather than a one-off stock report or chat answer.

Mira focuses on the investment thesis: what evidence supports it, when it is valid, what would disconfirm it, and how it should be monitored.

## Disclaimer

This repository is for research workflow design, documentation, and historical examples only. It does not constitute investment advice and does not provide legal, tax, accounting, or financial advice. The same disclaimer applies to any AI/agent output produced with this repository, including answers, memos, research packages, and derived analysis based on public sources, user-provided materials, local files, market data, or combined datasets. Treat all such outputs as research support, not advice, recommendations, or verified facts. Public case packages and generated outputs may be incomplete, inaccurate, or stale after their stated cutoff or refresh boundary.

## Start Here

If you want Codex, Claude Code or another code agent to use this repository for stock, industry, ETF, earnings or macro research, start with these files:

| Need | Read |
| --- | --- |
| Wake word, identity boundary and memory contract | [MIRA.md](MIRA.md) |
| One-screen agent loading contract | [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md) |
| User-facing prompts and task cards | [AGENT_QUICKSTART.md](AGENT_QUICKSTART.md) |
| Codex project rules | [AGENTS.md](AGENTS.md) |
| Claude Code entry | [CLAUDE.md](CLAUDE.md) |

Recommended first command:

```sh
scripts/check_updates.sh
```

Mira should check whether the local workspace is behind remote before substantive work when network access is available. It should not update automatically; run `git pull --ff-only` only after user confirmation.

## Quickstart

Minimal workflow:

1. Check remote freshness with `scripts/check_updates.sh`.
2. Read [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md) for the lazy-loading map.
3. Run [loops/analysis-routing.md](loops/analysis-routing.md) before formal analysis.
4. Load only the routed loop, skill and templates needed for the task.
5. Produce artifacts with evidence logs, time boundaries, refresh conditions and downgraded conclusions where evidence is weak.
6. Validate formal cases with [templates/delivery-checklist.md](templates/delivery-checklist.md) and the relevant script.

Typical prompt:

```text
Mira, research AAPL. Market scope: US. Time boundary: through 2026-04-14.
Run analysis routing, thesis horizon routing, framework selection and overlay selection first.
Then produce a research package with stale_after and must_refresh_if.
```

## What Mira Does

Mira supports:

- first-pass coverage or thesis rebuild for a stock, industry, ETF, macro variable or market theme
- monitoring updates that separate incremental evidence from thesis-changing evidence
- earnings, SEC filing, macro, industry-concept and ETF specialty analysis
- evidence logs that classify facts, claims, assumptions, opinions, market pricing and derived calculations
- thesis system objects such as expectation maps, event deltas, decision logs and postmortems
- position and portfolio reviews when the user provides holdings, weights, mandate or risk constraints
- methodology research for adopting, trialing or retiring reusable research methods

Mira is not a trade bot, market-data daemon or autonomous portfolio manager.

## Core Concepts

| Concept | Meaning | Details |
| --- | --- | --- |
| `research package` | Standard memo, evidence log and case notes for a formal research object. | [docs/research-artifacts.md](docs/research-artifacts.md) |
| `evidence log` | Claim-level source trail for conclusions and key observations. | [data/evidence-log-schema.md](data/evidence-log-schema.md) |
| `thesis system` | Durable chain from source to claim, expectation, thesis, event delta, decision log and postmortem. | [architecture/thesis-system.md](architecture/thesis-system.md) |
| `refresh boundary` | `stale_after`, `must_refresh_if` or equivalent conditions that make a conclusion unsafe to reuse. | [data/time-policy.md](data/time-policy.md) |
| `controlled vocabulary` | Stable state and action tokens for thesis state, readiness, research action and review outputs. | [data/controlled-vocabulary.md](data/controlled-vocabulary.md) |

## Task Routing

Formal work starts with [loops/analysis-routing.md](loops/analysis-routing.md). Common destinations:

| User Need | Primary Entry | Output |
| --- | --- | --- |
| Establish or rebuild an investment thesis | [loops/research-loop.md](loops/research-loop.md) | Standard research package |
| Update an existing thesis | [loops/monitoring-loop.md](loops/monitoring-loop.md) | Monitoring summary and thesis impact |
| Analyze earnings or guidance | [skills/earnings-report-analysis/](skills/earnings-report-analysis/) | Earnings package and update decision |
| Analyze industry or supply-chain concept | [skills/industry-concept-analysis/](skills/industry-concept-analysis/) | Industry map and stock handoff |
| Analyze macro transmission | [skills/macro-economic-analysis/](skills/macro-economic-analysis/) | Macro note or macro overlay |
| Discover or analyze ETFs | [skills/etf-listing-discovery/](skills/etf-listing-discovery/), [skills/etf-listing-analysis/](skills/etf-listing-analysis/) | ETF discovery or listing package |
| Review method quality | [loops/methodology-research-loop.md](loops/methodology-research-loop.md) | Methodology card and logs |
| Review a real position or portfolio | [loops/position-review-loop.md](loops/position-review-loop.md), [loops/portfolio-construction-review-loop.md](loops/portfolio-construction-review-loop.md) | Position or portfolio review artifacts |

Single-equity research should also run:

- [thesis horizon routing](skills/equity-research-core/references/thesis-horizon-routing.md)
- [framework routing](skills/equity-research-core/references/framework-routing.md)
- [overlay routing](skills/equity-research-core/references/overlay-routing.md), when a focused evidence path materially improves the answer

## Documentation Map

| Topic | Document |
| --- | --- |
| Agent contract and lazy loading | [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md) |
| Prompt examples and task cards | [AGENT_QUICKSTART.md](AGENT_QUICKSTART.md) |
| Wake word and memory boundary | [MIRA.md](MIRA.md) |
| Research artifacts and validation | [docs/research-artifacts.md](docs/research-artifacts.md) |
| Modules, loops, skills, cases and roadmap | [docs/module-map.md](docs/module-map.md) |
| Source and claim protocols | [data/](data/) |
| Templates and delivery checklist | [templates/](templates/) |
| Case examples and reading order | [examples/README.md](examples/README.md) |
| Thesis System architecture | [architecture/thesis-system.md](architecture/thesis-system.md) |

## Examples

Prefer these canonical examples before older cases:

- [cases/aapl-2026-04/](cases/aapl-2026-04/): single-equity research package with memo, evidence log, expectation map, thesis ledger, decision log and actionability bridge.
- [cases/nvts-2026-05/](cases/nvts-2026-05/): earnings/event package with peer verification and actionability bridge.
- [cases/abf-2026-05/](cases/abf-2026-05/): industry concept package.
- [cases/etf-discovery-2026-05-09/](cases/etf-discovery-2026-05-09/): ETF discovery example.
- [cases/etf-listing-analysis-2026-05-09/](cases/etf-listing-analysis-2026-05-09/): ETF listing analysis example.

All public cases are historical examples and should not be treated as live recommendations.

## Validation

Validate the repository or a formal case:

```sh
python3 scripts/validate_repo.py
python3 scripts/validate_repo.py cases/<case-id>
```

SEC supplement or filing package validation:

```sh
python3 scripts/validate_sec_filing_package.py path/to/sec-supplement-source-note.csv
python3 scripts/validate_sec_filing_package.py path/to/sec-filing-package-dir
```

More validation and package details: [docs/research-artifacts.md](docs/research-artifacts.md).

## Project Boundaries

Mira is a research protocol, not an adviser, trade executor or automated data platform.

- No autonomous trading or order generation.
- No position-size or portfolio-construction conclusion without user-provided holdings, weights, mandate and risk budget.
- No unsourced market view should be presented as a conclusion.
- Weak evidence must downgrade the conclusion.
- Real research outputs need source trails, time boundaries and refresh conditions.
- Public examples are historical and may be stale.

Open-source policies:

- License: [Apache-2.0](LICENSE)
- Contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md)
- Security policy: [SECURITY.md](SECURITY.md)
- Data/source policy: [DATA_POLICY.md](DATA_POLICY.md)
