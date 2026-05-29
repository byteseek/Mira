# Evidence Log Validation Report

- report_date: 2026-05-29
- validator: `scripts/validate_repo.py --report-only`
- schema_ref: `data/evidence-log-schema.md`
- status: migration_required

## Summary

Current repository state after introducing canonical evidence schema:

- errors: 12
- warnings: 0
- new templates: canonical
- migrated canonical cases:
  - `cases/nvts-2026-05/evidence-log.csv`
  - `cases/aapl-2026-04/evidence-log.csv`
  - `cases/crwv-2026-05/evidence-log.csv`
  - `cases/wolf-2026-05/evidence-log.csv`
- remaining historical cases: migration required

This report intentionally does not hide legacy drift. Existing case outputs remain useful as historical research artifacts, but they should not be treated as canonical evidence-log examples until migrated.

## P0 Findings

### Source-Record Schema Used As Evidence Log

These remaining files use source-registry style columns inside `evidence-log.csv`:

- `cases/a-share-etf-options-underlyings-2026-05-26/evidence-log.csv`
- `cases/ai-hardware-bottleneck-watchlist-2026-05/evidence-log.csv`
- `cases/etf-discovery-2026-05-09/evidence-log.csv`
- `cases/etf-listing-analysis-2026-05-09/evidence-log.csv`

Required action:

- Rename or migrate source-level records to `source-log.csv`, then create canonical claim-level `evidence-log.csv`.

### Missing Claim-Level Required Fields

These files are old claim logs but lack canonical claim fields such as `claim_text`, `source_speaker`, `verification_status`, `authority_level`, `source_date`, `url_or_path`, or `upstream_sources`:

- `cases/abf-2026-05/evidence-log.csv`
- `cases/cohr-2026-05/evidence-log.csv`
- `cases/eose-2026-05/evidence-log.csv`
- `cases/figr-2026-05/evidence-log.csv`

Required action:

- Migrate active cases first.
- If a historical case remains unmigrated, mark it as legacy and avoid using it as a sample package.

### Canonical Sample Created

These cases have been migrated to the canonical claim-level schema:

- `cases/nvts-2026-05/evidence-log.csv`: current earnings flagship sample.
- `cases/aapl-2026-04/evidence-log.csv`: legacy public sample now has canonical evidence rows.
- `cases/crwv-2026-05/evidence-log.csv`: earnings/event-delta sample now has canonical evidence rows.
- `cases/wolf-2026-05/evidence-log.csv`: narrative-heavy weak-evidence sample now has canonical evidence rows.

## Methodology Adoption Correction

`memory/methodologies/adopted.md` previously marked methods adopted based on design/sample work. This has been corrected, so the validator no longer reports methodology adoption warnings:

- no method is currently `adopted`
- `framework-routing` moved back to `trial`
- `supply-chain` moved back to `trial`
- future adoption requires real cases plus follow-through or postmortem

## Migration Priority

1. ETF discovery/listing cases, with `source-log.csv` split from claim evidence
2. AI hardware bottleneck watchlist and A-share ETF/options underlyings discovery packages
3. Remaining earnings cases: COHR, EOSE, FIGR
4. ABF industry package

## Acceptance Bar

The repo should not claim a case is a standard sample unless:

- `python3 scripts/validate_repo.py` passes for that case
- every durable conclusion can trace to canonical evidence rows
- weak claim types are downgraded
- L6 or derived calculations include upstream sources
- event or thesis outputs identify expectation variable impact
