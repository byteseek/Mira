# Mira

Agent-native investment research workspace for evidence-tracked, refreshable investment theses.

Mira 是一个面向 AI agent 和研究使用者的投资研究工作台。

如果你想用 Codex、Claude Code 或其他代码型 agent 直接引用本项目做股票、产业、ETF、财报或宏观经济分析，先读 [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md) 和 [AGENT_QUICKSTART.md](AGENT_QUICKSTART.md)。Mira 的唤醒词、身份边界和 memory contract 在 [MIRA.md](MIRA.md)，Codex 的项目规则在 [AGENTS.md](AGENTS.md)，Claude Code 的入口在 [CLAUDE.md](CLAUDE.md)。

它的目标不是生成一份孤立的股票报告，也不是把一次问答包装成研究结论，而是把多源材料组织成可追溯、可复核、可持续更新的投资判断。Mira 关注的是投资 thesis：这个判断基于什么证据、在什么时间点成立、哪些变量会证伪它、后续应该如何监控。

当前仓库是 `Mira` 的 research workspace，用来定义数据协议、分析能力、研究 loop、agent 职责、memory 规则和可复用的研究包模板。

## Disclaimer

This repository is for research workflow design, documentation, and historical examples only. It does not provide investment, legal, tax, accounting, or financial advice. Public case packages are stale after their stated cutoff or refresh boundary and should not be treated as live recommendations.

本仓库仅用于研究流程设计、文档化和历史案例展示，不构成投资、法律、税务、会计或财务建议。公开案例均有时间边界，超过其 `research_cutoff_date`、`analysis_cutoff_date`、`stale_after` 或刷新条件后应视为可能过期。

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
- 用 `claim classification` 区分事实、公司口径、承诺、指引、目标、预测、假设、观点、市场定价和弱信号。
- 用 `research package` 固化投资 memo、证据表和案例 notes。
- 用 `Thesis System` 把一次性报告升级成可维护的 thesis ledger、expectation map、event delta、decision log 和 postmortem。
- 用 [controlled vocabulary](data/controlled-vocabulary.md) 统一 thesis state、research action、setup type 和 position sizing token，避免不同 agent 产出漂移。
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
- 把 `存储`、`CPU`、`GPU`、`ABF`、`HBM`、`CPO`、`液冷`、`先进封装` 这类产业概念拆成产业链、供需瓶颈、利润池和候选标的。
- 按需监控已有 thesis 的新增信息，区分小更新、风险变化和完整重研触发。
- 维护机构级 `Thesis System`：当前 thesis、预期差、事件 delta、研究动作和复盘闭环。
- 在分析前执行 `framework routing`，识别当前主要定价变量。
- 在主框架外叠加 `overlay`，例如供应链、宏观、同业验证或后续扩展的渠道检查。
- 对预期差问题使用 `variant perception checklist`，明确市场共识、错价变量和证伪条件。
- 对进入正式结论的信息做 `claim classification`，避免把观点、承诺、预测、假设或价格反应误写成事实。
- 研究投资研究方法本身，把方法放入 `todo / trial / adopted / retired`。
- 把稳定结论写入 wiki-style `memory`，避免每轮研究从零开始。

## Quickstart

最短使用路径：

1. 检查本地仓库是否有 remote 更新：
   ```sh
   scripts/check_updates.sh
   ```
   如需脚本在发现更新时询问是否执行更新：
   ```sh
   scripts/check_updates.sh --prompt
   ```
   Mira 不应自动更新仓库；是否执行 `git pull --ff-only` 由用户决定。
2. 读 [AGENTS.md](AGENTS.md)，确认 `Mira Mode` 的触发规则和输出要求。
3. 读 [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md)，按 lazy-loading map 只加载当前任务需要的 loop、skill 和模板。
4. 选择任务类型：
   - 首次研究或 thesis 重建：走 [loops/research-loop.md](loops/research-loop.md)。
   - 已有 thesis 更新：走 [loops/monitoring-loop.md](loops/monitoring-loop.md)。
   - 方法论评估：走 [loops/methodology-research-loop.md](loops/methodology-research-loop.md)。
   - PM / 多 thesis 组合视角：走 [loops/portfolio-review-loop.md](loops/portfolio-review-loop.md)。
5. 先运行总路由：[loops/analysis-routing.md](loops/analysis-routing.md)。
6. 如果进入单票研究，再使用：
   - [skills/equity-research-core/references/thesis-horizon-routing.md](skills/equity-research-core/references/thesis-horizon-routing.md)
   - [skills/equity-research-core/references/framework-routing.md](skills/equity-research-core/references/framework-routing.md)
   - [skills/equity-research-core/references/overlay-routing.md](skills/equity-research-core/references/overlay-routing.md)
7. 从 [templates/](templates/) 复制对应研究包结构，输出 memo、evidence log 和 notes。
8. 用 [templates/delivery-checklist.md](templates/delivery-checklist.md) 做交付前自检。

当前推荐先看两个完整样板：

- [AAPL research package](cases/aapl-2026-04/README.md)：展示标准单票 golden case，包括 memo、canonical evidence log、expectation map、thesis ledger、decision log 和 actionability bridge。
- [NVTS earnings package](cases/nvts-2026-05/README.md)：展示财报事件、同行验证、canonical evidence log、expectation map 和 actionability bridge。

PM 视角总览见 [memory/research/INDEX.md](memory/research/INDEX.md)，组合层模板见 [templates/portfolio-system/portfolio-register.csv](templates/portfolio-system/portfolio-register.csv)。

典型 prompt：

```text
Mira, 研究 AAPL。市场范围 US，时间边界截至 2026-04-14。
请先做 analysis routing、thesis horizon routing、framework selection 和 overlay selection，
再输出 research package，并明确 stale_after 与 must_refresh_if。
```

本地开源检查：

```sh
python3 scripts/validate_repo.py
```

SEC supplement 或 SEC filing deep dive 产物可以额外校验：

```sh
python3 scripts/validate_sec_filing_package.py path/to/sec-supplement-source-note.csv
python3 scripts/validate_sec_filing_package.py path/to/sec-filing-package-dir
```

remote 更新检查：

```sh
scripts/check_updates.sh
```

## 核心原则

- 研究过程必须可追溯到来源，不接受无来源结论。
- 事实、推断、判断必须分层书写。
- 每条核心信息必须说明它是事实、公司口径、承诺、指引、目标、预测、假设、观点、市场定价还是弱信号。
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

## Thesis System

工程说明：[architecture/thesis-system.md](architecture/thesis-system.md)

`Thesis System` 是 Mira 的机构级研究协议层。它把研究链路固定为：

`source -> claim -> expectation -> thesis -> event delta -> decision log -> postmortem`

核心对象：

- `thesis-ledger`：当前 thesis、supporting claims、关键假设、证伪条件和状态变化。
- `expectation-map`：市场共识代理、Mira 分歧、已 price-in 部分和下一验证点。
- `event-delta`：财报、宏观、产品、监管或同业事件前后的预期差和 thesis impact。
- `decision-log`：研究动作记录，例如 watch、upgrade_watch、no_action；不是交易指令。
- `controlled-vocabulary`：状态和动作 token 的单一事实源。
- `postmortem`：复盘判断错在数据、推理、时间、市场定价还是执行约束。
- `actionability-bridge`：把 thesis 连接到研究动作、催化剂日历、下行路径和定性仓位含义，但不输出自动交易指令。
- `outcome-scorecard`：记录原判断、结果窗口、实现路径和 confidence 校准。

文档版应用骨架见 [architecture/mira-app-skeleton.md](architecture/mira-app-skeleton.md)。V1 不新增数据库、UI 或自动交易能力，Markdown + CSV 是正式接口。

## 五类 Loop

Mira 当前有五类核心 loop。文件名保持工程稳定，文档展示名采用更清楚的中文定位。

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

### Thesis 更新 loop

工程文件：[loops/thesis-update-loop.md](loops/thesis-update-loop.md)

`Thesis 更新 loop` 用于已有 thesis 的状态变化、预期差更新、研究动作记录和复盘入口。它不是完整重研；只有当新增 evidence 改变核心前提时，才升级回投资分析 loop。

### Event Delta loop

工程文件：[loops/event-delta-loop.md](loops/event-delta-loop.md)

`Event Delta loop` 用于财报、宏观、产品、监管、同业 read-through 等事件前后对比。它要求先写 pre-event setup，再判断实际披露相对预期改变了哪个变量，以及是否影响 thesis state。

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

## 产业概念分析

[skills/industry-concept-analysis/](skills/industry-concept-analysis/) 用于在单票研究前，把类似 `存储`、`CPU`、`GPU`、`ABF`、`HBM`、`CPO`、`液冷`、`先进封装` 这样的概念拆成：

- 一页版产业地图
- 概念边界
- 产业链地图
- 上下游供给和需求公司
- 定价机制
- 放量机制
- 紧供需平衡和高溢价环节
- 利润池排序
- 候选标的和单票研究交接

阅读顺序上，产业概念报告必须先给 `One-Page Industry Map`，把一句话定义、当前判断、紧缺环节、利润池、股票代理、核心公式、关键争论、跟踪指标和证伪条件放在最前面。完整产业链和证据日志放在后面作为底稿。

它的输出是 `industry-analysis-package`，用于先建立产业认知和公司池，再把重点标的交给 `equity-research-core`。

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

### Thesis System Package

持续跟踪对象使用：

- `thesis-ledger.md`
- `expectation-map.csv`
- `event-delta.md`
- `decision-log.csv`
- `postmortem.md`
- `actionability-bridge.md`
- `thesis-scorecard.csv`

Thesis 模板见 [templates/thesis-system/](templates/thesis-system/)，行动桥模板见 [templates/actionability-system/](templates/actionability-system/)，结果校准模板见 [templates/outcome-review/](templates/outcome-review/)。

## Validation

正式 case 的 evidence log 必须使用 [data/evidence-log-schema.md](data/evidence-log-schema.md)。

运行：

```text
python3 scripts/validate_repo.py cases/<case-id>
```

迁移历史 case 时可先运行：

```text
python3 scripts/validate_repo.py --report-only
```

当前 schema 漂移基线见 [reports/validation/evidence-log-2026-05-29.md](reports/validation/evidence-log-2026-05-29.md)。

### Long-Term Workflow Release QA

长期方法论外发前必须通过 release gate，而不是只依赖文档判断。当前候选包见 [cases/long-term-workflow-validation-2026-05-30/](cases/long-term-workflow-validation-2026-05-30/)。

运行：

```text
python3 scripts/run_long_term_release_checks.py
```

当前总 QA 包括 10 个 case 校验、28 个 release-control CSV shape check、G01 external method-source scan 校验、G06 reviewer packet/assignment tracker 校验、G06 reviewer candidate screen 校验、G06 reviewer selection rubric 校验、G06 reviewer independence screen 校验、G06 dispatch packet audit、G06 dispatch readiness checklist、external release action queue 校验、G04 trigger/event-watch/later-event candidate/execution tracker 校验、G04 default packet dry run、G04 four-case packet matrix、G06 packet dry run、institutional bundle 校验、public release freshness 校验、release verification command manifest 校验、go/no-go evidence coverage 校验、final release cutover 校验、objective readiness 校验、goal completion audit 和最终外发负向门禁。

关键 release 控制项：

- `g01-external-method-source-audit.csv` + `scripts/validate_g01_external_method_scan.py`：确认公开亚洲/中文 practitioner 来源已经补强，但仍只是 `partial_pass_improved`，需要 G06 reviewer 接受。
- `g04-follow-through-execution-tracker.csv` + `scripts/validate_follow_through_execution_tracker.py`：确认 follow-through 已准备执行但仍等待后续事件，并交叉检查 trigger tracker/event calendar，不能被误判为完成。
- `g04-follow-through-event-watch-calendar.csv` + `scripts/validate_g04_event_watch_calendar.py`：确认后续事件观察日历存在，且 scheduled/monitored event 不会被误判为已完成 G04。
- `g04-later-event-candidate-screen.csv` + `scripts/validate_g04_later_event_candidate_screen.py`：确认后续事件必须先通过 post-cutoff 日期、官方来源、materiality 和 execution-state 检查，才能进入 refresh。
- `scripts/validate_follow_through_refresh.py`：确认未来 G04 refresh 必须所有 qualification rows 为 yes，original_memo_date 匹配 cutoff，new event source 日期晚于 cutoff，stale_after 晚于 refresh_date，恰好选择一个 approved result label，refresh source_id 出现在 updated evidence log 的 later-event 行里，且 G04 intake requirements 完整。
- `scripts/validate_follow_through_packet_matrix.py`：确认 ETN、VRT、CRM、LLY 四个 live case 都能 dry-run 导出 G04 execution packet。
- `trial-theme-matrix.csv` + `scripts/validate_trial_theme_matrix.py`：确认近期热门方向选择覆盖 7 个主题，且每个主题都有 linked case、evidence log 和 source_id 可追踪。
- `public-workflow-pack/` + `scripts/validate_public_workflow_pack.py`：确认 public pack 的 README、workflow、fill guide、checklist、template inventory 和 source appendix 对 11 个 overlay、10 个案例/主题 source trail 与 release boundary 保持一致。
- `scripts/validate_public_release_freshness.py --as-of 2026-05-30`：确认 15 个公开/外审材料有未过期的 `stale_after` 和可观察 `must_refresh_if`，并确认 4 个模板保留刷新字段，防止过期材料被继续外发。
- `scripts/validate_validation_case_set.py`：非递归执行 10 个 case 的 repo validation，供 objective/goal audit 作为可执行证据使用。
- `g06-reviewer-assignment-tracker.csv` + `scripts/validate_external_review_assignment_tracker.py`：确认外部 reviewer 已准备分配但尚未完成，并交叉检查 independence screen 的 pending reviewer rows，不能被内部模拟替代。
- `g06-reviewer-candidate-screen.csv` + `scripts/validate_g06_reviewer_candidate_screen.py`：确认候选 reviewer 筛选是候选人级别、可审计的，且在未命名 reviewer 前不会伪装成 G06 完成。
- `g06-reviewer-independence-screen.csv` + `scripts/validate_g06_reviewer_independence_screen.py`：确认 reviewer 独立性、利益冲突、能力和 source-boundary 筛选标准已准备，但仍不命名 reviewer、不清 G06。
- `scripts/validate_external_review_return.py`：确认未来 reviewer return 必须绑定 assignment tracker 和 independence screen，且在 scorecard 和 results memo 两处明确通过 G04 readiness / false-completion control，severity/impact 必须合法，P1 修复必须有 `owner:`/`fix:`，results memo Findings 表的 P0/P1 行数必须匹配 summary/scorecard，reviewer/date 必须一致，intake 必须完整，且 memo summary 必须匹配 scorecard，不能用备忘录改写评审事实。
- `scripts/validate_external_review_dispatch_packet.py`：临时真实导出 G06 reviewer packet，确认 28 个 send items 可派发、internal rows 未外发且仍不清 G06。
- `g06-dispatch-readiness-checklist.csv` + `scripts/validate_g06_dispatch_readiness.py`：确认派发前 9 项控制已通过，实际 reviewer assignment/return 仍是外部 pending blocker。
- `goal-completion-audit.csv` + `scripts/validate_goal_completion_audit.py`：把原始目标映射到 10 个完成证据，逐行执行非递归 `verification_command`，额外检查 institutional packet dry-run 的 38 个 required export paths，并强制 G04/G06/final release 未完成时 `goal_complete: false`。
- `release-verification-command-manifest.csv` + `scripts/validate_release_verification_command_manifest.py`：把最终包的复验命令、当前期望退出码和外发阻断命令做成机器可读清单，防止复验逻辑只存在于 runbook 文本里。
- `scripts/validate_go_no_go_evidence_coverage.py`：确认 11 个外发必需 release gate 都映射到 final go/no-go 的 15 个证据行，并且 cutover validator 有对应拒绝逻辑，防止新增 gate 后最后签发模板漏检。
- `scripts/validate_final_release_cutover.py`：确认 final cutover 仍未 ready，且 go/no-go template 或带 placeholder/pending evidence 的 dated memo 不会被误当成已签署 go memo。
- `scripts/build_institutional_release_packet.py`：在 `python3 scripts/validate_long_term_release.py --require-external-ready` 失败时拒绝导出最终机构同事 release packet，同时 dry-run 检查 38 个 required export paths。

### Claim Classification

Mira 的 evidence log 不只记录来源，还记录每条被使用信息的性质。

`claim_type` 规则见 [data/claim-taxonomy.md](data/claim-taxonomy.md)。核心分类包括：

- `fact`
- `reported_metric`
- `company_claim`
- `guidance`
- `target`
- `commitment`
- `forecast`
- `assumption`
- `interpretation`
- `opinion`
- `market_pricing`
- `sentiment`
- `rumor_signal`
- `derived_calculation`

这是一层 LLM-native research workflow：LLM 负责把长文本拆成 claim、分类、标注 speaker 和 verification status；研究者负责复核关键 claim 是否足以支撑 memo 结论。

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

### Industry Analysis Package

产业概念研究先输出 `industry-analysis-package`：

- `industry-map`：一页版产业地图 + 完整 diligence 底稿。
- `company-map`：产业链位置、暴露度、定价权、放量可见度、股票代理质量。
- `evidence-log`：概念边界、供需、定价、放量和公司映射的来源记录。

模板见 [templates/industry-analysis-package/](templates/industry-analysis-package/)。

### Methodology Artifacts

ETF 上市事件可先输出一个轻量 `etf-listing-analysis package`：

- `etf-listing-analysis`
- `evidence-log`

当 ETF 分析指向具体股票、行业链条或资产类别机会时，再进入标准 `research package` 或对应单票研究。

ETF 新发发现可先输出一个轻量 `etf-listing-discovery package`：

- `new-etf-watchlist`
- `discovery-log`
- `evidence-log`

高优先级候选再进入 `etf-listing-analysis package`。

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
- 来源类别 taxonomy 和覆盖矩阵
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
- `industry-concept-analysis`：产业概念分析 skill，负责概念边界、产业链、供需/定价/放量机制、利润池和候选标的。
- `earnings-report-analysis`：财报专项 skill，负责财报质量、同业对比和 thesis impact。
- `sec-filing-analysis`：SEC 补充核验与专项 filing deep dive skill，负责 CIK/accession/form/tag provenance、filing metric extraction、risk delta 和 accounting-quality checks。
- `macro-economic-analysis`：宏观专项 skill，负责宏观变量、金融条件和资产定价链分析。
- `etf-listing-discovery`：ETF 新发发现 skill，负责结构化搜索新上市、即将上市、申请中或刚宣布的 ETF。
- `etf-listing-analysis`：ETF 上市分析 skill，负责拆解发行意图、暴露地图、管理/权重机制和上市后跟踪。

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
- [cases/abf-2026-05/](cases/abf-2026-05/)：产业概念分析包示例。
- [cases/cohr-2026-05/](cases/cohr-2026-05/)：财报事件分析包示例。
- [cases/etf-discovery-2026-05-09/](cases/etf-discovery-2026-05-09/)：ETF 新发发现示例。
- [cases/etf-listing-analysis-2026-05-09/](cases/etf-listing-analysis-2026-05-09/)：BUYB / EUV / JOUL ETF 上市分析示例。

案例阅读顺序和使用边界见 [examples/README.md](examples/README.md)。所有公开案例都是 historical examples，不构成投资建议。

## Open Source Notes

- License: [Apache-2.0](LICENSE)
- Contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md)
- Security policy: [SECURITY.md](SECURITY.md)
- Data/source policy: [DATA_POLICY.md](DATA_POLICY.md)

开源贡献的最低要求：

- 真实案例必须有 `evidence-log.csv`。
- 真实案例必须写明时间边界和刷新条件。
- 真实标的分析必须标注 `not_investment_advice: true` 或等价免责声明。
- 不提交 API key、cookie、券商账户数据、付费研报全文、私有纪要或不可再分发数据。
- 结论证据不足时必须降级，不把观点写成事实。

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

### 分析产业概念

1. 用 [skills/industry-concept-analysis/](skills/industry-concept-analysis/) 明确概念、市场范围、时间边界和研究重点。
2. 先输出 `One-Page Industry Map`，快速回答哪里紧、谁受益、买什么代理、什么会错。
3. 再输出完整产业链、供需、定价、放量、利润池、公司映射和证据日志。
4. 把候选标的交给 [skills/equity-research-core/](skills/equity-research-core/) 做单票研究，必要时启用 `supply-chain` overlay。

### 分析宏观驱动

1. 用 [skills/macro-economic-analysis/](skills/macro-economic-analysis/) 明确宏观问题、资产范围、时间窗口和目标变量。
2. 判断宏观变量是否只是背景，还是会改变收入、利润率、贴现率、风险溢价、融资条件、仓位或催化剂。
3. 如果宏观变量会改变定价链，在投资分析 loop 中启用 `macro` overlay。
4. 将稳定方法沉淀到 `memory/methodologies/`，并通过真实案例继续验证。

### 发现和分析新 ETF

1. 用 [skills/etf-listing-discovery/](skills/etf-listing-discovery/) 从交易所、发行人、监管文件、ETF 行业媒体和市场数据中生成候选 watchlist。
2. 输出 [templates/etf-listing-discovery-package/](templates/etf-listing-discovery-package/) 对应的发现包。
3. 对高优先级候选，用 [skills/etf-listing-analysis/](skills/etf-listing-analysis/) 拆解发行意图、结构与可达性、持仓暴露地图、管理/权重机制和同类产品语境。
4. 输出 [templates/etf-listing-analysis-package/](templates/etf-listing-analysis-package/) 对应的上市分析包。
5. 若 ETF 分析指向具体股票、行业链条或资产类别机会，再进入标准投资分析 loop。

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
│   ├── abf-2026-05/
│   ├── cohr-2026-05/
│   ├── etf-discovery-2026-05-09/
│   └── etf-listing-analysis-2026-05-09/
├── data/
│   ├── methodology-source-policy.md
│   ├── public-source-targets.md
│   ├── source-class-map.csv
│   ├── source-coverage-matrix.csv
│   ├── source-policy.md
│   ├── source-registry.csv
│   ├── source-schema.md
│   ├── source-taxonomy.md
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
│   ├── etf-listing-analysis/
│   ├── etf-listing-discovery/
│   ├── industry-concept-analysis/
│   ├── macro-economic-analysis/
│   └── equity-research-core/
└── templates/
    ├── earnings-analysis-package/
    ├── etf-listing-analysis-package/
    ├── etf-listing-discovery-package/
    ├── industry-analysis-package/
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
- 当前版本包含一个单票深度案例、一个财报事件案例和一个产业概念案例，暂不做完整主题篮子。
- 当前版本的 memory 只沉淀慢变量，不记录全部日常噪音。
- 当前版本先支持 `supply-chain` 和 `macro` overlay，并支持独立的 `industry-concept-analysis`，不把专题研究路径无限扩张。
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
- 用更多真实案例验证 `industry-concept-analysis`，例如 GPU、HBM、存储、CPO。
- 增加方法论评分与案例验证挂钩。
- 用真实案例验证 `llm-claim-classification`，通过后再从 `trial` 升级到 `adopted`。
- 增加方法论 review log 和长期 follow-through 记录。
- 增加 methodology query expansion 和搜索自动化。
- 拆分 `equity-research-core` 为独立主题 skills。
- 把 `research-orchestrator` 拆成多个 monitors 和专题 agents。
- 给 A 股补更细的本地数据源注册表与公开网页 target set。
- 增加第二个案例，例如 A 股龙头或周期股。
- 给 monitoring loop 增加固定日志模板。
