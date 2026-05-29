# Methodology Card: Institutional Thesis System

- status: trial
- role: protocol-layer
- last_updated: 2026-05-29
- source_bucket: mixed (`institutional`, `practitioner`, `first_principles`, `derived_internal`)
- source_quality: medium-high
- credibility_score: medium-high
- credibility_basis: 公开机构流程、预期差研究、事件复盘和 Mira 现有 evidence discipline 都支持该方向；仍需 live case 验证维护成本和状态变更质量
- search_coverage: medium
- search_gaps: 缺少更多 buy-side 内部 thesis ledger 样例、组合经理 decision journal 样例和跨资产复盘材料
- comparison_baseline: report-centric Mira research package
- empirical_validation_mode: trial -> live event trial + postmortem review
- follow_through_plan: 下一步在真实新财报事件中同时生成 pre-event setup、event-delta 和 thesis state decision

## Core Idea

把 Mira 从报告生成协议升级为可维护的 thesis system。每个 durable thesis 都必须连接 source、claim、expectation、event delta、decision log 和 postmortem。

## Reverse-Engineered From

- CFA Institute 对研究记录留存和决策流程反馈的公开材料
- Mauboussin/Rappaport expectations investing 的价格隐含预期和预期修正框架
- Oakmark 对 devil's advocate review 和 retrospective 的公开流程描述
- Bridgewater 对系统化投资判断和现实检验的公开表述
- Mira 当前 AAPL、CRWV、WOLF 案例中的 thesis impact、evidence log 和弱证据降权实践

## Search Paths Used

- `CFA record retention investment research notes`
- `process attribution investment decision making`
- `expectations investing price implied expectations`
- `earnings forecast revisions consensus estimates`
- `investment team retrospective devil advocate`
- `investment memo professional process improve`

## Use When

- 已有 research package 需要进入长期跟踪。
- 用户问“是否改变 thesis”“预期差在哪里”“这次事件有没有增量”。
- 财报、宏观、监管、产品或同业事件需要和 prior expectation 比较。
- 需要复盘过去判断，而不是只解释结果。

## Avoid When

- 只是一次轻量事实查询。
- 研究对象没有可维护 thesis。
- 来源不足以区分事实、预测、市场定价和 Mira 推断。

## Applies To

- 单票 research package 后的持续跟踪。
- 财报、investor day、宏观和监管事件。
- 高叙事小盘股的证据降权。
- 大票的预期差和估值隐含预期分析。

## Core Question

新增信息改变了哪条预期、哪条假设或哪条 supporting claim，是否足以改变 thesis state？

## Required Inputs

- evidence log
- current thesis or prior research package
- expectation proxy
- event or monitoring trigger
- refresh condition
- disconfirming evidence path

## Primary Signal

- 新信息能否定位到具体变量。
- 变量是否已被市场预期或价格反映。
- 新 claim 的证据强度是否足以改变 thesis state。
- 事件后是否有可跟踪的 revision path。

## Why It Works

Mira 已经有 source policy、claim taxonomy、framework routing、monitoring loop 和 memory，但这些对象尚未被组织成同一个状态机。Thesis System 把这些现有能力连接起来，让研究从“写一份结论”升级为“维护一个可证伪判断”。

## Failure Mode

- 把 thesis ledger 写成另一篇长 memo。
- 没有真实 consensus proxy，却虚构市场预期。
- 因为价格上涨就倒推 thesis 被验证。
- postmortem 只看结果，不区分当时可知信息和事后信息。
- decision-log 被误用成交易指令。

## Evidence Cost

medium-high

需要维护 expectation、事件 delta 和状态变更，但 V1 不需要数据库或 UI。

## Speed Vs Depth

medium

适合作为正式研究后的持续系统层，不适合作为所有轻量问答默认流程。

## Comparison To Existing Methods

相对 `variant-perception`，它更宽：variant perception 是 expectation lens，Thesis System 是持久对象和状态机。

相对 `research-loop`，它更持续：research-loop 建立首版认知，Thesis System 管理后续变化。

相对 `monitoring-loop`，它更结构化：monitoring-loop 扫描增量，Thesis System 决定 state change 和复盘。

## Follow-Through Criteria

- 每个 thesis 是否有 state、刷新条件和证伪条件。
- 每个事件是否能写出 delta，而不是摘要。
- sentiment、rumor_signal 和 market_pricing 是否被正确降权。
- 错误判断是否能转成 methodology 或 playbook 更新。

## Trial Design

- AAPL: 把现有 memory thesis 升级成 `thesis-ledger`。
- CRWV: 从 earnings package 生成 `event-delta`。
- WOLF: 用 expectation map 测试高叙事弱证据降权。

## Falsification Conditions

- 连续三个 live case 后，thesis state change 仍无法比普通 memo 更清楚。
- expectation map 经常找不到真实共识代理。
- 维护成本高到阻碍研究更新。
- decision-log 无法和投资建议边界分开。

## Adoption Decision

当前判断：`trial`

## Source Notes

- CFA Institute Standard V(C) Record Retention: https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-c
- CFA Institute process attribution digest: https://rpc.cfainstitute.org/research/cfa-digest/2016/09/process-attribution-revisiting-equity-attribution-and-decision-making-digest-summary
- Mauboussin/Rappaport expectations investing interview: https://www.fool.com/investing/2022/01/19/expectations-investing-qanda-mauboussin-rappaport/
- NBER earnings expectations paper: https://www.nber.org/papers/w27160
- Maryland Smith forecast revision summary: https://www.rhsmith.umd.edu/research/slow-motion-earnings-revisions-wall-street
- Oakmark decision process article: https://oakmark.com/news-insights/decide-like-an-athlete/
- Bridgewater process overview: https://www.bridgewater.com/
