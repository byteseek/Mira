# Industry Concept Analysis Skill

这个 skill 用于把一个不清晰的产业概念快速拆成可研究、可跟踪、可映射到标的的产业链框架。

典型输入包括：

- `存储`
- `CPU`
- `GPU`
- `ABF`
- `HBM`
- `CPO`
- `液冷`
- `先进封装`

它不是单票研究，也不是主题营销材料。它的目标是回答：

> 这个概念到底是什么，产业链谁负责什么，利润池和瓶颈在哪，哪些环节有定价权和放量弹性，哪些公司最值得进入下一轮单票研究。

## Use When

- 用户提到一个产业、技术、材料、零部件、工艺、设备或供应链概念，但概念边界不清晰
- 需要先建立产业地图，再决定研究哪些公司
- 需要比较上下游环节的议价权、供需状态、放量路径和盈利弹性
- 需要识别紧供需平衡、高溢价、高收益或潜在反转环节
- 需要把 T0/T1 机构式框架、产业实践经验和第一性思考沉淀成可复用研究流程

## Required Inputs

- `concept_name`
- `research_question`
- `market_scope`
  例如 `global` / `US` / `CN` / `multi`
- `research_cutoff_date`
- `thesis_horizon`
- `depth`
  可选：`quick_map` / `standard` / `deep_dive`
- `focus`
  可选：`supply_shortage` / `pricing_power` / `volume_ramp` / `stock_mapping` / `risk_scan`

## Core Principle

先定义概念边界，再画产业链；先判断利润池和瓶颈，再筛公司。

输出顺序必须服务实战阅读：先给一页结论和股票映射，再给完整底稿。完整产业链、证据和公司表是 diligence，不应该挡在最前面。

不要直接从热门公司或热门叙事出发。必须先回答：

1. 这个概念在物理、技术、工艺或商业流程中到底解决什么问题。
2. 它位于完整产业链的哪一层。
3. 需求端由谁真正拉动。
4. 供给端由谁真正卡住。
5. 哪一层能提价，哪一层只能放量，哪一层只是被动代工或交易拥挤。

## Analysis Sequence

### 0. One-Page Industry Map

正式报告最前面必须先给 `One-Page Industry Map`，用于 PM / 交易员 / 快速复盘阅读。

必须回答：

- `one_sentence_definition`
  一句话说清楚这个概念是什么。
- `current_judgment`
  当前是紧缺、均衡、宽松，还是结构性分化。
- `where_is_tight`
  紧在哪里，不紧在哪里。
- `best_economic_layers`
  哪些环节真正留利润。
- `best_stock_proxies`
  哪些上市公司最能映射这个概念，区分稳健、弹性、项目爬坡、间接映射。
- `core_formula`
  需求和供给分别由哪些变量相乘或相加决定。
- `key_debate`
  市场真正争论的变量。
- `what_to_monitor`
  5-8 个最关键跟踪指标。
- `falsification`
  什么事实会推翻当前判断。

这个部分允许压缩、判断、排序。后文 diligence 负责展开和追溯来源。

### 1. Concept Boundary

输出：

- plain-language definition
- technical definition
- adjacent concepts
- what it is not
- why the concept matters now

必须避免把相邻概念混在一起。例如：

- `GPU` 不是整个 AI 算力产业链
- `HBM` 不是所有 DRAM
- `ABF` 是高端封装基板材料/载板链条中的关键环节，不等同于所有 PCB
- `CPU` 的服务器、PC、手机、车载和边缘场景的供需逻辑不同

### 2. Value Chain Map

至少拆成：

- upstream inputs
- core technology or process layer
- manufacturing / integration layer
- downstream customers
- end-demand drivers
- substitutes and competing architectures

每一层必须记录：

- main function
- representative companies
- supply concentration
- demand concentration
- margin structure
- capex / capacity cycle
- typical lead time
- key bottleneck

### 3. Company Map

公司映射必须分层，不允许只列龙头。

建议分类：

- global leaders
- regional leaders
- focused pure plays
- diversified conglomerates
- critical private companies
- public proxies
- downstream beneficiaries
- upstream picks-and-shovels

对每家公司至少记录：

- ticker / market if public
- value-chain position
- exposure purity
- competitive edge
- customer or supplier dependency
- key disclosed metric to monitor
- why it matters for this concept

### 4. Pricing And Volume Mechanics

把每个环节拆成两条线：

- `pricing`
  价格由成本加成、供需缺口、产品代际、认证稀缺、客户切换成本、合同结构还是 spot price 决定。
- `volume`
  放量由终端需求、客户认证、产能扩建、良率、设备交期、材料瓶颈、渠道库存还是政策补贴决定。

必须显式判断：

- 谁能提价
- 谁只能靠出货
- 谁提价会被客户压回去
- 谁放量受制于上游
- 谁的高增长只是低基数

### 5. Tightness And Profit Pool Ranking

对每个环节给出定性评分：

- `supply_demand_tightness`
  `loose` / `balanced` / `tight` / `shortage`
- `pricing_power`
  `low` / `medium` / `high`
- `volume_visibility`
  `low` / `medium` / `high`
- `margin_capture`
  `low` / `medium` / `high`
- `stock_proxy_quality`
  `weak` / `usable` / `strong`

然后输出：

- current bottleneck layer
- best profit-pool layer
- best volume-ramp layer
- best public-market proxy layer
- most crowded narrative layer
- most fragile assumption

## Institutional + Practical + First-Principles Lens

每次研究必须把三类视角并排使用：

- `institutional_lens`
  像 T0/T1 机构一样关注 TAM、竞争格局、供需模型、价格曲线、盈利弹性、估值锚和可验证数据。
- `operator_lens`
  像产业实践者一样关注认证周期、良率、产能爬坡、客户导入、库存、合同、供应商切换成本和交付风险。
- `first_principles_lens`
  从物理约束、工艺约束、资本开支约束、组织能力约束和需求真实刚性出发，拆掉概念炒作。

如果三类视角冲突，必须明确写出：

- conflict
- which lens is probably more reliable for the current question
- what evidence would resolve it

## Required Source Types

至少使用：

- `L1` 公司披露、财报、招股书、业绩会、IR 材料
- `L2` 官方、监管、行业协会、技术标准、产业组织材料
- `L3` 高质量券商或专业行业研究
- `L5` 市场数据、估值、价格或股价表现数据

可选但有用：

- `L4` 权威新闻、访谈、行业媒体
- `L6` agent 整理的产业链表格，但必须指向上游 `L1` 到 `L5` 来源

## Output Package

这个 skill 必须输出 `industry-analysis-package`：

- `industry-map.md`
- `company-map.csv`
- `evidence-log.csv`

`industry-map.md` 必须包含：

- one-page industry map
- concept boundary
- value chain map
- demand map
- supply map
- pricing mechanics
- volume mechanics
- tightness and profit-pool ranking
- company shortlist
- stock research handoff
- monitoring dashboard
- open questions

## Handoff To Equity Research

当某个公司进入下一轮单票研究时，把它交给 `equity-research-core`。

handoff 必须包含：

- target company
- why this company is a good proxy
- concept exposure purity
- value-chain position
- expected pricing / volume driver
- top 3 evidence items
- top 3 risks
- falsification condition

如果单票研究需要继续沿上下游验证，可以在 `equity-research-core` 中启用 `supply-chain` overlay。

## Quality Bar

- 不能只解释概念，必须落到产业链层级和标的候选。
- 不能把完整底稿放在最前面；必须先输出一页版结论。
- 不能只列公司，必须说明每家公司处在哪一层、为什么重要、暴露度是否纯。
- 不能只讲需求，必须同时讲供给约束和放量路径。
- 不能只讲高景气，必须指出利润池在哪里、谁能留住利润、谁可能只是传导。
- 不能把 sell-side 观点直接当结论，必须用公司披露或产业数据交叉验证。
- 不能把公司口径、产业预测、长期目标或市场叙事写成已验证事实，必须在 evidence log 中保留 claim type。
- 不能把高增速等同于好股票，必须区分产业好、公司好、股票好。
- 每个核心判断都必须能回溯到 evidence log。
