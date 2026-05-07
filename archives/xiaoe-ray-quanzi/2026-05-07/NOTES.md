# 抓取笔记 · 2026-05-07

## 当前状态

- **已抓**: 2540 条圈主帖（2024-04-06 → 2026-05-07，约 25 个月）
- **未抓**: page 128 之后的帖子（理论上还应有少量更早的内容；page 127 cursor 仍非空）
- **媒体**: 1.1 GB（图片 4583 + 文件 106 已下载到 `media/`，未提交 git）

## 中断原因

抓到 page 128 时遇到 **本地代理 (FlClash 等) 临时 reset connection**：

```
requests.exceptions.ProxyError: HTTPSConnectionPool(...): Max retries exceeded ...
Caused by ProxyError('Unable to connect to proxy', RemoteDisconnected('Remote end closed connection without response'))
```

之后尝试 resume 时 `browser_cookie3` 在 macOS Keychain 这一步卡死（Keychain 此刻无人响应授权）。已 kill 卡住的进程。

## 恢复方法（明天打开机器后）

```bash
cd /Users/byteseek/Documents/Longmind/market-research-agents
# 确保 Chrome 仍登录在 quanzi.xiaoe-tech.com
python3 tools/xiaoe_quanzi/crawler.py \
  --community-id c_6544c6eb39716_hWkqHZtW8807 \
  --app-id appyuf4rl772054 \
  --feeds-list-type nav_ff8f2c600f60dbc6a0a3713e1a34c624 \
  --out archives/xiaoe-ray-quanzi/2026-05-07 \
  --role-filter 圈主 \
  --download-images --download-files \
  --sleep 0.5
```

行为：
1. **page 1–127 自动跳过**（从 `raw/page_*.json` 缓存读，不打 API）
2. 从 page 128 继续往下抓
3. 每页 5 次重试（指数退避 1/2/4/8/16s）应对临时网络抖动
4. manifest.json 记录已抓 feed_id，重复运行幂等

抓完后再跑：

```bash
python3 tools/xiaoe_quanzi/regenerate.py --out archives/xiaoe-ray-quanzi/2026-05-07 --role-filter 圈主
python3 tools/xiaoe_quanzi/analyze.py    --out archives/xiaoe-ray-quanzi/2026-05-07 --role-filter 圈主
python3 tools/xiaoe_quanzi/digest.py     --out archives/xiaoe-ray-quanzi/2026-05-07 --role-filter 圈主
```

更新 stats.md、monthly digest，覆盖输出。

## 已发现的圈子边界

- 总条数估算：基于 page 127 cursor 仍有，再加 ~5–15 页（100–300 条）应能爬完
- 时间跨度：community 创建时间约 2024-04-06（最早一条）
- 圈主只有 "一束光线" 一人，未见 "嘉宾" / 普通成员发帖

## 其他

- `samples/` 是最初手工挑选的 7 类形式样本，作为格式参考保留
- `media/` 和 `logs/` 在 `archives/.gitignore` 里，不会进 git
- 内容中的图片/视频 URL 来自 xiaoe CDN，公开可访问（去掉签名参数后仍能取）
