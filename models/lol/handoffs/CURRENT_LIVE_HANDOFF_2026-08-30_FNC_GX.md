# Current Live Handoff — Fnatic vs GIANTX — 2026-08-30

**State only — not analytical authority**

## Series
- Competition: `LEC 2026 Summer`
- Stage: `Week 6 / Regular Season`
- Match: `Fnatic vs GIANTX`
- Format: `Bo3 Fearless Draft`
- Scheduled: `2026-08-30 23:30 UTC+7 / 18:30 CEST`
- Series score: `0-0 / pre-series`
- Current map: `Game 1 not started`
- Blue/Red: `not supplied`

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

Same-series outcomes and sportsbook prices cannot change K/P0.

## Expected lineups — live card overrides
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

## Workflow
1. Receive Blue/Red and exact Game 1 draft.
2. Lock map-specific draft `D` price-blind.
3. No immediate-postdraft TAKE.
4. On synchronized live state + market, score ML `D_eff/R/X/O/T`, selected-side `C`, probability, then price.
5. If `C<=0`, selected side is PASS regardless of attractive odds.
6. Duration independently scores `V/Q/H/T/F` before line/price.
7. Verdict first and compact.
8. Exact user line confirmation required before accepted Position.
9. Defer Airtable writes until map end.

## Bootstrap next continuation
Fetch default `models/lol/CURRENT_MODEL.md`, load `LOL_SESSION_BOOTSTRAP.md`, fetch lock `LOL-2026-08-30-V13-FNC-GX-BENCH-2254-UTC7`, re-fetch CURRENT_MODEL at authority `ce84ef31eb743e8002603cdd083c871c28787221`, load exact benchmark-aware v1.3 stack, then this or a newer FNC-GX handoff last.
