# Current League of Legends Model

**Canonical namespace:** `models/lol/`  
**Activated:** 2026-08-29 UTC+7

# ACTIVE MODEL

**LoL v1.1 — Moneyline + Duration Core**

v1.1 is a controlled scope extension of the clean v1.x architecture. The v1.0 Moneyline analytical formula is carried forward unchanged; Duration is reintroduced as a new small independent core after explicit user authorization.

It does **not** restore the v0.3.58 decision tree or historical Duration certificate stack.

Active Moneyline rules:

`models/lol/rules/MODEL_RULES_LOL_V1.1_MONEYLINE_CORE.md`

Active Moneyline live procedure:

`models/lol/procedures/LOL_V1.1_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md`

Active Duration rules:

`models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md`

Active Duration live procedure:

`models/lol/procedures/LOL_V1.1_DURATION_LIVE_PROCEDURE_2026-08-29.md`

Active validation protocol:

`models/lol/procedures/LOL_V1.1_VALIDATION_PROTOCOL_2026-08-29.md`

Active authority/execution governance:

`models/lol/procedures/LOL_V1.1_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`

Mandatory version-neutral bootstrap:

`models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`

Historical clean-rebuild record:

`models/lol/reviews/LOL_V1.0_CLEAN_REBUILD_AUDIT_2026-08-29.md`

v1.1 Duration enablement/calibration record:

`models/lol/reviews/LOL_V1.1_DURATION_ENABLEMENT_2026-08-29.md`

---

# 1. Active betting scope

`LIVE MONEYLINE + LIVE DURATION OVER/UNDER`

Retired from betting:

- Kill Handicap;
- Total Kills.

No active v1.1 TAKE may be issued for KH or TK.

Historical KH/TK/Duration files and Airtable records remain preserved for audit/research only and do not become active merely because Duration is re-enabled.

There are no pregame/immediate-postdraft betting TAKES. Draft may prepare mechanisms/priors; betting requires synchronized live state.

---

# 2. Moneyline Core — unchanged analytical formula

## Draft prior

`SIDE A / EVEN / SIDE B`

State concrete professional win mechanisms and relevant exact-role, patch, player-fit and Fearless/restricted-pool context.

From Team A perspective:

`D = +1 / 0 / -1`

## Live state

`R/X/O/T` each on `-2..+2`:

- `R` role-weighted resources;
- `X` realized fight/contact execution;
- `O` objective access/control and next compulsory cycle;
- `T` composition trajectory.

Mechanism contradiction:

`INTACT / WEAKENING / BROKEN / REPLACED`

`D_eff = D / 0.5D / 0` for intact / weakening / broken-or-replaced.

## Probability

`S = 1.0*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`

`P(A) = clamp(50% + 3*S pp, 15%, 85%)`

`P(B) = 100% - P(A)`

Probability is locked before offered ML price is used as analytical evidence.

## ML price rule

`BOOK IMPLIED = 1/odds`

`EDGE = MODEL PROBABILITY - BOOK IMPLIED`

TAKE CANDIDATE requires:

- odds `>=1.60`;
- edge `>=+5.0pp`.

For ML, towers/structures remain context by default and matter only through demonstrated forward-control consequences.

---

# 3. Duration Core

Duration uses one central final-time estimate to price both Over and Under.

The central estimate is completed **before the offered Duration line or odds are used as analytical evidence**.

## Calibration anchor

Initial neutral final-duration anchor:

`31.0 minutes`

Derived from available Airtable August 2026 completed LCK map history at activation: 31 usable durations, median about 30:55, mean about 31:59, standard deviation about 5.0 minutes.

For current clock `t` in decimal minutes:

`R0(t) = max(5.0, 31.0 - t)`

## Live Duration variables

Score `V/Q/H/T` on `-2..+2`:

- `V` — net conversion velocity; positive means faster terminal conversion, negative means demonstrated stalled/slow conversion;
- `Q` — compulsory-cycle spacing; positive means more clock before the next decisive cycle, negative means imminent decisive/terminal cycle;
- `H` — terminal path depth; positive means more real map/base layers remain, negative means short/open Nexus path;
- `T` — terminal trajectory; positive means current state-usable tools extend the game, negative means current state accelerates closure.

Absent conversion opportunity is neutral, not stall proof.

## Central final estimate

`ER = max(2.0, R0 - 1.5*V + 1.0*Q + 1.0*H + 0.75*T)`

`F = t + ER`

Lock `F` before reading the line as analytical evidence.

## Line probability

For Duration line `L`:

`P(OVER) = clamp(50% + 7*(F-L) pp, 15%, 85%)`

`P(UNDER) = 100% - P(OVER)`

If settlement rules make push/void handling materially unclear, HOLD.

## Duration price rule

`BOOK IMPLIED = 1/odds`

`EDGE = MODEL SIDE PROBABILITY - BOOK IMPLIED`

TAKE CANDIDATE requires:

- odds `>=1.60`;
- selected-side edge `>=+7.5pp`.

The higher Duration buffer reflects greater final-clock uncertainty.

Unlike ML, structures can directly affect Duration through `H` because remaining structural/base layers are literal terminal path length.

---

# 4. Verdict semantics

Active families use only:

- `HOLD` — synchronized current state/market cannot be scored responsibly;
- `PASS` — usable state, but no executable selection clears its family price/edge requirements or an execution control fails;
- `TAKE CANDIDATE` — analytical and execution requirements pass, but this is not yet a Position.

Every TAKE CANDIDATE sets:

`USER_LINE_CONFIRMATION=PENDING`

For ML the user must confirm exact team ML + odds.

For Duration the user must confirm exact Over/Under side + duration line + odds.

No Position, W/L or P/L exists while confirmation is pending.

---

# 5. Shared execution controls

- GitHub is analytical/governance authority;
- Airtable is canonical historical map/snapshot/position ledger;
- valid frozen Session Authority Lock required before TAKE CANDIDATE;
- synchronized live evidence required;
- executable active-family market required;
- position-blind reassessment required;
- model probability / central Duration estimate locked before price evidence;
- minimum decimal odds 1.60;
- ML edge requirement +5.0pp;
- Duration edge requirement +7.5pp;
- exact user line-existence confirmation before Position logging;
- default shadow stake 0.25u unless current lock changes it;
- actual exposure 0u unless explicitly changed by user;
- no chasing, rescue, martingale, averaging down or stake escalation;
- no retroactive Position creation;
- material state change expires a pending candidate;
- historical prediction result and process validity remain separate.

ML and Duration can both qualify on one map only if each independently clears its own model. One family is not evidence for the other.

---

# 6. Frozen validation epoch

The user explicitly authorized Duration activation while the v1.0 Moneyline-only accepted sample was still 0.

The v1.0 Moneyline-only epoch is therefore closed at 0 confirmed Positions and v1.1 starts fresh family-specific counts:

- `ML_SAMPLE_N = 0`;
- `DURATION_SAMPLE_N = 0`.

Per family:

- 10 confirmed Positions: diagnostic only;
- 20: minimum architectural review point;
- 30: preferred first full calibration review.

Do not mutate either core after one ordinary loss.

Primary error taxonomy remains:

- `DRAFT READ ERROR`;
- `LIVE STATE ERROR`;
- `PROBABILITY/CALIBRATION ERROR`;
- `PRICE/EXECUTION ERROR`.

Material analytical changes during the freeze require explicit user authorization and a new calibration epoch when applicable.

---

# 7. Historical authority boundary

All v0.x materials remain **HISTORICAL / AUDIT / RESEARCH AUTHORITY ONLY**.

This includes legacy named systems such as:

- DIM/PDRL/PML certificates;
- CFC/DPS/LRO gate trees;
- fixed snapshot/cycle counts;
- KHMC/WMS/RNE/NKB and other KH machinery;
- TK recurrence/FRP machinery;
- historical Duration DOVC/FCR/FRP and PRE_TAKE certificate trees;
- family-specific GATE_SIG/PRE_TAKE trees;
- fixed late-market buffers.

Useful causal lessons may be absorbed only through the compact active v1.1 variables and procedures.

The v1.0 generation remains preserved as historical authority. Its Moneyline analytical formula is carried forward unchanged into the new v1.1 Moneyline files; do not load v1.0 files in parallel with v1.1 active authority unless performing an audit comparison.

Do not delete/rewrite/relabel historical GitHub files, Airtable Maps, Snapshots, Positions, screenshots, reviews, results, model labels or P/L.

---

# 8. Mandatory bootstrap / load order

Every new LoL chat/session must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch mutable `models/lol/session/CURRENT_SESSION_LOCK.md`;
4. if lock is ACTIVE, re-fetch `CURRENT_MODEL.md` at its exact `authority_commit`;
5. from that same authority commit load in order:
   1. `models/lol/rules/MODEL_RULES_LOL_V1.1_MONEYLINE_CORE.md`;
   2. `models/lol/procedures/LOL_V1.1_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md`;
   3. `models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md`;
   4. `models/lol/procedures/LOL_V1.1_DURATION_LIVE_PROCEDURE_2026-08-29.md`;
   5. `models/lol/procedures/LOL_V1.1_VALIDATION_PROTOCOL_2026-08-29.md`;
   6. `models/lol/procedures/LOL_V1.1_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`;
   7. `models/lol/reviews/LOL_V1.1_DURATION_ENABLEMENT_2026-08-29.md` when transition/calibration context is needed;
   8. `models/lol/reviews/LOL_V1.0_CLEAN_REBUILD_AUDIT_2026-08-29.md` when older transition context is needed;
6. use Airtable as ledger/history authority, not analytical model authority;
7. load the latest applicable live handoff last.

Historical v0.x/v1.0 analytical files are excluded from active live authority unless opened explicitly for audit/review.

If lock/authority cannot be matched:

`MODEL LOCK MISMATCH — HOLD`

If v1.1 activation/lock construction is incomplete:

`MODEL REBUILD IN PROGRESS — HOLD`

If procedural circuit breaker is active:

`TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`

---

# 9. Compact live output

## Moneyline

`ML — [A vs B]`

`Draft: [A / EVEN / B] — [mechanism]`

`Live: R [x] | X [x] | O [x] | T [x] | Mechanism [state]`

`Model: A [xx]% / B [yy]%`

`Price: [side] @[odds] -> book [q]% | edge [e]pp`

`Verdict: HOLD / PASS / TAKE CANDIDATE — [cause]`

## Duration

`DUR — Clock [t] | V [x] | Q [x] | H [x] | T [x] | F [xx.x]m`

`Line: [O/U L @odds] | model [p]% | book [q]% | edge [e]pp`

`Verdict: HOLD / PASS / TAKE CANDIDATE — [cause]`

For any TAKE CANDIDATE add exact line-confirmation request.

---

# 10. Activation statement

The user explicitly authorized the v1.x clean major rebuild and later explicitly authorized Duration activation on 2026-08-29 UTC+7.

**LoL v1.1 — Moneyline + Duration Core becomes active only when a fresh Session Authority Lock points to the authority commit containing this completed `CURRENT_MODEL.md` and all required v1.1 files.**

Until that fresh lock exists:

`MODEL REBUILD IN PROGRESS — HOLD`
