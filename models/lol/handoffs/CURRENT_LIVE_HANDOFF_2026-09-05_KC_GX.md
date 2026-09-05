# Current Live Handoff — Karmine Corp vs GIANTX — 2026-09-05

**Status:** ACTIVE SERIES HANDOFF — G1/G2/G3 SETTLED / KC LEADS 2-1 / AWAIT G4  
**Session lock:** `LOL-2026-09-05-V13-LEC-KC-GX-DRAFTONLY-FORCEDCHOICE-Q2-1950-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / ML FLOOR 1.45 / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

Karmine Corp vs GIANTX — LEC 2026 Summer Playoffs Upper Bracket Round 1, Bo5 Fearless Draft.

- G1 final: **KC won 12-8 in 40:40**.
- G2 final: **GX won 22-12 in 37:42**.
- G3 final: **KC won 14-1 in 26:27**.
- Series score after G3: **KC 2-1 GX**.
- User explicitly designated the supplied G3 screenshot as final; this overrides the source panel still showing LIVE/result pending.
- G1/G2/G3 map records and all 12 canonical positions are written to Airtable.
- Same-series results do not update frozen `K/P0/TK0`; prior maps may inform only Fearless champion availability.
- User-directed ML floor remains active as last explicitly stated: selected Moneyline must be `>=1.45`; no rule change has yet been explicitly requested.

## Frozen benchmark

- `B(KC)=+1.625030`
- `B(GX)=-0.241316`
- `GAP(KC-GX)=+1.866346 SD`
- `KC K=+2 / P0=60%`
- `GX K=-2 / P0=40%`
- `TK0=28.50`

## Game 1 settled

1. GX ML @3.522 — LOSS — `-0.25000u`
2. GX +8.5 @1.868 — WIN — `+0.21700u`
3. Over 32 @1.904 — WIN — `+0.22600u`
4. Over 25.5 @1.869 — LOSS — `-0.25000u`

**G1: `2W-2L / -0.05700u`.**

## Game 2 settled

1. GX ML @3.305 — WIN — `+0.57625u`
2. GX +8.5 @1.831 — WIN — `+0.20775u`
3. Under 32 @1.691 — LOSS — `-0.25000u`
4. Over 24.5 @1.735 — WIN — `+0.18375u`

**G2: `3W-1L / +0.71775u`.**

## Game 3 settled

Draft source truth:
- GX blue: `Olaf / Trundle / Viktor / Caitlyn / Bard`
- KC red: `Vayne / Naafiri / Ryze / Yunara / Lulu`

Board:
- ML KC `1.307` / GX `3.274`
- Duration 32.0: Over `1.694` / Under `2.083`
- Total Kills 24.5: Over `1.878` / Under `1.843`
- KH KC `-8.5 @1.979` / GX `+8.5 @1.770`

Locked card:
1. GX ML @3.274
2. GX +8.5 @1.770
3. Over 32 @1.694
4. Over 24.5 @1.878

Final supplied by user:
- winner: **Karmine Corp**
- kills: **KC 14-1 GX**
- duration: **26:27**
- total kills: `15`
- KC kill margin: `+13`

Settlement:
1. GX ML @3.274 — LOSS — `-0.25000u`
2. GX +8.5 @1.770 — LOSS — `-0.25000u`
3. Over 32 @1.694 — LOSS — `-0.25000u`
4. Over 24.5 @1.878 — LOSS — `-0.25000u`

**G3: `0W-4L / -1.00000u`.**

G3 micro-audit:
- Diagnostic `D=0` did not select a side, but the frozen underdog ML tail failed badly as KC won by 13 kills.
- GX +8.5 suffered a clean-tail miss; the 70% capped cover estimate was not realized.
- Duration Over 32 failed via a 26:27 one-sided close despite the pre-price `F=33.75m` extension read.
- TK Over 24.5 failed with only 15 kills; the explicit `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` branch was realized more severely than its locked 20% mass.
- No architecture/coefficient change before the 80-position checkpoint absent a clear implementation bug.

## KC-GX tracked block through G3

- `12 positions`
- `5W-7L`
- `-0.33925u`
- actual exposure `0u`

## Cohort after Game 3

- `76 Positions / 19 per family`
- overall **`38W-38L / -0.98225u`**
- ML **`5-14 / -2.19150u`**
- KH **`10-9 / -0.06200u`**
- Duration **`13-6 / +1.33650u`**
- TK **`10-9 / -0.06525u`**
- actual exposure `0u`

Preferred checkpoint remains `80 positions / 20 per family`: **one additional fully recorded map / four positions**.

## Game 4 workflow

1. Receive final G4 draft/roles + exact board.
2. Complete full price-blind DIM and all four family projections.
3. ML uses frozen `P0`; `D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`; selected ML must be `>=1.45` under the currently active floor rule.
4. KH signed margin bins include both 10+ tails and the 70% execution cap; `<5` must align with selected ML; `±5.5+` may diverge.
5. Duration keeps the frozen 31m-anchor formula.
6. TK keeps frozen `TK0=28.50` with explicit one-sided-fast-close / return-kill-suppression mass.
7. Exactly one ML/KH/Duration/TK line, `0.25u` shadow each / `0u actual`.
8. Airtable only at map end.
9. G4 settlement reaches the planned `80 positions / 20 per family` structural checkpoint and should trigger the checkpoint audit before any subsequent structural change.
