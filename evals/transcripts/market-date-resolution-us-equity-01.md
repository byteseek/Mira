# Market-Date Resolution: US Equity

不能直接按中国日期取“今日美股”。这个问题是美股同日行情判断：

| field | value |
| --- | --- |
| `research_object` | AAPL |
| `market_scope` | US equities |
| `time_boundary` | today / same-session quote |
| `user_local_datetime` | 2026-06-12 morning, China time |
| `market_timezone` | `America/New_York` |
| `market_session_date` | 2026-06-11 |
| `live_data_gate` | `required_quote_time` |

执行顺序：先用美东市场日解析“今天”，再刷新 AAPL quote。若只能取得延迟行情，必须写明 `live_freshness_status=delayed`；若无法取得带时间戳行情，则输出 `source_gap` / `needs_refresh`。用户本地日期不能替代行情日期，不能用中国 6 月 12 日当作美股 `market_session_date`。

正确的 source note 形状应类似：

- `quote_time`: 2026-06-11Txx:xx:xx-04:00, source shown as live/delayed.
- `as_of_date`: 2026-06-11 for the US market session.
- `stale_after`: 下一次盘前/盘中刷新、盘后报价变化，或 source quote time 超过可接受延迟。

判断层再写：

- Facts: AAPL 的价格、涨跌幅、成交量或相对大盘表现，全部绑定 quote time。
- Inferences: 价格走势可能对应的事件/市场环境，新闻只能解释 catalyst，不能替代 quote。
- Judgment: “今天强/弱/震荡”的结论必须降级到 source freshness 允许的置信度。
