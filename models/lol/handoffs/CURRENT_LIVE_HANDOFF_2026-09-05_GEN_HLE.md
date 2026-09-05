# Current Live Handoff — Gen.G vs Hanwha Life Esports — 2026-09-05

**Status:** SERIES COMPLETE — GEN 3-1 HLE / G4 SETTLED / Q2 VALIDATION  
**Session lock:** `LOL-2026-09-05-V13-GEN-HLE-DRAFTONLY-FORCEDCHOICE-Q2-1306-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series closure

Gen.G defeated Hanwha Life Esports **3-1** in the LCK 2026 Season Playoffs Upper Bracket Final.

Prospective canonical positions existed only for G2-G4 in this chat. G1 remains uncounted and must not be reconstructed retroactively.

- G2: GEN won `34-27` in `45:43`; card `1-3 / -0.49350u`.
- G3: GEN won `26-9` in `31:20`; card `2-2 / -0.09675u`.
- G4: GEN won `24-12` in `26:52`; card `4-0 / +0.82475u`.

Recorded GEN-HLE block: **`7W-5L / +0.23450u`** across 12 positions.  
Actual exposure: `0u`.

All G2-G4 map and position records are written to Airtable. No additional GEN-HLE position may be created under this lock.

## Frozen benchmark used for the series

- `B(GEN)=+1.467332`
- `B(HLE)=+0.931313`
- `GAP(GEN-HLE)=+0.536019 SD`
- `GEN K=+1 / P0=55%`
- `HLE K=-1 / P0=45%`
- `TK0=26.95`

Same-series results never changed these frozen values.

## Game 4 source-truth draft and board

Role order TOP / JUNGLE / MID / ADC / SUPPORT.

GEN blue: `Varus / Vi / Vex / Miss Fortune / Neeko`  
HLE red: `Nasus / Naafiri / Sylas / Kalista / Renata Glasc`

Board:
- ML: GEN `1.786` / HLE `1.959`
- Duration `32.0`: Over `1.903` / Under `1.836`
- Total Kills `30.5`: Over `1.816` / Under `1.925`
- KH: GEN `-3.5 @1.861` / HLE `+3.5 @1.876`

Diagnostic draft: `D=+1 GEN`; `D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`.

Locked G4 card:
1. GEN ML @1.786 — edge `-0.99pp` — `FORCED_NEG_EV=YES`
2. GEN -3.5 @1.861 — raw/capped cover `44%`, edge `-9.73pp` — `FORCED_NEG_EV=YES`; selected because `<5 => ML-aligned`
3. Under 32 @1.836 — `V=+1 Q=0 H=0 T=0 F=29.50m`, edge `+13.03pp` — `FORCED_NEG_EV=NO`
4. Over 30.5 @1.816 — model `58%`, edge `+2.93pp`, one-sided-fast-close / return-kill-suppression mass `17%` — `FORCED_NEG_EV=NO`

## Game 4 final and settlement

User explicitly designated the supplied scoreboard as final despite the source panel still displaying a live/pending label.

Final:
- winner: **GEN**
- kills: **GEN 24-12 HLE**
- duration: **26:52**
- total kills: `36`
- GEN kill margin: `+12`
- visible objectives: towers `9-3 GEN`, dragons `3-1 GEN`, barons `1-0 GEN`, inhibitors `2-0 GEN`.

Settlement:
- GEN ML @1.786 — **WIN** — `+0.19650u`
- GEN -3.5 @1.861 — **WIN** — `+0.21525u`
- Under 32 @1.836 — **WIN** — `+0.20900u`
- Over 30.5 @1.816 — **WIN** — `+0.20400u`

**G4 total: `4W-0L / +0.82475u`.**

## G4 micro-audit

- ML: diagnostic `D=+1 GEN` was directionally correct, while Q2 correctly kept the forced-choice ML probability at frozen `P0=55%`.
- KH: GEN -3.5 won by 12 despite the model assigning only 44% cover probability. This is a favorable realization of the GEN 10+ clean-cascade tail, not evidence to refit from one map.
- Duration: Under 32 won comfortably at `26:52`; the `F=29.50m` compression read was directionally and materially correct.
- TK: Over 30.5 won with 36 kills. Fast conversion and high-contact continuation coexisted; the one-sided suppression branch did not prevent the total from clearing.
- No coefficient or architecture change before the planned 80-position checkpoint absent a clear implementation bug.

## Cohort after GEN-HLE G4

- `60 Positions / 15 per family`
- overall **`31W-29L / -0.53825u`**
- ML **`4-11 / -2.01775u`**
- KH **`7-8 / -0.45225u`**
- Duration **`11-4 / +1.43075u`**
- TK **`9-6 / +0.50100u`**
- actual exposure `0u`

Preferred next structural checkpoint remains:
- `80 total Positions / 20 per family`;
- **5 additional fully recorded maps / 20 positions** from this closure state.

## Next-series requirement

This handoff is historical and closed. Before any further LCK position:
1. identify the next current series fresh;
2. build a fresh pre-series Gol.gg benchmark;
3. write a fresh Session Authority Lock explicitly carrying the Q2 forced-choice overlay if still intended.

If no fresh lock exists: `MODEL REBUILD IN PROGRESS — HOLD`.
