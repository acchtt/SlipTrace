# SlipTrace Football DeepEval QA

This directory is the executable regression layer for the football model.

It is **QA only**: adding or changing tests here does not alter
`models/football/CURRENT_MODEL.md`, model rules, execution procedures, launchers,
or any historical decision.

## Layers

### Layer A — deterministic DeepEval contracts

Runs automatically in GitHub Actions and needs no LLM API key.

It currently protects hard workflow invariants such as:

- no opportunistic official live exposure without a predeclared plan/exception;
- no ordinary prematch official lock before the mandatory post-XI research gate;
- no live-decay execution when state integrity is damaged;
- frozen historical-corpus privacy and hindsight separation.

Local run:

```bash
python -m pip install -r models/football/qa/deepeval/requirements.txt
deepeval test run models/football/qa/deepeval/tests
python models/football/qa/deepeval/historical_audit.py --summary --fail-on-blocking
```

### Layer B — frozen historical corpus

`cases/historical_2026-09-24_to_2026-09-29.json` is a sanitized snapshot of real
Football A Decision States joined to the closest frozen Daily Coverage/PRE row.

Snapshot properties:

- 99 real assessment states;
- 96 retain enough decision-time evidence for semantic QA;
- 13 have a settled outcome label kept in a separate `audit_outcome` object;
- actual betslip-audit rows are excluded;
- cash amounts, ticket identifiers and long external IDs are not retained;
- appended FT/settlement text is removed from `decision.decision_evidence`;
- an Airtable score field overwritten by a later FT value is excluded from judge
  input unless the original score is explicitly recoverable from the preserved
  pre-result evidence;
- a case whose original reasoning was overwritten by settlement text is marked
  `semantic_eligible=false` instead of reconstructing the missing decision with hindsight.

Historical findings are split into:

- `BLOCKING_*` — privacy/hindsight/corpus integrity faults; CI fails;
- `SIGNAL_*` — historical workflow QA signals; reported but do not rewrite the
  original verdict or automatically fail CI.

This distinction is deliberate: old decisions stay bound to the authority that
actually produced them.

### Layer C — semantic G-Eval judge

`run_semantic.py` evaluates decision-time reasoning with DeepEval `GEval`.

The judge can assess:

- evidence ↔ verdict consistency;
- live-plan adherence;
- H2H discipline;
- XI mechanism reasoning.

**Final scores and settlement outcomes are never included in the judge input.**
The semantic layer is manual because it consumes an external model API.

Local run after configuring `OPENAI_API_KEY`:

```bash
python models/football/qa/deepeval/run_semantic.py --limit 12
```

Optional judge model:

```bash
set DEEPEVAL_JUDGE_MODEL=<model-name>
```

GitHub also contains the manually triggered
`Football DeepEval Semantic QA` workflow. It requires an
`OPENAI_API_KEY` repository secret. The ordinary deterministic QA workflow
does not need any secret.

## Historical audit policy

Do **not** rewrite old decisions to make them conform to the current model.
The corpus exists to answer questions such as:

- did the process follow the authority active at the time?
- where do HOLD/PASS decisions and executable plans fail in different ways?
- did a later model change fix a process failure without introducing another?
- does a challenger improve decision quality on a frozen opportunity universe?

A final score is an audit label, never a decision-time feature.

## Adding future cases

For each imported historical case preserve, when available:

- Board ID / match identity / kickoff;
- model version and assessment timestamp;
- frozen PRE state and supported burden;
- H2H state used at that time;
- confirmed XI state;
- supplied market line/price and quote epoch;
- post-XI research status;
- market-history/current-market state;
- predeclared plan and target;
- live score/minute/card/injury state when applicable;
- original verdict/output.

Store the final settlement separately from decision-time evidence.
