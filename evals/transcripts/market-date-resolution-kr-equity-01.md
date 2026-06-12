# Market-Date Resolution: Korea Equity

不能直接按美国日期取“今日韩股”。这个问题是韩国股票同日行情判断：

| field | value |
| --- | --- |
| `research_object` | Samsung Electronics / 005930.KS |
| `market_scope` | KR equities |
| `time_boundary` | today / same-session quote |
| `user_local_datetime` | 2026-06-11, US local time |
| `market_timezone` | `Asia/Seoul` |
| `market_session_date` | 2026-06-12 |
| `live_data_gate` | `required_quote_time` |

执行顺序：先用首尔市场日解析“今天”，再刷新三星电子 quote。若只能取得延迟行情，必须写明 `live_freshness_status=delayed`；若无法取得带时间戳行情，则输出 `source_gap` / `needs_refresh`。用户本地日期不能替代行情日期，不能用美国 6 月 11 日当作韩国股票 `market_session_date`。

正确的 source note 形状应类似：

- `quote_time`: 2026-06-12Txx:xx:xx+09:00, source shown as live/delayed.
- `as_of_date`: 2026-06-12 for the Korea market session.
- `stale_after`: 韩国市场下一次盘中刷新、收盘后报价变化，或 source quote time 超过可接受延迟。

判断层再写：

- Facts: 三星电子的价格、涨跌幅、成交量或相对 KOSPI 表现，全部绑定 quote time。
- Inferences: 价格走势可能对应的事件/市场环境，新闻只能解释 catalyst，不能替代 quote。
- Judgment: “今天强/弱/震荡”的结论必须降级到 source freshness 允许的置信度。
