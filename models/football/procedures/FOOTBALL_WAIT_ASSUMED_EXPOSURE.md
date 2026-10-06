# Football WAIT Assumed-Exposure Accounting

**Status:** ACTIVE C-WAIT OPERATIONAL PERSISTENCE COMPATIBILITY  
**Applies to:** C/C2 WAIT operational fields; active-model audit accounting is governed by `FOOTBALL_MODEL_BET_ACCOUNTING.md`  
**Predictive effect:** none — this does not change BET/WAIT/PASS selection logic

## 1. Purpose

Read first:
`models/football/procedures/FOOTBALL_MODEL_BET_ACCOUNTING.md`

This file preserves the existing C-WAIT Website Pick / Decision State mechanics. Active accounting additionally handles C2 WAITs and C/C2 WATCHs with one-accounting-bet precedence.

A Football C `C-WAIT` is a model instruction with a predeclared target line and minimum odds. For audit simplicity, an unresolved WAIT is treated as if that target entry was taken unless the user supplies stronger execution truth.

The frozen model decision remains `C-WAIT`. This procedure changes only exposure/accounting semantics.

## 2. Default WAIT accounting

Immediately when Football C issues a valid `C-WAIT`:

- preserve `C Action = C-WAIT`;
- freeze `WAIT Target Line`;
- freeze `WAIT Min Odds`;
- create provisional official model exposure at that exact target/minimum price;
- use flat stake `1.0u` unless the model record explicitly uses another stake;
- set:
  - `Exposure Basis = WAIT_ASSUMED`;
  - `WAIT Resolution = ASSUMED_REACHED`.

For model audit/P&L, this provisional exposure is treated exactly like a bet.

Do not wait for a later market observation to create model exposure.

## 3. Deterministic target/minimum price

For deterministic C/C2 engine output, a WAIT must expose:

- `wait_target_line`;
- `wait_min_odds`;
- accounting status.

The target line is:
- the current quoted line when it is already at/below the model-supported line but price is the blocker;
- otherwise the model-supported line.

The minimum odds are:
- `1.60` only when the existing top-ranked FOCUS soft-zone rule is eligible;
- otherwise `1.65`.

This compiles existing WAIT policy into accounting fields; it does not change when WAIT is selected.

## 4. User execution is stronger truth

If the user later supplies an actual bet slip and identifies it as the corresponding WAIT:

- preserve the original frozen WAIT target/minimum odds;
- set `Exposure Basis = WAIT_USER_CONFIRMED`;
- set `WAIT Resolution = USER_CONFIRMED`;
- store the exact actual line, odds and stake from the slip;
- use that exact actual execution for the reconciled official exposure/accounting line, odds and stake;
- actual user P/L also uses the slip.

A corresponding user bet may differ from the original WAIT target. Do not erase the original model target; retain both for audit.

## 5. Explicit line-never-reached override

Only an explicit user statement that the target line never reached may cancel the WAIT layer.

Under the active-model policy, removing a WAIT layer does not erase an independently frozen WATCH accounting bet for the same model/fixture.

When the user says the line never reached:

- preserve the original `C-WAIT` decision;
- set `Exposure Basis = WAIT_NOT_REACHED`;
- set `WAIT Resolution = USER_DECLARED_NOT_REACHED`;
- remove operational C-WAIT exposure/P&L and the WAIT accounting layer;
- keep the Website Pick/exposure record as an audit trail and settle it `VOID` / 0u where the persistence layer requires a record.

For audit language:

`WAIT NOT REACHED — USER DECLARED — NO WAIT LAYER`

If the frozen board state was C-WATCH, model accounting falls back to WATCH_ASSUMED at C supported line @1.65, 1u.

## 6. What does not cancel an assumed WAIT

Do **not** change `WAIT_ASSUMED` merely because:

- no user bet slip was supplied;
- the user did not mention the fixture again;
- a later market-history lookup cannot prove the target was available;
- a live screenshot shows a different line;
- the model did not re-check the target before kickoff;
- an audit cannot reconstruct full intraday line history;
- the user says they personally did not bet, without saying the target line never reached.

The default remains: **WAIT counted as model bet**.

## 7. Website Pick persistence

For current Football C:

### C-BET
Publish/reconcile one Website Pick:
- `Origin C Action = C-BET`;
- `Exposure Basis = DIRECT_BET`;
- `WAIT Resolution = NOT_APPLICABLE`;
- primary Line/Odds = exact direct bet quote.

### C-WAIT
Publish/reconcile one Website Pick immediately:
- `Origin C Action = C-WAIT`;
- `Exposure Basis = WAIT_ASSUMED`;
- `WAIT Resolution = ASSUMED_REACHED`;
- `WAIT Target Line` = frozen target;
- `WAIT Min Odds` = frozen minimum;
- primary Line/Odds = target/minimum;
- Result = `PENDING` until settled.

### C-PASS
No Website Pick.

If a corresponding user slip arrives, update the existing C-WAIT Website Pick instead of creating a duplicate.

If the user declares the line never reached, update that record to `WAIT_NOT_REACHED`, `USER_DECLARED_NOT_REACHED`, Result=`VOID`, P/L=0.

## 8. Decision State persistence

For Football C persist:

- `C Exposure Basis`;
- `C Exposure Line`;
- `C Exposure Odds`;
- `WAIT Resolution`;
- `WAIT Reconciliation Note`.

Mappings:

- C-BET -> `DIRECT_BET`, quote line/odds, `NOT_APPLICABLE`;
- C-WAIT -> `WAIT_ASSUMED`, target/minimum odds, `ASSUMED_REACHED`;
- C-PASS -> `NONE`, no exposure line/odds, `NOT_APPLICABLE`;
- user-confirmed WAIT -> `WAIT_USER_CONFIRMED`, actual line/odds, `USER_CONFIRMED`;
- user-declared never reached -> `WAIT_NOT_REACHED`, no active exposure, `USER_DECLARED_NOT_REACHED`.

## 9. Shadow WAIT accounting

C2 remains shadow-only and never creates Website Picks.

For model-comparison audit:
- C2-WAIT defaults to a shadow assumed bet at its deterministic target/minimum odds;
- settle them through `FOOTBALL_MODEL_BET_ACCOUNTING.md`;
- if the corresponding WAIT is explicitly declared not reached, remove the WAIT layer;
- if that model's board state was WATCH, the WATCH accounting bet remains;
- this never creates official exposure or user P/L.

## 10. Audit rule

For unresolved Football C WAITs, audit assumes official model exposure.

Default:

`C-WAIT -> WAIT_ASSUMED -> settle target line @ minimum odds`

Override only with:

`matching user slip -> WAIT_USER_CONFIRMED`

or:

`explicit user "line never reached" -> WAIT_NOT_REACHED -> REMOVE WAIT LAYER`

A frozen WATCH accounting bet, if any, remains under `FOOTBALL_MODEL_BET_ACCOUNTING.md`.

Actual user P/L remains separate from model P/L.

## 11. Historical records

Do not rewrite the frozen historical action.

For an earlier Football C `C-WAIT` with a recoverable frozen target line/minimum odds and no explicit user statement that the line never reached, the audit may apply this current accounting convention and mark the exposure basis `WAIT_ASSUMED`.

If target/minimum odds cannot be recovered from the frozen record, mark:

`WAIT ACCOUNTING INCOMPLETE — TARGET/PRICE NOT RECOVERABLE`

Do not invent a target from FT or later market data.
