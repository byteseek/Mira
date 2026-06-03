#!/usr/bin/env python3
"""Build or dry-run the G06 external reviewer packet.

The packet is driven only by external-reviewer-bundle-manifest.csv rows where
send_to_reviewer=yes. Internal do-not-send rows are validated but never copied.
This script prepares reviewer assignment logistics; it does not clear G06.
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
MANIFEST = VALIDATION_DIR / "external-reviewer-bundle-manifest.csv"
DEFAULT_OUTPUT = Path("exports/mira-external-reviewer-packet")

REQUIRED_COLUMNS = {
    "bundle_section",
    "path",
    "send_to_reviewer",
    "required",
    "notes",
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
    manifest_path: str
    source_path: Path
    export_path: Path
    is_dir: bool


def is_relative_to(path: Path, base: Path) -> bool:
    try:
        path.relative_to(base)
        return True
    except ValueError:
        return False


def read_manifest() -> tuple[list[dict[str, str]], list[Issue]]:
    try:
        with (ROOT / MANIFEST).open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    except Exception as exc:
        return [], [Issue("ERROR", str(MANIFEST), f"could not parse CSV: {exc}")]
    if not rows:
        return [], [Issue("ERROR", str(MANIFEST), "manifest has no rows")]
    missing = sorted(REQUIRED_COLUMNS - set(rows[0].keys()))
    if missing:
        return rows, [Issue("ERROR", str(MANIFEST), f"missing columns: {missing}")]
    return rows, []


def collect_packet_items(output_dir: Path) -> tuple[list[PacketItem], list[Issue]]:
    issues: list[Issue] = []
    rows, manifest_issues = read_manifest()
    issues.extend(manifest_issues)
    if manifest_issues:
        return [], issues

    root_resolved = ROOT.resolve()
    output_root = output_dir.resolve()
    items: list[PacketItem] = []
    send_count = 0
    internal_send_count = 0

    for i, row in enumerate(rows, start=2):
        section = row.get("bundle_section", "").strip()
        rel_value = row.get("path", "").strip()
        send = row.get("send_to_reviewer", "").strip()
        required = row.get("required", "").strip()

        if send not in {"yes", "no"}:
            issues.append(Issue("ERROR", str(MANIFEST), f"row {i} invalid send_to_reviewer `{send}`"))
        if required not in {"yes", "no", "one_of"}:
            issues.append(Issue("ERROR", str(MANIFEST), f"row {i} invalid required `{required}`"))
        if not rel_value:
            issues.append(Issue("ERROR", str(MANIFEST), f"row {i} missing path"))
            continue
        if section == "internal_do_not_send" and send == "yes":
            internal_send_count += 1
            issues.append(Issue("ERROR", str(MANIFEST), f"row {i} internal_do_not_send marked yes"))
            continue
        if send != "yes":
            continue

        source = (ROOT / VALIDATION_DIR / rel_value).resolve()
        if not is_relative_to(source, root_resolved):
            issues.append(Issue("ERROR", str(MANIFEST), f"row {i} path escapes repository: {rel_value}"))
            continue
        if not source.exists():
            issues.append(Issue("ERROR", str(MANIFEST), f"row {i} send path missing: {rel_value}"))
            continue
        export_path = output_root / "files" / source.relative_to(root_resolved)
        items.append(PacketItem(rel_value, source, export_path, source.is_dir()))
        send_count += 1

    if send_count < 10:
        issues.append(Issue("ERROR", str(MANIFEST), "too few reviewer send items"))
    if internal_send_count:
        issues.append(Issue("ERROR", str(MANIFEST), "internal rows would be exported"))
    return items, issues


def write_export_manifest(output_dir: Path, items: list[PacketItem]) -> None:
    export_manifest = output_dir / "reviewer-packet-export-manifest.csv"
    with export_manifest.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "manifest_path",
                "source_path",
                "export_path",
                "item_type",
            ],
        )
        writer.writeheader()
        for item in items:
            writer.writerow(
                {
                    "manifest_path": item.manifest_path,
                    "source_path": str(item.source_path.relative_to(ROOT.resolve())),
                    "export_path": str(item.export_path.relative_to(output_dir.resolve())),
                    "item_type": "directory" if item.is_dir else "file",
                }
            )


def export_packet(output_dir: Path, items: list[PacketItem]) -> list[Issue]:
    issues: list[Issue] = []
    if output_dir.exists() and any(output_dir.iterdir()):
        return [Issue("ERROR", str(output_dir), "output directory exists and is not empty")]
    output_dir.mkdir(parents=True, exist_ok=True)
    for item in items:
        item.export_path.parent.mkdir(parents=True, exist_ok=True)
        if item.is_dir:
            if item.export_path.exists():
                issues.append(Issue("ERROR", str(item.export_path), "export directory already exists"))
                continue
            shutil.copytree(item.source_path, item.export_path)
        else:
            shutil.copy2(item.source_path, item.export_path)
    if not issues:
        write_export_manifest(output_dir, items)
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="destination directory for a real packet export",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate and summarize export contents without writing files",
    )
    args = parser.parse_args()

    output_dir = Path(args.output)
    items, issues = collect_packet_items(output_dir)
    if not args.dry_run and not issues:
        issues.extend(export_packet(output_dir, items))

    errors = [issue for issue in issues if issue.severity == "ERROR"]
    for issue in issues:
        print(issue.render())
    file_count = sum(1 for item in items if not item.is_dir)
    dir_count = sum(1 for item in items if item.is_dir)
    print("external_review_packet_export:")
    print(f"  export_ready: {str(not errors).lower()}")
    print(f"  dry_run: {str(args.dry_run).lower()}")
    print(f"  output: {output_dir}")
    print(f"  send_items: {len(items)}")
    print(f"  send_files: {file_count}")
    print(f"  send_directories: {dir_count}")
    print(f"  errors: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
