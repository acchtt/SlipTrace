# Football v0.2.55 — Execution Calibration Addendum

**Status:** ACTIVE OFFICIAL PATCH  
**Base:** Football v0.2.54  
**Effective:** 2026-09-14 ICT onward  
**Purpose:** correct execution-layer selection inversion without changing the structural ranking model.

This patch is prospective. It does not rewrite frozen PRE states, historical verdicts, official exposure, or settled P/L.

---

## 1. Scope lock — structural model unchanged

v0.2.55 changes only the execution/audit items stated below.

The following remain exactly as defined by v0.2.54 and its active dependencies:

- Structural Rank construction and same-window ordering;
- A1 / A2 / B+ grading standards;
- FOCUS / WATCHLIST assignment;
- route-pair and chance-quality requirements;
- supported-burden construction;
- league/regime exclusions and evidence-depth caps;
- XI integrity gates and failure-mode logic;
- active prematch price floors;
- DIRECT LOCK ELIGIBLE requirements;
- live/decay quarantine;
- strict carrier reopen requirements;
- official exposure discipline and official P/L accounting.

No structural rank, supported burden, league filter, B+ gate, or official price floor is loosened by this patch.

---

## 2. Price-only WAIT enforcement

When all active football, XI, evidence-confidence and failure-mode gates clear at the recorded supported burden, and the only blocker is either:

- the currently available line is above the supported burden; or
- the supported line is priced below the active executable price floor,

then the execution class **must** be:

`QUALIFIED — WAIT FOR DECAY`

It must not be recorded as STRUCTURAL HOLD.

Persist the blocker explicitly as one of:

- `PRICE-ONLY WAIT — LINE ABOVE BURDEN`
- `PRICE-ONLY WAIT — PRICE BELOW FLOOR`
- `PRICE-ONLY WAIT — BOTH`

STRUCTURAL HOLD remains reserved for unresolved or failed football structure exactly as defined in v0.2.54.

---

## 3. A1/A2 FOCUS +0.25 acceptance-band shadow

For a candidate that is already structurally qualified and satisfies **all** of the following:

1. Structural Rank is A1 or A2;
2. board status is FOCUS;
3. confirmed XI is clean enough to preserve the frozen thesis;
4. the supported burden remains valid and unchanged;
5. the lowest available prematch line is exactly **+0.25** above the supported-burden ceiling;
6. the offered +0.25 line price clears the existing active prematch price floor;
7. the observation is frozen before kickoff;

record an additional prospective shadow state:

`HIGH-SCORING +0.25 ACCEPTANCE BAND — SHADOW ONLY`

This shadow is recorded **in addition to**, not instead of, the official `QUALIFIED — WAIT FOR DECAY` state.

Required shadow fields:

- supported burden;
- +0.25 shadow line;
- shadow price;
- timestamp/evidence epoch;
- confirmed-XI state;
- structural rank and board status;
- final settlement and quarter-line-aware shadow P/L.

The +0.25 acceptance-band shadow **cannot create official exposure under v0.2.55**.

A line that is +0.50 or more above the supported-burden ceiling does not qualify for this automatic +0.25 lane. Existing v0.2.54 quarantine rules continue to apply.

---

## 4. Required market-path logging for qualified waits

For every `QUALIFIED — WAIT FOR DECAY` candidate, persist the following market path whenever observable:

- frozen supported burden;
- target minimum acceptable price;
- first offered prematch total and price seen at review;
- lowest prematch total observed before kickoff;
- best prematch price observed at the supported target line;
- whether the supported target line was ever actually obtainable before kickoff;
- timestamp when the supported target first became obtainable, if it did;
- +0.25 acceptance-band line/price/timestamp when Section 3 applies;
- first-goal time when a goal arrives before the target becomes executable;
- final score.

Audit label the execution outcome as one of:

- `TARGET OBTAINABLE — NOT TAKEN`
- `TARGET NEVER OBTAINABLE PRE-KICK`
- `FIRST GOAL BEFORE TARGET`
- `ACCEPTANCE-BAND SHADOW AVAILABLE`
- `NO ACCEPTANCE-BAND OFFER`

This logging is diagnostic only and does not change the frozen Structural Rank or supported burden.

---

## 5. B+ / CC+ remains a separate audit lane

The A1/A2 FOCUS +0.25 acceptance band in Section 3 does **not** automatically extend to B+ candidates.

B+ remains governed by the existing structural and positive-gate rules. Do not use one winning slate, attractive price, or a +0.25 market line to promote B+ into the A1/A2 acceptance lane.

When a B+ candidate has a genuine carrier/CC+ case but remains non-executable, record it separately as:

`B+ CC+ AUDIT LANE — NO AUTOMATIC PROMOTION`

Retain:

- supported burden;
- carrier ceiling evidence;
- secondary-route state;
- XI state;
- actual market line/price;
- final score;
- hypothetical supported-burden outcome.

The strict prematch `CARRIER REOPEN — XI CONFIRMED` rule from v0.2.54 remains unchanged and may still be official-eligible only under its existing requirements.

---

## 6. Acceptance-band quarantine and release gate

The high-scoring +0.25 acceptance band is a distinct shadow mechanism and remains quarantined.

It may not become official-eligible unless all are true:

1. at least **20 valid settled +0.25 acceptance-band shadow observations**;
2. every observation was predeclared before kickoff with contemporaneous XI and market evidence;
3. quarter-line-aware shadow ROI is positive;
4. the mechanism does not underperform the supported frozen-burden alternative on the recorded comparison;
5. performance is not concentrated in one league, one carrier, or one short run;
6. two consecutive post-slate audits recommend release;
7. the user explicitly approves a later model version that removes this quarantine.

Valid pre-kick +0.25 shadows already frozen prospectively under v0.2.54 may count toward this sample if they satisfy the same evidence requirements.

No automatic release is permitted.

---

## 7. Audit reporting change

Post-slate reporting must continue to separate:

- official DIRECT results;
- QUALIFIED — WAIT FOR DECAY target-burden outcomes;
- STRUCTURAL HOLD outcomes;
- A1/A2 FOCUS +0.25 acceptance-band shadow outcomes;
- B+ CC+ audit-lane outcomes;
- MCE shadow outcomes outside the new acceptance band;
- live/decay shadow outcomes;
- FOCUS vs WATCHLIST threshold performance.

Do not merge the A1/A2 +0.25 acceptance-band sample with B+ carrier audits or with official P/L.

---

## 8. Authority

v0.2.55 overrides v0.2.54 only where necessary to:

- force structurally qualified price/burden blocks into `QUALIFIED — WAIT FOR DECAY` rather than STRUCTURAL HOLD;
- automatically freeze a separate +0.25 shadow observation for clean-XI A1/A2 FOCUS candidates meeting Section 3;
- require the market-path logging in Section 4;
- keep B+ / CC+ calibration in a separate audit lane;
- apply the 20-observation release gate specifically to the new +0.25 acceptance-band mechanism.

All other v0.2.54 and earlier active rules remain unchanged.
