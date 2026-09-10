# SlipTrace Football Chat Operating Protocol

**Status:** ACTIVE  
**Authoritative model entry point:** `models/football/CURRENT_MODEL.md`

Purpose: enforce the same current football state across ChatGPT chats without reconstructing rules, boards, or kickoff times from memory.

---

## 1. Authority order

For current football work:

1. **GitHub `acchtt/SlipTrace`** — model rules, procedures, time/schedule policy, and durable operating policy.
2. **Frozen Work PRE artifact persisted to Airtable Daily Coverage Ledger** — current slate/board bridge.
3. **Airtable Decision States** — later material XI/market/live assessments.
4. **User-supplied current screenshots/text** — XI, odds, and live market evidence when supplied.

Always load `models/football/CURRENT_MODEL.md` first. Do not select an old model version from memory or an old chat handoff.

Always apply `models/football/procedures/FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md` before presenting schedules or trusting near-kickoff stored timestamps.

If a current Airtable coverage row demonstrably conflicts with the original frozen Work board, treat it as a persistence synchronization fault and preserve the original frozen Work PRE until corrected.

---

## 2. Current model routing

- **Official:** Football v0.2.50
- **Base:** v0.2.47 CLEAN
- **Official patches:** v0.2.49 Two-Sided Priority + v0.2.50 Extreme Goal Environment / Persistent High-Line
- **Shadow:** v0.2.47 CLEAN
- **Shadow:** v0.2.48-SHADOW

For comparable official grades:

`TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER`

Do not apply the v0.2.49 or v0.2.50 patches to the shadow models.

---

## 3. Fixture coverage rule

Fixture discovery is **AiScore only**.

Do not use a multi-source fixture union. Other providers may support match research only after AiScore establishes the fixture.

For any ICT window that crosses midnight, explicitly traverse every AiScore date listing touched by the window and verify the terminal cutoff block before claiming completeness.

Every discovered fixture must pass the canonical time chain:

`AiScore identity → kickoff_utc → one conversion to kickoff_ict → slate_date_ict → status revalidation`

If traversal is incomplete:

`COVERAGE INCOMPLETE — AiScore sweep incomplete`

If date/time identity is contradictory:

`UNRESOLVED — SCHEDULE INTEGRITY`

---

## 4. Timezone and schedule non-negotiable

Canonical timezone is `Asia/Ho_Chi_Minh` (ICT, UTC+7).

- A timestamp ending in `Z` is UTC, never ICT.
- Airtable may return UTC `Z` even when the field displays in ICT.
- Convert a raw UTC value to ICT exactly once.
- Never add +7 to a value already expressed in ICT.
- Derive `Slate Date` from the ICT-converted kickoff.

When the user asks for `upcoming`, `next matches`, or a schedule:

1. resolve current ICT time;
2. read the frozen board;
3. revalidate near-term fixtures against AiScore;
4. remove LIVE/HT/FT/postponed/cancelled matches from the upcoming list;
5. sort by corrected ICT kickoff;
6. show the date when the list crosses midnight or multiple ICT dates.

A stored Airtable timestamp alone is not sufficient to call a near-term fixture upcoming.

---

## 5. Current actionable competition overlay

Exclude from the normal actionable board:

- youth/Uxx (U17/U18/U19/U20/U21/U23);
- academy/junior;
- reserve/B-team/development;
- amateur/semi-pro;
- regional/state/provincial;
- very small/obscure weak-data leagues;
- domestic lower divisions below top flight unless explicitly approved/whitelisted;
- all Finnish domestic league competitions at every tier/category from 2026-09-09 ICT onward.

Do not weaken the overlay to fill the slate.

Do not inherit old generic continental/cup exclusions. Senior first-team competitions such as UEFA Champions League, UEFA Europa League and UEFA Conference League are actionable when otherwise eligible.

---

## 6. Current production workflow

`AiScore universe → time/schedule integrity → quality filter → Work price/XI-blind structural screen → frozen FOCUS/WATCHLIST board → Airtable publish → user supplies XI + odds → Normal Chat XI rerank → STANDARD/EGE burden → official v0.2.50 LOCK/HOLD/PASS`

Work publication to Airtable is a state copy/upsert, **not a second structural model run**.

---

## 7. User-supplied XI + odds policy

Normal Chat does not automatically fetch confirmed XI or bookmaker odds.

- user supplies XI + odds;
- only search externally when the user explicitly asks for verification;
- no OFFICIAL LOCK without required current XI + executable price;
- if missing, state `WAITING FOR USER XI/ODDS — NO OFFICIAL DECISION`.

Current executable price policy:

- hard floor 1.65;
- preferred 1.70+;
- never stretch the total merely to improve price.

---

## 8. v0.2.50 goal-burden regime

After confirmed XI classify:

- `STANDARD`; or
- `EGE — EXTREME GOAL ENVIRONMENT`.

EGE is normally for A1 FOCUS TWO-SIDED / ELITE CARRIER cases, with the strict A2 exception defined in the active rule file.

A high bookmaker total alone does not create EGE. Structure + team profile + XI must independently justify the higher burden.

When EGE clears:

- preserve frozen PRE burden;
- document a new post-XI EGE supported burden;
- if the current total is inside that burden and price clears 1.65, a prematch lock is allowed;
- do not wait for an arbitrary absolute decay target;
- if only 0.25 above support, use relative quarter-line decay;
- never chase goal-driven line expansion.

---

## 9. Pre-verdict discipline

Before a material verdict:

- resolve the fixture against frozen PRE;
- verify official model version;
- verify corrected current fixture time/status when near kickoff;
- review team GF/GA/profile and chance-quality support as required by the active rules;
- rerank from confirmed XI;
- classify rotation as attacking-depth-preserved vs cohesion/route damage;
- identify the main failure mode;
- choose STANDARD or EGE burden before price;
- apply current price policy;
- log the material assessment under the model version that produced it.

Price cannot rescue weaker structure.

---

## 10. Record separation

- **Daily Coverage Ledger:** complete-slate coverage + frozen PRE bridge + schedule correction notes.
- **Decision States:** later material XI/market/live STANDARD/EGE assessment epochs and official/shadow evidence.
- **Official picks/ledger path:** actual official LOCK exposure and settlement according to the current repository contract.
- **GitHub:** current model and durable procedures.

Do not rewrite frozen PRE with a later assessment.

---

## 11. Live and settlement boundary

Live evidence validates or invalidates the frozen thesis; it does not rewrite prematch history.

A quiet opening may corroborate a pre-established EGE burden; it cannot create EGE by itself.

An early goal is not permission to chase an expanded total.

Shadow/counterfactual/HOLD selections never enter official P/L.

Standard full-match Asian totals settle on 90 minutes + stoppage time unless the market explicitly includes extra time.

---

## 12. Cross-chat non-negotiable

When connected sources can be queried, do not reconstruct authoritative football state from conversational memory.

Load the current repo, read the persisted frozen slate, apply time/schedule integrity, then apply the user’s current evidence.
