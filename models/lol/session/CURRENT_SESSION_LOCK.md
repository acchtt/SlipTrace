# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-05-V13-GEN-HLE-DRAFTONLY-FORCEDCHOICE-Q2-1306-UTC7`  
**Status:** `CLOSED — SERIES COMPLETE`  
**Scope:** `LCK 2026 Season Playoffs — Upper Bracket Final — Gen.G vs Hanwha Life Esports — Bo5 Fearless Draft`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution overlay:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE`  
**Actual exposure:** `0u`

## Final series state

Gen.G defeated Hanwha Life Esports **3-1**.

Prospective tracked maps under this lock:
- G2: `1-3 / -0.49350u`
- G3: `2-2 / -0.09675u`
- G4: `4-0 / +0.82475u`

GEN-HLE tracked block: **`7-5 / +0.23450u`** across 12 positions.

G1 had no prospective canonical position in this chat and remains uncounted.

## Final cohort state

- `60 Positions / 15 per family`
- overall `31W-29L / -0.53825u`
- ML `4-11 / -2.01775u`
- KH `7-8 / -0.45225u`
- Duration `11-4 / +1.43075u`
- TK `9-6 / +0.50100u`
- actual exposure `0u`

Preferred next checkpoint: `80 positions / 20 per family`, requiring 5 additional fully recorded maps / 20 positions.

## Historical frozen benchmark

For this completed series only:
- `GEN B=+1.467332 / K=+1 / P0=55%`
- `HLE B=+0.931313 / K=-1 / P0=45%`
- `GAP GEN-HLE=+0.536019 SD`
- `TK0=26.95`

Do not reuse these values for another series.

## Closure rule

No additional GEN-HLE position may be created under this lock.

Before any next LCK position:
1. identify the next series fresh;
2. compute a fresh pre-series Gol.gg benchmark with same-series and sportsbook data excluded;
3. write and verify a new active Session Authority Lock;
4. explicitly re-activate the Q2 forced-choice overlay if it is to continue.

Until that is complete: `MODEL REBUILD IN PROGRESS — HOLD`.

Historical handoff:
`models/lol/handoffs/CURRENT_LIVE_HANDOFF_2026-09-05_GEN_HLE.md`
