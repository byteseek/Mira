#!/usr/bin/env python3
"""Run Mira's local quality gate.

This is the one-command maintainer check for repository discipline. It avoids
network access by default and reports every sub-check before returning.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PY_COMPILE_TARGETS = [
    "scripts/validate_repo.py",
    "scripts/generate_case_manifests.py",
    "scripts/migrate_evidence_log_v1_to_v1_1.py",
    "scripts/test_repo_validation_contracts.py",
    "scripts/validate_release.py",
]

# Historical regression target for the release gate: the one case that
# exercised the full 2026-05 release workflow (pipeline since removed;
# recoverable from git history).
RELEASE_GATE_CASE = "cases/long-term-workflow-validation-2026-05-30"
RELEASE_GATE_AS_OF = "2026-05-30"


@dataclass
class CheckResult:
    name: str
    passed: bool
    returncode: int
    detail: str = ""
    required: bool = True


def run_command(
    name: str,
    args: list[str],
    expected_codes: set[int],
    *,
    required: bool = True,
) -> CheckResult:
    env = os.environ.copy()
    env.setdefault("PYTHONPYCACHEPREFIX", str(Path(tempfile.gettempdir()) / "mira-pycache"))
    result = subprocess.run(args, cwd=ROOT, env=env, text=True, capture_output=True)
    output = "\n".join(part for part in (result.stdout, result.stderr) if part).strip()
    return CheckResult(
        name=name,
        passed=result.returncode in expected_codes,
        returncode=result.returncode,
        detail=output,
        required=required,
    )


def build_checks(args: argparse.Namespace) -> list[tuple[str, list[str], set[int], bool]]:
    checks: list[tuple[str, list[str], set[int], bool]] = []

    if args.check_updates:
        checks.append(
            ("update_check_local_refs", ["scripts/check_updates.sh", "--no-fetch"], {0, 1}, False)
        )

    checks.extend(
        [
            ("py_compile", [sys.executable, "-m", "py_compile", *PY_COMPILE_TARGETS], {0}, True),
            ("repo_validation_contract_tests", [sys.executable, "scripts/test_repo_validation_contracts.py"], {0}, True),
            ("repo_validation", [sys.executable, "scripts/validate_repo.py"], {0}, True),
        ]
    )

    if not args.skip_long_term:
        checks.append(
            (
                "release_gate",
                [
                    sys.executable,
                    "scripts/validate_release.py",
                    RELEASE_GATE_CASE,
                    "--as-of",
                    RELEASE_GATE_AS_OF,
                ],
                {0},
                True,
            )
        )

    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skip-long-term",
        action="store_true",
        help="skip the release-gate check (scripts/validate_release.py)",
    )
    parser.add_argument(
        "--check-updates",
        action="store_true",
        help="compare local remote-tracking refs without network fetch; advisory only",
    )
    args = parser.parse_args()

    results = [
        run_command(name, command, expected_codes, required=required)
        for name, command, expected_codes, required in build_checks(args)
    ]
    failures = [result for result in results if result.required and not result.passed]

    print("quality_gate:")
    print(f"  passed: {str(not failures).lower()}")
    print(f"  mode: {'fast' if args.skip_long_term else 'full'}")
    print(f"  advisory_update_check: {str(args.check_updates).lower()}")
    print(f"  errors: {len(failures)}")
    print("  results:")
    for result in results:
        status = "pass" if result.passed else "fail"
        required = "required" if result.required else "advisory"
        print(f"    - {result.name}: {status} exit={result.returncode} {required}")
        if not result.passed and result.detail:
            detail = result.detail.replace("\n", "\n        ")
            print(f"        {detail}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
