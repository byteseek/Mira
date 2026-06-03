# Public Source Targets

这个文件定义公开网页/公开端点的按需读取目标。它不是订阅、采集或落库计划；agent 只在研究需要时打开对应页面或端点，读取并解析当时可见的数据。

`source-registry.csv` 里可以登记可复用 target 模板；进入具体研究包时，必须在 `evidence-log.csv` 或 case notes 里写清楚实际 ticker、CIK、series id、日期区间、读取日期和 as-of date。

## Default Target Set

首版研究或 monitoring 默认优先检查以下按需目标：

| layer | default targets | role |
| --- | --- | --- |
| 原始披露 | SEC EDGAR company submissions、companyfacts、公司 IR | 核心事实、财务、公告时间线 |
| 市场快照 | Yahoo Finance quote、statistics、history、options、holders | 价格、估值、技术面、量价、持仓、期权和市场背景 |
| 财务交叉核验 | Yahoo Finance financials、StockAnalysis、MacroTrends | 快速 screening 和趋势核验 |
| 宏观背景 | FRED、BLS、BEA | 利率、通胀、就业、GDP、行业周期 |
| 新闻与叙事 | Yahoo Finance news、主流媒体原文、X/YouTube watchlist | 事件发现、情绪和叙事变化 |
| ETF 新发发现 | 交易所 new listings、issuer launch pages、SEC fund filings、ETF.com launch news | 新上市 ETF 候选、申请状态、产品语境 |
| 非美本地市场披露 | CNINFO / SSE / SZSE、HKEXnews、JPX / EDINET、MOPS / TWSE、DART / KRX、ESMA / OAM / Euronext | 本地公告、监管披露、上市状态、行情和市场结构 |

## Non-US Equity Targets

非美单股研究不能默认把 SEC / Yahoo Finance 当成完整 source stack。默认顺序是：

1. 本地监管、交易所或官方披露平台。
2. 公司 IR 的公告、年报、季报、presentation 和 webcast。
3. 交易所或官方行情 / 统计入口。
4. Yahoo Finance、Stooq 或其他聚合页，只做延迟行情、估值或三表 screening 交叉核验。
5. 专业媒体、卖方、社交源只用于事件发现、叙事和解释，不能替代本地披露。

分市场默认 target：

| market | primary disclosure targets | market / structure targets | notes |
| --- | --- | --- | --- |
| A 股 | `cninfo_a_share_disclosure_search`; `sse_listed_company_announcements`; `szse_listed_company_announcements` | `csrc_listed_company_disclosure_rules`; Yahoo / Stooq as delayed cross-check | CNINFO、上交所、深交所优先。若涉及政策、再融资、减持、停复牌、指数/北向资金或治理折价，必须跑 market-structure-policy gate。 |
| 港股 | `hkexnews_listed_company_publications`; company IR | `hkex_new_listing_information`; `hkex_ccass_shareholding_search`; Yahoo / Stooq as delayed cross-check | HKEXnews 是公告和报告主入口。CCASS 只能说明中央结算系统参与者持仓/托管状态，不等于最终实益拥有人。 |
| 日股 | `jpx_company_announcements_service`; `edinet_disclosure_system`; company IR | `jpx_listed_company_search`; Yahoo / Stooq as delayed cross-check | JPX 英文公告可能是摘要或英文材料，关键事实应回到日文 TDnet / EDINET / issuer IR。 |
| 台股 | `mops_twse_disclosure_search`; company IR | `twse_market_statistics`; Yahoo / Stooq as delayed cross-check | MOPS 优先用于公告、财报、重大讯息；TWSE 统计用于价格、成交和上市状态。 |
| 韩股 | `opendart_fss_api`; `english_dart_fss`; company IR | `krx_kind_disclosure_system`; Yahoo / Stooq as delayed cross-check | English DART 有翻译/法律效力限制；关键结论优先用 Korean DART / OpenDART 的原始记录。 |
| 欧股 | issuer IR; national OAM routed through `ec_transparency_oam_directory` | `esma_issuer_disclosure_hub`; `euronext_live_markets`; venue pages | 欧洲没有单一“欧股 EDGAR”。先确定上市地、issuer home member state、OAM、交易场所和 ISIN，再登记具体 OAM 或公司 IR source。 |

记录要求：

- 每条本地披露必须记录本地代码、交易所/市场板块、文件标题、发布日期、报告期、读取日期和实际 URL。
- 多地上市、A/H、ADR/H、存托凭证或 secondary listing 必须记录价格发现地、主要披露地和 share-class 差异。
- 使用英文翻译页面时，必须标注 translation_or_summary，并说明是否回查原文。
- 欧股必须记录 home member state、OAM 或公司 IR route；不能只写 “Europe filing”。
- 如果只找到聚合行情而缺本地披露，输出应标为 `source_gap` 或 `watch_only`，不得升级为 durable thesis。

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

## Technical / Market Pricing Targets

技术面只作为 `market_price_and_trading` 来源下的市场定价层。它适合回答价格、成交、波动、事件反应、流动性和仓位问题，不适合证明基本面兑现。

默认按需目标：

- `daily_ohlcv`: 至少 252 个交易日的开高低收和成交量，用于趋势、均线、回撤、波动和量能计算。
- `benchmark_ohlcv`: 指数 ETF、行业 ETF 或 peer basket，用于相对强弱和异常收益。
- `event_calendar`: 财报、指引、监管、产品发布、宏观事件或其他明确 catalyst 日期。
- `options_chain`: expiry、strike、bid/ask、open interest、volume、implied volatility 和 quote time，用于隐含波动、skew、put/call 和 event implied move。
- `short_interest`: short interest、float、days to cover 和 as-of date，用于拥挤度和挤压风险。
- `holders_or_float`: 机构持仓、内部人持仓、float 和 share count，用于流动性和仓位背景。

记录要求：

- 所有技术面数据必须写 `as_of_date`。
- 盘中、期权和 quote 类数据必须写 `quote_time`。
- 事件反应必须写明 `event_date` 和 event source。
- 相对收益必须写明 benchmark 或 peer basket。
- 派生指标必须在 evidence log 里标为 `derived_calculation`，并列出上游 market-data source id。

## Public Endpoint Targets

公开 JSON/API 端点只作为“按需打开的结构化网页目标”。默认不做定时请求、不批量抓取、不保存完整镜像：

- `sec_company_archive_filing`: 读取具体 10-K、10-Q、8-K、S-1、DEF 14A 或 exhibit；进入 case 时必须记录 CIK、accession number、form type、filing date、report period、section/exhibit。
- `sec_inline_xbrl_viewer`: 读取 Inline XBRL 可读页面和 tag/context；用于导航和 tag trace，指标事实仍要保留 archive 或 companyfacts provenance。
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
- SEC supplement 只补充当前研究的事实核验；专项拆 10-K / 10-Q / S-1 / proxy / 8-K exhibit 时进入 `skills/sec-filing-analysis/SKILL.md`。
- SEC companyfacts 指标必须记录 CIK、taxonomy、tag、unit、period、form、filed date 和 frame（如有）；非标准 tag 或公司自定义 tag 不能直接做跨公司比较。
- 所有市场数据必须带 as-of date；期权、盘中价格和新闻还必须带 quote time 或 publish time。
- `free_with_key` 不等于付费，但需要记录 key 依赖、限流和失败降级路径。
- 新闻聚合页只用于发现事件；memo 中引用新闻结论时要登记原始文章或公告的 source record。
