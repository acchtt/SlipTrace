# Current Football Model

**Active model:** Football **v0.2.47-R**  
**Active operating profile:** **PRE-HARDENING**  
**Status:** Operational / official-lock mode  
**Timezone:** `Asia/Ho_Chi_Minh` (ICT, UTC+7)  
**Canonical namespace:** `models/football/`

`v0.2.47-R` remains the consolidated operational revision used by Football v1.0.

## Critical regime directive

The Sep 1, 2026 enforcement-hardening experiment is **INACTIVE for official selection**.

Do **not** automatically apply, restore, or infer any of the former hardening gates in official decision-making. In particular, the following are not active hard caps:

- reserve/youth A1 cap;
- O3.75 exceptional hard gate;
- A2 O3.5+ burden prohibition;
- XI "names cannot create a route" hard prohibition;
- H2H de-weighting as a mandatory override rule.

Those ideas may be studied only in a clearly labeled **SHADOW / BENCHMARK** context and must not affect the official shortlist, XI rerank, line choice, or lock unless the active model is explicitly changed again.

If any future document, note, memory, audit, or prior commit conflicts with this directive, **this file wins**.

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
- Chance quality is assessed as supporting evidence, not as a rigid promotion veto.
- **Recent-total / leakage confirmation rule:** when a candidate's high grade is driven heavily by an extreme recent run of high totals or defensive leakage, those scorelines may identify the candidate but cannot by themselves justify top-board promotion or an official lock. Require supporting evidence that the necessary scoring routes are producing repeatable good chances; if that support is weak or unavailable, reduce priority or HOLD.
- This calibration is narrow: it is **not** a reserve/youth cap, short-sample hard cap, burden gate, XI prohibition, or revival of the Sep 1 hardened framework.
- Failure modes must be identified before selection.
- Protected Asian totals are preferred when they preserve the thesis at reasonable price.
- An affirmative final betting selection is automatically an **OFFICIAL LOCK**.
- `PASS` / `NO BET — HOLD` means no bet.
- Live evidence validates or invalidates the frozen prematch thesis; it does not rewrite history.
- Manual live overrides are allowed only as a separately labelled state.
- **Cup exclusion:** exclude all cup/knockout competitions from the normal board and official locks except the **English FA Cup** and Germany's **DFB-Pokal**.
- **League Cup exclusion:** all League Cup competitions are excluded in every country, including the English EFL/Carabao Cup. League Cup matches cannot be restored by XI, price, or live evidence.
- European/continental cup competitions remain excluded under this cup rule.
- K League is a permanent hard exclusion.
- Full-match Asian totals settle on 90 minutes plus stoppage time only unless the market explicitly includes extra time.
- Counterfactual simulations never enter official P/L.
- Every material decision state is logged to Airtable.

## Board policy

For daily/upcoming requests:

1. scan the full ICT slate;
2. remove excluded competitions, including every League Cup and all other cup matches except the English FA Cup and DFB-Pokal;
3. use the **pre-hardening** structural ranking logic;
4. apply the recent-total/leakage confirmation rule before promoting scoreline-driven candidates into the top focus group;
5. aggressively shorten to the best few matches worth focusing on;
6. freeze those matches before XI;
7. rerank from confirmed XI and market;
8. lock only the strongest expressions.

The inactive hardened framework may be tracked in parallel only as a shadow benchmark.

## Anti-hindsight rule

Never rewrite a prematch grade, XI rerank, line, price, or verdict after the result is known. A later winning score does not convert a prior HOLD into a model win, and a losing score does not by itself prove that the original process was wrong.

Historical versions and the Sep 1 hardening experiment remain recoverable from Git history but are not part of the active official-selection regime.
