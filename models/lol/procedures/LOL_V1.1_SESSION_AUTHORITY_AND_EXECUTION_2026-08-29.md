# LoL v1.1 Session Authority & Execution Governance — 2026-08-29

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Model:** LoL v1.1 — Moneyline + Duration Core

## 1. Purpose

Provide the minimum governance needed to run two active live market families—Moneyline and Duration—without reviving the v0.3.58 multi-family gate architecture.

---

# 2. Frozen authority

Every live v1.1 epoch requires an ACTIVE Session Authority Lock in:

`models/lol/session/CURRENT_SESSION_LOCK.md`

The lock must record:

- authority commit;
- active model generation;
- active market families;
- family-specific edge thresholds;
- minimum odds;
- circuit-breaker state;
- shadow stake and actual exposure;
- validation sample state;
- series scope when applicable.

When a lock is ACTIVE, analytical/procedural files must be loaded from its authority commit.

If the lock cannot be matched:

`MODEL LOCK MISMATCH — HOLD`

---

# 3. Active market families

Under v1.1:

- `Moneyline = ACTIVE`
- `Duration = ACTIVE`
- `Kill Handicap = RETIRED_FROM_BETTING`
- `Total Kills = RETIRED_FROM_BETTING`

Do not import KH/TK gates into either active family.

Historical v0.x Duration procedures are audit/research material only. DOVC/FCR/FRP and old Duration PRE_TAKE certificates are not active v1.1 authority.

---

# 4. Family-specific analytical interlocks

## 4.1 Moneyline

Before `TAKE CANDIDATE`, resolve the unchanged compact v1.0 record:

`ML_CORE[D=...;MC=...;R=...;X=...;O=...;T=...;S=...;P=...;BOOK=...;EDGE=...;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`

Requirements:

- synchronized executable Moneyline;
- probability locked before price is used as state evidence;
- odds >=1.60;
- edge >=+5.0pp;
- position-blind;
- actual exposure 0u.

## 4.2 Duration

Before `TAKE CANDIDATE`, resolve:

`DUR_CORE[t=...;V=...;Q=...;H=...;T=...;R0=...;ER=...;F=...;LINE=...;P_SIDE=...;BOOK=...;EDGE=...;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`

Requirements:

- synchronized executable Duration market;
- central final-duration `F` locked before line/odds are used as analytical evidence;
- settlement semantics sufficiently clear;
- odds >=1.60;
- selected-side edge >=+7.5pp;
- position-blind;
- actual exposure 0u.

These are compact execution interlocks, not named analytical gate trees.

---

# 5. State-change expiry

A TAKE CANDIDATE belongs to one assessed live decision window.

If a material live event occurs before user confirmation—meaningful fight, objective, resource swing, structure/base change, or schedule change—the candidate expires.

For ML, rebuild the relevant `R/X/O/T`/mechanism state.

For Duration, rebuild `V/Q/H/T` and central final estimate `F`.

If only the price changes with materially unchanged state:

- ML may reuse the locked win probability and reprice;
- Duration may reuse `F`, but a changed Duration line requires recalculating Over/Under probability from the new line before repricing.

---

# 6. User line confirmation

All active families require:

`USER_LINE_CONFIRMATION = PENDING / CONFIRMED / FAILED`

### PENDING

No Position, W/L or P/L.

### CONFIRMED

User confirms the exact quoted market still exists before material state change.

For Duration confirmation must include exact:

- Over/Under side;
- duration line;
- odds.

For Moneyline confirmation must include exact team ML and odds.

### FAILED

No accepted Position exists.

No retroactive logging because a candidate later wins.

---

# 7. Stake and position controls

- default shadow stake `0.25u` per accepted Position;
- actual exposure `0u`;
- no martingale;
- no rescue;
- no chasing;
- no averaging down;
- no stake escalation;
- no position-driven probability adjustment.

An ML Position does not justify a Duration hedge/rescue entry, and a Duration Position does not justify an ML rescue entry.

---

# 8. Simultaneous family candidates

ML and Duration may both qualify on the same map because they answer different questions.

Each must independently clear its own probability/price and execution rules.

Do not:

- treat ML confidence as automatic Duration evidence;
- treat Duration Over as evidence for underdog ML;
- treat a favorite ML edge as automatic Duration Under evidence.

Shared live evidence may inform both models only through each model's own variables.

---

# 9. Airtable truthfulness

Airtable remains the canonical historical map/snapshot/position ledger.

For v1.1:

- preserve all v0.x and v1.0 records unchanged;
- unconfirmed candidates may be snapshots but not Positions;
- accepted Position must preserve exact market family, selection, line where applicable, odds, entry clock, 0.25u shadow stake, 0u exposure, model generation and compact family record;
- settlement never rewrites entry probability or evidence;
- never claim logging/settlement succeeded unless the connector write actually succeeded.

---

# 10. Circuit breaker

Suspend new TAKE CANDIDATE issuance for material governance failures including:

- authority/model mismatch;
- actual exposure policy violation;
- Position created without user line confirmation;
- KH or TK Position created while retired;
- model probability/central duration materially back-fit from price;
- stale candidate reused after a material state change;
- missing synchronization/executability caused a false accepted entry.

Visible status:

`TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`

An ordinary prediction loss is not a circuit-breaker event.

---

# 11. Validation freeze

Use `models/lol/procedures/LOL_V1.1_VALIDATION_PROTOCOL_2026-08-29.md`.

ML and Duration sample counts are tracked separately. A material change to one family does not automatically authorize changing the other.

---

# 12. Durable-fix verification

An analytical/governance change is canonical only after:

1. relevant GitHub files are written;
2. fetched back and verified;
3. `CURRENT_MODEL.md` activates them;
4. a fresh Session Authority Lock points to the authority commit containing the complete stack.

Until then:

`MODEL REBUILD IN PROGRESS — HOLD`
