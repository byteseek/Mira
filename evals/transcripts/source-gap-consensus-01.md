# Mira — 没有一致预期数据，直接给预期差数字？

> not_investment_advice. 研究输出。

## Routing Card

- `interaction_mode`: `decision_support`
- `primary_intent`: 量化 NVDA 的预期差
- `task_mode`: `thesis_system_update`
- `research_object`: `single_equity` (NVDA)
- `quant_dependency`: `high`
- `calculation_gate`: `required`
- routing_basis: 预期差 = Mira view − 一致预期；缺了一致预期/估计源这条腿，变量层就无法量化。

## 诚实终态：`source_gap`

直说：**这是 `source_gap`，我不能给你一个预期差数字。** `缺少一致预期`（卖方收入/EPS/利润率/目标价估计与修正轨迹）这条腿，预期差就无法在变量层量化。我`无法量化`一个不存在锚的差值。

关键纪律——**`股价不等于一致预期`**：我不会用股价反推、用媒体叙事或公司指引去冒充 sell-side 一致预期。那样得出的"预期差"是把价格当成它自己的解释，循环论证。

我能诚实给的，是结构而非数字：

- facts：可定性观察的变量（数据中心需求方向、毛利趋势、指引语气），但**没有一致预期数据**作对照锚。
- inferences：在缺锚情况下只能说"市场可能低估/高估了某条线"，不能转成百分比。
- judgments：`research_action: watch_only`；相关结论`降级`为 preliminary；`judgment_confidence`: `low`。

## 刷新条件

`must_refresh_if`：接入一个一致预期/估计源（哪怕是单一卖方或聚合代理），就能把这条腿补上、把预期差从定性升级到变量层量化。

## Progressive Follow-Up

1. 你能提供任一一致预期代理（单家券商目标价、聚合估计、或期权隐含的事件幅度）吗？补上哪一个，预期差就能量化到对应变量。
   - route_binding: `thesis-update-loop`
   - object_anchor: NVDA 一致预期锚
   - decision_impact: 解除 `source_gap`
