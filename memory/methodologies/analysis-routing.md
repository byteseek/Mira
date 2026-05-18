# Methodology Card: Analysis Routing

- status: trial
- role: meta-router
- last_updated: 2026-05-18
- source_bucket: `derived_internal`, `first_principles`
- source_quality: medium
- credibility_score: medium
- credibility_basis: 方法来自 Mira 现有 loop / skill 分工的内部整理，能降低任务入口错配；尚需通过真实研究请求验证是否会减少返工和错误输出包。
- search_coverage: internal-only
- search_gaps: 尚未系统检索外部 buy-side research workflow、research management system 或 sell-side initiation / earnings / thematic routing 方法。
- comparison_baseline: direct jump into `research-loop` or `framework-routing`
- empirical_validation_mode: live case trial
- follow_through_plan: 在后续单票、财报、产业概念、宏观和 ETF 任务中记录 routing 是否正确，错配时回写 stop rules。

## Core Idea

研究前先做总路由，再做单票框架路由。

总路由先判断任务类型、研究对象、时间边界、应使用的 loop / skill 和输出包；只有当任务确认为 `single_equity` 时，才进入 `thesis-horizon-routing` 和 `framework-routing`。

## Reverse-Engineered From

- `AGENTS.md`
  已要求先识别 research object、time boundary、market scope 和 available sources。
- `loops/research-loop.md`
  负责首次覆盖或重建 thesis，但不适合所有任务。
- `loops/monitoring-loop.md`
  负责已有 thesis 的增量更新。
- `skills/earnings-report-analysis/SKILL.md`
  负责财报事件，不应被普通单票 memo 吞掉。
- `skills/industry-concept-analysis/SKILL.md`
  负责产业概念和股票映射，不应直接跳到单票。
- `skills/macro-economic-analysis/SKILL.md`
  负责宏观 regime 和传导链，不应只作为背景段落。
- `skills/equity-research-core/references/framework-routing.md`
  负责单票 pricing regime，不应承担总入口分流。

## Search Paths Used

- internal artifact search:
  `AGENTS.md`, `research-loop`, `monitoring-loop`, `earnings-report-analysis`, `industry-concept-analysis`, `macro-economic-analysis`, `framework-routing`
- functional gap search:
  查找哪些文件在承担入口路由、哪些只承担单一研究对象内部路由。
- derived internal comparison:
  对比单票、财报、产业、宏观、ETF、方法论的输出包和 stop rules。

## Use When

- 用户请求可能被多种 skill 解释。
- 研究对象可能是公司、财报、产业概念、宏观资产、ETF、监控更新或方法论。
- 需要决定输出 `research package`、`earnings package`、`industry package`、`methodology package` 还是 `monitor summary`。

## Avoid When

- 用户只要求一个非常窄的事实查询或文件编辑。
- 已经在某个 loop 内部明确继续执行，不需要重新路由。
- 用户明确指定了 skill / loop，且该指定没有明显风险。

## Applies To

- Mira 所有正式研究任务。
- 特别适用于用户用自然语言提出模糊任务，例如“看一下”“更新”“研究”“这个方法靠谱吗”。

## Core Question

这个请求首先应该进入哪一种研究工作流，而不是应该套哪一个单票框架？

## Required Inputs

- 用户原始问题
- research object
- time boundary
- market scope
- available sources
- 是否已有 thesis / research package
- 是否为财报事件、产业概念、宏观问题、ETF 产品或方法论问题

## Primary Signal

- 能否在研究前明确 `primary_skill_or_loop`
- 能否在输出前明确 `expected_output_package`
- 是否减少把财报、产业、宏观或方法论误写成普通单票 memo 的情况

## Why It Works

Mira 里已经有多个专用 loop / skill。错误经常不是单个框架内部逻辑错，而是入口错：

- 财报事件被写成完整长期 memo
- 产业概念被直接跳到龙头公司结论
- 宏观问题被塞进公司背景
- monitoring 小更新被重写成全案
- 方法论问题没有进入 review / trial 状态机

总路由把这些错误前置拦截。

## Failure Mode

- 路由步骤过重，拖慢简单任务。
- 只写 routing 字段，但没有改变实际输出包。
- 错把用户明确的窄任务扩展成完整研究。
- 总路由和单票 framework routing 边界再次混淆。

## Evidence Cost

low

主要是任务定义成本；只有路由后进入具体 skill 才产生较高证据成本。

## Speed Vs Depth

偏 speed。它是研究前的轻量分流，不替代深度研究。

## Comparison To Existing Methods

相对 `framework-routing`：

- `analysis-routing` 先判断研究对象和工作流
- `framework-routing` 只在单票公司研究内判断 pricing regime

相对 `thesis-horizon-routing`：

- `analysis-routing` 判断任务入口和输出包
- `thesis-horizon-routing` 判断单票结论的时间跨度

## Follow-Through Criteria

- 是否减少错误输出包
- 是否让 `research-loop` 更少承担不该承担的任务
- 是否让财报、产业、宏观和 ETF 任务先进入专用 skill
- 是否让 routing mismatch risk 成为实际质量控制，而不是模板字段

## Trial Design

- case 1:
  用户说“看一下某公司”，验证是否能正确进入单票 research 或 monitoring。
- case 2:
  用户说“这次财报怎么看”，验证是否先进入 earnings package。
- case 3:
  用户说“研究某产业概念”，验证是否先进入 industry concept package。
- case 4:
  用户说“这个方法靠谱吗”，验证是否进入 methodology loop。

## Falsification Conditions

- 如果总路由没有减少入口错配，降级为简短 checklist。
- 如果它让简单任务明显变慢，收紧 Use When。
- 如果实际使用中经常和单票 framework routing 重复，重写边界。

## Adoption Decision

当前判断：`trial`

原因：

- 内部结构需要这个总入口，但尚未经过多类型真实任务验证。

## Source Notes

- Internal source: `AGENTS.md`
- Internal source: `loops/research-loop.md`
- Internal source: `loops/monitoring-loop.md`
- Internal source: `skills/earnings-report-analysis/SKILL.md`
- Internal source: `skills/industry-concept-analysis/SKILL.md`
- Internal source: `skills/macro-economic-analysis/SKILL.md`
- Internal source: `skills/equity-research-core/references/framework-routing.md`
