# Football v0.2.54 — Selection Inversion Guard + Promotion Quarantine

**Status:** ACTIVE OFFICIAL PATCH  
**Base:** Football v0.2.47 CLEAN  
**Depends on:** v0.2.49, v0.2.50, v0.2.51, v0.2.52 and v0.2.53  
**Effective:** 2026-09-13 ICT onward  
**Purpose:** preserve structural ranking through execution, separate price/burden waiting states from structural rejection, and quarantine promotion mechanisms that failed the settled audit.

This patch is prospective. It does not rewrite frozen PRE states, historical verdicts, official exposure, or settled P/L.

---

## 1. Audit basis

The settled audit contained 53 official bets for -5.505u (-10.4% ROI). The most recent completed v0.2.52 block returned -6.23u from 10 bets. Within the audited data:

- prematch v0.2.52 entries returned -4.23u from seven bets;
- live/decay v0.2.52 entries returned -2.00u from three bets;
- MCE/+0.25 entries returned -1.73u from four bets;
- a representative five-match qualified-HOLD counterfactual returned +2.29u while five comparable selected LOCKs returned -2.73u.

These are diagnostic samples, not retrospective reclassification. They establish enough repeated evidence to stop automatic promotion while preserving the underlying structural candidates for prospective measurement.

---

## 2. Two-axis decision state

Every final reviewed candidate must retain two separate outputs:

1. **Structural Rank** — football quality relative to the same practical kickoff window.
2. **Execution Class** — whether the presently offered state is directly executable.

Price, market movement, line availability, or elapsed match time may change Execution Class. They must not increase Structural Rank.

Required execution classes:

### DIRECT LOCK ELIGIBLE

Use only when:

- every active structural/XI/failure-mode gate clears;
- the actual line is no higher than the model-supported structural burden;
- the current prematch price clears the active price floor;
- the decision does not depend on a quarantined mechanism.

Eligibility is not an automatic LOCK. Same-window relative ranking and exposure discipline still apply.

### QUALIFIED — WAIT FOR DECAY

Use when the football thesis remains qualified at a recorded supported burden, but the current offer is unattractive because:

- the available line is above the supported burden; or
- the supported line is offered below the executable price floor.

Record the exact target line and minimum acceptable price. Keep the candidate in the active structural ranking/watch list. Do not collapse it into an ordinary HOLD.

### STRUCTURAL HOLD

Use when football structure fails or remains materially unresolved: route proof, chance quality, dominant failure mode, burden fit, league regime, XI integrity, or evidence confidence.

Price improvement or clock decay cannot promote this state.

### SHADOW ONLY

Use for a mechanism that is currently quarantined. Preserve its hypothetical line, odds, time, evidence epoch and settlement, but create no official exposure or official P/L.

---

## 3. Structural-rank preservation

The frozen Work rank is the starting rank. At the final prematch review:

- new football evidence may downgrade it;
- a genuine documented football change, such as a strict carrier reopen, may upgrade it;
- price and market evidence may validate execution or trigger reinspection, but cannot add structural rank points;
- a higher available total cannot be treated as evidence that the higher burden is better;
- a candidate classified QUALIFIED — WAIT FOR DECAY retains its structural position.

For every same-window comparison, display or persist:

- structural rank position;
- route pair;
- chance-quality state;
- CC+ state;
- dominant failure mode;
- supported burden;
- execution class;
- reason any lower-ranked candidate received official exposure ahead of it.

If a lower structural candidate is exposed while a higher one is directly executable, require a documented football reason. Price alone is not sufficient.

---

## 4. Promotion quarantine

### 4.1 MCE +0.25

MCE validation remains useful as a shadow diagnostic, but MCE/+0.25 cannot create an official LOCK under v0.2.54.

When all legacy MCE fields clear, record:

`SHADOW MCE +0.25 — NO OFFICIAL EXPOSURE`

The official decision must instead use:

- the supported STANDARD/EGE burden if directly available; or
- `QUALIFIED — WAIT FOR DECAY` at the recorded target burden/price.

A bullish line move remains contextual corroboration. It cannot justify accepting an extra quarter-goal burden.

### 4.2 Live and relative-decay Over entry

All new live/decay Over entries are shadow-only under v0.2.54, even when synchronized chance-quality evidence is available.

Use:

`SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`

If chance-quality evidence is missing or stale, retain:

`LIVE CHANCE QUALITY UNAVAILABLE — HOLD`

This quarantine includes STANDARD DECAY and EGE RELATIVE DECAY. It does not prohibit a direct prematch STANDARD or structurally supported direct prematch EGE selection.

### 4.3 Carrier reopen

A strict football-led `CARRIER REOPEN — XI CONFIRMED` may remain official-eligible only when it occurs prematch and the proposed line does not exceed the independently supported burden. Market movement or price improvement alone cannot trigger it.

---

## 5. Promotion cannot displace structure

Quarantined MCE/live candidates stay visible for audit but are removed from the official exposure pool.

The official exposure pool is ranked only from DIRECT LOCK ELIGIBLE candidates. QUALIFIED — WAIT FOR DECAY candidates stay on the active watch list at their structural rank but carry no exposure.

A candidate may not move ahead because:

- its odds are higher;
- its total moved up;
- the same line became cheaper after elapsed minutes;
- a protected Asian quarter line appears attractive;
- another structurally stronger candidate is temporarily unavailable at the target price.

This creates separate structural and execution boards instead of one mixed verdict order.

---

## 6. Burden integrity

The supported burden is selected before current price.

If the market offers only a higher line:

- do not stretch;
- do not invoke MCE for official exposure;
- record the candidate as QUALIFIED — WAIT FOR DECAY at the last supported burden.

Protection is settlement geometry, not positive football evidence. O2.25/O2.75 protection may reduce loss severity but cannot repair a weak route or promote STRUCTURAL HOLD.

---

## 7. Prospective measurement

For every completed FOCUS/WATCHLIST candidate, retain the final score and evaluate:

- whether the frozen structural threshold was reached;
- official result/P&L when exposed;
- hypothetical result at the recorded qualified target burden when not exposed;
- MCE shadow result at the actual higher line/price;
- live/decay shadow result at its synchronized evidence epoch;
- structural rank position and execution class.

Counterfactual and shadow outcomes remain excluded from official P/L.

Report separately:

- official DIRECT results;
- QUALIFIED — WAIT FOR DECAY target-burden outcomes;
- STRUCTURAL HOLD outcomes;
- MCE shadow outcomes;
- live/decay shadow outcomes;
- FOCUS vs WATCHLIST threshold performance.

Do not group all HOLD states together.

---

## 8. Quarantine release gate

MCE and live/decay are evaluated separately. Neither mechanism may return to official eligibility unless all are true:

1. at least 20 valid settled shadow observations for that mechanism;
2. every observation had contemporaneous required evidence and a recorded predeclared target;
3. quarter-line-aware shadow ROI is positive;
4. the mechanism does not underperform the supported frozen-burden alternative on the recorded comparison;
5. performance is not concentrated in one league, one carrier, or one short run;
6. two consecutive post-slate audits recommend release;
7. the user explicitly approves a later model version that removes the quarantine.

No mechanism reactivates automatically from one winning slate.

---

## 9. Audit labels

Use prospectively:

- `SELECTION INVERSION`
- `STRUCTURAL RANK PRESERVED`
- `QUALIFIED PRICE/BURDEN HOLD`
- `STRUCTURAL HOLD CORRECT`
- `LOWER-RANK EXPOSURE EXCEPTION`
- `PROMOTION QUARANTINE PASS`
- `PROMOTION QUARANTINE BREACH`
- `MCE SHADOW OUTPERFORMED/UNDERPERFORMED`
- `LIVE-DECAY SHADOW OUTPERFORMED/UNDERPERFORMED`

---

## 10. Authority

v0.2.54 overrides subordinate wording that:

- collapses structural and price/burden HOLDs into one state;
- permits MCE/+0.25 to create official exposure;
- permits any new live/decay Over to create official exposure;
- lets price, line movement, or elapsed time increase structural rank;
- removes qualified price/burden holds from active comparison;
- evaluates only official LOCKs while discarding qualified-HOLD outcomes.

All unchanged v0.2.47/v0.2.49/v0.2.50/v0.2.51/v0.2.52/v0.2.53 rules remain active.
