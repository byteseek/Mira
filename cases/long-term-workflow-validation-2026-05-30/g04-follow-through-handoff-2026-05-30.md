# G04 Follow-Through Handoff

- handoff_date: 2026-05-30
- gate: `G04 true_follow_through_refresh`
- status: ready_to_execute_waiting_event
- release_impact: not_cleared
- preferred_case: `CRM_2026`

## Purpose

G04 requires a real follow-through refresh after a later material event. This cannot be completed with evidence inside the original memo cutoff window.

This handoff makes the first valid refresh executable once a later event occurs.

## Valid Event Rule

A G04 refresh qualifies only if all are true:

- event date is after the original memo cutoff;
- event is material to a named thesis variable;
- new source evidence is added to the case evidence log;
- before/after action label is explicit;
- original `must_refresh_if` quality is evaluated;
- exactly one refresh result label is selected from the approved list;
- public-readiness audit and methodology review log are updated.

## Preferred First Assignment

Use `CRM_2026`.

Reason:

- CRM has the clearest product-to-company monetization blocker.
- Q2 FY2027 should test Agentforce/Data 360 ARR, Agentic Work Units, bookings growth, organic acceleration and margin guide.
- CRM now has a stronger G05 expectation map, so follow-through can test both product monetization and expectation-map refresh mechanics.

## Required Source Package

For CRM, collect:

- Q2 FY2027 earnings release or 8-K exhibit;
- Q2 FY2027 10-Q;
- earnings transcript if available;
- updated market data;
- updated FY2028 estimates / FCF forecast if materially changed;
- product metric disclosure for Agentforce/Data 360/AWUs/bookings if available.

## Required Output

Create:

- `../crm-2026-05-product-workflow-trial/follow-through-refresh-YYYY-MM-DD.md`
- updated `../crm-2026-05-product-workflow-trial/evidence-log.csv`
- updated `../crm-2026-05-product-workflow-trial/expectation-map.csv` if valuation changed
- updated `../crm-2026-05-product-workflow-trial/workflow-scorecard.csv`
- updated `public-readiness-audit.md`
- review-log entry

Use:

- `templates/follow-through-refresh.md`
- `g04-follow-through-intake-checklist.csv`

## Execution Packet

Before a later event occurs, dry-run the execution packet:

```bash
python3 ../../scripts/build_follow_through_packet.py --dry-run
```

After the later event occurs and source materials are available, export the packet:

```bash
python3 ../../scripts/build_follow_through_packet.py --output exports/mira-follow-through-packet
```

The builder should select `CRM_2026` by default while it remains the highest-priority waiting event. This packet does not clear G04; it only packages the assignment, trigger tracker, template, validation scripts and original CRM case materials for execution.

## Refresh Validation

After the completed refresh is written, run:

```bash
python3 ../../scripts/validate_follow_through_refresh.py \
  --refresh ../crm-2026-05-product-workflow-trial/follow-through-refresh-YYYY-MM-DD.md \
  --original-cutoff 2026-05-30 \
  --evidence-log ../crm-2026-05-product-workflow-trial/evidence-log.csv \
  --intake g04-follow-through-intake-checklist.csv \
  --gate-tracker public-release-gate-tracker.csv \
  --public-readiness-audit public-readiness-audit.md \
  --review-log ../../memory/methodologies/review-log.csv
```

See:

- `g04-follow-through-refresh-validation-standard.md`

This command must exit 0 before G04 can be marked complete.

## G04 Clearing Rule

G04 can clear only if:

- `qualifies_as_true_follow_through: yes`;
- event date is after original memo cutoff;
- evidence log has new source rows dated after the original cutoff;
- before and after action labels are present;
- refresh trigger quality is evaluated;
- public-grade impact states `follow_through_gate_status: pass`;
- release gate tracker points G04 evidence to the completed refresh file.

If the refresh is only a source-gap cleanup, same-window update, or commentary refresh, G04 remains blocked.

## Current Status

Ready to execute after later event. Not completed.

## Refresh Conditions

- stale_after: 2026-06-30
- must_refresh_if: CRM publishes Q2 FY2027 earnings/product metrics, another tracked case publishes a later material event first, or external reviewer says CRM is not the right first G04 case.
