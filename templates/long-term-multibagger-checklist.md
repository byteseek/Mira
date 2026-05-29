# Long-Term Multibagger Checklist

- company_name: {{ company_name }}
- ticker: {{ ticker }}
- market: {{ market }}
- research_cutoff_date: {{ research_cutoff_date }}
- horizon_bucket: long_term_thesis
- selected_framework: {{ selected_framework }}
- selected_lenses: long-term-multibagger
- stale_after: {{ stale_after }}
- not_investment_advice: true

## Target Return Path

- target_multiple: {{ target_multiple }}
- target_years: {{ target_years }}
- implied_cagr: {{ implied_cagr }}
- required_revenue_outcome: {{ required_revenue_outcome }}
- required_margin_or_fcf_outcome: {{ required_margin_or_fcf_outcome }}
- required_valuation_outcome: {{ required_valuation_outcome }}
- dividend_or_buyback_contribution: {{ dividend_or_buyback_contribution }}

## Business Compounding Engine

- market_expansion: {{ market_expansion }}
- current_penetration: {{ current_penetration }}
- right_to_win: {{ right_to_win }}
- reinvestment_runway: {{ reinvestment_runway }}
- operating_leverage: {{ operating_leverage }}
- capital_intensity: {{ capital_intensity }}
- unit_economics: {{ unit_economics }}

## Shareholder Return Path

- current_valuation: {{ current_valuation }}
- valuation_tolerance: {{ valuation_tolerance }}
- dilution_risk: {{ dilution_risk }}
- balance_sheet_survivability: {{ balance_sheet_survivability }}
- capital_allocation_quality: {{ capital_allocation_quality }}
- position_sizing_implication: {{ position_sizing_implication }}

## Evidence Ladder

| Level | Evidence | Current Status | Source Trail | Upgrade Trigger | Downgrade Trigger |
| --- | --- | --- | --- | --- | --- |
| weak_signal | {{ weak_signal }} | {{ weak_signal_status }} | {{ weak_signal_sources }} | {{ weak_signal_upgrade }} | {{ weak_signal_downgrade }} |
| operating_confirmation | {{ operating_confirmation }} | {{ operating_confirmation_status }} | {{ operating_confirmation_sources }} | {{ operating_confirmation_upgrade }} | {{ operating_confirmation_downgrade }} |
| financial_confirmation | {{ financial_confirmation }} | {{ financial_confirmation_status }} | {{ financial_confirmation_sources }} | {{ financial_confirmation_upgrade }} | {{ financial_confirmation_downgrade }} |
| external_confirmation | {{ external_confirmation }} | {{ external_confirmation_status }} | {{ external_confirmation_sources }} | {{ external_confirmation_upgrade }} | {{ external_confirmation_downgrade }} |

## Kill Criteria

- thesis_break: {{ thesis_break }}
- financing_or_dilution_break: {{ financing_or_dilution_break }}
- competition_break: {{ competition_break }}
- market_size_break: {{ market_size_break }}
- valuation_break: {{ valuation_break }}
- management_or_governance_break: {{ management_or_governance_break }}

## Must Refresh If

{{ must_refresh_if }}
