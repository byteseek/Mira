# Long-Term Methodology Review

- task_mode: methodology_review
- research_object: long-term analysis methodology
- market_scope: public equity research across US, HK and A-share contexts unless a case narrows scope
- time_boundary: gt_1y, usually 3-5 year thesis formation and refresh
- research_cutoff_date: 2026-05-30
- as_of: 2026-05-30
- primary_skill_or_loop: loops/methodology-research-loop.md
- routing_basis: user asked to optimize Mira's long-term analysis method and explicitly approved external deep research before workflow design
- routing_mismatch_risk: source scan may overrepresent public institutional frameworks and underrepresent private buyside execution details
- expected_output_package: methodology-card.md, methodology-search-log.csv, methodology-review-log.csv, methodology-queue.csv
- created: 2026-05-30
- not_investment_advice: true

## Provisional Conclusion

The best design is not five separate workflows for consumer, product, economy, industry and company analysis. Mira should use one integrated `long-term-thesis` workflow with mandatory conflict checks across five lenses:

- `consumer_demand`
- `product_reality`
- `macro_economy`
- `industry_structure`
- `company_execution`

The external scan supports adding a sixth mandatory bridge:

- `valuation_expectations`

This bridge asks what the current market price already implies about the five long-term lenses. Without it, the workflow may identify a good long-term business but fail as an investment research process.

## Candidate Architecture

1. Define the research object and horizon.
2. Select relevant long-term lenses.
3. Build a fact / inference / judgment table for each lens.
4. Identify lens conflicts and dependency order.
5. Translate the operating thesis into ROIC, growth, cash-flow, balance-sheet and capital-allocation variables.
6. Reverse-engineer what the current price appears to require.
7. Write evidence ladder, refresh triggers and falsification conditions.

## Source Quality Note

This review emphasizes institutional, first-principles and practitioner sources with public pages that can be revisited. It is not enough for adoption. The workflow should enter `trial` and be tested against historical and live cases before moving to `adopted`.

## Source Trail

- CFA Institute, Industry and Competitive Analysis: https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/industry-and-competitive-analysis
- Harvard Business School, Porter Five Forces: https://www.isc.hbs.edu/strategy/business-strategy/Pages/the-five-forces.aspx
- BCG, Growth-Share Matrix: https://www.bcg.com/about/overview/our-history/growth-share-matrix
- McKinsey, Consumer Decision Journey: https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/the-consumer-decision-journey
- Harvard Business Review, Jobs to Be Done: https://hbr.org/2016/09/know-your-customers-jobs-to-be-done
- Silicon Valley Product Group, Product Discovery: https://www.svpg.com/product-discovery/
- Morgan Stanley / Mauboussin, Return on Invested Capital: https://www.morganstanley.com/im/en-us/individual-investor/insights/consilient-observer/return-on-invested-capital.html
- Expectations Investing: https://www.expectationsinvesting.com/about-expectations-investing
- Capital Group, Investment Philosophy: https://www.capitalgroup.com/individual-investors/ch/en/about-us/philosophy.html
- IMF, World Economic Outlook: https://www.imf.org/en/publications/weo
- World Bank, Global Economic Prospects: https://www.worldbank.org/en/publication/global-economic-prospects

## Refresh Conditions

- stale_after: 2026-08-30
- must_refresh_if: a live case shows the lens map adds process cost without improving conclusion quality; external high-quality buyside process notes are found; or at least two long-term cases reveal a recurring missing lens.
