# /audit — Football C lightweight audit

> **Normal chat role — AUDIT ONLY.** This conversation diagnoses the current
> Football C slate/incident from the smallest relevant set of frozen evidence.
> Load current SlipTrace authority before auditing. Do not execute a new
> /sweep, /rank, /xi or /live slate, and do not turn outcomes into retrospective
> decisions. This is the default audit route.

Football C is the only active model. C2/C3/C4 are historical audit material only.

## Default scope

Start narrow. Read only what is needed for the incident:

- the relevant sweep/rank receipt or coverage row;
- frozen C certificate/board state and G3/G4/G5/G6 fields;
- the actual /xi or WAIT/ACT/PASS evidence when material;
- user-supplied screenshot evidence when it was part of the original decision;
- current/final outcome only to classify process/model performance, never to
  manufacture prospective evidence.

Do not load the entire repository, all historical boards, or unrelated receipts
unless the defect itself requires that breadth.

## Diagnose separately

Classify findings into one or more of:

- SCREENING_MISS;
- SWEEP_HANDOFF_FAILURE;
- RANK_COVERAGE_FAILURE;
- RANKING_INVERSION;
- CERTIFICATE_FALSE_POSITIVE;
- CERTIFICATE_FALSE_NEGATIVE;
- G4_RESEARCH_COMPLETENESS_FAILURE;
- AVAILABILITY_EVIDENCE_ASYMMETRY;
- TOURNAMENT_INCENTIVE_FAILURE;
- UNREALISTIC_WAIT;
- EXECUTION_PROCESS_MISS;
- PERSISTENCE_OR_SOURCE_INTEGRITY;
- NO_OFFICIAL_EXPOSURE_OPPORTUNITY_COST.

A final score alone is never proof that a certificate was wrong. The audit must
identify what prospective evidence was or was not available before the decision.

## Normal-audit output

Keep the output compact:

1. affected fixture(s) / run;
2. defect class;
3. frozen prospective evidence;
4. what the model/workflow did;
5. why that was correct or incorrect prospectively;
6. user-visible impact;
7. recommended next action.

If the issue can be resolved from those records, stop there. Do not escalate
merely because the outcome was surprising or because one decision was wrong.

When the zero-authority calibration ledger is available, `/audit` must use its
universal denominator and report:

- ACT count and win/push/half-win/half-loss/loss, clear rate, average evaluated
  burden, and coverage;
- priced PASS count, correct rejects, false negatives/rate, and PASSes that had
  a lower supported visible screenshot line;
- GOAL_PRIORITY, GOAL_REVIEW, CONTROL_REVIEW, and terminal-negative counts,
  plus settled 3+/4+ outcomes by screen state;
- FOCUS versus REVIEW_ONLY 3+/4+, supported-burden reach, top-3/top-5
  clearability, certificate-depth and robustness distributions;
- exceptions as a separate list while retaining them in the universal ledger.

Outcome fields are appended only after settlement and have zero selection or
automatic-threshold-learning authority.

## Automatic deep-escalation rule

The user should not need to choose a deep audit. Emit `DEEP AUDIT REQUIRED`
only when at least one of these is true:

- the same defect pattern appears across multiple fixtures or slates;
- two current Football C authorities/launchers/runtimes conflict;
- source, persistence or runtime integrity cannot be resolved from the relevant
  receipts and targeted checks;
- a reliable repair requires repository-wide inspection, code modification or
  regression tests;
- the normal audit cannot distinguish a model defect from an implementation
  defect without inspecting code.

Do **not** perform the deep repository pass in normal chat after this threshold
is reached. Prepare the handoff instead.

## Compact deep-audit handoff

When escalation is required, end with exactly this logical payload:

- `status: DEEP AUDIT REQUIRED`
- `defect_class`
- `scope`: affected fixture/run IDs and time window
- `frozen_evidence`: only the decisive prospective facts/receipt references
- `observed_failure`
- `suspected_area`: named launcher/rule/runtime/persistence area when known
- `ruled_out`: causes already checked
- `questions_for_deep_audit`: the smallest exact questions to answer
- `recommended_tests`: specific regression cases, if already apparent
- `implementation_requested`: true only when the user has explicitly asked to
  apply/fix the defect

This handoff is the input to the Work-only
`models/football/prompts/04_WORK_POST_SLATE_AUDIT.md` route. The deep audit
should not need the entire normal-chat transcript.

## Historical integrity

Never rewrite a frozen rank, board, action, bet or screenshot price after the
fact. Audit opportunity cost separately from official exposure and physical P/L.
