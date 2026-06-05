# Mira Behavior Evals

This is where Mira eats its own cooking.

Mira demands a lot of every user thesis: separate facts from judgments, downgrade
weak evidence, run a disconfirmation under decision pressure, return an honest
`irreducible_uncertainty` instead of a fake point call, never size a position
without holdings. Until now those demands were *asserted* by the contract and
checked only at the syntactic layer. This harness makes them *measured*.

## What this is (and is not)

| layer | tool | question it answers |
| --- | --- | --- |
| syntax / routing tokens | `scripts/validate_repo.py` | Are tokens in-vocabulary? Are headers canonical? Are the golden routing cards correct? |
| **behavior / judgment quality** | `scripts/score_behavior_eval.py` (this) | Given a prompt, did the model **actually do** what the contract demands? |

`validate_repo.py` can confirm a card emitted `decision_pressure: medium`. It
cannot confirm the model then *ran a real disconfirmation*. That gap — between
"emitted the token" and "did the thinking" — is exactly where a structured
output can become a more sophisticated confidence-laundering machine. This eval
is the regression test for that gap.

It operationalizes the semantic teeth of
[../templates/delivery-checklist.md](../templates/delivery-checklist.md) and the
routing stop rules in [../loops/analysis-routing.md](../loops/analysis-routing.md).
It also guards against the opposite failure: visible ceremony bloat. Short
answers should not expose the full internal routing state when
[../data/output-surface-matrix.md](../data/output-surface-matrix.md) says the
discipline can stay brief.
Progressive follow-up cases also check rung progression: standard and
decision-grade answers should not end with only refresh or data-hygiene
questions when a pricing variable, consensus proxy, falsification condition or
next route is available.

## Run it

```sh
# Score recorded transcripts (no API needed):
python3 scripts/score_behavior_eval.py --transcripts evals/transcripts

# See what a violation looks like (the demo-fail dir holds a deliberately bad answer):
python3 scripts/score_behavior_eval.py --transcripts evals/transcripts-demo-fail

# Generate fresh outputs with your own model CLI, then score them.
# {prompt} is substituted; if absent, the prompt is piped to stdin.
python3 scripts/score_behavior_eval.py \
    --command 'your-model-cli --flag {prompt}' \
    --save-transcripts evals/transcripts-run

# Machine-readable, and fail if any case lacks a transcript:
python3 scripts/score_behavior_eval.py --transcripts evals/transcripts --json --require-all
```

Exit code is non-zero when any `error`-severity case **fails**. A case with no
transcript is `MISSING` (reported, not failed) unless `--require-all`, so the
dataset can grow ahead of recorded outputs. Use `--report-only` to surface
results without failing a run.

## Case schema

Cases live in [behavior-eval-cases.jsonl](behavior-eval-cases.jsonl), one JSON
object per line (`#`-comment lines are ignored).

| field | meaning |
| --- | --- |
| `id` | unique; the transcript file is `<id>.md` or `<id>.txt` |
| `prompt` | the user prompt fed to the model |
| `behavior` | the behavior family being tested |
| `rationale` | why this is the correct behavior (human-readable) |
| `contract_refs` | pointers to the contract lines this enforces |
| `routing_tokens` | optional `field: value` tokens that must appear in the card |
| `must_contain_all` | list of groups; each group is OR alternatives; **all** groups must hit |
| `must_not_contain` | forbidden content (anti-sycophancy / no-trade guards) |
| `severity` | `error` (default, fails the run) or `warn` |

`must_contain_all` is an AND of ORs: `[["A","B"], ["C"]]` passes if the output
contains (A or B) **and** C.

`must_not_contain` entries are negation-guarded by default: a forbidden hit
immediately preceded by a negator (不/别/无需/避免/...) does not count, so the
forbidden phrase `建议加仓` is **not** tripped by `不建议加仓`. For strict
matching use an object form:

```json
{"text": "配置?\\s*\\d+\\s*%", "regex": true, "guard": false, "note": "concrete size"}
```

## Recording a transcript

1. Take a `prompt` from the dataset.
2. Run it through Mira (whichever agent/model you are validating).
3. Save the model's full reply to `evals/transcripts/<id>.md`.
4. Re-run the scorer.

Record which model produced the transcript in your commit message or a sibling
note — this eval measures a *model + contract* pair, and the result drifts as
either side changes. That drift is the point: it tells you when a contract edit
or a model upgrade quietly changed Mira's behavior.

## How this feeds the rest of the roadmap

This is step 1 of three. The pass/fail data it produces is the evidence for
step 2 (subtracting low-value ceremony from the contract without weakening real
discipline) and step 3 (hardening the data/calculation layer). Measure first,
then cut.

> not_investment_advice: true — prompts and transcripts here are routing/behavior
> fixtures, not investment recommendations.
