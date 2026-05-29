# Valuation And Expectation Overlay

这个 overlay 用于把 thesis 从“方向性判断”推进到“市场已经 price in 什么、需要什么修正才有收益”的量化层。

它不是独立估值模型，也不是目标价机器。它服务于 Mira 的核心问题：

- 当前价格隐含了什么预期？
- Mira 的 view 与市场预期差在哪里？
- 需要 revenue、margin、FCF、multiple 或 risk premium 出现什么变化，thesis 才有实际价值？
- 下行场景和证伪条件是否足够清楚？

## Use When

- `key_debate` 涉及估值是否已经反映质量、成长、风险或主题热度。
- 标的是 large-mega、mid-cap 或已有可用市场估值锚的公司。
- 研究结论需要进入 `thesis-ledger`、`expectation-map` 或 `actionability_bridge`。
- 用户关心“能不能做”“风险收益比”或“是不是已经 price in”。

## Avoid When

- 公司没有稳定财务锚，且只能用叙事或 binary catalyst 定价。
- 基础财务数据缺失，无法形成任何 base/bull/bear 场景。
- 估值数字会给人虚假精度，且无法说明核心假设。

## Required Inputs

- `price_date`
- current price / market cap / enterprise value，按可得性记录
- current multiple: P/E、EV/Sales、EV/EBITDA、P/FCF 或 sector-specific metric
- peer or historical range
- consensus proxy 或 guidance proxy
- Mira base/bull/bear operating assumptions
- downside driver and invalidation condition

## Required Output

### Valuation Snapshot

| field | requirement |
| --- | --- |
| `price_date` | 必填 |
| `current_valuation` | 当前估值锚，无法取得则写 `source_gap` |
| `historical_or_peer_range` | 至少一种对照 |
| `valuation_anchor_quality` | `high` / `medium` / `low` |
| `what_is_priced_in` | 价格隐含或市场正在定价的关键预期 |

### Scenario Table

| scenario | required fields |
| --- | --- |
| `bear` | 关键假设、估值锚、下行变量、证伪路径 |
| `base` | 关键假设、估值锚、预期收益驱动 |
| `bull` | 关键假设、估值锚、需要兑现的增量证据 |

### Revision Path

必须说明主要收益或风险来自哪里：

- `revenue_revision`
- `margin_revision`
- `cash_flow_revision`
- `multiple_rerating`
- `risk_premium_change`
- `positioning_unwind`
- `no_clear_revision_path`

## Quality Bar

- 不能只写“估值合理 / 估值偏贵”。
- 至少给出一组 base/bull/bear 数字或明确 `source_gap`。
- 如果 valuation anchor quality 是 `low`，核心结论不能依赖估值精度。
- 价格反应只能作为 `market_pricing`，不能替代基本面验证。
- 对高叙事股票，必须说明当前价格是否已经提前反映催化剂。

## Failure Modes

- 用目标价制造虚假精度。
- 只看相对 PE，不看增长、利润率、资本强度和现金流。
- 把优质公司自动等同于有吸引力股票。
- 没有说明下行场景和 risk premium。
- 忽略事件前市场已经 price in 的部分。
