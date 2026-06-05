# Source Taxonomy

这个文件定义 Mira 如何把 data source 按研究用途分层。它不替代
[source-schema.md](source-schema.md) 或 [source-policy.md](source-policy.md)：

- `source-schema.md` 定义 source record 字段。
- `source-policy.md` 定义来源优先级和使用边界。
- `source-taxonomy.md` 定义来源类别、可支持的 claim、禁止用途和刷新规则。

正式研究中仍然必须把具体 source 写入 `source-registry.csv` 或 case-local
source note，并把被使用的信息写入 canonical `evidence-log.csv`。

When a source enters through a user file, public API call, authorized data
provider, portfolio export or retained derived dataset, first apply
[ingestion-layer.md](ingestion-layer.md). The ingestion artifact records
permission, storage, field mapping and refresh scope; the evidence log records
the claim-level use.

仓库级 registry 的逐条分类见 [source-class-map.csv](source-class-map.csv)。

## Core Distinction

`source class` 不是可信度本身。高质量来源也可能只提供观点，低层级来源也可能提供有用线索。Mira 先判断来源类别，再判断具体 claim：

1. 来源从哪里来。
2. 这条信息是什么 claim。
3. 该 claim 能否支撑 durable conclusion。
4. 什么时候必须刷新。

## Source Classes

| source_class | typical source_group | default_authority | default_role | allowed_claims | disallowed_uses | refresh_rule |
| --- | --- | --- | --- | --- | --- | --- |
| `issuer_primary_disclosure` | `official_and_industry` | `L1` | `primary` | `fact`; `reported_metric`; `guidance`; `target`; `commitment`; management `company_claim` | 不把长期目标写成短期指引；不把管理层说法写成已验证事实 | 财报、8-K、公告、IR 更新后必须刷新 |
| `regulatory_and_exchange` | `official_and_industry` | `L2` | `primary` | `fact`; `reported_metric`; listing/status/governance/regulatory event | 不替代公司经营解释；不推断基本面质量 | 监管文件、交易所状态或规则变化后刷新 |
| `official_macro_and_industry` | `official_and_industry` | `L2` | `primary` / `secondary` | official statistics; industry capacity; demand indicators; policy facts | 不把宏观相关性写成公司级因果结论 | 新数据 release 或政策变更后刷新 |
| `market_price_and_trading` | `market_data` | `L5` | `secondary` | `market_pricing`; price; volume; valuation; options; short interest; ownership snapshot | 不用价格走势证明基本面兑现；不替代 consensus | 实时/日频数据按 as-of date；事件研究需记录 quote time |
| `aggregated_financial_data` | `market_data` | `L5` | `secondary` | screening metrics; standardized financial snapshot; cross-check | 不替代 SEC、公司财报或原始三表 | 重大结论前回查 L1/L2；至少随财报周期刷新 |
| `consensus_and_estimates` | `market_data` / `sellside_research` | `L5` | `secondary` / `signal` | `forecast`; revision; target-price distribution; expectation baseline | 不写成事实；不把单一估计当市场共识 | 财报前后、指引变更、重大修正后刷新 |
| `sellside_and_expert_research` | `sellside_research` | `L3` | `secondary` / `signal` | industry framework; forecast; opinion; variant perception; valuation method | 不替代原始披露；未批准付费内容不能假设可用 | 新研报、评级变化、行业数据更新后刷新 |
| `professional_media` | `social_and_community` / `sellside_research` | `L4` | `secondary` / `signal` | event report; interview; context; sentiment; reported claim | 不单独支撑核心 business quality 或 financial fact | 事件后 14 天默认降级为背景，除非有后续确认 |
| `industry_and_supply_chain_signal` | `official_and_industry` / `social_and_community` | `L2`-`L4` | `secondary` / `signal` | customer validation; product certification; channel check; capacity signal; competitor read-through | 不把单点渠道消息写成订单兑现；不把生态参与写成收入确认 | 新客户公告、认证、竞品财报或供应链反证后刷新 |
| `social_and_community_signal` | `social_and_community` | `L4` | `signal` | `sentiment`; `rumor_signal`; narrative shift; idea generation | 不进入 core conclusion；不支撑 bull/bear case，除非被 L1/L2/L4 high-quality source 确认 | 高频事件需 24-72 小时复查；未确认则保留为 watch |
| `local_user_material` | varies | varies | varies | user-provided filings, notes, exported data, screenshots, transcripts | 不自动假设版权、完整性或时效；缺日期不能支撑正式结论 | 按文件日期、用户说明和 case cutoff 记录 |
| `mira_derived_analysis` | `derived_analysis` | `L6` | `secondary` | `derived_calculation`; assumption; interpretation; scenario; memo conclusion | 不伪装成事实；没有 upstream source 不能支撑结论 | 上游 source 刷新或模型假设变化后刷新 |

## SEC Authority Note

SEC sources have two different roles:

- Specific issuer filings or filed exhibits from SEC Archives / Inline XBRL are `issuer_primary_disclosure` and can support `L1` company facts when the evidence row records CIK, accession number, form type, filing date, report period and section or exhibit.
- SEC `submissions`, `companyfacts` and `frames` endpoints are official regulatory datasets. They are usually `regulatory_and_exchange` with default `L2` authority in the source registry. Case rows using them must record taxonomy, tag, unit, period and frame when available.

Do not silently change authority level between registry and case evidence. If a case promotes or downgrades a specific SEC-derived claim, explain the reason in `notes`.

## Registry Classification

[source-class-map.csv](source-class-map.csv) maps every row in
`source-registry.csv` to one `source_class`. The map is intentionally separate
from the registry table so older source records keep their stable schema while
taxonomy review can evolve.

Rules:

- Every `source_id` in `source-registry.csv` must appear exactly once.
- Every mapped `source_class` must be listed in the `Source Classes` table.
- `review_status` should be `reviewed`, `needs_review`, or `deprecated`.
- If a source has mixed behavior, classify by its dominant approved use and put
  the caveat in `notes`.

## Usage Rules By Research Need

### Company Facts

Use `issuer_primary_disclosure` first. `aggregated_financial_data` can speed up screening, but durable financial facts must trace to filings, company releases or official exhibits when available.

### Expectations

Use `consensus_and_estimates` for market expectation baseline. If unavailable, write `source_gap` and avoid replacing consensus with price action, media tone or company guidance.

### Market Reaction

Use `market_price_and_trading` for price, volume, valuation and options-implied reaction. Treat it as `market_pricing`, not evidence that fundamentals improved or deteriorated.

For technical / market-pricing context, record price, volume, volatility, options, short interest and derived levels as `market_pricing` or `derived_calculation`. These claims can support setup quality, follow-through, trigger levels, invalidation and refresh priority, but they cannot by themselves support business execution, demand, margin or moat conclusions.

When the user asks about today, now, current market reaction, intraday direction
or whether a move is a pullback/crash/panic, first apply
[live-data-source-policy.md](live-data-source-policy.md). Live-use market
judgments require `quote_time` or `publish_time`, source freshness status and a
cross-check or explicit downgrade.

### Industry Context

Use `official_macro_and_industry`, `industry_and_supply_chain_signal`, `sellside_and_expert_research` and `professional_media` together. Single-source industry narratives should be downgraded unless confirmed by primary data or multiple independent sources.

### Early Alpha And Rumor Watch

Use `social_and_community_signal` only for discovery, monitoring and variant perception. The output must include:

- `verification_path`
- `what_would_confirm`
- `what_would_disconfirm`
- `next_refresh_trigger`

### Derived Work

Any `mira_derived_analysis` source must list upstream sources. If the upstream source becomes stale, contradicted or unavailable, the derived conclusion becomes `needs_refresh`.

## Default Source Stack

For formal single-equity research, the default source stack is:

1. `issuer_primary_disclosure`
2. `market_price_and_trading`
3. `consensus_and_estimates` or explicit `source_gap`
4. `professional_media` or `industry_and_supply_chain_signal` for event context
5. `mira_derived_analysis` with upstream links

For a monitoring update, the minimum source stack is:

1. source that triggered the update
2. existing thesis/evidence log
3. at least one confirming or disconfirming source where practical
4. market reaction source if the update is market-relevant

## Refresh Contract

Every case output using this taxonomy should include either:

- `stale_after`
- `must_refresh_if`
- or a case-specific refresh condition

Default stale rules:

- Company financial facts: next quarterly or annual report.
- Live market data: 30-60 minutes for intraday use unless the output states a
  stricter `stale_after`; same day for closing-session summaries.
- Market data: same day for live use; 30 days for background technical context.
- Event/news sources: 14 days unless confirmed by primary disclosure.
- Social and rumor signals: 24-72 hours for active monitoring; otherwise `watch_only`.
- Derived analysis: whenever any upstream source changes materially.

## Validation Questions

Before using a source for a durable conclusion, ask:

1. Is the source class appropriate for this claim?
2. Is the `claim_type` recorded separately from source quality?
3. Is there an `as_of_date` or `source_date`?
4. Is this source primary, secondary, signal or blocked for the specific conclusion?
5. What would refresh, weaken or invalidate the claim?
