#!/usr/bin/env python3
"""Build or dry-run the G04 follow-through execution packet.

The packet packages the preferred waiting follow-through case, validation
standard, intake checklist and refresh template. It prepares execution after a
later material event; it does not validate a completed refresh or clear G04.
"""

from __future__ import annotations

import argparse
import csv
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATION_DIR = Path("cases/long-term-workflow-validation-2026-05-30")
TRIGGER_TRACKER = VALIDATION_DIR / "follow-through-trigger-tracker.csv"
DEFAULT_OUTPUT = Path("exports/mira-follow-through-packet")

PRIORITY_ORDER = {
    "highest": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
}

COMMON_PACKET_PATHS = [
    VALIDATION_DIR / "follow-through-trigger-tracker.csv",
    VALIDATION_DIR / "g04-follow-through-event-watch-calendar.csv",
    VALIDATION_DIR / "g04-later-event-candidate-screen.csv",
    VALIDATION_DIR / "g04-follow-through-execution-tracker.csv",
    VALIDATION_DIR / "follow-through-refresh-playbook.md",
    VALIDATION_DIR / "g04-follow-through-handoff-2026-05-30.md",
    VALIDATION_DIR / "g04-follow-through-intake-checklist.csv",
    VALIDATION_DIR / "g04-follow-through-refresh-validation-standard.md",
    Path("templates/follow-through-refresh.md"),
    Path("scripts/validate_follow_through_refresh.py"),
    Path("scripts/validate_follow_through_trigger_tracker.py"),
    Path("scripts/validate_g04_later_event_candidate_screen.py"),
    Path("scripts/validate_follow_through_execution_tracker.py"),
]

CASE_PACKET_PATHS = {
    "ETN_2026": [
        Path("cases/etn-2026-05-long-term-workflow-trial/evidence-log.csv"),
        Path("cases/etn-2026-05-long-term-workflow-trial/expectation-map.csv"),
        Path("cases/etn-2026-05-long-term-workflow-trial/workflow-scorecard.csv"),
        Path("cases/etn-2026-05-long-term-workflow-trial/investment-memo.md"),
        Path("cases/etn-2026-05-long-term-workflow-trial/case-notes.md"),
    ],
    "VRT_2026": [
        Path("cases/vrt-2026-05-long-term-workflow-trial/evidence-log.csv"),
        Path("cases/vrt-2026-05-long-term-workflow-trial/expectation-map.csv"),
        Path("cases/vrt-2026-05-long-term-workflow-trial/workflow-scorecard.csv"),
        Path("cases/vrt-2026-05-long-term-workflow-trial/investment-memo.md"),
        Path("cases/vrt-2026-05-long-term-workflow-trial/case-notes.md"),
    ],
    "CRM_2026": [
        VALIDATION_DIR / "crm-g04-follow-through-assignment.md",
        Path("cases/crm-2026-05-product-workflow-trial/evidence-log.csv"),
        Path("cases/crm-2026-05-product-workflow-trial/expectation-map.csv"),
        Path("cases/crm-2026-05-product-workflow-trial/workflow-scorecard.csv"),
        Path("cases/crm-2026-05-product-workflow-trial/investment-memo.md"),
        Path("cases/crm-2026-05-product-workflow-trial/case-notes.md"),
    ],
    "LLY_2026": [
        Path("cases/lly-2026-05-glp1-workflow-dry-run/evidence-log.csv"),
        Path("cases/lly-2026-05-glp1-workflow-dry-run/expectation-map.csv"),
        Path("cases/lly-2026-05-glp1-workflow-dry-run/workflow-scorecard.csv"),
        Path("cases/lly-2026-05-glp1-workflow-dry-run/investment-memo.md"),
        Path("cases/lly-2026-05-glp1-workflow-dry-run/case-notes.md"),
        Path("cases/lly-2026-05-glp1-workflow-dry-run/payer-access-net-price-check.csv"),
        Path("cases/lly-2026-05-glp1-workflow-dry-run/source-gap-refresh-2026-05-30.md"),
    ],
}

CASE_DIRS = {
    "ETN_2026": "cases/etn-2026-05-long-term-workflow-trial",
    "VRT_2026": "cases/vrt-2026-05-long-term-workflow-trial",
    "CRM_2026": "cases/crm-2026-05-product-workflow-trial",
    "LLY_2026": "cases/lly-2026-05-glp1-workflow-dry-run",
}


@dataclass
class Issue:
    severity: str
    subject: str
    message: str

    def render(self) -> str:
        return f"{self.severity}: {self.subject}: {self.message}"


@dataclass
class PacketItem:
    source_path: Path
    export_path: Path
    item_role: str


def read_tracker() -> tuple[list[dict[str, str]], list[Issue]]:
    try:
        with (ROOT / TRIGGER_TRACKER).open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    except Exception as exc:
        return [], [Issue("ERROR", str(TRIGGER_TRACKER), f"could not parse CSV: {exc}")]
    if not rows:
        return [], [Issue("ERROR", str(TRIGGER_TRACKER), "trigger tracker has no rows")]
    required = {
        "case_id",
        "ticker",
        "current_action_label",
        "next_event_needed",
        "trigger_metric_or_evidence",
        "expected_source",
        "refresh_priority",
        "current_status",
        "why_it_matters",
        "owner_next_step",
    }
    missing = sorted(required - set(rows[0].keys()))
    if missing:
        return rows, [Issue("ERROR", str(TRIGGER_TRACKER), f"missing columns: {missing}")]
    return rows, []


def select_case(case_id: str | None) -> tuple[dict[str, str] | None, list[Issue]]:
    rows, issues = read_tracker()
    if issues:
        return None, issues
    waiting_rows = [
        row
        for row in rows
        if row.get("current_status", "").strip()
        in {"waiting_for_later_event", "waiting_for_material_disclosure", "ready_to_refresh"}
    ]
    if case_id:
        selected = next((row for row in rows if row.get("case_id", "").strip() == case_id), None)
        if not selected:
            return None, [Issue("ERROR", str(TRIGGER_TRACKER), f"case_id not found: {case_id}")]
        if selected not in waiting_rows:
            return None, [Issue("ERROR", str(TRIGGER_TRACKER), f"case is not waiting/ready: {case_id}")]
        return selected, []

    if not waiting_rows:
        return None, [Issue("ERROR", str(TRIGGER_TRACKER), "no waiting follow-through candidate")]
    waiting_rows.sort(
        key=lambda row: (
            PRIORITY_ORDER.get(row.get("refresh_priority", "").strip(), 99),
            row.get("case_id", "").strip(),
        )
    )
    return waiting_rows[0], []


def build_items(output_dir: Path, case_id: str | None) -> tuple[dict[str, str] | None, list[PacketItem], list[Issue]]:
    selected, issues = select_case(case_id)
    if not selected:
        return None, [], issues

    selected_case_id = selected.get("case_id", "").strip()
    case_paths = CASE_PACKET_PATHS.get(selected_case_id)
    if not case_paths:
        return selected, [], [Issue("ERROR", selected_case_id, "no packet path map for selected case")]

    paths: list[tuple[str, Path]] = []
    paths.extend(("common", path) for path in COMMON_PACKET_PATHS)
    paths.extend(("case", path) for path in case_paths)

    output_root = output_dir.resolve()
    root_resolved = ROOT.resolve()
    items: list[PacketItem] = []
    for role, rel_path in paths:
        source = (ROOT / rel_path).resolve()
        try:
            relative_source = source.relative_to(root_resolved)
        except ValueError:
            issues.append(Issue("ERROR", str(rel_path), "packet path escapes repository"))
            continue
        if not source.exists():
            issues.append(Issue("ERROR", str(rel_path), "packet source missing"))
            continue
        items.append(PacketItem(source, output_root / "files" / relative_source, role))

    if case_id is None and selected_case_id != "CRM_2026":
        issues.append(Issue("ERROR", selected_case_id, "default G04 packet must select CRM_2026"))
    return selected, items, issues


def write_packet_summary(output_dir: Path, selected: dict[str, str], items: list[PacketItem]) -> None:
    selected_case_id = selected.get("case_id", "").strip()
    case_dir = CASE_DIRS.get(selected_case_id, "cases/CASE_ID")
    summary = output_dir / "follow-through-packet-summary.md"
    lines = [
        "# Follow-Through Packet Summary",
        "",
        f"- case_id: `{selected.get('case_id', '').strip()}`",
        f"- ticker: `{selected.get('ticker', '').strip()}`",
        f"- current_action_label: `{selected.get('current_action_label', '').strip()}`",
        f"- next_event_needed: {selected.get('next_event_needed', '').strip()}",
        f"- trigger_metric_or_evidence: {selected.get('trigger_metric_or_evidence', '').strip()}",
        f"- expected_source: {selected.get('expected_source', '').strip()}",
        f"- refresh_priority: {selected.get('refresh_priority', '').strip()}",
        f"- current_status: {selected.get('current_status', '').strip()}",
        "",
        "## Execution",
        "",
        "Before drafting a refresh, update the later-event candidate screen and run:",
        "",
        "```bash",
        "python3 scripts/validate_g04_later_event_candidate_screen.py",
        "```",
        "",
        "Draft the refresh only when the candidate screen marks `later_event_available`, `selected_for_refresh: yes` and `refresh_allowed: yes` for the selected case. Scheduled future events, monitored events and packet exports are not completed G04 evidence.",
        "",
        "After drafting the refresh, run:",
        "",
        "```bash",
        "python3 scripts/validate_follow_through_refresh.py \\",
        f"  --refresh {case_dir}/follow-through-refresh-YYYY-MM-DD.md \\",
        "  --original-cutoff 2026-05-30 \\",
        f"  --evidence-log {case_dir}/evidence-log.csv \\",
        "  --intake cases/long-term-workflow-validation-2026-05-30/g04-follow-through-intake-checklist.csv \\",
        "  --gate-tracker cases/long-term-workflow-validation-2026-05-30/public-release-gate-tracker.csv \\",
        "  --public-readiness-audit cases/long-term-workflow-validation-2026-05-30/public-readiness-audit.md \\",
        "  --review-log memory/methodologies/review-log.csv",
        "```",
        "",
        "This packet does not clear G04 by itself.",
        "",
    ]
    summary.write_text("\n".join(lines), encoding="utf-8")

    manifest = output_dir / "follow-through-packet-export-manifest.csv"
    with manifest.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["item_role", "source_path", "export_path"])
        writer.writeheader()
        for item in items:
            writer.writerow(
                {
                    "item_role": item.item_role,
                    "source_path": str(item.source_path.relative_to(ROOT.resolve())),
                    "export_path": str(item.export_path.relative_to(output_dir.resolve())),
                }
            )


def export_packet(output_dir: Path, selected: dict[str, str], items: list[PacketItem]) -> list[Issue]:
    if output_dir.exists() and any(output_dir.iterdir()):
        return [Issue("ERROR", str(output_dir), "output directory exists and is not empty")]
    output_dir.mkdir(parents=True, exist_ok=True)
    issues: list[Issue] = []
    for item in items:
        item.export_path.parent.mkdir(parents=True, exist_ok=True)
        if item.source_path.is_dir():
            if item.export_path.exists():
                issues.append(Issue("ERROR", str(item.export_path), "export directory already exists"))
                continue
            shutil.copytree(item.source_path, item.export_path)
        else:
            shutil.copy2(item.source_path, item.export_path)
    if not issues:
        write_packet_summary(output_dir, selected, items)
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-id", help="follow-through tracker case_id to export")
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="destination directory for a real packet export",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate and summarize packet contents without writing files",
    )
    args = parser.parse_args()

    output_dir = Path(args.output)
    selected, items, issues = build_items(output_dir, args.case_id)
    if selected and not args.dry_run and not issues:
        issues.extend(export_packet(output_dir, selected, items))

    errors = [issue for issue in issues if issue.severity == "ERROR"]
    for issue in issues:
        print(issue.render())
    print("follow_through_packet_export:")
    print(f"  export_ready: {str(not errors).lower()}")
    print(f"  dry_run: {str(args.dry_run).lower()}")
    print(f"  output: {output_dir}")
    print(f"  selected_case: {selected.get('case_id', '').strip() if selected else ''}")
    print(f"  packet_items: {len(items)}")
    print(f"  errors: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
