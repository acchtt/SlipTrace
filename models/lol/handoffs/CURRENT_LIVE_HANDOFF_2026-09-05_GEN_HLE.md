# Current Live Handoff — Gen.G vs Hanwha Life Esports — 2026-09-05

**Status:** ACTIVE SERIES HANDOFF — PRE-GAME 1 / Q2 VALIDATION  
**Session lock:** `LOL-2026-09-05-V13-GEN-HLE-DRAFTONLY-FORCEDCHOICE-Q2-1306-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

- Gen.G vs Hanwha Life Esports — LCK 2026 Season Playoffs Upper Bracket Final, Bo5 Fearless Draft.
- Scheduled 2026-09-05 08:00 UTC / 15:00 UTC+7.
- No current-series Position exists yet.
- No Airtable write before map end.
- Same-series results never update K/P0/TK0; they may affect only Fearless champion availability.

## Frozen benchmark

- `B(GEN)=+1.467332`
- `B(HLE)=+0.931313`
- `GAP(GEN-HLE)=+0.536019 SD`
- `GEN K=+1 / P0=55%`
- `HLE K=-1 / P0=45%`
- `TK0=26.95`
- Current benchmark windows: completed LCK 2026 Rounds 3-4 plus Rounds 1-2.
- GEN and HLE both use normal 70/30 current/previous roster-continuity blend.
- Prior playoff results, sportsbook prices and current-series results are excluded from benchmark construction.

Current-window core inputs:
- GEN: 19 games, WR 63.2%, GDM +91, GD@15 +638, Towers 6.5-5.3, DRA 55.6%, NASH 48.0%; TK environment 23.6.
- HLE: 21 games, WR 52.4%, GDM +56, GD@15 +596, Towers 6.3-5.4, DRA 48.7%, NASH 49.1%; TK environment 30.3.

Previous-window split scores / current-window split scores:
- `B_current(GEN)=+1.043999`, `B_previous(GEN)=+1.253139`, raw 70/30 `+1.106741`.
- `B_current(HLE)=+0.501517`, `B_previous(HLE)=+1.135456`, raw 70/30 `+0.691699`.

## Expected primary rosters

GEN: Kiin / Canyon / Chovy / Ruler / Duro.  
HLE: Zeus / Kanavi / Zeka / Gumayusi / Delight.

HLE Bluffing is a support sub in Gol.gg data; Delight remains the primary starter. User-supplied final map roles/lineup override saved context if contradictory.

## Q2 forced-choice controls

- exactly one canonical position in each family: ML / KH / Duration / Total Kills;
- 0.25u shadow each / 0u actual;
- final draft + exact board are the only prediction inputs; ignore displayed live state;
- full DIM mandatory;
- diagnostic `D` persists but `D_PROBABILITY_CONTRIBUTION=0` for forced-choice ML;
- ML forced-choice probability = frozen P0 only;
- KH full signed margin bins before price, both 10+ tails explicit, execution probability capped at 70%;
- KH `<5` kills must align with selected ML side; `±5.5+` may be independent;
- Duration v1.1 anchor/formula frozen; selected Over gets `OVER_BRANCH_WARNING=YES`;
- TK full bins must include explicit numeric `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` branch;
- price cannot change any price-blind projection;
- every selected side tagged `MODEL_EDGE` and `FORCED_NEG_EV=YES/NO`;
- Airtable only at map end.

## Cohort entering series

Corrected forced-choice cohort:
- `48 Positions / 12 per family`
- `24W-24L / -0.77275u`
- ML `3-9 / -1.71425u`
- KH `6-6 / -0.16750u`
- Duration `9-3 / +1.23700u`
- TK `6-6 / -0.12800u`
- actual exposure `0u`.

Next preferred checkpoint:
- `80 Positions / 20 per family`;
- `8 fully recorded maps / 32 Positions` remaining.

KT-DK G4 no longer carries a DATA-INTEGRITY MISMATCH tag; the later Renekton reassessment left all corrected canonical picks unchanged. The sportsbook line-transcription correction remains historical documentation only.

## Game workflow

1. Receive final map draft in exact role order plus exact sportsbook board.
2. Build DIM and all four price-blind projections first.
3. Select exactly one canonical side/line per family.
4. First visible line: `[Map]: ML / KH / Duration / Total Kills — 1.00u shadow total.`
5. Persist compact audit state.
6. Do not write Airtable until map final.
