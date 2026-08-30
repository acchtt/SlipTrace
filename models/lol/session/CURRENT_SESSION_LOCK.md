# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-30-V13-TH-MKOI-THESIS-2227-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-30 22:27 UTC+7`  
**Scope:** `LEC 2026 Summer — Week 6 — Team Heretics vs Movistar KOI — Bo3 Fearless Draft`  
**Scheduled:** `2026-08-30 21:15 UTC+7 / 16:15 CEST`  
**Supersedes:** `LOL-2026-08-30-V13-TH-MKOI-2150-UTC7` prospectively  
**Authority commit:** `369babb212e806ad4ac251f75c8f909009ea8eed`  
**Active analytical model:** `LoL v1.3 — Hierarchy Moneyline + Duration Core`  
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

All model-certified analysis from this relock onward must use the complete v1.3 stack frozen at:

`369babb212e806ad4ac251f75c8f909009ea8eed`

Required stack from that exact commit:

1. `models/lol/CURRENT_MODEL.md`;
2. `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. `models/lol/rules/MODEL_RULES_LOL_V1.3_MONEYLINE_HIERARCHY_CORE.md`;
4. `models/lol/procedures/LOL_V1.3_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md`;
5. `models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md`;
6. `models/lol/procedures/LOL_V1.1_DURATION_LIVE_PROCEDURE_2026-08-29.md`;
7. `models/lol/procedures/LOL_V1.3_VALIDATION_PROTOCOL_2026-08-29.md`;
8. `models/lol/procedures/LOL_V1.3_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`.

Mutable handoff/Airtable state may be newer than the authority commit.

## TH vs MKOI series-frozen strength prior

Assigned only from pre-series, non-price evidence. Sportsbook prices and same-series results are excluded.

From Team Heretics perspective:
- `K=-1`
- `P0(TH)=45%`

From Movistar KOI perspective:
- `K=+1`
- `P0(MKOI)=55%`

Freeze this `K/P0` for the full series unless there is a genuine roster/availability change. Same-series maps do not modify it.

## Moneyline v1.3 core

From selected-side perspective:

- `K=-2..+2`;
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

Before price is used as evidence, the selected side must have:
- `C>0`;
- a coherent, currently reachable draft/live win mechanism.

Team strength alone does not satisfy this gate. If selected-side `C<=0`, verdict is `PASS` even if the price creates apparent numerical edge above +5.0pp.

TAKE CANDIDATE then additionally requires:
- odds `>=1.60`;
- edge `>=+5.0pp`;
- synchronized executable market;
- probability/thesis locked before price;
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
- Confirmed Game 2 position `TH ML @3.396` settled LOSS and is historical under the prior execution rules.
- Do not retroactively invalidate or relabel earlier accepted Positions.

## User workflow preference

- Visible live responses: `VERDICT FIRST` and compact.
- Do not write live snapshots/positions to Airtable during a map; perform Airtable map/snapshot/position logging at map end.
- Exact user confirmation still required for any TAKE CANDIDATE before accepted Position.
- Most importantly: do not issue a TAKE merely because the odds look generous; require positive selected-side causal thesis first.

## Shared controls

- live only; no immediate-postdraft TAKE;
- synchronized executable evidence required;
- position-blind reassessment;
- material state change expires candidate;
- exact live user confirmation before accepted Position;
- actual exposure `0u`;
- shadow stake `0.25u`;
- no rescue/martingale/chasing/averaging down/stake escalation;
- ML and Duration qualify independently;
- no retroactive accepted Position creation.

## Bootstrap / continuation

Every new continuation must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this mutable lock and verify `LOL-2026-08-30-V13-TH-MKOI-THESIS-2227-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `369babb212e806ad4ac251f75c8f909009ea8eed`;
5. load the exact v1.3 stack in locked CURRENT_MODEL order;
6. use Airtable as ledger/history authority only and defer in-map writes until map end;
7. load the latest TH-MKOI handoff last.

Mismatch -> `MODEL LOCK MISMATCH — HOLD`.

Procedural breaker -> `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`.
