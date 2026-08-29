# Current League of Legends Model

**Canonical namespace:** `models/lol/`  
**Activated:** 2026-08-29 UTC+7

# ACTIVE MODEL

**LoL v1.0 — Moneyline Core**

This is a clean major-generation rebuild. It does **not** patch or simplify the v0.3.58 decision tree in place.

Active analytical rules:

`models/lol/rules/MODEL_RULES_LOL_V1.0_MONEYLINE_CORE.md`

Active live procedure:

`models/lol/procedures/LOL_V1.0_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md`

Active validation protocol:

`models/lol/procedures/LOL_V1.0_VALIDATION_PROTOCOL_2026-08-29.md`

Active authority/execution governance:

`models/lol/procedures/LOL_V1.0_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`

Mandatory version-neutral new-chat bootstrap:

`models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`

Rebuild audit / historical transition record:

`models/lol/reviews/LOL_V1.0_CLEAN_REBUILD_AUDIT_2026-08-29.md`

---

# 1. Active betting scope

`LIVE MONEYLINE ONLY`

Temporarily retired from betting:

- Kill Handicap;
- Total Kills;
- Duration.

These families and their historical procedures remain in GitHub/Airtable for audit/history, but they are not active v1.0 betting authority and their gates must not be imported into Moneyline for compatibility.

v1.0 does not issue pregame/immediate-postdraft Moneyline TAKES. Draft supplies the prior; betting requires synchronized live state.

---

# 2. v1.0 architecture at a glance

## Draft prior

Output:

`SIDE A / EVEN / SIDE B`

State the concrete professional win mechanism. Include exact roles, professional patch/context and Fearless/restricted-pool effects where materially relevant without restoring the old acronym tree.

## Live state

Score four variables from one team's perspective on `-2..+2`:

- `R` — role-weighted resources;
- `X` — realized fight/contact execution;
- `O` — objective access/control and next compulsory cycle;
- `T` — composition trajectory.

Structures are context by default and affect the model only when they cause a forward-control change.

## Mechanism contradiction

Original draft thesis is:

- `INTACT`;
- `WEAKENING`;
- `BROKEN`;
- `REPLACED`.

A directional/verdict reversal requires a genuine causal state change, not an attractive price or descriptive-stat movement.

## Probability

Draft unit from Team A perspective:

`D = +1 / 0 / -1`

Effective draft:

- INTACT -> `D_eff = D`;
- WEAKENING -> `D_eff = 0.5D`;
- BROKEN or REPLACED -> `D_eff = 0`.

State score:

`S = 1.0*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`

Model probability:

`P(A) = clamp(50% + 3*S percentage points, 15%, 85%)`

`P(B) = 100% - P(A)`

Probability is estimated **before** offered price is used as evidence.

## Price

For decimal odds `O`:

`BOOK IMPLIED = 1 / O`

`EDGE = MODEL PROBABILITY - BOOK IMPLIED`

Initial frozen TAKE requirements:

- decimal odds `>= 1.60`;
- edge `>= +5.0 percentage points`.

Use raw implied probability during the first validation sample.

---

# 3. Execution policy

Standing controls:

- GitHub is analytical/governance authority;
- Airtable is canonical historical map/snapshot/position ledger;
- valid frozen Session Authority Lock required before TAKE CANDIDATE;
- synchronized live evidence required;
- executable Moneyline required;
- position-blind reassessment required;
- model probability locked before price comparison;
- minimum odds 1.60;
- required edge +5.0pp;
- user must explicitly confirm the quoted line/odds still exist before a Position is created;
- default shadow stake 0.25u;
- actual exposure 0u;
- no chasing, rescue, martingale, averaging down or stake escalation;
- no retroactive Position creation;
- historical prediction result and process validity remain separate.

Verdicts:

- `HOLD` — state/market not usable enough to score responsibly;
- `PASS` — usable state, but price/edge or execution controls do not qualify;
- `TAKE CANDIDATE` — qualifies analytically; `USER_LINE_CONFIRMATION=PENDING`, not yet a Position.

---

# 4. Initial validation freeze

Core v1.0 rules are frozen for the initial user-confirmed executable Moneyline Position sample.

- diagnostic checkpoint: 10 Positions, no architecture change by default;
- minimum architecture review point: 20 Positions;
- preferred first full calibration review: 30 Positions.

Do not mutate the model after one ordinary loss.

Primary error taxonomy only:

- `DRAFT READ ERROR`;
- `LIVE STATE ERROR`;
- `PROBABILITY/CALIBRATION ERROR`;
- `PRICE/EXECUTION ERROR`.

A material analytical change during the freeze requires explicit user authorization and begins a new calibration epoch rather than silently mixing samples.

---

# 5. Historical authority and retired architecture

All LoL v0.x materials, including v0.3.58 and its accumulated amendments/overlays, remain preserved as **HISTORICAL / AUDIT / RESEARCH AUTHORITY ONLY**.

They are not active v1.0 analytical authority.

This includes legacy named analytical systems such as, where applicable:

- DIM / PDRL / PML certificates;
- CFC / DPS / LRO gate tree;
- fixed 2SNAP / 3SNAP / 2CYCLE eligibility counts;
- KHMC / WMS / FFD / RNE / NKB;
- UDKC / KPA / KMS / RLD / UCS / LAC;
- FRP / FCR / DOVC;
- family-specific PRE_TAKE/GATE_SIG trees;
- fixed derivative/late-market buffers.

Useful ideas from those systems have already been absorbed into v1.0's compact Draft Prior, `R/X/O/T`, mechanism contradiction and execution controls where they earned retention.

Do not delete, rewrite or relabel:

- historical GitHub files;
- Airtable Maps;
- Airtable Snapshots;
- Airtable Positions;
- screenshots;
- reviews;
- results;
- historical P/L;
- original historical model/version labels.

LoL v0.3.59 and v0.3.60 also remain historical/retired and are not revived.

---

# 6. Mandatory bootstrap / load order

Every new LoL chat/session must:

1. fetch this `models/lol/CURRENT_MODEL.md` first from default branch;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch mutable `models/lol/session/CURRENT_SESSION_LOCK.md`;
4. if the lock is ACTIVE, re-fetch this `CURRENT_MODEL.md` at its frozen `authority_commit`;
5. from that same authority commit load, in order:
   1. `models/lol/rules/MODEL_RULES_LOL_V1.0_MONEYLINE_CORE.md`;
   2. `models/lol/procedures/LOL_V1.0_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md`;
   3. `models/lol/procedures/LOL_V1.0_VALIDATION_PROTOCOL_2026-08-29.md`;
   4. `models/lol/procedures/LOL_V1.0_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`;
   5. `models/lol/reviews/LOL_V1.0_CLEAN_REBUILD_AUDIT_2026-08-29.md` when historical-transition context is needed;
6. consult Airtable only as live/historical ledger, not analytical model authority;
7. load the latest applicable live handoff last.

Historical v0.x analytical/procedure files are not part of the active load order unless explicitly opened for a review/audit task. If opened, they do not become active authority.

If an ACTIVE lock cannot be matched:

`MODEL LOCK MISMATCH — HOLD`

If the new generation has been authorized but activation/lock construction is incomplete:

`MODEL REBUILD IN PROGRESS — HOLD`

If an active procedural circuit breaker is set:

`TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`

---

# 7. Historical calibration basis for this rebuild

The clean rebuild audit is the canonical transition record. It uses recent evidence including:

- EDG–NIP Game 1: tower/resource improvement was over-read as repaired ML control while NIP retained the decisive objective/fight mechanism;
- BRO–BFX Game 2: a correct directional collapse read was complicated by derivative expression/sign handling;
- TH–SHFT Game 2: early map control was incorrectly extrapolated into large kill-margin persistence;
- NS–BFX: ML opportunity could decay while waiting for legacy confirmation counts, while role-weighted state could identify value despite misleading raw kills.

These examples inform v1.0's simpler variables and probability discipline. They do not create one new named gate per failure.

---

# 8. Activation statement

The user explicitly authorized a new major model generation on 2026-08-29 UTC+7.

**LoL v1.0 — Moneyline Core is the active analytical model once the fresh v1.0 Session Authority Lock points to the authority commit containing this file and the full v1.0 stack.**

Until that fresh lock exists, live betting remains:

`MODEL REBUILD IN PROGRESS — HOLD`
