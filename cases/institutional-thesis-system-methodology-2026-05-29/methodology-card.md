# Methodology Card: Institutional Thesis System

- status: trial
- role: protocol-layer
- last_updated: 2026-05-29
- source_bucket: mixed (`institutional`, `practitioner`, `first_principles`, `derived_internal`)
- source_quality: medium-high
- credibility_score: medium-high
- credibility_basis: 方法与机构研究记录、预期差、事件复盘和流程归因高度一致；当前缺口是尚未经过多个 live case 的自动化校验
- search_coverage: medium
- search_gaps: 还缺更多 buy-side 内部 thesis ledger 样例、组合经理实际 decision journal 样例、以及跨资产事件复盘流程
- comparison_baseline: report-centric Mira research package
- empirical_validation_mode: trial -> live event trial + postmortem review
- follow_through_plan: 用 AAPL、CRWV、WOLF 完成首轮文档验收；下一步用于一个真实新财报事件

## Core Idea

机构级研究系统不应只生成报告，而应维护可更新、可证伪、可复盘的 thesis object。每个 thesis 都需要连接来源、claim、预期、事件变化、研究动作和复盘。

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
- 财报、宏观、监管、产品、同业事件需要和 prior expectation 比较。
- 需要复盘过去判断，而不是只解释结果。

## Avoid When

- 只是一次很轻的事实查询。
- 研究对象没有可维护的 thesis 或刷新条件。
- 来源不足以区分事实、预测、市场定价和 Mira 推断。

## Applies To

- 单票首次覆盖后的持续跟踪。
- 财报和 investor day。
- 高叙事小盘股的证据降权。
- 大票的预期差和估值隐含预期分析。
- 未来 PMS/portfolio context 接入前的研究动作记录。

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
- 变量是否已经被市场预期或价格反映。
- 新 claim 的证据强度是否足以改变 thesis state。
- 事件后是否有可跟踪的 revision path。

## Why It Works

这个方法把 Mira 已有的 source policy、claim taxonomy、framework routing 和 memory 连接成闭环。它避免把一次性报告误当成可持续研究，也避免在事件后只做新闻摘要。

公开来源支持三条原则：

- 研究记录需要可追溯，支持后续沟通和动作。
- 预期和预期修正是股票价格变化的重要机制。
- 投资团队需要复盘原始 thesis、挑战假设并把反馈写回流程。

## Failure Mode

- 把 thesis ledger 写成另一篇长 memo。
- 没有真实 consensus proxy，却虚构“市场预期”。
- 因为价格上涨就倒推 thesis 被验证。
- postmortem 只看结果，不区分当时可知信息和事后信息。
- decision-log 被误用成交易指令。

## Evidence Cost

medium-high

它要求比普通 memo 多维护 expectation、事件 delta 和状态变更，但不要求一开始接数据库。

## Speed Vs Depth

medium

适合作为正式研究后的持续系统层，不适合作为所有轻量问答的默认流程。

## Comparison To Existing Methods

相对 `variant-perception`，它更宽：variant perception 是 expectation lens，Thesis System 是持久对象和状态机。

相对 `research-loop`，它更持续：research-loop 建立首版认知，Thesis System 管理后续变化。

相对 `monitoring-loop`，它更结构化：monitoring-loop 扫描增量，Thesis System 决定 state change 和复盘。

## Follow-Through Criteria

- 是否能让每个 thesis 有明确 state、刷新条件和证伪条件。
- 是否能让事件后分析写出 delta，而不是总结。
- 是否能防止 sentiment、rumor_signal 和 market_pricing 直接升级 thesis。
- 是否能把错误判断转成 methodology 或 playbook 更新。

## Trial Design

- AAPL: 把现有 memory thesis 升级成 `thesis-ledger`。
- CRWV: 从 earnings package 生成 `event-delta`。
- WOLF: 用 expectation map 测试高叙事弱证据降权。

## Falsification Conditions

- 连续三个 live case 后，thesis state change 仍无法比普通 memo 更清楚。
- expectation map 经常无法找到真实共识代理。
- 维护成本高到阻碍研究更新。
- decision-log 无法和投资建议边界分开。

## Adoption Decision

当前判断：`trial`

理由：现有仓库已具备 claim taxonomy、evidence log、monitoring loop 和 memory，但 thesis object 仍不完整。先以文档协议落地，等 live case 验证后再考虑代码校验器。

## Source Notes

- CFA Institute Standard V(C) Record Retention: https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-c
- CFA Institute process attribution digest: https://rpc.cfainstitute.org/research/cfa-digest/2016/09/process-attribution-revisiting-equity-attribution-and-decision-making-digest-summary
- Mauboussin/Rappaport expectations investing interview: https://www.fool.com/investing/2022/01/19/expectations-investing-qanda-mauboussin-rappaport/
- NBER earnings expectations paper: https://www.nber.org/papers/w27160
- Maryland Smith forecast revision summary: https://www.rhsmith.umd.edu/research/slow-motion-earnings-revisions-wall-street
- Oakmark decision process article: https://oakmark.com/news-insights/decide-like-an-athlete/
- Bridgewater process overview: https://www.bridgewater.com/
