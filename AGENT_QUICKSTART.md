# Mira Agent Quickstart

这份文档给使用 Codex、Claude Code 或其他代码型 agent 的研究者一个执行入口：如何引用本项目做股票、产业、ETF、财报和宏观经济分析。

用户侧的统一入口卡是 [START_HERE.md](START_HERE.md)。当用户问“怎么用 Mira / Mira help / start here / Mira 能做什么”，或只说 `hi Mira` / `你好 Mira` / `Mira mode` 时，优先返回 `START_HERE.md` 的分层入口和 Help 矩阵；本文件继续维护 agent 执行规则、路由、输出位置和证据纪律。

Mira 不是一个自动荐股器，也不是后台行情机器人。它是一套可复核的投研工作流：先路由研究类型，再选择框架和证据路径，最后输出带来源链、时效边界和刷新条件的研究包。

Mira 也是本项目的唤醒词。完整定义见 [MIRA.md](MIRA.md)：Mira 是有名字的研究协议，不是会替代证据判断的虚构人格。

## 1. Agent 入口

### 更新和启动

| 场景 | 命令 | 说明 |
| --- | --- | --- |
| 用户明确要更新 Mira 本体 | `scripts/mira_update.sh` | 安全更新入口；会 fetch、拒绝 dirty/ahead/diverged，并在成功后校验仓库。 |
| 开始正式研究前检查 freshness | `scripts/check_updates.sh` | 只报告是否落后 remote，不自动更新。 |
| 离线或权限受限时只比较本地 remote refs | `scripts/check_updates.sh --no-fetch` | 不联网，结果可能基于旧 refs。 |
| 想让检查脚本在发现落后时询问更新 | `scripts/check_updates.sh --prompt` | 只适合有 upstream 的普通分支。 |

原则：用户已经明确说“更新 Mira”时，不要先跑 freshness check；直接跑 `scripts/mira_update.sh`。研究任务开始前才跑 `scripts/check_updates.sh`。

### 用户入口

面向用户的 prompt 不在本文件重复维护，统一见 [START_HERE.md](START_HERE.md)。短入口、完整任务卡、Help 类型矩阵和边界说明都以该文件为准。

### Codex

在 Codex 中打开本仓库后，根目录的 [AGENTS.md](AGENTS.md) 会提供默认项目规则，[MIRA.md](MIRA.md) 会定义唤醒词和 memory 边界。用户入口提示统一从 [START_HERE.md](START_HERE.md) 摘要。

用户需要示例时，返回 [START_HERE.md](START_HERE.md) 的摘要，不从本文件复制 prompt。

### Claude Code

Claude Code 默认读取根目录 [CLAUDE.md](CLAUDE.md)。该文件会要求 Claude 同步遵守 [AGENTS.md](AGENTS.md)、[MIRA.md](MIRA.md) 和本 quickstart。

## 2. 最小任务卡

完整用户任务卡的 canonical 版本见 [START_HERE.md](START_HERE.md)。缺字段时，agent 应该先做合理补全或提出最少问题；不要在本文件维护第二份任务卡。

## 3. 路由规则

正式分析前必须先运行 [loops/analysis-routing.md](loops/analysis-routing.md)，不要直接套股票模板。

路由第一步是 Step 0 意图入口：先把复合 prompt 拆成 `primary_intent` / `secondary_intents`，显式声明本轮运行假设，并按 `depth_mode` 给出可缩放的路由卡（quick_map 只需一行假设条）。如果问题接近“能不能买 / 加 / 减 / 冲 / 抄底 / 目标价到了还能买”或 position / portfolio，必须同时跑 Step 0.5 decision pressure gate：标注 `decision_pressure` 与 `framing_risk`（锚问题不锚人、瞬时不存储），压力为 medium/high 时给一个反向检验。选定 depth 后，用 Step 3.3 校验信息价值和可知性；主导变量不可知时输出 `irreducible_uncertainty`，不要强行深挖。

如果 context 紧张，先读 [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md)。它给出最短 loading map：每一步只读当前需要的 loop、skill 或模板。

先确定 `depth_mode`，避免快看被完整模板拖慢，也避免正式研究缺少证据：

| depth_mode | 默认场景 | 输出边界 |
| --- | --- | --- |
| `quick_map` | “看一下”、早期 triage、来源边界不完整 | routing card、核心判断、source notes、source gaps、refresh triggers、1 个 light follow-up 或显式 waiver |
| `standard` | “研究 X”、正式 case、普通财报或 monitoring update | routed package 的必需文件 |
| `deep_dive` | “深挖”、长期 thesis、复杂估值、SEC 深拆、PM / 方法论复核 | 完整 package + 被 gate 触发的附加 artifact |

显式输出哪些字段由 [data/output-surface-matrix.md](data/output-surface-matrix.md) 控制。原则是：短答可以少露字段，但不能少做证据、刷新条件、follow-up 和触发式 gate 的内部检查。Mira 只保留 `quick_map` / `standard` / `deep_dive` 三个输出 surface；`quick_answer` 只是 `interaction_mode`，表示答案要直接、短，但仍渲染到某个 depth surface。

注意 `interaction_mode`（答案形状，Step 0）和 `depth_mode`（研究力度）是两个轴，别因为都带 “quick” 就混用：`quick_answer + quick_map`（看一下方向，浅研究一句话）、`quick_answer + deep_dive`（只要一句结论，但问题需要真估值才答得诚实）、`routed_research + quick_map`（triage 但仍出结构化卡）。组合样例见 [examples/routing-examples.md](examples/routing-examples.md)。

| 用户意图 | 默认路由 | 输出 |
| --- | --- | --- |
| 首次研究或重建 thesis | [loops/research-loop.md](loops/research-loop.md) | `investment-memo.md`, `case-notes.md`, `evidence-log.csv` |
| 更新已有 thesis | [loops/monitoring-loop.md](loops/monitoring-loop.md) | monitor summary, impact assessment, escalation decision |
| 更新 thesis object / 看预期差 / 复盘判断 | [loops/thesis-update-loop.md](loops/thesis-update-loop.md) | thesis-ledger, expectation-map, decision-log, postmortem |
| 事件前后 delta | [loops/event-delta-loop.md](loops/event-delta-loop.md) | event-delta, expectation map update, thesis impact |
| 财报、业绩会、指引 | [skills/earnings-report-analysis/SKILL.md](skills/earnings-report-analysis/SKILL.md) | earnings package |
| SEC 补充核验 | [skills/sec-filing-analysis/SKILL.md](skills/sec-filing-analysis/SKILL.md) | `sec-supplement-source-note.csv` + active case updates |
| SEC 文件专项拆解 | [skills/sec-filing-analysis/SKILL.md](skills/sec-filing-analysis/SKILL.md) | SEC filing analysis package |
| 多 thesis / PM 研究 book 视角 | [loops/portfolio-review-loop.md](loops/portfolio-review-loop.md) | thesis register, exposure notes, follow-up queue |
| 单一真实头寸复盘 | [loops/position-review-loop.md](loops/position-review-loop.md) | position review, sizing context, required follow-up |
| 真实组合结构复盘 | [loops/portfolio-construction-review-loop.md](loops/portfolio-construction-review-loop.md) | portfolio exposure review, duplicate-bet notes, position-review queue |
| 决策质量复盘 | [loops/decision-quality-review-loop.md](loops/decision-quality-review-loop.md) | decision-quality review, postmortem, methodology update candidate |
| 单一股票 | [skills/equity-research-core/SKILL.md](skills/equity-research-core/SKILL.md) | research package |
| 产业、技术、供应链概念 | [skills/industry-concept-analysis/SKILL.md](skills/industry-concept-analysis/SKILL.md) | industry package |
| 宏观、利率、通胀、美元、信用、流动性 | [skills/macro-economic-analysis/SKILL.md](skills/macro-economic-analysis/SKILL.md) | macro note 或 macro overlay |
| ETF 新发或上市结构 | `skills/etf-listing-*` | ETF discovery / listing package |
| 研究方法是否靠谱 | [loops/methodology-research-loop.md](loops/methodology-research-loop.md) | methodology artifacts |

如果路由进入单票研究，还必须继续运行：

- [skills/equity-research-core/references/thesis-horizon-routing.md](skills/equity-research-core/references/thesis-horizon-routing.md)
- [skills/equity-research-core/references/framework-routing.md](skills/equity-research-core/references/framework-routing.md)
- [skills/equity-research-core/references/overlay-routing.md](skills/equity-research-core/references/overlay-routing.md)，如果专题证据路径有增量价值

## 4. 用户 prompt 源头

用户可见 prompt、分角色入口和 Help 矩阵统一维护在 [START_HERE.md](START_HERE.md)。本 quickstart 不维护第二份 prompt 菜单；需要选择执行 loop 或 artifact 时，使用上面的路由表和下面的输出位置。

## 5. 输出位置

新研究建议放到 [cases/](cases)：

```text
cases/<object>-<YYYY-MM>/
```

常见输出结构：

```text
cases/<ticker>-<YYYY-MM>/
├── README.md
├── investment-memo.md
├── case-notes.md
└── evidence-log.csv
```

财报事件：

```text
cases/<ticker>-<YYYY-MM>/
├── README.md
├── earnings-analysis.md
├── event-delta.md
├── financial-snapshot.csv
├── peer-comparison.csv
└── evidence-log.csv
```

用户私有观点和工作视图默认位置：

```text
private/views/view-register.csv
private/research/<OBJECT>/
├── working-view.md
├── thesis-ledger.md
└── expectation-map.csv
```

`private/` 已被 gitignore，用于用户私有状态，不随 Mira 本体更新提交。模板见 [templates/private-state/](templates/private-state)，执行规则见 [loops/view-continuity-loop.md](loops/view-continuity-loop.md)。

Thesis System 产品样例或公共对象：

```text
memory/research/<OBJECT>/
├── thesis-ledger.md
├── expectation-map.csv
├── decision-log.csv
└── postmortem.md
```

决策质量复盘模板：

```text
templates/outcome-review/decision-quality-review.md
```

PM / 组合研究对象：

```text
memory/research/INDEX.md
templates/portfolio-system/portfolio-register.csv
templates/portfolio-system/position-register.csv
templates/portfolio-system/position-review.md
templates/portfolio-system/portfolio-construction-review.md
templates/portfolio-system/portfolio-exposure-review.csv
```

产业概念：

```text
cases/<concept>-<YYYY-MM>/
├── README.md
├── industry-map.md
├── company-map.csv
└── evidence-log.csv
```

模板在 [templates/](templates)。

## 5.1 完整样板

优先参考：

- [cases/aapl-2026-04/](cases/aapl-2026-04/)：标准单票 research package，包含 `investment-memo.md`、canonical `evidence-log.csv`、`expectation-map.csv` 和 `actionability-bridge.md`。
- [cases/aapl-2026-04/](cases/aapl-2026-04/) 也是 golden case：case 包内放了 `thesis-ledger.md` 和 `decision-log.csv`，用于 agent few-shot。
- [cases/nvts-2026-05/](cases/nvts-2026-05/)：财报事件样板，包含 earnings package、同行验证、canonical `evidence-log.csv`、`expectation-map.csv` 和 `actionability-bridge.md`。

PM / 组合研究视角的产品样例可参考 [memory/research/INDEX.md](memory/research/INDEX.md)。用户私有组合、持仓和观点默认使用 `private/portfolio/` 与 `private/views/view-register.csv`。

交付前用 [templates/delivery-checklist.md](templates/delivery-checklist.md) 做自检。

状态和动作字段必须使用 [data/controlled-vocabulary.md](data/controlled-vocabulary.md)。如果需要更细解释，写到 `basis`、`notes`、`risk` 或正文，不要发明新 token。

### 强习惯三件套

每次正式研究输出收尾前，先做一个很短的最终门槛检查：

1. **证据强度**：事实、推断、判断是否分层；耐久结论是否能追到 evidence log 或明确 source note。
2. **刷新条件**：是否写出 `stale_after`、`must_refresh_if` 或等价刷新条件。
3. **渐进反问**：是否写出 `followup_prompt_mode` 和 1-3 个 route-bound、object-specific follow-up；如果没有，是否显式写 `followup_prompt_mode=none` 和具体 waiver reason。

不要把 progressive follow-up 当成可选闲聊。它和刷新条件一样，是防止研究输出停在不可升级状态的交付字段；`quick_map` 默认至少给 1 个 light follow-up，除非用户明确不要反问、任务是机械更新/格式转换，或下一步已经唯一确定。

用 [data/output-surface-matrix.md](data/output-surface-matrix.md) 判断这些强习惯应该是 `internal_check`、`brief_visible` 还是 `full_visible`。强习惯不能被省略，但不必在每个短答里展开成完整表格。

## 6. 证据和结论规则

Mira 输出里必须分开写：

- `facts`: 已核验事实、披露数据、官方数据或可复核市场数据。
- `inferences`: 基于事实链推出的解释。
- `judgments`: 投资判断、权重、概率和风险取舍。

所有耐久结论必须有来源链。若来源弱，只能写成弱信号或待验证假设，不能写成结论。

每份正式输出必须包含至少一个刷新条件：

- `stale_after`: 这份判断在什么日期或事件后默认过期。
- `must_refresh_if`: 哪些信息出现时必须重做或更新。
- `kill_criteria`: 哪些证据会证伪主要 thesis。

每份正式输出也必须包含渐进反问：

- `followup_prompt_mode`: `light` / `standard` / `decision_grade` / `none`。
- route-bound follow-up: 问题要连接当前 route、对象、证据缺口、readiness 或下一层 loop。
- `followup_waiver_reason`: 只有在不提 follow-up 时才需要，且必须具体。

## 7. 拟人化和记忆边界

可以把 `Mira` 当成自然调用入口，例如“`Mira, 更新 NVDA`”。但 Mira 的核心不是人格，而是投研协议。

允许记住：

- 稳定的用户偏好，例如市场范围、语言、输出深度、关注行业。
- 经过案例验证的方法论。
- 有来源、有日期、有刷新条件的研究结论。

不允许记住：

- 没有来源的市场观点。
- 一次性闲聊或短期情绪。
- 会影响证据判断的主观偏好，例如默认看多或默认看空。
- 未验证却被写成长期事实的假设。

如果需要写入长期记忆，先按 [memory/MEMORY-RULES.md](memory/MEMORY-RULES.md) 和 [MIRA.md](MIRA.md) 检查。

## 8. 快速检查清单

交付前，agent 应检查：

- 是否记录 `task_mode`, `research_object`, `market_scope`, `time_boundary`。
- 是否完成总路由，而不是直接套模板。
- 是否先做 Step 0 意图入口：拆分复合意图、声明运行假设、按 depth 给出路由卡。
- 若问题涉及 actionability / position / portfolio，是否输出 `decision_pressure`，压力高时是否给 disconfirmation。
- 是否做了信息价值 / 可知性判断；主导变量不可知时是否诚实输出 `irreducible_uncertainty`，而非强行深挖。
- 若使用新文件、API、vendor export 或 portfolio/risk 数据，是否先走 ingestion layer 并记录权限、as-of、field mapping 和 evidence/calculation 映射。
- 正式判断是否带 `judgment_confidence`、`confidence_basis` 和 `reversal_condition`。
- 同一会话内 carryover 是否只沿用范围 / 时间 / 对象等白名单字段，未把偏误读数当长期偏好。
- 是否遵守 [MIRA.md](MIRA.md) 的唤醒词、人格边界和 memory 规则。
- 单票研究是否写明 `horizon_bucket`, `selected_framework`, `selected_overlays`。
- 若维护已有 thesis，是否更新或明确 waived `thesis-ledger`、`expectation-map` 和 state change。
- 若处理事件，是否写出 `event-delta`，而不是只做新闻摘要。
- 事实、推断和判断是否分层。
- 核心结论是否能追到 evidence log 或明确 source note。
- 是否说明 `stale_after`、`must_refresh_if` 或等价刷新条件。
- 是否说明 `followup_prompt_mode`，并给出 route-bound、object-specific follow-up；若没有，是否写明具体 waiver reason。
- 弱证据是否被降级，没有被写成确定结论。

## 9. Repo Validation

新增或更新正式 case 后，运行：

```text
python3 scripts/validate_repo.py cases/<case-id>
```

迁移历史 case 时可以先用 report-only 模式查看问题：

```text
python3 scripts/validate_repo.py --report-only
```

当前 canonical evidence schema 见 [data/evidence-log-schema.md](data/evidence-log-schema.md)。新的 `evidence-log.csv` 必须是 claim-level 表，不再允许把 source registry 表头直接放入 evidence log。

SEC supplement 或 SEC filing deep dive 还可以额外跑：

```sh
python3 scripts/validate_sec_filing_package.py templates/sec-supplement-source-note.csv
python3 scripts/validate_sec_filing_package.py templates/sec-filing-analysis-package
```

上面的脚本校验的是**语法**（schema、词表、路由卡 token）。要校验**行为**——模型在真实回答里是否真的做了契约要求的事（决策压力下的反向检验、弱证据降级、不可知时的诚实终态、无持仓不给仓位），跑行为级 eval：

`examples/routing-json-examples.md` 中的 JSON code block 也会被
`scripts/validate_repo.py` 按 `schemas/routing.schema.json` 校验；更新 routing
示例时不要只改可见 markdown 卡片。

```sh
python3 scripts/score_behavior_eval.py --transcripts evals/transcripts
```

它把 [templates/delivery-checklist.md](templates/delivery-checklist.md) 的语义纪律变成对模型输出的可打分断言。用例、schema 和录制 transcript 的方法见 [evals/README.md](evals/README.md)。
