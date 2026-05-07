# xiaoe_quanzi crawler

Archive a 小鹅通 (xiaoe-tech) 圈子 feed list to local disk. Reads cookies
straight from your already-running Chrome, walks the paginated API, and
writes one markdown per feed plus optional media downloads.

## Setup

```bash
pip3 install --user -r tools/xiaoe_quanzi/requirements.txt
```

Make sure you're logged in to the target 圈子 in Chrome — the crawler
borrows that session's cookies, so no manual export is needed.

> macOS may prompt you (once) to grant Keychain access so
> `browser_cookie3` can decrypt Chrome's cookie jar. Approve it.

## Find the parameters

Open the 圈子 in Chrome, then DevTools → Network → filter `feed`. Look
at the `get_feeds_list/1.1.0` request URL:

```
https://quanzi.xiaoe-tech.com/.../get_feeds_list/1.1.0
  ?app_id=appyuf4rl772054
  &community_id=c_6544c6eb39716_hWkqHZtW8807
  &feeds_list_type=nav_ff8f2c600f60dbc6a0a3713e1a34c624
  &page=1&page_size=10
```

Pull `app_id`, `community_id`, `feeds_list_type` from there.
`feeds_list_type` is the active tab/filter — different sub-tabs (动态 /
精选 / 课程) have different values.

## Run

```bash
python3 tools/xiaoe_quanzi/crawler.py \
    --community-id c_6544c6eb39716_hWkqHZtW8807 \
    --app-id appyuf4rl772054 \
    --feeds-list-type nav_ff8f2c600f60dbc6a0a3713e1a34c624 \
    --out archives/xiaoe-ray-quanzi/2026-05-07 \
    --role-filter 圈主 \
    --download-images --download-files
```

### Useful flags

| flag | effect |
|---|---|
| `--max-pages N` | stop after N pages (good for smoke tests) |
| `--page-size N` | API page size (default 20) |
| `--sleep S` | seconds between page requests (default 0.3) |
| `--role-filter ROLE` | only archive posts where `role_name` matches (e.g. `圈主`) |
| `--download-images` | fetch image files into `media/images/<feed_id>/` |
| `--download-files` | fetch attachment files (PDFs etc.) |
| `--download-videos` | placeholder — videos are HLS m3u8, handle with ffmpeg externally |

## Output layout

```
<out>/
  raw/page_001.json …       # raw API responses (replayable / auditable)
  feeds/<date>_<id>[_title].md
  media/
    images/<feed_id>/01.jpg, 02.jpg …
    files/<feed_id>/<filename>.pdf
  manifest.json             # {feed_ids, last_cursor, fetched_at, …}
  index.md                  # human-readable index + form distribution
```

## Idempotence / incremental updates

`manifest.json` records every feed_id already saved. Re-running the
crawler against the same `--out` skips known feeds and only writes new
markdowns / downloads new media. To re-fetch from scratch, delete the
`<out>` directory.

## Form classification

Each feed is auto-classified into one of:

- `文件帖` — has `file_json[]` attachments
- `视频帖` — has `mix_records[].type == VIDEO`
- `音频帖` — has `audio_records[]`
- `短文+图` / `长文+图` — IMAGE in mix_records (split at 80 chars)
- `短文 / 中等文 / 长文（无媒体）` — pure text (split at 50 / 300 chars)

The form goes into the markdown frontmatter and is summarized in
`index.md` as a count table.

## Notes / limitations

- **Videos**: the API returns HLS m3u8 URLs. Downloading needs `ffmpeg`,
  not in scope here.
- **Cookie freshness**: cookies expire. If you start getting `code != 0`
  responses, log in again in Chrome and rerun.
- **Rate limit**: default 0.3s between pages. If you see HTTP errors,
  bump `--sleep`.
- **Other browsers**: the crawler currently hardcodes Chrome. To use
  Safari/Firefox/Edge, change `load_cookies(..., browser=...)` in
  `crawler.py`.
