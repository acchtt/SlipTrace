# Football Decision States — Airtable Contract

**Status:** ACTIVE  
**Base:** `SlipTrace Football Decision Control`  
**Table:** `Decision States`  
**Official model:** Football v0.2.50  
**Shadow comparison models:** v0.2.47 CLEAN and v0.2.48-SHADOW

This table records material football assessment states after the frozen coverage/PRE stage. It must preserve version fidelity and must not rewrite historical PRE state.

---

## 1. Model/version rule

Every material record must identify the model version that actually produced it.

Current tracks:

- **Official:** `Football v0.2.50`
- **Shadow:** `Football v0.2.47 CLEAN`
- **Shadow:** `Football v0.2.48-SHADOW`

Historical v0.2.49 decisions remain v0.2.49. Do not relabel them as v0.2.50.

Do not import the v0.2.49 Two-Sided Priority or v0.2.50 EGE patch into either shadow track.

---

## 2. Frozen PRE dependency

Before a later XI/market assessment is written, resolve the fixture against the frozen Work PRE state persisted in `Daily Coverage Ledger`.

Preserve:

- original PRE grade;
- original structural archetype;
- original FOCUS/WATCHLIST/PASS/UNRESOLVED state;
- original primary/secondary routes and failure mode where available;
- original frozen structural burden.

A Decision State may record a later downgrade/rerank or v0.2.50 EGE burden re-open, but it must not imply that the later state was the original PRE.

If the coverage row demonstrably conflicts with the original Work artifact, classify a persistence sync fault and use the original frozen Work thesis until the bridge is corrected.

---

## 3. Time and fixture-identity rule

Decision States must resolve against the corrected fixture identity and time contract in `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`.

When a serialized timestamp ends in `Z`, treat it as UTC and convert to ICT exactly once for display.

If a material decision is made near kickoff, confirm the fixture is actually in the expected PRE/LIVE state rather than trusting a stale stored schedule.

A later schedule correction does not rewrite the timestamp/evidence state that actually existed when the historical decision was made; annotate the correction separately.

---

## 4. Material assessment fields

Use the existing schema to record material state, including where applicable:

- `Assessment ID`;
- `Match`;
- `Competition`;
- `Model Version`;
- `Assessment Time`;
- `Minute`;
- `Score`;
- `Reset Epoch`;
- `Assessment Period`;
- `Verdict`;
- `Candidate`;
- `Line`;
- `Odds`;
- `Goal Environment`;
- synchronized/reset fields;
- competition-format / utility checks when relevant;
- xG/chance-quality role;
- primary evidence channels;
- failure-mode / favorite-fade / directional-persistence fields where applicable;
- market scan status where applicable;
- validator result;
- fail reasons;
- evidence summary.

Use provider/evidence-version fields when the decision depends on an external normalized evidence snapshot.

---

## 5. v0.2.50 STANDARD / EGE recording

For material official v0.2.50 decisions, record in `Evidence Summary` and/or available environment fields whether the goal-burden regime is:

- `STANDARD`; or
- `EGE — EXTREME GOAL ENVIRONMENT`.

For EGE, preserve explicitly:

- frozen PRE burden;
- new post-XI EGE supported burden;
- structural/team/XI reasons for reopening the burden;
- current market line/price;
- whether execution is `EGE DIRECT` or `EGE RELATIVE DECAY`;
- main failure mode and why it remains acceptable.

A high market line alone must never be documented as the reason EGE was created.

Use audit labels where useful:

- `STANDARD DIRECT`
- `STANDARD DECAY`
- `EGE DIRECT`
- `EGE RELATIVE DECAY`
- `NON-DECAY HOLD`
- `GOAL-EXPANSION HOLD`

---

## 6. User-supplied XI + odds workflow

Current normal prematch execution expects the user to supply confirmed XI and odds.

When a user screenshot/text is the current evidence:

- treat it as the evidence input for that assessment epoch;
- match it to the frozen PRE fixture;
- record the actual line/odds evaluated;
- do not fabricate missing market data;
- do not automatically search for missing XI/odds unless the user explicitly requests external verification.

If either required final input is missing:

`WAITING FOR USER XI/ODDS — NO OFFICIAL DECISION`

---

## 7. Current decision order

Official v0.2.50 material decisions follow:

`STRUCTURAL QUALITY → CARRIER CEILING → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE QUALITY → XI RERANK → GOAL BURDEN / REGIME → PRICE → LOCK / HOLD`

For comparable official grades:

`TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER`

Price cannot rescue weaker structure.

---

## 8. Price policy in final assessment

Current user overlay:

- hard minimum decimal odds = `1.65`;
- preferred = `1.70+`;
- below 1.65 = `NO BET — HOLD — PRICE TOO SHORT`;
- do not stretch the Asian-total line merely to obtain a better price;
- higher burden must be independently supported by structure + XI;
- under EGE, the reopened burden must be set before price is evaluated.

Record the line actually selected/evaluated, not merely the bookmaker’s headline total.

---

## 9. Official verdict semantics

### Official v0.2.50

- affirmative final selection = **OFFICIAL LOCK**;
- HOLD/PASS = no official exposure.

### Shadows

Shadow selections are comparison states only. They do not enter official P/L and do not suppress the official v0.2.50 verdict.

When all three tracks are materially assessed, create/version the states so the evidence snapshot is comparable but each model remains identifiable.

---

## 10. Synchronization rule

For a material three-track comparison, all tracks should use the same underlying fixture/XI/market evidence epoch where possible.

Synchronize:

- match identity;
- assessment time;
- score/minute for live assessments;
- XI evidence;
- evaluated line and current price snapshot;
- relevant team/chance-quality evidence.

Version-specific conclusions may differ. Evidence synchronization does not mean verdict synchronization.

---

## 11. Live-state rules

Live evidence validates or invalidates the frozen prematch thesis; it does not rewrite PRE history.

Use reset/synchronization fields when score/minute/market state materially changes.

For inherited v0.2.47 halftime logic, use the existing HT fields where applicable:

- `HT Goals`;
- `HT Saturation Gate`;
- `Conversion Quality Gate`;
- `Second-Half Hazard`;
- `Remaining Goal Budget`.

For EGE, a quiet opening may corroborate a previously established high-line calibration, but an early goal must not be used to justify chasing an expanded line. Record such states as `GOAL-EXPANSION HOLD` when applicable.

Manual live overrides must be separately labelled.

---

## 12. Result/P&L boundary

Only official selections that actually became official exposure belong in official result/P&L accounting.

Do not convert:

- HOLD;
- PASS;
- shadow;
- counterfactual;
- missed-opportunity review

into official P/L.

Standard full-match Asian totals settle on 90 minutes + stoppage time unless the market explicitly includes extra time.

---

## 13. Coverage vs Decision States

`Daily Coverage Ledger` = fixture coverage + frozen PRE bridge.

`Decision States` = material later assessment epochs, including v0.2.50 STANDARD/EGE state, plus official/shadow verdict evidence.

Do not use a later Decision State to overwrite what the frozen Work PRE originally was.
