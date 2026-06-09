# `case_c` Answer Key (reverse control — should NOT downgrade)

- source golden case: `cases/aapl-2026-04/` (a quality-compounder "no new action" memo, **not** a failure case).
- grader-facing only. Test-blind generation agents never see this.
- role: `case_c` exists to catch any arm that **downgrades on a recognized-risk reflex**. The
  hard part is that the *correct* answer is itself a mild "no new action" — so the grader must
  separate **fully-valued quality** (correct) from **broken thesis** (erroneous).

## The correct conclusion

A high-quality, **non-shock** mega-cap platform: strong current fundamentals (rev +16% YoY,
EPS +19%, ~$54B operating cash flow), durable installed base, growing services. Valuation is
**mostly priced-in**, so there is no strong variant edge right now. Correct action state:

> `no_action` / `watch` — quality compounder; conviction medium on business quality, low on
> *new-upside* actionability; valuation anchor is a `source_gap` pending a refreshed model.

Key debate is **"quality but is it cheap?"**, not **"is the business intact?"**.

## What counts as CORRECT (pass)

- Recognizes a durable, non-shock business; does not treat current strength as demand-shock pull-forward.
- May land on `no_action` / `watch` / "mostly priced-in" / "no variant edge now" — this is **correct caution about actionability**, not a thesis downgrade.
- Flags tariff/margin, product-cycle, and the foldable-delay rumor as **monitorable risks** while keeping the platform thesis intact.
- Treats the L5 price data and the April drawdown as market context, and the foldable rumor as an L4 unverified signal — not as thesis-breaking evidence.
- Marks valuation anchor as `source_gap` and asks for a refreshed model before any action.

## What counts as ERRONEOUS DOWNGRADE (fail the reverse control)

- Applies the demand-shock / pull-forward pattern to a business with **no** demand shock
  (e.g., `watch_only_pending_normalized_demand`, "growth is pulled forward", "shock-contaminated").
- Declares the **thesis broken / structurally impaired / avoid / sell**, or assigns a
  distress / kill state.
- Downgrades the **business quality** thesis (as opposed to merely declining to act on
  valuation) on the basis of the April price drawdown or the foldable-delay rumor **alone**.
- Any downgrade whose real basis is a "I recognize this and it will fall" reflex rather than the
  dated facts.

## The decisive distinction (for the grader)

| agent output | verdict |
| --- | --- |
| `no_action` / `watch` because **valuation is mostly priced-in**, business intact | **CORRECT** (this is the golden answer) |
| reasonable caution on tariff / product-cycle risk, thesis kept | **CORRECT** |
| `watch_only_pending_normalized_demand` or shock/pull-forward framing | **ERRONEOUS DOWNGRADE** |
| "thesis broken / avoid / sell / impaired" | **ERRONEOUS DOWNGRADE** |
| downgrade driven by drawdown or rumor alone | **ERRONEOUS DOWNGRADE** |

`downgrade_timing` scoring for `case_c` (per `scoring-rubric.md`): the **golden** answer
(`no_action`/`watch`, business intact, priced-in) scores 4–5; an erroneous downgrade scores 1–2;
a muddled "no_action but for shock-pull-forward reasons" scores 2 (right surface state, wrong
reasoning). Win-rule item 4 fails if **any** run in an arm produces an erroneous downgrade.
