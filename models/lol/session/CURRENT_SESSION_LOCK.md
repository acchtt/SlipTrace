# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-29-V11-T1-BFX-1429-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-29 14:29 UTC+7`  
**Scope:** `LCK 2026 Playoffs — Upper Bracket Round 1 — T1 vs BNK FEARX — Bo5 Fearless Draft — scheduled 2026-08-29 15:00 UTC+7 / 17:00 KST`  
**Supersedes:** `LOL-2026-08-29-V1-T1-BFX-1352-UTC7` prospectively  
**Authority commit:** `f2ee41755508a9286c9a6cb45acacf57dcbe974e`  
**Active analytical model:** `LoL v1.1 — Moneyline + Duration Core`  
**Active betting markets:** `Moneyline + Duration Over/Under`  
**Kill Handicap:** `RETIRED_FROM_BETTING`  
**Total Kills:** `RETIRED_FROM_BETTING`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`  
**Moneyline required edge:** `+5.0pp vs raw book implied probability`  
**Duration required edge:** `+7.5pp vs raw book implied probability`  
**Validation sample:** `ML_SAMPLE_N=0; DURATION_SAMPLE_N=0 at v1.1 series-lock creation; review floor 20 per family, preferred 30`

## Authorization and epoch transition

The user explicitly authorized Duration activation on 2026-08-29 UTC+7 because available Moneyline prices were very low.

This authorization changes market scope, not Moneyline probability because of price. The prior v1.0 Moneyline-only epoch closed with 0 confirmed Positions. v1.1 begins a fresh family-separated validation epoch.

## Series authority

This lock scopes v1.1 to:

`T1 vs BNK FEARX`

Competition state:

- LCK 2026 Playoffs;
- Upper Bracket Round 1;
- best-of-five;
- Fearless Draft across the series;
- scheduled start `2026-08-29 15:00 UTC+7 / 17:00 KST`.

Series schedule and low displayed ML odds are context only and do not alter model probability thresholds.

## Frozen authority

All model-certified live analysis during this series must use the complete v1.1 stack frozen at:

`f2ee41755508a9286c9a6cb45acacf57dcbe974e`

Required active stack from that exact commit:

1. `models/lol/CURRENT_MODEL.md`;
2. `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. `models/lol/rules/MODEL_RULES_LOL_V1.1_MONEYLINE_CORE.md`;
4. `models/lol/procedures/LOL_V1.1_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md`;
5. `models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md`;
6. `models/lol/procedures/LOL_V1.1_DURATION_LIVE_PROCEDURE_2026-08-29.md`;
7. `models/lol/procedures/LOL_V1.1_VALIDATION_PROTOCOL_2026-08-29.md`;
8. `models/lol/procedures/LOL_V1.1_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`;
9. `models/lol/reviews/LOL_V1.1_DURATION_ENABLEMENT_2026-08-29.md` when transition/calibration context is needed;
10. `models/lol/reviews/LOL_V1.0_CLEAN_REBUILD_AUDIT_2026-08-29.md` when older transition context is needed.

Mutable session state and Airtable may be newer than the authority commit. Handoffs carry state only.

## Historical authority boundary

All v0.x analytical/procedural material remains historical/audit/research authority only. The v1.0 generation also becomes historical generation authority after this lock; its Moneyline analytical core has been carried forward unchanged in the active v1.1 Moneyline files.

Do not blend historical:

- DIM/PDRL/PML certificates;
- CFC/DPS/LRO named gate trees;
- fixed 2SNAP/3SNAP/2CYCLE requirements;
- KHMC/WMS/RNE/NKB or other KH machinery;
- TK recurrence/FRP machinery;
- Duration DOVC/FCR/FRP or historical PRE_TAKE certificate trees;
- family-specific legacy GATE_SIG trees;
- fixed derivative/late-market buffers.

Duration is active only through the compact v1.1 Duration Core.

## Moneyline core

From Team A perspective:

- `D = +1 / 0 / -1`;
- `R/X/O/T = -2..+2`;
- mechanism state `INTACT / WEAKENING / BROKEN / REPLACED`;
- `D_eff = D / 0.5D / 0` according to mechanism state;
- `S = 1.0*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`;
- `P(A) = clamp(50% + 3*S pp, 15%, 85%)`;
- raw implied `q = 1/odds`;
- TAKE CANDIDATE requires odds >=1.60 and ML edge >=+5.0pp.

Moneyline probability must be locked before offered price is used as analytical evidence.

For ML, structures remain context unless they demonstrably alter forward control.

## Duration core

For current clock `t` in decimal minutes:

`R0(t) = max(5.0, 31.0 - t)`

Score:

- `V` — net conversion velocity, `-2..+2`; positive means faster closure;
- `Q` — compulsory-cycle spacing, `-2..+2`; positive means more future clock;
- `H` — terminal path depth, `-2..+2`; positive means more real map/base layers remain;
- `T` — terminal trajectory, `-2..+2`; positive means current state-usable clock extension.

Then:

`ER = max(2.0, R0 - 1.5*V + 1.0*Q + 1.0*H + 0.75*T)`

`F = t + ER`

Central final-duration estimate `F` must be locked before the offered line/odds are used as analytical evidence.

For offered line `L`:

`P(OVER) = clamp(50% + 7*(F-L) pp, 15%, 85%)`

`P(UNDER) = 100% - P(OVER)` when settlement semantics are clear.

TAKE CANDIDATE requires odds >=1.60 and selected Duration edge >=+7.5pp versus raw implied probability.

Absent conversion opportunity is neutral; low kills/low towers/close gold alone are not demonstrated stall evidence.

## Series-specific Fearless handling

- Game 1 uses the full currently legal pool;
- Games 2+ incorporate champions consumed earlier in the series under the applicable Fearless restrictions;
- remaining functional archetypes and player execution burden matter only where they causally affect the compact draft mechanism or active live variables;
- Fearless does not restore historical PDRL/PML certificates;
- each map receives its own compact draft prior/mechanisms.

No pregame or immediate-postdraft betting TAKE is allowed.

## Active execution controls

Shared:

- synchronized evidence required;
- executable active-family market required;
- no universal fixed snapshot-count gate;
- position-blind reassessment required;
- stale/contradictory evidence fails closed;
- material state change expires a pending TAKE CANDIDATE;
- no rescue, martingale, chasing, averaging down or stake escalation;
- actual exposure remains 0u;
- default fixed shadow stake remains 0.25u.

Family-specific price-only movement:

- ML: if state is unchanged, retain locked ML probability and reprice new odds;
- Duration: if state is unchanged, retain `F`; if line changes, recalculate Over/Under probability from the new line, then reprice odds.

ML and Duration may both qualify on one map only if each independently clears its own model. One family is not evidence for the other.

## User line-existence confirmation gate — ACTIVE

No analytical TAKE CANDIDATE is a Position until explicit confirmation.

`USER_LINE_CONFIRMATION = PENDING / CONFIRMED / FAILED`

For Moneyline, confirmation requires exact team ML and odds.

For Duration, confirmation requires exact Over/Under side, exact duration line and exact odds.

- `PENDING`: no Position, W/L or P/L;
- `CONFIRMED`: accepted shadow Position may be created if no material state change invalidated the candidate;
- `FAILED`: no Position exists;
- a moved quote must be repriced/reassessed before acceptance.

## Validation freeze

Track separately:

- `ML_SAMPLE_N = 0` at lock creation;
- `DURATION_SAMPLE_N = 0` at lock creation.

Per family:

- 10 confirmed Positions: diagnostic checkpoint only;
- 20 confirmed Positions: minimum architecture review point;
- 30 confirmed Positions: preferred full calibration review.

Do not change ML because Duration loses, or Duration because ML loses. Do not mutate either model after one ordinary result.

Primary error taxonomy only:

- `DRAFT READ ERROR`;
- `LIVE STATE ERROR`;
- `PROBABILITY/CALIBRATION ERROR`;
- `PRICE/EXECUTION ERROR`.

## Airtable workflow

GitHub is model/rules authority. Airtable remains the canonical historical map/snapshot/position ledger.

- preserve every historical v0.x/v1.0 record unchanged;
- T1–BFX map/snapshot records are created only as live evidence arrives;
- HOLD/PASS may be snapshots when useful;
- pending TAKE CANDIDATE is not a Position;
- accepted ML Position preserves `ML_CORE[...]`;
- accepted Duration Position preserves `DUR_CORE[...]`, exact side/line/odds and entry clock;
- all accepted positions use 0.25u shadow stake and 0u actual exposure under this lock;
- never claim a write or settlement occurred unless the connector action succeeded.

## Bootstrap / continuation requirement

Every continuation/new chat for this series must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this mutable lock and verify `LOL-2026-08-29-V11-T1-BFX-1429-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `f2ee41755508a9286c9a6cb45acacf57dcbe974e`;
5. load the exact v1.1 stack in locked CURRENT_MODEL order from that commit;
6. use Airtable only as ledger/history authority, not analytical model authority;
7. load the latest applicable T1–BFX handoff last.

If the lock/authority cannot be matched:

`MODEL LOCK MISMATCH — HOLD`

If the procedural circuit breaker becomes active:

`TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`
