# Current Live Handoff — Team Heretics vs Movistar KOI — 2026-08-30

**State only — not analytical authority**

## Series
- Competition: `LEC 2026 Summer`
- Stage: `Week 6 / Regular Season`
- Match: `Team Heretics vs Movistar KOI`
- Format: `Bo3 Fearless Draft`
- Scheduled: `2026-08-30 21:15 UTC+7 / 16:15 CEST`
- Series score: `not supplied / do not infer`
- Current map: `Game 2 completed — Movistar KOI won`
- Blue/Red: `not explicitly supplied; do not infer from scoreboard orientation`

## Active model
- Model: `LoL v1.3 — Hierarchy Moneyline + Duration Core`
- Active lock: `LOL-2026-08-30-V13-TH-MKOI-BENCH-2248-UTC7`
- Frozen authority commit: `ce84ef31eb743e8002603cdd083c871c28787221`
- Team benchmark: `Gol.gg league-relative benchmark ACTIVE`
- Circuit breaker: `CLEAR`
- Active markets: `Moneyline + Duration Over/Under`
- Kill Handicap / Total Kills: `RETIRED_FROM_BETTING`
- Actual exposure: `0u`
- Shadow stake: `0.25u`
- Minimum odds: `1.60`
- ML edge threshold: `+5.0pp`
- Duration edge threshold: `+7.5pp`
- Accepted v1.3 samples after Game 2: `ML_SAMPLE_N=3; DURATION_SAMPLE_N=0`

## Prospectively active team benchmark
User authorized replacing loose subjective team tiering with our own Gol.gg-derived benchmark.

Formula:

`B_split = 0.30*z(WinRate) + 0.30*z(GDM) + 0.20*z(GD@15) + 0.10*z(TowerDiff/Game) + 0.05*z(DRA%) + 0.05*z(NASH%)`

Current/previous split blend by current games:
- 15+: 70/30
- 8-14: 55/45
- under 8: 40/60
subject to roster continuity.

Re-standardize blended peer scores. Pairwise final gap maps to K:
- `<0.50 SD` -> K=0
- `0.50-<1.25 SD` -> K=±1
- `>=1.25 SD` -> K=±2

No sportsbook price or same-series result enters the benchmark.

### TH vs MKOI reconstructed pre-series benchmark
Current LEC Summer pre-series values used:
- MKOI: `20 games | WR 40.0% | GDM -21 | GD@15 +912 | towers 5.6-6.5 | DRA 56.3% | NASH 43.3%`
- TH: `17 games | WR 23.5% | GDM -176 | GD@15 -1262 | towers 3.5-7.8 | DRA 40.0% | NASH 25.0%`

Split scores:
- current: `MKOI +0.018 | TH -1.355`
- previous Spring: `MKOI +0.758 | TH -1.696`

70/30 raw blend:
- `MKOI +0.240`
- `TH -1.457`

Final league-standardized blend:
- `MKOI +0.262`
- `TH -1.590`

Pairwise gap from MKOI perspective:
`+1.852 SD`

Prospectively frozen for remainder of series:
- `MKOI K=+2 / P0=60%`
- `TH K=-2 / P0=40%`

Earlier TH @3.396 position remains historical under the prior K construction and is not rewritten.

## Prospectively active execution gate
User instruction after Game 2:

> Do not take a bet just because the price looks good.

For selected ML side:

`C = 1.5*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`

Require:
- `C>0` before price is betting evidence;
- coherent, currently reachable draft/live win mechanism;
- strength prior alone cannot satisfy gate;
- if `C<=0`, `PASS` even if apparent edge exceeds +5pp.

## Confirmed live lineups from Game 2 scoreboard
TH:
- Tracyn — top
- Daglas — jungle
- Serin — mid
- Hype — ADC
- Way — support

MKOI:
- Myrwn — top
- Elyoya — jungle
- Jojopyun — mid
- Supa — ADC
- Alvaro — support

## Game 2 draft
TH:
- Aatrox / Xin Zhao / Syndra / Ezreal / Karma

MKOI:
- Ambessa / Skarner / Viktor / Ashe / Seraphine

Game 2 draft prior used from TH perspective:
- `D=-1` — MKOI draft edge.
- Mechanism initially `INTACT`.

## Game 2 confirmed position and settlement
Decision window at `03:50`:
- kills `0-0`
- towers `0-0`
- dragons `0-0`
- barons `0-0`
- MKOI about `+322g`

Historical state/rules at entry:
- TH `K=-1 / P0=45%`
- `D=-1, MC=INTACT, R=-1, X=0, O=0, T=0`
- old-rule model TH `36.0%`
- TH @3.396 implied `29.45%`, old edge `+6.55pp`
- user confirmed exact line
- result `LOSS`, shadow `-0.25u`, actual `0u`

Under the new causal gate this state would fail because TH `C=-3.0`. Under the new benchmark, TH would also start from `P0=40%`. Do not retroactively alter the historical accepted record.

Airtable map-end logging completed:
- Position `recxJWOaEYGhaf0N4`
- Map `recaTAM7cHvQAZOmC`
- Snapshot `receTc67nmlpfuhhW`

## Validation running context
Known v1.3 ML positions:
1. KT ML @4.259 vs DK — WIN `+0.81475u`
2. DK ML @3.114 vs KT — LOSS `-0.25u`
3. TH ML @3.396 vs MKOI — LOSS `-0.25u`

Running known v1.3 ML shadow P/L: `+0.31475u`.

## User workflow preference
- `VERDICT FIRST`, compact.
- No Airtable writes during map; log at map end.
- Exact confirmation required before accepted Position.
- Never TAKE from price alone.

## Next workflow
1. If series continues, receive series score/map and Blue/Red.
2. Resolve Fearless consumed pool from Games 1-2; Game 1 draft/result still needs supply if unavailable.
3. Use frozen `MKOI K=+2 / TH K=-2` from benchmark.
4. Lock map-specific D price-blind after draft; no immediate-postdraft TAKE.
5. On synchronized live state + market, score ML state and selected-side C before price.
6. Duration unchanged.
7. Verdict first, compact.
8. Candidate requires exact line confirmation; material state change expires it.
9. Defer Airtable writes to map end.

## Bootstrap next continuation
Fetch default `models/lol/CURRENT_MODEL.md`, load `LOL_SESSION_BOOTSTRAP.md`, fetch lock `LOL-2026-08-30-V13-TH-MKOI-BENCH-2248-UTC7`, re-fetch `CURRENT_MODEL.md` at authority `ce84ef31eb743e8002603cdd083c871c28787221`, load exact benchmark-aware v1.3 stack, then this or newer handoff last.
