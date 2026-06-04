#!/usr/bin/env python3
"""Score Mira behavior-level eval cases against real model outputs.

`validate_repo.py` checks *syntax*: are tokens in-vocabulary, are headers
canonical, are dates well-formed. This scorer checks *behavior*: given a Mira
prompt, did the model actually do the thing the contract demands -- run a
disconfirmation under decision pressure, downgrade weak evidence, return an
honest `irreducible_uncertainty` instead of a fake point call, refuse position
sizing without holdings, and so on.

It operationalizes the semantic teeth of `templates/delivery-checklist.md` and
the routing stop rules into machine-checkable assertions over a transcript:

- `must_contain_all`: a list of groups; each group is a list of alternative
  phrases (OR within a group). The case passes a group if ANY alternative is a
  substring of the output. ALL groups must pass.
- `must_not_contain`: forbidden content (anti-sycophancy / no-trade-instruction
  guards). A literal entry is negation-guarded: a hit immediately preceded by a
  negator (不/别/无需/避免/...) does not count, so "不建议加仓" does not trip the
  forbidden phrase "建议加仓". Set guard=false or use regex for strict matching.
- `routing_tokens`: optional `field: value` token checks reused from the
  routing card layer.

Cases live in `evals/behavior-eval-cases.jsonl`. Model outputs (transcripts) are
read from a transcripts directory as `<case-id>.md` or `<case-id>.txt`. A case
with no transcript is reported as MISSING (not a failure) unless --require-all,
so the dataset can grow ahead of recorded outputs.

Usage:
    # score recorded transcripts (zero API needed)
    python3 scripts/score_behavior_eval.py --transcripts evals/transcripts

    # generate then score with your own model CLI ({prompt} is substituted)
    python3 scripts/score_behavior_eval.py --command 'mymodel --stdin' \\
        --save-transcripts evals/transcripts-run

Exit code is non-zero if any error-severity case FAILS, unless --report-only.
"""

from __future__ import annotations

import argparse
import json
import re
import shlex
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path


NEGATORS = (
    "不", "别", "无需", "不要", "避免", "不应", "不能", "勿", "未", "没有",
    "并非", "而不是", "切勿", "无法",
)
NEGATION_WINDOW = 8

PASS = "PASS"
FAIL = "FAIL"
MISS = "MISS"


@dataclass
class Case:
    case_id: str
    prompt: str
    behavior: str
    rationale: str
    severity: str = "error"
    contract_refs: list[str] = field(default_factory=list)
    routing_tokens: dict[str, str] = field(default_factory=dict)
    must_contain_all: list[list[str]] = field(default_factory=list)
    must_not_contain: list[dict] = field(default_factory=list)


@dataclass
class Result:
    case: Case
    status: str
    failures: list[str] = field(default_factory=list)
    transcript_path: Path | None = None


def parse_forbidden(entry: object) -> dict:
    """Normalize a must_not_contain entry to {text, regex, guard, note}."""
    if isinstance(entry, str):
        return {"text": entry, "regex": False, "guard": True, "note": ""}
    if isinstance(entry, dict):
        return {
            "text": entry.get("text", ""),
            "regex": bool(entry.get("regex", False)),
            "guard": bool(entry.get("guard", True)),
            "note": entry.get("note", ""),
        }
    raise ValueError(f"invalid must_not_contain entry: {entry!r}")


def load_cases(path: Path) -> tuple[list[Case], list[str]]:
    cases: list[Case] = []
    errors: list[str] = []
    seen: set[str] = set()
    for i, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{i}: invalid JSON: {exc}")
            continue
        case_id = data.get("id", "")
        if not case_id:
            errors.append(f"{path}:{i}: case missing `id`")
            continue
        if case_id in seen:
            errors.append(f"{path}:{i}: duplicate case id `{case_id}`")
            continue
        seen.add(case_id)
        try:
            forbidden = [parse_forbidden(e) for e in data.get("must_not_contain", [])]
        except ValueError as exc:
            errors.append(f"{path}:{i}: {exc}")
            continue
        cases.append(
            Case(
                case_id=case_id,
                prompt=data.get("prompt", ""),
                behavior=data.get("behavior", ""),
                rationale=data.get("rationale", ""),
                severity=data.get("severity", "error"),
                contract_refs=list(data.get("contract_refs", [])),
                routing_tokens=dict(data.get("routing_tokens", {})),
                must_contain_all=[list(group) for group in data.get("must_contain_all", [])],
                must_not_contain=forbidden,
            )
        )
    return cases, errors


def find_transcript(case_id: str, transcripts_dir: Path) -> Path | None:
    for suffix in (".md", ".txt"):
        candidate = transcripts_dir / f"{case_id}{suffix}"
        if candidate.exists():
            return candidate
    return None


def generate_transcript(prompt: str, command: str) -> str:
    """Run a model CLI, substituting {prompt}; capture stdout as the output."""
    if "{prompt}" in command:
        rendered = command.replace("{prompt}", shlex.quote(prompt))
        completed = subprocess.run(
            rendered, shell=True, capture_output=True, text=True, timeout=600
        )
    else:
        completed = subprocess.run(
            shlex.split(command), input=prompt, capture_output=True, text=True, timeout=600
        )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or "command failed")
    return completed.stdout


def negation_guarded(text: str, start: int) -> bool:
    window = text[max(0, start - NEGATION_WINDOW):start]
    return any(neg in window for neg in NEGATORS)


def check_forbidden(text: str, entry: dict) -> bool:
    """Return True if the forbidden entry really appears (a violation)."""
    needle = entry["text"]
    if not needle:
        return False
    if entry["regex"]:
        for match in re.finditer(needle, text):
            if entry["guard"] and negation_guarded(text, match.start()):
                continue
            return True
        return False
    start = 0
    while True:
        idx = text.find(needle, start)
        if idx == -1:
            return False
        if entry["guard"] and negation_guarded(text, idx):
            start = idx + len(needle)
            continue
        return True


def check_routing_token(text: str, token: str, value: str) -> bool:
    # Accept both `field: value` (card/bullet) and `| field | value |` (table) forms.
    pattern = (
        r"`?" + re.escape(token) + r"`?\s*[:：|]\s*`?" + re.escape(value) + r"`?"
    )
    return re.search(pattern, text) is not None


def score_case(case: Case, output: str, transcript_path: Path | None) -> Result:
    failures: list[str] = []

    for token, value in case.routing_tokens.items():
        if not check_routing_token(output, token, value):
            failures.append(f"routing token not found: `{token}: {value}`")

    for group in case.must_contain_all:
        if not any(alt in output for alt in group):
            failures.append(f"missing required content (any of): {group}")

    for entry in case.must_not_contain:
        if check_forbidden(output, entry):
            label = entry["text"] + (f" ({entry['note']})" if entry["note"] else "")
            failures.append(f"forbidden content present: {label}")

    status = PASS if not failures else FAIL
    return Result(case=case, status=status, failures=failures, transcript_path=transcript_path)


def render(result: Result) -> str:
    head = f"{result.status:4}  {result.case.case_id}  [{result.case.behavior}]"
    if result.status == MISS:
        return head + "  (no transcript)"
    lines = [head]
    for failure in result.failures:
        lines.append(f"        - {failure}")
    return "\n".join(lines)


def run(
    cases: list[Case],
    transcripts_dir: Path | None,
    command: str | None,
    save_dir: Path | None,
) -> list[Result]:
    results: list[Result] = []
    for case in cases:
        output: str | None = None
        transcript_path: Path | None = None

        if command:
            try:
                output = generate_transcript(case.prompt, command)
            except Exception as exc:  # noqa: BLE001 - surfaced as a failure
                results.append(
                    Result(case=case, status=FAIL, failures=[f"generation error: {exc}"])
                )
                continue
            if save_dir:
                save_dir.mkdir(parents=True, exist_ok=True)
                saved = save_dir / f"{case.case_id}.md"
                saved.write_text(output, encoding="utf-8")
                transcript_path = saved
        elif transcripts_dir:
            transcript_path = find_transcript(case.case_id, transcripts_dir)
            if transcript_path:
                output = transcript_path.read_text(encoding="utf-8")

        if output is None:
            results.append(Result(case=case, status=MISS))
            continue

        results.append(score_case(case, output, transcript_path))
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cases", default="evals/behavior-eval-cases.jsonl", help="JSONL eval dataset")
    parser.add_argument("--transcripts", help="directory of recorded <case-id>.md/.txt outputs")
    parser.add_argument("--command", help="model CLI to generate outputs; {prompt} is substituted, else prompt is piped to stdin")
    parser.add_argument("--save-transcripts", help="when generating, also write outputs to this directory")
    parser.add_argument("--require-all", action="store_true", help="treat MISSING transcripts as errors")
    parser.add_argument("--report-only", action="store_true", help="print results but exit 0")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON summary")
    args = parser.parse_args()

    cases_path = Path(args.cases)
    if not cases_path.exists():
        print(f"ERROR: cases file not found: {cases_path}")
        return 2

    cases, load_errors = load_cases(cases_path)
    for err in load_errors:
        print(f"ERROR: {err}")
    if load_errors:
        return 2

    if not args.command and not args.transcripts:
        print("ERROR: provide --transcripts DIR or --command CMD")
        return 2

    transcripts_dir = Path(args.transcripts) if args.transcripts else None
    save_dir = Path(args.save_transcripts) if args.save_transcripts else None
    results = run(cases, transcripts_dir, args.command, save_dir)

    passed = [r for r in results if r.status == PASS]
    failed = [r for r in results if r.status == FAIL]
    missing = [r for r in results if r.status == MISS]
    error_failures = [r for r in failed if r.case.severity == "error"]
    if args.require_all:
        error_failures += [r for r in missing if r.case.severity == "error"]

    if args.json:
        payload = {
            "summary": {
                "total": len(results),
                "passed": len(passed),
                "failed": len(failed),
                "missing": len(missing),
                "errors": len(error_failures),
            },
            "results": [
                {
                    "id": r.case.case_id,
                    "behavior": r.case.behavior,
                    "status": r.status,
                    "severity": r.case.severity,
                    "failures": r.failures,
                }
                for r in results
            ],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for result in results:
            print(render(result))
        print(
            f"summary: {len(passed)} passed, {len(failed)} failed, "
            f"{len(missing)} missing (errors={len(error_failures)})"
        )

    if args.report_only:
        return 0
    return 1 if error_failures else 0


if __name__ == "__main__":
    sys.exit(main())
