# Current Football Model

**Active official model:** Football **v0.2.50**  
**Official base:** Football **v0.2.47 CLEAN**  
**Active official patches:**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.49.md` — **TWO-SIDED PRIORITY**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.50.md` — **EXTREME GOAL ENVIRONMENT / PERSISTENT HIGH-LINE**  
**Shadow comparison tracks:** Football **v0.2.47 CLEAN** and Football **v0.2.48-SHADOW**  
**Fixture authority:** **AiScore only**  
**Operating workflow:** **AiScore fixture handoff → price/XI-blind Work structural sweep → frozen FOCUS/WATCHLIST board → user-supplied XI + odds → v0.2.50 official verdict**  
**Canonical timezone:** `Asia/Ho_Chi_Minh` (ICT, UTC+7)

This file is the operating authority for Football. Historical rules are recoverable from Git history and must not be inferred into current decisions.

---

## 1. Canonical load order

Load only the current active stack:

1. `models/football/CURRENT_MODEL.md`
2. `models/football/procedures/FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`
3. `models/football/procedures/FOOTBALL_MATCH_SWEEP_AND_RESEARCH_PROCEDURE.md`
4. `models/football/procedures/FOOTBALL_COVERAGE_CONTROLLER.md`
5. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.47.md`
6. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.49.md`
7. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.50.md`
8. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.48-SHADOW.md`
9. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
10. `models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md`
11. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`

**Conditional auxiliary trial load:** when the user explicitly asks to assess, continue, review, audit, fetch, or rank UEFA Youth League / U19 trial matches, additionally load:

`models/football/trials/UEFA_YOUTH_LEAGUE_TRIAL.md`

That file is persistent cross-chat trial memory only. It may define UYL-specific experimental calibration and preserve trial results/lessons, but it does **not** whitelist youth football for the normal actionable board, does not create official Football v0.2.50 exposure, and does not override the official senior model outside an explicitly invoked UYL trial.

Do not load superseded rule files from chat memory, old handoffs, or Git history into a current decision.

Where older active procedure text still names v0.2.49, treat it as inherited procedure text and apply the current v0.2.50 patches and this file as the higher authority.

---

## 2. Fixture-source directive

**AiScore is the sole fixture-discovery authority.**

Build the requested fixture universe only from:

- `aiscore.com`
- `m.aiscore.com`
- AiScore daily/live listings
- AiScore match pages

Soccerway, FotMob, Google/web search, BSD/Bzzoiro, league sites, bookmaker pages, and other providers may be used for **research after AiScore establishes the fixture**, but they may not add fixtures to the universe.

If the relevant AiScore window cannot be traversed sufficiently, state:

`COVERAGE INCOMPLETE — AiScore sweep incomplete`

Do not backfill the universe from another schedule provider.

### Cross-midnight completeness rule

If a requested ICT window touches more than one calendar date, explicitly traverse **every AiScore calendar-date listing touched by that window**. A sweep cannot be marked complete merely because no later fixture was discovered.

Before `complete:true` / `Reconciled = true`:

- verify each touched AiScore date page/block;
- verify the terminal requested kickoff interval/cutoff;
- account for every discovered fixture exactly once;
- confirm no known major competition block inside the window is missing.

If the requested window ends at 03:00 ICT, for example, the absence of a 03:00 block must be verified rather than inferred from a last-found 02:00 kickoff.

**SHORTEN THE DISPLAY, NEVER THE SCREENED UNIVERSE.**

---

## 3. Time and schedule integrity — mandatory

All football fixture times follow `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`.

Canonical invariant:

`AISCORE IDENTITY → kickoff_utc → ONE conversion to Asia/Ho_Chi_Minh → kickoff_ict → slate_date_ict → status revalidation → schedule display`

Critical rules:

- a timestamp ending in `Z` is UTC, never ICT;
- Airtable may serialize a date field as UTC `Z` even when the field displays in ICT;
- convert a raw UTC value to ICT **exactly once**;
- never add +7 to a timestamp already expressed in ICT;
- derive `Slate Date` from the ICT-converted kickoff, not from the raw UTC date;
- a fixture outside the requested normalized ICT window cannot enter that board;
- before an `upcoming` / `next matches` schedule is shown, near-term fixtures must be revalidated against AiScore status so LIVE/FT/postponed fixtures are not presented as upcoming;
- a date/time mismatch is `UNRESOLVED — SCHEDULE INTEGRITY` until corrected.

Historical schedule faults are annotated; they do not rewrite frozen PRE history.

---

## 4. Actionable competition quality — current user overlay

The normal actionable board is governed by a **senior-quality overlay**, not a legacy competition whitelist.

Exclude from the actionable board:

- all youth/Uxx competitions: U17, U18, U19, U20, U21, U23;
- academy/junior competitions;
- reserve/B-team/development competitions;
- amateur/semi-professional competitions;
- regional/state/provincial leagues;
- very small/obscure weak-data leagues;
- domestic lower divisions below top flight unless explicitly user-approved or explicitly whitelisted;
- **all Finnish domestic league competitions at every tier/category, including men's and women's leagues — hard exclusion effective 2026-09-09 ICT onward.**

The Finnish-league exclusion is prospective and does not rewrite historical decisions. It applies to every domestic league competition in Finland, including Veikkausliiga and all lower-tier Finnish leagues. Keep such fixtures in the raw AiScore universe for reconciliation, but classify them as excluded before structural screening. This is a competition rule, not a club-nationality rule: Finnish Cup and UEFA club competitions involving Finnish clubs are not excluded by this rule unless they fail another active eligibility rule.

Do not weaken this overlay to fill the slate. Excluded fixtures must not appear as FOCUS, WATCHLIST, or official betting candidates.

There is **no generic exclusion for senior continental competitions, domestic cups, or competitions merely because their name contains “Cup.”** Senior first-team elite continental competitions are actionable when they otherwise clear the overlay, explicitly including:

- UEFA Champions League;
- UEFA Europa League;
- UEFA Conference League.

Competition-name legacy filters must never remove an otherwise qualifying senior first-team fixture.

---

## 5. Mandatory coverage sequence

The shared production sequence is:

`AISCORE FIXTURE UNIVERSE → TIME/SCHEDULE INTEGRITY → SENIOR-QUALITY ELIGIBILITY → SCREEN EVERY ACTIONABLE FIXTURE → FOCUS/WATCHLIST/PASS/UNRESOLVED → FREEZE PRE → USER-SUPPLIED XI RERANK → GOAL BURDEN / EGE REGIME → USER-SUPPLIED PRICE → v0.2.50 OFFICIAL VERDICT + SHADOW COMPARISONS`

Every actionable fixture must receive a PRE disposition before the visible board is shortened.

Required count invariants:

`Universe = Actionable eligible + Excluded`

`Actionable eligible = Focus + Watchlist + Pass + Unresolved`

If counts fail, state:

`COVERAGE INCOMPLETE — board provisional`

---

## 6. Core decision order

Official v0.2.50 decision order:

`STRUCTURAL QUALITY → CARRIER CEILING → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE QUALITY → CONFIRMED XI RERANK → GOAL BURDEN / REGIME → PRICE → LOCK / HOLD`

Price never promotes a structurally weaker match.

For comparable grades, v0.2.49 remains active inside v0.2.50:

`TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER`

A genuine TWO-SIDED label requires credible independent scoring routes from both teams. Leakage, recent high totals, or an occasional opponent goal does not by itself create a two-sided profile.

An ELITE CARRIER may leapfrog a genuine same-grade TWO-SIDED candidate only when clearly superior on both:

1. repeatable chance quality / self-funding 3+ capacity; and
2. failure-mode resistance.

---

## 7. Active structural bands

- **A1** — genuine Two-Sided Tier A, or an exceptional Elite Carrier that clearly meets the v0.2.49 exception standard.
- **A2** — strong two-sided environment, or strong carrier with one meaningful weakness.
- **B+** — good environment but materially dependent on opponent contribution, rotation, game state, or another failure mode.
- **B / PASS** — fragile route, strong resistance, cohesion problem, weak chance quality, or excessive goal burden.

Archetype priority controls ranking and attention; it does not automatically change the grade and does not force a lock.

---

## 8. Mandatory evidence rules

Before final promotion, evaluate the actual team profile, including where available:

- season GF / GA;
- relevant recent GF / GA;
- scoring 2+ frequency;
- conceding 2+ frequency;
- clean-sheet / suppression tendency;
- home/away splits;
- competition-specific context.

Chance quality is supporting evidence, not a rigid universal veto. Where available, use big chances, penalty-area/central access, shots-on-target quality, box touches, xG/xGA/xGOT, and comparable creation evidence.

Before selection, explicitly identify the main failure mode. Examples include carrier slowdown after 1-0/2-0, weak opponent scoring route, sterile possession, heavy rotation/cohesion risk, strong central suppression, or excessive dependence on late goals.

---

## 9. Frozen PRE and confirmed-XI rerank

**Confirmed XI is the first legitimate rerank gate after frozen PRE.**

FOCUS and WATCHLIST candidates must survive in frozen state until the XI stage unless explicitly downgraded for new material evidence.

At XI, inspect:

- creators and finishers;
- defensive absences;
- formation / attacking shape;
- rotation and cohesion;
- bench vs starters;
- whether the frozen primary and secondary scoring routes remain credible.

Do not rebuild PRE from scratch merely because XI or price is now available.

### Rotation interpretation — v0.2.50

Do not downgrade merely because a lineup is rotated. Distinguish:

- `ROTATION — ATTACKING DEPTH PRESERVED` — equivalent senior attacking quality and coherent roles remain;
- `ROTATION — COHESION / ROUTE DAMAGE` — important routes or service materially weaken.

Only the second is an automatic burden downgrade.

### Frozen-state persistence rule

The Work structural board is a frozen PRE artifact. Publishing it to Airtable must be a **state copy/upsert, not a second structural screen**. Normal Chat should read that persisted frozen state for the later user-supplied XI/odds review.

If an Airtable row conflicts with the original frozen Work board, classify it as a persistence/synchronization fault; do not silently replace the frozen thesis with a newly reconstructed PRE.

---

## 10. v0.2.50 Extreme Goal Environment (EGE)

After confirmed XI, classify the goal-burden regime as either:

- `STANDARD`; or
- `EGE — EXTREME GOAL ENVIRONMENT`.

EGE normally requires **A1 FOCUS TWO-SIDED or A1 FOCUS ELITE CARRIER**. An A2 FOCUS may qualify only under the strict exception defined in `MODEL_RULES_FOOTBALL_V0.2.50.md`.

EGE must be supported independently by structure + team profile + XI. A high bookmaker line alone cannot create EGE.

If EGE clears:

- preserve the frozen PRE burden as history;
- create a documented post-XI `EGE supported burden`;
- the new burden may be above the frozen PRE band when structural evidence independently supports it;
- compare price only after this burden is set.

### Persistent High-Line Acceptance

A confirmed EGE match does **not** have to wait for an arbitrary absolute decay target.

If the current total is inside the independently supported EGE burden and odds are at least 1.65, the match may be locked prematch.

If the line is only 0.25 above EGE support, wait for a relative quarter-line improvement rather than requiring a return to the old frozen PRE range.

An early-goal expansion is never a reason to raise burden. Do not chase goal-driven line expansion.

---

## 11. User-supplied XI + odds — current execution policy

For the normal pre-kickoff workflow:

- do **not** automatically fetch confirmed lineups or bookmaker odds;
- the user supplies XI and odds later;
- until both required inputs are supplied, keep surviving candidates PROVISIONAL / HOLD;
- only search externally for XI/odds if the user explicitly asks for external verification;
- do not issue an OFFICIAL LOCK without the required current XI + executable price.

User screenshots/text are valid current evidence and should be matched to the frozen PRE state.

---

## 12. Executable price policy — current user overlay

- **Hard minimum decimal odds:** `1.65`
- **Preferred decimal odds:** `1.70+`
- odds below `1.65` → `NO BET — HOLD — PRICE TOO SHORT`
- never stretch to a higher Asian-total line merely to reach 1.65/1.70;
- choose a higher line only when the model independently supports the extra goal burden;
- structural ranking remains price-independent;
- protected Asian totals are preferred when they preserve the thesis at a reasonable price.

Goal burden/regime is chosen **after structure and XI** and **before price**.

v0.2.50 does not weaken this rule: EGE is a documented structural/XI burden re-open, not a price-driven stretch.

---

## 13. Official and shadow tracks

Use the same frozen evidence snapshot for all tracks:

- **Official:** Football v0.2.50
- **Shadow:** Football v0.2.47 CLEAN
- **Shadow:** Football v0.2.48-SHADOW

The v0.2.49 structural-priority patch and v0.2.50 EGE patch apply only to the official track. Shadow tracks remain version-faithful.

An affirmative final selection on the official track is an **OFFICIAL LOCK**. HOLD/PASS creates no official exposure. Shadow selections never enter official P/L.

Every material state must be logged with the model version that actually produced it.

---

## 14. Research policy

Once AiScore establishes a fixture, normal research may use the best available evidence from official sources, Soccerway, FotMob, FBref, BSD/Bzzoiro where supported, reputable statistics/news sources, and user-supplied screenshots.

Research can refine team profile, chance quality, incentives, tactical shape, confirmed XI, failure modes, EGE qualification, and market expression. Research sources cannot add a fixture to the universe without AiScore verification.

---

## 15. Live and settlement boundary

Live evidence validates or invalidates the frozen prematch thesis; it does not rewrite history.

The clean v0.2.47 halftime compression/saturation gate remains active where inherited and applicable. Manual live overrides must be separately labelled.

For EGE, a quiet 0-0 opening may corroborate persistent high-line calibration but does not create EGE by itself. An early goal never licenses immediate line chasing.

Standard full-match Asian totals settle on **90 minutes plus stoppage time** unless the market explicitly includes extra time.

Counterfactual simulations never enter official P/L.

---

## 16. Schedule-output rule

When the user asks for upcoming/next matches or a schedule:

- resolve current ICT time;
- read the frozen board;
- revalidate near-term AiScore status;
- exclude matches already LIVE/HT/FT/postponed/cancelled;
- convert raw UTC `Z` timestamps to ICT exactly once;
- sort by corrected ICT kickoff;
- show the date when crossing midnight or multiple ICT dates.

If the schedule cannot be reconciled, state:

`SCHEDULE INTEGRITY CHECK FAILED — revalidation required`

---

## 17. Authority and history

For current football decisions, this file and its canonical load order win over stale handoffs, old chat text, archived screenshots, or superseded documentation.

Historical model versions and removed rules remain recoverable from Git history; they are not retained in the active football tree as executable instructions.
