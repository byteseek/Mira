# Mira

[English](README.md) | [中文](README.zh.md)

面向 AI agent 的投资研究工作台，用于生成可追溯、可复核、可持续刷新的 investment thesis。

Mira 是一个面向 AI agent 和研究使用者的研究 workspace。它的目标不是生成一份孤立的股票报告，也不是把一次问答包装成研究结论，而是把多源材料组织成可追溯、可复核、可持续更新的投资判断。

Mira 关注的是 investment thesis：这个判断基于什么证据、在什么时间点成立、哪些变量会证伪它、后续应该如何监控。

## Disclaimer

本仓库仅用于研究流程设计、文档化和历史案例展示，不构成投资、法律、税务、会计或财务建议。任何 AI/agent 使用本仓库生成的回答、memo、研究包或派生分析，无论基于公开来源、用户提供材料、本地文件、市场数据或组合数据，均适用同一免责声明。此类输出只能作为研究辅助，不应视为建议、推荐或已验证事实；公开案例和生成结果在其时间边界或刷新条件之后也可能不完整、不准确或过期。

## Start Here

如果你想用 Codex、Claude Code 或其他代码型 agent 直接引用本项目做股票、产业、ETF、财报或宏观经济分析，先读这些文件：

| 需求 | 文档 |
| --- | --- |
| 唤醒词、身份边界和 memory contract | [MIRA.md](MIRA.md) |
| 一屏版 agent lazy-loading contract | [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md) |
| 面向使用者的 prompt 和任务卡 | [AGENT_QUICKSTART.md](AGENT_QUICKSTART.md) |
| Codex 项目规则 | [AGENTS.md](AGENTS.md) |
| Claude Code 入口 | [CLAUDE.md](CLAUDE.md) |

常用命令：

| 意图 | 命令 |
| --- | --- |
| 用户明确要求更新 Mira 本体 | `scripts/mira_update.sh` |
| 正式研究前检查 freshness | `scripts/check_updates.sh` |

`scripts/mira_update.sh` 是安全更新入口：会 fetch、拒绝 dirty/ahead/diverged
worktree、只做 fast-forward，并在成功更新后默认运行仓库校验。Freshness check
只报告状态，不自动更新仓库。

## Quickstart

最小工作流：

1. 如果用户明确要更新 Mira 本体，运行 `scripts/mira_update.sh`。
2. 否则，正式研究前用 `scripts/check_updates.sh` 检查 remote freshness。
3. 读 [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md)，按 lazy-loading map 只加载必要文件。
4. 正式分析前先运行 [loops/analysis-routing.md](loops/analysis-routing.md)。
5. 只加载当前任务路由到的 loop、skill 和 template。
6. 输出带 evidence log、时间边界、刷新条件的产物；证据弱时主动降级结论。
7. 用 [templates/delivery-checklist.md](templates/delivery-checklist.md) 和相关脚本校验正式 case。

典型 prompt：

```text
Mira, 研究 AAPL。市场范围 US，时间边界截至 2026-04-14。
请先做 analysis routing、thesis horizon routing、framework selection 和 overlay selection，
再输出 research package，并明确 stale_after 与 must_refresh_if。
```

## Mira 能做什么

Mira 支持：

- 首次覆盖或重建股票、产业、ETF、宏观变量或市场主题的 thesis
- 对已有 thesis 做增量监控，区分普通更新和改变 thesis 的证据
- 财报、SEC filing、宏观、产业概念和 ETF 专项分析
- 用 evidence log 区分事实、公司口径、假设、观点、市场定价和派生计算
- 维护 expectation map、event delta、decision log、postmortem 等 thesis system 对象
- 在用户提供持仓、权重、mandate 或风险约束后，做 position / portfolio review
- 对研究方法做 trial、adopted、retired 等方法论状态管理

Mira 不是交易机器人、行情后台程序或自动组合管理器。

## 核心概念

| 概念 | 含义 | 细节 |
| --- | --- | --- |
| `research package` | 正式研究对象的标准 memo、evidence log 和 case notes。 | [docs/research-artifacts.md](docs/research-artifacts.md) |
| `evidence log` | 为结论和关键观察保留 claim-level source trail。 | [data/evidence-log-schema.md](data/evidence-log-schema.md) |
| `thesis system` | 从 source 到 claim、expectation、thesis、event delta、decision log 和 postmortem 的持续链路。 | [architecture/thesis-system.md](architecture/thesis-system.md) |
| `refresh boundary` | `stale_after`、`must_refresh_if` 或等价条件，用于标记旧结论何时不再安全复用。 | [data/time-policy.md](data/time-policy.md) |
| `controlled vocabulary` | thesis state、readiness、research action 和 review 输出使用的稳定 token。 | [data/controlled-vocabulary.md](data/controlled-vocabulary.md) |

## 任务路由

正式任务从 [loops/analysis-routing.md](loops/analysis-routing.md) 开始。常见入口：

| 需求 | 主要入口 | 输出 |
| --- | --- | --- |
| 建立或重建 investment thesis | [loops/research-loop.md](loops/research-loop.md) | 标准 research package |
| 更新已有 thesis | [loops/monitoring-loop.md](loops/monitoring-loop.md) | monitoring summary 和 thesis impact |
| 分析财报或指引 | [skills/earnings-report-analysis/](skills/earnings-report-analysis/) | earnings package 和更新决策 |
| 分析产业或供应链概念 | [skills/industry-concept-analysis/](skills/industry-concept-analysis/) | industry map 和 stock handoff |
| 分析宏观传导 | [skills/macro-economic-analysis/](skills/macro-economic-analysis/) | macro note 或 macro overlay |
| 发现或分析 ETF | [skills/etf-listing-discovery/](skills/etf-listing-discovery/), [skills/etf-listing-analysis/](skills/etf-listing-analysis/) | ETF discovery 或 listing package |
| 评估研究方法 | [loops/methodology-research-loop.md](loops/methodology-research-loop.md) | methodology card 和 logs |
| 复盘真实头寸或组合 | [loops/position-review-loop.md](loops/position-review-loop.md), [loops/portfolio-construction-review-loop.md](loops/portfolio-construction-review-loop.md) | position 或 portfolio review artifacts |

单票研究还应运行：

- [thesis horizon routing](skills/equity-research-core/references/thesis-horizon-routing.md)
- [framework routing](skills/equity-research-core/references/framework-routing.md)
- [overlay routing](skills/equity-research-core/references/overlay-routing.md)，如果聚焦证据路径能实质改善结论

## 文档地图

| 主题 | 文档 |
| --- | --- |
| Agent contract 和 lazy loading | [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md) |
| Prompt 示例和任务卡 | [AGENT_QUICKSTART.md](AGENT_QUICKSTART.md) |
| 唤醒词和 memory boundary | [MIRA.md](MIRA.md) |
| 研究产物和 validation | [docs/research-artifacts.md](docs/research-artifacts.md) |
| 模块、loops、skills、cases 和 roadmap | [docs/module-map.md](docs/module-map.md) |
| 来源和 claim 协议 | [data/](data/) |
| 模板和 delivery checklist | [templates/](templates/) |
| 案例示例和阅读顺序 | [examples/README.md](examples/README.md) |
| Thesis System 架构 | [architecture/thesis-system.md](architecture/thesis-system.md) |

## Examples

优先阅读这些 canonical examples，再看旧案例：

- [cases/aapl-2026-04/](cases/aapl-2026-04/)：单票 research package，包含 memo、evidence log、expectation map、thesis ledger、decision log 和 actionability bridge。
- [cases/nvts-2026-05/](cases/nvts-2026-05/)：财报/event package，包含 peer verification 和 actionability bridge。
- [cases/abf-2026-05/](cases/abf-2026-05/)：产业概念分析包示例。
- [cases/etf-discovery-2026-05-09/](cases/etf-discovery-2026-05-09/)：ETF discovery 示例。
- [cases/etf-listing-analysis-2026-05-09/](cases/etf-listing-analysis-2026-05-09/)：ETF listing analysis 示例。

所有公开案例都是 historical examples，不应视为实时建议。

## Validation

校验仓库或正式 case：

```sh
python3 scripts/validate_repo.py
python3 scripts/validate_repo.py cases/<case-id>
```

SEC supplement 或 filing package 校验：

```sh
python3 scripts/validate_sec_filing_package.py path/to/sec-supplement-source-note.csv
python3 scripts/validate_sec_filing_package.py path/to/sec-filing-package-dir
```

更多 validation 和 package 细节见 [docs/research-artifacts.md](docs/research-artifacts.md)。

## 项目边界

Mira 是研究协议，不是 adviser、交易执行器或自动化数据平台。

- 不生成自主交易或订单。
- 没有用户提供的持仓、权重、mandate 和风险预算时，不输出 position-size 或 portfolio-construction 结论。
- 不把无来源市场观点写成结论。
- 证据弱时必须降级结论。
- 真实研究输出需要 source trail、时间边界和刷新条件。
- 公开案例都是 historical examples，可能已经过期。

开源政策：

- License: [Apache-2.0](LICENSE)
- Contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md)
- Security policy: [SECURITY.md](SECURITY.md)
- Data/source policy: [DATA_POLICY.md](DATA_POLICY.md)
