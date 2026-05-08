#!/usr/bin/env python3
"""Build per-month digest markdowns from raw/page_*.json.

Each digest contains every post that month, sorted by time, rendered inline
(text + media URLs). Much nicer to read continuously than browsing the
flat feeds/ directory.

Usage:
    python3 tools/xiaoe_quanzi/digest.py \\
        --out archives/xiaoe-ray-quanzi/2026-05-07 \\
        [--role-filter 圈主]
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

from crawler import classify_form  # type: ignore


def iter_feeds(out_dir: Path) -> list[dict[str, Any]]:
    raw_dir = out_dir / "raw"
    if not raw_dir.exists():
        return []
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for page_path in sorted(raw_dir.glob("page_*.json")):
        try:
            data = json.loads(page_path.read_text())
        except json.JSONDecodeError:
            continue
        for it in (data.get("data") or {}).get("list") or []:
            fid = it.get("id")
            if not fid or fid in seen:
                continue
            seen.add(fid)
            out.append(it)
    return out


def month_key(it: dict[str, Any]) -> str:
    s = it.get("created_at") or ""
    m = re.match(r"(\d{4})-(\d{2})", s)
    return f"{m.group(1)}-{m.group(2)}" if m else "unknown"


def render_post(it: dict[str, Any]) -> str:
    content = it.get("content") or {}
    text = (content.get("text") or "").strip()
    records = content.get("mix_records") or []
    imgs = [r.get("url") for r in records if r.get("type") == "IMAGE" and r.get("url")]
    vids = [r for r in records if r.get("type") == "VIDEO"]
    files = it.get("file_json") or []
    if isinstance(files, str):
        try:
            files = json.loads(files)
        except json.JSONDecodeError:
            files = []
    tags = [f"#{t.get('tag_name')}" for t in (it.get("tags") or []) if t.get("tag_name")]
    form = classify_form(it)
    region = it.get("ip_place") or it.get("ip") or ""
    title = it.get("title") or "(无标题)"
    time_s = it.get("created_at") or it.get("show_time") or ""

    parts = [
        f"### {time_s} · {title}",
        "",
        f"_{form}_ · {region} · "
        f"👍 {it.get('zan_num',0)} 💬 {it.get('comment_count',0)} 🔄 {it.get('share_num',0)} · "
        f"`{it.get('id')}`",
        "",
    ]
    if tags:
        parts.append(" ".join(tags))
        parts.append("")
    if text:
        parts.append(text)
        parts.append("")
    if imgs:
        for u in imgs:
            parts.append(f"![]({u})")
        parts.append("")
    if vids:
        for v in vids:
            poster = v.get("showUrl")
            if poster:
                parts.append(f"封面: ![]({poster})")
            parts.append(f"视频: <{v.get('url')}>")
        parts.append("")
    if files:
        for f in files:
            parts.append(f"📄 [{f.get('name', 'file')}]({f.get('url', '')}) · {f.get('size',0)} bytes · 下载 {f.get('down_num',0)}")
        parts.append("")
    return "\n".join(parts)


def render_month(month: str, items: list[dict[str, Any]]) -> str:
    items = sorted(items, key=lambda x: x.get("created_at") or "")
    forms_count: dict[str, int] = {}
    tag_count: dict[str, int] = {}
    for it in items:
        forms_count[classify_form(it)] = forms_count.get(classify_form(it), 0) + 1
        for t in (it.get("tags") or []):
            n = t.get("tag_name")
            if n:
                tag_count[f"#{n}"] = tag_count.get(f"#{n}", 0) + 1
    head = [
        f"# {month} · 圈子月度文摘",
        "",
        f"- 帖数: {len(items)}",
        f"- 形式: " + "  ".join(f"{f}×{c}" for f, c in sorted(forms_count.items(), key=lambda kv: -kv[1])),
    ]
    if tag_count:
        top_tags = sorted(tag_count.items(), key=lambda kv: -kv[1])[:8]
        head.append("- 热门标签: " + "  ".join(f"{t}×{c}" for t, c in top_tags))
    head += ["", "---", ""]
    body = "\n".join(render_post(it) for it in items)
    return "\n".join(head) + body


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--out", required=True)
    p.add_argument("--role-filter", default=None)
    args = p.parse_args()

    out = Path(args.out)
    feeds = iter_feeds(out)
    if args.role_filter:
        feeds = [f for f in feeds if f.get("role_name") == args.role_filter]

    by_month: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for it in feeds:
        by_month[month_key(it)].append(it)

    digest_dir = out / "monthly"
    digest_dir.mkdir(exist_ok=True)
    for month, items in sorted(by_month.items()):
        if month == "unknown":
            continue
        (digest_dir / f"{month}.md").write_text(render_month(month, items))

    # write digest index
    index_lines = [
        f"# 月度文摘索引",
        "",
        "| 月份 | 帖数 |",
        "|---|---|",
    ]
    for month, items in sorted(by_month.items()):
        if month == "unknown":
            continue
        index_lines.append(f"| [{month}](monthly/{month}.md) | {len(items)} |")
    (out / "monthly_index.md").write_text("\n".join(index_lines) + "\n")
    print(f"wrote {len(by_month)} monthly digests to {digest_dir}/ and monthly_index.md")


if __name__ == "__main__":
    main()
