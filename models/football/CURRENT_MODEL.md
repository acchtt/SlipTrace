# Current Football Model

**Active official model:** Football **v0.2.49**  
**Official base:** Football **v0.2.47 CLEAN**  
**Active official patch:** `rules/MODEL_RULES_FOOTBALL_V0.2.49.md` — **TWO-SIDED PRIORITY**  
**Shadow comparison models:** Football **v0.2.47 CLEAN** and Football **v0.2.48-SHADOW**  
**Active operating profile:** **AISCORE-ONLY SWEEP + NORMAL MATCH RESEARCH + v0.2.49 OFFICIAL + v0.2.47/v0.2.48 SHADOWS**  
**Status:** Operational / official-lock mode  
**Timezone:** `Asia/Ho_Chi_Minh` (ICT, UTC+7)  
**Canonical namespace:** `models/football/`

Football v0.2.49 is the active official operating model. It inherits the clean original `v0.2.47` rules and adds the narrow prospective two-sided-priority patch in `rules/MODEL_RULES_FOOTBALL_V0.2.49.md`.

For forward comparison, the clean legacy v0.2.47 logic is also run as a shadow track, and `v0.2.48-SHADOW` continues as a separate shadow track. Neither shadow enters official P/L.

`v0.2.47-R` remains archived and must not be loaded into active decisions.

---

## Critical fixture-source directive

**Fixture sweep authority is AiScore only.**

For daily slates, upcoming-match lists, and requested fixture windows, build the fixture universe only from:

- `aiscore.com`
- `m.aiscore.com`
- AiScore daily/live listings and AiScore match pages

Do not build a multi-source fixture union and do not allow Soccerway, FotMob, Google/web search, BSD/Bzzoiro, league sites, bookmaker pages, or any other schedule provider to add fixtures to the slate.

After AiScore establishes a fixture, **match research runs normally** using the best available sources.

`procedures/FOOTBALL_MATCH_SWEEP_AND_RESEARCH_PROCEDURE.md` is the authority for this separation and supersedes older multi-source reconciliation instructions.

If the relevant AiScore window cannot be traversed sufficiently, state:

`COVERAGE INCOMPLETE — AiScore sweep incomplete`

Do not backfill the universe from another provider.

---

## Critical coverage directive

**Coverage control is mandatory before model ranking.**

The system must not start by choosing a few `credible candidates`. It must first sweep the full requested AiScore fixture window, apply eligibility, and give **every eligible fixture** a PRE disposition.

The mandatory shared sequence is:

`AISCORE FIXTURE UNIVERSE → ELIGIBILITY → SCREEN EVERY ELIGIBLE FIXTURE → FOCUS/WATCHLIST/PASS → XI WINDOW RERANK → MARKET → v0.2.49 OFFICIAL + v0.2.47 SHADOW + v0.2.48 SHADOW`

The visible board may be aggressively shortened. The internal screened universe may not.

**SHORTEN THE DISPLAY, NEVER THE SCREENED UNIVERSE.**

`procedures/FOOTBALL_COVERAGE_CONTROLLER.md` remains the authority for screening completeness, same-window survival, late discovery, and coverage counts, subject to the AiScore-only source policy above.

---

## Critical regime directive

The Sep 1, 2026 enforcement-hardening experiment is **INACTIVE for official selection**.

Do **not** automatically apply, restore, or infer any of the former hardening gates in official decision-making. In particular, the following are not active official hard caps:

- reserve/youth A1 cap;
- O3.75 exceptional hard gate;
- A2 O3.5+ burden prohibition;
- XI "names cannot create a route" hard prohibition;
- H2H de-weighting as a mandatory override rule.

If any historical note conflicts with this file, this file wins for the operating layer. `rules/MODEL_RULES_FOOTBALL_V0.2.47.md` remains the immutable clean base, and `rules/MODEL_RULES_FOOTBALL_V0.2.49.md` is the active official ranking patch.

---

## Canonical load order

Load these files for the active workflow:

1. `models/football/CURRENT_MODEL.md`
2. `models/football/procedures/FOOTBALL_MATCH_SWEEP_AND_RESEARCH_PROCEDURE.md`
3. `models/football/procedures/FOOTBALL_COVERAGE_CONTROLLER.md`
4. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.47.md`
5. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.49.md`
6. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.48-SHADOW.md`
7. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
8. `models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md`
9. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`

Do **not** load `models/football/archive/rules/MODEL_RULES_FOOTBALL_V0.2.47-R.md` into active decisions.

---

## Coverage control plane

Daily coverage is persisted to Airtable:

- Base: `SlipTrace Football Decision Control`
- Table: `Daily Coverage Ledger`
- Table ID: `tblcl1UAyMqZT6Ub0`

For every requested slate/window:

1. traverse the relevant AiScore fixture listing completely for the requested ICT window;
2. normalize kickoffs to ICT;
3. write/upsert every discovered AiScore fixture to the coverage ledger;
4. mark exclusions explicitly instead of omitting them;
5. screen every eligible fixture to A1 / A2 / B+ / B-PASS / DATA INCOMPLETE;
6. assign FOCUS / WATCHLIST / PASS / UNRESOLVED;
7. verify coverage counts reconcile before claiming a full slate;
8. persist FOCUS and WATCHLIST so `what's next?` does not rebuild a partial board from memory;
9. rerank all surviving same-window candidates at confirmed XI.

Under the current single-source policy, `Reconciled = true` means the relevant AiScore window itself was fully traversed, normalized, and accounted for. It does not require an independent schedule provider.

Required count invariants:

`Universe = Eligible + Excluded`

`Eligible = Focus + Watchlist + Pass + Unresolved`

If counts fail, state:

`COVERAGE INCOMPLETE — board provisional`

---

## Research policy

Once AiScore has established the fixture, research runs normally.

Use the best available evidence from official sources, Soccerway, FotMob, FBref, BSD/Bzzoiro where supported, reputable statistics/news sources, and user-supplied screenshots as appropriate.

Research may refine team profile, chance quality, incentives, XI, tactical shape, failure modes, and market expression.

A research source may not add a fixture to the universe unless that same fixture is verified on AiScore.

---

## Core decision order

After coverage completion, the official structural decision order is:

`STRUCTURAL QUALITY → CARRIER CEILING → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE QUALITY → XI RERANK → GOAL BURDEN → PRICE → LOCK / HOLD`

**v0.2.49 clarification:** structural archetype is part of `STRUCTURAL QUALITY`. When grades are comparable, apply:

`TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER`

Carrier ceiling may break ties only after that structural preference has been respected. Price is a tiebreaker only and must not promote a structurally weaker match.

---

## Active ranking bands

- **A1** — genuine Two-Sided Tier A, or an exceptional Elite Carrier that clearly clears the v0.2.49 exception standard.
- **A2** — strong two-sided environment, or a strong carrier with one meaningful weakness.
- **B+** — good environment but materially dependent on opponent contribution, rotation, game state, or another failure mode.
- **B / PASS** — fragile route, strong resistance, cohesion problem, weak chance quality, or excessive goal burden.

**Two-Sided A is the default priority over same-grade Elite Carrier A.** An Elite Carrier may leapfrog a genuine same-grade Two-Sided candidate only when it is clearly superior on both repeatable chance quality / self-funding 3+ capacity and failure-mode resistance.

This ordering controls ranking and attention; it does not automatically promote a B+ two-sided match to A2 or force a lock.

---

## Current operating rules

- Confirmed XI is the first legitimate rerank gate after frozen PRE.
- Team GF/GA and scoring/conceding-frequency profile is mandatory.
- Chance quality is supporting evidence, not a rigid universal veto.
- **Two-sided priority rule:** when grades are comparable, rank `TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER` on the v0.2.49 official track.
- **Elite-carrier exception:** an elite carrier may outrank a genuine same-grade two-sided match only when clearly superior on both repeatable chance quality / self-funding capacity and failure-mode resistance.
- **Recent-total / leakage confirmation rule:** extreme recent totals or leakage may identify a candidate but cannot alone justify top-board promotion or an official lock. Require supporting evidence that the necessary scoring routes are repeatable; if weak/unavailable, reduce priority or HOLD.
- Failure modes must be identified before selection.
- Protected Asian totals are preferred when they preserve the thesis at reasonable price.
- An affirmative final selection on the official track is automatically an **OFFICIAL LOCK**.
- `PASS` / `NO BET — HOLD` means no official bet.
- Live evidence validates or invalidates the frozen prematch thesis; it does not rewrite history.
- The clean v0.2.47 halftime compression / saturation gate remains active where applicable on models that inherit it.
- Manual live overrides must be separately labelled.
- Full-match Asian totals settle on 90 minutes plus stoppage time unless the market explicitly includes extra time.
- Counterfactual simulations never enter official P/L.
- Every material official/shadow decision state is logged with its actual model version.

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

1. sweep AiScore only;
2. do not publish the board as complete until the requested AiScore window and coverage counts reconcile;
3. screen every eligible fixture before display shortening;
4. show the strongest FOCUS matches prominently;
5. preserve all FOCUS + WATCHLIST matches internally through XI unless explicitly downgraded;
6. do not omit earlier kickoff blocks;
7. when matches overlap, compare all surviving FOCUS/WATCHLIST fixtures in the same practical kickoff window;
8. on the official v0.2.49 track, apply `TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER` for comparable grades;
9. if a leading candidate is downgraded by XI or market, immediately promote the next strongest surviving candidate;
10. use the persisted coverage ledger for `what's next?`;
11. mark AiScore fixtures missed by the first sweep with the coverage taxonomy rather than silently inserting or ignoring them.

A user-facing board should include a compact coverage line, e.g.:

`Coverage: 42 universe | 27 eligible | 27 screened | 5 focus | 8 watch | 14 pass | 0 unresolved`

---

## Three-track output

Every eligible match that survives far enough for a material verdict uses the **same evidence snapshot** for all three tracks.

### Official track — Football v0.2.49

Allowed final outcomes:

- `OFFICIAL LOCK — <line> @ <odds>`
- `NO BET — HOLD`
- `PASS`

Only this track enters official P/L.

### Shadow track 1 — Football v0.2.47 CLEAN

Run the clean legacy v0.2.47 logic on the same evidence state **without** applying the v0.2.49 two-sided-priority patch.

Allowed outcomes:

- `SHADOW v0.2.47 LOCK — <line> @ <odds> — DO NOT PLACE`
- `SHADOW v0.2.47 HOLD`
- `SHADOW v0.2.47 PASS`

### Shadow track 2 — Football v0.2.48-SHADOW

Run the documented v0.2.48 shadow rules on the same evidence state. Do not silently import the v0.2.49 priority patch into this comparison track unless a later rule explicitly changes that.

Allowed outcomes:

- `SHADOW v0.2.48 LOCK — <line> @ <odds> — DO NOT PLACE`
- `SHADOW v0.2.48 HOLD`
- `SHADOW v0.2.48 PASS`

Both shadows are comparison tracks only and never enter official P/L. A shadow HOLD/PASS cannot suppress an official v0.2.49 decision.

---

## Airtable routing

- Official v0.2.49 material states use model version `v0.2.49`.
- Official v0.2.49 LOCKs are the only picks that enter Website Picks / official P/L.
- v0.2.47 material comparison states use model version `v0.2.47` and are shadow only.
- v0.2.48 material comparison states use model version `v0.2.48-SHADOW` and are shadow only.
- Existing Daily Coverage Ledger v0.2.47 and v0.2.48 PRE fields remain comparison/shadow fields; do not relabel them as v0.2.49 official states.

---

## Coverage/audit taxonomy

- **SCREENED** — actually assessed before/around kickoff, regardless of visible board placement.
- **LATE-DISCOVERED BUT SCREENED** — present on AiScore, omitted initially, then found and assessed in time.
- **TRUE MISSED SCREEN** — present on AiScore but never properly assessed before kickoff.
- **RANKING MISS** — screened but another match was prioritized incorrectly.
- **HOLD/PASS** — screened and deliberately rejected.
- **FALSE-NEGATIVE HOLD** — screened correctly, but rejected despite prematch evidence likely justifying a lock.
- **BAD LOCK** — locked despite structure/XI/line probably not clearing.
- **CORRECT HOLD, OVER LANDED** — final score went Over but prematch evidence did not justify a bet.

Do not infer missed-lock status from the final score alone.

---

## Anti-hindsight rule

Never rewrite a prematch grade, XI rerank, line, price, coverage status, or verdict after the result is known. A later winning score does not convert a prior HOLD into a model win, and a losing score does not by itself prove that the original process was wrong.

The v0.2.49 patch is prospective from 2026-09-08 ICT. Historical v0.2.47 decisions and P/L remain recorded under the model version that actually produced them.

Historical versions and the Sep 1 hardening experiment remain recoverable from Git history but are not part of the active official-selection regime.
