# LoL v1.3 Session Authority & Execution Governance — 2026-08-29

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Model:** LoL v1.3 — Hierarchy Moneyline + Duration Core

## 1. Purpose

Run the compact Moneyline + Duration architecture with reproducible league-relative team benchmarking, meaningful draft correction and live-state dominance.

---

## 2. Frozen authority

Every live v1.3 epoch requires an ACTIVE Session Authority Lock in `models/lol/session/CURRENT_SESSION_LOCK.md` that points to the authority commit containing the complete v1.3 stack, including the active team benchmark procedure.

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

Before the first model-certified ML verdict of a series, resolve and preserve:

`TEAM_BENCH[LEAGUE=...;CURRENT=...;PREVIOUS=...;G=...;B_CUR_A=...;B_CUR_B=...;B_PREV_A=...;B_PREV_B=...;BLEND_A=...;BLEND_B=...;B_A=...;B_B=...;GAP=...;K_A=...;K_B=...;ROSTER_ADJ=...;PRICE_USED=N]`

Benchmark authority:
`models/lol/procedures/LOL_V1.3_TEAM_BENCHMARK_GOLGG_2026-08-30.md`

Then before TAKE CANDIDATE resolve:

`ML_CORE[K=...;P0=...;D=...;MC=...;R=...;X=...;O=...;T=...;C=...;S=...;P=...;BOOK=...;EDGE=...;THESIS=P;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`

Requirements:

- `K/P0` frozen from the pre-series Gol.gg league-relative benchmark;
- sportsbook price and same-series results excluded from benchmark construction;
- benchmark peer set/source/sample/roster continuity sufficiently resolved;
- `P0=50%+5*K pp`;
- `C=1.5D_eff+1.5R+1.5X+1.25O+T`;
- `S=C`;
- probability locked before price evidence;
- selected-side causal thesis `C>0`;
- coherent, currently reachable draft/live win mechanism for selected side;
- team-strength prior alone cannot satisfy thesis gate;
- synchronized executable live ML;
- odds >=1.60;
- edge >=+5.0pp;
- position-blind;
- actual exposure 0u.

**Price cannot create the bet.** If selected-side `C<=0`, verdict is `PASS` even when numerical edge clears +5.0pp. A long price is never a substitute for positive draft/live causality.

If benchmark certification is incomplete, ML status is `HOLD` rather than subjective K substitution.

---

## 5. Duration interlock

Use unchanged v1.1 Duration Core:

`DUR_CORE[t=...;V=...;Q=...;H=...;T=...;R0=...;ER=...;F=...;LINE=...;P_SIDE=...;BOOK=...;EDGE=...;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`

Requirements remain odds >=1.60 and edge >=+7.5pp, with F locked before line/price evidence.

---

## 6. State change / price movement

Material state change expires pending candidate.

ML: retain frozen benchmark-derived K/P0, rebuild D_eff/R/X/O/T and causal thesis as needed.

Duration: rebuild V/Q/H/T/F.

Price-only movement with unchanged state may reuse locked ML probability/thesis or Duration F; changed Duration line requires new side probability.

Same-series map results do not update `K`.

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

Suspend TAKE CANDIDATE issuance for authority mismatch, actual-exposure violation, Position without timely confirmation, retired-market Position, sportsbook contamination of benchmark/K/probability, subjective K substitution when benchmark certification is required, price-only candidate issuance without positive causal thesis, stale candidate reuse, or sync/executability failure causing a false accepted entry.

Visible: `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`.

Ordinary model loss is not a breaker.

---

## 11. Durable activation

Canonical only after:

1. relevant GitHub files written;
2. fetched/verified;
3. `CURRENT_MODEL.md` activates the benchmark-aware v1.3 stack;
4. fresh Session Authority Lock points to the activation commit.
