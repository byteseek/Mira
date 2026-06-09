# Field Delta (净减负 guard)

- locked: 2026-06-09, after Stage 1.
- the 净减负 metric is the **hot-path field/gate/pause count the model EMITS**, not document length.
  Doc length is allowed to grow if emitted surface does not.

## Per-intervention

| intervention | doc length | new emitted fields | new gate/pause | net |
| --- | --- | --- | --- | --- |
| ① adversarial pass | +~10 lines | **0** (explicitly output-invisible; feeds existing `must_refresh_if` / `reversal_condition` / `source_gap`) | **none** — a sub-step of the *existing* Final Strong-Habit Gate, not a new checkpoint | 0 |
| ② reasoning chain | +~14 lines | **0** (chain outputs map to existing `evidence-log` rows + existing downgrade states) | none | **−1 section** (2 descriptive → 1 procedural) |
| ③ quant traps | +~15 lines | **0** (gates existing calc fields; the decision-relevance gate ADDS A WAIVE PATH) | none — adds a waive, not a stop | 0 (arguably negative) |

## Aggregate

- **Net emitted hot-path field delta: 0** (≤ 0 ✓). No new visible field, no new gate, no new pause across all three.
- **Net section delta: −1** (intervention ② consolidates two descriptive sections into one procedural one — consolidation over addition, per the design stance).
- Document length grows ~39 lines total across three files; this is internal reasoning guidance, not emitted surface, so it does not count against 净减负.

## Verification hook

The harder guard is behavioral, not static: re-running `evals/BASELINE` after any merge must stay
12/12. A drop signals that the added reasoning text quietly changed emitted behavior — caught in
Stage 3, not assumed here.
