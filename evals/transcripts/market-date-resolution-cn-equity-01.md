# Market-Date Resolution: China A-Share

不能直接按美国日期取“今日 A 股”。这个问题是 A 股同日行情判断：

| field | value |
| --- | --- |
| `research_object` | Kweichow Moutai / 600519.SH |
| `market_scope` | CN A-share |
| `time_boundary` | today / same-session quote |
| `user_local_datetime` | 2026-06-11, US local time |
| `market_timezone` | `Asia/Shanghai` |
| `market_session_date` | 2026-06-12 |
| `live_data_gate` | `required_quote_time` |

执行顺序：先用上海市场日解析“今天”，再刷新贵州茅台 quote。若只能取得延迟行情，必须写明 `live_freshness_status=delayed`；若无法取得带时间戳行情，则输出 `source_gap` / `needs_refresh`。用户本地日期不能替代行情日期，不能用美国 6 月 11 日当作 A 股 `market_session_date`。

正确的 source note 形状应类似：

- `quote_time`: 2026-06-12Txx:xx:xx+08:00, source shown as live/delayed.
- `as_of_date`: 2026-06-12 for the China A-share market session.
- `stale_after`: A 股下一次盘中刷新、收盘后报价变化，或 source quote time 超过可接受延迟。

判断层再写：

- Facts: 贵州茅台的价格、涨跌幅、成交量或相对沪深基准表现，全部绑定 quote time。
- Inferences: 价格走势可能对应的事件/市场环境，新闻只能解释 catalyst，不能替代 quote。
- Judgment: “今天强/弱/震荡”的结论必须降级到 source freshness 允许的置信度。
