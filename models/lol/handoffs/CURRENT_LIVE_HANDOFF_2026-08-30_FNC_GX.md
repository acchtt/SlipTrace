# Current Live Handoff — Fnatic vs GIANTX — 2026-08-30

**State only — not analytical authority**

## Series
- Competition: `LEC 2026 Summer`
- Stage: `Week 6 / Regular Season`
- Match: `Fnatic vs GIANTX`
- Format: `Bo3 Fearless Draft`
- Series score: `GIANTX 1-0 Fnatic`
- Current map: `Game 1 complete — GIANTX won`
- Requested workflow: `prepare for Game 2`
- Blue/Red Game 2: `not yet supplied`

## Active authority
- Model: `LoL v1.3 — Hierarchy Moneyline + Duration Core`
- Active lock: `LOL-2026-08-30-V13-FNC-GX-BENCH-2254-UTC7`
- Frozen authority commit: `ce84ef31eb743e8002603cdd083c871c28787221`
- Team benchmark: `Gol.gg league-relative benchmark ACTIVE`
- Causal thesis gate: `selected-side C>0; price cannot create the bet`
- Circuit breaker: `CLEAR`
- Active markets: `Moneyline + Duration Over/Under`
- KH/TK: `RETIRED_FROM_BETTING`
- Actual exposure: `0u`
- Shadow stake: `0.25u`
- Minimum odds: `1.60`
- ML edge threshold: `+5.0pp`
- Duration edge threshold: `+7.5pp`
- Accepted v1.3 samples entering series: `ML_SAMPLE_N=3; DURATION_SAMPLE_N=0`

## Frozen team benchmark
Pre-series-only Gol.gg LEC Summer + Spring data, with roster-continuity adjustment.

Fnatic:
- `B_current=-0.134`
- `B_previous=-0.261`
- one starter change `Empyros -> Soboro`
- adjusted blend `85/15`
- `B_raw=-0.153`
- final league-relative `B≈-0.165`

GIANTX:
- `B_current=-0.330`
- `B_previous=-0.283` descriptive only
- two starter changes `Lot -> Oscarinin`, `Noah -> Flakked`
- current split only under benchmark procedure
- `B_raw=-0.330`
- final league-relative `B≈-0.361`

Pairwise FNC gap:
`+0.196 SD`

Frozen strength prior:
- Fnatic `K=0 / P0=50%`
- GIANTX `K=0 / P0=50%`

**Game 1 result does not change K/P0. Same-series outcomes and sportsbook prices are forbidden benchmark inputs.**

## Confirmed current lineups from user Game 1 scoreboard
Fnatic:
- Soboro — top
- Razork — jungle
- Vladi — mid
- Upset — bot
- Lospa — support

GIANTX:
- Oscarinin — top
- ISMA — jungle
- Jackies — mid
- Flakked — bot
- Jun — support

## Game 1 confirmed draft / Fearless pool
GIANTX:
- Oscarinin — `Camille`
- ISMA — `Jarvan IV`
- Jackies — `Syndra`
- Flakked — `Ashe`
- Jun — `Seraphine`

Fnatic:
- Soboro — `Olaf`
- Razork — `Skarner`
- Vladi — `Cassiopeia`
- Upset — `Yunara`
- Lospa — `Lulu`

### Game 2 Fearless-consumed champions
Unavailable to either team in Game 2:

`Camille / Jarvan IV / Syndra / Ashe / Seraphine / Olaf / Skarner / Cassiopeia / Yunara / Lulu`

## Game 1 result / ledger
- User reported: `GIANTX won Game 1`.
- No Game 1 betting Position existed.
- Final duration/full final scoreboard not supplied.
- Airtable Map: `LEC-2026-08-30-FNC-GX-G1` / record `rec4cAfXn6Hn7g4Ev`.
- Airtable prep snapshot at `18:14`: record `recdnY77GZ3xq2aXZ`.

At the prep snapshot `18:14`:
- kills: `GIANTX 4 - 8 Fnatic`
- towers: `1-1`
- dragons: `GIANTX 2 - 1 Fnatic`
- barons: `0-0`
- inhibitors: `0-0`
- displayed overall gold lead: about `Fnatic +2.5k`

## Game 2 prep state
- Series score is `GX 1-0 FNC`, but this does **not** alter benchmark `K/P0`.
- Freeze strength: `FNC K=0/P0=50%`, `GX K=0/P0=50%`.
- Consumed pool is fully resolved.
- Once Game 2 sides/draft are known, verify none of the 10 consumed champions are selected and lock map-specific `D` price-blind.
- No immediate-postdraft TAKE.
- On synchronized Game 2 live state + market, score ML `D_eff/R/X/O/T`, selected-side `C`, probability, then price.
- If `C<=0`, selected side is PASS regardless of attractive odds.
- Duration independently scores `V/Q/H/T/F` before line/price.
- Verdict first and compact.
- Exact user line confirmation required before accepted Position.
- Defer Airtable writes until Game 2 map end.

## Bootstrap next continuation
Fetch default `models/lol/CURRENT_MODEL.md`, load `LOL_SESSION_BOOTSTRAP.md`, fetch lock `LOL-2026-08-30-V13-FNC-GX-BENCH-2254-UTC7`, re-fetch CURRENT_MODEL at authority `ce84ef31eb743e8002603cdd083c871c28787221`, load exact benchmark-aware v1.3 stack, then this or a newer FNC-GX handoff last.
