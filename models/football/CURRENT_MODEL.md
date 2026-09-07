# Current Football Model

**Active official model:** Football **v0.2.47 CLEAN**  
**Parallel shadow model:** Football **v0.2.48-SHADOW**  
**Active operating profile:** **CLEAN ORIGINAL BASE + COVERAGE-CONTROLLED OFFICIAL-LOCK OPERATING LAYER**  
**Status:** Operational / official-lock mode  
**Timezone:** `Asia/Ho_Chi_Minh` (ICT, UTC+7)  
**Canonical namespace:** `models/football/`

The clean original `v0.2.47` rules file is the official base rule source. `v0.2.47-R` is archived and must not be loaded into official decisions. `v0.2.48-SHADOW` runs in parallel as a forward-test candidate and never enters official P/L unless explicitly promoted.

The original v0.2.47 file is an incremental rules file focused on the high-scoring halftime compression / goal-saturation gate and explicitly retains earlier v0.2.44-v0.2.46 controls. The current prematch board, structural ranking, XI, market, competition-scope, coverage, and Airtable instructions in this file and the procedure files are the operating layer around that clean base. They do not rewrite the clean source file.

---

## Critical coverage directive

**Coverage control is mandatory before model ranking.**

The system must not start by choosing a few `credible candidates`. It must first build and reconcile the fixture universe, apply eligibility, and give **every eligible fixture** a PRE disposition.

The mandatory shared sequence is:

`FIXTURE UNIVERSE → RECONCILE → ELIGIBILITY → SCREEN EVERY ELIGIBLE FIXTURE → FOCUS/WATCHLIST/PASS → XI WINDOW RERANK → MARKET → v0.2.47 OFFICIAL + v0.2.48 SHADOW`

The visible board may be aggressively shortened. The internal screened universe may not.

`procedures/FOOTBALL_COVERAGE_CONTROLLER.md` is the authority for fixture completeness, same-window survival, late discovery, and coverage reconciliation.

---

## Critical regime directive

The Sep 1, 2026 enforcement-hardening experiment is **INACTIVE for official selection**.

Do **not** automatically apply, restore, or infer any of the former hardening gates in official decision-making. In particular, the following are not active hard caps:

- reserve/youth A1 cap;
- O3.75 exceptional hard gate;
- A2 O3.5+ burden prohibition;
- XI "names cannot create a route" hard prohibition;
- H2H de-weighting as a mandatory override rule.

Those ideas may be studied only in a clearly labeled SHADOW/BENCHMARK context and must not affect the official v0.2.47 shortlist, XI rerank, line choice, or lock unless the active model is explicitly changed again.

If any future document, note, memory, audit, or prior commit conflicts with this directive, **this file wins for the operating layer**, while `rules/MODEL_RULES_FOOTBALL_V0.2.47.md` remains immutable as the clean base rule source.

---

## Canonical load order

Load these files for the active workflow:

1. `models/football/CURRENT_MODEL.md`
2. `models/football/procedures/FOOTBALL_COVERAGE_CONTROLLER.md`
3. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.47.md`
4. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.48-SHADOW.md`
5. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
6. `models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md`
7. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`

Do **not** load `models/football/archive/rules/MODEL_RULES_FOOTBALL_V0.2.47-R.md` into active decisions.

No historical handoff, review, benchmark, addendum, or prior version is required to operate the current model.

---

## Coverage control plane

Daily coverage is persisted to Airtable:

- Base: `SlipTrace Football Decision Control`
- Table: `Daily Coverage Ledger`
- Table ID: `tblcl1UAyMqZT6Ub0`

For every requested slate/window:

1. reconcile a fixture union from the available canonical feed plus an independent schedule source when possible;
2. convert all kickoffs to ICT;
3. write/upsert every discovered fixture to the coverage ledger;
4. mark exclusions explicitly instead of omitting them;
5. screen every eligible fixture to A1 / A2 / B+ / B-PASS / DATA INCOMPLETE;
6. assign FOCUS / WATCHLIST / PASS / UNRESOLVED;
7. verify coverage counts reconcile before claiming a full slate;
8. persist FOCUS and WATCHLIST so `what's next?` does not rebuild a partial board from memory;
9. rerank all surviving same-window candidates at confirmed XI.

Required count invariants:

`Universe = Eligible + Excluded`

`Eligible = Focus + Watchlist + Pass + Unresolved`

If reconciliation fails, state:

`COVERAGE INCOMPLETE — board provisional`

---

## Core decision order

After coverage completion, the official structural decision order is:

`STRUCTURAL QUALITY → CARRIER CEILING → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE QUALITY → XI RERANK → GOAL BURDEN → PRICE → LOCK / HOLD`

Price is a tiebreaker only. It must not promote a structurally weaker match.

---

## Active ranking bands

- **A1** — genuine Two-Sided Tier A, or proven Elite Carrier with a credible independent 3+ route and acceptable opponent resistance.
- **A2** — strong two-sided environment or strong carrier with one meaningful weakness.
- **B+** — good environment but materially dependent on opponent contribution, rotation, game state, or another failure mode.
- **B / PASS** — fragile route, strong resistance, cohesion problem, weak chance quality, or excessive goal burden.

Two-Sided A and Elite Carrier A are peers. Do not demote an elite carrier merely because the opponent contributes less.

---

## Current operating rules

- Confirmed XI is the first legitimate rerank gate after frozen PRE.
- Team GF/GA and scoring/conceding-frequency profile is mandatory.
- Chance quality is assessed as supporting evidence, not as a rigid promotion veto.
- **Recent-total / leakage confirmation rule:** when a candidate's high grade is driven heavily by an extreme recent run of high totals or defensive leakage, those scorelines may identify the candidate but cannot by themselves justify top-board promotion or an official lock. Require supporting evidence that the necessary scoring routes are producing repeatable good chances; if that support is weak or unavailable, reduce priority or HOLD.
- This calibration is narrow: it is **not** a reserve/youth cap, short-sample hard cap, burden gate, XI prohibition, or revival of the Sep 1 hardened framework.
- Failure modes must be identified before selection.
- Protected Asian totals are preferred when they preserve the thesis at reasonable price.
- An affirmative final betting selection on the official track is automatically an **OFFICIAL LOCK**.
- `PASS` / `NO BET — HOLD` means no official bet.
- Live evidence validates or invalidates the frozen prematch thesis; it does not rewrite history.
- The clean v0.2.47 high-scoring halftime compression / saturation gate remains active for relevant post-HT live decisions.
- Manual live overrides are allowed only as a separately labelled state.
- Full-match Asian totals settle on 90 minutes plus stoppage time only unless the market explicitly includes extra time.
- Counterfactual simulations never enter official P/L.
- Every material official/shadow decision state is logged to Airtable with its actual model version.

---

## Competition scope

Eligible cup/knockout competitions for the normal board and official locks are only:

- English domestic cups, including FA Cup and EFL/Carabao Cup;
- Germany's DFB-Pokal;
- North American Leagues Cup (MLS/Liga MX).

All other domestic, continental, and League Cup competitions remain excluded unless explicitly added later.

Hard exclusions:

- K League;
- Belgian Pro League / Jupiler Pro League.

The North American **Leagues Cup** is an explicit named exception and must not be removed by a generic “League Cup” filter.

---

## Board policy

For daily/upcoming requests:

1. run the Coverage Controller first;
2. do not publish the board as complete until fixture counts reconcile;
3. screen every eligible fixture before display shortening;
4. show the strongest FOCUS matches prominently;
5. preserve all FOCUS + WATCHLIST matches internally through XI unless explicitly downgraded;
6. do not omit earlier kickoff blocks;
7. when matches overlap, compare all surviving FOCUS/WATCHLIST fixtures in the same practical kickoff window;
8. if a leading candidate is downgraded by XI or market, immediately promote the next strongest surviving candidate;
9. use the persisted coverage ledger for `what's next?`;
10. mark newly discovered fixtures with the coverage taxonomy rather than silently inserting or ignoring them.

A user-facing board should include a compact coverage line, e.g.:

`Coverage: 42 universe | 27 eligible | 27 screened | 5 focus | 8 watch | 14 pass | 0 unresolved`

---

## Dual-model output

Every eligible match that survives far enough for a model verdict uses the same information state for both tracks.

### Official track

**Football v0.2.47 CLEAN**

Allowed final outcomes:

- `OFFICIAL LOCK — <line> @ <odds>`
- `NO BET — HOLD`
- `PASS`

Only this track enters official P/L.

### Shadow track

**Football v0.2.48-SHADOW**

Allowed final outcomes:

- `SHADOW LOCK — <line> @ <odds> — DO NOT PLACE`
- `SHADOW HOLD`
- `SHADOW PASS`

Shadow outcomes are logged separately and never enter official P/L until explicit promotion.

A shadow HOLD must not suppress an official v0.2.47 candidate. An official HOLD/PASS must not erase the shadow result for an eligible screened match.

---

## Coverage/audit taxonomy

- **SCREENED** — actually assessed before/around kickoff, regardless of visible board placement.
- **LATE-DISCOVERED BUT SCREENED** — omitted initially, found and assessed in time.
- **TRUE MISSED SCREEN** — never properly assessed before kickoff.
- **RANKING MISS** — screened but another match was prioritized incorrectly.
- **HOLD/PASS** — screened and deliberately rejected.
- **FALSE-NEGATIVE HOLD** — screened correctly, but rejected despite prematch evidence likely justifying a lock.
- **BAD LOCK** — locked despite structure/XI/line probably not clearing.
- **CORRECT HOLD, OVER LANDED** — final score went Over but prematch evidence did not justify a bet.

Do not infer missed-lock status from the final score alone.

---

## Anti-hindsight rule

Never rewrite a prematch grade, XI rerank, line, price, coverage status, or verdict after the result is known. A later winning score does not convert a prior HOLD into a model win, and a losing score does not by itself prove that the original process was wrong.

Historical versions and the Sep 1 hardening experiment remain recoverable from Git history but are not part of the active official-selection regime.