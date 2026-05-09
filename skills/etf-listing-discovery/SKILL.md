# ETF Listing Discovery Skill

这个 skill 用于查找新上市、即将上市、已提交申请或刚被媒体/发行人宣布的 ETF/ETP。

它是 `etf-listing-analysis` 的前置发现层：

```text
ETF listing discovery -> new-etf-watchlist -> ETF listing analysis
```

它不负责深度判断 ETF 是否值得买入，只负责把候选产品找出来、去重、补齐关键字段、排序，并决定哪些进入 `etf-listing-analysis`。

## Use When

- 用户要求查找最近新上市 ETF
- 用户要求监控新 ETF、ETF 申请、ETF launch、ETF issuer 新产品
- 用户想从 ETF 新发中发现市场偏好、配置方向、主题热度或结构变化
- 用户给出一个主题，要求找相关新 ETF 或申请中的 ETF
- `etf-listing-analysis` 缺少输入，需要先发现候选产品

## Required Inputs

- market_scope
  例如 US、global、HK、CN、EU
- discovery_window
  例如 last 7 days、last 30 days、YTD、since date
- discovery_mode
  例如 listed、upcoming、filed、announced、all
- theme_filter
  可选，例如 crypto、AI、covered call、single-stock、duration、China、commodity
- output_limit
  默认先保留前 20 个候选
- research_cutoff_date

## Source Priority

优先级从高到低：

1. `exchange notices`
   交易所新上市/新发行通知，确认 ticker、上市日期、交易所。
2. `issuer launch pages`
   发行人产品页、新闻稿、招募说明书，确认策略、费用、持仓、指数。
3. `regulatory filings`
   SEC/监管文件，确认申请、修订、规则和基金注册信息。
4. `ETF industry media`
   ETF.com、ETF Trends、VettaFi、Bloomberg/Reuters 等，用于发现线索和语境。
5. `market data`
   AUM、成交、价差、首日交易数据，用于初步排序，不替代上市确认。

## Discovery Workflow

### 1. Define Search Scope

先明确：

- 市场：US / global / local market
- 时间窗口：上市日、公告日、申请日，不能混用
- 状态：已上市、即将上市、已申请、传闻/媒体报道
- 产品范围：ETF only，还是包含 ETN、ETC、ETP、closed-end fund

### 2. Search Source Buckets

至少覆盖三类来源：

- 交易所或监管来源
- 发行人或指数提供商来源
- ETF 行业媒体或市场数据来源

如果只找到媒体文章，必须标记为 `needs_primary_confirmation`。

### 3. Normalize Candidate Records

每个候选至少补齐：

- ticker
- ETF name
- issuer
- exchange
- listing_status
- listing_date 或 filing_date
- product_type
- underlying_exposure
- source_id
- source_url
- source_publish_date 或 last_checked_date
- why_worth_analyzing

### 4. Deduplicate

去重规则：

- 同 ticker 同 exchange 视为同一产品
- 同一 ETF 的媒体报道、交易所通知、发行人页面合并成一个候选
- share class、dual listing、fund conversion 不能误判为全新产品，必须标记

### 5. Score Priority

每个候选给出 `priority_score`，建议 0 到 5：

- `5`: 新主题/新资产可达性/多发行人集中推出/上市后快速放量
- `4`: 有清晰结构创新、机构配置含义或高热度主题
- `3`: 普通但值得观察的新 ETF
- `2`: 低费率复制、存量产品变体或主题纯度存疑
- `1`: 信息不足、可能只是产品噪音
- `0`: 重复、转换、清盘替代或不属于 ETF/ETP 范围

### 6. Route Next Action

每个候选必须落到一个动作：

- `analyze_now`
  进入 `etf-listing-analysis`。
- `watch_t1`
  等 5、20、60 个交易日数据。
- `needs_primary_confirmation`
  先找交易所、发行人或监管来源。
- `ignore_duplicate`
  重复或只是 share class / dual listing。
- `ignore_noise`
  暂不跟踪。

## Output Package

默认输出 `etf-listing-discovery-package`：

- `new-etf-watchlist.csv`
- `discovery-log.md`
- `evidence-log.csv`

`new-etf-watchlist.csv` 是传给 `etf-listing-analysis` 的入口。

## Search Query Patterns

英文查询：

- `new ETF launches this week`
- `site:cboe.com/us/equities/notices/new_listings ETF first trade date`
- `site:nyse.com ETF lists new fund`
- `site:sec.gov N-1A ETF prospectus`
- `{issuer} launches ETF`
- `{theme} ETF launch`
- `{theme} ETF filed SEC`

中文查询：

- `新上市 ETF`
- `ETF 新发 上市`
- `{主题} ETF 上市`
- `{发行人} 推出 ETF`
- `ETF 申请 文件`

## Quality Bar

- 不允许把媒体标题直接写成 confirmed listing
- 不允许把 filed、approved、announced、listed 混成一个状态
- 不允许只列 ticker，不补 issuer、exchange、listing date/source
- 不允许把 dual listing、share class conversion、mutual fund conversion 默认当新 ETF
- 不允许把 ETF 新发数量本身当趋势结论，必须交给 `etf-listing-analysis` 做 T0/T1 判断

## Handoff To ETF Listing Analysis

满足任一条件时进入 `etf-listing-analysis`：

- priority_score >= 4
- 同一主题 30 天内出现多个 issuer launch/filed
- 产品提供了新的资产可达性、收益结构、杠杆/反向工具或监管突破
- 上市后 AUM、成交或期权活动明显放量
- 成分股流动性较低，可能存在资金传导

