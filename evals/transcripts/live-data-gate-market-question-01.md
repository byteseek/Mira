# 今天目前大盘是调整还是崩盘？

| 字段 | 值 |
| --- | --- |
| `interaction_mode` | `quick_answer` |
| `depth_mode` | `quick_map` |
| `live_data_gate` | `required_quote_time` |
| `research_object` | broad market indexes |
| `time_boundary` | 今天 / 目前 / 同日盘中 |
| `source_boundary` | 必须先搜索或刷新同日行情源；至少记录一个行情源和一个交叉验证来源，无法交叉验证则降级 |
| `quote_time` | 需要写明，例如 `2026-06-05T10:07:00-04:00`；若只有新闻源则写 `publish_time` |
| `live_freshness_status` | `live` / `delayed` / `stale` / `unavailable` |
| `cross_check_status` | `passed` / `partial` / `failed` |

这个问题不能凭印象回答。"今天"、"目前"、"大盘"、"调整还是崩盘"都是实时 / 同日市场判断触发词。Mira 必须先刷新或搜索可用来源，记录时间戳、来源边界和交叉验证状态，再给结论。行情/指数类走 `required_quote_time`；宏观发布或新闻发布且无盘中报价时走 `required_publish_time`。

如果只能拿到一个延迟聚合行情源，输出应写成：

- `live_freshness_status`: `delayed`
- `cross_check_status`: `partial`
- `source_boundary`: 单一延迟源，结论只能是 quick_map，不升级为 durable market call
- `stale_after`: 30-60 分钟或盘中出现更大波动时

判断时先列事实，再列推断：指数跌幅、VIX/波动率、市场宽度和是否有跨资产压力是事实层；"调整 / sharp selloff / crash" 是 judgment。若缺少 quote_time、publish_time 或 source_boundary，应降级为 `needs_refresh` / `source_gap`，不能直接说"崩盘"或"没事"。
