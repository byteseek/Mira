# Methodology Card: Variant Perception

- status: trial
- role: framework-lens
- last_updated: 2026-04-22
- source_bucket: mixed (`institutional`, `practitioner`, `first_principles`, `reverse_engineered`)
- source_quality: medium-high
- credibility_score: medium
- credibility_basis: 核心直觉强、来源广、和投资实践高度一致，但方法边界容易过宽，若没有“如何测 consensus”与“如何验证差异”就会退化成空泛的“我要和市场不一样”
- search_coverage: medium-high
- search_gaps: 还缺更系统的失败案例集合、中文 buy-side 实操写法，以及把概念落成单票 checklist 的材料
- comparison_baseline: `manual expectation mismatch thinking`
- empirical_validation_mode: trial -> live case trial + forward watch
- follow_through_plan: 已完成一轮 `AAPL` 与 `HIMS` 简化试跑；下一步是把 consensus proxy checklist 固化后继续跟踪后续财报和价格反应

## Core Idea

`variant perception` 的核心不是单纯“唱反调”，而是先判断市场共识到底预期了什么，再提出一个有根据、可验证、且与共识存在有效偏差的判断。

## Reverse-Engineered From

- Michael Steinhardt 对 `variant perception` 的经典定义
- Howard Marks 关于 second-level thinking、共识与定价的思路
- Variant Perception 研究机构把 macro、fundamental 和 behavioral 结合成“可重复的差异化判断”框架
- Morgan Stanley Counterpoint 对 popular delusions / myth busting 的写法

## Search Paths Used

- 方法名搜索
  `variant perception`, `variant view`, `variant perception investing`
- 功能描述搜索
  `how to know market expectations`, `consensus expectations investing`, `how differentiated view creates alpha`
- 人物与机构搜索
  `Michael Steinhardt`, `Howard Marks`, `Variant Perception`, `Morgan Stanley Counterpoint`
- 反面问题搜索
  `being contrarian is not enough`, `variant perception criticism`, `consensus already priced in`
- 输出形态搜索
  机构文章、投资评论、历史访谈、方法论营销页和观点文章

## Core Idea

真正的机会不在“我觉得会涨跌”，而在三件事的交集：

- 市场共识预期是什么
- 我不同意的地方是什么
- 如果我对，为什么价格还没有充分反映

## Use When

- 研究对象的核心问题本质上是“市场预期 vs 现实结果”的错配
- 需要判断一个事件、财报、产品周期或行业拐点到底有没有被 price in
- 需要明确 thesis 不是“公司很好”，而是“市场对它哪里看错了”
- 想把宏观、基本面、行为和定价联系起来

## Avoid When

- 没法描述当前共识，只能描述自己的观点
- 没法说明分歧会通过什么机制体现在价格上
- 票太小且共识几乎不存在，这时谈“variant”容易失焦
- 研究者只是为了显得聪明而追求差异化

## Applies To

- `large-mega`
  特别适合判断宏观、盈利预期和配置共识是否过度一致
- `mid-cap`
  适合判断叙事强化和盈利修正是否已被市场提前押注
- `thematic / macro`
  适合把热门主题拆成“大家以为什么会发生”与“真正可能发生什么”

## Core Question

市场已经预期了什么，而我的不同判断为什么更可能接近现实？

## Application Chain

不是描述方法，而是按顺序执行的推理链。每一步要么产出 evidence-log 的具体行，要么触发降级。

1. `consensus-triangulate` 共识三角测量
   - 列出 3 个共识代理：sell-side 一致预期 / 持仓拥挤度 / 价格隐含预期。
   - 每个都必须落到一个**具体数字或事件**——“市场在 FY1 收入上隐含 +X%”、“价格隐含 Y 的毛利持续”。
   - 写不出数字 = 你没测到共识，只测到情绪。停在 `source_gap`，不要继续。
   - 产出 evidence-log：每个 proxy 一行（`claim_type=consensus_proxy`）。

2. `disagreement-to-variable` 分歧定到变量
   - 说出你和**哪一个**具体数字 / 机制不同（收入斜率？毛利？某客户？某产品周期？库存？），以及你的数字是多少、差多少。
   - 只能说“我更谨慎 / 更乐观”却点不到变量 = 还没有 variant，回到第 1 步。

3. `mechanism-chain` 机制链
   - 给出 2-3 步因果链解释为什么你的数字更可能对，**每步挂一个 evidence / calc ref**。
   - 不能是“我觉得”——每一步要能指向具体事实或可复算计算。

4. `why-not-priced` 为什么还没 price in
   - 在三类里**指认至少一个**原因：信息（没人看 / 看不到）｜行为（叙事惯性、锚定、近期偏差）｜结构（指数、流动性、强制买卖）。
   - 指认不出 = “差异存在但不构成 edge”，actionability 降级为 `watch_only`，不要伪装成机会。

5. `repricing-and-falsifier` 重定价路径 + 单一证伪点
   - 如果你对，价格通过**什么事件 / 时间窗**重定价。
   - 哪**一个**观察一旦出现就证明你错——直接写进 `must_refresh_if` / `kill_criteria` / `reversal_condition`。
   - 产出 evidence-log：falsification 行 + refresh 条件。

链条出口：5 步都过 → variant 成立，可进 actionability / thesis；任一步卡住 → 停在该步对应的降级态（`source_gap` / `watch_only` / “无 edge”），不要硬凑结论。

## Why It Works

我基于本轮搜索的综合判断是，这个方法之所以长期有吸引力，是因为投资回报本来就是“现实 - 预期”的函数，而不是“质量 - 口号”的函数。  
来源支持大致分三类：

- `institutional`
  多家机构都把“识别 market consensus 并找到被低估的分歧”作为差异化判断核心。
- `practitioner`
  Steinhardt、Howard Marks 一类实践者都把“和共识不同且最终正确”视为 alpha 来源。
- `first_principles`
  如果价格是市场对未来现金流和风险的折现，那么真正有价值的研究天然要处理预期错配，而不是只描述事实本身。

## Failure Mode

- 最常见失败是把“不同”误当成“有 edge”
- 第二个失败是根本没有测到共识，只是虚构一个 strawman consensus
- 第三个失败是分歧虽然存在，但不足以带来价格重估
- 第四个失败是方法太宽泛，最后只能在事后解释一切

## Evidence Cost

medium

它不像 channel check 那样高度依赖一线访谈，但需要更强的 expectation mapping 能力，尤其要能找到共识代理和分歧证据。

## Speed Vs Depth

介于 `medium` 和 `depth`

它不是单独的发现引擎，更像一个 thesis sharpening layer，用来把研究从“公司分析”推进到“预期差分析”。

## Comparison To Existing Methods

相对当前 Mira 里的 framework 和 overlay：

- 它不是替代 `micro-small / mid-cap / large-mega`
- 它更像横跨所有框架的一层 `expectation lens`
- 它也不是 `supply-chain` 那样的具体 overlay，因为它不告诉你去看哪条链，而是告诉你“要先定义市场已经看了什么”

增量在于：

- 强制研究者写出 `consensus`
- 强制区分“公司真的好”与“市场有没有低估它”
- 更容易把 thesis 写成可交易、可证伪的结构

## Follow-Through Criteria

- 它是否能稳定逼迫研究写出清晰的 consensus proxy
- 它是否提升了 memo 中 `key debate` 和 `must refresh if` 的质量
- 它是否能在不同风格股票上保持解释力
- 它是否只是事后复盘工具，而不是事前判断工具

## Trial Design

- case 1: `large-mega`
  选一只 consensus 很强的大票，要求显式写出 sell-side / buy-side / price action 三种 consensus proxy，再判断真正的分歧点。
- case 2: `mid-cap`
  选一只叙事和业绩同时变化的中盘股，验证 variant perception 是否能提前识别“叙事已 price in 还是仍有预期差”。

预期增量：

- 让研究从“质量判断”升级到“预期错配判断”
- 改善 thesis 的可交易性和可证伪性
- 避免把漂亮公司分析误当成投资机会分析

## Falsification Conditions

- 如果实际使用时研究者始终无法稳定刻画 consensus，这个方法只能停留在概念层
- 如果它不能带来比普通 thesis 更清晰的催化剂和失效条件，就不算有效落地
- 如果事后几乎任何结果都能被解释成“variant”，说明方法过宽，应降级

## Adoption Decision

当前判断：`trial`

原因：

- 它已经通过两只风格不同股票完成首轮 live trial，证明方法有实际约束力
- 但当前仍依赖研究者手工刻画 consensus proxy，尚未形成稳定 checklist
- 在没有更多跨 case follow-through 前，不适合直接进入 `adopted`

## Source Notes

- Variant Perception official explanation and philosophy pages
- Variant Perception article "Finding Your Variant Perception: Why Being Different Isn't Enough" published on January 16, 2026
- Michael Steinhardt interview summary in The Washington Post archive
- Morgan Stanley Counterpoint Global article on myth busting and variant perception
- Howard Marks discussion of consensus / first-level vs second-level thinking as surfaced by secondary summaries
