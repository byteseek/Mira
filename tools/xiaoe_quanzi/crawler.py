#!/usr/bin/env python3
"""Crawl a 小鹅通 (xiaoe-tech) 圈子 feed list and archive to local disk.

Reads cookies from your already-running Chrome via browser_cookie3 (no manual
export needed). Walks the get_feeds_list paginated API, saves raw JSON pages,
emits one markdown per feed, and optionally downloads images/files.

Usage example:
    python3 tools/xiaoe_quanzi/crawler.py \\
        --community-id c_6544c6eb39716_hWkqHZtW8807 \\
        --app-id appyuf4rl772054 \\
        --feeds-list-type nav_ff8f2c600f60dbc6a0a3713e1a34c624 \\
        --out archives/xiaoe-ray-quanzi/2026-05-07 \\
        --download-images --download-files
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests

API_HOST = "quanzi.xiaoe-tech.com"
API_PATH = "/xe.community.community_service/small_community/xe.community/get_feeds_list/1.1.0"


def load_cookies(domain: str = "xiaoe-tech.com", browser: str = "chrome") -> requests.cookies.RequestsCookieJar:
    """Load cookies for the given domain from a running browser."""
    try:
        import browser_cookie3
    except ImportError:
        sys.exit("browser_cookie3 not installed. Run: pip3 install --user browser_cookie3")

    loader = getattr(browser_cookie3, browser, None)
    if loader is None:
        sys.exit(f"Unknown browser {browser!r}. Try chrome/safari/firefox/edge.")
    cj = loader(domain_name=domain)
    jar = requests.cookies.RequestsCookieJar()
    for c in cj:
        jar.set(c.name, c.value, domain=c.domain, path=c.path)
    if not jar:
        sys.exit(
            f"No cookies found for {domain!r} in {browser}. "
            "Make sure you've logged in to the site in that browser."
        )
    return jar


def make_session(jar: requests.cookies.RequestsCookieJar, referer: str) -> requests.Session:
    s = requests.Session()
    s.cookies = jar
    s.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0 Safari/537.36"
        ),
        "Accept": "application/json, text/plain, */*",
        "Referer": referer,
        "Origin": f"https://{API_HOST}",
    })
    return s


def fetch_page(
    session: requests.Session,
    *,
    app_id: str,
    community_id: str,
    feeds_list_type: str,
    page: int,
    page_size: int = 20,
) -> dict[str, Any]:
    params = {
        "app_id": app_id,
        "community_id": community_id,
        "feeds_list_type": feeds_list_type,
        "order_filed": "created_at",
        "hide_exercise": 1,
        "page": page,
        "page_size": page_size,
        "created_start_at": "",
        "created_end_at": "",
    }
    url = f"https://{API_HOST}{API_PATH}"
    r = session.get(url, params=params, timeout=30)
    r.raise_for_status()
    j = r.json()
    if j.get("code") != 0:
        raise RuntimeError(f"API error code={j.get('code')} msg={j.get('msg')}")
    return j


# ---------- formatting ----------

SAFE_NAME_RE = re.compile(r"[^\w一-鿿.\-]+")


def safe_filename(s: str, fallback: str = "untitled") -> str:
    s = SAFE_NAME_RE.sub("_", s).strip("_")
    return s or fallback


def feed_to_markdown(it: dict[str, Any]) -> str:
    content = it.get("content") or {}
    text = content.get("text") or ""
    records = content.get("mix_records") or []
    imgs = [r.get("url") for r in records if r.get("type") == "IMAGE"]
    vids = [r for r in records if r.get("type") == "VIDEO"]
    audios = content.get("audio_records") or []
    files = it.get("file_json") or []
    if isinstance(files, str):
        try:
            files = json.loads(files)
        except json.JSONDecodeError:
            files = []
    tags = re.findall(r"#[^#\s\"]+", it.get("tags_content") or "")

    form = classify_form(it)
    lines = [
        f"# {it.get('title') or '(无标题)'}",
        "",
        f"- **形式**: {form}",
        f"- **作者**: {it.get('nick_name')} · {it.get('role_name') or ''}".rstrip(" ·"),
        f"- **时间**: {it.get('show_time')} · {it.get('ip') or ''}".rstrip(" ·"),
        f"- **标签**: {' '.join(tags) or '-'}",
        f"- **统计**: 👍 {it.get('zan_num', 0)} / 💬 {it.get('comment_count', 0)} / 🔄 {it.get('share_num', 0)}",
        f"- **feed_id**: {it.get('id')}",
        f"- **feeds_type**: {it.get('feeds_type')}",
        f"- **created_at**: {it.get('created_at')}",
        "",
        "## 正文",
        "",
        text or "(空)",
        "",
    ]
    if imgs:
        lines.append(f"## 图片 ({len(imgs)})")
        lines.append("")
        for i, u in enumerate(imgs, 1):
            lines.append(f"![img{i}]({u})")
        lines.append("")
    if vids:
        lines.append(f"## 视频 ({len(vids)})")
        lines.append("")
        for i, v in enumerate(vids, 1):
            poster = v.get("showUrl")
            if poster:
                lines.append(f"封面: ![poster{i}]({poster})")
            lines.append(f"视频{i}: <{v.get('url')}>")
        lines.append("")
    if audios:
        lines.append(f"## 音频 ({len(audios)})")
        lines.append("")
        for i, a in enumerate(audios, 1):
            lines.append(f"音频{i}: <{a.get('url') or a}>")
        lines.append("")
    if files:
        lines.append(f"## 文件 ({len(files)})")
        lines.append("")
        for f in files:
            name = f.get("name") or "file"
            lines.append(
                f"- {name} · {f.get('size', 0)} bytes · {f.get('fileType', '?')} "
                f"· 下载 {f.get('down_num', 0)} · <{f.get('url') or ''}>"
            )
        lines.append("")
    return "\n".join(lines)


def classify_form(it: dict[str, Any]) -> str:
    content = it.get("content") or {}
    records = content.get("mix_records") or []
    has_img = any(r.get("type") == "IMAGE" for r in records)
    has_vid = any(r.get("type") == "VIDEO" for r in records)
    has_audio = bool(content.get("audio_records"))
    files = it.get("file_json")
    has_file = bool(files) and (
        (isinstance(files, list) and len(files) > 0)
        or (isinstance(files, str) and files not in ("", "[]"))
        or bool(it.get("file_url"))
    )
    text_len = len(content.get("text") or "")
    if has_file:
        return "文件帖"
    if has_vid:
        return "视频帖"
    if has_audio:
        return "音频帖"
    if has_img:
        return "短文+图" if text_len < 80 else "长文+图"
    if text_len < 50:
        return "短文（无媒体）"
    if text_len >= 300:
        return "长文（无媒体）"
    return "中等文（无媒体）"


# ---------- archive ----------

@dataclass
class CrawlConfig:
    community_id: str
    app_id: str
    feeds_list_type: str
    out_dir: Path
    page_size: int = 20
    max_pages: int | None = None
    sleep: float = 0.3
    download_images: bool = False
    download_files: bool = False
    download_videos: bool = False  # m3u8 — usually skipped
    role_filter: str | None = None  # e.g. "圈主"


@dataclass
class Manifest:
    fetched_at: str
    community_id: str
    app_id: str
    feeds_list_type: str
    feed_ids: list[str] = field(default_factory=list)
    last_cursor: str | None = None
    pages_fetched: int = 0


def load_manifest(path: Path) -> Manifest | None:
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    return Manifest(**data)


def save_manifest(path: Path, m: Manifest) -> None:
    path.write_text(json.dumps(m.__dict__, ensure_ascii=False, indent=2))


def feed_filename(it: dict[str, Any]) -> str:
    created = (it.get("created_at") or it.get("show_time") or "").split(" ")[0] or "unknown"
    title = safe_filename((it.get("title") or "")[:30], fallback="")
    fid = it.get("id") or "unknown"
    return f"{created}_{fid}{('_' + title) if title else ''}.md"


def download_to(session: requests.Session, url: str, dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 0:
        return True
    try:
        r = session.get(url, timeout=60, stream=True)
        r.raise_for_status()
        dest.parent.mkdir(parents=True, exist_ok=True)
        with dest.open("wb") as f:
            for chunk in r.iter_content(chunk_size=64 * 1024):
                if chunk:
                    f.write(chunk)
        return True
    except Exception as e:
        print(f"  ! download failed: {url} -> {e}", file=sys.stderr)
        return False


def archive_feed(session: requests.Session, cfg: CrawlConfig, it: dict[str, Any]) -> Path:
    feeds_dir = cfg.out_dir / "feeds"
    feeds_dir.mkdir(parents=True, exist_ok=True)
    md_path = feeds_dir / feed_filename(it)
    md_path.write_text(feed_to_markdown(it))

    if cfg.download_images:
        records = (it.get("content") or {}).get("mix_records") or []
        imgs = [r.get("url") for r in records if r.get("type") == "IMAGE" and r.get("url")]
        for i, u in enumerate(imgs, 1):
            ext = Path(urlparse(u).path).suffix or ".jpg"
            dest = cfg.out_dir / "media" / "images" / it["id"] / f"{i:02d}{ext}"
            download_to(session, u, dest)

    if cfg.download_files:
        files = it.get("file_json") or []
        if isinstance(files, str):
            try:
                files = json.loads(files)
            except json.JSONDecodeError:
                files = []
        for f in files:
            url = f.get("url")
            if not url:
                continue
            name = safe_filename(f.get("name") or "file", fallback="file")
            dest = cfg.out_dir / "media" / "files" / it["id"] / name
            download_to(session, url, dest)

    return md_path


# ---------- main ----------

def crawl(cfg: CrawlConfig) -> None:
    cfg.out_dir.mkdir(parents=True, exist_ok=True)
    raw_dir = cfg.out_dir / "raw"
    raw_dir.mkdir(exist_ok=True)
    manifest_path = cfg.out_dir / "manifest.json"
    manifest = load_manifest(manifest_path) or Manifest(
        fetched_at="",
        community_id=cfg.community_id,
        app_id=cfg.app_id,
        feeds_list_type=cfg.feeds_list_type,
    )
    seen = set(manifest.feed_ids)

    referer = (
        f"https://{API_HOST}/{cfg.community_id}/feed_list?app_id={cfg.app_id}"
    )
    jar = load_cookies()
    session = make_session(jar, referer)

    page = 1
    last_cursor = None
    new_count = 0
    while True:
        if cfg.max_pages is not None and page > cfg.max_pages:
            print(f"reached --max-pages={cfg.max_pages}")
            break
        print(f"page {page} ...", flush=True)
        try:
            j = fetch_page(
                session,
                app_id=cfg.app_id,
                community_id=cfg.community_id,
                feeds_list_type=cfg.feeds_list_type,
                page=page,
                page_size=cfg.page_size,
            )
        except requests.HTTPError as e:
            print(f"  ! HTTP error: {e}", file=sys.stderr)
            break

        data = j.get("data") or {}
        items: list[dict[str, Any]] = data.get("list") or []
        if not items:
            print("  (empty page, stop)")
            break

        # save raw
        raw_path = raw_dir / f"page_{page:03d}.json"
        raw_path.write_text(json.dumps(j, ensure_ascii=False, indent=2))

        # archive each feed (filter / dedup / save md)
        for it in items:
            if cfg.role_filter and it.get("role_name") != cfg.role_filter:
                continue
            fid = it.get("id")
            if not fid or fid in seen:
                continue
            seen.add(fid)
            archive_feed(session, cfg, it)
            new_count += 1

        cursor = data.get("cursor")
        if cursor and cursor == last_cursor:
            print("  (cursor stuck, stop)")
            break
        last_cursor = cursor

        if len(items) < cfg.page_size:
            print(f"  (short page {len(items)} < {cfg.page_size}, last page)")
            break

        page += 1
        time.sleep(cfg.sleep)

    manifest.feed_ids = sorted(seen)
    manifest.last_cursor = last_cursor
    manifest.pages_fetched = page
    manifest.fetched_at = time.strftime("%Y-%m-%d %H:%M:%S")
    save_manifest(manifest_path, manifest)

    write_index(cfg.out_dir, manifest)
    print(f"\ndone. new_feeds={new_count} total_in_manifest={len(manifest.feed_ids)}")


def write_index(out_dir: Path, m: Manifest) -> None:
    feeds_dir = out_dir / "feeds"
    files = sorted(feeds_dir.glob("*.md")) if feeds_dir.exists() else []
    forms_count: dict[str, int] = {}
    rows: list[tuple[str, str, str]] = []
    for p in files:
        head = p.read_text().splitlines()[:5]
        title = head[0].lstrip("# ").strip() if head else p.stem
        form = ""
        for line in head:
            if line.startswith("- **形式**"):
                form = line.split(":", 1)[1].strip()
                break
        forms_count[form] = forms_count.get(form, 0) + 1
        rows.append((p.name, title, form))

    lines = [
        f"# 圈子归档索引",
        "",
        f"- 抓取时间: {m.fetched_at}",
        f"- community_id: `{m.community_id}`",
        f"- app_id: `{m.app_id}`",
        f"- feeds_list_type: `{m.feeds_list_type}`",
        f"- 总条数: {len(m.feed_ids)}",
        "",
        "## 形式分布",
        "",
        "| 形式 | 数量 |",
        "|---|---|",
    ]
    for form, n in sorted(forms_count.items(), key=lambda kv: -kv[1]):
        lines.append(f"| {form or '(未分类)'} | {n} |")
    lines += ["", "## 全部帖子（按文件名/时间倒序）", ""]
    for name, title, form in sorted(rows, reverse=True):
        lines.append(f"- [{title}](feeds/{name}) · _{form}_")
    (out_dir / "index.md").write_text("\n".join(lines) + "\n")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--community-id", required=True)
    p.add_argument("--app-id", required=True)
    p.add_argument("--feeds-list-type", required=True, help="e.g. nav_ff8f2c... (visible in network calls)")
    p.add_argument("--out", required=True, help="output directory")
    p.add_argument("--page-size", type=int, default=20)
    p.add_argument("--max-pages", type=int, default=None)
    p.add_argument("--sleep", type=float, default=0.3)
    p.add_argument("--role-filter", default=None, help="only archive posts where role_name == this (e.g. 圈主)")
    p.add_argument("--download-images", action="store_true")
    p.add_argument("--download-files", action="store_true")
    p.add_argument("--download-videos", action="store_true")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    cfg = CrawlConfig(
        community_id=args.community_id,
        app_id=args.app_id,
        feeds_list_type=args.feeds_list_type,
        out_dir=Path(args.out),
        page_size=args.page_size,
        max_pages=args.max_pages,
        sleep=args.sleep,
        role_filter=args.role_filter,
        download_images=args.download_images,
        download_files=args.download_files,
        download_videos=args.download_videos,
    )
    crawl(cfg)


if __name__ == "__main__":
    main()
