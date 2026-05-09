# Mira

> Mira System

一个面向 `Codex`、`Claude Code` 等代理的股票投研系统。

这个仓库不是单一报告模板，也不是一次性问题求解脚本。它提供一套可 clone 的研究系统框架，用来组织：

- 多源数据
- 一个可路由的核心分析 skill
- 一个研究 orchestrator
- 三类 loop
- 分层 memory
- 一个可复用的 `research package`

`Mira` 的当前最小方向是“主题驱动的双循环研究框架 + framework routing + optional overlays + empirical methodology research”。

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

## Mira Mode

当用户在这个项目语境里说 `Mira`，默认表示进入项目思考模式，而不是只把它当作普通名称。

`Mira Mode` 的含义：

- 先把问题理解为一个投研任务、方法论任务或监控任务。
- 先确认时间边界、研究对象、市场范围和已有来源。
- 默认使用 `research-loop`、`monitoring-loop` 或 `methodology-research-loop` 中最匹配的一条路径。
- 在正式分析前先做 `framework selection`，必要时再做 `overlay selection`。
- 输出时分离事实、推断和判断，并写明证据来源、时效边界、刷新条件和失效条件。
- 不把无来源观点写成结论；证据不足时明确降级。

简写触发约定：

- `Mira, 看一下 X`：按当前上下文判断是首次研究、增量监控还是方法论研究。
- `Mira, 更新 X`：优先进入 `monitoring-loop`，只处理新增信息和 thesis impact。
- `Mira, 研究 X`：优先进入 `research-loop`，建立或重建首版研究包。
- `Mira, 这个方法靠谱吗`：优先进入 `methodology-research-loop`。

如果用户没有给出足够上下文，先补齐最少必要字段，再开始研究；不要把 `Mira` 理解成自动化抓取或后台常驻监控承诺。

## Repository Layout

```text
.
├── README.md
├── agents/
│   └── research-orchestrator.md
├── cases/
│   ├── aapl-2026-04/
│   │   ├── README.md
│   │   ├── case-notes.md
│   │   ├── evidence-log.csv
│   │   └── investment-memo.md
│   └── cohr-2026-05/
│       ├── README.md
│       ├── earnings-analysis.md
│       ├── evidence-log.csv
│       ├── financial-snapshot.csv
│       └── peer-comparison.csv
├── data/
│   ├── methodology-source-policy.md
│   ├── source-policy.md
│   ├── public-source-targets.md
│   ├── source-registry.csv
│   ├── source-schema.md
│   └── time-policy.md
├── loops/
│   ├── methodology-research-loop.md
│   ├── monitoring-loop.md
│   └── research-loop.md
├── memory/
│   ├── MEMORY-RULES.md
│   ├── methodologies/
│   │   ├── adopted.md
│   │   ├── retired.md
│   │   ├── todo.md
│   │   └── trial.md
│   ├── playbooks/
│   │   ├── ai-theme-crowding.md
│   │   └── earnings-reaction.md
│   ├── research/
│   │   └── AAPL/
│   │       ├── refresh-log.md
│   │       ├── thesis.md
│   │       └── timeline.md
│   └── skills/
│       ├── earnings-report-analysis.md
│       ├── financial-quality.md
│       └── technical-analysis.md
├── skills/
│   ├── earnings-report-analysis/
│   │   └── SKILL.md
│   ├── macro-economic-analysis/
│   │   └── SKILL.md
│   └── equity-research-core/
│       ├── SKILL.md
│       └── references/
│           ├── framework-routing.md
│           ├── large-mega.md
│           ├── macro-overlay.md
│           ├── micro-small.md
│           ├── mid-cap.md
│           ├── overlay-routing.md
│           └── supply-chain-overlay.md
└── templates/
    ├── earnings-analysis-package/
    │   ├── earnings-analysis.md
    │   ├── evidence-log.csv
    │   ├── financial-snapshot.csv
    │   └── peer-comparison.csv
    ├── methodology-card.md
    ├── methodology-queue.csv
    ├── methodology-review-log.csv
    ├── methodology-search-log.csv
    ├── variant-perception-checklist.md
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
- 公开网页/端点的按需读取目标
- 获取方式分类
- 时效窗口与失效条件
- 常用来源注册表
- 方法论来源分层规则

### 2. Core Skill

`skills/` 当前保留一个主 skill 和一个财报专项 skill：

- `equity-research-core`
- `earnings-report-analysis`

`equity-research-core` 在一份研究里统一组织五类视角：

- 公司与行业
- 财务质量
- 宏观经济与金融条件
- 技术面上下文
- 事件与舆情

但在进入分析前，会先做 `framework selection`。

当前默认提供三个主框架：

- `micro-small`
- `mid-cap`
- `large-mega`

这三个框架不改变统一产物格式，只改变：

- 研究问题的优先级
- 证据权重
- 章节侧重点
- 刷新触发条件

在主框架之外，还可以叠加专题 `overlay`。

当前默认先支持：

- `supply-chain`
- `macro`

overlay 用于沿上下游和同层级继续挖证据链，不替代主框架。

`macro` overlay 用于判断增长、通胀、政策、利率、美元、信用、流动性和风险偏好是否正在改变目标资产的定价链。它不是固定宏观背景段落；只有当宏观能改变收入、利润率、贴现率、风险溢价、融资条件、仓位或催化剂时，才进入核心结论。

`earnings-report-analysis` 用于对单份季报、半年报或年报做结构化拆解，重点覆盖：

- 披露核验
- 核心业务、核心增长、核心拖累
- 定价权和放量能力
- 三表联动
- 经营驱动桥接
- 同业同期财报对比
- 管理层口径
- 市场预期差
- thesis impact

### 3. Orchestrator Agent

`agents/` 当前只保留一个 agent：

- `research-orchestrator`

这个 agent 目前负责：

- 检查 source metadata
- 按 `research-loop` 建立初始 thesis
- 按 `monitoring-loop` 做持续更新
- 路由研究框架、选择 overlay，并组织五类研究视角
- 输出统一研究包
- 决定哪些内容进入长期 memory

后续如果需要，再拆成多个 monitors 和专题 analysts。

### 4. Loops

[loops/research-loop.md](/Users/byteseek/Documents/Longmind/market-research-agents/loops/research-loop.md:1) 用于首次研究或 thesis 重建。

[loops/monitoring-loop.md](/Users/byteseek/Documents/Longmind/market-research-agents/loops/monitoring-loop.md:1) 用于对已建立 thesis 的主题做持续更新。

[loops/methodology-research-loop.md](/Users/byteseek/.codex/worktrees/9ee2/market-research-agents/loops/methodology-research-loop.md:1) 用于研究研究方法本身，决定哪些方法进入 `todo / trial / adopted / retired`。

这条 loop 不预设“机构方法更好”或“野路子方法更差”。它允许从研报、帖子、纪要和他人分析中逆向抽方法，再按可信度、可复现性、案例表现和后续跟踪决定是否保留。

它还要求方法论搜索本身具备覆盖度，不允许只搜单一语言、单一圈层或单一立场后就下结论。

### 5. Memory

`memory/` 使用 wiki-style 分层结构：

- `research/`
  存研究结果链
- `methodologies/`
  存方法论队列、试用、采用和退役状态
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

统一研究包之外，当前版本要求每次研究都明确写出：

- `selected_framework`
- `framework_basis`
- `framework_mismatch_risk`
- `selected_overlays`
- `overlay_basis`

财报事件可先输出一个轻量 `earnings analysis package`：

- `earnings-analysis`
- `financial-snapshot`
- `peer-comparison`
- `evidence-log`

当财报足以改变 thesis 时，再把结论并入标准 `research package`。

方法论研究使用单独产物：

- `methodology-card.md`
- `methodology-queue.csv`
- `methodology-review-log.csv`
- `methodology-search-log.csv`
- `variant-perception-checklist.md`

## Recommended Usage

1. 先在 `data/` 里确认来源类型、时效规则、获取方式。
2. 在 `research-loop` 的 `define` 后先完成 `route-framework`。
3. 如有必要，再完成 `select-overlays`，例如 `supply-chain` 或 `macro`。
4. 按选定框架与 overlay 建立首版 thesis。
5. 由 `agents/research-orchestrator.md` 汇总并输出统一研究包。
6. 稳定内容写入 `memory/`。
7. 后续更新走 `loops/monitoring-loop.md`，同时检查框架和 overlay 是否仍成立。
8. 财报事件先用 `skills/earnings-report-analysis/` 和 `templates/earnings-analysis-package/` 做专项拆解。
9. 参考 `templates/research-package/` 生成研究包。
10. 查看 `cases/aapl-2026-04/` 和 `cases/cohr-2026-05/` 作为当前样板。

如果研究对象是典型预期差问题，可以额外跑：

1. [templates/variant-perception-checklist.md](/Users/byteseek/.codex/worktrees/9ee2/market-research-agents/templates/variant-perception-checklist.md:1)
2. 先写 `consensus proxy`
3. 再写真正被错价的变量
4. 最后只允许落到 `wide variant / thin variant / no usable variant`

方法论研究使用独立路径：

1. 用 `loops/methodology-research-loop.md` 明确要研究的方法对象。
2. 允许从研报、纪要、帖子或别人的分析里逆向拆出隐含方法。
3. 用 `templates/methodology-search-log.csv` 记录搜索词族、语言圈层、支持与反对材料，以及遗漏点。
4. 用 `templates/methodology-card.md` 拆解方法、假设、适用范围、失效模式、credibility 和 search coverage。
5. 用 `templates/methodology-queue.csv` 比较方法的解释力、可复用性、可信度、搜索覆盖度和 follow-through 质量。
6. 把方法放入 `memory/methodologies/todo.md` 或 `trial.md`。
7. 通过 `case backtest`、`forward watch` 或 live trial 做验证。
8. 只有经过真实案例验证的方法，才进入 `adopted.md`。
9. 已失效、重复或噪音过高的方法移到 `retired.md`。

## V1 Boundaries

- 当前版本不是自动化抓取平台。
- 当前版本先定义 monitor 职责，不实现完整多 agent 调度系统。
- 当前版本包含一个单票深度案例和一个财报事件案例，暂不做主题篮子。
- 当前版本的 memory 只沉淀慢变量，不记录全部日常噪音。
- 当前版本先支持一个 overlay，不把专题研究路径无限扩张。
- 当前版本定义 methodology research loop，但不承诺自动联网归档全部方法论来源。
- 当前版本的方法论验证仍以 case-level follow-through 为主，不提供完整量化回测引擎。
- 当前版本的方法论搜索仍以手工查询设计和记录为主，尚未接自动 query expansion engine。

## What To Extend Next

- 继续补强 `earnings-report-analysis` 的行业特定指标
- 增加更多 framework，例如 `cyclical`、`turnaround`、`compounder`
- 增加更多 overlay，例如 `channel-check`、`peer-benchmark`
- 用真实案例验证 `macro-regime-analysis`，通过后再从 `trial` 升级到 `adopted`
- 增加方法论评分与案例验证挂钩
- 增加方法论 review log 和长期 follow-through 记录
- 增加 methodology query expansion 和搜索自动化
- 拆分 `equity-research-core` 为独立主题 skills
- 把 `research-orchestrator` 拆成多个 monitors 和专题 agents
- 给 A 股补更细的本地数据源注册表与公开网页 target set
- 增加第二个案例，例如 A 股龙头或周期股
- 给 monitoring loop 增加固定日志模板
