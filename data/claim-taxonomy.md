# Claim Taxonomy

这个文件定义 Mira 如何给研究中的每条信息做 `claim_type` 分类。

`source` 回答“信息从哪里来”。`claim` 回答“这条信息本质上是什么”。同一个来源可以同时包含事实、管理层说法、正式指引、长期目标、预测、假设和观点，因此不能只用来源可信度替代 claim 分类。

## Core Rule

每条进入 `evidence-log.csv` 的信息都必须标注：

- `claim_type`
- `claim_text`
- `source_speaker`
- `verification_status`

正式结论必须区分：

- 已发生事实
- 可验证承诺
- 公司指引
- 外部预测
- Mira 或研究员假设
- 观点解释
- 弱信号或传闻
- 市场定价

## Claim Types

| claim_type | meaning | example | default_use |
| --- | --- | --- | --- |
| `fact` | 已发生或可核验事实 | Q1 revenue, cash balance, signed filing date | 可支撑事实层结论 |
| `reported_metric` | 来源披露的指标或统计值 | backlog, RPO, active power, CPI print | 可支撑事实，但需记录口径 |
| `company_claim` | 公司或管理层说法 | demand remains strong, customer feedback is positive | 只能作为公司口径，需交叉验证 |
| `guidance` | 公司正式短中期指引 | FY revenue range, margin outlook, capex outlook | 可作为预期输入，不能当已兑现事实 |
| `target` | 长期目标、战略愿景或 aspirational goal | 2030 margin target, long-term TAM goal | 只能作为战略意图或情景输入 |
| `commitment` | 带责任主体、金额、时间或义务的承诺 | purchase commitment, take-or-pay, minimum volume | 可跟踪兑现，但需核验条款 |
| `forecast` | 外部或内部预测 | consensus EPS, sell-side TAM, agency forecast | 只代表预期，不代表事实 |
| `assumption` | 模型或 thesis 假设 | utilization improves, ASP flat, churn stable | 必须在 memo 中显式标为假设 |
| `interpretation` | 对事实或价格行为的解释 | stock fell because capex risk offset beat | 需要替代解释和证据链 |
| `opinion` | 观点、判断或建议 | analyst believes growth will accelerate | 不单独支撑 durable conclusion |
| `market_pricing` | 市场价格、估值、仓位或隐含预期 | multiple expansion, options IV, rate futures | 说明市场如何定价，不等于基本面验证 |
| `sentiment` | 情绪、叙事或关注度 | social chatter, media narrative intensity | 只作叙事或拥挤度信号 |
| `rumor_signal` | 未验证传闻或弱信号 | anonymous supply-chain rumor | 只能触发研究，默认不得支撑结论 |
| `derived_calculation` | Mira 或研究员基于上游来源计算 | YoY bridge, implied guide, FCF proxy | 必须列上游来源和公式 |

## Verification Status

| verification_status | meaning |
| --- | --- |
| `verified` | 已由原始披露、官方数据或多个高质量来源核验 |
| `disclosed` | 来源已经披露，但尚未独立验证 |
| `claimed` | 由公司、管理层、专家或媒体声称 |
| `estimated` | 外部机构、市场共识或 Mira 估算 |
| `modeled` | 模型假设或情景推演 |
| `unverified` | 尚未核验 |
| `contradicted` | 已被其他证据削弱或反驳 |

## Source Speakers

常用 `source_speaker`：

- `company`
- `management`
- `regulator`
- `official_agency`
- `exchange`
- `sellside`
- `buyside`
- `media`
- `industry_body`
- `market`
- `social`
- `mira`

## Required Distinctions

### Fact Vs Opinion

事实可以被核验。观点只能作为解释、假设来源或对手盘输入。观点型来源即使来自高声誉机构，也不能直接升级成事实。

### Commitment Vs Forecast

承诺通常有责任主体、义务、金额、时间或合同条款。预测只是对未来的估计。研究包必须说明一条未来信息是 `commitment`、`guidance`、`forecast` 还是 `assumption`。

### Guidance Vs Target

正式指引通常影响短中期预期和估值。长期目标更多反映战略意图，不能直接作为 near-term thesis anchor。

### Signal Vs Evidence

弱信号可以触发搜索、监控或假设生成，但不能单独支撑核心结论。

### Market Pricing Vs Fundamental Validation

价格反应说明市场如何处理信息，不说明基本面已经被验证。`market_pricing` 必须与事实或经营证据分开记录。

## Evidence Weight Rules

- `fact`、`reported_metric` 和经核验的 `commitment` 权重最高。
- `guidance` 是正式预期输入，但必须跟历史兑现率、订单、产能、现金流或同行数据交叉验证。
- `company_claim` 默认低于披露指标和第三方验证。
- `forecast` 和 `assumption` 只能支撑情景分析，不能伪装成事实。
- `interpretation` 必须写出替代解释或反证路径。
- `rumor_signal` 默认不得进入正式结论，除非升级为已核验来源。

## LLM-Native Use

LLM 在 Mira 中应优先用于：

- 从长文本中抽取 claim。
- 给每条 claim 分类。
- 标出公司口径、市场预期、Mira 推断和可核验事实的边界。
- 发现同一来源内部的事实、承诺、预测和观点混写。
- 在监控中比较新 claim 是否验证、削弱或替代旧 claim。

## Output Rule

研究输出中任何 durable conclusion 都应能回溯到 evidence log 中至少一条高权重 claim。若结论主要依赖 `company_claim`、`forecast`、`assumption`、`opinion`、`sentiment` 或 `rumor_signal`，必须降级置信度并写明刷新条件。
