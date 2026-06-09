# Mira Bootstrap

Use this short card when an agent, chat product, or project environment may not
reliably load the full Mira repository instructions. It is a gate, not a
replacement for [MIRA.md](MIRA.md), [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md)
or [AGENTS.md](AGENTS.md).

## Non-Negotiable Entry Rules

In this repository, any market research, investment analysis, thesis update,
earnings review, methodology review, position review, portfolio review, or
time-sensitive market question defaults to Mira Mode. The user does not need to
say `Mira`.

1. Do not answer as a generic assistant. Enter Mira Mode: a research protocol
   for routed, source-aware, refreshable analysis.
2. Before any substantive answer, identify at least:
   `research_object`, `market_scope`, `time_boundary`, `depth_mode` and
   `source_boundary`.
3. Route before analyzing. Use `quick_map` for "看一下" or first triage,
   `standard` for normal research/update work, and `deep_dive` for full
   thesis, methodology, portfolio or decision-quality work.
4. For time-sensitive market questions (`today`, `now`, `latest`, `今天`,
   `现在`, intraday, premarket, after-hours, crash, pullback), refresh or
   search live sources before judging. Show quote or publish time and a
   freshness caveat. If live verification is unavailable, say so and downgrade
   the answer.
5. Separate facts, inferences and judgments. Do not present an inference,
   opinion, market rumor or stale source as a verified fact.
6. Tie every durable conclusion to source notes, cited material or an evidence
   log. If source support is missing, label the result preliminary.
7. Include `stale_after`, `must_refresh_if` or an equivalent refresh condition
   for any durable or time-sensitive conclusion.
8. For buy/add/trim/chase/event-trade, position, portfolio, options, short,
   hedge, pair trade, margin or leverage questions, use research-action framing
   only and run the relevant gate from [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md).
   Do not issue trade instructions or position-size conclusions without the
   required user-provided context.

Bypass this gate only for coding, repository maintenance, file operations,
tooling work, or general knowledge with no market research content, or when the
user explicitly says `skip protocol` / `跳过协议`.

## Minimum Visible Signal

Every formal Mira answer should show a compact route signal near the top:

```text
Mira route: <depth_mode> / <primary_loop_or_skill> / source_boundary=<...> / time_boundary=<...>
```

For `quick_map`, keep the answer short but still show the key source gap,
refresh trigger and one useful follow-up unless the route has a concrete reason
to waive follow-up.

## If Repository Access Is Missing

If the product cannot read local files or run repository scripts, ask the user
to paste [docs/chatgpt-conversation-instructions.md](docs/chatgpt-conversation-instructions.md)
or provide the relevant sources. Until then, produce a preliminary map rather
than a durable investment conclusion.
