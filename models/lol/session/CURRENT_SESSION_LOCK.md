# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-29-V13-T1-BFX-G4-1757-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-29 17:57 UTC+7 — prospective from Game 4 before any v1.3 certified betting verdict`  
**Scope:** `LCK 2026 Playoffs — Upper Bracket Round 1 — T1 vs BNK FEARX — Bo5 Fearless Draft`  
**Supersedes:** `LOL-2026-08-29-V12-T1-BFX-G3-1650-UTC7` prospectively  
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
**v1.3 ML validation sample at activation:** `ML_SAMPLE_N=0`  
**Duration sample at activation:** `DURATION_SAMPLE_N=0`

## Authorization / transition

During Game 3 the user explicitly authorized a prospective weighting repair for the next game onward: persistent team strength should remain a starting prior, but draft and realized in-game advantage should carry more weight.

Game 3 remains v1.2 historical evidence and is not rescored under v1.3.

The Game 3 final result was not required to choose the new weights and is not used as analytical calibration evidence in this lock.

## Frozen authority

All v1.3-certified analysis from Game 4 onward must use the complete stack at:

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

## T1 vs BNK FEARX strength tier

Retain the same pre-series non-price tier reconstructed under v1.2:

- T1 `K=+1`;
- BFX `K=-1`.

Only the probability weight changes under v1.3:

- `P0(T1)=55%`;
- `P0(BFX)=45%`.

Same-series map results and sportsbook prices do not modify K.

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
- TAKE CANDIDATE requires odds >=1.60 and edge >=+5.0pp.

Probability is locked before price evidence.

## Duration — unchanged

`R0(t)=max(5.0,31.0-t)`

`ER=max(2.0,R0-1.5*V+1.0*Q+1.0*H+0.75*T)`

`F=t+ER`

`P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`

Duration candidate requires odds >=1.60 and selected-side edge >=+7.5pp.

Absent conversion opportunity remains neutral.

## Fearless state entering Game 4

Consumed through Game 1:
- BFX: `K'Sante, Jarvan IV, Ryze, Lucian, Milio`
- T1: `Jayce, Vi, Taliyah, Yunara, Lulu`

Consumed through Game 2:
- BFX: `Rumble, Pantheon, Ahri, Zeri, Yuumi`
- T1: `Ornn, Nocturne, Akali, Ezreal, Seraphine`

Consumed in Game 3:
- BFX: `Kled, Lee Sin, Annie, Kai'Sa, Shen`
- T1: `Olaf, Naafiri, Galio, Jhin, Bard`

Apply all thirty consumed champions to Game 4 draft reading subject to tournament Fearless rules.

## Game 4 supplied draft

User screenshot at ~1:50 confirms:

- BFX: `Yorick / Maokai / Viktor / Corki / Nami`
- T1: `Nasus / Skarner / Anivia / Miss Fortune / Neeko`

Expected roles from listed order:
- BFX: Yorick top / Maokai jungle / Viktor mid / Corki bot / Nami support;
- T1: Nasus top / Skarner jungle / Anivia mid / Miss Fortune bot / Neeko support.

Blue/Red side is not explicitly locked from this screenshot alone.

## Shared controls

- live only; no immediate-postdraft TAKE;
- synchronized executable evidence required;
- position-blind reassessment;
- material state change expires candidate;
- exact live user confirmation before accepted Position;
- actual exposure 0u;
- shadow stake 0.25u;
- no rescue/martingale/chasing/averaging down/stake escalation;
- ML and Duration independent;
- no retroactive accepted Position creation.

## Bootstrap

Every new continuation must fetch default CURRENT_MODEL, bootstrap procedure, this mutable lock, then re-fetch CURRENT_MODEL and required stack at authority commit `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`, use Airtable as ledger/history only, and load latest handoff last.

Mismatch -> `MODEL LOCK MISMATCH — HOLD`.

Breaker -> `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`.
