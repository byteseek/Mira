# ETF Listing Discovery Log

- market_scope: `US`
- discovery_window: `2026-04-01 to 2026-05-09`
- discovery_mode: `listed / launched / media_reported_launched`
- theme_filter: `none`
- research_cutoff_date: `2026-05-09`
- output_limit: `priority shortlist`

## Search Paths Used

- ETF.com launch table for 2026 launches.
- ETF.com latest launch coverage.
- ProShares issuer launch page and product page for `BUYB`.
- Defiance issuer launch releases for `AMKL` and `AMA`.
- Corgi launch article for the 34-ETF batch and Corgi thematic list.

## Source Coverage

Covered:

- ETF industry media: `ETF.com`
- Issuer primary pages: `ProShares`, `Defiance`
- Product page confirmation: `BUYB`

Not yet covered:

- Exchange-level confirmation for Corgi tickers.
- Corgi issuer product pages and holdings.
- SEC prospectus / filing details for Corgi products and crypto products.
- Live AUM/volume/spread for all candidates beyond `BUYB`.

## Candidate Summary

The latest ETF supply is heavy in:

- structured buffer / defined-outcome products
- YieldBOOST / options income products
- single-stock leveraged products
- crypto and altcoin ETFs
- AI infrastructure subtheme ETFs
- broad factor/quality products

Most monthly buffer and term-bond ETFs were excluded from the high-priority list because they are more product-line rolling launches than new market-preference signals.

## High Priority Candidates

### `BUYB`

Priority: `5`

Rationale:

- First ETF focused exclusively on companies with persistent share buybacks.
- Useful for testing whether investor demand is moving from dividends toward broader shareholder yield.
- Product page has primary confirmation and enough initial product details for immediate T0 analysis.

Next action: `analyze_now`

### `EUV`

Priority: `5`

Rationale:

- Potentially clean exposure to lithography and semiconductor photonics.
- Fits AI infrastructure second-derivative theme after memory and optical/photonic names attracted attention.
- ETF.com explicitly framed it as one of the more genuinely interesting Corgi launches.

Next action: `needs_primary_confirmation`

### `JOUL` / `GASZ`

Priority: `4`

Rationale:

- Both are AI power-demand read-throughs.
- `JOUL` maps to grid equipment; `GASZ` maps to natural gas power and turbines.
- Useful for testing whether ETF product supply is following AI data-center power bottlenecks.

Next action: `needs_primary_confirmation`

### Single-stock leveraged semiconductor ETFs

Priority: `4`

Candidates:

- `AMKL`
- `AMA`

Rationale:

- Useful as trading-demand and retail/tactical sentiment signals.
- Not suitable as fundamental confirmation by themselves.

Next action: `liquidity_tool`

## Needs Primary Confirmation

The Corgi products should not be treated as fully confirmed investment candidates until these are collected:

- issuer product page
- exchange listing confirmation
- prospectus / SEC filing
- holdings or active mandate description
- fee and waiver details

## Duplicates / Exclusions

Excluded from priority list:

- monthly buffer roll series
- iBonds / term Treasury / term muni series
- ordinary sector YieldBOOST products without early AUM or volume confirmation
- broad style-box enhanced beta launches unless they show unusual T1 flow

## Handoff To ETF Listing Analysis

Immediate:

- `BUYB`

After primary confirmation:

- `EUV`
- `JOUL`
- `GASZ`

Watch-only:

- `CBOT`
- `CQTM`
- `XA`
- `BAVA`
- `BESO`
- `REXC`

## Search Gaps

- Need exchange notice confirmation for all Corgi tickers.
- Need issuer pages and holdings for Corgi thematic ETFs.
- Need AUM, volume, bid-ask spread and premium/discount after 5 trading days.
- Need peer comparison for `BUYB` vs `PKW`, `SYLD`, `NOBL`, `VIG`.

