#!/usr/bin/env python3
"""Post-crawl analysis: read raw/page_*.json and produce a stats report.

Outputs <out>/stats.md with:
- posting cadence by month
- form distribution
- top tags (parsed from tags_content JSON)
- top-N most-engaged posts (zan + comment + share)
- IP-region distribution
- media volume

Usage:
    python3 tools/xiaoe_quanzi/analyze.py --out archives/xiaoe-ray-quanzi/2026-05-07
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

from crawler import classify_form  # type: ignore


def iter_feeds(out_dir: Path) -> Iterable[dict[str, Any]]:
    raw_dir = out_dir / "raw"
    if not raw_dir.exists():
        return
    seen: set[str] = set()
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
            yield it


def parse_tags(it: dict[str, Any]) -> list[str]:
    """Real tags live in it['tags'] as [{tag_name, ...}, ...]."""
    tags_arr = it.get("tags") or []
    return [f"#{t.get('tag_name')}" for t in tags_arr if t.get("tag_name")]


def month_of(it: dict[str, Any]) -> str:
    s = it.get("created_at") or it.get("show_time") or ""
    m = re.match(r"(\d{4})-(\d{2})", s)
    if m:
        return f"{m.group(1)}-{m.group(2)}"
    return "unknown"


def engagement(it: dict[str, Any]) -> int:
    return int(it.get("zan_num", 0)) + int(it.get("comment_count", 0)) + int(it.get("share_num", 0))


def media_counts(it: dict[str, Any]) -> tuple[int, int, int]:
    recs = (it.get("content") or {}).get("mix_records") or []
    n_img = sum(1 for r in recs if r.get("type") == "IMAGE")
    n_vid = sum(1 for r in recs if r.get("type") == "VIDEO")
    files = it.get("file_json") or []
    if isinstance(files, str):
        try:
            files = json.loads(files)
        except json.JSONDecodeError:
            files = []
    n_file = len(files) if isinstance(files, list) else 0
    return n_img, n_vid, n_file


def render_report(out_dir: Path, role_filter: str | None) -> str:
    feeds = list(iter_feeds(out_dir))
    if role_filter:
        feeds = [f for f in feeds if f.get("role_name") == role_filter]
    feeds.sort(key=lambda x: x.get("created_at") or "", reverse=True)

    n = len(feeds)
    by_month: Counter[str] = Counter()
    by_form: Counter[str] = Counter()
    tag_counter: Counter[str] = Counter()
    ip_counter: Counter[str] = Counter()
    total_imgs = total_vids = total_files = 0
    text_lens: list[int] = []
    for it in feeds:
        by_month[month_of(it)] += 1
        by_form[classify_form(it)] += 1
        for t in parse_tags(it):
            tag_counter[t] += 1
        place = it.get("ip_place") or it.get("ip")
        if place:
            ip_counter[place] += 1
        n_img, n_vid, n_file = media_counts(it)
        total_imgs += n_img
        total_vids += n_vid
        total_files += n_file
        text_lens.append(len((it.get("content") or {}).get("text") or ""))
    text_lens.sort()
    avg_len = sum(text_lens) / len(text_lens) if text_lens else 0
    median_len = text_lens[len(text_lens) // 2] if text_lens else 0

    top_engaged = sorted(feeds, key=engagement, reverse=True)[:15]

    lines = [
        f"# 圈子归档统计",
        "",
        f"- 帖子总数: **{n}**" + (f"（仅 role_name={role_filter!r}）" if role_filter else ""),
        f"- 时间范围: {feeds[-1].get('created_at') if feeds else '?'} ~ {feeds[0].get('created_at') if feeds else '?'}",
        f"- 正文长度: avg {avg_len:.0f} / median {median_len} / max {text_lens[-1] if text_lens else 0}",
        f"- 媒体总量: 图片 {total_imgs} · 视频 {total_vids} · 文件 {total_files}",
        "",
        "## 形式分布",
        "",
        "| 形式 | 数量 | 占比 |",
        "|---|---|---|",
    ]
    for form, c in by_form.most_common():
        lines.append(f"| {form} | {c} | {c / n * 100:.1f}% |")
    lines += ["", "## 月度发帖量", "", "| 月份 | 数量 |", "|---|---|"]
    for m in sorted(by_month):
        lines.append(f"| {m} | {by_month[m]} |")
    lines += ["", "## Top 标签 (前 20)", "", "| 标签 | 出现次数 |", "|---|---|"]
    for tag, c in tag_counter.most_common(20):
        lines.append(f"| {tag} | {c} |")
    lines += ["", "## IP 归属地分布 (前 15)", "", "| IP/地区 | 数量 |", "|---|---|"]
    for ip, c in ip_counter.most_common(15):
        lines.append(f"| {ip} | {c} |")
    lines += ["", "## 互动最高的 15 条", "", "| 时间 | 标题 | 👍 | 💬 | 🔄 | 形式 |", "|---|---|---|---|---|---|"]
    for it in top_engaged:
        lines.append(
            f"| {it.get('created_at', '')[:10]} | {(it.get('title') or '')[:30]} "
            f"| {it.get('zan_num', 0)} | {it.get('comment_count', 0)} | {it.get('share_num', 0)} "
            f"| {classify_form(it)} |"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--out", required=True, help="archive directory (must contain raw/page_*.json)")
    p.add_argument("--role-filter", default=None)
    args = p.parse_args()
    out = Path(args.out)
    report = render_report(out, args.role_filter)
    target = out / "stats.md"
    target.write_text(report)
    print(f"wrote {target}")


if __name__ == "__main__":
    main()
