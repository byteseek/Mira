# CRWV Event Delta

- event_name: Q1 2026 earnings
- event_type: earnings
- event_date: 2026-05-07
- analysis_cutoff_date: 2026-05-08
- prior_thesis_ref: `cases/crwv-2026-05/earnings-analysis.md`
- evidence_log_ref: `cases/crwv-2026-05/evidence-log.csv`
- thesis_impact: +1
- thesis_state_change: watch -> upgrade_watch candidate, not active upgrade

## Pre-Event Setup

The case evidence indicates the market focus was not only revenue growth, but whether backlog, active power, customer wins and financing capacity could support the multi-year AI infrastructure thesis. Pre-event consensus proxy is incomplete in the current case and should be marked `source_gap` for exact consensus numbers.

## Actual Disclosure

The earnings package records strong reported revenue growth, backlog and customer diversification signals, but also continuing concerns around leverage, financing cost and conversion of capacity into revenue.

## Delta Vs Expectation

| variable | delta | evidence status | interpretation |
| --- | --- | --- | --- |
| demand / backlog | positive | disclosed | Reinforces demand and customer diversification thesis. |
| delivery / capacity conversion | unresolved | disclosed / inferred | Backlog is not the same as timely revenue conversion. |
| financing burden | negative / unresolved | disclosed | Interest expense and leverage remain central thesis risks. |
| market expectation | source_gap | estimated | Exact consensus proxy needs stronger L5 estimate source in future event setup. |

## Revision Path

Most likely revision path: `revenue_revision` positive, partially offset by `cash_flow_revision` and `risk_premium_change` concerns from financing burden.

## Price Reaction Quality

Price reaction evidence should be treated as `market_pricing`, not proof of fundamental validation. A high-quality positive reaction would require follow-through in estimate revisions, funding cost, and capacity conversion evidence.

## Thesis Impact

Thesis impact remains `+1`, consistent with the earnings package: the quarter strengthens demand and customer diversification, but does not resolve execution and financing risks enough for a full thesis upgrade.

## Expectation Map Updates

- `demand_visibility`: upgrade from weak/unknown to medium, pending backlog conversion evidence.
- `financing_risk`: keep high.
- `capacity_conversion`: keep watch item.
- `customer_concentration`: modestly improved if customer wins are verified through future disclosures.

## Fact Vs Inference

- Facts: reported financials, backlog, customer and operating metrics disclosed in the earnings package and evidence log.
- Inferences: revenue revision path, risk premium interpretation and price reaction quality.
- Weakness: exact pre-event consensus proxy is incomplete and must be strengthened in future event-delta runs.

## Required Follow-Up

- Capture exact consensus revenue, EBITDA/EPS, capex and financing assumptions before the next earnings event.
- Track backlog conversion into recognized revenue.
- Track interest expense, refinancing terms and liquidity.
- Compare peer AI infrastructure disclosures for demand durability.
