# SEC Filing Analysis Skill

This skill is used when Mira needs to analyze SEC disclosure itself, not merely cite SEC as a source.

It supports two routes:

- `sec_supplement`: lightweight SEC fact verification inside another research workflow.
- `sec_filing_deep_dive`: dedicated analysis of a filing such as 10-K, 10-Q, S-1, 8-K exhibit, DEF 14A, 13F, or Form 4.

## Route Selection

Use `sec_supplement` when:

- the primary task is single-equity research, earnings analysis, monitoring, event delta, or portfolio review
- SEC data is needed to verify a fact, metric, filing timeline, share count, cash flow item, debt item, SBC, inventory, RPO/backlog, segment value, risk factor, or governance detail
- the output should update the active case evidence log, financial snapshot, or case notes

Use `sec_filing_deep_dive` when:

- the user explicitly asks to analyze a filing, annual report, quarterly report, S-1, proxy, 8-K exhibit, 13F, Form 4, or similar document
- a thesis depends on filing-level details that cannot be answered by a quick metric lookup
- a company release, management commentary, market-data page, or prior case conflicts with the filing
- accounting quality, risk-factor delta, related-party transactions, debt/liquidity, customer concentration, segment disclosure, ownership/control, dilution, or non-GAAP reconciliation is central to the conclusion

If a filing is not yet available, do not fabricate filing analysis. Write a source-gap refresh item and state what the later filing must verify.

## SEC Authority Rules

- A specific issuer filing from SEC Archives, company IR, or filed exhibit can support `issuer_primary_disclosure` claims.
- SEC `submissions` metadata and `companyfacts` JSON are official regulatory data sources, but record them as the registry/source-class authority defines unless the case has a specific reason to classify the extracted claim differently.
- Companyfacts rows must record CIK, taxonomy, tag, unit, fiscal period, form, filed date, frame if available, and as-of date.
- Filing rows must record CIK, accession number, form type, filing date, report period, source URL, and section or exhibit when relevant.
- Do not treat an XBRL tag name as self-explanatory. If the tag is non-standard or company-specific, state the label/context and downgrade comparability.

## Required Inputs

For `sec_supplement`:

- company_name
- ticker
- market
- target_question
- needed_metrics_or_sections
- research_cutoff_date
- active_case_path

For `sec_filing_deep_dive`:

- company_name
- ticker
- market
- filing_type
- filing_period_or_event
- filing_date
- accession_number_or_source_url
- analysis_cutoff_date
- research_question
- prior_release_or_thesis_optional

## Source Retrieval Order

1. Identify CIK and ticker mapping.
2. Use SEC company submissions to confirm latest relevant filings and filing dates.
3. Use the specific SEC Archive filing or filed exhibit for textual filing analysis.
4. Use companyfacts only for structured fact extraction and cross-period metric checks.
5. Use company IR only as a navigation or duplicate-primary route when SEC rendering is unavailable.
6. Use market-data or media sources only for expectation, reaction, or context; they do not replace the filing.

## SEC Supplement Output

Default output is `templates/sec-supplement-source-note.csv` plus updates to the active case:

- active case `evidence-log.csv`
- active case `financial-snapshot.csv`, if financial facts are extracted
- active case notes source note
- `templates/source-gap-refresh.md`, if a filing or section is missing

Supplement notes must answer:

- what exact SEC source was checked
- what claim or metric it verified
- what provenance fields allow reproduction
- whether the result confirms, corrects, or conflicts with the current case
- what must refresh next

## SEC Filing Deep Dive Output

Default output package:

- `filing-analysis.md`
- `filing-metric-table.csv`
- `filing-risk-delta.csv`
- `accounting-quality-check.csv`
- `evidence-log.csv`

Optional outputs when relevant:

- `thesis-impact.md`
- `event-delta.md`
- updated research package or earnings package

## Analysis Flow

### 1. Filing Identity

Record:

- company name and ticker
- CIK
- accession number
- form type
- filing date
- report period or event date
- amendment status
- source URL
- analysis cutoff date

### 2. Filing Completeness Check

Check whether the filing includes the sections needed for the research question:

- financial statements and notes
- MD&A
- risk factors
- business description
- segment disclosure
- liquidity and capital resources
- debt, leases, commitments and contingencies
- customer concentration
- related-party transactions
- non-GAAP reconciliation
- share count, dilution, SBC, repurchases
- governance, control, compensation or ownership

Mark unavailable sections as `source_gap`, not as absent risk.

### 3. Metric Extraction

Extract only metrics that matter to the question. For each metric, record:

- statement or section
- value, unit and period
- source method: filing text/table, XBRL companyfacts, exhibit table, or derived calculation
- provenance fields sufficient for reproduction
- whether the metric confirms, corrects, or conflicts with other sources

### 4. Filing Delta

Compare against:

- prior filing
- earnings release or 8-K exhibit
- prior Mira thesis or expectation map
- peer filing if needed

Separate:

- facts disclosed in the filing
- management explanations
- Mira inferences
- judgments about thesis impact

### 5. Accounting And Quality Checks

At minimum consider:

- cash conversion versus earnings
- working-capital movement
- revenue recognition, deferred revenue, contract assets or reserves
- inventory, obsolescence or capitalized costs
- debt maturity, covenants, interest expense and liquidity
- SBC, dilution and share-count changes
- acquisition accounting, impairments, restructuring or one-time items
- non-GAAP reconciliation quality
- related-party or off-balance-sheet exposure

### 6. Risk-Factor And Language Delta

Look for:

- new risk factors
- materially expanded risk language
- removed or softened risk language
- changes in customer, supplier, regulatory, litigation, liquidity or going-concern disclosures

Do not overstate boilerplate. A risk delta matters only if it is new, more specific, tied to numbers, or inconsistent with the thesis.

### 7. Thesis Impact

Classify impact:

- `confirming`: supports an existing fact or thesis variable
- `correcting`: changes a metric, timing, or interpretation
- `conflicting`: contradicts release, management commentary, market data, or prior Mira work
- `source_gap`: filing does not contain enough evidence
- `no_material_change`: filing adds no thesis-relevant change

If impact is `conflicting`, consider upgrading the workflow to thesis update or event delta.

## Stop Rules

- Do not make a durable conclusion from a filing link without extracted claims in evidence log.
- Do not infer that missing disclosure means no risk unless the filing affirmatively says so.
- Do not compare companyfacts tags across companies without checking taxonomy, unit, fiscal calendar and company-specific tags.
- Do not treat non-GAAP metrics as facts without the reconciliation and adjustment list.
- Do not upgrade actionability if cash flow, debt/liquidity, dilution or segment evidence remains a source gap for the thesis variable.

## Refresh Conditions

Every output must include either:

- `stale_after`
- `must_refresh_if`
- or a filing-specific refresh condition

Default `must_refresh_if`:

- amended filing appears
- next 10-Q / 10-K is filed
- company releases an 8-K, exhibit or investor presentation that changes the same variable
- companyfacts data changes or restates the relevant tag
- SEC comment letter, enforcement action, proxy update, Form 4, 13F, or ownership filing changes the thesis variable
