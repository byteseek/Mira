# 样本：Ray哥的理财圈子（圈主"一束光线"发帖形式）

抓取时间：2026-05-07
数据源：`https://quanzi.xiaoe-tech.com/c_6544c6eb39716_hWkqHZtW8807/feed_list`
API：`xe.community/get_feeds_list/1.1.0`（cursor/page 分页，page_size=20）

## 当前已抓取

- 已抓 feed 数：1200（全部 role_name=圈主，均为"一束光线"本人发布）
- 时间范围：2025-06-30 ~ 2026-05-07（约 10 个月，背景仍在继续往更早时间爬）

## 圈主帖按形式分布（截至 1200 条）

| # | 形式 | 数量 | 样本文件 |
|---|---|---|---|
| 1 | 长文+图 | 486 | [01-长文+图.md](01-长文+图.md) |
| 2 | 视频帖 | 357 | [02-视频帖.md](02-视频帖.md) |
| 3 | 短文+图 | 47 | [03-短文+图.md](03-短文+图.md) |
| 4 | 中等文（无媒体） | 130 | [04-中等文（无媒体）.md](04-中等文（无媒体）.md) |
| 5 | 长文（无媒体） | 152 | [05-长文（无媒体）.md](05-长文（无媒体）.md) |
| 6 | 文件帖 | 2 | [06-文件帖.md](06-文件帖.md) |
| 7 | 短文（无媒体） | 26 | [07-短文（无媒体）.md](07-短文（无媒体）.md) |

分类规则（按优先级）：
1. `file_json[]` 非空 → **文件帖**
2. `mix_records[].type === 'VIDEO'` → **视频帖**
3. `audio_records[]` 非空 → **音频帖**（暂未发现）
4. 含 IMAGE：正文 <80 字 → **短文+图**；≥80 字 → **长文+图**
5. 无媒体：<50 字 → **短文**；≥300 字 → **长文**；其余 → **中等文**

## 字段映射（API → markdown）

| API 字段 | 含义 |
|---|---|
| `id` | feed_id（去重键） |
| `nick_name` / `role_name` / `ip` | 作者/角色/IP 归属地 |
| `show_time` / `created_at` | 显示时间 / 服务器时间戳 |
| `title` | 帖子标题（首行/正文头部派生） |
| `content.text` | 纯文本正文（已展开，无截断） |
| `org_content` | 富文本原始内容（含 emoji/标签结构，未保留到 md） |
| `tags_content` | 圈子标签结构（JSON 字符串，按需解析） |
| `content.mix_records[]` | 媒体列表，`type` ∈ {IMAGE, VIDEO}，含 `url`/`showUrl` |
| `content.audio_records[]` | 音频 |
| `file_json[]` | 文件附件，含 `name`/`url`/`size`/`fileType`/`down_num` |
| `zan_num` / `comment_count` / `share_num` | 互动统计 |
| `feeds_type` | 1=普通；其余暂未见 |

## 已知/待解决

- **媒体 URL** 已去除 querystring（防止安全层拦截），重新拉取需要带签名参数才能下载（图片/视频是否公开可访问待验证）
- **"展开"折叠** 不影响：API 直接返回完整 `content.text`
- **标签**：当前 markdown 标签字段为空——`tags_content` 是 JSON 字符串而非简单 `#xxx` 串，需另解析
- **org_content** 未保留：可后续加（保留富文本结构）
- **总条数** 还在抓，不止 1200 条；下一步要把全部抓完后落库
