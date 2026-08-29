# Current League of Legends Model

**Canonical namespace:** `models/lol/`  
**Activated:** 2026-08-29 UTC+7

# ACTIVE MODEL

**LoL v1.3 — Hierarchy Moneyline + Duration Core**

v1.3 is the user-authorized prospective Moneyline weighting repair after T1 vs BNK FEARX Game 3. It keeps the v1.2 independent team-strength tier but makes strength a lighter starting prior, gives draft a meaningful map-specific correction, and lets synchronized live state dominate once real evidence develops.

Duration remains analytically unchanged from v1.1/v1.2.

Active Moneyline rules:
`models/lol/rules/MODEL_RULES_LOL_V1.3_MONEYLINE_HIERARCHY_CORE.md`

Active Moneyline live procedure:
`models/lol/procedures/LOL_V1.3_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md`

Active Duration rules — unchanged:
`models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md`

Active Duration live procedure — unchanged:
`models/lol/procedures/LOL_V1.1_DURATION_LIVE_PROCEDURE_2026-08-29.md`

Active validation protocol:
`models/lol/procedures/LOL_V1.3_VALIDATION_PROTOCOL_2026-08-29.md`

Active authority/execution governance:
`models/lol/procedures/LOL_V1.3_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`

Mandatory bootstrap:
`models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`

Transition review:
`models/lol/reviews/LOL_V1.3_HIERARCHY_WEIGHT_PATCH_2026-08-29.md`

Historical transition context when needed:
- `models/lol/reviews/LOL_V1.2_TEAM_STRENGTH_PRIOR_PATCH_2026-08-29.md`
- `models/lol/reviews/LOL_V1.1_DURATION_ENABLEMENT_2026-08-29.md`
- `models/lol/reviews/LOL_V1.0_CLEAN_REBUILD_AUDIT_2026-08-29.md`

---

# 1. Active betting scope

`LIVE MONEYLINE + LIVE DURATION OVER/UNDER`

Retired from betting:
- Kill Handicap;
- Total Kills.

No pregame or immediate-postdraft betting TAKE.

---

# 2. Moneyline v1.3 hierarchy

## Team strength

From Team A perspective:

`K=-2,-1,0,+1,+2`

Use only pre-series non-price evidence. Never use sportsbook odds, current-map state, same-series earlier map results or hindsight to choose K.

Freeze K for the series absent genuine roster/availability change.

Light baseline:

`P0(A)=50%+5*K percentage points`

## Draft

`D=+1/0/-1` from Team A perspective.

Draft is map-specific and separate from team reputation.

## Live state

`R/X/O/T=-2..+2`:
- R role-weighted useful resources;
- X realized meaningful fight/contact execution;
- O objective access/control and next compulsory cycle;
- T reachable composition trajectory.

Mechanism contradiction:
`INTACT / WEAKENING / BROKEN / REPLACED`

`D_eff=D / 0.5D / 0` for intact / weakening / broken-or-replaced.

## Probability

`S=1.5*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`

`P(A)=clamp(P0(A)+3*S pp,15%,85%)`

`P(B)=100%-P(A)`

Lock K/P0, draft/live state and probability before offered Moneyline price is used as analytical evidence.

Causal hierarchy:

`LIGHT TEAM-STRENGTH PRIOR -> MEANINGFUL DRAFT CORRECTION -> LIVE STATE DOMINATES AS EVIDENCE ACCUMULATES`

## ML price rule

`BOOK IMPLIED=1/odds`

`EDGE=MODEL PROBABILITY-BOOK IMPLIED`

TAKE CANDIDATE requires:
- synchronized executable live ML;
- odds >=1.60;
- edge >=+5.0pp;
- price-independent K/P0;
- probability locked before price use;
- position-blind;
- actual exposure 0u.

---

# 3. Duration Core — unchanged

Neutral anchor `31.0 minutes`.

At current clock t:

`R0(t)=max(5.0,31.0-t)`

Score `V/Q/H/T=-2..+2`.

`ER=max(2.0,R0-1.5*V+1.0*Q+1.0*H+0.75*T)`

`F=t+ER`

Lock F before line/odds are analytical evidence.

For line L:

`P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`

`P(UNDER)=100%-P(OVER)` when settlement semantics are clear.

Duration TAKE CANDIDATE requires odds >=1.60 and selected-side edge >=+7.5pp.

Absent conversion opportunity is neutral, not stall proof.

---

# 4. Verdict / execution controls

Verdicts:
- HOLD
- PASS
- TAKE CANDIDATE

Every TAKE CANDIDATE sets `USER_LINE_CONFIRMATION=PENDING`.

No Position until exact quoted market is confirmed before material state change.

Shared controls:
- GitHub analytical/governance authority;
- Airtable canonical ledger/history only;
- valid active Session Authority Lock;
- synchronized executable evidence;
- position-blind reassessment;
- ML probability / Duration F locked before price evidence;
- minimum odds 1.60;
- ML edge +5.0pp;
- Duration edge +7.5pp;
- default shadow stake 0.25u unless lock changes it;
- actual exposure 0u;
- no chasing/rescue/martingale/averaging down/stake escalation;
- no retroactive accepted Position creation;
- material state change expires pending candidate;
- ML and Duration qualify independently.

---

# 5. Validation epoch

v1.2 remains historical through Game 3 of T1 vs BNK FEARX.

v1.3 is prospective from the fresh post-Game-3 lock.

Initial v1.3 Moneyline accepted sample:
`ML_SAMPLE_N=0`

Duration sample continues unchanged and remains family-separated.

Review cadence per family:
- 10 accepted: diagnostic only;
- 20: minimum architecture review;
- 30: preferred full calibration review.

Primary taxonomy only:
- DRAFT READ ERROR
- LIVE STATE ERROR
- PROBABILITY/CALIBRATION ERROR
- PRICE/EXECUTION ERROR

---

# 6. Historical authority boundary

All v0.x/v1.0/v1.1/v1.2 analytical generations remain historical/audit authority only after v1.3 activation.

Do not blend legacy certificate/gate stacks into v1.3.

Do not relabel earlier T1–BFX maps as v1.3.

---

# 7. Mandatory bootstrap / load order

Every new LoL chat/session must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch mutable `models/lol/session/CURRENT_SESSION_LOCK.md`;
4. if lock ACTIVE, re-fetch `CURRENT_MODEL.md` at exact `authority_commit`;
5. from that same authority commit load in order:
   1. `models/lol/rules/MODEL_RULES_LOL_V1.3_MONEYLINE_HIERARCHY_CORE.md`;
   2. `models/lol/procedures/LOL_V1.3_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md`;
   3. `models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md`;
   4. `models/lol/procedures/LOL_V1.1_DURATION_LIVE_PROCEDURE_2026-08-29.md`;
   5. `models/lol/procedures/LOL_V1.3_VALIDATION_PROTOCOL_2026-08-29.md`;
   6. `models/lol/procedures/LOL_V1.3_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`;
   7. `models/lol/reviews/LOL_V1.3_HIERARCHY_WEIGHT_PATCH_2026-08-29.md` when transition context is needed;
   8. `models/lol/reviews/LOL_V1.2_TEAM_STRENGTH_PRIOR_PATCH_2026-08-29.md` when earlier strength-prior context is needed;
6. use Airtable only as ledger/history authority;
7. load latest applicable live handoff last.

If lock/authority cannot be matched:
`MODEL LOCK MISMATCH — HOLD`

If activation/lock construction incomplete:
`MODEL REBUILD IN PROGRESS — HOLD`

If procedural breaker active:
`TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`

---

# 8. Compact live output

Moneyline:
`Strength: K [x] | P0 [xx]%`
`Draft: [A/EVEN/B] — [mechanism]`
`Live: R [x] | X [x] | O [x] | T [x] | Mechanism [state]`
`Model: A [xx]% / B [yy]%`
`Price: [side] @[odds] -> book [q]% | edge [e]pp`
`Verdict: HOLD / PASS / TAKE CANDIDATE`

Duration:
`Clock [t] | V [x] | Q [x] | H [x] | T [x] | F [xx.x]m`
`Line: [O/U L @odds] | model [p]% | book [q]% | edge [e]pp`
`Verdict: HOLD / PASS / TAKE CANDIDATE`

For any TAKE CANDIDATE add exact line confirmation request.

---

# 9. Activation statement

The user explicitly authorized this hierarchy weighting repair during T1 vs BNK FEARX Game 3, effective prospectively from the next game.

**LoL v1.3 becomes active only when a fresh Session Authority Lock points to the authority commit containing this completed `CURRENT_MODEL.md` and the complete v1.3 stack.**
