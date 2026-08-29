# Current League of Legends Model

**Canonical namespace:** `models/lol/`  
**Activated:** 2026-08-29 UTC+7

# ACTIVE MODEL

**LoL v1.2 — Strength-Prior Moneyline + Duration Core**

v1.2 is a targeted Moneyline architecture repair authorized by the user after v1.1 exposed a clear mechanical omission: persistent team strength was not represented and all maps began from a neutral 50% ML baseline.

Duration remains analytically unchanged from v1.1.

Active Moneyline rules:

`models/lol/rules/MODEL_RULES_LOL_V1.2_MONEYLINE_STRENGTH_PRIOR_CORE.md`

Active Moneyline live procedure:

`models/lol/procedures/LOL_V1.2_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md`

Active Duration rules — unchanged:

`models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md`

Active Duration live procedure — unchanged:

`models/lol/procedures/LOL_V1.1_DURATION_LIVE_PROCEDURE_2026-08-29.md`

Active validation protocol:

`models/lol/procedures/LOL_V1.2_VALIDATION_PROTOCOL_2026-08-29.md`

Active authority/execution governance:

`models/lol/procedures/LOL_V1.2_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`

Mandatory version-neutral bootstrap:

`models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`

Transition review:

`models/lol/reviews/LOL_V1.2_TEAM_STRENGTH_PRIOR_PATCH_2026-08-29.md`

Historical context when needed:

`models/lol/reviews/LOL_V1.1_DURATION_ENABLEMENT_2026-08-29.md`

`models/lol/reviews/LOL_V1.0_CLEAN_REBUILD_AUDIT_2026-08-29.md`

---

# 1. Active betting scope

`LIVE MONEYLINE + LIVE DURATION OVER/UNDER`

Retired from betting:

- Kill Handicap;
- Total Kills.

No pregame or immediate-postdraft betting TAKE.

---

# 2. Moneyline v1.2

## 2.1 Team-strength prior

From Team A perspective:

`K = -2,-1,0,+1,+2`

Interpretation:

- `+2` clear major persistent strength edge;
- `+1` meaningful persistent strength edge;
- `0` no robust persistent edge;
- `-1` meaningful persistent disadvantage;
- `-2` clear major persistent disadvantage.

Use only pre-series non-price evidence: recent official same-league results, opponent quality/competition path, roster continuity/substitutions and established current form.

Never use sportsbook odds, current-map state, same-series earlier map results or hindsight to choose `K`.

For a series, freeze `K` before Game 1 and keep it fixed unless a genuine roster/availability change occurs. If v1.2 activates mid-series, reconstruct `K` only from evidence that existed before Game 1.

Baseline:

`P0(A) = 50% + 10*K percentage points`

## 2.2 Draft prior

`SIDE A / EVEN / SIDE B`

From Team A perspective:

`D = +1 / 0 / -1`

Draft remains a small map-specific composition/mechanism prior and must not absorb team reputation.

## 2.3 Live state

`R/X/O/T` each on `-2..+2`:

- `R` role-weighted useful resources;
- `X` realized meaningful fight/contact execution;
- `O` objective access/control and next compulsory cycle;
- `T` composition trajectory.

Mechanism contradiction:

`INTACT / WEAKENING / BROKEN / REPLACED`

`D_eff = D / 0.5D / 0` for intact / weakening / broken-or-replaced.

## 2.4 Probability

`S = 1.0*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`

`P(A) = clamp(P0(A) + 3*S pp, 15%, 85%)`

`P(B) = 100% - P(A)`

Lock `K/P0`, draft/live state and probability before offered Moneyline price is used as analytical evidence.

For ML, towers/structures remain contextual unless they demonstrably change forward control.

## 2.5 Price rule

`BOOK IMPLIED = 1/odds`

`EDGE = MODEL PROBABILITY - BOOK IMPLIED`

TAKE CANDIDATE requires:

- odds `>=1.60`;
- edge `>=+5.0pp`;
- synchronized executable live ML;
- price-independent `K/P0`;
- probability locked before price use;
- position-blind reassessment;
- actual exposure `0u`.

---

# 3. Duration Core — unchanged from v1.1

Neutral final-duration anchor:

`31.0 minutes`

At current clock `t`:

`R0(t) = max(5.0, 31.0 - t)`

Score `V/Q/H/T` on `-2..+2`:

- `V` net conversion velocity;
- `Q` compulsory-cycle spacing;
- `H` terminal path depth;
- `T` terminal trajectory.

Absent conversion opportunity is neutral, not stall proof.

`ER = max(2.0, R0 - 1.5*V + 1.0*Q + 1.0*H + 0.75*T)`

`F = t + ER`

Lock `F` before line/odds are used as analytical evidence.

For line `L`:

`P(OVER) = clamp(50% + 7*(F-L) pp, 15%, 85%)`

`P(UNDER) = 100% - P(OVER)` when settlement semantics are clear.

Duration TAKE CANDIDATE requires:

- odds `>=1.60`;
- selected-side edge `>=+7.5pp`;
- synchronized executable market;
- position-blind reassessment;
- actual exposure `0u`.

---

# 4. Verdict semantics

- `HOLD` — state/market/strength prior cannot be scored responsibly;
- `PASS` — usable state but no executable selection clears its family requirements;
- `TAKE CANDIDATE` — analytical/execution requirements pass, but no Position yet.

Every TAKE CANDIDATE sets:

`USER_LINE_CONFIRMATION=PENDING`

ML confirmation = exact team ML + odds.

Duration confirmation = exact Over/Under side + line + odds.

No Position, W/L or P/L exists while confirmation is pending.

---

# 5. Shared execution controls

- GitHub = analytical/governance authority;
- Airtable = canonical map/snapshot/position ledger;
- valid frozen Session Authority Lock required;
- synchronized live evidence;
- executable active-family market;
- position-blind reassessment;
- probability / Duration `F` locked before price evidence;
- minimum odds `1.60`;
- ML edge `+5.0pp`;
- Duration edge `+7.5pp`;
- exact user line confirmation before accepted Position;
- default shadow stake `0.25u` unless lock changes it;
- actual exposure `0u` unless explicitly changed;
- no chasing/rescue/martingale/averaging down/stake escalation;
- no retroactive accepted Position creation;
- material state change expires pending candidate.

ML and Duration qualify independently.

---

# 6. Validation epoch

v1.1 closes prospectively at:

- `ML_SAMPLE_N=0` accepted Positions;
- `DURATION_SAMPLE_N=0` accepted Positions.

Game 1 retroactive user-designated ledger entries remain outside validation.

v1.2 begins:

- `ML_SAMPLE_N=0`;
- `DURATION_SAMPLE_N=0`.

Per family:

- 10 accepted Positions: diagnostic checkpoint only;
- 20: minimum architecture review;
- 30: preferred full calibration review.

Primary taxonomy:

- `DRAFT READ ERROR`;
- `LIVE STATE ERROR`;
- `PROBABILITY/CALIBRATION ERROR`;
- `PRICE/EXECUTION ERROR`.

A material future change normally requires repeated evidence, persistent calibration bias, a clear mechanical defect, or explicit user-authorized redesign.

---

# 7. Historical authority boundary

All v0.x, v1.0 and v1.1 analytical generations remain historical/audit authority after v1.2 activation.

Do not blend legacy DIM/PDRL/PML, CFC/DPS/LRO, KHMC/WMS/RNE/NKB, TK recurrence/FRP, historical Duration DOVC/FCR/FRP, PRE_TAKE trees or fixed snapshot/cycle gates into v1.2.

Do not relabel T1–BFX Games 1 or 2 as v1.2. v1.2 is prospective from its fresh lock.

---

# 8. Mandatory bootstrap / load order

Every new LoL chat/session must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch mutable `models/lol/session/CURRENT_SESSION_LOCK.md`;
4. if lock ACTIVE, re-fetch `CURRENT_MODEL.md` at exact `authority_commit`;
5. from that same authority commit load in order:
   1. `models/lol/rules/MODEL_RULES_LOL_V1.2_MONEYLINE_STRENGTH_PRIOR_CORE.md`;
   2. `models/lol/procedures/LOL_V1.2_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md`;
   3. `models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md`;
   4. `models/lol/procedures/LOL_V1.1_DURATION_LIVE_PROCEDURE_2026-08-29.md`;
   5. `models/lol/procedures/LOL_V1.2_VALIDATION_PROTOCOL_2026-08-29.md`;
   6. `models/lol/procedures/LOL_V1.2_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`;
   7. `models/lol/reviews/LOL_V1.2_TEAM_STRENGTH_PRIOR_PATCH_2026-08-29.md` when transition/series prior context is needed;
   8. `models/lol/reviews/LOL_V1.1_DURATION_ENABLEMENT_2026-08-29.md` when Duration transition context is needed;
   9. `models/lol/reviews/LOL_V1.0_CLEAN_REBUILD_AUDIT_2026-08-29.md` when older rebuild context is needed;
6. use Airtable only as ledger/history authority;
7. load latest applicable live handoff last.

If lock/authority cannot be matched:

`MODEL LOCK MISMATCH — HOLD`

If activation/lock construction is incomplete:

`MODEL REBUILD IN PROGRESS — HOLD`

If procedural breaker active:

`TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`

---

# 9. Compact live output

## Moneyline

`ML — [A vs B]`

`Strength: K [x] | P0 [xx]% — [non-price basis]`

`Draft: [A / EVEN / B] — [mechanism]`

`Live: R [x] | X [x] | O [x] | T [x] | Mechanism [state]`

`Model: A [xx]% / B [yy]%`

`Price: [side] @[odds] -> book [q]% | edge [e]pp`

`Verdict: HOLD / PASS / TAKE CANDIDATE — [cause]`

## Duration

`DUR — Clock [t] | V [x] | Q [x] | H [x] | T [x] | F [xx.x]m`

`Line: [O/U L @odds] | model [p]% | book [q]% | edge [e]pp`

`Verdict: HOLD / PASS / TAKE CANDIDATE — [cause]`

For TAKE CANDIDATE add exact line-confirmation request.

---

# 10. Activation statement

The user explicitly authorized the v1.2 Moneyline strength-prior repair on 2026-08-29 UTC+7.

**LoL v1.2 becomes active only when a fresh Session Authority Lock points to the authority commit containing this completed `CURRENT_MODEL.md` and the complete required stack.**

Until that lock exists:

`MODEL REBUILD IN PROGRESS — HOLD`
