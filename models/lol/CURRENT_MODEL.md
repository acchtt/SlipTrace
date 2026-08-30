# Current League of Legends Model

**Canonical namespace:** `models/lol/`  
**Activated:** 2026-08-29 UTC+7  
**Execution / benchmark patches activated:** 2026-08-30 UTC+7

# ACTIVE MODEL

**LoL v1.3 — Hierarchy Moneyline + Duration Core**

v1.3 uses:

`REPRODUCIBLE LEAGUE-RELATIVE TEAM BENCHMARK = LIGHT STARTING PRIOR`
`DRAFT = MEANINGFUL MAP-SPECIFIC CORRECTION`
`LIVE STATE = DOMINANT ONCE REAL EVIDENCE EXISTS`

On 2026-08-30 the user explicitly added two prospective controls:
1. **do not take a bet just because the price looks good** — selected-side non-price causal thesis must already be positive;
2. construct team-strength `K` from our own **Gol.gg league-relative benchmark**, not loose subjective tiering.

Duration remains analytically unchanged from v1.1/v1.2.

Active team benchmark procedure:
`models/lol/procedures/LOL_V1.3_TEAM_BENCHMARK_GOLGG_2026-08-30.md`

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

Transition context when needed:
- `models/lol/reviews/LOL_V1.3_HIERARCHY_WEIGHT_PATCH_2026-08-29.md`
- `models/lol/reviews/LOL_V1.2_TEAM_STRENGTH_PRIOR_PATCH_2026-08-29.md`

---

# 1. Active betting scope

`LIVE MONEYLINE + LIVE DURATION OVER/UNDER`

Retired from betting:
- Kill Handicap;
- Total Kills.

No pregame or immediate-postdraft betting TAKE.

---

# 2. Moneyline v1.3 hierarchy

## Team benchmark -> K

Primary statistical source: **Games of Legends / gol.gg** same-league/tournament team tables, frozen before Game 1.

Within the current league/tournament peer set:

`B_split = 0.30*z(WinRate) + 0.30*z(GDM) + 0.20*z(GD@15) + 0.10*z(TowerDiff/Game) + 0.05*z(DRA%) + 0.05*z(NASH%)`

Current/previous split blend by current games `G`:
- `G>=15`: 70/30;
- `8<=G<=14`: 55/45;
- `G<8`: 40/60;
subject to roster-continuity adjustment in the benchmark procedure.

Re-standardize blended peer scores to final `B`.

For Team A vs B:

`GAP=B(A)-B(B)`

- `|GAP|<0.50` -> `K=0`
- `0.50<=|GAP|<1.25` -> `K=sign(GAP)*1`
- `|GAP|>=1.25` -> `K=sign(GAP)*2`

Sportsbook odds, current-map state and same-series results are forbidden from benchmark construction.

Freeze `K` for the series after the pre-series benchmark unless genuine roster/availability change or explicit model redesign occurs.

Light baseline:

`P0(A)=50%+5*K pp`

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

## Probability and thesis

`C=1.5*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`

`S=C`

`P(A)=clamp(P0(A)+3*S pp,15%,85%)`

`P(B)=100%-P(A)`

Lock `TEAM_BENCH`, K/P0, draft/live state, causal thesis and probability before offered ML price is analytical evidence.

### Causal thesis gate

For the selected side:

`C > 0`

A coherent, currently reachable draft/live win mechanism is also required.

Hard interpretation:
- team strength alone cannot make a bet;
- price cannot create the bet;
- if selected-side `C<=0`, verdict is `PASS` even if apparent numerical edge is large.

## ML price rule

`BOOK IMPLIED=1/odds`

`EDGE=MODEL PROBABILITY-BOOK IMPLIED`

TAKE CANDIDATE requires:
- benchmark-certified price-independent K/P0;
- selected-side `C>0` and coherent reachable mechanism;
- synchronized executable live ML;
- odds >=1.60;
- edge >=+5.0pp;
- probability/thesis locked before price;
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
- benchmark and ML probability/thesis / Duration F locked before price evidence;
- Moneyline price cannot create directional thesis;
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

Earlier v1.3 accepted Positions remain historical under the rules active at entry. Do not retroactively rewrite them.

The 2026-08-30 causal-thesis and Gol.gg benchmark patches apply prospectively from the fresh lock that activates this authority commit.

Review cadence per family:
- 10 accepted: diagnostic only;
- 20: minimum architecture review;
- 30: preferred full calibration review.

Primary taxonomy only:
- DRAFT READ ERROR
- LIVE STATE ERROR
- PROBABILITY/CALIBRATION ERROR
- PRICE/EXECUTION ERROR

Benchmark/tier construction error is `PROBABILITY/CALIBRATION ERROR`.

---

# 6. Historical authority boundary

All legacy analytical generations remain historical/audit authority only when not declared active here.

Do not blend historical certificate/gate stacks into v1.3.

---

# 7. Mandatory bootstrap / load order

Every new LoL chat/session must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch mutable `models/lol/session/CURRENT_SESSION_LOCK.md`;
4. if lock ACTIVE, re-fetch `CURRENT_MODEL.md` at exact `authority_commit`;
5. from that same authority commit load in order:
   1. `models/lol/procedures/LOL_V1.3_TEAM_BENCHMARK_GOLGG_2026-08-30.md`;
   2. `models/lol/rules/MODEL_RULES_LOL_V1.3_MONEYLINE_HIERARCHY_CORE.md`;
   3. `models/lol/procedures/LOL_V1.3_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md`;
   4. `models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md`;
   5. `models/lol/procedures/LOL_V1.1_DURATION_LIVE_PROCEDURE_2026-08-29.md`;
   6. `models/lol/procedures/LOL_V1.3_VALIDATION_PROTOCOL_2026-08-29.md`;
   7. `models/lol/procedures/LOL_V1.3_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`;
   8. transition reviews only when needed;
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
`Strength: K [x] | P0 [xx]% | Benchmark gap [x.xx] SD`
`Draft: [A/EVEN/B] — [mechanism]`
`Live: R [x] | X [x] | O [x] | T [x] | Mechanism [state]`
`Thesis: C [x] | PASS/FAIL`
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

The user explicitly authorized the hierarchy weighting repair during T1 vs BNK FEARX Game 3.

The user explicitly authorized the causal-thesis execution gate after TH vs MKOI Game 2.

The user explicitly authorized Gol.gg-derived league-relative team benchmarking on 2026-08-30.

**This benchmark-aware v1.3 stack becomes active only when a fresh Session Authority Lock points to the authority commit containing this completed `CURRENT_MODEL.md` and the complete declared stack.**
