# Mira Thesis System

`Thesis System` 是 Mira 的机构级研究协议层。它把一次性研究报告升级为可维护的 thesis object，并把研究流程固定为：

`source -> claim -> expectation -> thesis -> event delta -> decision log -> postmortem`

它不替代 `research-loop`、`monitoring-loop`、`earnings-report-analysis` 或 `evidence log`。它定义这些产物之间如何持续连接。

## Objectives

- 让每个 durable thesis 都能追溯到具体 claim 和来源。
- 明确市场预期、Mira 分歧、已 price-in 部分和下一验证点。
- 把财报、宏观、产品、监管、同业事件转成 `event-delta`，而不是只写事件摘要。
- 把研究判断记录成可复盘的 `decision-log`，但不输出投资建议或自动交易指令。
- 复盘判断质量，区分数据错误、推理错误、时间错误、市场定价错误和执行约束。

## First-Class Objects

### `thesis-ledger`

`thesis-ledger` 是一个研究对象的当前 thesis 账本。它回答：

- 当前 thesis 是什么。
- 哪些 claim 支撑它。
- 哪些输入只是 assumption、forecast、company_claim 或 sentiment。
- 哪些证据会证伪它。
- 当前状态是 `active`、`watch`、`upgrade_watch`、`downgrade_watch`、`stale` 还是 `retired`。

Required fields:

- `current_thesis`
- `supporting_claims`
- `key_assumptions`
- `variant_view`
- `disconfirming_evidence`
- `state`
- `stale_after`
- `must_refresh_if`

### `expectation-map`

`expectation-map` 把研究从“发生了什么”推进到“市场以为什么会发生”。它按变量记录：

- `consensus_proxy`
- `mira_view`
- `evidence_status`
- `price_in_status`
- `next_check`

共识代理可以来自 sell-side consensus、公司指引、价格反应、估值、期权定价、持仓拥挤度、媒体叙事或同业表现。若共识不可得，必须写 `source_gap`，不能虚构 consensus。

### `event-delta`

`event-delta` 用于事件前后比较：

- 事件前市场和 Mira 预期。
- 实际披露或实际发生的事实。
- 和预期的差异。
- 哪些变量可能触发 estimate revision、multiple rerating、risk premium change 或 positioning unwind。
- 价格反应质量是否与基本面 delta 匹配。
- 对 thesis 的影响方向和强度。

### `decision-log`

`decision-log` 记录研究动作，不是交易指令。允许的 `decision_type`：

- `watch`
- `upgrade_watch`
- `downgrade_watch`
- `add_to_research_queue`
- `reduce_research_priority`
- `hedge_context`
- `no_action`
- `retire_thesis`

如果接入 PMS 或组合系统，`decision-log` 只能作为研究输入，不能绕过用户或组合规则直接变成交易。

### `postmortem`

`postmortem` 复盘判断质量。核心错误类型：

- `data_error`
- `claim_weighting_error`
- `reasoning_error`
- `timing_error`
- `market_pricing_error`
- `execution_constraint`
- `not_an_error`

复盘必须写入 methodology 或 playbook 的候选更新，避免只做结果归因。

### `outcome-scorecard`

`outcome-scorecard` 用于校准 thesis 和 confidence。它回答：

- 原判断的 confidence 是否和后续结果匹配。
- 预期路径是否发生。
- 收益或风险是否来自 thesis 变量，而不是 unrelated beta。
- 错误来自数据、权重、推理、时间、市场定价还是执行约束。

### `actionability-bridge`

`actionability-bridge` 把 thesis 转成研究动作，不是交易指令。它必须包含：

- what is priced in
- base/bull/bear
- downside path
- invalidation conditions
- catalyst calendar
- qualitative position sizing implication

允许的研究动作包括 `watch_only`、`upgrade_watch`、`event_setup`、`post_event_follow_through`、`valuation_reset_watch`、`risk_reduction_context` 和 `no_action`。

## State Machine

Thesis state:

- `draft`: 首版研究中，证据链未完成。
- `active`: 有完整 evidence trail、刷新条件和主要反证路径。
- `watch`: 有方向性判断，但关键证据尚不足以升级。
- `upgrade_watch`: 新证据正在强化 thesis，但仍需后续验证。
- `downgrade_watch`: 新证据削弱 thesis，但尚未达到 retired。
- `stale`: 超过 `stale_after` 或关键来源过期。
- `retired`: 核心假设被证伪，或研究对象不再符合 Mira 覆盖范围。

Event impact:

- `+2`: 核心 thesis 被强验证。
- `+1`: 方向改善，但仍需后续确认。
- `0`: 与 thesis 一致，信息增量有限。
- `-1`: 出现可解释但需要跟踪的瑕疵。
- `-2`: 核心 thesis 被削弱或证伪。

## Data Flow

1. `research-loop` 产生 research package。
2. `write-thesis-ledger` 把稳定判断写入 `memory/research/<OBJECT>/thesis-ledger.md`。
3. `expectation-map` 记录关键变量的共识、Mira view 和下一验证点。
4. `event-delta-loop` 在事件前后更新 expectation 和 thesis impact。
5. `monitoring-loop` 只处理增量 claim，并决定是否进入 thesis state change。
6. `decision-log` 记录研究动作。
7. `postmortem` 在结果窗口结束后复盘，并把方法改进写入 `memory/methodologies/` 或 `memory/playbooks/`。

## Evidence Discipline

- `thesis-ledger` 中每个核心结论必须指向 case evidence log 或 explicit source note。
- `expectation-map` 中的共识代理不能由 Mira 凭空生成。
- `event-delta` 必须区分 `actual_disclosure`、`management_explanation`、`market_reaction` 和 `mira_interpretation`。
- `decision-log` 只能记录研究动作和风险语境，不写成投资建议。
- `postmortem` 不按结果好坏评价流程，必须区分当时可知信息和事后信息。
- `actionability-bridge` 不能绕过用户或组合规则变成交易指令。
- `outcome-scorecard` 必须记录原始 confidence，后续用于校准而不是事后改写原判断。

## Source Notes

- CFA Institute Standard V(C) 强调应保留支持投资沟通、建议或行动的研究记录。
- CFA Institute process attribution materials强调要把结果反馈到投资决策和组合构建流程，而不只看最终收益。
- Mauboussin/Rappaport 的 expectations investing 强调价格反映预期，研究应关注价格隐含预期和预期修正。
- Oakmark 的公开流程材料强调 thesis 简洁性、devil's advocate review 和 retrospective。
- Bridgewater 的公开材料强调把判断系统化、接受现实检验并持续改进决策过程。

## Refresh

- `stale_after`: 2026-08-29
- `must_refresh_if`: Mira 接入可运行 CLI/API、PMS 组合接口、期权/估值数据库，或发现更强的机构研究流程来源。
