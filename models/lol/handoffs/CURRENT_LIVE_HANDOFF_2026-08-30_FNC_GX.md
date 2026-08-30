# Current Live Handoff — Fnatic vs GIANTX — 2026-08-30

**State only — not analytical authority**

## Series
- Competition: `LEC 2026 Summer`
- Stage: `Week 6 / Regular Season`
- Match: `Fnatic vs GIANTX`
- Format: `Bo3 Fearless Draft`
- Series score: `1-1`
- Game 1 winner: `GIANTX`
- Game 2 winner: `Fnatic`
- Current map: `Game 2 complete; prepare for deciding Game 3`
- Blue/Red Game 3: `not yet supplied`

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
- Accepted v1.3 samples remain: `ML_SAMPLE_N=3; DURATION_SAMPLE_N=0`

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

**Game 1 and Game 2 results do not change K/P0. Same-series outcomes and sportsbook prices are forbidden benchmark inputs.**

## Confirmed lineups
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

## Game 1 draft
GIANTX:
- Camille / Jarvan IV / Syndra / Ashe / Seraphine

Fnatic:
- Olaf / Skarner / Cassiopeia / Yunara / Lulu

## Game 2 draft
GIANTX:
- K'Sante / Maokai / Orianna / Kalista / Renata

Fnatic:
- Jayce / Wukong / Viktor / Xayah / Rakan

Game 2 draft prior used from GX perspective:
- `D=+1` — slight GIANTX draft edge.
- Main GX mechanism: Maokai + Orianna engage/control with Kalista/Renata follow-through and K'Sante frontline.
- Main FNC mechanism: Jayce/Viktor ranged resource pressure plus Xayah/Rakan counter-engage and scaling.

## Game 3 Fearless-consumed pool
Unavailable to either team in deciding Game 3:

`Camille / Jarvan IV / Syndra / Ashe / Seraphine / Olaf / Skarner / Cassiopeia / Yunara / Lulu / K'Sante / Maokai / Orianna / Kalista / Renata / Jayce / Wukong / Viktor / Xayah / Rakan`

## Game 2 observed decision windows
No Game 2 Position was accepted; every supplied ML state was PASS.

At `01:42`:
- 0-0 kills, no objectives, gold even.
- GX ML `1.791`, FNC `1.954`.
- GX state: `K=0; P0=50%; D=+1; R=0; X=0; O=0; T=0; C=+1.5`.
- Model GX `54.5%`; implied `55.83%`; edge `-1.33pp` -> PASS.

At `07:11`:
- 0-0 kills, GX first dragon, FNC about +0.6k gold.
- GX ML `2.037`, FNC `1.726`.
- GX state: `D=+1; R=-1; X=0; O=+1; T=0; C=+1.25`.
- Model GX `53.75%`; implied `49.09%`; edge `+4.66pp` -> PASS below +5.0pp threshold.

At `08:42`:
- GX 1-0 kills, GX 1-0 dragons, total gold effectively even.
- GX ML `1.708`, FNC `2.063`.
- GX state: `D=+1; R=0; X=+1; O=+1; T=0; C=+4.25`.
- Model GX `62.75%`; implied `58.55%`; edge `+4.20pp` -> PASS.

At `11:31`:
- GX 2-0 kills, 2-0 dragons, about +0.3k gold.
- GX ML `1.442`, FNC `2.654`.
- GX state: `D=+1; R=+1; X=+1; O=+1; T=+1; C=+6.75`.
- Model GX `70.25%`; implied `69.35%`; edge about `+0.9pp` -> PASS.

User later reported: `Fnatic won Game 2`.

Do not assign an audit taxonomy error solely because Fnatic won. No accepted Position existed. The observed GX early-state probabilities should remain available for later calibration review.

## Airtable Game 2 ledger
- Map ID: `LEC-2026-08-30-FNC-GX-G2`
- Map record: `recqLiwJDuZ2VjUHg`
- Snapshot 01:42: `recfVdzgeWRQZT7ZA`
- Snapshot 07:11: `rec2rH8IbZDtEGGVh`
- Snapshot 08:42: `recXLSDsw8MXV4Z8y`
- Snapshot 11:31: `recIsguUvkHH8hjf7`
- No Game 2 Position record exists.
- Final duration/full final scoreboard not supplied.

## Game 3 prep state
- Series is `1-1`.
- Freeze strength: `FNC K=0/P0=50%`, `GX K=0/P0=50%`.
- All 20 champions used in Games 1-2 are Fearless-consumed and unavailable to either side in Game 3.
- Once Game 3 sides/draft are known, verify none of the 20 consumed champions are selected and lock map-specific `D` price-blind.
- No immediate-postdraft TAKE.
- On synchronized Game 3 live state + market, score ML `D_eff/R/X/O/T`, selected-side `C`, probability, then price.
- If `C<=0`, selected side is PASS regardless of attractive odds.
- Duration independently scores `V/Q/H/T/F` before line/price.
- Verdict first and compact.
- Exact user line confirmation required before accepted Position.
- Defer Airtable writes until Game 3 map end.

## Bootstrap next continuation
Fetch default `models/lol/CURRENT_MODEL.md`, load `LOL_SESSION_BOOTSTRAP.md`, fetch lock `LOL-2026-08-30-V13-FNC-GX-BENCH-2254-UTC7`, re-fetch CURRENT_MODEL at authority `ce84ef31eb743e8002603cdd083c871c28787221`, load exact benchmark-aware v1.3 stack, then this or a newer FNC-GX handoff last.
