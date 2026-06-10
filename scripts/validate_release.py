#!/usr/bin/env python3
"""Validate release-gate artifacts for a case directory.

Consolidated replacement for the 2026-05-30 long-term release pipeline
(~39 scripts, removed 2026-06-10; recoverable from git history). It keeps the
four durable gate semantics — objective readiness, goal completion, go/no-go
gate coverage and release freshness — parameterized by case directory instead
of hardcoded paths.

Usage:
  python3 scripts/validate_release.py cases/<case-dir> [--as-of YYYY-MM-DD]
      [--require-external-ready]

Default mode validates record integrity and discipline: required headers,
non-empty key fields, evidence paths that exist, and blocking items carrying
a next action. An honest record of an incomplete release passes.

--require-external-ready additionally fails on any blocked/incomplete/
not-ready status or unresolved gate blocker. Use it for a real
external-release go decision.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OBJECTIVE_AUDIT = "objective-readiness-audit.csv"
GOAL_AUDIT = "goal-completion-audit.csv"
GATE_TRACKER = "public-release-gate-tracker.csv"

OBJECTIVE_HEADERS = {"requirement_id", "completion_status", "evidence_path", "next_action"}
GOAL_HEADERS = {"component_id", "current_state", "evidence_path", "next_action"}
TRACKER_HEADERS = {"gate_id", "gate", "required_for_external_release", "current_status", "evidence_path"}

SATISFIED_PREFIXES = ("met_", "proved_", "pass", "ready_")
BLOCKING_PREFIXES = ("blocked", "incomplete", "not_ready", "failed", "missing")

STALE_AFTER_RE = re.compile(r"stale_after:?\s*\**\s*(\d{4}-\d{2}-\d{2})")


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    stats: dict[str, object] = field(default_factory=dict)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def classify_status(value: str) -> str:
    token = value.strip().lower()
    if any(token.startswith(prefix) for prefix in BLOCKING_PREFIXES):
        return "blocking"
    if any(token.startswith(prefix) for prefix in SATISFIED_PREFIXES):
        return "satisfied"
    return "unknown"


def read_rows(path: Path, required_headers: set[str], report: Report) -> list[dict[str, str]]:
    try:
        with path.open(encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            headers = set(reader.fieldnames or [])
            missing = required_headers - headers
            if missing:
                report.error(f"{path.name}: missing required headers {sorted(missing)}")
                return []
            return [row for row in reader]
    except OSError as exc:
        report.error(f"{path.name}: could not read ({exc})")
        return []


def check_evidence_path(name: str, row_id: str, value: str, report: Report) -> None:
    if not value.strip():
        report.error(f"{name}: {row_id}: empty evidence_path")
        return
    if not (ROOT / value.strip()).exists():
        report.error(f"{name}: {row_id}: evidence_path does not exist: {value.strip()}")


def check_objective_readiness(case_dir: Path, report: Report, strict: bool) -> None:
    path = case_dir / OBJECTIVE_AUDIT
    rows = read_rows(path, OBJECTIVE_HEADERS, report)
    blocking = 0
    for row in rows:
        row_id = row.get("requirement_id", "").strip() or "<missing requirement_id>"
        if row_id == "<missing requirement_id>":
            report.error(f"{OBJECTIVE_AUDIT}: row with empty requirement_id")
        check_evidence_path(OBJECTIVE_AUDIT, row_id, row.get("evidence_path", ""), report)
        status = row.get("completion_status", "").strip()
        if not status:
            report.error(f"{OBJECTIVE_AUDIT}: {row_id}: empty completion_status")
            continue
        kind = classify_status(status)
        if kind == "unknown":
            report.warn(f"{OBJECTIVE_AUDIT}: {row_id}: unrecognized completion_status `{status}`")
        if kind == "blocking":
            blocking += 1
            if not row.get("next_action", "").strip():
                report.error(f"{OBJECTIVE_AUDIT}: {row_id}: blocking status `{status}` without next_action")
            if strict:
                report.error(f"{OBJECTIVE_AUDIT}: {row_id}: not external-ready (`{status}`)")
    report.stats["objective_requirements"] = len(rows)
    report.stats["objective_blocking"] = blocking


def check_goal_completion(case_dir: Path, report: Report, strict: bool, tracker_gate_ids: set[str]) -> None:
    path = case_dir / GOAL_AUDIT
    rows = read_rows(path, GOAL_HEADERS, report)
    blocked = 0
    for row in rows:
        row_id = row.get("component_id", "").strip() or "<missing component_id>"
        if row_id == "<missing component_id>":
            report.error(f"{GOAL_AUDIT}: row with empty component_id")
        check_evidence_path(GOAL_AUDIT, row_id, row.get("evidence_path", ""), report)
        state = row.get("current_state", "").strip()
        if not state:
            report.error(f"{GOAL_AUDIT}: {row_id}: empty current_state")
            continue
        kind = classify_status(state)
        if kind == "unknown":
            report.warn(f"{GOAL_AUDIT}: {row_id}: unrecognized current_state `{state}`")
        if kind == "blocking":
            blocked += 1
            if not row.get("next_action", "").strip():
                report.error(f"{GOAL_AUDIT}: {row_id}: blocking state `{state}` without next_action")
            if strict:
                report.error(f"{GOAL_AUDIT}: {row_id}: not external-ready (`{state}`)")
        blocking_gate = row.get("blocking_gate", "").strip()
        if blocking_gate and tracker_gate_ids:
            for gate_ref in re.split(r"[|,;]\s*", blocking_gate):
                if gate_ref and gate_ref not in tracker_gate_ids:
                    report.warn(f"{GOAL_AUDIT}: {row_id}: blocking_gate `{gate_ref}` not found in {GATE_TRACKER}")
    report.stats["goal_components"] = len(rows)
    report.stats["goal_blocked"] = blocked


def check_gate_tracker(case_dir: Path, report: Report, strict: bool) -> set[str]:
    path = case_dir / GATE_TRACKER
    rows = read_rows(path, TRACKER_HEADERS, report)
    gate_ids: set[str] = set()
    required = 0
    with_blockers = 0
    for row in rows:
        gate_id = row.get("gate_id", "").strip() or "<missing gate_id>"
        if gate_id == "<missing gate_id>":
            report.error(f"{GATE_TRACKER}: row with empty gate_id")
        else:
            gate_ids.add(gate_id)
        if row.get("required_for_external_release", "").strip().lower() != "yes":
            continue
        required += 1
        check_evidence_path(GATE_TRACKER, gate_id, row.get("evidence_path", ""), report)
        status = row.get("current_status", "").strip()
        if not status:
            report.error(f"{GATE_TRACKER}: {gate_id}: empty current_status")
        blocker = row.get("remaining_blocker", "").strip()
        if blocker:
            with_blockers += 1
            if not row.get("next_action", "").strip():
                report.error(f"{GATE_TRACKER}: {gate_id}: remaining_blocker without next_action")
            if strict:
                report.error(f"{GATE_TRACKER}: {gate_id}: unresolved blocker: {blocker}")
        elif strict and classify_status(status) != "satisfied":
            report.error(f"{GATE_TRACKER}: {gate_id}: not external-ready (`{status}`)")
    report.stats["required_gates"] = required
    report.stats["gates_with_blockers"] = with_blockers
    return gate_ids


def check_freshness(case_dir: Path, report: Report, as_of: dt.date) -> None:
    documents = 0
    for path in sorted(case_dir.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        dates = STALE_AFTER_RE.findall(text)
        if not dates:
            continue
        documents += 1
        for raw in dates:
            try:
                stale_after = dt.date.fromisoformat(raw)
            except ValueError:
                report.error(f"{path.relative_to(case_dir)}: invalid stale_after date `{raw}`")
                continue
            if stale_after < as_of:
                report.error(
                    f"{path.relative_to(case_dir)}: stale_after {raw} is before as-of date {as_of.isoformat()}"
                )
    report.stats["freshness_documents_checked"] = documents


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("case_dir", help="case directory containing release-gate artifacts")
    parser.add_argument("--as-of", default=None, help="freshness reference date YYYY-MM-DD (default: today)")
    parser.add_argument(
        "--require-external-ready",
        action="store_true",
        help="fail on any blocked/incomplete status or unresolved gate blocker",
    )
    args = parser.parse_args()

    case_dir = (ROOT / args.case_dir).resolve() if not Path(args.case_dir).is_absolute() else Path(args.case_dir)
    if not case_dir.is_dir():
        print(f"ERROR: case directory not found: {args.case_dir}")
        return 1

    if args.as_of is None:
        as_of = dt.date.today()
    else:
        try:
            as_of = dt.date.fromisoformat(args.as_of)
        except ValueError:
            print(f"ERROR: --as-of must be YYYY-MM-DD, got `{args.as_of}`")
            return 1

    report = Report()
    strict = args.require_external_ready

    gate_artifacts = [OBJECTIVE_AUDIT, GOAL_AUDIT, GATE_TRACKER]
    present = [name for name in gate_artifacts if (case_dir / name).exists()]
    if not present:
        print(f"ERROR: {args.case_dir}: no release-gate artifacts found ({', '.join(gate_artifacts)})")
        return 1
    for name in gate_artifacts:
        if name not in present:
            report.warn(f"{name}: not present; gate skipped")

    tracker_gate_ids: set[str] = set()
    if GATE_TRACKER in present:
        tracker_gate_ids = check_gate_tracker(case_dir, report, strict)
    if OBJECTIVE_AUDIT in present:
        check_objective_readiness(case_dir, report, strict)
    if GOAL_AUDIT in present:
        check_goal_completion(case_dir, report, strict, tracker_gate_ids)
    check_freshness(case_dir, report, as_of)

    for message in report.errors:
        print(f"ERROR: {message}")
    for message in report.warnings:
        print(f"WARN: {message}")

    external_ready = not strict or not report.errors
    blocking_total = int(report.stats.get("objective_blocking", 0) or 0) + int(
        report.stats.get("goal_blocked", 0) or 0
    ) + int(report.stats.get("gates_with_blockers", 0) or 0)

    print("release_gate_validation:")
    print(f"  case: {args.case_dir}")
    print(f"  as_of: {as_of.isoformat()}")
    print(f"  mode: {'require_external_ready' if strict else 'record_integrity'}")
    print(f"  gates_present: {len(present)}/3")
    for key in (
        "objective_requirements",
        "objective_blocking",
        "goal_components",
        "goal_blocked",
        "required_gates",
        "gates_with_blockers",
        "freshness_documents_checked",
    ):
        if key in report.stats:
            print(f"  {key}: {report.stats[key]}")
    print(f"  blocking_total: {blocking_total}")
    if strict:
        print(f"  external_ready: {str(external_ready and not report.errors).lower()}")
    print(f"  errors: {len(report.errors)}")
    print(f"  warnings: {len(report.warnings)}")
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
