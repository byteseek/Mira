# Methodology Card: Channel Check / Scuttlebutt

- status: trial
- role: overlay
- last_updated: 2026-04-22
- source_bucket: mixed (`institutional`, `practitioner`, `first_principles`)
- source_quality: medium-high
- credibility_score: medium-high
- credibility_basis: 输入变量清晰、逻辑链可拆、失效条件明确，但高成本且容易受 anecdote 和样本偏差污染
- search_coverage: medium
- search_gaps: 还没有系统覆盖中文 buy-side 圈层、失败案例集合和长期多年 follow-through 样本
- comparison_baseline: `supply-chain` overlay without explicit primary research workflow
- empirical_validation_mode: trial -> forward_watch + live case trial
- follow_through_plan: 用一个 `large-mega` 和一个 `micro-small` case 持续记录增量信息是否真的提升 thesis 质量

## Core Idea

`channel-check / scuttlebutt` 的核心不是“多打几个电话”，而是沿公司上下游、客户、渠道、竞品和行业参与者主动搜集非公司口径信息，再把这些碎片与公开披露和财务事实拼接，形成更接近真实经营状态的判断。

## Reverse-Engineered From

- Phil Fisher / scuttlebutt 一类 primary research 叙事
- buy-side / sell-side 的 channel check 写法
- 我们当前 `supply-chain` overlay 往前再推进一层时自然需要的验证动作

## Search Paths Used

- 方法名搜索
  `channel check`, `channel checks`, `scuttlebutt method`, `primary research investing`
- 功能描述搜索
  `how to verify demand without company guidance`, `how investors check channel inventory`
- 机构与合规搜索
  `mosaic theory`, `nonmaterial nonpublic information`, `analyst channel checks ethics`
- 实践派搜索
  scuttlebutt practitioner writeups, investing blogs, practical primary research guides
- 反面问题搜索
  anecdotes bias, confirmation bias in scuttlebutt, why channel checks fail

## Use When

- 公司的收入、订单、库存、渠道补库去库、客户采用率或产品竞争力很难只靠公开披露判断
- 需要验证管理层叙事是否与一线反馈一致
- 需要判断 moat、切换成本、客户粘性或竞品压力
- 需要在 `supply-chain` overlay 上再往前走一步，从“画链条”升级到“验证链条”
- 研究对象处于景气拐点、产品周期切换、渠道库存波动或客户集中度高的阶段

## Avoid When

- 票太小、流动性太差，且信息极度稀薄，容易把零碎 anecdote 误当结论
- 单次事件完全由监管批文、融资生死线或 binary outcome 决定，渠道反馈帮助有限
- 研究者无法区分 material nonpublic information 与合法 primary research
- 没有公开信息底座，只想靠访谈替代基本功

## Applies To

- `large-mega + supply-chain`
  用来验证终端需求、渠道库存、上游受益映射和产业链利润分配
- `mid-cap`
  用来验证叙事和业绩兑现是否真的在渠道和客户层面发生
- `micro-small`
  用来验证客户集中度、订单真实性、单一供应商约束和产品稀缺性是否成立

## Core Question

除了公司自己说的版本，渠道、客户、供应商、竞品和行业参与者看到的真实经营状态是什么？

## Required Inputs

- 公司公开披露、财报、10-K/10-Q、管理层表态
- 初步的供应链和同层级公司地图
- 需要验证的具体假设
  例如需求强弱、库存方向、订单质量、产品优势、切换成本、份额变化
- 访谈对象清单
  包括客户、供应商、分销商、前员工、行业顾问、竞品相关方
- 合规边界
  明确不得采集和使用 material nonpublic information

## Primary Signal

- 客户是否继续下单、缩单、延单或切换供应商
- 渠道库存是积压、正常还是正在补库
- 一线对产品竞争力、定价、交付、服务和切换成本的真实评价
- 供应商或分销商对订单节奏、产能约束和议价权的反馈
- 同层竞品是否验证或证伪公司叙事

## Why It Works

它有效的原因不是神秘，而是经营真实信号往往先出现在渠道和行业关系网里，再滞后反映到财报和公司口径里。  
我基于来源的综合判断是：

- `institutional`
  CFA 的 mosaic theory 明确认可把公开信息与非重大非公开信息拼成结论，也明确要求记录研究过程和保留证据链。
- `practitioner`
  实践派 scuttlebutt 更强调 primary research 带来的 conviction，以及用多视角访谈来对抗 echo chamber。
- `first_principles`
  如果公司价值最终取决于需求、供给、竞争和议价权，那么这些变量最直接的承载者本来就在客户、供应商、渠道和竞品那里。

## Failure Mode

- 最大风险是把 anecdote 当统计事实
- 第二个风险是只访谈支持自己假设的人，形成 confirmation bias
- 第三个风险是合规失守，碰到或误用 material nonpublic information
- 第四个风险是没有公开信息底座，导致“听故事代替研究”

## Evidence Cost

high

这个方法通常需要更高的时间成本、访谈成本和判断成本；对单只票来说，只有当预期差足够大或公开信息明显不够时才值得启用。

## Speed Vs Depth

偏 `depth`

它不适合作为全市场快速筛选主方法，更适合作为：

- 高价值候选标的的二次验证
- `supply-chain` overlay 的深挖层
- 对关键争议点做定性证伪

## Comparison To Existing Methods

相对当前 `supply-chain` overlay，这个方法的增量在于：

- `supply-chain` 更像结构映射，回答“链条长什么样”
- `channel-check / scuttlebutt` 更像 primary research workflow，回答“链条上真实发生了什么”

相对纯公开信息研究，它多带来：

- 一线经营温度
- 真实竞争反馈
- 对管理层口径的交叉验证

相对单纯技术面或事件面，它更能解释：

- 需求是否真的改善
- 份额变化是否为真
- moat 和 switching cost 是否真实存在

## Follow-Through Criteria

- 它是否稳定提供了超出公开披露的有效增量
- 它是否在后续季度或事件中被公开数据验证
- 它是否真实降低了 thesis 的误判率，而不是只是增加材料数量
- 它是否能在不同市值和不同产业链位置上保持方法一致性

## Trial Design

- case 1: `large-mega + supply-chain`
  以 AAPL 一类平台型大票为样板，验证终端需求、渠道库存和核心供应链受益映射是否能补强对产品周期的判断。
- case 2: `micro-small + supply-chain`
  选一个客户集中度高或单一产品驱动的小票，验证订单真实性、客户依赖度和供给约束。

预期增量：

- 减少“只看公司说法”的偏差
- 增强对需求、库存、客户粘性和竞品压力的判断
- 让 `supply-chain` overlay 从结构图升级成可证伪研究链

## Falsification Conditions

- 如果访谈获得的增量信息大多与公开信息重复，这个方法对该 case 的增量价值不足
- 如果不同访谈对象的反馈高度分裂，且无法与公开数据交叉验证，这个方法只能作为弱信号
- 如果启用后并不能提升 thesis 解释力或 refresh 质量，应降级回普通 `supply-chain` overlay

## Adoption Decision

当前判断：`trial`

原因：

- 它与 Mira 现有 `supply-chain` overlay 高度兼容
- 解释力强，但成本也高，不适合默认启用
- 在没有真实 case 验证前，不应直接进入 `adopted`

## Source Notes

- CFA Institute Standards of Practice Handbook on mosaic theory and use of public plus nonmaterial nonpublic information
- CFA Institute Enterprising Investor summary of Phil Fisher's scuttlebutt method
- Scuttlebutt Investor practical guide on combining anecdotal and empirical research and explicitly seeking disconfirming evidence
- Investopedia summaries on channel checks and mosaic theory for plain-language mechanics and legal boundary framing
