# Public Source Targets

这个文件定义公开网页/公开端点的按需读取目标。它不是订阅、采集或落库计划；agent 只在研究需要时打开对应页面或端点，读取并解析当时可见的数据。

`source-registry.csv` 里可以登记可复用 target 模板；进入具体研究包时，必须在 `evidence-log.csv` 或 case notes 里写清楚实际 ticker、CIK、series id、日期区间、读取日期和 as-of date。

## Default Target Set

首版研究或 monitoring 默认优先检查以下按需目标：

| layer | default targets | role |
| --- | --- | --- |
| 原始披露 | SEC EDGAR company submissions、companyfacts、公司 IR | 核心事实、财务、公告时间线 |
| 市场快照 | Yahoo Finance quote、statistics、history、options、holders | 价格、估值、量价、持仓、期权和市场背景 |
| 财务交叉核验 | Yahoo Finance financials、StockAnalysis、MacroTrends | 快速 screening 和趋势核验 |
| 宏观背景 | FRED、BLS、BEA | 利率、通胀、就业、GDP、行业周期 |
| 新闻与叙事 | Yahoo Finance news、主流媒体原文、X/YouTube watchlist | 事件发现、情绪和叙事变化 |
| ETF 新发发现 | 交易所 new listings、issuer launch pages、SEC fund filings、ETF.com launch news | 新上市 ETF 候选、申请状态、产品语境 |

## Yahoo Finance Targets

Yahoo Finance 适合做公开市场数据入口，但不作为公司原始事实来源：

- `quote`: 最新价、涨跌幅、市值、成交量、估值快照。
- `history`: 日线价格和成交量，用于技术面和回撤/收益测算。
- `key-statistics`: 估值、盈利能力、杠杆、股本和交易统计。
- `financials` / `balance-sheet` / `cash-flow`: 标准化三表，用于快速筛选和趋势判断。
- `analysis`: 分析师预期、修正和成长假设，只作为 consensus/sentiment signal。
- `options`: 期权链、隐含波动和期限结构，需要记录 expiry 和 quote time。
- `holders`: 机构和内部人持仓概览，重大持仓结论需回到 13F、proxy 或其他原始文件。
- `profile`: 业务描述、行业、管理层和地址，只用于快速定位。
- `news`: 聚合新闻入口，正式引用必须追到原始媒体、公告或公司材料。

## Public Endpoint Targets

公开 JSON/API 端点只作为“按需打开的结构化网页目标”。默认不做定时请求、不批量抓取、不保存完整镜像：

- `sec_company_submissions_api`: 查 filing timeline、8-K、10-Q、10-K、proxy、Form 4 等。
- `sec_companyfacts_api`: 查 US issuer 的 XBRL 财务事实，优先级高于聚合站三表。
- `sec_xbrl_frames_api`: 做跨公司同一 XBRL tag 的横截面比较。
- `fred_macro_series_api`: 查利率、通胀、信用、流动性和宏观周期序列。
- `fred_release_calendar_api`: 给 monitoring loop 生成宏观数据刷新触发。
- `bls_public_data_api`: 查 CPI、PPI、就业、工资和行业劳动数据。
- `bea_data_api`: 查 GDP、收入、消费、行业增加值等周期背景。

## ETF Listing Discovery Targets

ETF 新发发现是按需搜索，不是后台批量采集。默认先覆盖：

- 交易所新上市/新发行通知：确认 ticker、exchange、first trade date。
- 发行人 launch page 和产品页：确认 strategy、fee、holdings、index 或 active mandate。
- SEC / 本地监管 fund filings：确认 filed、effective、amended、withdrawn 等状态。
- ETF 行业媒体：用于发现线索和主题语境，必须回到 primary source 确认。
- 市场数据页：用于上市后 AUM、成交、价差和 T1 watch，不替代上市确认。

## Usage Rules

- 只在具体研究问题需要时读取目标页面；不要因为 target 存在就自动扫全量页面。
- 核心业务和财务事实优先使用 `L1/L2`；Yahoo、StockAnalysis、MacroTrends 只作为 `L5` secondary 或 signal。
- 同一指标如果聚合站之间不一致，先检查口径、时间点、调整项，再回到 SEC 或公司披露。
- 所有市场数据必须带 as-of date；期权、盘中价格和新闻还必须带 quote time 或 publish time。
- `free_with_key` 不等于付费，但需要记录 key 依赖、限流和失败降级路径。
- 新闻聚合页只用于发现事件；memo 中引用新闻结论时要登记原始文章或公告的 source record。
