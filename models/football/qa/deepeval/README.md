# SlipTrace Football DeepEval QA

This directory is the executable regression layer for the football model.
It is **QA only**: adding or changing tests here does not alter
`models/football/CURRENT_MODEL.md`, model rules, execution procedures, or any
historical decision.

## Why this exists

The existing Football Model QA procedure governs whether a challenger earns
promotion. DeepEval adds repeatable executable checks so workflow regressions
can be caught before a candidate rule or procedure is promoted.

Phase 1 intentionally starts with deterministic process contracts. These run
without an LLM judge and therefore without an API key. They are implemented as
a custom DeepEval metric, not as ad-hoc shell assertions.

Initial protected invariants:

1. no opportunistic official live exposure without a predeclared plan or active
   match-specific exception;
2. no ordinary prematch official lock when the mandatory post-XI football
   research gate has not been satisfied;
3. no live-decay execution when state integrity is materially damaged.

These are harness seed cases, not evidence that the predictive model is good.
They exist to prove that the QA machinery rejects known workflow violations.

## Local run

From the repository root:

```bash
python -m pip install -r models/football/qa/deepeval/requirements.txt
deepeval test run models/football/qa/deepeval/tests
```

The dependency is pinned to DeepEval 4.2.6 so CI and local runs use the same
metric/test-case API.

## Case format

Saved cases use a DeepEval `LLMTestCase` plus a deterministic contract stored in
`metadata.contract`.

Supported checks:

- `required_all`: every phrase must appear;
- `forbidden_any`: none of the phrases may appear;
- `required_any`: each group requires at least one member;
- `required_regex`: every regex must match;
- `forbidden_regex`: no regex may match.

Checks are case-insensitive. Phrase checks normalize whitespace.

## Next phase: historical regression dataset

Do **not** rewrite old decisions to match the current model. Each imported case
must retain the original information clock and model/version that produced it.
For a real historical regression case, preserve at minimum:

- Board ID / match identity / kickoff;
- model version and commit;
- frozen PRE state and supported burden;
- H2H state used at that time;
- confirmed XI state when applicable;
- supplied market line/price and quote timestamp;
- post-XI research status;
- market-history/current-market state;
- predeclared plan and target, if any;
- score/minute/red-card/injury state for live epochs;
- original model output/verdict;
- final settlement separately from the decision-time evidence.

The final score is an audit label, not an input to the decision-time model.

## Planned metric layers

### Layer A — deterministic process contracts

Hard invariants such as gates, required fields, forbidden state transitions,
no-hindsight constraints, and persistence/output schema. These should fail CI.

### Layer B — semantic DeepEval judge metrics

Later, add `GEval`/custom judge criteria for evidence-verdict consistency,
quality of H2H interpretation, XI mechanism reasoning, market conflict
resolution, and whether the explanation actually supports the stated plan.
These require a configured judge model and should initially report separately
from the deterministic gate.

### Layer C — outcome/decision analytics

Champion-vs-challenger coverage, yield/settlement deltas, drawdown, route and
regime stability, decay-target reachability, and paired decision differences.
These remain governed by `FOOTBALL_MODEL_QA_AND_PROMOTION.md`; DeepEval does not
turn a small retrospective sample into promotion evidence.
