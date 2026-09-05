# Current Live Handoff — Karmine Corp vs GIANTX — 2026-09-05

**Status:** ACTIVE SERIES HANDOFF — G1/G2 SETTLED / SERIES 1-1 / AWAIT G3  
**Session lock:** `LOL-2026-09-05-V13-LEC-KC-GX-DRAFTONLY-FORCEDCHOICE-Q2-1950-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / ML FLOOR 1.45 / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

Karmine Corp vs GIANTX — LEC 2026 Summer Playoffs Upper Bracket Round 1, Bo5 Fearless Draft.

- G1 final: **KC won 12-8 in 40:40**.
- G2 final: **GX won 22-12 in 37:42**.
- Series score after G2: **1-1**.
- User explicitly designated both supplied screenshots as final; for G2 this overrides the source panel still showing LIVE/result pending.
- G1 and G2 map records plus all 8 canonical positions are written to Airtable.
- Same-series results do not update frozen `K/P0/TK0`; prior maps may inform only Fearless champion availability.
- User-directed ML floor remains active: selected Moneyline must be `>=1.45`.

## Frozen benchmark

- `B(KC)=+1.625030`
- `B(GX)=-0.241316`
- `GAP(KC-GX)=+1.866346 SD`
- `KC K=+2 / P0=60%`
- `GX K=-2 / P0=40%`
- `TK0=28.50`

## Game 1 settled

Draft:
- KC blue: `Jayce / Jarvan IV / Anivia / Ashe / Seraphine`
- GX red: `Yorick / Skarner / Cassiopeia / Lucian / Milio`

Board:
- ML KC `1.272` / GX `3.522`
- Duration `32.0`: Over `1.904` / Under `1.835`
- Total Kills `25.5`: Over `1.869` / Under `1.851`
- KH KC `-8.5 @1.869` / GX `+8.5 @1.868`

Locked card and settlement:
1. GX ML @3.522 — **LOSS** — `-0.25000u`
2. GX +8.5 @1.868 — **WIN** — `+0.21700u`
3. Over 32 @1.904 — **WIN** — `+0.22600u`
4. Over 25.5 @1.869 — **LOSS** — `-0.25000u`

**G1: `2W-2L / -0.05700u`.**

Micro-audit:
- Diagnostic `D=0` remained non-directional.
- GX +8.5 covered because KC kill margin was only +4.
- Duration Over was correct at 40:40.
- TK Over missed badly with only 20 kills despite the long game; this is a low-contact/return-kill-suppression realization rather than a fast-close realization.

## Game 2 settled

Draft:
- KC blue: `Gnar / Wukong / Akali / Ezreal / Rell`
- GX red: `Ambessa / Sejuani / Orianna / Kai'Sa / Nautilus`

Board:
- ML KC `1.302` / GX `3.305`
- Duration `32.0`: Over `2.088` / Under `1.691`
- Total Kills `24.5`: Over `1.735` / Under `2.004`
- KH KC `-8.5 @1.908` / GX `+8.5 @1.831`

Locked card and settlement:
1. GX ML @3.305 — **WIN** — `+0.57625u`
2. GX +8.5 @1.831 — **WIN** — `+0.20775u`
3. Under 32 @1.691 — **LOSS** — `-0.25000u`
4. Over 24.5 @1.735 — **WIN** — `+0.18375u`

**G2: `3W-1L / +0.71775u`.**

Micro-audit:
- Diagnostic `D=0` remained non-directional; GX won outright despite frozen KC 60% prior.
- GX +8.5 won outright, strongly realizing the underdog/wide-cover branch.
- Duration Under 32 missed materially at 37:42; pre-map compression understated extension risk.
- TK Over 24.5 won with 34 total kills.

## KC-GX tracked block through G2

- `8 positions`
- `5W-3L`
- `+0.66075u`
- actual exposure `0u`

## Cohort after G2

- `72 Positions / 18 per family`
- overall **`38W-34L / +0.01775u`**
- ML **`5-13 / -1.94150u`**
- KH **`10-8 / +0.18800u`**
- Duration **`13-5 / +1.58650u`**
- TK **`10-8 / +0.18475u`**
- actual exposure `0u`

Preferred checkpoint remains `80 positions / 20 per family`: **2 additional fully recorded maps / 8 positions**.

## Game 3 workflow

1. Receive final G3 draft/roles + exact board.
2. Complete full price-blind DIM and all four family projections.
3. ML uses frozen `P0`; `D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`; selected ML must be `>=1.45`.
4. KH signed margin bins include both 10+ tails and the 70% execution cap; `<5` must align with ML; `±5.5+` may diverge.
5. Duration keeps the frozen 31m-anchor formula.
6. TK keeps frozen `TK0=28.50` with explicit one-sided-fast-close / return-kill-suppression mass.
7. Exactly one ML/KH/Duration/TK line, `0.25u` shadow each / `0u actual`.
8. Airtable only at map end.
