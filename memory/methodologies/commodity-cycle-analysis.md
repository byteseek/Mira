# Methodology Card: commodity-cycle-analysis

- status: trial
- role: standalone skill and equity overlay
- last_updated: 2026-05-30
- source_bucket: official, market_data, institutional, practitioner, first_principles, derived_internal
- source_quality: medium-high
- credibility_score: medium
- credibility_basis: The method is anchored in observable commodity research inputs: official supply-demand data, exchange or market pricing, futures curve structure, positioning data and company disclosure. Credibility remains medium until tested in live Mira cases.
- search_coverage: initial official and market-data coverage across energy, metals, agriculture, futures curves and positioning
- search_gaps: Needs more specialist mining, shipping, refining, power/gas and China-specific source paths; needs failure cases where price signals diverged from fundamentals.
- comparison_baseline: macro-regime-analysis plus supply-chain overlay
- empirical_validation_mode: live trial and case backtest
- follow_through_plan: Test on at least three cases: crude/oil equities, copper/miners and gold/gold miners; optionally lithium/battery materials.

## Core Idea

Commodity research should start from physical balance and market structure, then map the result into assets. The method separates seven layers:

- physical supply-demand balance
- inventory and futures curve
- cost curve and supply response
- demand map
- policy, geopolitics and trade flow
- financial conditions and positioning
- asset transmission and market pricing

The goal is to avoid treating every commodity move as either generic macro or a simple price chart.

## Reverse-Engineered From

- Official energy balance workflows such as EIA, IEA and OPEC materials.
- Official agriculture balance-sheet workflows such as USDA WASDE.
- Exchange and regulatory market data workflows such as LME market data and CFTC COT.
- Existing Mira `macro-regime-analysis`, `supply-chain` and `industry-concept-analysis` methods.

## Search Paths Used

See `memory/methodologies/commodity-cycle-analysis-search-log.csv`.

Search families covered:

- official energy balance data
- agriculture supply-demand tables
- exchange warehouse inventory
- futures curve mechanics
- regulatory positioning data
- cross-commodity institutional framing

## Use When

- The research object is a commodity, commodity future, commodity ETF or resource cycle.
- A company or ETF's main variable is commodity beta.
- The question depends on inventories, futures curve structure, cost curve, supply disruption, trade flows, OPEC/USDA/EIA/IEA/LME/CFTC signals or policy shocks.
- The goal is to distinguish commodity beta from company alpha.

## Avoid When

- The asset is primarily driven by company-specific orders, financing, regulatory approval, technology validation or M&A.
- Commodity exposure is too small to change earnings, cash flow, risk premium or valuation.
- Available evidence is only price action with no balance, inventory, curve or source trail.

## Applies To

- crude oil, refined products, natural gas, LNG, coal
- copper, aluminum, nickel, lithium, uranium, iron ore, steel
- gold, silver and other precious metals
- grains, oilseeds and other agriculture commodities
- resource equities, commodity ETFs, materials and energy companies
- inflation-sensitive macro assets when the commodity shock is the key driver

## Core Question

Is the market repricing a durable commodity balance change, a temporary inventory or curve squeeze, a cost-curve reset, a policy/geopolitical shock, or a financial-positioning move?

## Required Inputs

- current spot and futures pricing
- inventory level and direction
- supply and demand baseline
- cost curve or incentive-cost proxy
- policy/geopolitical and trade-flow context
- positioning or flow data where relevant
- company disclosure if mapped to equities
- market-pricing and consensus/proxy view

## Primary Signal

The primary signal is the consistency between:

- physical balance
- inventory direction
- futures curve structure
- marginal cost / supply response
- market pricing

The strongest setups occur when these layers point in the same direction and the target asset has not fully priced the change.

## Why It Works

Commodity prices connect observable physical constraints with financial market pricing. Inventories and curves often reveal whether spot price moves reflect scarcity, storage economics, financing cost, seasonality or positioning. Cost curves explain whether price levels can change supply behavior. Asset transmission prevents the analyst from assuming that producers, consumers, ETFs and macro assets all have the same exposure.

## Failure Mode

- Physical balance data is stale or revised.
- Visible inventories miss hidden or regional inventories.
- Futures curve is distorted by logistics, financing or contract squeezes.
- Producer equity exposure is weakened by hedges, costs, project risk or political risk.
- A correct commodity call is already fully priced into equities or ETFs.
- The method becomes a long checklist and loses the dominant-driver discipline.

## Evidence Cost

Medium to high. Quick notes can use official balances, curve snapshots and company disclosures. Deep dives need trade-flow, cost-curve, regional basis, positioning and company-level sensitivity work.

## Speed Vs Depth

- `quick_check`: price, curve, inventory, one official balance source, market pricing and refresh triggers.
- `standard`: full balance, curve, inventory, cost curve, demand map, policy/trade-flow and asset transmission.
- `deep_dive`: regional basis, company sensitivity, hedges, project economics, positioning and scenario table.

## Comparison To Existing Methods

Compared with `macro-regime-analysis`, this method explains commodity-specific physical and market-structure variables rather than broad growth, inflation, rates and liquidity.

Compared with `supply-chain`, this method is centered on traded commodities, inventories, curves and cost curves rather than company supply-chain validation.

Compared with `industry-concept-analysis`, this method is less about mapping a technology or industry concept and more about balancing supply, demand, inventory and price formation.

## Follow-Through Criteria

The method is useful if it improves:

- dominant-driver identification
- separation of physical facts from market interpretation
- commodity beta versus company alpha separation
- refresh triggers and falsification conditions
- equity and ETF transmission quality

## Trial Design

Run the method on at least three cases:

- crude oil or oil equities
- copper or copper miners
- gold or gold miners

Optional fourth case:

- lithium or battery materials, because it tests cost curve, inventory and long-cycle demand assumptions.

Each trial should include a `commodity-cycle-note.md`, evidence log and a short post-case review.

## Falsification Conditions

Do not upgrade to adopted if:

- it mostly repeats `macro-regime-analysis`
- it fails to distinguish inventory/curve tightness from durable supply-demand change
- it cannot separate commodity beta from company alpha
- it produces conclusions without official, market-data or company source trails
- it materially slows simple research without improving decision quality

## Adoption Decision

Keep under `trial`.

Required before adoption:

- at least two completed real commodity or commodity-equity cases
- at least one follow-through or postmortem
- documented failure mode from a real case
- comparison against macro-only or supply-chain-only analysis
- no unresolved source-quality issue in the trial cases
