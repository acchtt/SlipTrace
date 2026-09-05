# Current Live Handoff — Gen.G vs Hanwha Life Esports — 2026-09-05

**Status:** ACTIVE SERIES HANDOFF — GAME 2 SETTLED / READY FOR GAME 3  
**Session lock:** `LOL-2026-09-05-V13-GEN-HLE-DRAFTONLY-FORCEDCHOICE-Q2-1306-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

- Gen.G vs Hanwha Life Esports — LCK 2026 Season Playoffs Upper Bracket Final, Bo5 Fearless Draft.
- G1 had no prospective canonical Position in this chat; do not create retroactive G1 Positions.
- G2 is settled and written to Airtable: GEN won `34-27` in `45:43`.
- Same-series results do not update K/P0/TK0; only Fearless champion availability may carry forward.
- Await G3 final draft + exact board before any new Position.

## Frozen benchmark

- `B(GEN)=+1.467332`
- `B(HLE)=+0.931313`
- `GAP(GEN-HLE)=+0.536019 SD`
- `GEN K=+1 / P0=55%`
- `HLE K=-1 / P0=45%`
- `TK0=26.95`
- benchmark windows: completed LCK 2026 Rounds 3-4 + Rounds 1-2; no playoff result or sportsbook price used.

## Game 2 draft and source-truth board

Role order TOP / JUNGLE / MID / ADC / SUPPORT.

GEN blue: `Rumble / Jarvan IV / Locke / Jhin / Shen`  
HLE red: `Ambessa / Qiyana / Syndra / Caitlyn / Bard`

Board:
- ML: GEN `1.678` / HLE `2.109`
- Duration `32.0`: Over `1.756` / Under `1.996`
- Total Kills `26.5`: Over `2.026` / Under `1.734`
- KH: GEN `-3.5 @1.753` / HLE `+3.5 @2.001`

Diagnostic draft label: `D=0 / EVEN-STYLE-DEPENDENT`; `D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`.

Locked card:
1. HLE ML @2.109 — `MODEL_EDGE=-2.42pp` — `FORCED_NEG_EV=YES`
2. HLE +3.5 @2.001 — raw/capped cover `62%`, edge `+12.02pp` — `FORCED_NEG_EV=NO`
3. Under 32 @1.996 — `V=0 Q=0 H=0 T=-1 F=30.25m`, edge `+12.15pp` — `FORCED_NEG_EV=NO`
4. Over 26.5 @2.026 — model `54%`, edge `+4.64pp`, one-sided-fast-close / return-kill-suppression branch `23%` — `FORCED_NEG_EV=NO`

## Game 2 final and settlement

User explicitly designated the supplied scoreboard as final.

Final:
- winner: **GEN**
- kills: **GEN 34-27 HLE**
- duration: **45:43**
- total kills: `61`
- GEN kill margin: `+7`

Settlement:
- HLE ML @2.109 — **LOSS** — `-0.2500u`
- HLE +3.5 @2.001 — **LOSS** — `-0.2500u`
- Under 32 @1.996 — **LOSS** — `-0.2500u`
- Over 26.5 @2.026 — **WIN** — `+0.2565u`

**G2 total: `1W-3L / -0.4935u`; actual exposure `0u`.**

Airtable map record `LCK-2026-09-05-GEN-HLE-G2` and four canonical Position records were created at map end.

## Game 2 micro-audit

- ML: diagnostic `D=0` was non-directional; Q2 benchmark-only HLE forced choice lost. No inference about draft coefficient because `D` contributed 0pp.
- KH: HLE +3.5 lost by a 7-kill GEN margin. The raw 62% cover read overestimated HLE margin resilience on this map, but the loss is not a 10+ tail miss.
- Duration: the principal miss. Draft-only `F=30.25m` and Under 32 were far below the realized `45:43`; repeated contact and game extension were materially underweighted in the pre-price clock read.
- TK: Over 26.5 won emphatically with `61` total kills; the high-contact / two-sided-brawl upper tail was realized rather than the one-sided fast-close suppression branch.
- No coefficient or architecture change before the preferred 80-position checkpoint absent a clear implementation bug.

## Cohort after Game 2

- `52 Positions / 13 per family`
- overall **`25W-27L / -1.26625u`**
- ML **`3-10 / -1.96425u`**
- KH **`6-7 / -0.41750u`**
- Duration **`9-4 / +0.98700u`**
- TK **`7-6 / +0.12850u`**
- actual exposure `0u`

Preferred next structural checkpoint remains `80 total Positions / 20 per family`.

## Game 3 workflow

1. Receive final G3 draft/roles + exact board.
2. Complete full DIM and all four price-blind projections first.
3. ML uses frozen P0 only; D remains diagnostic.
4. KH signed bins include both 10+ tails, 70% cap, and `<5 => ML-aligned` rule.
5. Duration keeps frozen v1.1 formula; Over selection gets warning tag.
6. TK keeps frozen TK0 and explicit one-sided-fast-close / return-kill-suppression mass.
7. Select exactly one ML/KH/Duration/TK line; `0.25u` shadow each / `0u` actual.
8. Airtable only at map end.
