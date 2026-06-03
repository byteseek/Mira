#!/usr/bin/env python3
"""Build the final institutional colleague release packet.

This builder is intentionally gated. It refuses to export while
validate_long_term_release.py --require-external-ready fails. That makes it a
final-release tool, not an internal-candidate sharing shortcut.
"""

from __future__ import annotations

import argparse
import csv
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATION_DIR = Path("cases/long-term-workflow-validation-2026-05-30")
MANIFEST = VALIDATION_DIR / "institutional-release-bundle-manifest.csv"
DEFAULT_OUTPUT = Path("exports/mira-institutional-release-packet")

REQUIRED_COLUMNS = {
    "bundle_section",
    "path",
    "include_in_external_release",
    "required",
    "release_phase",
    "notes",
}

REQUIRED_EXPORT_PATHS = {
    "public-workflow-pack/README.md",
    "public-workflow-pack/workflow.md",
    "public-workflow-pack/fill-guide.md",
    "public-workflow-pack/template-inventory.md",
    "public-workflow-pack/source-appendix.md",
    "public-workflow-pack/analyst-checklist.csv",
    "public-workflow-pack/operator-runbook.md",
    "public-workflow-pack/institutional-colleague-release-notes-template.md",
    "public-workflow-pack/institutional-colleague-acceptance-memo-template.md",
    "public-workflow-pack/institutional-use-boundaries.md",
    "public-workflow-pack/institutional-adoption-faq.md",
    "public-release-decision.md",
    "public-release-gate-tracker.csv",
    "objective-readiness-audit.csv",
    "goal-completion-audit.csv",
    "release-verification-command-manifest.csv",
    "external-release-action-queue.csv",
    "final-release-cutover-checklist.csv",
    "institutional-colleague-acceptance-checklist.csv",
    "release-qa-report-2026-05-30.md",
    "external-reviewer-bundle-manifest.csv",
    "g06-dispatch-readiness-checklist.csv",
    "g06-reviewer-candidate-screen.csv",
    "g06-reviewer-selection-rubric.csv",
    "g06-reviewer-independence-screen.csv",
    "g06-external-review-handoff-2026-05-30.md",
    "trial-theme-matrix.csv",
    "theme-selection-refresh-audit.csv",
    "practice-falsification-audit.csv",
    "methodology-iteration-trace-audit.csv",
    "multi-lens-coverage-audit.csv",
    "g04-follow-through-handoff-2026-05-30.md",
    "follow-through-trigger-tracker.csv",
    "g04-follow-through-event-watch-calendar.csv",
    "g04-later-event-candidate-screen.csv",
    "g04-follow-through-execution-tracker.csv",
    "g05-fy2-fcf-source-upgrade-2026-05-30.md",
    "g05-crm-source-attempts.csv",
    "historical-consensus-source-attempts.csv",
    "historical-consensus-unavailable-data-exception-2026-05-30.md",
}


@dataclass
class Issue:
    severity: str
    subject: str
    message: str

    def render(self) -> str:
        return f"{self.severity}: {self.subject}: {self.message}"


@dataclass
class ReleaseItem:
    manifest_path: str
    source_path: Path
    export_path: Path
    bundle_section: str


def run_check(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True)


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


def validate_release_ready() -> tuple[bool, list[Issue]]:
    issues: list[Issue] = []
    bundle = run_check([sys.executable, "scripts/validate_institutional_release_bundle.py"])
    if bundle.returncode != 0:
        issues.append(
            Issue(
                "ERROR",
                "validate_institutional_release_bundle.py",
                f"institutional bundle validation failed with exit {bundle.returncode}",
            )
        )

    external = run_check([sys.executable, "scripts/validate_long_term_release.py", "--require-external-ready"])
    if external.returncode != 0:
        detail = (external.stdout or external.stderr or "").strip().replace("\n", " | ")
        issues.append(
            Issue(
                "BLOCKED",
                "validate_long_term_release.py --require-external-ready",
                f"external release gate not clear; builder refused export: {detail}",
            )
        )
        return False, issues
    return not any(issue.severity == "ERROR" for issue in issues), issues


def collect_items(output_dir: Path, include_optional: bool) -> tuple[list[ReleaseItem], list[Issue]]:
    rows, issues = read_manifest()
    if issues:
        return [], issues

    root_resolved = ROOT.resolve()
    validation_root = (ROOT / VALIDATION_DIR).resolve()
    output_root = output_dir.resolve()
    items: list[ReleaseItem] = []

    for i, row in enumerate(rows, start=2):
        section = row.get("bundle_section", "").strip()
        rel_value = row.get("path", "").strip()
        include = row.get("include_in_external_release", "").strip()
        required = row.get("required", "").strip()
        phase = row.get("release_phase", "").strip()

        if include not in {"yes", "no", "optional"}:
            issues.append(Issue("ERROR", str(MANIFEST), f"row {i} invalid include value `{include}`"))
        if required not in {"yes", "no"}:
            issues.append(Issue("ERROR", str(MANIFEST), f"row {i} invalid required `{required}`"))
        if phase not in {"external_release_only", "external_release_optional", "template_only", "internal_only"}:
            issues.append(Issue("ERROR", str(MANIFEST), f"row {i} invalid release_phase `{phase}`"))
        if not rel_value:
            issues.append(Issue("ERROR", str(MANIFEST), f"row {i} missing path"))
            continue
        if section == "internal_do_not_send" and include != "no":
            issues.append(Issue("ERROR", str(MANIFEST), f"row {i} internal item is not protected"))
            continue
        should_export = include == "yes" or (include == "optional" and include_optional)
        if not should_export:
            continue

        source = (ROOT / VALIDATION_DIR / rel_value).resolve()
        if not is_relative_to(source, root_resolved):
            issues.append(Issue("ERROR", str(MANIFEST), f"row {i} path escapes repository: {rel_value}"))
            continue
        if should_export and not is_relative_to(source, validation_root):
            issues.append(Issue("ERROR", str(MANIFEST), f"row {i} export path escapes validation directory: {rel_value}"))
            continue
        if required == "yes" and not source.exists():
            issues.append(Issue("ERROR", str(MANIFEST), f"row {i} required path missing: {rel_value}"))
            continue
        if not source.exists():
            continue
        items.append(
            ReleaseItem(
                manifest_path=rel_value,
                source_path=source,
                export_path=output_root / "files" / source.relative_to(root_resolved),
                bundle_section=section,
            )
        )

    if len(items) < 15:
        issues.append(Issue("ERROR", str(MANIFEST), "too few release export items"))
    item_paths = {item.manifest_path for item in items}
    missing_required_exports = sorted(REQUIRED_EXPORT_PATHS - item_paths)
    if missing_required_exports:
        issues.append(Issue("ERROR", str(MANIFEST), f"missing required export paths: {missing_required_exports}"))
    return items, issues


def write_export_manifest(output_dir: Path, items: list[ReleaseItem]) -> None:
    export_manifest = output_dir / "institutional-release-export-manifest.csv"
    with export_manifest.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["bundle_section", "manifest_path", "source_path", "export_path", "item_type"],
        )
        writer.writeheader()
        for item in items:
            writer.writerow(
                {
                    "bundle_section": item.bundle_section,
                    "manifest_path": item.manifest_path,
                    "source_path": str(item.source_path.relative_to(ROOT.resolve())),
                    "export_path": str(item.export_path.relative_to(output_dir.resolve())),
                    "item_type": "directory" if item.source_path.is_dir() else "file",
                }
            )


def export_packet(output_dir: Path, items: list[ReleaseItem]) -> list[Issue]:
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
        write_export_manifest(output_dir, items)
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="destination directory for a real institutional release export",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="check readiness and summarize without writing files",
    )
    parser.add_argument(
        "--include-optional",
        action="store_true",
        help="include manifest rows marked optional after release is externally ready",
    )
    args = parser.parse_args()

    output_dir = Path(args.output)
    release_ready, ready_issues = validate_release_ready()
    items, item_issues = collect_items(output_dir, args.include_optional)
    issues = ready_issues + item_issues
    if release_ready and not args.dry_run and not [i for i in issues if i.severity == "ERROR"]:
        issues.extend(export_packet(output_dir, items))

    errors = [issue for issue in issues if issue.severity == "ERROR"]
    blockers = [issue for issue in issues if issue.severity == "BLOCKED"]
    for issue in issues:
        print(issue.render())
    print("institutional_release_packet_export:")
    print(f"  export_ready: {str(release_ready and not errors and not blockers).lower()}")
    print(f"  dry_run: {str(args.dry_run).lower()}")
    print(f"  output: {output_dir}")
    print(f"  release_items: {len(items)}")
    print(f"  required_export_paths_checked: {len(REQUIRED_EXPORT_PATHS)}")
    print(f"  blockers: {len(blockers)}")
    print(f"  errors: {len(errors)}")
    if blockers:
        return 2
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
