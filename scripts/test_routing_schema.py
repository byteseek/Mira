#!/usr/bin/env python3
"""Regression tests for the routing-card schema checker in validate_repo.py.

Run: python3 scripts/test_routing_schema.py  (or `just test`)

These lock the conditional-`required` teeth so a guessed enum or a dropped
gate cannot silently regress. The follow-up case in particular guards the
`decision_grade` bypass: the contract (loops/analysis-routing.md line 706)
requires follow-up questions for light/standard/decision_grade, and an earlier
schema used a non-existent `deep` token instead of `decision_grade`.
"""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_repo as V  # noqa: E402

SCHEMA = V._load_schema_doc(V.SCHEMA_DIR / "routing.schema.json")
ROOT = Path(__file__).resolve().parent.parent
VALID = json.loads((ROOT / "cases" / "aapl-2026-04" / "routing.json").read_text())


def errs(card: dict) -> list[str]:
    return V.schema_errors(card, SCHEMA)


def expect_valid(name: str, card: dict) -> None:
    e = errs(card)
    assert not e, f"{name}: expected valid, got {e}"
    print(f"ok  {name}")


def expect_invalid(name: str, card: dict, needle: str = "") -> None:
    e = errs(card)
    assert e, f"{name}: expected validation errors, got none"
    if needle:
        assert any(needle in m for m in e), f"{name}: {needle!r} not in {e}"
    print(f"ok  {name}  ({e[0]})")


def mutate(**changes) -> dict:
    card = copy.deepcopy(VALID)
    for key, value in changes.items():
        if value is V_DROP:
            card.pop(key, None)
        else:
            card[key] = value
    return card


V_DROP = object()


def main() -> int:
    # baseline
    expect_valid("valid golden card (aapl)", VALID)

    # --- the follow-up bypass this test exists for ---
    expect_invalid(
        "decision_grade without followup_questions",
        mutate(followup_prompt_mode="decision_grade", followup_questions=V_DROP),
        "followup_questions",
    )
    expect_valid(
        "decision_grade WITH followup_questions",
        mutate(followup_prompt_mode="decision_grade"),
    )
    expect_invalid(
        "none without followup_waiver_reason",
        mutate(followup_prompt_mode="none", followup_questions=V_DROP),
        "followup_waiver_reason",
    )
    expect_invalid(
        "out-of-vocab followup_prompt_mode",
        mutate(followup_prompt_mode="deep"),
        "not one of",
    )

    # --- other conditional teeth (regression guards) ---
    expect_invalid("out-of-vocab interaction_mode", mutate(interaction_mode="bogus"), "not one of")
    expect_invalid(
        "quant!=none without calculation_gate",
        mutate(quant_dependency="high", calculation_gate=V_DROP),
        "calculation_gate",
    )
    expect_invalid(
        "decision_pressure high + disconfirmation no",
        mutate(decision_pressure="high", disconfirmation_required="no"),
        "disconfirmation_required",
    )
    expect_invalid("empty required string", mutate(routing_basis="   "), "routing_basis")

    print("routing_schema_tests: pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
