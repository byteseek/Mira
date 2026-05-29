# Contributing to Mira

Mira is an agent-native investment research workspace. Contributions should
improve source quality, routing discipline, evidence logging, or reusable
research workflows.

## Contribution Types

- `data/`: source schemas, source policies, time policies, and source registries.
- `loops/`: operating loops for research, monitoring, methodology review, or routing.
- `skills/`: reusable analysis skills and framework references.
- `templates/`: package templates and structured output skeletons.
- `cases/`: historical example runs that demonstrate the workflow.
- `memory/`: slow-moving methodology notes, playbooks, and validated reusable lessons.

## Research Standards

Every durable research conclusion must have a source trail. Do not submit
market views, investment judgments, or methodology claims as conclusions unless
the evidence path is visible.

Required standards:

- Separate facts, inferences, and judgments.
- Classify important claims using `data/claim-taxonomy.md`.
- Prefer primary sources for facts and filings; label secondary, sell-side,
  social, and market-data sources clearly.
- Include `research_cutoff_date`, `analysis_cutoff_date`, or equivalent `as_of`
  metadata for every case.
- Include `stale_after`, `must_refresh_if`, `Next Refresh`, or equivalent refresh
  conditions for every case.
- Include `evidence-log.csv` for any case package that contains a conclusion.
- Downgrade conclusions when source quality is weak or important sources are
  missing.

## Case Contributions

Case packages are historical examples, not investment recommendations.

When adding a case:

- Add a `README.md` with package type, date boundary, source boundary, refresh
  policy, and `not_investment_advice: true`.
- Add the relevant output files from `templates/`.
- Add an `evidence-log.csv` that maps source records to the claims used.
- Do not include paid research PDFs, private notes, raw transcripts under
  restricted licenses, account data, personal data, cookies, API keys, or broker
  exports.
- If a source is paywalled or restricted, record metadata and a short compliant
  summary only.

## Skill and Loop Contributions

When adding or changing a skill or loop:

- Explain when it should be used and when it should not be used.
- Define required inputs, source expectations, output package shape, and stop
  rules.
- State common failure modes.
- Keep responsibilities clear: `skills` define analysis capability; `agents`
  organize work; `loops` define operating process.

## Validation

Run the lightweight repository checks before opening a pull request:

```sh
python3 scripts/validate_repo.py
```

The validator checks for open-source governance files, basic case metadata,
evidence logs, and refresh/disclaimer coverage.

## Pull Request Checklist

- [ ] The change is scoped to one clear workflow, skill, template, or case.
- [ ] New conclusions have source trails.
- [ ] Case outputs include stale/refresh conditions.
- [ ] Real-market examples are marked as historical and not investment advice.
- [ ] No secrets, paid content, private account data, or personal data are
      included.
- [ ] `python3 scripts/validate_repo.py` passes.
