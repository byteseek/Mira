# Mira

> Mira System

一个面向 `Codex`、`Claude Code` 等代理的股票投研系统。

这个仓库不是单一报告模板，也不是一次性问题求解脚本。它提供一套可 clone 的研究系统框架，用来组织：

- 多源数据
- 一个核心分析 skill
- 一个研究 orchestrator
- 两类 loop
- 分层 memory
- 一个可复用的 `research package`

`Mira` 的当前最小方向已经升级为“主题驱动的双循环研究框架”。

`Mira` 这个名字用于表达：

- observation
- insight
- research-first cognition
- 可扩展的 agent system

## V1 Principles

- 研究过程必须可追溯到来源，不接受“无来源结论”。
- 事实、推断、判断必须分层书写。
- 本地材料和网页抓取材料必须使用同一套 source metadata。
- 每份研究包必须明确时效边界与刷新触发条件。
- `skills` 负责分析能力，`agents` 负责研究组织，不混用概念。

## Naming

- system: `Mira`
- current repo role: `Mira` 的 research workspace
- future-friendly module naming:
  - `mira-agents`
  - `mira-skills`
  - `mira-research`
  - `mira-exec`

## Repository Layout

```text
.
├── README.md
├── agents/
│   └── research-orchestrator.md
├── cases/
│   └── aapl-2026-04/
│       ├── README.md
│       ├── case-notes.md
│       ├── evidence-log.csv
│       └── investment-memo.md
├── data/
│   ├── source-policy.md
│   ├── source-registry.csv
│   ├── source-schema.md
│   └── time-policy.md
├── loops/
│   ├── monitoring-loop.md
│   └── research-loop.md
├── memory/
│   ├── MEMORY-RULES.md
│   ├── playbooks/
│   │   ├── ai-theme-crowding.md
│   │   └── earnings-reaction.md
│   ├── research/
│   │   └── AAPL/
│   │       ├── refresh-log.md
│   │       ├── thesis.md
│   │       └── timeline.md
│   └── skills/
│       ├── financial-quality.md
│       └── technical-analysis.md
├── skills/
│   └── equity-research-core/
│       └── SKILL.md
└── templates/
    └── research-package/
        ├── case-notes.md
        ├── evidence-log.csv
        └── investment-memo.md
```

## Core Building Blocks

### 1. Data Layer

`data/` 定义统一的数据协议：

- 来源字段 schema
- 来源优先级与使用规则
- 获取方式分类
- 时效窗口与失效条件
- 常用来源注册表

### 2. Core Skill

`skills/` 当前只保留一个主 skill：

- `equity-research-core`

它在一份研究里统一组织四个视角：

- 公司与行业
- 财务质量
- 技术面上下文
- 事件与舆情

### 3. Orchestrator Agent

`agents/` 当前只保留一个 agent：

- `research-orchestrator`

这个 agent 目前负责：

- 检查 source metadata
- 按 `research-loop` 建立初始 thesis
- 按 `monitoring-loop` 做持续更新
- 组织四个研究视角
- 输出统一研究包
- 决定哪些内容进入长期 memory

后续如果需要，再拆成多个 monitors 和专题 analysts。

### 4. Loops

[loops/research-loop.md](/Users/byteseek/Documents/Longmind/market-research-agents/loops/research-loop.md:1) 用于首次研究或 thesis 重建。

[loops/monitoring-loop.md](/Users/byteseek/Documents/Longmind/market-research-agents/loops/monitoring-loop.md:1) 用于对已建立 thesis 的主题做持续更新。

### 5. Memory

`memory/` 使用 wiki-style 分层结构：

- `research/`
  存研究结果链
- `playbooks/`
  存市场经验类型
- `skills/`
  存技能方法论

完整规则见 [memory/MEMORY-RULES.md](/Users/byteseek/Documents/Longmind/market-research-agents/memory/MEMORY-RULES.md:1)。

### 6. Research Package

每个案例都输出一个统一研究包，由三部分组成：

- `investment memo`
- `evidence log`
- `case notes`

## Recommended Usage

1. 先在 `data/` 里确认来源类型、时效规则、获取方式。
2. 先用 `loops/research-loop.md` 建立首版 thesis。
3. 由 `agents/research-orchestrator.md` 汇总并输出研究包。
4. 稳定内容写入 `memory/`。
5. 后续更新走 `loops/monitoring-loop.md`。
6. 参考 `templates/research-package/` 生成研究包。
7. 查看 `cases/aapl-2026-04/` 作为完整样板。

## V1 Boundaries

- 当前版本不是自动化抓取平台。
- 当前版本先定义 monitor 职责，不实现完整多 agent 调度系统。
- 当前版本只放一个单票深度案例，不做主题篮子或双票对比。
- 当前版本的 memory 只沉淀慢变量，不记录全部日常噪音。

## What To Extend Next

- 拆分 `equity-research-core` 为独立主题 skills
- 把 `research-orchestrator` 拆成多个 monitors 和专题 agents
- 给 A 股补更细的本地数据源注册表
- 增加第二个案例，例如 A 股龙头或周期股
- 给 monitoring loop 增加固定日志模板
