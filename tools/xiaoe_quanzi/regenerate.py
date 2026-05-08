#!/usr/bin/env python3
"""Regenerate feeds/<id>.md from previously-saved raw/page_*.json.

Useful after improving the markdown formatter or adding new fields — no need
to re-fetch the API.

Usage:
    python3 tools/xiaoe_quanzi/regenerate.py \\
        --out archives/xiaoe-ray-quanzi/2026-05-07 \\
        [--role-filter 圈主]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from crawler import feed_to_markdown, feed_filename  # type: ignore


def regenerate(out_dir: Path, role_filter: str | None) -> int:
    raw_dir = out_dir / "raw"
    feeds_dir = out_dir / "feeds"
    feeds_dir.mkdir(parents=True, exist_ok=True)
    seen: set[str] = set()
    n = 0
    for page_path in sorted(raw_dir.glob("page_*.json")):
        try:
            data = json.loads(page_path.read_text())
        except json.JSONDecodeError:
            continue
        for it in (data.get("data") or {}).get("list") or []:
            if role_filter and it.get("role_name") != role_filter:
                continue
            fid = it.get("id")
            if not fid or fid in seen:
                continue
            seen.add(fid)
            md_path = feeds_dir / feed_filename(it)
            md_path.write_text(feed_to_markdown(it))
            n += 1
    return n


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--out", required=True)
    p.add_argument("--role-filter", default=None)
    args = p.parse_args()
    n = regenerate(Path(args.out), args.role_filter)
    print(f"regenerated {n} markdown files in {args.out}/feeds/")


if __name__ == "__main__":
    main()
