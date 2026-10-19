# Football C — full rule consistency audit

**Audit date:** 2026-10-19 ICT  
**Scope:** active Football C model/routing/runtime plus legacy files that could be mistaken for active authority  
**Implementation branch:** `repair/wait-reachability-rule-audit-20261019`

## Executive result

The audit found one active runtime defect and several authority-drift defects.

The runtime defect was WAIT reachability: a caller-provided
`wait_reachable=true` could permit C to wait from a materially higher
unsupported market line down to a much lower certified burden. This could turn a
0.50–1.50 goal disagreement into an unrealistic decay plan.

Authority drift was concentrated in old documentation that still described
pre-V4 caps, paired C+C2 execution, Airtable persistence, synthetic WATCH/WAIT
accounting and an older ranking order.

These defects are repaired on this branch without changing Football C goal
certificate thresholds.

## Repairs applied

### 1. WAIT reachability

Active C now enforces:

- unsupported higher line gap <=0.25: WAIT may remain possible when all other
  reachability/football conditions are satisfied;
- unsupported higher line gap >=0.50: complete the market-disagreement football
  recheck, then either fund/evaluate the observed burden or PASS;
- no far-lower pre-goal decay target can be manufactured by setting
  `wait_reachable=true`.

The material market-disagreement trigger remains 0.50. The new WAIT invariant
therefore aligns execution with the existing recheck boundary.

### 2. Production spec consolidation

`production/FOOTBALL_C.md` was reduced to current Football C semantics only.

Removed stale active claims included:

- 15-fixture normal Work admission cap;
- old AiScore-senior-universe flow;
- old ranking comparator;
- synthetic C-WATCH model-accounting exposure;
- WAIT assumed-exposure accounting;
- legacy Website Pick WAIT exposure;
- paired/retired-model operational language.

Current routing/stage/persistence mechanics now remain in their canonical files
instead of being redefined inside the model spec.

### 3. V4 README repair

`stages_v4/README.md` previously contained active-looking C+C2, Airtable and
legacy rank examples. It now describes only the current C-only V4 path and
points to `SWEEP.md`, `RANK.md` and `stage.py` for executable detail.

### 4. Legacy-procedure retirement

The following stale procedure files now carry a hard first-line retirement
banner so internal historical `Status: ACTIVE` text cannot be mistaken for
current authority:

- `FOOTBALL_MATCH_SWEEP_AND_RESEARCH_PROCEDURE.md`
- `FOOTBALL_COMPACT_SWEEP_WORK_BUDGET.md`
- `FOOTBALL_CAPACITY_REPLENISHMENT.md`
- `FOOTBALL_OPERATIONAL_VIABILITY_GATE.md`
- `FOOTBALL_PRE_DECISION_SPEC.md`
- `FOOTBALL_STEP2_EXECUTION_SPEC.md`
- `FOOTBALL_XI_MARKET_FIRST_INTAKE.md`

Historical receipts remain immutable.

### 5. Market-history scope

The market-history procedure is now C-only and applies to strict authorized
non-screenshot execution context. USER_SCREENSHOT_ONLY comparisons do not
search replacement/current odds or historical bookmaker prices merely to fill a
legacy field.

### 6. Semantic basis

The active semantic-decision contract is now Football C only. It also states
that prose cannot make a 0.50+ unsupported line gap reachable.

### 7. Active-adapter C2 test drift

An obsolete adapter test still expected a new C2 WAIT decision even though the
active adapter already rejects every non-C model. It now verifies retirement
instead.

## Consistency checks — no defect found

### Goal certificate mapping

Runtime and active docs agree:

- G3 -> O2.50
- G4 -> O3.50
- G5 -> O4.50
- G6 -> O5.50

No threshold was changed.

### G4 evidence state

Adapter, G4 evidence contract and V4 rank agree on the expanded states:
INCOMPLETE, EVIDENCE_LIMITED, COMPLETE_MIXED, COMPLETE_REJECTED,
COMPLETE_FUNDED and NOT_APPLICABLE.

V4 rank checkpoints G3-funded C-FOCUS rows whose G4 research is INCOMPLETE or
EVIDENCE_LIMITED.

### Ranking

Runtime and active rank docs agree on:

1. certificate robustness;
2. certificate depth;
3. endpoint/control risk;
4. frozen V4 goal signal;
5. remaining football-mechanism quality.

No price enters the ranking key.

### Operational lanes

FOCUS/WATCH/PASS remains predictive selection. FOLLOW/RESERVE/STOP remains an
operational workload lane. V4 has no fixed official board-size cap.

### Market disagreement

The active material disagreement threshold remains 0.50 goals. Market movement
triggers football reinspection only and cannot manufacture a certificate.

### Tournament incentive

Step 1 may keep an otherwise eligible tournament fixture visible with explicit
unresolved incentive fields. Step 2 requires the applicable incentive state to
be VERIFIED before final BET/WAIT/PASS authorization. No positive-pressure
effect may be invented from missing information.

### Screenshot authority

USER_SCREENSHOT_ONLY remains exact supplied quote authority. No replacement
odds search, inferred price or retiming is allowed.

### Accounting

Active accounting remains:

- WATCH: no exposure;
- unresolved WAIT: no exposure;
- direct strict C BET: exact actual terms;
- reached WAIT: exposure only from confirmed reached terms;
- user P/L: Actual Bets — Current only.

Legacy WAIT_ASSUMED parsing remains solely so frozen historical records stay
readable.

### Live boundary

Started fixtures continue football assessment but cannot recreate a historical
prematch ACT/WAIT/PASS.

## Retained compatibility code

C2 helper functions remain in `engine/core.py` for historical regression and
frozen-record interpretation. They are not an active production route:
`engine/adapter.py` accepts only `model='c'`.

This was not deleted because removing historical compatibility would add audit
risk without reducing active decision ambiguity. The active router, adapter and
CI guard prevent it from becoming production authority.

## Rule-duplication policy after repair

Some concise rule summaries intentionally appear in the canonical launcher and
CURRENT_MODEL so an operator sees the required invariant at the point of use.
The executable source remains single-authority.

New CI checks prevent active production docs from reintroducing:

- the 15-fixture Work cap;
- synthetic WATCH accounting;
- assumed WAIT accounting;
- AiScore-only active flow;
- far-lower unsupported WAIT targets;
- non-retired status on the identified legacy procedures.

## Deliberately unchanged

This audit does **not** change:

- G3/G4/G5/G6 thresholds;
- G4 transferability/comparable-context rules;
- ranking weights/order;
- 0.50 market-disagreement threshold;
- 1.65 normal price floor;
- 1.60 supported-line soft zone;
- tournament-incentive semantics;
- screenshot-only odds authority;
- historical receipts or past decisions.
