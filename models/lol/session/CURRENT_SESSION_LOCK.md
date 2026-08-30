# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-30-V13-TH-MKOI-2150-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-30 21:50 UTC+7`  
**Scope:** `LEC 2026 Summer — Week 6 — Team Heretics vs Movistar KOI — Bo3 Fearless Draft`  
**Scheduled:** `2026-08-30 21:15 UTC+7 / 16:15 CEST`  
**Supersedes:** `LOL-2026-08-30-V13-DK-KT-1612-UTC7` prospectively  
**Authority commit:** `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`  
**Active analytical model:** `LoL v1.3 — Hierarchy Moneyline + Duration Core`  
**Active betting markets:** `Moneyline + Duration Over/Under`  
**Kill Handicap:** `RETIRED_FROM_BETTING`  
**Total Kills:** `RETIRED_FROM_BETTING`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`  
**Moneyline required edge:** `+5.0pp vs raw book implied probability`  
**Duration required edge:** `+7.5pp vs raw book implied probability`  
**v1.3 ML validation sample at relock:** `ML_SAMPLE_N=2`  
**Duration sample at relock:** `DURATION_SAMPLE_N=0`

## Frozen authority

All model-certified analysis for this TH vs MKOI series must use the complete v1.3 stack frozen at:

`083a7a97c04e9fb4fd40b74c3dd931643539aaa0`

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

Basis available before the series:
- current LEC Summer game performance entering Aug 30 materially favored MKOI over TH (`40.0%` vs `23.5%` game win rate in Games of Legends' current tournament team data);
- TH's latest week included a `0-2` loss to Shifters after a `0-2` loss to GIANTX, despite a prior `2-0` win over SK;
- MKOI also had mixed recent Summer results (`2-0` over NAVI followed by `0-2` to SK), so the edge is meaningful but not a maximum `K=±2` tier;
- MKOI's established 2026 top-level baseline was stronger, including 3rd place in LEC Spring.

Freeze this `K/P0` for the full series unless there is a genuine roster/availability change. Same-series maps do not modify it.

## Moneyline v1.3 core

From Team A perspective:

- `K=-2..+2`;
- `P0=50%+5*K pp`;
- `D=+1/0/-1`;
- `R/X/O/T=-2..+2`;
- mechanism `INTACT / WEAKENING / BROKEN / REPLACED`;
- `D_eff=D / 0.5D / 0`;
- `S=1.5*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`;
- `P(A)=clamp(P0(A)+3*S pp,15%,85%)`;
- raw implied `1/odds`;
- TAKE CANDIDATE requires odds `>=1.60` and edge `>=+5.0pp`.

Probability must be locked before price evidence.

## Duration — unchanged

`R0(t)=max(5.0,31.0-t)`

`ER=max(2.0,R0-1.5*V+1.0*Q+1.0*H+0.75*T)`

`F=t+ER`

`P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`

Duration TAKE CANDIDATE requires odds `>=1.60` and selected-side edge `>=+7.5pp`.

Absent conversion opportunity remains neutral.

## Series initialization

- Series score at relock: `not supplied / do not infer`.
- Current map number at relock: `not supplied / do not infer`.
- Blue/Red side assignment: `not supplied`.
- Draft: `not supplied`.
- Live state/market: `not supplied`.
- No TH vs MKOI Position exists under this lock yet.
- Regular season format is Bo3 Fearless Draft.

Before player-fit or live certification, resolve current five-player lineups from user-supplied card/scoreboard or reliable saved/current evidence.

## User workflow preference

- Visible live responses: `VERDICT FIRST` and compact.
- Do not write live snapshots/positions to Airtable during a map; perform Airtable map/snapshot/position logging at map end.
- GitHub handoff/lock may still be maintained for governance/state continuity.

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
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this mutable lock and verify `LOL-2026-08-30-V13-TH-MKOI-2150-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`;
5. load the exact v1.3 stack in locked CURRENT_MODEL order;
6. use Airtable as ledger/history authority only and defer in-map writes until map end per user preference;
7. load the latest TH-MKOI handoff last.

Mismatch -> `MODEL LOCK MISMATCH — HOLD`.

Procedural breaker -> `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`.
