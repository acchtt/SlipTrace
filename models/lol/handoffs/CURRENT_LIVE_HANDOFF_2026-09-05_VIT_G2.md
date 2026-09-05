# Current Live Handoff — Team Vitality vs G2 Esports — 2026-09-05

**Status:** ACTIVE SERIES HANDOFF — GAME 3 SETTLED / AWAIT NEXT MAP OR SERIES-END CONFIRMATION  
**Session lock:** `LOL-2026-09-05-V13-LEC-VIT-G2-DRAFTONLY-FORCEDCHOICE-Q2-1903-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

- Team Vitality vs G2 Esports — LEC 2026 Summer Playoffs Upper Bracket Round 1, Bo5 Fearless Draft.
- G1/G2 occurred before this lock and remain same-series history only; no retroactive positions.
- G3 was prospectively locked and is now settled; Airtable map + four canonical positions are written.
- Same-series results do not update `K/P0/TK0`; prior maps may inform only Fearless champion availability where structurally needed.
- Do not infer final series score from the G3 result alone; await next-map or explicit series-end confirmation.

## Frozen benchmark

- `B(G2)=+1.000135`
- `B(VIT)=+0.917530`
- `GAP(G2-VIT)=+0.082605 SD`
- `G2 K=0 / P0=50%`
- `VIT K=0 / P0=50%`
- `TK0=29.25`

## Game 3 draft and board

Role order TOP / JUNGLE / MID / ADC / SUPPORT.

G2 blue: `Olaf / Pantheon / LeBlanc / Xayah / Rakan`  
VIT red: `Trundle / Cho'Gath / Hwei / Lucian / Milio`

Board:
- ML: G2 `1.446` / VIT `2.640`
- Duration `33.0`: Over `2.047` / Under `1.719`
- Total Kills `26.5`: Over `1.832` / Under `1.889`
- KH: G2 `-6.5 @1.876` / VIT `+6.5 @1.862`

Diagnostic draft: `D=+1 VIT`; `D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`.

Locked card:
1. VIT ML @2.640 — model `50%`, edge `+12.12pp` — `FORCED_NEG_EV=NO`
2. VIT +6.5 @1.862 — raw cover `76%`, Q2 capped `70%`, edge `+16.29pp` — `FORCED_NEG_EV=NO`
3. Under 33 @1.719 — `V=+1 Q=0 H=0 T=+1 F=30.25m`, edge `+11.08pp` — `FORCED_NEG_EV=NO`
4. Over 26.5 @1.832 — model `66%`, edge `+11.41pp`, one-sided-fast-close / return-kill-suppression mass `17%` — `FORCED_NEG_EV=NO`

## Game 3 final and settlement

User explicitly designated supplied scoreboard as final.

Final:
- winner: **G2 Esports**
- kills: **G2 15-10 VIT**
- duration: **29:07**
- total kills: `25`
- G2 kill margin: `+5`
- scoreboard also showed towers `10-3 G2`, dragons `2-2`, barons `2-0 G2`, inhibitors `2-0 G2`.

Settlement:
- VIT ML @2.640 — **LOSS** — `-0.25000u`
- VIT +6.5 @1.862 — **WIN** — `+0.21550u`
- Under 33 @1.719 — **WIN** — `+0.17975u`
- Over 26.5 @1.832 — **LOSS** — `-0.25000u`

**G3 total: `2W-2L / -0.10475u`; actual exposure `0u`.**

Airtable map `LEC-2026-09-05-VIT-G2-G3` and four canonical position records were created at map end.

## Game 3 micro-audit

- ML: diagnostic `D=+1 VIT` was directionally wrong as G2 won. Q2 still kept draft from moving ML probability, but frozen `P0=50%` plus price selected VIT and lost.
- KH: VIT +6.5 covered despite losing the map because the final kill margin was only `5`; the wide-handicap margin-compression branch was realized.
- Duration: Under 33 won comfortably at `29:07`; `F=30.25m` was directionally sound.
- TK: Over 26.5 missed narrowly with `25` total kills; the lower one-sided-fast-close / return-kill-suppression side of the distribution was realized.
- No coefficient or architecture change before the planned 80-position checkpoint absent a clear implementation bug.

## Cohort after Game 3

- `64 Positions / 16 per family`
- overall **`33W-31L / -0.64300u`**
- ML **`4-12 / -2.26775u`**
- KH **`8-8 / -0.23675u`**
- Duration **`12-4 / +1.61050u`**
- TK **`9-7 / +0.25100u`**
- actual exposure `0u`

Preferred next structural checkpoint remains `80 total / 20 per family`, requiring **4 additional fully recorded maps / 16 positions**.

## Next-map workflow

1. Receive final next-map draft/roles + exact board.
2. Complete full price-blind DIM and all four family projections.
3. ML uses frozen `P0`; D remains diagnostic only.
4. KH signed bins include both 10+ tails and 70% cap; `<5` must align with ML, `±5.5+` may diverge.
5. Duration keeps frozen 31m-anchor formula.
6. TK keeps frozen `TK0=29.25` with explicit one-sided-fast-close / return-kill-suppression mass.
7. Select exactly one ML/KH/Duration/TK line; `0.25u` shadow each / `0u` actual.
8. Airtable only at map end.
