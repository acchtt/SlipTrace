# Current Football Model

**Active model:** Football **v0.2.47-R**  
**Status:** Operational / official-lock mode  
**Timezone:** `Asia/Ho_Chi_Minh` (ICT, UTC+7)  
**Canonical namespace:** `models/football/`

`v0.2.47-R` is the consolidated operational revision used by the current Football v1.0 workflow. It replaces the old audit/shadow stack and the historical incremental-load chain that previously required loading many rule files in sequence.

## Canonical load order

Load only these files:

1. `models/football/CURRENT_MODEL.md`
2. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.47-R.md`
3. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
4. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`

No historical handoff, review, benchmark, addendum, or prior version is required to operate the current model.

## Core decision order

`FULL SLATE → STRUCTURAL QUALITY → CARRIER CEILING → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE QUALITY → XI RERANK → GOAL BURDEN → PRICE → LOCK / HOLD`

Price is a tiebreaker only. It must not promote a structurally weaker match.

## Active ranking bands

- **A1** — genuine Two-Sided Tier A, or proven Elite Carrier with a credible independent 3+ route and acceptable opponent resistance.
- **A2** — strong two-sided environment or strong carrier with one meaningful weakness.
- **B+** — good environment but materially dependent on opponent contribution, rotation, game state, or another failure mode.
- **B / PASS** — fragile route, strong resistance, cohesion problem, weak chance quality, or excessive goal burden.

Two-Sided A and Elite Carrier A are peers. Do not demote an elite carrier merely because the opponent contributes less.

## Current operating rules

- Confirmed XI is the first legitimate rerank gate.
- Team GF/GA and scoring/conceding-frequency profile is mandatory.
- Repeatable chance quality is mandatory before A1 promotion.
- xG is a modifier, not the primary engine or a veto by itself.
- Failure modes must be stated before selection.
- Protected Asian totals are preferred when they preserve the thesis at reasonable price.
- An affirmative final betting selection is automatically an **OFFICIAL LOCK**.
- `PASS` / `NO BET — HOLD` means no bet.
- Live evidence validates or invalidates the frozen prematch thesis; it does not rewrite history.
- Manual live overrides are allowed only as a separately labelled state.
- K League is a permanent hard exclusion.
- Full-match Asian totals settle on 90 minutes plus stoppage time only unless the market explicitly includes extra time.
- Counterfactual simulations never enter official P/L.
- Every material decision state is logged to Airtable.

## Anti-hindsight rule

Never rewrite a prematch grade, XI rerank, line, price, or verdict after the result is known. A later winning score does not convert a prior HOLD into a model win, and a losing score does not by itself prove that the original process was wrong.

Historical versions remain recoverable from Git history but are not part of the active model tree.