# Football Audit Hindsight Integrity

**Status:** mandatory post-slate audit contract  
**Scope:** Football C official, Football C2 shadow, engine comparison, and historical version-faithful audits  
**Purpose:** prevent outcome knowledge from rewriting frozen football judgments or exposure semantics.

## 1. Three-layer audit record

Every audited fixture must keep three layers separate.

### A. FROZEN STATE — immutable

Copy the exact prospectively frozen values. Never edit them after HT/FT:

- C board state and rank;
- FOLLOW / RESERVE / STOP lane;
- C supported line;
- C2 state/rank/supported line when valid;
- home/away route grades;
- carrier state;
- completion mode;
- burden-completion quality;
- continuation quality;
- opponent leakage;
- burden stall risk;
- failure mode / suppression state;
- H2H state;
- tournament-incentive state;
- Step-2 C action and exact quote;
- C2 shadow action and exact quote where applicable;
- engine outputs.

Canonical enum vocabulary is exact:
- grades: `LOW / MEDIUM / HIGH`;
- routes: `WEAK / USABLE / STRONG`;
- completion modes: `NONE / TWO_SIDED / CARRIER_LED / FORCED_CHAOS / MIXED`.

Do not invent compound grades such as:
- `MEDIUM-HIGH`;
- `LOW-MEDIUM`;
- `HIGH+`;
- `STRONG-ish`.

If a historical model used another explicit enum, preserve that historical enum exactly.

### B. OBSERVED OUTCOME — descriptive, not a re-grade

Record what actually happened:

- HT / FT score;
- goal timing when known;
- settlement of the exact recorded line/odds;
- whether the frozen completion path materialized;
- whether continuation materialized after key score states;
- whether the carrier self-funded;
- whether the opponent route produced;
- whether a stall scoreline occurred.

Examples:

`OBSERVED: 2-0 HT -> 2-0 FT; no further goal after the two-goal cushion.`

`OBSERVED: frozen CARRIER_LED path cleared through a 3-0 carrier output.`

Do not convert observed outcome into a new retrospective grade.

Wrong:
`Continuation should have been MEDIUM.`

Correct:
`Frozen continuation = HIGH; observed continuation did not materialize after 2-0.`

### C. AUDIT DIAGNOSIS — evidence-bounded

Classify what the outcome means without rewriting the frozen state.

Allowed diagnosis classes:

- `MODEL FALSE POSITIVE` — prospectively selected/supportive thesis failed;
- `MODEL FALSE NEGATIVE` — prospectively rejected thesis later cleared;
- `FOLLOW PRIORITY MISS` — same-block ordering/lane allocation was prospectively inferior;
- `PROCESS MISS` — mandatory evidence/gate/procedure was absent or violated;
- `EXECUTION MISS` — decision was valid but execution/persistence/price handling failed;
- `OPERATIONAL OPPORTUNITY COST` — STOP/deferred match later cleared;
- `NO OFFICIAL EXPOSURE` — assessment existed but no official C exposure;
- `NO RETROSPECTIVE MODEL CHANGE` — outcome is informative but does not prove a prospectively detectable model error.

A more specific existing integrity tag such as `TOURNAMENT INCENTIVE MISS` may accompany these.

## 2. When may an audit say the original read was wrong?

Only when the audit can point to **contemporaneous evidence available before the freeze** that was:

- omitted;
- misread;
- contradicted by the frozen grade;
- or handled contrary to the active model rules.

Required format:

`PRE-FREEZE EVIDENCE MISS — <specific frozen/pre-freeze evidence> -> <specific rule/grade conflict>`

The eventual FT result alone is never proof that a frozen grade "should have been" different.

If the diagnosis depends mainly on FT/HT knowledge:

`RETROSPECTIVE HYPOTHESIS ONLY — DO NOT RE-GRADE HISTORICAL STATE`

This hypothesis may motivate a prospective observer/new model patch, but it cannot rewrite the audited fixture.

## 3. Mechanism claims after kickoff

Scoreline alone does not prove why a team stopped attacking, why a route disappeared, or what tactical intent changed.

Statements such as:
- "they had no reason to keep forcing";
- "the second route disappeared";
- "the favorite shut the game down";

require contemporaneous live/event/stat/tactical evidence if presented as mechanism facts.

Without such evidence, use descriptive language:

`The score path ended 2-0; the frozen continuation thesis did not materialize.`

Do not invent causal match narratives from the final score.

## 4. Exposure and P/L separation

Keep three concepts distinct.

### Model decision

A persisted `C-BET` is an official Football C decision.

### Official Football C exposure / model P&L

Count official C model P&L only when an official C-BET was successfully published/reconciled as an official Website Pick/exposure record with exact line/odds.

User personal execution is **not required** for model P&L once official model exposure exists.

If a C-BET exists but official publication/exposure failed:

`OFFICIAL C DECISION — NO OFFICIAL EXPOSURE / NO MODEL P&L`

### Actual user P&L

Count only exact user bet-slip execution.

A user may:
- not place an official C pick;
- place a different line/odds;
- place a non-official bet.

Therefore:
`OFFICIAL C MODEL P&L != ACTUAL USER P&L`

Never use "the user did not bet" to erase an already-published official model loss/win.

Never assign official model P&L to:
- C-PASS;
- unexecuted C-WAIT;
- C2 shadow;
- counterfactual lines;
- assessment-only cases.

## 5. Required fixture audit format

For every material audited fixture use:

`FROZEN:`
- model/version;
- board state/rank/lane;
- exact supported line;
- exact completion/continuation/stall grades;
- exact Step-2 action/quote when any.

`OBSERVED:`
- HT/FT;
- exact settlement if an official exposure existed;
- which frozen completion/continuation claim materialized or failed to materialize.

`DIAGNOSIS:`
- one or more canonical diagnosis tags;
- prospectively detectable evidence miss, if proven;
- otherwise `RETROSPECTIVE HYPOTHESIS ONLY`.

`P&L STATUS:`
- official C model exposure/P&L;
- actual user execution/P&L;
- C2 shadow separately.

## 6. Example — 2-0 stall

Do not write:

`Continuation was MEDIUM-HIGH and should have been MEDIUM; the second route failed, so the pre-match read was wrong.`

Write:

`FROZEN: continuation=HIGH, stall risk=LOW, supported line=O2.5.`

`OBSERVED: 2-0 HT -> 2-0 FT; no third goal; the frozen continuation path did not materialize.`

Then choose one:

- if contemporaneous pre-freeze evidence clearly contradicted HIGH continuation:
  `DIAGNOSIS: MODEL FALSE POSITIVE + PRE-FREEZE EVIDENCE MISS — <evidence>.`

- otherwise:
  `DIAGNOSIS: MODEL FALSE POSITIVE; RETROSPECTIVE HYPOTHESIS ONLY — possible two-goal control/stall mechanism for future prospective testing.`

The second form is the default when only outcome information reveals the failure.

## 7. No-backfill rule

Never overwrite Airtable frozen Step-1/Step-2 fields because of an audit.

Any new audit hypothesis belongs in:
- audit notes;
- a prospective observer;
- a challenger/new version;
- or a separately versioned model patch.

Historical state remains immutable.
