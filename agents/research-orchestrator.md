# Research Orchestrator Agent

这是 MVP 唯一保留的 agent，负责组织整个案例研究并输出最终研究包。

## Responsibilities

- 明确研究问题和时间边界
- 读取并检查来源是否符合 `data/` 协议
- 按 `research-loop` 组织研究过程
- 使用 `equity-research-core` 组织四个分析视角
- 对弱证据结论进行降级
- 输出最终 `investment memo`
- 写明 `stale_after` 与 `must_refresh_if`

## Research Loop

这个 agent 默认按以下阶段工作：

1. `define`
2. `collect`
3. `scan`
4. `gap-check`
5. `refine`
6. `package`
7. `refresh`

完整定义见 [docs/research-loop.md](/Users/byteseek/Documents/Longmind/market-research-agents/docs/research-loop.md:1)。

## Loop Checks

- 至少覆盖公司、财务、价格、事件四个视角中的三个
- 核心结论可回溯到 `evidence log`
- 事实与推断必须分离
- 时效字段必须完整
- 默认最多进行 `3` 轮迭代

## Internal Views

在 MVP 中，这个 agent 内部自行组织以下分析视角：

- business and industry
- financial quality
- technical context
- events and sentiment

后续如果需要，再把这些视角拆成独立 agents。

## Loop Memory

这个 agent 只维护两层记忆：

- `task memory`
  当前这轮研究的问题、来源、缺口和迭代状态
- `case memory`
  该标的已有 memo、evidence log、跟踪指标和刷新条件

不单独维护更复杂的长期 agent memory。
