# Live Data Source Policy

This file defines the minimum source behavior for time-sensitive market
questions. It is a source and freshness gate, not a promise of background
monitoring or autonomous trading.

Use this gate when the user asks about:

- today, now, current, live, intraday, premarket, after-hours, latest move
- 是否崩盘 / 是否调整 / 今天怎么了 / 现在还能不能看
- market reaction to an event that is still trading
- price, index, yield, FX, commodity, VIX, options or volume conditions where
  same-day data changes the answer

## Core Rule

For live-use answers, do a fresh source check before making a market judgment.
Do not rely on model memory, old case notes or stale market data.

Minimum live chain:

```text
time-sensitive prompt -> live data gate -> source cross-check -> quote_time/as_of
-> facts/inferences/judgment -> stale_after/must_refresh_if
```

If fresh data is unavailable, say so and downgrade the answer to `needs_refresh`,
`source_gap` or `watch_only`.

## Source Stack

Prefer the narrowest available source stack for the object:

| object | preferred live sources | fallback sources | minimum cross-check |
| --- | --- | --- | --- |
| US major index / ETF | exchange or official index page; Google Finance; Yahoo Finance; Stooq; broker/provider connector if authorized | professional media live blog with timestamp | two independent market-data sources, or one source plus a timestamped high-quality live article |
| single US equity | exchange/issuer trading page where available; Google Finance; Yahoo Finance quote; Nasdaq/NYSE page; authorized provider | professional media live article | quote source plus news/source explaining the event if the question asks "why" |
| non-US equity | local exchange/official quote page first; local disclosure/IR for events | Yahoo/Stooq/Google as delayed cross-check | local market source where practical; otherwise label as delayed/aggregated |
| rates / macro release | official release page or Treasury/FRED/Fed/BLS/BEA where applicable | professional media live coverage | official source for the released number; market source for reaction |
| crypto / FX / commodities | exchange/venue or reputable market-data provider | professional media live coverage | two venues/providers if the move is material |

For non-US markets, apply `data/market-default-packs.csv` first. Aggregated
quotes alone are enough for a quick delayed market read, not for a durable local
market conclusion.

## Required Fields

Every live or same-day market-pricing answer should state or carry internally:

- `research_object`
- `market_scope`
- `time_boundary`
- `source_boundary`
- `quote_time` or `publish_time`
- `as_of_date`
- `source_names`
- `freshness_status`: `live`, `delayed`, `stale`, or `unavailable`
- `cross_check_status`: `passed`, `partial`, or `failed`
- `stale_after`
- `must_refresh_if`

For quick answers, the visible output can be compact, but it must still include
the time boundary and freshness caveat when the judgment depends on live data.

## Search Requirement

Search or live-source lookup is required when the answer uses any of these
freshness claims:

- "today", "currently", "right now", "latest", "premarket", "after-hours"
- same-session index/price/volatility direction
- market reaction to a newly published event
- whether a move is a pullback, correction, crash, squeeze, breakout or panic

When the question asks only for a stable definition, historical explanation or
methodology, this gate can be waived with `live_data_gate=waived_definition`.

## Classification Heuristics

Use explicit thresholds where possible, and state them:

- `normal_noise`: major index move less than about 1% and volatility calm.
- `pullback_or_adjustment`: major index down about 1-3%, or sector/index
  weakness with contained volatility and no broad liquidity stress.
- `sharp_selloff`: major index down about 3-5%, VIX or equivalent volatility
  rising sharply, breadth materially weak.
- `crash_or_panic`: major index down more than about 5% intraday or over a very
  short window, volatility in a stress regime, broad cross-asset or liquidity
  deterioration, and credible evidence of forced selling or systemic stress.

These are heuristics, not labels to force. If the object is a high-volatility
single stock, use object-specific history, beta and event context instead of
major-index thresholds.

## Failure Modes

Common live-data failures:

- source is delayed but not labeled as delayed
- quote time is missing or from a previous session
- search result headline is current but underlying article is old
- one aggregator has a stale cached quote
- futures, ETF and cash index are mixed without naming the instrument
- premarket/after-hours move is treated as regular-session breadth
- price action is used to prove a fundamental conclusion
- a news headline explains correlation but not causality

If any of these affect the answer, downgrade the judgment and state the gap.

## Output Rules

For a live market quick map, include:

- core judgment
- fact snapshot with source/time
- inference separating price action from cause
- confidence and reversal condition
- `stale_after` or `must_refresh_if`

Do not give trade execution instructions. If the user asks about buying,
selling, adding, trimming, hedging or options, route through the actionability
and instrument gates after the live-data gate.

