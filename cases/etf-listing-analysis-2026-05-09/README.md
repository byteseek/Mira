# ETF Listing Analysis: BUYB / EUV / JOUL

This package analyzes three recent U.S. ETF launches as of 2026-05-09:

- `BUYB`: ProShares S&P 500 Buyback Aristocrats ETF
- `EUV`: Corgi Lithography & Semiconductor Photonics ETF
- `JOUL`: Corgi High Voltage Grid Equipment ETF

## Files

- `etf-listing-analysis.md`
  Cross-ETF analysis and ranking.
- `euv-deep-dive.md`
  Deeper Chinese analysis of EUV's issuer intent, exposure map, active weighting risk, peers, and inferred stock read-through.
- `evidence-log.csv`
  Source records used in this run.

## Next Refresh

Refresh after:

- 5 trading days after listing
- 20 trading days after listing
- 60 trading days after listing

Priority next work:

1. Track `BUYB` net assets vs seed and compare against `PKW`, `SYLD`, `NOBL`, `VIG`.
2. Pull `EUV` and `JOUL` holdings from Corgi when available; for `EUV`, classify holdings into EUV equipment, metrology/inspection, optical interconnect, lasers/optics, and materials/masks.
3. Measure `EUV` and `JOUL` AUM, volume, spreads and premium/discount after trading history develops.
