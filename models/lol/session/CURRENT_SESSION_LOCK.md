# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-29-V1-ML-1341-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-29 13:41 UTC+7`  
**Scope:** `LoL v1.0 — Moneyline Core initial validation epoch; no specific live series selected`  
**Supersedes:** `LOL-2026-08-28-E18-TH-SHFT-2159-UTC7` prospectively  
**Authority commit:** `1be61970a3b586fd173479a4e591cfe391e03f0f`  
**Active analytical model:** `LoL v1.0 — Moneyline Core`  
**Active betting market:** `Moneyline only`  
**Kill Handicap:** `RETIRED_FROM_BETTING`  
**Total Kills:** `RETIRED_FROM_BETTING`  
**Duration:** `RETIRED_FROM_BETTING`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`  
**Required model edge:** `+5.0pp vs raw book implied probability`  
**Validation sample:** `0 confirmed v1.0 Moneyline Positions at lock creation; review floor 20, preferred 30`

## Authorization

The user explicitly authorized a **new major model generation** on 2026-08-29 UTC+7 and requested a clean rebuild from first principles as **LoL v1.0 — Moneyline Core**.

This authorization explicitly retires the old v0.3.58 analytical architecture from active use after v1.0 activation while preserving all historical files, reviews, screenshots, Airtable records, positions, settlements and P/L.

## Frozen authority

All v1.0 model-certified live Moneyline analysis during this authority epoch must use analytical/procedural files frozen at:

`1be61970a3b586fd173479a4e591cfe391e03f0f`

Required active stack from that commit:

1. `models/lol/CURRENT_MODEL.md`;
2. `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. `models/lol/rules/MODEL_RULES_LOL_V1.0_MONEYLINE_CORE.md`;
4. `models/lol/procedures/LOL_V1.0_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md`;
5. `models/lol/procedures/LOL_V1.0_VALIDATION_PROTOCOL_2026-08-29.md`;
6. `models/lol/procedures/LOL_V1.0_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`;
7. `models/lol/reviews/LOL_V1.0_CLEAN_REBUILD_AUDIT_2026-08-29.md` when transition/history context is needed.

The mutable session lock and Airtable ledgers may be newer than the authority commit. Handoffs carry state only.

## Historical authority boundary

LoL v0.3.58 and all v0.x procedures remain preserved as historical/audit/research authority only.

They are **not active v1.0 analytical authority** and must not be blended into current Moneyline analysis.

In particular, do not require legacy:

- DIM/PDRL/PML certificates;
- CFC/DPS/LRO named gate tree;
- fixed 2SNAP/3SNAP/2CYCLE eligibility counts;
- KHMC/WMS/FFD/RNE/NKB;
- UDKC/KPA/KMS/RLD/UCS/LAC;
- FRP/FCR/DOVC;
- derivative-family PRE_TAKE/GATE_SIG trees;
- derivative or fixed late-market buffers.

Useful causal ideas already absorbed into v1.0 remain active only through the v1.0 files.

## v1.0 analytical core

From one team's perspective:

- draft unit `D = +1 / 0 / -1`;
- live variables `R/X/O/T` each on `-2..+2`;
- mechanism contradiction `INTACT / WEAKENING / BROKEN / REPLACED`;
- `D_eff = D / 0.5D / 0` according to mechanism state;
- `S = 1.0*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`;
- `P = clamp(50% + 3*S pp, 15%, 85%)`;
- raw book implied probability `q = 1/odds`;
- TAKE CANDIDATE requires `P - q >= +5.0pp` and odds `>=1.60`.

Probability must be estimated before price is used as analytical evidence.

Structures are context by default and matter only through demonstrated forward-control consequences.

## Active execution controls

- synchronized live evidence required;
- executable live Moneyline required;
- no pregame/immediate-postdraft betting TAKE;
- no universal fixed snapshot-count gate;
- position-blind reassessment required;
- stale/contradictory evidence fails closed;
- material state change expires a pending TAKE CANDIDATE;
- price-only movement with unchanged state may be repriced from the already locked model probability;
- no rescue, martingale, chasing, averaging down or stake escalation;
- actual exposure remains 0u;
- default fixed shadow stake remains 0.25u.

## User line-existence confirmation gate — ACTIVE

Standing instruction remains:

Only log a bet when the user confirms the exact quoted line/odds still exist.

Required state:

`USER_LINE_CONFIRMATION = PENDING / CONFIRMED / FAILED`

- `PENDING`: TAKE CANDIDATE only; no Position, W/L or P/L;
- `CONFIRMED`: accepted shadow Position may be created if no material state change invalidated the candidate;
- `FAILED`: no Position exists;
- moved price must be repriced/reassessed before acceptance.

## Validation freeze

The v1.0 analytical core is frozen for the initial accepted Moneyline sample.

- 10 confirmed Positions: diagnostic checkpoint only;
- 20 confirmed Positions: minimum architectural review point;
- 30 confirmed Positions: preferred first full calibration review.

Do not mutate the model after one ordinary loss.

Primary error taxonomy only:

- `DRAFT READ ERROR`;
- `LIVE STATE ERROR`;
- `PROBABILITY/CALIBRATION ERROR`;
- `PRICE/EXECUTION ERROR`.

## Airtable workflow

GitHub is model/rules authority. Airtable remains the canonical historical map/snapshot/position ledger.

- preserve all v0.x records unchanged;
- HOLD/PASS may be stored as snapshots when useful;
- unconfirmed TAKE CANDIDATE is not a Position;
- confirmed v1.0 Position should preserve exact odds, entry state, 0.25u shadow stake, 0u actual exposure and compact `ML_CORE[...]` entry evidence;
- never claim a write/settlement occurred unless the connector action actually succeeded.

## Bootstrap / continuation requirement

Every continuation/new chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this mutable lock and verify `LOL-2026-08-29-V1-ML-1341-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `1be61970a3b586fd173479a4e591cfe391e03f0f`;
5. load the active v1.0 stack in the exact order specified by locked `CURRENT_MODEL.md`;
6. use Airtable only as ledger/history authority, not analytical model authority;
7. load the latest applicable live handoff last.

If the lock/authority cannot be matched:

`MODEL LOCK MISMATCH — HOLD`

If the procedural circuit breaker becomes active:

`TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`
