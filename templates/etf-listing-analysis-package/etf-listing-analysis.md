# {{ etf_name }} ({{ ticker }}) ETF 上市分析

- market: {{ market }}
- issuer: {{ issuer }}
- listing_date: {{ listing_date }}
- product_type: {{ product_type }}
- management_mode: {{ management_mode }}
- weighting_mode: {{ weighting_mode }}
- underlying_exposure: {{ underlying_exposure }}
- holdings_status: {{ holdings_status }}
- research_question: {{ research_question }}
- research_cutoff_date: {{ research_cutoff_date }}
- thesis_horizon: {{ thesis_horizon }}
- stale_after: {{ stale_after }}

## 核心结论

{{ core_conclusion }}

## 产品拆解

{{ product_anatomy }}

## 发行意图

- primary_intent: {{ primary_intent }}
- secondary_intents: {{ secondary_intents }}
- why_now: {{ why_now }}
- target_buyer: {{ target_buyer }}
- issuer_edge: {{ issuer_edge }}
- marketing_vs_real_need: {{ marketing_vs_real_need }}

## 结构与可达性

- product_structure_signal: {{ product_structure_signal }}
- access_change: {{ access_change }}
- distribution_fit: {{ distribution_fit }}
- timing_context: {{ timing_context }}
- issuer_quality: {{ issuer_quality }}

## 持仓与暴露地图

- holdings_status: {{ holdings_status }}
- selection_universe: {{ selection_universe }}
- selection_rules: {{ selection_rules }}
- top_holdings: {{ top_holdings }}
- top10_weight: {{ top10_weight }}
- exposure_purity: {{ exposure_purity }}
- inferred_vs_confirmed: {{ inferred_vs_confirmed }}
- constituent_transmission: {{ constituent_transmission }}
- liquidity_sensitivity: {{ liquidity_sensitivity }}

## 管理与权重机制

- management_mode: {{ management_mode }}
- weighting_mode: {{ weighting_mode }}
- rebalance_frequency: {{ rebalance_frequency }}
- single_name_cap: {{ single_name_cap }}
- sector_country_caps: {{ sector_country_caps }}
- derivative_usage: {{ derivative_usage }}
- turnover_expectation: {{ turnover_expectation }}
- index_or_manager_discretion: {{ index_or_manager_discretion }}
- practical_readthrough: {{ weighting_practical_readthrough }}

## 同类产品对比

{{ peer_and_category_comparison }}

## Bull 解读

{{ bull_interpretation }}

## Bear 解读

{{ bear_interpretation }}

## 实战读法

{{ practical_trade_readthrough }}

## 上市后跟踪

这部分用于复盘首轮判断，不作为新 ETF 首轮结论成立的前置条件。

- aum_and_flow: {{ aum_and_flow_tracking }}
- liquidity_quality: {{ liquidity_quality_tracking }}
- holdings_confirmation: {{ holdings_confirmation_tracking }}
- peer_cannibalization: {{ peer_cannibalization_tracking }}
- narrative_confirmation: {{ narrative_confirmation_tracking }}

## 证伪条件

{{ falsification_conditions }}

## 证据记录

{{ evidence_log_notes }}
