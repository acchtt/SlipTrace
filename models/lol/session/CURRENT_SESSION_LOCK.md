# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-30-V13-DK-KT-1612-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-30 16:12 UTC+7`  
**Scope:** `LCK 2026 Playoffs — Round 1 — Dplus KIA vs KT Rolster — Bo5 Fearless Draft`  
**Scheduled:** `2026-08-30 15:00 UTC+7 / 17:00 KST`  
**Supersedes:** `LOL-2026-08-29-V13-T1-BFX-G4-1757-UTC7` prospectively  
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
**v1.3 ML validation sample at relock:** `ML_SAMPLE_N=0`  
**Duration sample at relock:** `DURATION_SAMPLE_N=0`

## Frozen authority

All model-certified analysis for this DK vs KT series must use the complete v1.3 stack frozen at:

`083a7a97c04e9fb4fd40b74c3dd931643539aaa0`

Required stack from that exact commit:

1. `models/lol/CURRENT_MODEL.md`;
2. `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. `models/lol/rules/MODEL_RULES_LOL_V1.3_MONEYLINE_HIERARCHY_CORE.md`;
4. `models/lol/procedures/LOL_V1.3_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md`;
5. `models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md`;
6. `models/lol/procedures/LOL_V1.1_DURATION_LIVE_PROCEDURE_2026-08-29.md`;
7. `models/lol/procedures/LOL_V1.3_VALIDATION_PROTOCOL_2026-08-29.md`;
8. `models/lol/procedures/LOL_V1.3_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`;
9. `models/lol/reviews/LOL_V1.3_HIERARCHY_WEIGHT_PATCH_2026-08-29.md` when transition context is needed.

Mutable handoff/Airtable state may be newer than the authority commit.

## DK vs KT series-frozen strength prior

Assigned only from pre-series, non-price evidence. Sportsbook prices and any live/current-series result are excluded.

From Dplus KIA perspective:

- `K=+1`
- `P0(DK)=55%`

From KT Rolster perspective:

- `K=-1`
- `P0(KT)=45%`

Basis: DK won both recent August LCK head-to-head series against KT (`2-1` on Aug 9 and `2-0` on Aug 12) and also beat T1 `2-1` on Aug 14. KT entered this playoff round through the Play-In path after a `3-2` win over Hanjin BRION. The edge is meaningful but not the maximum `K=±2` tier.

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
- No DK vs KT betting verdict or Position exists under this lock yet.

Before player-fit or live certification, use saved LCK roster context first and resolve any current substitutions from user-supplied lineup/card or reliable evidence.

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
3. fetch this mutable lock and verify `LOL-2026-08-30-V13-DK-KT-1612-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`;
5. load the exact v1.3 stack in locked CURRENT_MODEL order;
6. use Airtable as ledger/history authority only;
7. load the latest DK-KT handoff last.

Mismatch -> `MODEL LOCK MISMATCH — HOLD`.

Procedural breaker -> `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`.
