# Football Model Bet Accounting

**Status:** ACTIVE AUDIT / MODEL-ACCOUNTING CONVENTION  
**Current active roster:** Football C + Football C2  
**Historical compatibility:** C3/C4 may be settled only from genuinely frozen historical rows using explicit historical-roster mode.

## 1. Purpose

This procedure defines deterministic model-performance accounting. It is separate from actual user execution and separate from official Website Pick authority.

Current new accounting uses only:
- Football C;
- Football C2.

C is official. C2 is shadow-only.

Historical C3/C4 records remain immutable and may still be settled when their original frozen state exists. They are never required in a new/current accounting payload.

## 2. Accounting priority

Per model / fixture / frozen epoch:

`DIRECT BET > COUNTABLE WAIT > WATCH > NONE`

Only one accounting entry is active per model/fixture under this precedence.

A later Step-2 PASS does not erase an independently frozen WATCH accounting entry unless a higher-priority direct/WAIT entry replaces it.

## 3. WATCH accounting

Every prospectively frozen current:
- `C-WATCH`;
- `C2-WATCH`;

is a model-accounting bet at:
- that model's own supported line;
- assumed odds = **1.65**;
- stake = **1.0u**.

Accounting basis:
- C -> `WATCH_ASSUMED`;
- C2 -> `SHADOW_WATCH_ASSUMED`.

WATCH accounting does not itself create a Website Pick.

Only Football C may ever create official exposure.

## 4. WAIT accounting

For current C/C2 Step-2 actions:
- use that model's own deterministic WAIT target line;
- use that model's own minimum odds;
- use the frozen WAIT resolution state.

Football C:
- default countable basis = `WAIT_ASSUMED`;
- user-confirmed matching execution may become `WAIT_USER_CONFIRMED`;
- explicit user declaration that the target never reached removes the WAIT layer under `WAIT_NOT_REACHED`.

Football C2:
- shadow WAIT basis = `SHADOW_WAIT_ASSUMED`;
- it never creates official exposure.

A valid WAIT replaces WATCH for accounting priority when the WAIT is countable.

If a WAIT is explicitly declared not reached, the lower-priority WATCH may remain countable if it was prospectively frozen.

## 5. Direct BET accounting

For current direct BET:
- use exact frozen/revalidated line;
- use exact frozen/revalidated odds;
- use frozen stake.

Basis:
- C -> `DIRECT_BET`;
- C2 -> `SHADOW_DIRECT_BET`.

Only C direct BET may create official exposure / Website Pick.

## 6. Settlement

Use regulation-time goals unless the original market explicitly included extra time.

Quarter-line settlement must be exact.

Examples at 1u stake:
- O2.25 with 2 goals -> HALF LOSS;
- O2.75 with 3 goals -> HALF WIN;
- O3.0 with 3 goals -> PUSH;
- O2.0 with 2 goals -> PUSH.

Do not flatten quarter-line settlement into a full WIN/LOSS.

## 7. Current deterministic payload

For new/current accounting, the payload must contain **exactly C and C2**.

Run:

`python models/football/engine/model_bet_accounting_cli.py --input <model_accounting.json>`

or under XI portable runtime:

`python xi_portable.py accounting --input <model_accounting.json>`

Expected current result roster:

`ACTIVE_C_C2`

A current payload containing retired-model rows is invalid:

`active accounting permits C/C2 only`

C2 missing from a current completed active-roster assessment is an incomplete workflow state, not a C2 PASS.

## 8. Historical accounting mode

Historical C3/C4 settlement is allowed only when:
- the record was prospectively frozen during the model's active era;
- its own supported line/action/accounting basis exists;
- no FT/current information is used to reconstruct missing prospective state.

Set:

`historical_roster = true`

Historical mode expects the historical roster defined by the deterministic accounting compiler.

Expected result roster:

`HISTORICAL_C_C2_C3_C4`

This mode exists only to preserve old audit history. It must not be used for a new/current decision.

## 9. Official model P/L vs actual user P/L

These are separate.

Official C model P/L comes from the model-accounting/official exposure convention.

Actual user P/L comes only from physical execution evidence such as:
- user bet slip;
- explicit user-confirmed exact execution.

A model bet can exist without a user bet.

A user bet at different line/odds/stake does not retroactively change the frozen model decision.

## 10. Persistence

For new/current rows persist:
- C Model Accounting;
- C2 Shadow Accounting;
- active accounting result JSON;
- Model Accounting Revision.

Current Decision State aggregate field may retain its historical name `All Model Accounting Result`, but for new rows it contains the active C+C2 result only.

Historical C3/C4 accounting fields may remain populated on old rows and must not be deleted.

Do not populate new C3/C4 accounting fields in current production.

## 11. Website Pick boundary

Website Picks are official Football C exposure only.

C2:
- never creates a Website Pick;
- never creates real exposure;
- remains shadow accounting only.

WATCH accounting is model-performance accounting and does not create official exposure.

WAIT official-exposure behavior for Football C follows:

`models/football/procedures/FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`

## 12. Audit reporting

Current forward model comparison should report:
- C official model P/L;
- C2 shadow model P/L only where frozen executable accounting terms exist;
- actual user P/L separately.

Do not:
- treat incomplete C2 rows as PASS;
- manufacture C2 odds from C;
- reconstruct missing C2 actions after FT;
- combine current C+C2 metrics with historical C3/C4 into one current leaderboard.

Historical retired-model results may be reported in a separate explicitly historical appendix.
