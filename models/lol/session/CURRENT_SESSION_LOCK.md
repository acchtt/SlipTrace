# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-30-V13-TH-MKOI-BENCH-2248-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-30 22:48 UTC+7`  
**Scope:** `LEC 2026 Summer — Week 6 — Team Heretics vs Movistar KOI — Bo3 Fearless Draft`  
**Scheduled:** `2026-08-30 21:15 UTC+7 / 16:15 CEST`  
**Supersedes:** `LOL-2026-08-30-V13-TH-MKOI-THESIS-2227-UTC7` prospectively  
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

All model-certified analysis from this relock onward must use the benchmark-aware v1.3 stack frozen at:

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

## TH vs MKOI benchmark reconstruction

User explicitly authorized benchmark redesign after Game 2. This relock reconstructs the strength prior from **pre-series-only** Gol.gg data. Game 2 outcome and sportsbook prices are excluded.

Benchmark formula:

`B_split = 0.30*z(WinRate) + 0.30*z(GDM) + 0.20*z(GD@15) + 0.10*z(TowerDiff/Game) + 0.05*z(DRA%) + 0.05*z(NASH%)`

Current Summer pre-series inputs:
- MKOI: `G=20; WR=40.0%; GDM=-21; GD@15=+912; Towers=5.6-6.5; DRA%=56.3; NASH%=43.3`
- TH: `G=17; WR=23.5%; GDM=-176; GD@15=-1262; Towers=3.5-7.8; DRA%=40.0; NASH%=25.0`

League-relative current split scores:
- `B_current(MKOI)=+0.018`
- `B_current(TH)=-1.355`

Previous LEC Spring scores under the same metric construction:
- `B_previous(MKOI)=+0.758`
- `B_previous(TH)=-1.696`

Both teams had >=15 current-split games, so normal blend is `70% current / 30% previous`. No decision-critical roster discontinuity requiring an adjustment has been established.

Raw blended scores:
- `B_raw(MKOI)=+0.240`
- `B_raw(TH)=-1.457`

After re-standardizing all LEC blended scores:
- `B(MKOI)=+0.262`
- `B(TH)=-1.590`

Pairwise gap from MKOI perspective:

`GAP = +1.852 SD`

This clears the `>=1.25 SD` major-strength threshold.

### Prospectively frozen strength prior from this relock

- Movistar KOI: `K=+2 / P0=60%`
- Team Heretics: `K=-2 / P0=40%`

Do not use sportsbook favoritism as justification. The classification is derived from the independent benchmark.

Same-series results do not update this reconstructed K/P0. It is frozen prospectively for the remainder of this series unless a genuine roster/availability change occurs.

The earlier confirmed TH ML @3.396 position remains a historical v1.3 sample under the prior strength-construction/execution rules. Do not retroactively rewrite or invalidate it.

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
- `P=clamp(P0+3*S pp,15%,85%)`;
- raw implied `1/odds`.

### Hard causal thesis gate

`PRICE CANNOT CREATE THE BET`.

Before price evidence, selected side must have:
- `C>0`;
- coherent, currently reachable draft/live win mechanism.

Team strength alone does not satisfy this gate. If selected-side `C<=0`, verdict is `PASS` regardless of apparent numerical edge.

TAKE CANDIDATE additionally requires:
- odds `>=1.60`;
- edge `>=+5.0pp`;
- synchronized executable market;
- benchmark/probability/thesis locked before price;
- position-blind reassessment;
- actual exposure `0u`.

## Duration — unchanged

`R0(t)=max(5.0,31.0-t)`

`ER=max(2.0,R0-1.5*V+1.0*Q+1.0*H+0.75*T)`

`F=t+ER`

`P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`

Duration TAKE CANDIDATE requires odds `>=1.60` and selected-side edge `>=+7.5pp`.

Absent conversion opportunity remains neutral.

## Current series state at relock

- Game 2 completed: `Movistar KOI won`.
- Series score: `not explicitly supplied / do not infer`.
- Final Game 2 duration/full scoreboard: `not supplied`.
- Confirmed Game 2 position `TH ML @3.396` settled LOSS and remains historical.

## User workflow preference

- `VERDICT FIRST` and compact live output.
- No Airtable writes during a map; perform snapshot/position/map logging at map end.
- Exact user confirmation required for any TAKE CANDIDATE before accepted Position.
- Do not issue a TAKE merely because odds look generous.

## Bootstrap / continuation

Every new continuation must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this mutable lock and verify `LOL-2026-08-30-V13-TH-MKOI-BENCH-2248-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `ce84ef31eb743e8002603cdd083c871c28787221`;
5. load exact benchmark-aware v1.3 stack in locked CURRENT_MODEL order;
6. use Airtable as ledger/history authority only and defer in-map writes until map end;
7. load latest TH-MKOI handoff last.

Mismatch -> `MODEL LOCK MISMATCH — HOLD`.

Procedural breaker -> `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`.
