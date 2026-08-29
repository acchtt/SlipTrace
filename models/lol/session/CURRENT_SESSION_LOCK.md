# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-29-V12-T1-BFX-G3-1650-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-29 16:50 UTC+7 — prospectively after Game 2 / before Game 3`  
**Scope:** `LCK 2026 Playoffs — Upper Bracket Round 1 — T1 vs BNK FEARX — Bo5 Fearless Draft`  
**Series score at activation:** `T1 1-1 BNK FEARX`  
**Supersedes:** `LOL-2026-08-29-V11-T1-BFX-1429-UTC7` prospectively  
**Authority commit:** `18a5c9c6e6e2a7efe820b6da3f0269d2e8e1e18f`  
**Active analytical model:** `LoL v1.2 — Strength-Prior Moneyline + Duration Core`  
**Active betting markets:** `Moneyline + Duration Over/Under`  
**Kill Handicap:** `RETIRED_FROM_BETTING`  
**Total Kills:** `RETIRED_FROM_BETTING`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`  
**Moneyline required edge:** `+5.0pp vs raw book implied probability`  
**Duration required edge:** `+7.5pp vs raw book implied probability`  
**Validation sample at activation:** `ML_SAMPLE_N=0; DURATION_SAMPLE_N=0`

## Authorization / defect repair

The user explicitly authorized an immediate Moneyline model patch after Game 2 because v1.1 omitted persistent team strength and therefore forced every matchup to begin from a neutral 50% ML baseline.

This is treated as a clear mechanical architecture defect, not an ordinary-loss reaction.

Game 1 and Game 2 remain historical v1.1 assessments and are not relabeled. Game 1 retroactive user-designated ledger entries remain outside validation.

## Frozen authority

All model-certified live analysis from Game 3 onward must use the complete v1.2 stack frozen at:

`18a5c9c6e6e2a7efe820b6da3f0269d2e8e1e18f`

Required stack from that exact commit:

1. `models/lol/CURRENT_MODEL.md`;
2. `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. `models/lol/rules/MODEL_RULES_LOL_V1.2_MONEYLINE_STRENGTH_PRIOR_CORE.md`;
4. `models/lol/procedures/LOL_V1.2_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md`;
5. `models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md`;
6. `models/lol/procedures/LOL_V1.1_DURATION_LIVE_PROCEDURE_2026-08-29.md`;
7. `models/lol/procedures/LOL_V1.2_VALIDATION_PROTOCOL_2026-08-29.md`;
8. `models/lol/procedures/LOL_V1.2_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`;
9. `models/lol/reviews/LOL_V1.2_TEAM_STRENGTH_PRIOR_PATCH_2026-08-29.md` when transition/series-strength context is needed;
10. `models/lol/reviews/LOL_V1.1_DURATION_ENABLEMENT_2026-08-29.md` when Duration context is needed.

Mutable handoff/Airtable state may be newer than the authority commit.

## T1 vs BNK FEARX series-frozen strength prior

Reconstructed only from evidence available before Game 1; Game 1/Game 2 results and sportsbook prices were excluded from assignment.

From BNK FEARX perspective:

`K=-1`

`P0(BFX)=40%`

From T1 perspective:

`K=+1`

`P0(T1)=60%`

Basis: T1 carried the stronger established top-level competitive baseline and direct playoff path; BFX had enough recent official same-league wins and successful Play-In qualification that the gap is meaningful but not the maximum `K=±2` tier.

This `K/P0` is frozen for the rest of the series unless a genuine roster/availability change occurs. Earlier maps in the same series do not modify it.

## Moneyline v1.2 core

From Team A perspective:

- `K=-2..+2` pre-series team-strength tier;
- `P0=50%+10*K pp`;
- `D=+1/0/-1` draft prior;
- `R/X/O/T=-2..+2`;
- mechanism `INTACT / WEAKENING / BROKEN / REPLACED`;
- `D_eff=D / 0.5D / 0`;
- `S=1.0*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`;
- `P(A)=clamp(P0(A)+3*S pp,15%,85%)`;
- raw implied `1/odds`;
- TAKE CANDIDATE requires odds >=1.60 and edge >=+5.0pp.

`K/P0` and final probability must be locked before offered price is used as analytical evidence. Price may never determine `K`.

## Duration core — unchanged

Use the v1.1 compact Duration Core unchanged:

`R0(t)=max(5.0,31.0-t)`

`ER=max(2.0,R0-1.5*V+1.0*Q+1.0*H+0.75*T)`

`F=t+ER`

`P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`

Duration candidate requires odds >=1.60 and selected edge >=+7.5pp.

Absent conversion opportunity remains neutral.

## Fearless state entering Game 3

Consumed in Game 1:

- BFX: `K'Sante, Jarvan IV, Ryze, Lucian, Milio`
- T1: `Jayce, Vi, Taliyah, Yunara, Lulu`

Consumed in Game 2:

- BFX: `Rumble, Pantheon, Ahri, Zeri, Yuumi`
- T1: `Ornn, Nocturne, Akali, Ezreal, Seraphine`

Apply all 20 consumed champions to Game 3 draft reading subject to the tournament's Fearless rules.

## Shared execution controls

- live only; no pregame/immediate-postdraft TAKE;
- synchronized evidence required;
- executable active-family market required;
- position-blind reassessment;
- material state change expires a pending candidate;
- exact user line confirmation before accepted Position;
- actual exposure `0u`;
- shadow stake `0.25u`;
- no rescue, martingale, chasing, averaging down or stake escalation;
- ML and Duration qualify independently;
- no retroactive accepted Position creation.

## Bootstrap / continuation

Every new continuation must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this mutable lock and verify `LOL-2026-08-29-V12-T1-BFX-G3-1650-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `18a5c9c6e6e2a7efe820b6da3f0269d2e8e1e18f`;
5. load the exact v1.2 stack in locked CURRENT_MODEL order;
6. use Airtable as ledger/history authority only;
7. load the latest T1–BFX handoff last.

Mismatch -> `MODEL LOCK MISMATCH — HOLD`.

Procedural breaker -> `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`.
