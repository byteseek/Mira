# Mira

Mira 是一个面向 AI agent 和研究使用者的投资研究工作台。

它的目标不是生成一份孤立的股票报告，也不是把一次问答包装成研究结论，而是把多源材料组织成可追溯、可复核、可持续更新的投资判断。Mira 关注的是投资 thesis：这个判断基于什么证据、在什么时间点成立、哪些变量会证伪它、后续应该如何监控。

当前仓库是 `Mira` 的 research workspace，用来定义数据协议、分析能力、研究 loop、agent 职责、memory 规则和可复用的研究包模板。

## 为什么设计 Mira

投资研究在 agent 环境里最容易出现几个问题：

- 一次性问答不可复用，下一次研究又要重新组织上下文。
- 结论没有来源链，无法判断哪些是事实、哪些是推断、哪些只是观点。
- 研究对象变化后仍套同一份模板，忽略了不同标的的定价主导变量。
- 财报、新闻、价格、宏观变量和社媒信息混在一起，重要更新和噪音难以区分。
- 好的方法论散落在单次案例里，不能沉淀、试用、复盘和退役。
- 后续跟踪缺少刷新条件，旧 thesis 很容易在环境变化后继续被误用。

Mira 用一套明确的系统边界解决这些问题：

- 用 `source metadata` 和 `evidence log` 记录来源、时间、可信度和使用位置。
- 用 `research package` 固化投资 memo、证据表和案例 notes。
- 用 `framework routing` 先判断定价机制，再决定分析权重。
- 用 `overlay` 在主框架外叠加高价值专题研究路径。
- 用 `monitoring loop` 对已有 thesis 做增量更新和升级判断。
- 用 `methodology research loop` 研究方法本身，把可复用方法纳入状态机。
- 用 `memory` 只沉淀慢变量、稳定经验和经过验证的方法。

## Mira 能做什么

Mira 当前支持这些研究动作：

- 首次覆盖一个投资主题或单一标的，并输出标准 `research package`。
- 在核心前提变化后重建 thesis，而不是只修补旧结论。
- 对财报、业绩会、指引和同业财报做专项拆解，判断 `thesis impact`。
- 判断宏观经济、利率、美元、信用、流动性和风险偏好是否改变资产定价链。
- 按需监控已有 thesis 的新增信息，区分小更新、风险变化和完整重研触发。
- 在分析前执行 `framework routing`，识别当前主要定价变量。
- 在主框架外叠加 `overlay`，例如供应链、宏观、同业验证或后续扩展的渠道检查。
- 对预期差问题使用 `variant perception checklist`，明确市场共识、错价变量和证伪条件。
- 研究投资研究方法本身，把方法放入 `todo / trial / adopted / retired`。
- 把稳定结论写入 wiki-style `memory`，避免每轮研究从零开始。

## 核心原则

- 研究过程必须可追溯到来源，不接受无来源结论。
- 事实、推断、判断必须分层书写。
- 本地材料、网页材料、市场数据、宏观数据和派生分析使用同一套来源协议。
- 每份研究包必须明确时效边界、刷新条件和证伪条件。
- `skills` 负责分析能力，`agents` 负责研究组织，不混用概念。
- 技术面、宏观面、事件面和舆情都服务于投资 thesis，不单独变成交易系统。

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

## 三类 Loop

Mira 当前有三类 loop。文件名保持工程稳定，文档展示名采用更清楚的中文定位。

### 投资分析 loop

工程文件：[loops/research-loop.md](loops/research-loop.md)

`投资分析 loop` 用于首次覆盖或 thesis 重建。它围绕投资问题建立初始认知，经过定义问题、框架路由、选择 overlay、收集来源、扫描、缺口检查、修正和打包，最后输出 `research package`。

这条 loop 的核心对象是投资判断，可以覆盖单一股票、行业主题、宏观变量驱动的资产线索，以及后续扩展的商品、加密或跨资产主题。只要目标是形成或重建投资 thesis，就应该走这条 loop。

### 监控 loop

工程文件：[loops/monitoring-loop.md](loops/monitoring-loop.md)

`监控 loop` 用于已有 thesis 的持续更新。它不是后台采集任务，也不是重新研究全案，而是在用户触发、研究刷新或明确监控窗口内按需读取新增信号。

它负责过滤噪音、写入监控记录、判断增量信息是否改变 thesis、风险、节奏、框架或 overlay，并决定是否升级回完整的投资分析 loop。

### 方法论研究 loop

工程文件：[loops/methodology-research-loop.md](loops/methodology-research-loop.md)

`方法论研究 loop` 研究的是研究方法本身，而不是某一只股票。它回答哪些方法在哪些场景有效、核心假设是什么、失效模式是什么、是否值得进入正式 framework 或 overlay。

这条 loop 允许从研报、访谈、帖子、纪要、投资笔记或他人分析结果中逆向拆方法，再按可信度、可复现性、解释力、验证方式和后续跟踪质量决定进入 `todo / trial / adopted / retired`。

## 投资分析框架

Mira 当前的主分析能力由 [skills/equity-research-core/](skills/equity-research-core/) 提供。它在统一输出格式下组织五类视角：

- 公司与行业
- 财务质量
- 宏观经济与金融条件
- 技术面上下文
- 事件与舆情

但 Mira 不会默认对所有标的套同一权重。正式分析前必须先做 `framework routing`，也就是判断当前标的主要由什么变量定价。

当前默认主框架包括：

- `micro-small`：适合低流动性、估值锚弱、单一催化剂可能重写预期的小微盘或事件型标的。
- `mid-cap`：适合中盘且流动性尚可、板块轮动、行业景气、公司叙事和业绩兑现共同影响的标的。
- `large-mega`：适合大盘或超大盘，盈利预期、贴现率、资本开支、机构配置和宏观周期主导中期方向的标的。

框架选择规则见 [skills/equity-research-core/references/framework-routing.md](skills/equity-research-core/references/framework-routing.md)。

主框架之外可以叠加 `overlay`。overlay 不替代主框架，只补充一条高价值研究路径。

当前默认支持：

- `supply-chain`：验证上下游传导、客户集中度、收入确定性和同层级公司对照。
- `macro`：判断增长、通胀、政策、利率、美元、信用、流动性和风险偏好是否正在改变目标资产的定价链。

`macro` 不是固定宏观背景段落。只有当宏观能改变收入、利润率、贴现率、风险溢价、融资条件、仓位或催化剂时，才进入核心结论。

overlay 规则见 [skills/equity-research-core/references/overlay-routing.md](skills/equity-research-core/references/overlay-routing.md)，宏观 overlay 说明见 [skills/equity-research-core/references/macro-overlay.md](skills/equity-research-core/references/macro-overlay.md)。

## 研究产物

### Research Package

标准研究包由三部分组成：

- `investment memo`：投资判断、关键证据、时效边界、刷新条件和证伪条件。
- `evidence log`：来源、claim area、claim type、使用位置、as-of date、confidence 和备注。
- `case notes`：研究过程中的中间观察、缺口、冲突和事实/推断分层。

每份标准研究包还必须写明：

- `selected_framework`
- `framework_basis`
- `framework_mismatch_risk`
- `selected_overlays`
- `overlay_basis`

模板见 [templates/research-package/](templates/research-package/)。

### Earnings Analysis Package

财报事件可先输出轻量财报分析包，再决定是否更新标准研究包。

当前财报专项 skill 是 [skills/earnings-report-analysis/](skills/earnings-report-analysis/)，重点覆盖：

- 披露核验
- 核心业务、核心增长、核心拖累
- 定价权和放量能力
- 三表联动
- 经营驱动桥接
- 同业同期财报对比
- 管理层口径
- 市场预期差
- thesis impact

模板见 [templates/earnings-analysis-package/](templates/earnings-analysis-package/)。

### Macro Analysis

宏观经济专项分析由 [skills/macro-economic-analysis/](skills/macro-economic-analysis/) 承载。它用于拆解增长、通胀、政策、利率、美元、信用、流动性和风险偏好，并判断这些变量是否改变某个资产或主题的投资 thesis。

方法论沉淀见 [memory/methodologies/macro-regime-analysis.md](memory/methodologies/macro-regime-analysis.md)。

### Methodology Artifacts

方法论研究使用单独产物：

- [templates/methodology-card.md](templates/methodology-card.md)
- [templates/methodology-queue.csv](templates/methodology-queue.csv)
- [templates/methodology-review-log.csv](templates/methodology-review-log.csv)
- [templates/methodology-search-log.csv](templates/methodology-search-log.csv)
- [templates/variant-perception-checklist.md](templates/variant-perception-checklist.md)

## 主要模块

### Data Layer

[data/](data/) 定义统一的数据协议：

- 来源字段 schema
- 来源优先级与使用规则
- 公开网页和公开端点的按需读取目标
- 获取方式分类
- 时效窗口与失效条件
- 常用来源注册表
- 方法论来源分层规则

### Skills

[skills/](skills/) 定义可复用分析能力。

当前包括：

- `equity-research-core`：主投资分析 skill，负责统一视角、框架路由和 overlay 选择。
- `earnings-report-analysis`：财报专项 skill，负责财报质量、同业对比和 thesis impact。
- `macro-economic-analysis`：宏观专项 skill，负责宏观变量、金融条件和资产定价链分析。

### Agent

[agents/research-orchestrator.md](agents/research-orchestrator.md) 是当前主控 agent。

它负责明确研究问题和时间边界、检查来源协议、运行投资分析 loop 或监控 loop、执行 framework / overlay selection、组织统一输出、降级弱证据结论，并决定哪些内容写入 memory。

当前版本先保留一个 orchestrator。未来如果职责变复杂，再拆成多个 monitors 和专题 analysts。

### Memory

[memory/](memory/) 使用 wiki-style 分层结构：

- `research/`：存研究结果链。
- `methodologies/`：存方法论队列、试用、采用和退役状态。
- `playbooks/`：存市场经验类型。
- `skills/`：存技能方法论。

完整规则见 [memory/MEMORY-RULES.md](memory/MEMORY-RULES.md)。

### Cases

[cases/](cases/) 存当前样板案例：

- [cases/aapl-2026-04/](cases/aapl-2026-04/)：标准 research package 示例。
- [cases/cohr-2026-05/](cases/cohr-2026-05/)：财报事件分析包示例。

## 推荐使用路径

### 建立或重建投资 thesis

1. 在 [data/](data/) 中确认来源类型、时效规则和获取方式。
2. 用 [loops/research-loop.md](loops/research-loop.md) 进入投资分析 loop。
3. 在 `define` 后先完成 `route-framework`。
4. 如有必要，再完成 `select-overlays`，例如 `supply-chain` 或 `macro`。
5. 按选定框架与 overlay 建立首版 thesis。
6. 由 [agents/research-orchestrator.md](agents/research-orchestrator.md) 汇总并输出统一研究包。
7. 稳定内容写入 [memory/](memory/)。
8. 后续更新走 [loops/monitoring-loop.md](loops/monitoring-loop.md)。

### 分析财报事件

1. 用 [skills/earnings-report-analysis/](skills/earnings-report-analysis/) 登记财报、业绩会、市场预期、价格反应和至少一家可比同行财报来源。
2. 输出 [templates/earnings-analysis-package/](templates/earnings-analysis-package/) 对应的轻量分析包。
3. 判断 `thesis_impact`。
4. 仅当财报改变 thesis 或引入新风险时，再更新标准 `research package`。

### 分析宏观驱动

1. 用 [skills/macro-economic-analysis/](skills/macro-economic-analysis/) 明确宏观问题、资产范围、时间窗口和目标变量。
2. 判断宏观变量是否只是背景，还是会改变收入、利润率、贴现率、风险溢价、融资条件、仓位或催化剂。
3. 如果宏观变量会改变定价链，在投资分析 loop 中启用 `macro` overlay。
4. 将稳定方法沉淀到 `memory/methodologies/`，并通过真实案例继续验证。

### 研究方法论

1. 用 [loops/methodology-research-loop.md](loops/methodology-research-loop.md) 明确方法论研究对象。
2. 从研报、纪要、帖子、访谈、课程或别人分析中抽取候选方法。
3. 用 [templates/methodology-search-log.csv](templates/methodology-search-log.csv) 记录搜索路径、语言圈层、支持与反对材料，以及遗漏点。
4. 用 [templates/methodology-card.md](templates/methodology-card.md) 拆解方法、假设、适用范围、失效模式、credibility 和 search coverage。
5. 用 [templates/methodology-queue.csv](templates/methodology-queue.csv) 比较方法的解释力、可复用性、可信度和 follow-through 质量。
6. 把方法放入 `memory/methodologies/todo.md` 或 `trial.md`。
7. 通过 case backtest、forward watch 或 live trial 做验证。
8. 只有经过真实案例验证的方法，才进入 `adopted.md`。
9. 已失效、重复或噪音过高的方法移到 `retired.md`。

## 仓库结构

```text
.
├── agents/
│   └── research-orchestrator.md
├── cases/
│   ├── aapl-2026-04/
│   └── cohr-2026-05/
├── data/
│   ├── methodology-source-policy.md
│   ├── public-source-targets.md
│   ├── source-policy.md
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
│   ├── playbooks/
│   └── skills/
├── skills/
│   ├── earnings-report-analysis/
│   ├── macro-economic-analysis/
│   └── equity-research-core/
└── templates/
    ├── earnings-analysis-package/
    ├── research-package/
    ├── methodology-card.md
    ├── methodology-queue.csv
    ├── methodology-review-log.csv
    ├── methodology-search-log.csv
    └── variant-perception-checklist.md
```

## V1 边界

- 当前版本不是自动化抓取平台。
- 当前版本不是交易执行系统。
- 当前版本先定义 monitor 职责，不实现完整多 agent 调度系统。
- 当前版本包含一个单票深度案例和一个财报事件案例，暂不做完整主题篮子。
- 当前版本的 memory 只沉淀慢变量，不记录全部日常噪音。
- 当前版本先支持 `supply-chain` 和 `macro` overlay，不把专题研究路径无限扩张。
- 当前版本定义 methodology research loop，但不承诺自动联网归档全部方法论来源。
- 当前版本的方法论验证仍以 case-level follow-through 为主，不提供完整量化回测引擎。
- 当前版本的方法论搜索仍以手工查询设计和记录为主，尚未接自动 query expansion engine。

## Naming

- system: `Mira`
- current repo role: `Mira` 的 research workspace
- current main document: `README.md`
- future-friendly module naming:
  - `mira-agents`
  - `mira-skills`
  - `mira-research`
  - `mira-exec`

## What To Extend Next

- 继续补强 `earnings-report-analysis` 的行业特定指标。
- 增加更多 framework，例如 `cyclical`、`turnaround`、`compounder`。
- 增加更多 overlay，例如 `channel-check`、`peer-benchmark`。
- 用真实案例验证 `macro-regime-analysis`，通过后再从 `trial` 升级到 `adopted`。
- 增加方法论评分与案例验证挂钩。
- 增加方法论 review log 和长期 follow-through 记录。
- 增加 methodology query expansion 和搜索自动化。
- 拆分 `equity-research-core` 为独立主题 skills。
- 把 `research-orchestrator` 拆成多个 monitors 和专题 agents。
- 给 A 股补更细的本地数据源注册表与公开网页 target set。
- 增加第二个案例，例如 A 股龙头或周期股。
- 给 monitoring loop 增加固定日志模板。
