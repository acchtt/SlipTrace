# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-31-V13-KTC-KRXC-BENCH-1205-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-31 12:05 UTC+7`  
**Scope:** `LCK CL 2026 Season — Playoffs Upper Round 1 — KT Rolster Challengers vs DRX/KRX Challengers — Bo5 Fearless Draft`  
**Scheduled:** `2026-08-31 12:00 UTC+7 / 14:00 KST`  
**Supersedes:** `LOL-2026-08-30-V13-FNC-GX-BENCH-2254-UTC7` prospectively  
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

## KT.C vs KRX.C pre-series benchmark

Constructed from pre-series-only Games of Legends / gol.gg LCK CL peer tables. Sportsbook prices, current-map state and same-series outcomes are excluded.

Current competitive window: `LCK CL 2026 Rounds 3-4`.  
Previous comparable window: `LCK CL 2026 Rounds 1-2`.

Benchmark formula:

`B_split = 0.30*z(WinRate) + 0.30*z(GDM) + 0.20*z(GD@15) + 0.10*z(TowerDiff/Game) + 0.05*z(DRA%) + 0.05*z(NASH%)`

### Current Rounds 3-4 inputs

KRX Challengers:
- `G=20`
- `WR=75.0%`
- `GDM=+203`
- `GD@15=+943`
- `Towers=8.1-3.8`
- `DRA%=60.5`
- `NASH%=71.1`
- `B_current=+1.666`

KT Rolster Challengers:
- `G=20`
- `WR=50.0%`
- `GDM=-32`
- `GD@15=-822`
- `Towers=5.8-5.7`
- `DRA%=52.1`
- `NASH%=55.0`
- `B_current=-0.206`

### Previous Rounds 1-2 scores

- `B_previous(KRX)=-0.127`
- `B_previous(KT)=+0.765`

### Roster continuity adjustment

Latest reliable pre-series lineup evidence indicates:

KT.C expected five:
- Sero — top
- Sylvie — jungle
- Hwichan — mid
- FenRir — bot
- Pollu — support

This matches the Rounds 1-2 decision-core lineup, so KT uses normal `70% current / 30% previous` weighting.

KRX.C / DRX Challengers expected five from the most recent Play-In:
- Frog — top
- Winner — jungle
- AKaJe — mid
- Vincenzo — bot
- Minous — support

Relative to the Rounds 1-2 decision-core lineup, the material starter change is `Jiwoo -> Vincenzo` at bot. KRX therefore halves previous-window weight and uses `85% current / 15% previous`.

Live official card/user scoreboard overrides these expected fives. A decision-critical unexpected additional starter change requires benchmark review before ML TAKE.

### Blended benchmark

Participant raw blends:
- `B_raw(KRX)=+1.397`
- `B_raw(KT)=+0.085`

Using normal 70/30 peer blending for nonparticipants as the display baseline, re-standardized league-relative values are:
- `B(KRX)=+1.623`
- `B(KT)=+0.069`
- pairwise `GAP(KRX-KT)=+1.554 SD`

Nonparticipant roster-continuity choices are not decision-critical to this tier: exhaustively varying every other peer among the benchmark's allowed `70/30`, `85/15`, or current-only adjustments leaves the KRX-KT final gap in approximately `+1.430 to +1.653 SD`, always above the `+1.25 SD` major-strength threshold.

### Frozen strength prior

From KRX/DRX perspective:
- `K=+2`
- `P0(KRX)=60%`

From KT perspective:
- `K=-2`
- `P0(KT)=40%`

This K/P0 is frozen for the series unless a genuine current-series roster/availability change is confirmed. Same-series map results and sportsbook prices do not update it.

## Moneyline v1.3 core

From selected-side perspective:

- `P0=50%+5*K pp`;
- `D=+1/0/-1`;
- `R/X/O/T=-2..+2`;
- mechanism `INTACT / WEAKENING / BROKEN / REPLACED`;
- `D_eff=D / 0.5D / 0`;
- `C=1.5*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`;
- `S=C`;
- `P=clamp(P0+3*S pp,15%,85%)`.

Before price evidence, selected side must have `C>0` plus a coherent, currently reachable draft/live win mechanism. Team benchmark alone cannot satisfy the thesis gate. Price cannot create the bet.

TAKE CANDIDATE additionally requires:
- synchronized executable live ML;
- odds `>=1.60`;
- edge `>=+5.0pp`;
- probability/thesis locked before price;
- position-blind reassessment;
- actual exposure `0u`.

## Duration — unchanged

`R0(t)=max(5.0,31.0-t)`

`ER=max(2.0,R0-1.5*V+1.0*Q+1.0*H+0.75*T)`

`F=t+ER`

`P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`

Duration TAKE CANDIDATE requires odds `>=1.60` and selected-side edge `>=+7.5pp`.

## Current series state at relock

- Match scheduled for `12:00 UTC+7`; user requested the current LCK CL match at `12:02 UTC+7`.
- Series score: `not supplied / do not infer`.
- Current map/state: `Game 1 expected underway, exact draft/live state not supplied`.
- Blue/Red: `not supplied`.
- No KT.C-KRX.C Position exists under this lock.
- Format: `Bo5 Fearless Draft`.

## User workflow preference

- `VERDICT FIRST` and compact live output.
- No Airtable writes during a map; perform map/snapshot/position logging at map end.
- Exact user confirmation required for any TAKE CANDIDATE before accepted Position.
- Never issue a TAKE merely because odds look generous.

## Bootstrap / continuation

Every new continuation must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this mutable lock and verify `LOL-2026-08-31-V13-KTC-KRXC-BENCH-1205-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `ce84ef31eb743e8002603cdd083c871c28787221`;
5. load exact benchmark-aware v1.3 stack in locked CURRENT_MODEL order;
6. use Airtable as ledger/history authority only and defer in-map writes until map end;
7. load latest KT.C-KRX.C handoff last.

Mismatch -> `MODEL LOCK MISMATCH — HOLD`.

Procedural breaker -> `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`.
