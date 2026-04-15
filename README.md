# Market Research Toolbox

一个面向 `Codex`、`Claude Code` 等代理的股票投研工具箱。

这个仓库不是单一报告模板，也不是一次性问题求解脚本。它提供一套可 clone 的研究框架，用来组织：

- 多源数据
- 一个核心分析 skill
- 一个研究 orchestrator
- 一个可复用的 `research package`

当前仓库已经收敛到 MVP：先证明单一核心 skill 和单一 orchestrator 就能跑通一份完整研究包。

## V1 Principles

- 研究过程必须可追溯到来源，不接受“无来源结论”。
- 事实、推断、判断必须分层书写。
- 本地材料和网页抓取材料必须使用同一套 source metadata。
- 每份研究包必须明确时效边界与刷新触发条件。
- `skills` 负责分析能力，`agents` 负责研究组织，不混用概念。

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
├── docs/
│   └── research-loop.md
├── skills/
│   └── equity-research-core/
│       └── SKILL.md
└── templates/
    └── research-package/
        ├── case-notes.md
        ├── evidence-log.csv
        └── investment-memo.md
```

## MVP Building Blocks

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

这个 agent 在 MVP 里负责：

- 检查 source metadata
- 按 `research-loop` 推进任务
- 组织四个研究视角
- 输出统一研究包

后续如果需要，再拆回多主题 agents。

### 4. Research Loop

`docs/research-loop.md` 定义一次研究任务如何循环推进：

- loop input
- loop states
- loop memory
- loop exit criteria
- loop refresh triggers

### 5. Research Package

每个案例都输出一个统一研究包，由三部分组成：

- `investment memo`
- `evidence log`
- `case notes`

## Recommended Usage

1. 先在 `data/` 里确认来源类型、时效规则、获取方式。
2. 阅读 `docs/research-loop.md`，明确本轮研究输入、阶段和退出条件。
3. 使用 `skills/equity-research-core/` 组织研究。
4. 由 `agents/research-orchestrator.md` 负责汇总与输出。
5. 参考 `templates/research-package/` 生成研究包。
6. 查看 `cases/aapl-2026-04/` 作为完整样板。

## V1 Boundaries

- MVP 不是自动化抓取平台。
- MVP 不区分短线、中线、长线为独立 agent。
- MVP 只放一个单票深度案例，不做主题篮子或双票对比。
- MVP 不并列定义多个 skills 或多个 analysts。

## What To Extend Next

- 拆分 `equity-research-core` 为独立主题 skills
- 把 `research-orchestrator` 拆成多个主题 agents
- 给 A 股补更细的本地数据源注册表
- 增加第二个案例，例如 A 股龙头或周期股
