# Football Model A — Execution Selection Correction

**Status:** ACTIVE OFFICIAL PATCH  
**Model version:** **Football A**  
**Base:** Football v0.2.55  
**Effective:** 2026-09-15 11:01 ICT onward  
**Purpose:** correct repeated execution-selection inversion by separating technical execution eligibility from final official exposure selection.

This patch is prospective. It does not rewrite frozen PRE states, historical verdicts, settled P/L, or prior shadow/counterfactual outcomes.

---

## 1. Scope lock — structural model unchanged

Model A does **not** rebuild the structural model.

The following remain governed by v0.2.55 and its active dependencies:

- fixture/scope and league-regime rules;
- A1 / A2 / B+ structural grading;
- FOCUS / WATCHLIST assignment;
- home/away route proof;
- chance-quality requirements;
- CC+ / carrier-ceiling proof;
- dominant failure-mode logic;
- supported-burden construction;
- confirmed-XI integrity and carrier reopen rules;
- active price floors;
- MCE, +0.25 acceptance-band, and live/decay quarantines;
- official settlement and P/L accounting.

Model A changes **which technically executable candidates are allowed to become official exposure**.

---

## 2. Three separate outputs are now mandatory

Every material final review must preserve three distinct outputs:

1. **Structural Rank** — football quality within the practical same-window board.
2. **Execution Class** — whether the current line/price is technically executable.
3. **Exposure Decision** — whether Model A actually permits an official bet.

Execution Class remains one of:

- `DIRECT LOCK ELIGIBLE`;
- `QUALIFIED — WAIT FOR DECAY`;
- `STRUCTURAL HOLD`;
- `SHADOW ONLY`.

**Critical Model A rule:**

`DIRECT LOCK ELIGIBLE != AUTOMATIC OFFICIAL LOCK`

A technically executable candidate must also clear the Model A exposure gate below.

When a DIRECT candidate fails the new exposure gate, preserve its Execution Class as `DIRECT LOCK ELIGIBLE` but set final action to:

`NO BET — EXPOSURE HOLD`

and persist the exact blocker.

---

## 3. Model A official exposure gate

An `OFFICIAL LOCK` requires all legacy DIRECT LOCK ELIGIBLE requirements **plus** Model A exposure approval.

Exposure approval is evaluated in this order:

`STRUCTURAL RANK → UPPER-TAIL PROOF → PRIORITY-INVERSION GUARD → BURDEN PROTECTION → PRICE AS TIE-BREAKER`

Price and simple market accessibility are not allowed to become the primary selector.

### 3.1 A2 upper-tail requirement at the supported ceiling

For an **A2** candidate where the current executable line is at the **top of the supported-burden range / supported ceiling**, official exposure requires a genuine upper-tail pass.

At least one of the following must be present from pre-kick evidence:

- **4+ TOTAL PATH — QUALITY PROVEN:** repeatable high-value chance creation across the two routes, with credible evidence that the match can continue beyond merely reaching three goals;
- **TRUE CC+ PATH:** one team has a genuine independent 3+ team-goal ceiling and the opponent route/defensive vulnerability gives a credible path to the additional goal(s);
- **ELITE TWO-SIDED PATH:** the route pair is materially stronger than ordinary A2, with strong chance quality and failure resistance such that the upper tail is not dependent on a late low-probability event.

If none clears:

`DIRECT LOCK ELIGIBLE — NO BET — EXPOSURE HOLD — UPPER-TAIL INSUFFICIENT`

This rule is designed specifically to stop an ordinary lower-ceiling A2 from becoming official merely because O2.5/O2.75 is available inside its technical burden.

### 3.2 Protected line below the ceiling

If an A1/A2 candidate is executable **below** its supported ceiling, the protection is a legitimate execution advantage, but protection still does not create football quality.

The candidate may pass the exposure gate when:

- the structural thesis remains intact;
- no material same-window priority inversion exists under Section 4;
- the protected burden is meaningfully below the supported ceiling;
- no quarantined mechanism is required.

### 3.3 A1 treatment

A1 remains the strongest primary lane because it requires PROVEN + PROVEN. A clean-XI A1 that is directly executable at a supported burden normally clears the upper-tail exposure requirement unless a named compression/failure branch, chance-quality downgrade, or burden-specific rule says otherwise.

EGE/high-burden rules still apply independently.

### 3.4 B+ treatment

Model A does **not** relax B+.

B+ still requires all legacy positive gates, compression hardening, and CC+ rules. B+ does not gain access to the A1/A2 +0.25 acceptance mechanism and receives no promotion merely because its lower line is easier to execute.

---

## 4. Priority-inversion guard

Before issuing any official exposure, compare the candidate against higher-ranked active candidates in the same practical kickoff/exposure window.

If a higher-ranked **clean-XI A1/A2 FOCUS** candidate is still structurally qualified and is withheld **only** because:

- its available line is above supported burden; or
- its supported line price is below the active floor,

then a materially weaker lower-ranked candidate must **not** become official merely because its O2.5/O2.75 line happens to be available.

The lower-ranked candidate may still be exposed only when there is a documented football-led reason that defeats the inversion concern, such as:

- clearly stronger upper-tail evidence at the actual offered burden;
- materially better route quality after confirmed XI;
- a genuine failure-mode downgrade to the higher-ranked match;
- a strict carrier/football change recognized by the active model.

Price, lower nominal total, or simple availability is **not** a valid override.

If no football-led override exists, preserve:

- Execution Class: `DIRECT LOCK ELIGIBLE`;
- Final Action: `NO BET — EXPOSURE HOLD`;
- Blocker: `PRIORITY INVERSION GUARD`.

Required audit label:

`DIRECT-ELIGIBLE EXPOSURE SUPPRESSED — PRIORITY INVERSION`

---

## 5. Qualified waits remain active high-priority candidates

Model A keeps the v0.2.55 distinction intact.

Use `QUALIFIED — WAIT FOR DECAY` when football/XI/evidence gates clear at a supported burden and the only blocker is line or price.

Do not downgrade a high-ranked qualified wait to structural hold simply because an easier lower-ranked bet exists.

Continue mandatory market-path logging:

- supported target burden;
- target minimum price;
- first observed line/price;
- lowest pre-kick line;
- best target-line price;
- whether/when target became executable;
- first-goal-before-target state where relevant;
- final score.

No retroactive official exposure is created from a successful target outcome.

---

## 6. +0.25 acceptance band remains quarantined

The v0.2.55 A1/A2 FOCUS +0.25 acceptance-band mechanism remains:

`HIGH-SCORING +0.25 ACCEPTANCE BAND — SHADOW ONLY`

It does **not** become official under Model A.

The existing release gate remains unchanged, including:

- at least 20 valid settled predeclared observations;
- positive quarter-line-aware ROI;
- no underperformance versus the supported-burden alternative;
- diversified sample;
- two consecutive release audits;
- explicit user approval of a later model version.

No automatic release.

---

## 7. MCE and live/decay quarantine unchanged

Model A does not reactivate MCE/+0.25 or ordinary live/relative-decay official exposure.

Continue:

- `SHADOW MCE +0.25 — NO OFFICIAL EXPOSURE`;
- `SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`.

A user-granted match-specific prematch-equivalent exception remains explicit and does not generalize to other fixtures.

---

## 8. Official exposure ordering

When multiple DIRECT candidates exist, official exposure priority is now:

1. structural rank / tier quality;
2. upper-tail proof at the actual burden;
3. route quality and failure resistance after XI;
4. burden protection relative to independently supported ceiling;
5. price only as a tie-breaker among otherwise comparable candidates.

Do not reverse this order because one candidate offers a superficially easier O2.5/O2.75 line.

The objective is to avoid repeatedly selecting the most market-accessible candidate instead of the best scoring environment.

---

## 9. Persistence rules

For every Model A final review, persist:

- `Model Version = Football A`;
- Structural Rank;
- Execution Class;
- supported burden;
- actual line/price;
- upper-tail state: `PASS / FAIL / NOT REQUIRED`;
- priority-inversion state: `CLEAR / BLOCKED / FOOTBALL OVERRIDE`;
- final Exposure Decision;
- exact reason for any DIRECT-eligible exposure hold.

Existing Airtable fields may be used without schema migration:

- keep `Execution Class = DIRECT LOCK ELIGIBLE` when technically true;
- use `Verdict = NO BET — HOLD` for `NO BET — EXPOSURE HOLD`;
- put `UPPER-TAIL INSUFFICIENT` or `PRIORITY INVERSION GUARD` in Candidate/Evidence Summary;
- create Website Picks only for actual `OFFICIAL LOCK` exposure.

Do not relabel a technically direct candidate as STRUCTURAL HOLD merely because Model A suppresses exposure.

---

## 10. Model A audit separation

Post-slate audit must report separately:

- official Model A LOCK results and P/L;
- `DIRECT LOCK ELIGIBLE` candidates suppressed by the upper-tail gate;
- `DIRECT LOCK ELIGIBLE` candidates suppressed by the priority-inversion guard;
- QUALIFIED — WAIT target-burden outcomes;
- STRUCTURAL HOLD outcomes;
- +0.25 acceptance-band shadows;
- B+ / CC+ audit lane;
- MCE shadows;
- live/decay shadows;
- FOCUS vs WATCHLIST threshold and 4+ upper-tail performance.

The primary Model A diagnostic is whether the new exposure gate improves **official selection quality** without degrading the structural board.

Do not outcome-fit isolated winners. Review the gate prospectively over a meaningful settled sample.

---

## 11. Authority

Model A overrides v0.2.55/v0.2.54 only where necessary to:

- separate DIRECT eligibility from official exposure permission;
- require upper-tail proof for A2 exposure at the supported ceiling;
- block materially weaker lower-ranked exposure when a higher-ranked A1/A2 FOCUS is withheld only by line/price, absent a football-led override;
- rank exposure by structural quality and upper-tail proof before burden convenience and price;
- create the `NO BET — EXPOSURE HOLD` state without corrupting the underlying Execution Class.

All other v0.2.55 and earlier active rules remain in force.
