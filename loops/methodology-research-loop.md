# Methodology Research Loop

`methodology-research-loop` 用于研究研究方法本身，而不是研究某一只股票。

它的目标是持续回答：

- 哪种研究方法在哪些场景下有效
- 这些方法的核心假设是什么
- 哪些值得进入正式 framework 或 overlay
- 哪些“分析结果”背后其实藏着可复用的方法
- 还能从哪些搜索路径继续发现新的方法候选

## Loop Input

- `methodology_topic`
- `research_goal`
- `scope_hint`
  可选
- `source_buckets`
  可选，默认同时覆盖 `institutional`、`practitioner`、`first_principles`、`derived_internal`、`reverse_engineered`
- `comparison_baseline`
  可选
- `candidate_outputs`
  可选，用于对研报、帖子、纪要或别人分析做逆向拆解
- `search_seed_terms`
  可选，用于扩展搜索词族

## Source Buckets

- `institutional`
  券商、基金、投资人长文、正式研究流程
- `practitioner`
  实践型研究者、行业从业者、交易者总结
- `first_principles`
  从定价、竞争、产业链、行为和信息结构出发的底层方法
- `derived_internal`
  基于本仓库已有案例和经验提炼的方法
- `reverse_engineered`
  从研报、访谈纪要、社媒长文、投资笔记或他人分析结果中逆向抽方法

## States

### `define`

明确要研究的方法对象、目标和比较基线。

### `collect`

按 source buckets 收集候选方法，不要求一开始就下结论。

### `search`

搜索不是只搜方法名，而要同时做多维检索：

- `keyword search`
  直接搜方法名、同义词、缩写、常见变体
- `artifact search`
  搜研报、长文、纪要、访谈、播客、课程、论坛帖、招聘 JD、投资者信里隐含的方法
- `people search`
  搜哪些作者、机构、行业研究者反复使用类似方法
- `contradiction search`
  主动搜反例、批评、失败案例和方法争议
- `follow-through search`
  搜该方法是否有后续复盘、持续跟踪或多年使用记录
- `translation search`
  允许中英双语甚至同义表达切换，避免只被某个圈层术语绑住

每次搜索至少要尝试：

- 方法名
- 方法的功能描述
- 方法的反面问题
  例如不是搜 `channel check`，还要搜 `how to verify demand without company guidance`
- 作者或机构名
- 相关变量名
  例如库存、渠道、份额、切换成本、订单、capex、拥挤度

### `reverse-engineer`

如果候选材料不是在“讲方法”，而是在“展示一个分析结果”，允许逆向拆解：

- 作者到底看了哪些变量
- 变量优先级是什么
- 哪些证据被赋予高权重
- 隐含假设是什么
- 哪一步最像可复用方法，哪一步只是结论修辞

### `expand-query-set`

拿到一个候选方法后，继续自动扩展查询族：

- 同义词
- 相邻术语
- 更抽象的上位概念
- 更具体的下位动作
- 反对者常用的批评术语
- 作者本人未明说但读者会用的标签

### `extract`

把每条方法拆成统一字段：

- `method_name`
- `source_bucket`
- `source_quality`
- `credibility_score`
- `credibility_basis`
- `applies_to`
- `core_question`
- `required_inputs`
- `primary_signal`
- `failure_mode`
- `why_it_works`
- `when_not_to_use`
- `evidence_cost`
- `speed_vs_depth`
- `empirical_validation_mode`
- `follow_through_plan`

### `compare`

与现有方法做横向比较，至少回答：

- 它比现有方法多解释了什么
- 它在哪些场景更强
- 它在哪些场景只是噪音
- 它是“真方法”，还是“事后把结论包装得像方法”

### `score-credibility`

不要按来源类型直接判优劣，而要按以下问题打分：

- 逻辑链是否完整
- 输入变量是否清晰
- 有没有明确失效条件
- 是否能被别人复现
- 是否有真实案例或后续跟踪支撑
- 作者是否存在明显叙事偏见或结果导向包装

### `score-search-coverage`

不要因为找到一两篇高质量材料就停止搜索。

至少要判断：

- 来源类型是否足够分散
- 是否覆盖支持与反对两边
- 是否既看到了方法论表述，也看到了实际应用
- 是否找到了方法失效或被批评的场景

### `queue`

把候选方法放入状态机：

- `todo`
- `trial`
- `adopted`
- `retired`

### `trial-design`

如果值得试用，明确：

- 准备用什么 case 验证
- 预期提升什么
- 证伪条件是什么
- 是做 `case backtest`、`forward watch`，还是 `live trial`

### `review`

对进入 `trial` 或 `adopted` 的方法持续复盘：

- 有没有真的改善研究质量
- 有没有在后续 case 中表现稳定
- 是不是开始退化成噪音或故事化框架

### `write-memory`

把高质量结论写入 `memory/methodologies/`。

## Evaluation Dimensions

每条方法至少从以下维度评估：

- `credibility_score`
- `search_coverage`
- `explanatory_power`
- `repeatability`
- `falsifiability`
- `information_advantage`
- `cost_efficiency`
- `fit_with_mira`
- `follow_through_quality`

## Exit Criteria

- 已形成至少一张完整 `methodology card`
- 已说明相对现有方法的增量价值
- 已进入 `todo / trial / adopted / retired` 之一
- 如果进入 `trial` 或 `adopted`，已写明验证方式
- 如果是 reverse-engineered 方法，已说明逆向拆解依据
- 已记录核心搜索路径和遗漏点

## Stop Rules

- 如果只有表面话术、没有可执行差异，不进入 `trial`
- 如果方法不能说明适用场景与失效模式，不进入正式 memory
- 如果方法只是现有框架的改写，不重复建新条目
- 如果方法只在结果正确时看起来合理、结果错误时无法解释，不视为高质量方法
- 如果搜索只覆盖单一圈层或单一语言，不视为充分搜索
