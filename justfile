# Mira developer entry points. Thin wrappers over existing stdlib scripts —
# no new logic, zero third-party deps. Run `just` to list recipes.
#
# These exist so agents (Claude Code / Codex) and humans call stable commands
# instead of re-deriving long script invocations from the docs.

# Show available recipes.
default:
    @just --list

# Strict full-repo validation (schemas, vocab, routing artifacts, cases). Exits non-zero on errors.
validate:
    python3 scripts/validate_repo.py

# Validation in report-only mode: print issues, always exit 0 (use while migrating).
validate-report:
    python3 scripts/validate_repo.py --report-only

# Validate a single case directory, e.g. `just check-case aapl-2026-04`.
check-case CASE:
    python3 scripts/validate_repo.py cases/{{CASE}}

# Score behavior evals against recorded transcripts (human-readable).
eval:
    python3 scripts/score_behavior_eval.py --transcripts evals/transcripts

# Strict behavior eval: JSON summary, fail if any case lacks a transcript.
eval-strict:
    python3 scripts/score_behavior_eval.py --transcripts evals/transcripts --json --require-all

# Unit tests for the routing-card schema checker (conditional-required teeth).
test:
    python3 scripts/test_routing_schema.py

# Everything CI should gate on: strict validation + schema tests + strict behavior eval.
check: validate test eval-strict

# Print the routing controlled vocabulary as seen by the machine (schemas/vocab.json).
vocab:
    @python3 -c "import json; v=json.load(open('schemas/vocab.json')); [print(f'{k}: {x[\"enum\"]}') for k,x in v.items() if isinstance(x,dict) and 'enum' in x]"
