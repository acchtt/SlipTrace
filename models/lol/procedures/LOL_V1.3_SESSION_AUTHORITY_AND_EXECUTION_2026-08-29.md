# LoL v1.3 Session Authority & Execution Governance — 2026-08-29

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Model:** LoL v1.3 — Hierarchy Moneyline + Duration Core

## 1. Purpose

Run the compact Moneyline + Duration architecture with light persistent team strength, meaningful draft correction and live-state dominance.

---

## 2. Frozen authority

Every live v1.3 epoch requires an ACTIVE Session Authority Lock in `models/lol/session/CURRENT_SESSION_LOCK.md` that points to the authority commit containing the complete v1.3 stack.

Mismatch -> `MODEL LOCK MISMATCH — HOLD`.

Until complete activation -> `MODEL REBUILD IN PROGRESS — HOLD`.

---

## 3. Active families

- Moneyline ACTIVE
- Duration ACTIVE
- Kill Handicap RETIRED_FROM_BETTING
- Total Kills RETIRED_FROM_BETTING

---

## 4. Moneyline interlock

Resolve before TAKE CANDIDATE:

`ML_CORE[K=...;P0=...;D=...;MC=...;R=...;X=...;O=...;T=...;S=...;P=...;BOOK=...;EDGE=...;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`

Requirements:

- `K/P0` frozen from pre-series non-price evidence;
- `P0=50%+5*K pp`;
- `S=1.5D_eff+1.5R+1.5X+1.25O+T`;
- probability locked before price evidence;
- synchronized executable live ML;
- odds >=1.60;
- edge >=+5.0pp;
- position-blind;
- actual exposure 0u.

---

## 5. Duration interlock

Use unchanged v1.1 Duration Core:

`DUR_CORE[t=...;V=...;Q=...;H=...;T=...;R0=...;ER=...;F=...;LINE=...;P_SIDE=...;BOOK=...;EDGE=...;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`

Requirements remain odds >=1.60 and edge >=+7.5pp, with F locked before line/price evidence.

---

## 6. State change / price movement

Material state change expires pending candidate.

ML: retain frozen K/P0, rebuild D_eff/R/X/O/T as needed.

Duration: rebuild V/Q/H/T/F.

Price-only movement with unchanged state may reuse locked ML probability or Duration F; changed Duration line requires new side probability.

---

## 7. User confirmation

`USER_LINE_CONFIRMATION=PENDING / CONFIRMED / FAILED`

No accepted Position without timely exact confirmation.

No retroactive accepted Position creation.

---

## 8. Stake / anti-chase

- default shadow stake 0.25u unless lock changes it;
- actual exposure 0u;
- no martingale/rescue/chasing/averaging down/stake escalation;
- no position-driven probability adjustment;
- ML and Duration qualify independently.

---

## 9. Airtable truthfulness

Airtable is canonical map/snapshot/position ledger only. Accepted Positions preserve exact market, odds/line, entry clock, generation, compact record, shadow stake and actual exposure.

Never claim a write succeeded unless connector mutation succeeded.

---

## 10. Circuit breaker

Suspend TAKE CANDIDATE issuance for authority mismatch, actual-exposure violation, Position without timely confirmation, retired-market Position, price contamination of K/probability, stale candidate reuse, or sync/executability failure causing a false accepted entry.

Visible: `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`.

Ordinary model loss is not a breaker.

---

## 11. Durable activation

Canonical only after:

1. relevant GitHub files written;
2. fetched/verified;
3. `CURRENT_MODEL.md` activates v1.3;
4. fresh Session Authority Lock points to the activation commit.
