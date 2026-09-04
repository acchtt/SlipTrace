# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-04-V13-KT-DK-DRAFTONLY-FORCEDCHOICE-Q2-1955-UTC7`  
**Status:** `CLOSED — SERIES COMPLETE`  
**Scope:** `LCK 2026 Season Playoffs — Lower Bracket Round 2 — KT Rolster vs Dplus KIA — Bo5 Fearless Draft`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Actual exposure:** `0u`

## Closure

- Final series score: **Dplus KIA 3-1 KT Rolster**.
- No additional Position may be created under this lock.
- G3-G4 canonical Positions are settled and written to Airtable.
- G1-G2 remain uncounted because no prospective final draft + exact board was supplied; no retroactive Positions were created.

Cohort after series:
- `48 Positions / 12 per family`;
- overall `22W-26L / -1.76975u`;
- ML `3-9 / -1.7315u`;
- KH `5-7 / -0.6505u`;
- Duration `9-3 / +1.26175u`;
- TK `5-7 / -0.6495u`;
- actual exposure `0u`.

## Data-integrity exception

G4 was entered and priced on the user-supplied draft `DK Jax / Vi / Annie / Miss Fortune / Neeko` vs `KT Gwen / Skarner / Akali / Kalista / Renata`, but the final scoreboard shows DK top **Renekton**, not Jax.

Governance treatment:
- settle G4 Positions as entered because map/market/final-result identity is clear;
- retain their historical P/L in the forced-choice ledger;
- tag the map and all four G4 records `DATA-INTEGRITY MISMATCH`;
- exclude G4 from clean champion-draft / DIM calibration evidence;
- do not infer coefficient changes from this contaminated map.

## Frozen benchmark historical record

- `B(DK)=+0.355702`
- `B(KT)=-1.465479`
- `GAP(DK-KT)=+1.821180 SD`
- `DK K=+2 / P0=60%`
- `KT K=-2 / P0=40%`
- `TK0=25.45`

These values are historical to this closed series and must not be reused for a new matchup.

## Q2 overlay state for future fresh lock

Canonical `CURRENT_MODEL.md` remains unchanged. A future fresh forced-choice lock may continue the checkpoint quarantine only if it explicitly activates it:
- full DIM required;
- `D_DIAGNOSTIC_ONLY=YES`;
- `D_PROBABILITY_CONTRIBUTION=0` for forced-choice ML;
- KH `<5` must align with ML; `±5.5+` may be independent;
- `KH_MODEL_PROB_CAP=70%`;
- Duration formula frozen with diagnostic Over warning;
- TK explicit one-sided fast-close / return-kill-suppression branch;
- exactly one canonical ML/KH/Duration/TK position per executable map;
- `0.25u shadow / 0u actual`;
- `MODEL_EDGE` + `FORCED_NEG_EV` tags;
- Airtable only at map end.

Preferred structural checkpoint remains `80 total Positions / 20 per family`, with G4 flagged as contaminated for draft-calibration analysis.

## Mandatory next-session behavior

Before any new LoL Position:
1. bootstrap from `models/lol/CURRENT_MODEL.md` and `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
2. observe this lock is CLOSED and do not reuse it;
3. identify the current match fresh;
4. build a fresh price-independent Gol.gg benchmark;
5. create a fresh Session Authority Lock for that match;
6. load the newest applicable handoff last.

If no fresh lock exists: `MODEL REBUILD IN PROGRESS — HOLD`.
