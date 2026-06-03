# ETF Listing Analysis: BUYB / EUV / JOUL

This package analyzes three recent U.S. ETF launches as of 2026-05-09.

## Open Source Notice

- case_status: historical_example
- not_investment_advice: true
- research_cutoff_date: 2026-05-09
- stale_after: first 5 / 20 / 60 trading-day follow-up windows after listing
- refresh_policy: refresh before any live trading or portfolio decision

## Products

- `BUYB`: ProShares S&P 500 Buyback Aristocrats ETF
- `EUV`: Corgi Lithography & Semiconductor Photonics ETF
- `JOUL`: Corgi High Voltage Grid Equipment ETF

## Files

- `etf-listing-analysis.md`
  Cross-ETF analysis and ranking.
- `euv-deep-dive.md`
  Deeper Chinese analysis of EUV's issuer intent, exposure map, active weighting risk, peers, and inferred stock read-through.
- `evidence-log.csv`
  Claim-level evidence records used in this run.

## Next Refresh

Refresh after:

- 5 trading days after listing
- 20 trading days after listing
- 60 trading days after listing

Priority next work:

1. Track `BUYB` net assets vs seed and compare against `PKW`, `SYLD`, `NOBL`, `VIG`.
2. Pull `EUV` and `JOUL` holdings from Corgi when available; for `EUV`, classify holdings into EUV equipment, metrology/inspection, optical interconnect, lasers/optics, and materials/masks.
3. Measure `EUV` and `JOUL` AUM, volume, spreads and premium/discount after trading history develops.
