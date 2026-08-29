# LoL v1.2 Session Authority & Execution Governance — 2026-08-29

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Model:** LoL v1.2 — Strength-Prior Moneyline + Duration Core

## 1. Purpose

Run the compact Moneyline + Duration architecture after repairing the missing Moneyline team-strength prior, without reviving v0.x gate trees.

---

# 2. Frozen authority

Every live v1.2 epoch requires an ACTIVE Session Authority Lock in:

`models/lol/session/CURRENT_SESSION_LOCK.md`

The lock must record authority commit, active model, families, thresholds, minimum odds, circuit breaker, stake/exposure, sample state and series scope.

When ACTIVE, analytical/procedural files must be loaded from its authority commit.

Mismatch -> `MODEL LOCK MISMATCH — HOLD`.

---

# 3. Active families

- Moneyline = ACTIVE
- Duration = ACTIVE
- Kill Handicap = RETIRED_FROM_BETTING
- Total Kills = RETIRED_FROM_BETTING

Historical v0.x/v1.0/v1.1 material remains audit/research authority only unless explicitly referenced for transition review.

---

# 4. Moneyline interlock

Before TAKE CANDIDATE resolve:

`ML_CORE[K=...;P0=...;D=...;MC=...;R=...;X=...;O=...;T=...;S=...;P=...;BOOK=...;EDGE=...;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`

Requirements:

- series-frozen `K/P0` established from pre-series non-price evidence;
- synchronized executable live ML;
- probability locked before price evidence;
- odds `>=1.60`;
- edge `>=+5.0pp`;
- position-blind;
- actual exposure `0u`.

Price may never determine or modify `K`.

---

# 5. Duration interlock

Use the unchanged v1.1 Duration Core:

`DUR_CORE[t=...;V=...;Q=...;H=...;T=...;R0=...;ER=...;F=...;LINE=...;P_SIDE=...;BOOK=...;EDGE=...;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`

Requirements remain:

- synchronized executable Duration market;
- `F` locked before line/odds as analytical evidence;
- clear settlement semantics;
- odds `>=1.60`;
- selected edge `>=+7.5pp`;
- position-blind;
- actual exposure `0u`.

---

# 6. State-change expiry and price movement

A TAKE CANDIDATE belongs to one decision window and expires on a material live event before confirmation.

ML material state change -> rebuild `R/X/O/T`/mechanism while retaining series-frozen `K/P0`.

Duration material state change -> rebuild `V/Q/H/T` and `F`.

Price-only movement:

- ML: retain locked probability if state unchanged and reprice;
- Duration: retain `F` if state unchanged, recalculate probability if line changes, then reprice.

---

# 7. User line confirmation

`USER_LINE_CONFIRMATION = PENDING / CONFIRMED / FAILED`

PENDING -> no Position/WL/PL.

CONFIRMED -> exact quoted active-family market still exists before material state change.

FAILED -> no accepted Position.

No retroactive accepted Position creation.

---

# 8. Stake / anti-chase controls

- default shadow stake `0.25u`;
- actual exposure `0u`;
- no martingale, rescue, chasing, averaging down or stake escalation;
- no position-driven probability adjustment;
- ML and Duration qualify independently.

---

# 9. Airtable truthfulness

Airtable is canonical ledger/history authority only.

For v1.2 accepted Positions preserve exact market, odds/line, entry clock, model generation, 0.25u shadow stake, 0u exposure and compact family record.

Unconfirmed candidates may be snapshots but not accepted validation Positions.

Retroactive user-designated ledger entries remain clearly outside validation.

Never claim a write succeeded unless connector mutation succeeded.

---

# 10. Circuit breaker

Suspend new TAKE CANDIDATE issuance for material governance failures including:

- authority/model mismatch;
- actual-exposure violation;
- Position without timely exact confirmation;
- retired KH/TK Position;
- price used to choose/modify `K` or model probability;
- stale candidate reused after state change;
- sync/executability failure causing false accepted entry.

Visible status:

`TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`

Ordinary model loss or upset is not a breaker.

---

# 11. Validation

Use:

`models/lol/procedures/LOL_V1.2_VALIDATION_PROTOCOL_2026-08-29.md`

ML and Duration counts remain family-separated.

---

# 12. Durable activation

A change is canonical only after:

1. all relevant GitHub files are written;
2. fetched back and verified;
3. `CURRENT_MODEL.md` activates the stack;
4. a fresh Session Authority Lock points to the activation authority commit.

Until complete:

`MODEL REBUILD IN PROGRESS — HOLD`
