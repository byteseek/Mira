# Actionability Risk Control Policy

Mira can translate research into a participation frame, but it must not become
an autonomous trading system.

Use this policy whenever a user asks whether a research object is "buyable",
"can participate", "can add", "can chase", "can sell", "can trim", "can trade
around an event", or any similar actionability question. Before assigning a
participation posture, run
[marginal-buyer-payoff-bridge.md](marginal-buyer-payoff-bridge.md) to identify
the next marginal buyer or seller, payoff source, repricing trigger and
priced-in status. If the user asks about options, short selling, pair trades,
hedges or other instruments, also load
[instrument-strategy-gate.md](instrument-strategy-gate.md).

## Boundary

Actionability language is research-bound. It can describe:

- thesis quality versus price
- evidence required before stronger participation
- event risk and invalidation conditions
- qualitative participation posture
- follow-up and refresh triggers

It must not describe:

- executed orders
- exact share quantity
- exact portfolio weight without user-provided mandate and constraints
- autonomous stop, hedge, sell or buy instructions
- advice that bypasses a user's portfolio, tax, liquidity or risk process
- option, short-sale, hedge or derivative structures without the instrument
  gate when those tools are requested

If the user provides no holdings, weights, cost basis, mandate, risk budget or
liquidity constraint, keep the output at `research_only`,
`watchlist_only`, `starter_only`, `small_if_confirmed` or
`normal_only_after_confirmation` language.

Machine tokens can stay precise, but user-visible wording must not read like a
trade ticket or portfolio instruction. Prefer plain labels such as
`research_only`, `watchlist_only`, `participation_frame`,
`confirmation_required` and `no_position_data` in the visible answer. If an
internal token such as `starter_only`, `small_if_confirmed`,
`add_only_if_confirmed` or `normal_only_after_confirmation` is shown, explicitly
state that it is a research posture, not an instruction to buy, sell, add,
trim, size or rebalance.

## Participation Frame

A participation frame answers:

1. why participation is being considered
2. who the next marginal buyer or seller is
3. what payoff source or downside repricing source remains from here
4. what evidence is already confirmed
5. what evidence remains unconfirmed
6. what price, valuation or expectation burden is being accepted
7. what would invalidate the view
8. what must happen before the participation posture can strengthen

It is not a trade ticket.

## Participation Stage Gate

Before assigning a participation posture, separate the setup into one of three
research stages:

| stage | meaning | default posture |
| --- | --- | --- |
| `watch_only` | Interesting object, but evidence, valuation, pricing or timing is not strong enough for participation. | `watch_only` / `needs_refresh` |
| `left_side_candidate` | Participation is being considered before confirmation because the payoff may be asymmetric, but the reversal evidence is incomplete. | `starter_only` or `small_if_confirmed` only after the left-side check passes |
| `confirmed_participation` | The core confirmation variable has arrived and the remaining payoff source is still identifiable. | `normal_only_after_confirmation` only if other controls pass |

Do not let "worth watching" become "buyable" without crossing this gate. If the
object is only thematically attractive, down a lot, or owned by a high-quality
company, keep it at `watch_only` until the marginal buyer, payoff source,
valuation or expectation anchor, and invalidation path are all named.

When the setup is a `left_side_candidate`, complete the left-side evidence check
in [../templates/actionability-system/left-side-participation-check.md](../templates/actionability-system/left-side-participation-check.md)
or explicitly waive it with a downgrade. A left-side setup is not valid merely
because price has fallen. It must state:

- whether the drawdown is valuation compression, cycle pressure, sentiment /
  liquidity pressure, or thesis damage
- the reversal variable and observation window
- why the next marginal buyer has not acted yet
- whether further drawdown would strengthen the setup, leave it unchanged, or
  falsify the thesis
- the cost or opportunity-cost risk of waiting through the cycle

If these cannot be answered, keep the actionability label at `watch_only`,
`needs_refresh` or `research_only`.

## Default Controls

Use the controls below before issuing an actionability bridge or a quick
participation answer.

- `source_control`: Material claims need evidence logs or explicit source
  notes. If the source trail is weak, downgrade to `watch_only` or
  `needs_refresh`.
- `valuation_control`: If price, valuation or expected return matters, state a
  valuation anchor. If missing, downgrade actionability.
- `payoff_control`: If the next marginal buyer or seller, payoff source,
  repricing trigger or priced-in status cannot be stated, downgrade
  actionability.
- `event_control`: Before binary or near-term catalysts, default to
  `starter_only` or `watchlist_only` unless the user has provided explicit risk
  budget and confirms event-risk tolerance.
- `confirmation_control`: Adding or moving beyond starter exposure requires a
  named confirmation variable, not merely a lower price or emotional conviction.
- `path_fit_control`: If the thesis requires waiting through a business,
  commodity, product or market cycle, state the expected pain path, the evidence
  that justifies enduring it, and the alternative waiting condition. If the
  path cannot be held inside the stated horizon or risk context, downgrade to
  `watch_only`, `valuation_reset_watch` or `needs_refresh`.
- `invalidation_control`: Every participation frame needs thesis-level
  invalidation. Price drawdown can be a risk-control trigger, but should not be
  the only invalidation condition.
- `position_data_control`: Without position data, do not make position-size or
  portfolio-construction conclusions.
- `refresh_control`: If the view depends on a pending event, stale market data,
  guidance, estimates or filings, include `stale_after` and `must_refresh_if`.

## Starter Participation Rule

`starter_only` is appropriate when:

- the thesis is plausible or strong but the next catalyst can materially change
  the view
- valuation is not clearly cheap
- the user wants participation before confirmation
- evidence is sufficient for watch or discussion, but not enough for a full
  normal position review

When using `starter_only`, state the confirming evidence required before
upgrading to `normal_if_confirmed` or
`normal_only_after_confirmation`.

Do not treat a starter frame as a command to buy. Use wording such as "research
participation frame", "starter exposure review" or "small-if-confirmed posture".

## Event Participation

For earnings, regulatory decisions, product launches, macro releases and other
event-driven setups:

- define the event date or window
- state the expected variable
- state what result would be confirmatory, neutral or disconfirming
- avoid full participation posture before the event unless user-provided risk
  budget and constraints support it
- after the event, refresh before carrying forward the pre-event view

If the user asks for an impulsive entry, keep the answer honest:

- participation may be allowed at `starter_only`
- adding should wait for confirmation or a reset
- averaging down is not a default response to failed evidence
- price-only stop language must be secondary to thesis invalidation

## Token Mapping

Use existing controlled vocabulary. Do not invent machine-facing action tokens.

| situation | preferred token |
| --- | --- |
| interesting but not actionable | `watch_only` |
| stale or source-gapped | `needs_refresh` |
| event setup with limited participation | `event_setup` + `starter_only` |
| participation only after evidence arrives | `add_only_if_confirmed` or `normal_only_after_confirmation` |
| position appears too large for evidence | `risk_cap_review` or `too_large_for_evidence` |
| no real position context | `research_only` or `no_position_data` |
| no further action | `no_action` |

## Minimum Output

For a quick participation answer, include:

- `research_object`
- `time_boundary`
- `marginal_buyer_or_seller`
- `payoff_source`
- `repricing_trigger`
- `priced_in_status`
- `participation_posture`
- `basis`
- `confirmation_required`
- `invalidation`
- `participation_stage`
- `path_fit`
- `refresh_condition`
- `action_boundary`

For a formal thesis-system output, include the above inside
`actionability-bridge.md` and tie material claims to the evidence log.

If the user explicitly asks for a structure, attach an instrument route using
[../templates/actionability-system/instrument-strategy-gate.md](../templates/actionability-system/instrument-strategy-gate.md).
