# Mira Hardening Summary - 2026-06-05

This report summarizes the repository hardening work completed after the Mira
analysis-quality review. It is a maintenance handoff, not investment research
evidence.

## Scope

The work focused on making Mira easier to verify, hand off and reuse in agent
or ChatGPT-style conversations:

- evidence-log schema adoption and posture fields
- case-level package manifests
- calculation-ledger and derived-calculation traceability
- validator regression tests
- one-command local quality gate
- copyable ChatGPT conversation instructions

## Key Changes

### Evidence Logs

- Active non-template `evidence-log.csv` files were migrated to the canonical
  v1.1 evidence posture shape.
- Template evidence logs were updated so new cases start with the same schema.
- Weak, contradicted, stale or inference-only evidence now has explicit posture
  fields instead of relying on prose.

### Package Manifests

- `research-package-manifest.json` now exists for every case with an evidence
  log.
- `scripts/generate_case_manifests.py` generates manifests from present case
  artifacts while preserving hand-authored manifests unless overwrite is
  explicit.
- `scripts/validate_repo.py` checks manifest shape, package type, list fields,
  referenced artifacts and case coverage.

### Calculation Traceability

- `calculation-ledger.csv` is now a validated case artifact.
- Derived calculations must have either a `Formula:` note in the evidence row
  or a sibling calculation-ledger row whose `evidence_log_ref` points back to
  the evidence row.
- Historical failure-backtest cases now include calculation ledgers for derived
  valuation and pull-forward claims.

### Regression Tests

- `scripts/test_repo_validation_contracts.py` locks the new repo-validation
  contracts into executable tests.
- `scripts/run_long_term_release_checks.py` now includes the contract tests in
  the long release QA suite.

### Quality Gate

- `scripts/run_quality_gate.py` is the maintainer-facing one-command gate.
- Full mode runs syntax checks, repository contract tests, full repository
  validation and long release QA checks.
- Fast mode can skip the long release suite and optionally run an advisory
  local-ref update check.

### ChatGPT Instructions

- `docs/chatgpt-conversation-instructions.md` contains a copyable Mira
  instruction pack for ordinary ChatGPT conversations.
- The instruction pack preserves Mira's routing, evidence, source-gap,
  calculation and actionability boundaries without requiring local repository
  access.

## Verification Commands

Current passing commands:

```sh
python3 scripts/run_quality_gate.py
python3 scripts/run_quality_gate.py --skip-long-term --check-updates
python3 scripts/validate_repo.py
python3 scripts/run_long_term_release_checks.py
```

Latest observed status:

- full quality gate: passed
- fast quality gate with advisory update check: passed
- repository validation: 0 errors, 0 warnings
- long release QA: passed with 0 errors

## Remaining Handoff Step

The remaining operational step is version-control handling: review, stage and
commit the changes when ready. No commit is created by this report.
