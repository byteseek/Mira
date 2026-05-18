# Thesis Horizon Routing

这个文档定义 `equity-research-core` 在选择主框架前，如何先判断研究结论的时间跨度。

目标不是把研究机械分成“短线”和“长线”，而是避免把单季财报、短期事件、长期产业趋势和长期公司质量混在同一个结论里。

## Core Rule

先判断 `thesis_horizon`，再判断 `pricing regime`。

`thesis_horizon` 回答的是：

- 这个研究结论想解释多长时间内的风险回报？
- 哪些证据在这个时间跨度内最有解释力？
- 哪些短期信号不能外推成长期 thesis？
- 哪些长期趋势又不能忽略短期现金流、指引和估值约束？

## Horizon Buckets

### `near_term_execution`

适用于 `1Q-2Q`。

核心问题：

- 本期财报、指引、订单、库存、价格、费用或现金流有没有改变短期预期？
- 市场短期在交易 beat / miss、guidance revision、催化剂兑现，还是风险暴露？

常见证据：

- 最新财报、新闻稿、监管文件、业绩会
- 指引、consensus、sell-side revision、价格反应
- 订单、backlog、库存、应收、现金流和同行同期财报

主要风险：

- 把单季经营波动误判为结构性变化
- 只看 headline beat / miss，不看指引质量和现金流

### `medium_term_revision`

适用于 `2Q-8Q` 或 `FY1/FY2`。

核心问题：

- 接下来几个季度的收入、利润率、现金流和估值锚是否需要上修或下修？
- 公司叙事、行业景气和盈利兑现是否同向？

常见证据：

- 多季度财务趋势
- FY1 / FY2 预期修正
- 产能、客户预算、订单持续性、价格和成本曲线
- 同行财报、供应链信号、行业景气指标

主要风险：

- 只用长期故事掩盖近期盈利修正恶化
- 把一次性补库存、提前拉货或成本红利外推为多季度趋势

### `long_term_thesis`

适用于 `>1 year`，通常是 `3-5 year` 现金流、竞争位置或产业趋势判断。

核心问题：

- 公司是否站在正确的产业趋势、利润池迁移、技术路径或竞争格局里？
- 长期现金流曲线、资本回报、护城河或估值范式是否可能改变？

常见证据：

- 产业链位置、利润池、技术路线、客户切换成本和竞争壁垒
- 多年资本开支、研发、产能、监管和商业模式变化
- 大客户、供应商、竞品和行业数据的交叉验证

主要风险：

- 用长期叙事忽略短期资产负债表、现金流和估值约束
- 用一份好财报直接证明长期 thesis

### `regime_transition`

适用于短期证据可能正在改变长期 thesis 的场景。

核心问题：

- 最新财报、事件或行业信号是否只是短期扰动，还是正在改变长期变量？
- 这次变化影响的是收入时点、盈利周期，还是长期利润池和竞争格局？

常见证据：

- 财报和业绩会中新增的长期变量
- 同行同步变化或背离
- 供应链、客户预算、资本开支、监管、技术路线和价格机制变化

主要风险：

- 把长期 thesis 的初始拐点当成普通季度噪音
- 把普通季度修复包装成长周期重估

## Decision Order

按以下顺序判断：

1. 用户问题的真实时间边界是什么。
2. 当前最关键证据来自最新财报、多个季度趋势，还是产业/竞争结构。
3. 结论是否依赖未来 `1Q-2Q`、`FY1/FY2`，还是 `3-5 year` 变量。
4. 短期证据是否足以改变长期 thesis。
5. 如果短期和长期信号冲突，哪一个更应该控制结论强度。

## Practical Routing Rules

满足以下情形时，优先路由到 `near_term_execution`：

- 用户问的是“这次财报怎么看”“短期趋势有没有变”“指引是否可信”
- 关键证据是最新财报、指引、market reaction 或短期催化剂
- 结论的有效期主要到下一份财报或下一次关键披露

满足以下情形时，优先路由到 `medium_term_revision`：

- 用户关心的是未来几个季度的收入、利润率、EPS、FCF 或估值锚
- 关键问题是 FY1 / FY2 预期是否需要 revision
- 公司叙事需要和多个季度业绩兑现相互验证

满足以下情形时，优先路由到 `long_term_thesis`：

- 用户问的是“长期值不值得押注”“这个板块趋势是不是成立”
- 关键证据来自产业趋势、竞争格局、利润池、技术路线或资本周期
- 单季财报只能作为验证点，不能单独决定结论

满足以下情形时，标记为 `regime_transition`：

- 最新财报、订单、资本开支、监管或技术事件可能改变长期利润池
- 同行和产业链同步出现与原 thesis 不一致的新信号
- 市场正在从短期 beat / miss 切换到长期曲线重估

## Earnings-To-Thesis Bridge

财报分析默认服务于 `near_term_execution` 和 `medium_term_revision`。

只有当财报证据同时满足以下条件时，才允许上升到 `long_term_thesis`：

- 变化触及长期驱动变量，而不只是季度时点
- 管理层解释有财务、订单、客户、产能、现金流或同行证据支撑
- 至少一个外部证据链支持这不是公司单方面叙事
- 已写出为什么这次变化不是 one-off
- 已写出后续哪些披露会证伪长期外推

如果不满足这些条件，财报结论只能写成短中期 `thesis impact`，不能直接升级为长期结论。

## Output Requirements

在 `investment memo` 和 `case notes` 中都要留下：

- `thesis_horizon`
- `horizon_bucket`
- `horizon_basis`
- `horizon_mismatch_risk`

如果涉及财报，还要写：

- `earnings_to_thesis_bridge`
- `what_can_be_extrapolated`
- `what_cannot_be_extrapolated`

`horizon_mismatch_risk` 用于回答：

如果时间跨度选错，最可能导致哪类误判。

## Refresh Conditions

不同 horizon 的默认刷新条件不同：

- `near_term_execution`: 下一份财报、指引更新、重大催化剂或价格显著反应后刷新
- `medium_term_revision`: FY1 / FY2 consensus、同行财报、订单/库存/价格趋势变化后刷新
- `long_term_thesis`: 产业路线、竞争格局、资本开支、监管、大客户预算或利润池假设变化后刷新
- `regime_transition`: 每次新披露都要判断它是在确认长期拐点，还是回落为短期噪音
