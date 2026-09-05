# Current Live Handoff — Gen.G vs Hanwha Life Esports — 2026-09-05

**Status:** ACTIVE SERIES HANDOFF — GAME 3 SETTLED / READY FOR GAME 4  
**Session lock:** `LOL-2026-09-05-V13-GEN-HLE-DRAFTONLY-FORCEDCHOICE-Q2-1306-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

- Gen.G vs Hanwha Life Esports — LCK 2026 Season Playoffs Upper Bracket Final, Bo5 Fearless Draft.
- G1 had no prospective canonical Position in this chat; no retroactive G1 Positions.
- G2 settled: GEN won `34-27` in `45:43`; card `1-3 / -0.4935u`; Airtable written.
- G3 settled: GEN won `26-9` in `31:20`; card `2-2 / -0.09675u`; Airtable written.
- Same-series results do not update `K/P0/TK0`; only Fearless champion availability may carry forward.
- Await G4 final draft + exact board before any new Position.

## Frozen benchmark

- `B(GEN)=+1.467332`
- `B(HLE)=+0.931313`
- `GAP(GEN-HLE)=+0.536019 SD`
- `GEN K=+1 / P0=55%`
- `HLE K=-1 / P0=45%`
- `TK0=26.95`

## Game 3 draft and source-truth board

Role order TOP / JUNGLE / MID / ADC / SUPPORT.

HLE blue: `Camille / Pantheon / Ahri / Ziggs / Pyke`  
GEN red: `Gwen / Aatrox / Akali / Ashe / Seraphine`

Board:
- ML: GEN `1.703` / HLE `2.069`
- Duration `32.0`: Over `1.803` / Under `1.939`
- Total Kills `27.5`: Over `1.674` / Under `2.114`
- KH: GEN `-3.5 @1.816` / HLE `+3.5 @1.924`

Diagnostic draft label: `D=+1 HLE`; `D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`.

Locked card:
1. HLE ML @2.069 — `MODEL_EDGE=-3.33pp` — `FORCED_NEG_EV=YES`
2. HLE +3.5 @1.924 — raw/capped cover `63%`, edge `+11.02pp` — `FORCED_NEG_EV=NO`
3. Under 32 @1.939 — `V=+1 Q=0 H=0 T=0 F=29.50m`, edge `+15.93pp` — `FORCED_NEG_EV=NO`
4. Over 27.5 @1.674 — model `62%`, edge `+2.26pp`, one-sided-fast-close / return-kill-suppression branch `18%` — `FORCED_NEG_EV=NO`

## Game 3 final and settlement

User explicitly designated supplied scoreboard as final.

Final:
- winner: **GEN**
- kills: **GEN 26-9 HLE**
- duration: **31:20**
- total kills: `35`
- GEN kill margin: `+17`
- scoreboard also showed towers `10-3 GEN`, dragons `4-0 GEN`, barons `2-0 GEN`, inhibitors `2-0 GEN`.

Settlement:
- HLE ML @2.069 — **LOSS** — `-0.2500u`
- HLE +3.5 @1.924 — **LOSS** — `-0.2500u`
- Under 32 @1.939 — **WIN** — `+0.23475u`
- Over 27.5 @1.674 — **WIN** — `+0.16850u`

**G3 total: `2W-2L / -0.09675u`; actual exposure `0u`.**

Airtable map record `LCK-2026-09-05-GEN-HLE-G3` and four canonical Position records were created at map end.

## Game 3 micro-audit

- ML: diagnostic `D=+1 HLE` was directionally wrong; Q2 correctly prevented it from moving ML probability, but forced-choice HLE ML still lost from the benchmark-price comparison.
- KH: HLE +3.5 lost by `17`; the realized GEN 10+ clean-cascade branch was far more severe than the locked `15%` tail mass. This is another margin-tail compression miss, but the 70% cap remains active and no coefficients change before checkpoint.
- Duration: Under 32 won narrowly at `31:20`; the `F=29.50m` compression direction was correct, though realized duration was 1:50 above F.
- TK: Over 27.5 won with `35`; the high-contact upper branch was realized despite the one-sided fast-close branch.
- No coefficient or architecture change before the preferred 80-position checkpoint absent a clear implementation bug.

## Cohort after Game 3

- `56 Positions / 14 per family`
- overall **`27W-29L / -1.36300u`**
- ML **`3-11 / -2.21425u`**
- KH **`6-8 / -0.66750u`**
- Duration **`10-4 / +1.22175u`**
- TK **`8-6 / +0.29700u`**
- actual exposure `0u`

Preferred next structural checkpoint remains `80 total Positions / 20 per family`.

## Game 4 workflow

1. Receive final G4 draft/roles + exact board.
2. Complete full DIM and all four price-blind projections first.
3. ML uses frozen P0 only; D remains diagnostic.
4. KH signed bins include both 10+ tails, 70% cap, and `<5 => ML-aligned` rule.
5. Duration keeps frozen v1.1 formula; Over selection gets warning tag.
6. TK keeps frozen TK0 and explicit one-sided-fast-close / return-kill-suppression mass.
7. Select exactly one ML/KH/Duration/TK line; `0.25u` shadow each / `0u` actual.
8. Airtable only at map end.
