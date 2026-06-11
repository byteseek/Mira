# Mira Start Here

这是一张给用户的入口卡：不知道怎么问时，从这里开始。

Mira 是 AI 投资研究系统，底层是一套投研协议；它不是自动荐股器、交易机器人或后台行情服务。你可以用一句话启动；信息给得越清楚，Mira 越少猜，证据路径和输出质量越稳定。

你负责问题、约束和最终判断；AI 模型负责扩展阅读、归纳和假设生成；Mira 负责把这些工作约束成可追踪、可刷新、可反驳的研究过程。

## 1. 一句话启动

适合先打开问题、快速判断方向。

```text
Mira, 看一下 NVDA
Mira, 研究一下 AAPL
Mira, 更新 CRWV
Mira, 做一份美股盘前简报
Mira, 做一份 AI 半导体周报
Mira, 分析 TSLA 最新财报
Mira, 这个估值方法靠谱吗
```

默认解释：

| 说法 | 默认深度 | Mira 会做什么 |
| --- | --- | --- |
| `看一下 X` | `quick_map` | 先路由，给核心判断、source notes、关键缺口和刷新触发条件。 |
| `研究一下 X` / `研究 X` | `standard` | 进入正式研究路径，除非路由选中更窄的财报、产业、宏观、ETF 或方法论路径。 |
| `更新 X` | `standard` | 聚焦增量证据、thesis impact 和是否需要升级完整研究。 |
| `日报/周报/盘前简报/收盘复盘` | `standard` | 进入 market briefing，输出市场快照、driver map、事件日历、source notes 和 research escalation queue。 |
| `深挖 X` / `完整研究 X` / `方法验证` / `PM review` | `deep_dive` | 用更完整证据路径和附加 artifact，但仍只加载有用材料。 |

## 2. 更好的问法

补四个字段就够：研究对象、真正问题、市场范围、时间边界。

```text
Mira, 研究一下 NVDA
我真正想判断的是：未来 2-4 个季度云厂 capex 是否还能支撑收入上修。
市场范围：美股
时间边界：截至今天
输出：先给 quick_map，判断是否值得升级成标准研究包。
```

另一个例子：

```text
Mira, 更新 AAPL 的 thesis
只看 2026-04-15 之后的新信息。
重点判断：最近财报和指引是否改变服务收入、iPhone 周期和估值前提。
输出：monitoring update，写清 must_refresh_if。
```

## 3. 完整任务卡

适合正式研究、可复核产物或需要保存的 thesis。

```text
Mira, 研究/更新/看一下/评估方法: <对象>
研究问题: <你真正想判断什么>
市场范围: <美股/A股/港股/全球/宏观区域>
时间边界: <日内/1-2个季度/未来1-2年/长期>
来源边界: <公开来源/本地文件/指定链接/已有 case>
输出深度: <quick_map / standard / deep_dive>
输出要求: <研究包/财报包/宏观 note/产业地图/只要结论摘要>
```

示例：

```text
Mira, 研究 CRWV
研究问题: 市场是不是高估了未来 GPU 云收入持续性？
市场范围: 美股
时间边界: 未来 2-8 个季度
来源边界: 公开财报、招股书、公司 IR、同业信息和市场数据
输出深度: standard
输出要求: research package，包含 evidence log、stale_after 和 must_refresh_if。
```

## 4. Help: 更多类型怎么问

| 任务类型 | 可以这样问 | 默认产出 |
| --- | --- | --- |
| 快速判断方向 | `Mira, 看一下 <ticker/company>` | `quick_map`、source notes、source gaps、refresh triggers |
| 市场日报/盘前简报 | `Mira, 做一份 <市场> 盘前简报/日报` | market snapshot、key moves、driver map、今日事件、research escalation queue |
| 市场周报/主题周报 | `Mira, 做一份 <市场/行业/主题> 周报` | week in review、主导变量、rotation、下周 watchpoints、thesis impact queue |
| 收盘复盘 | `Mira, 复盘今天 <市场> 收盘` | close wrap、move attribution、rotation、unexplained moves、next-session watchpoints |
| 股票首次研究 | `Mira, 研究一下 <ticker/company>` | research package、evidence log、case notes |
| 股票增量更新 | `Mira, 更新 <ticker/company> 的 thesis` | monitoring summary、thesis impact、升级判断 |
| 预期差判断 | `Mira, <ticker/company> 的预期差在哪？` | variant-perception 路由、consensus proxy、可证伪条件 |
| 买卖动作判断 | `Mira, 现在能不能买/卖 <ticker/company/asset>？` | marginal buyer/payoff bridge、price-in 判断、actionability risk-control、research-bound posture |
| 财报/指引 | `Mira, 分析 <ticker/company> 最新财报` | earnings analysis、financial snapshot、peer comparison、evidence log |
| 研报解读 | `Mira, 解读这篇 <ticker/company> 研报` | report readout、claim map、权限边界、独立核验和 thesis impact |
| 事件 delta | `Mira, 看 <ticker/company> 这次 <事件> 是否改变 thesis` | pre-event setup、actual vs expectation、event-delta、required research follow-up |
| SEC / 招股书 | `Mira, 拆一下 <ticker/company> 的 <10-K/10-Q/S-1>` | filing analysis、metric table、risk delta、accounting-quality check |
| 产业/供应链 | `Mira, 研究 <产业/技术/供应链概念>` | industry map、company map、stock research handoff |
| 宏观传导 | `Mira, 看 <宏观变量> 对 <资产/行业/股票> 的影响` | transmission chain、asset impact、what would change the view |
| ETF | `Mira, 看一下 <ETF/新发 ETF/主题 ETF>` | ETF discovery 或 listing analysis |
| 方法论评估 | `Mira, 这个方法靠谱吗: <方法/指标/框架>` | methodology card、适用范围、失效模式、trial/adopted 建议 |
| 单一持仓复盘 | `Mira, review 我的 <ticker/company> 仓位` | position review、证据强度、仓位语义、follow-up queue |
| 组合结构复盘 | `Mira, 看这个组合是不是暴露太集中` | portfolio-construction review、主题/因子/催化剂暴露 |
| 决策质量复盘 | `Mira, 复盘我当时对 <对象> 的判断质量` | decision-quality review、postmortem、methodology update candidate |

## 5. 需要注意的边界

- Mira 输出是研究辅助，不是投资建议、交易指令或自动下单。
- 如果你问“能不能买 / 卖 / 加 / 减 / 冲 / 追 / 抄底”，Mira 会先判断边际买家/卖家、边际收益来源、重定价触发器和 price-in 状态，再做 actionability risk-control gate；输出是研究边界、确认条件、失效条件和反向检验，不是交易命令。
- 如果你要仓位或组合结论，需要提供持仓、权重、mandate 和风险预算；否则只能输出 research-only 结论。
- 如果你提供本地文件、API 输出、vendor 数据或组合导出，Mira 会先走 ingestion layer，记录来源、授权、as-of 和计算边界。

## 6. Agent 启动规则

给 agent 使用时，默认流程是：

1. 用户空白启动、只说 `hi Mira`、`你好 Mira`、`Mira mode`，或问怎么开始时，先返回本文件的 Start Here 摘要。
2. 用户已经给出具体研究任务时，不要插入完整 onboarding；直接按任务路由，最多附一句 `可输入 Mira help 查看更多问法`。
3. 用户明确要求更新 Mira 本体时，运行 `scripts/mira_update.sh`。
4. `standard` / `deep_dive` 研究前运行 `scripts/check_updates.sh`（默认 local-first，24h remote TTL）只检查 freshness，不自动更新；`quick_map` / 看一下跳过。fetch 被拦就降级到 local refs 并说明，不为此提权。
5. 正式分析前先路由，再加载被路由选中的 loop、skill 和 template。
6. 输出时保留事实、推断、判断分层，并写清 `stale_after` 或 `must_refresh_if`。

更完整的 agent 执行规则见 [AGENT_QUICKSTART.md](AGENT_QUICKSTART.md)、[OPERATING_CONTRACT.md](OPERATING_CONTRACT.md) 和 [MIRA.md](MIRA.md)。
