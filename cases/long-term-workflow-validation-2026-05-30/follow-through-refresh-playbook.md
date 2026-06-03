# Follow-Through Refresh Playbook

- created: 2026-05-30
- purpose: convert pending refresh triggers into a reproducible post-memo follow-through process
- status: ready_to_run_not_completed

## Why This Exists

The methodology is not public-grade until at least one live case is refreshed after a later material event.

The LLY source-gap refresh was useful, but it does not count because it used evidence inside the original research window. A valid follow-through refresh must use a later event that could change the thesis state.

## Valid Follow-Through Event

A refresh qualifies only if:

1. the event occurs after the original memo cutoff;
2. the event is material to a named thesis variable;
3. the refresh uses new source evidence, not just updated commentary;
4. the refresh states whether the action label changed;
5. the refresh evaluates whether the original `must_refresh_if` was specific enough.

## Preferred First Refresh

Use `CRM_2026` first if available.

Reason:

- CRM has the clearest product-to-company monetization blocker.
- Q2 FY2027 should directly test Agentforce/Data 360 metrics, organic acceleration and margin guide.
- It also tests the expectation-map unavailable-data exception.

Fallback order:

1. `ETN_2026`
2. `VRT_2026`
3. `LLY_2026`
4. `HUMANOID_2026`

## Refresh Steps

1. Open the original memo, evidence log, expectation map and workflow scorecard.
2. Record the original action label and weakest lens.
3. Add new event sources to the evidence log.
4. Update only the thesis variables affected by the event.
5. Compare before/after state:
   - source quality
   - key metric
   - expectation burden
   - stop rule
   - action label
6. Decide whether the original refresh trigger was:
   - too vague
   - specific enough
   - too strict
   - missing a key variable
7. Update the public-readiness audit.

## Required Output

For the first true follow-through refresh, create:

- `follow-through-refresh-YYYY-MM-DD.md`
- updated `evidence-log.csv`
- updated `expectation-map.csv`, if valuation changed
- updated `workflow-scorecard.csv`
- updated `public-readiness-audit.md`
- review-log entry

## Refresh Result Labels

Use one:

- `thesis_strengthened_action_unchanged`
- `thesis_strengthened_action_upgraded`
- `thesis_weakened_action_unchanged`
- `thesis_weakened_action_downgraded`
- `source_gap_closed_action_unchanged`
- `refresh_trigger_failed_too_vague`
- `refresh_trigger_failed_wrong_variable`

## Public-Grade Gate

The follow-through gate passes only if:

- a later event exists;
- all durable new claims have source trail;
- before/after action label is explicit;
- the refresh evaluates the original refresh trigger;
- an independent reviewer can reproduce the refresh logic.

## Current Status

No true follow-through refresh has been completed.

Current tracker:

- `follow-through-trigger-tracker.csv`
- `g04-follow-through-execution-tracker.csv`

G04 execution packet:

- `g04-follow-through-handoff-2026-05-30.md`
- `g04-follow-through-intake-checklist.csv`
- `crm-g04-follow-through-assignment.md`
- `scripts/build_follow_through_packet.py`
- `scripts/validate_follow_through_execution_tracker.py`

Default packet:

```bash
python3 scripts/build_follow_through_packet.py --output exports/mira-follow-through-packet
```

Explicit live-case overrides:

```bash
python3 scripts/build_follow_through_packet.py --case-id ETN_2026 --output exports/mira-follow-through-packet-etn
python3 scripts/build_follow_through_packet.py --case-id VRT_2026 --output exports/mira-follow-through-packet-vrt
python3 scripts/build_follow_through_packet.py --case-id LLY_2026 --output exports/mira-follow-through-packet-lly
```

## Refresh Conditions

- stale_after: 2026-06-30
- must_refresh_if: any tracked case reports a later material event or an external reviewer says a refresh trigger is too vague to execute.
