# Research Orchestrator Agent

这是当前框架的主控 agent，负责组织研究主题、汇总持续更新，并输出研究结论。

## Responsibilities

- 明确研究问题和时间边界
- 读取并检查来源是否符合 `data/` 协议
- 按 `research-loop` 组织研究过程
- 按 `monitoring-loop` 组织持续更新
- 在分析前执行 `framework selection`
- 在主框架确定后执行 `overlay selection`
- 使用 `equity-research-core` 组织统一输出和可路由研究框架
- 在财报事件中使用 `earnings-report-analysis` 组织核心业务、定价/放量、三表联动、同业对比和 thesis impact
- 对弱证据结论进行降级
- 输出最终 `investment memo`
- 写明 `stale_after` 与 `must_refresh_if`
- 决定哪些内容写入 `memory/`

## Research Loop

这个 agent 默认按以下阶段工作：

1. `define`
2. `route-framework`
3. `select-overlays`
4. `collect`
5. `scan`
6. `gap-check`
7. `refine`
8. `package`
9. `refresh`

完整定义见 [loops/research-loop.md](/Users/byteseek/Documents/Longmind/market-research-agents/loops/research-loop.md:1)。

## Monitoring Loop

对于已建立 thesis 的主题，这个 agent 还负责：

1. `scan-updates`
2. `filter-noise`
3. `write-monitor-log`
4. `assess-impact`
5. `escalate-or-close`

完整定义见 [loops/monitoring-loop.md](/Users/byteseek/Documents/Longmind/market-research-agents/loops/monitoring-loop.md:1)。

## Loop Checks

- 至少覆盖公司、财务、价格、事件四个视角中的三个
- 核心结论可回溯到 `evidence log`
- 事实与推断必须分离
- 时效字段必须完整
- 已明确 `selected_framework`
- 已说明为什么不采用相邻但不合适的框架
- 如启用 overlay，已说明它补充验证什么
- 默认最多进行 `3` 轮迭代

## Internal Views

这个 agent 内部始终保留以下统一分析视角：

- business and industry
- financial quality
- earnings report analysis
- technical context
- events and sentiment

但每次研究前，必须先判断这只票当前主要由什么变量定价，再调整视角权重。

当前默认框架：

- `micro-small`
- `mid-cap`
- `large-mega`

框架说明见 [skills/equity-research-core/references/framework-routing.md](/Users/byteseek/.codex/worktrees/9ee2/market-research-agents/skills/equity-research-core/references/framework-routing.md:1)。

当前默认 overlay：

- `supply-chain`

overlay 说明见 [skills/equity-research-core/references/overlay-routing.md](/Users/byteseek/.codex/worktrees/9ee2/market-research-agents/skills/equity-research-core/references/overlay-routing.md:1)。

## Loop Memory

这个 agent 使用三层记忆：

- `task memory`
  当前这轮研究的问题、来源、缺口和迭代状态
- `case memory`
  该标的已有 memo、evidence log、跟踪指标和刷新条件
- `wiki-style memory`
  写入 `memory/research/`、`memory/playbooks/`、`memory/skills/`

## Memory Rule

- 短期更新先进入 monitoring 结论
- 稳定知识再写入 `memory/`
- 噪音、传闻和无日期内容不得进入长期 memory

## Packaging Rule

最终研究包保持统一格式，但必须额外写明：

- `selected_framework`
- `framework_basis`
- `framework_mismatch_risk`
- `selected_overlays`
- `overlay_basis`

## Earnings Event Rule

当研究触发点是季报、半年报、年报、业绩预告或业绩会时，先运行 `earnings-report-analysis`：

1. 登记财报、业绩会、市场预期、价格反应和至少 1 家可比同行财报来源
2. 输出 `earnings-analysis-package`
3. 先描述核心业务、核心增长和核心拖累
4. 用定价权和放量能力判断增长质量
5. 用同行财报验证公司口径是行业 beta 还是公司 alpha
6. 判断 `thesis_impact`
7. 仅当 `thesis_impact` 不为 `0` 或出现新风险时，更新标准 `research package`
