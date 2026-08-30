# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-30-V13-FNC-GX-BENCH-2254-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-30 22:54 UTC+7`  
**Scope:** `LEC 2026 Summer — Week 6 — Fnatic vs GIANTX — Bo3 Fearless Draft`  
**Scheduled:** `2026-08-30 23:30 UTC+7 / 18:30 CEST`  
**Supersedes:** `LOL-2026-08-30-V13-TH-MKOI-BENCH-2248-UTC7` prospectively  
**Authority commit:** `ce84ef31eb743e8002603cdd083c871c28787221`  
**Active analytical model:** `LoL v1.3 — Hierarchy Moneyline + Duration Core`  
**Team benchmark:** `GOL.GG LEAGUE-RELATIVE BENCHMARK ACTIVE`  
**Execution patch:** `PRICE CANNOT CREATE THE BET / SELECTED-SIDE CAUSAL THESIS C>0`  
**Active betting markets:** `Moneyline + Duration Over/Under`  
**Kill Handicap:** `RETIRED_FROM_BETTING`  
**Total Kills:** `RETIRED_FROM_BETTING`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`  
**Moneyline required edge:** `+5.0pp vs raw book implied probability`  
**Duration required edge:** `+7.5pp vs raw book implied probability`  
**v1.3 ML validation sample at relock:** `ML_SAMPLE_N=3`  
**Duration sample at relock:** `DURATION_SAMPLE_N=0`

## Frozen authority

All model-certified analysis for this series must use the benchmark-aware v1.3 stack frozen at:

`ce84ef31eb743e8002603cdd083c871c28787221`

Required stack from that exact commit:

1. `models/lol/CURRENT_MODEL.md`;
2. `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. `models/lol/procedures/LOL_V1.3_TEAM_BENCHMARK_GOLGG_2026-08-30.md`;
4. `models/lol/rules/MODEL_RULES_LOL_V1.3_MONEYLINE_HIERARCHY_CORE.md`;
5. `models/lol/procedures/LOL_V1.3_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md`;
6. `models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md`;
7. `models/lol/procedures/LOL_V1.1_DURATION_LIVE_PROCEDURE_2026-08-29.md`;
8. `models/lol/procedures/LOL_V1.3_VALIDATION_PROTOCOL_2026-08-29.md`;
9. `models/lol/procedures/LOL_V1.3_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`.

Mutable handoff/Airtable state may be newer than the authority commit.

## Fnatic vs GIANTX pre-series benchmark

Constructed from pre-series-only Games of Legends / gol.gg LEC 2026 Summer and Spring team tables. Sportsbook prices and same-series outcomes are excluded.

Benchmark formula:

`B_split = 0.30*z(WinRate) + 0.30*z(GDM) + 0.20*z(GD@15) + 0.10*z(TowerDiff/Game) + 0.05*z(DRA%) + 0.05*z(NASH%)`

### Current Summer inputs

Fnatic:
- `G=19`
- `WR=47.4%`
- `GDM=-54`
- `GD@15=+320`
- `Towers=5.6-6.3`
- `DRA%=47.2`
- `NASH%=36.8`
- league-relative `B_current=-0.134`

GIANTX:
- `G=21`
- `WR=52.4%`
- `GDM=-58`
- `GD@15=-792`
- `Towers=5.7-6.3`
- `DRA%=41.9`
- `NASH%=41.7`
- league-relative `B_current=-0.330`

### Previous Spring inputs

- `B_previous(FNC)=-0.261`
- `B_previous(GX)=-0.283`

### Roster continuity adjustment

Fnatic made one decision-critical starter change from Spring to Summer: `Empyros -> Soboro` top. Normal 70/30 weighting is adjusted by halving previous-split weight, giving `85% current / 15% previous`.

GIANTX made two decision-critical starter changes from Spring to Summer: `Lot -> Oscarinin` top and `Noah -> Flakked` bot. Under the benchmark procedure, previous split is descriptive context only; use current split for the blended score. Current sample exceeds 15 games.

Resulting raw blends:
- `B_raw(FNC)=-0.153`
- `B_raw(GX)=-0.330`

After re-standardizing the LEC peer-set blended scores under the active roster-adjustment rules:
- `B(FNC)≈-0.165`
- `B(GX)≈-0.361`

Pairwise gap from Fnatic perspective:

`GAP = B(FNC)-B(GX) ≈ +0.196 SD`

This is below the `0.50 SD` meaningful-strength threshold.

### Frozen strength prior

- Fnatic: `K=0 / P0=50%`
- GIANTX: `K=0 / P0=50%`

This is a statistically EVEN team-strength benchmark. Draft and live evidence must separate the teams.

Freeze this K/P0 for the full series unless a genuine roster/availability change occurs. Same-series results never update it.

## Moneyline v1.3 core

From selected-side perspective:

- `K=-2..+2` from benchmark gap;
- `P0=50%+5*K pp`;
- `D=+1/0/-1`;
- `R/X/O/T=-2..+2`;
- mechanism `INTACT / WEAKENING / BROKEN / REPLACED`;
- `D_eff=D / 0.5D / 0`;
- `C=1.5*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`;
- `S=C`;
- `P=clamp(P0+3*S pp,15%,85%)`.

Before price evidence, selected side must have `C>0` plus a coherent reachable draft/live win mechanism. Price cannot create the bet.

## Duration — unchanged

`R0(t)=max(5.0,31.0-t)`

`ER=max(2.0,R0-1.5*V+1.0*Q+1.0*H+0.75*T)`

`F=t+ER`

`P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`

Duration TAKE CANDIDATE requires odds `>=1.60` and selected-side edge `>=+7.5pp`.

## Series initialization

- Series score at relock: `0-0 / pre-series`.
- Current map: `Game 1 not started`.
- Blue/Red assignment: `not supplied`.
- Draft: `not supplied`.
- Live state/market: `not supplied`.
- No FNC-GX Position exists under this lock.
- Format: `Bo3 Fearless Draft`.

Expected current lineups from reliable pre-series roster evidence, subject to user/live-card override:

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

## User workflow preference

- `VERDICT FIRST` and compact live output.
- No Airtable writes during a map; perform snapshot/position/map logging at map end.
- Exact user confirmation required for any TAKE CANDIDATE before accepted Position.
- Never issue a TAKE merely because odds look generous.

## Bootstrap / continuation

Every new continuation must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this mutable lock and verify `LOL-2026-08-30-V13-FNC-GX-BENCH-2254-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `ce84ef31eb743e8002603cdd083c871c28787221`;
5. load exact benchmark-aware v1.3 stack in locked CURRENT_MODEL order;
6. use Airtable as ledger/history authority only and defer in-map writes until map end;
7. load latest FNC-GX handoff last.

Mismatch -> `MODEL LOCK MISMATCH — HOLD`.

Procedural breaker -> `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`.
