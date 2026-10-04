# Football All-Model Bet Accounting

**Status:** ACTIVE AUDIT / MODEL-ACCOUNTING CONVENTION  
**Applies to:** Football C, C2, C3 and C4  
**Predictive effect:** none — this does not change model state/action selection

## 1. Purpose

For audit simplicity, model states/actions that express a usable Over opinion must not disappear merely because they did not become a physical user bet.

This convention therefore counts:

- every model's frozen `WATCH` state as a model-accounting bet;
- every C/C2/C3 `WAIT` action as a model-accounting bet;
- existing direct BET actions as bets under their exact execution quote.

C4 has no Step-2 action policy, so C4 participates through Step-1 WATCH accounting only.

## 2. One accounting bet per model per fixture

Do not double-count one model/fixture.

Resolution priority:

`DIRECT BET > COUNTABLE WAIT > WATCH > NONE`

Meaning:
- a later direct BET replaces the same model's WATCH/WAIT accounting entry;
- a countable WAIT replaces the same model's WATCH accounting entry;
- if a WAIT is explicitly declared not reached, that WAIT layer is removed and the frozen WATCH still counts when the model's board state was WATCH;
- a Step-2 PASS does not erase a prospectively frozen WATCH accounting bet;
- FOCUS is unchanged by this policy and is not automatically converted into a bet merely because it is FOCUS.

## 3. WATCH accounting — all four models

For:
- `C-WATCH`;
- `C2-WATCH`;
- `C3-WATCH`;
- `C4-WATCH`;

freeze one model-accounting bet at:

- line = that model's own frozen supported line;
- odds = **1.65** assumed audit price;
- stake = **1.0u**;
- side = Over.

Accounting basis:
- Football C -> `WATCH_ASSUMED`;
- C2/C3/C4 -> `SHADOW_WATCH_ASSUMED`.

The 1.65 price is a deterministic accounting convention derived from the current normal acceptable price floor. It is not a claim that a bookmaker quote at 1.65 was observed.

WATCH accounting is audit/model-performance accounting only.

A C-WATCH:
- does not create a user bet;
- does not create a Website Pick by itself;
- does not authorize live exposure;
- remains distinct from an actual C-BET/C-WAIT.

C2/C3/C4 WATCH accounting is shadow-only.

## 4. WAIT accounting — C/C2/C3

WAIT accounting remains model-specific and uses each model's own deterministic WAIT terms.

For a countable WAIT:
- line = that model's `wait_target_line`;
- odds = that model's `wait_min_odds`;
- stake = 1.0u unless an explicitly persisted model stake applies.

Basis:
- Football C -> `WAIT_ASSUMED`;
- C2/C3 -> `SHADOW_WAIT_ASSUMED`.

Current deterministic WAIT target/minimum rules remain unchanged:
- target = protected model target produced by the decision engine;
- minimum odds = 1.60 only where the existing top-ranked FOCUS soft-zone rule applies;
- otherwise minimum odds = 1.65.

This policy changes accounting scope, not WAIT selection logic.

## 5. WAIT user confirmation / line-never-reached

### Matching user bet — official C only

When the user supplies the actual corresponding Football C bet:
- preserve the original WAIT target/minimum;
- replace C's WAIT accounting entry with `WAIT_USER_CONFIRMED`;
- use exact actual line/odds/stake for C model-accounting reconciliation;
- use the same slip for actual user P/L.

Shadow C2/C3 are not rewritten from a user slip unless the user explicitly identifies a separate shadow-model mapping.

### Explicit line never reached

When the user explicitly says a model's WAIT target line never reached:
- remove that WAIT accounting layer for the specified model;
- do not infer this from missing history;
- do not infer this from later screenshots;
- do not infer this from no user bet.

If the same model had a frozen WATCH board state, the WATCH accounting bet remains because WATCH is now independently countable under this policy.

## 6. Direct BET precedence

For C/C2/C3 direct BET:
- line/odds = exact Step-2 quote;
- stake = persisted model stake;
- basis:
  - C -> `DIRECT_BET`;
  - C2/C3 -> `SHADOW_DIRECT_BET`.

Direct BET replaces WATCH/WAIT accounting for the same model/fixture.

C4 has no direct BET action.

## 7. FOCUS / PASS behavior

This change is intentionally narrow.

- `FOCUS` without a BET/WAIT is not automatically a bet under this patch.
- `PASS` without a prior WATCH is no bet.
- a prospectively frozen WATCH remains countable even if later Step-2 action is PASS.
- historical state labels are never rewritten because of accounting.

This preserves the user's requested WATCH/WAIT accounting without silently redefining the model classifiers.

## 8. Settlement

Settle Over Asian totals deterministically at each accounting line.

Possible settlement:
- WIN;
- HALF_WIN;
- PUSH;
- HALF_LOSS;
- LOSS;
- NO_BET / PENDING.

P/L uses the accounting odds/stake for that model.

WATCH synthetic P/L therefore uses 1.65.
WAIT P/L uses its frozen minimum odds unless user-confirmed C execution replaces it.
Direct BET P/L uses exact quote odds.

Run:

`python models/football/engine/model_bet_accounting_cli.py --input <model_accounting.json>`

One input must contain C/C2/C3/C4 rows for the same fixture.

## 9. Official vs shadow

Football C:
- C model-accounting P/L is an official model-performance metric;
- WATCH accounting does **not** create a Website Pick;
- C-BET/C-WAIT operational exposure behavior remains governed by their existing persistence rules.

C2/C3/C4:
- accounting is shadow-only;
- never create Website Picks;
- never create real exposure;
- never affect official workload.

## 10. Persistence

Daily Coverage stores the latest model-accounting JSON per model:
- `C Model Accounting` — `fldND2leUXgAq9UQl`
- `C2 Shadow Accounting` — `fldlWroOrJdYF3lHn`
- `C3 Shadow Accounting` — `fldEMKp5LzS5IZQpJ`
- `C4 Shadow Accounting` — `fldNvPrq9WTW9118X`
- `Model Accounting Revision` — `fldAt3A1bZW4QSGbF`

Decision States stores the current all-model Step-2 reconciliation:
- `All Model Accounting Result` — `fldOEt6DO20U9Yyab`
- `Model Accounting Revision` — `fldIAqPB03Oian4Fw`

Persist exact engine JSON, not prose paraphrase.

## 11. Rank-stage accounting

After C/C2/C3/C4 Step-1 states/lines are frozen:
- compile all four model rows;
- WATCHs become PENDING accounting bets;
- other board states remain NONE unless a later Step-2 action exists;
- persist the four model-accounting outputs.

This makes C4 WATCH immediately auditable despite C4 having no Step-2 action.

## 12. XI-stage accounting

After C/C2/C3 Step-2 action:
- recompile C/C2/C3 using direct/WAIT action data;
- include the unchanged frozen C4 row;
- persist the all-model result;
- direct BET/WAIT replaces prior WATCH for that model;
- C4 remains Step-1 shadow accounting.

## 13. Audit totals

For every audited fixture report one row per model:

`MODEL | BASIS | LINE | ODDS | STAKE | SETTLEMENT | P/L`

Slate totals:
- Football C model-accounting P/L;
- actual user P/L;
- C2 shadow model-accounting P/L;
- C3 shadow model-accounting P/L;
- C4 shadow model-accounting P/L.

Do not label C2/C3/C4 as official exposure.

## 14. Historical use

Do not fabricate a supported line or WAIT target.

Historical application is allowed only when:
- the model's frozen WATCH + supported line is recoverable; or
- the model's WAIT target/minimum is recoverable; or
- exact direct bet quote is recoverable.

Otherwise:
`MODEL ACCOUNTING INCOMPLETE — TERMS NOT RECOVERABLE`

Do not infer missing line/price from FT or later market history.
