# Football v2.0 — Chat Handoff — 2026-09-20 ICT

This handoff preserves the exact operating state after the **DECAY-FIRST BURDEN PROTECTION** correction. The next chat must continue from this state and must not drift back into using structural rank / HMA to justify worse goal burdens.

## 1. Canonical repo / active model

Repo: `acchtt/SlipTrace`, branch `main`.

Official track: **Football A**.  
Immediate parent: **v0.2.55** plus active Football A patches.

Read first:

1. `models/football/CURRENT_MODEL.md`
2. `models/football/rules/MODEL_RULES_FOOTBALL_AB_DECAY_FIRST_EXECUTION.md`
3. `models/football/rules/MODEL_RULES_FOOTBALL_A_LIVE_DECAY.md`
4. `models/football/rules/MODEL_RULES_FOOTBALL_A_HIGH_MARKET_ACCEPTANCE.md`
5. `models/football/rules/MODEL_RULES_FOOTBALL_AB_MARKET_ALIGNMENT.md`
6. `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md`
7. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`

Latest decay-first commits:
- new authority patch: `565e01e8709e261065f17660889c87a4acb4ec3f`
- CURRENT_MODEL latest: `a32e42658672ab7888039fda104442cb7408ad3d`
- HMA supersession notice: `7dd366dd5fb51fcbb50746efde715e0514005b98`
- live-decay target correction: `5ed51f40f8f0dbe3e9acc2b02ae48fdc686e5d02`
- XI/odds workflow: `d03bc5d8a9958ffe75f19d965d6972426fe0275b`
- betting procedure: `715bba7fb8aea91b743e7d82d037ca9601cde289`
- Sep19/20 override interaction: `5baef613646e029192d1d742326cc0900f0c38de`

Airtable model-control record for this patch:
- `recsrEGPeDCoEEEYH`

## 2. CRITICAL NEW RULE — DO NOT REPEAT THE OLD MISTAKE

The user identified a real selection inversion:

- high-ranked / strong-structure matches were being allowed to LOCK at O3.25–O4.0;
- lower-ranked but protected O2.5/O2.75 candidates were often HOLD;
- completed HOLDs were converting better than the official lock set.

The correction is now permanent/prospective:

`STRONGER STRUCTURE = MORE CONFIDENCE TO WAIT, NOT PERMISSION TO BUY A HIGHER TOTAL`

### Direct prematch lock

A direct prematch official lock requires:

- football/XI valid;
- market alignment clear;
- **selected line <= frozen supported execution burden**;
- price >= active floor;
- exposure gates clear;
- no suppression/compression veto.

### If market is above supported burden

Do **not** HMA-lock it.

Use:

`QUALIFIED — LIVE DECAY PLAN`

Freeze:
- lowest acceptable supported target line;
- minimum price;
- current line/price;
- cancellation condition.

Examples:
- support O2.75, market O3.25 -> **WAIT O2.75**
- support O3.0, market O3.5 -> **WAIT O3.0**
- support O3.0–3.25, market O3.75 -> normally target lowest independently supported line, not the HMA boundary.

### HMA after this patch

Football A HMA can no longer create automatic prematch exposure above burden.

HMA is now only a **monitoring/audit tolerance overlay**:
- it may keep a strong A1/A2/CC+ fixture worth monitoring;
- it may not raise the official entry target.

### Model B after this patch

Model B also becomes decay-first:
- +0.25/+0.50/+0.75 participation allowances cannot create direct prematch exposure above frozen burden;
- those fixtures become **MODEL B — QUALIFIED LIVE DECAY**;
- Model B exposure slots are not pre-reserved by rank for above-burden fixtures;
- only actual executable exposures count against any cap.

Structural Rank orders review. It does not grant burden permission.

## 3. WAIT / HOLD classification — mandatory

Do not collapse qualified execution problems into HOLD.

Use:

- supported line available + price clears -> **LOCK / direct eligible**
- supported line available + price below floor -> **WAIT — PRICE BELOW FLOOR**
- current line above supported burden -> **WAIT — LIVE DECAY**
- football/XI/evidence itself fails -> **STRUCTURAL HOLD**
- frozen real PASS with no valid reopen -> **PASS**

Every WAIT shown to the user must include:
- target line;
- minimum price;
- current line/price;
- cancellation condition.

A WAIT must remain visible until it executes, is invalidated, or expires.

## 4. O3.0+ suppression screen

Before any supported O3.0+ execution, explicitly check:

1. recent same-opponent H2H;
2. recent **same-venue** H2H;
3. whether low-total history matches the current failure mechanism;
4. recent conversion stability / independent scoring-route quality.

Do not let long-run H2H averages wash out a recent same-venue suppression pattern.

This was missed in:
- KR Reykjavik–Vikingur;
- Stuttgart–Dortmund.

## 5. Active temporary Sep19/20 rule

Until **2026-09-21 00:00 ICT**, the temporary burden-specific upper-tail relaxation remains active:

- O2.5: quality-proven **3+ path** is enough;
- O2.75: robust **3+ path + non-trivial fourth-goal support**;
- O3.0+: normal strict 4+ / TRUE CC+ / elite two-sided standard;
- B+/B/PASS remain outside the automatic temporary relaxation.

Interaction with decay-first:

`QUALIFY LOWER PROTECTED BURDEN -> WAIT IF MARKET IS HIGHER -> EXECUTE ONLY WHEN PROTECTED BURDEN APPEARS`

Early-conversion score-epoch rule remains active for eligible A1/A2 FOCUS matches. If a goal comes before the 0-0 decay target, the old target expires and the score epoch must be re-priced. Do not chase the expanded total.

## 6. Other active workflow patches that remain in force

### No cross-match suppression
A match is not blocked because another higher-ranked match is active, waiting, or already exposed.

### User prematch odds auto-publish
Any user-supplied prematch odds screenshot/text is treated as currently executable for that evidence epoch.

If all gates clear at a supported burden:
- finalize **OFFICIAL LOCK** immediately;
- create Website Pick immediately;
- default 1u unless user says otherwise;
- do not ask a second “take it / publish it / still available?” question.

### One exposure per match
Still mandatory.

### Netherlands Eerste Divisie
Official Eerste Divisie fixtures involving Jong/U21/reserve-branded teams are included in the normal sweep.

## 7. Why the decay-first correction was made

Current Sep19 official settled set at the time of correction:

- KR–Vikingur O4.0 @1.71 -> LOSS
- ADO–Cambuur O3.0 @1.73 -> LOSS
- Molde–Aalesund O3.75 @1.67 -> LOSS
- Roma–Inter O2.75 @1.71 -> WIN
- Luzern–Grasshopper O3.5 @1.78 -> WIN
- Stuttgart–Dortmund O3.25 @1.66 -> LOSS
- Sparta–Heerenveen O3.25 @1.84 -> WIN

Settled official subset: **3W–4L, -1.67u**.

Completed HOLD board at audit:
- Brighton–Arsenal O2.5 -> WIN
- Newcastle–Hull O2.75 -> HALF WIN
- Dundee–Motherwell O2.5 -> WIN
- HSV–Köln O2.75 -> HALF WIN
- Paris FC–Strasbourg O2.75 -> HALF WIN
- Young Boys–Servette O3.5 -> WIN
- Odense–Midtjylland -> LOSS
- Hibernian–Aberdeen -> LOSS

Counterfactual HOLD performance was about **+1.285u**.

Main diagnosis:
- false negatives: protected lower-burden A2/B+ opportunities filtered too aggressively;
- false positives: high confidence was being used to tolerate inflated O3.25–O4 burdens.

Do not “solve” this by betting every HOLD. The correction is **burden discipline + explicit decay WAITs**.

## 8. Model B audit conclusion

A retrospective Model B shadow re-screen showed that several old HOLDs would have become eligible, but the old rank-first max-six logic still concentrated selection in high-ranked high-burden matches.

Airtable Model B audit:
- `recrDwaHCXLE9Izkx`

The new decay-first patch fixes the key execution problem:
- no above-burden direct participation;
- no rank-first pre-reservation of Model B slots for above-burden fixtures.

Do not use the old Model B rank-first shortlist as authority after this patch.

## 9. Current session states to revalidate immediately in the new chat

Do not assume these are still prematch/live. Revalidate status before acting.

### Official picks not settled in Airtable at last handoff sync
- **Ajax–Excelsior — O3.5 @1.74, 1u**
- **Sevilla–Barcelona — O3.5 @1.76, 1u**

These were created before the decay-first patch. Do not retroactively cancel/rewrite them; settle normally from actual result.

### Last active WAIT
- **Anderlecht–Zulte**
  - frozen #13 B+ WATCHLIST / carrier-led
  - same-source bullish price hardener cleared B+ positive gate
  - last board O2.5 @1.63 / O2.75 @1.79 / O3 @2.06
  - **WAIT target: O2.5 >=1.65**
  - revalidate match state before execution.

### Current structural HOLD/PASS examples
- Motor Lublin–Gornik: HOLD, same-venue suppression + weak secondary route
- KA Akureyri–Thor: HOLD, strong same-venue suppression + Nordic false-positive risk
- Willem II–Fortuna: PASS after high-market conflict re-screen; current form bullish but no valid carrier reopen

### Schedule item that may still need Step-2 review
- **Sion–Zurich #10 A2 FOCUS** was on the published board; no persisted XI/odds assessment was found in this chat. Revalidate fixture status before doing anything.

## 10. Nordic warning — audit signal, not yet a blanket exclusion

Recent settled Nordic official sample logged:
- Fredrikstad–Sarpsborg O2.5 LOSS
- Djurgardens–GAIS O2.75 LOSS
- Vejle–Brondby O2.5 WIN
- KR–Vikingur O4 LOSS
- Molde–Aalesund O3.75 LOSS

Audit: **1W–4L, -3.15u**.

Do not create a blanket Nordic PASS unless the user explicitly promotes that safeguard. But for Nordic candidates, take same-venue H2H, route independence and conversion stability seriously; do not let league scoring reputation / huge market totals erase matchup-specific suppression.

Airtable Nordic audit:
- `recrAeaEMw5OLClhT`

## 11. Airtable

Base: `appWyZJjitSBATXAU`

Tables:
- Coverage: `tblcl1UAyMqZT6Ub0`
- Decision States: `tblQmUpd5WjBLQ38X`
- Website Picks: `tblg3J5sbJYbzuTYD`

Important control rows:
- auto-publish patch: search `MODEL PATCH — Auto-Publish User Prematch Odds`
- restored WAIT process: `rec9vyKWtOrjgoOaY`
- decay-first patch: `recsrEGPeDCoEEEYH`
- Model B shadow reassessment: `recrDwaHCXLE9Izkx`
- Nordic audit: `recrAeaEMw5OLClhT`

Search Airtable before reconstructing official bets or results.

## 12. New-chat operating instruction

When the user sends XI + odds:

1. read frozen PRE;
2. assess XI football-first;
3. attempt market history;
4. run same-venue suppression screen;
5. identify supported burden;
6. compare current market with supported burden;
7. **if market > supported burden -> WAIT, do not HMA-lock**;
8. if target line exists but price is short -> price WAIT;
9. only lock when protected supported burden is actually executable and all gates clear;
10. auto-publish immediately when it does;
11. never allow Structural Rank to justify a worse line.

The mistake to avoid is explicit:

**DO NOT TURN “BEST MATCH” INTO “HIGHEST TOTAL WE ARE WILLING TO BUY.”**

This handoff is continuity only. Canonical repo files remain the final authority.
