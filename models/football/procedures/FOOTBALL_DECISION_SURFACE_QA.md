# Football Decision-Surface QA Procedure

**Status:** ACTIVE QA CONTROL  
**Purpose:** prevent operational QA from missing any input, rule, threshold, state transition, or persistence effect that can change a football verdict.  
**Applies to:** Step 1 PRE, Step 2 XI+odds, live execution, persistence, and post-slate workflow audits.  
**Model effect:** none. This is a process-compliance QA framework.

This procedure complements `FOOTBALL_MODEL_QA_AND_PROMOTION.md`. It does not alter predictive thresholds. It determines whether the current production stack is internally complete, deterministic, and faithfully executable.

---

## 1. QA completion rule

A production-stage QA audit is **not complete** until it has:

1. enumerated every material decision input used by that stage;
2. traced every input from collection to interpretation to threshold/effect to persistence;
3. mapped precedence when more than one active file touches that input;
4. tested contradictory/edge branches;
5. identified stale active-looking text that can still steer execution;
6. produced a coverage matrix with no unclassified material input.

Required completion equation:

`MATERIAL DECISION INPUTS = FULLY TRACED + EXPLICITLY NON-MATERIAL`

with:

`UNTRACED MATERIAL INPUTS = 0`

If any verdict-changing input has no deterministic treatment, the audit result is:

`QA INCOMPLETE — DECISION SURFACE GAP`

Do not call an audit complete merely because no direct textual contradiction was found.

---

## 2. Mandatory decision-input inventory

For the audited stage, begin by listing all inputs that can affect any of:

- structural grade;
- board tier;
- structural rank;
- supported burden;
- current/post-XI burden;
- LOCK / WAIT / HOLD / PASS;
- live-plan survival;
- official publication;
- persistence/audit classification.

The inventory must include, when relevant:

### Identity / state
- AiScore fixture ID;
- competition;
- home/away identity;
- kickoff/status;
- score/minute / reset epoch;
- requested/slate time window.

### Frozen structural state
- PRE grade;
- board tier;
- route pair;
- second-route independence;
- practical carrier state;
- dominant failure mode + severity;
- supported burden/range;
- upper-tail state;
- evidence confidence;
- structural rank;
- complete compiled PRE trace when available.

### Current football evidence
- confirmed XI;
- formations / roles;
- creators / finishers;
- attacking mechanism survival;
- defensive absences;
- bench / rotation / cohesion;
- current injuries/suspensions/illness;
- chance creation/concession;
- recent scoring/conceding;
- relevant home/away splits;
- tactical matchup;
- competition format/incentive;
- fatigue/schedule;
- weather/pitch only if an active rule permits it;
- H2H / matchup history.

### Market evidence
- opening total;
- PRE-XI total;
- post-XI/current total;
- current Asian handicap;
- current 1X2 favorite price;
- adjacent total board;
- current executable user price;
- market-center delta;
- MCL/MOS where carrier decomposition applies.

### Execution controls
- market alignment;
- frozen-PRE vs current-PRE distinction;
- B+ protected-line lane;
- carrier decomposition;
- current PRE / carrier band;
- HMA state where still relevant;
- decay-first target;
- decay gap / reachability;
- upper-tail gate;
- price floor;
- one-exposure-per-match;
- live state-integrity / no-chase rules;
- research-compliance gates.

### Persistence
- Decision State epoch;
- Website Pick epoch;
- line/odds/stake;
- timestamps;
- model version;
- duplicate prevention;
- frozen PRE immutability;
- result/P&L boundary.

The auditor must add any additional input discovered in the active stack. This list is a minimum, not a whitelist.

---

## 3. Decision-surface trace matrix

Every material input must have one row with all columns resolved:

| Field | Required content |
|---|---|
| Input | exact decision variable |
| Collection authority | where/how it is obtained |
| Evidence epoch | PRE / post-XI / prematch / live / historical |
| Freshness requirement | when stale data is invalid |
| Interpretation | allowed semantic meaning |
| Classification/threshold | exact state/threshold, if any |
| Allowed effect | what it may change |
| Forbidden effect | what it may never create/change |
| Precedence | later/compiled authority when files overlap |
| Missing-data behavior | UNKNOWN / HOLD / cap / continue |
| Persistence | where the state/evidence is stored |
| QA assertion | deterministic test that must pass |

A row is incomplete if any required column is absent for an input that can affect a verdict.

---

## 4. Stage-boundary audit

For each stage, explicitly test what information is **forbidden** from leaking backward.

Examples:

- Step 1 PRE: confirmed XI and current market price cannot create PRE structure/rank.
- Step 2: current market may trigger a football re-screen but cannot rewrite frozen PRE history.
- Live: new score/minute/market begins a new evidence epoch; it cannot backfill a missed historical exposure.
- Live provider telemetry (shots, xG/xGOT, big chances, dangerous attacks, possession, corners, box entries, momentum) is **non-authoritative** for current Football C/C2 execution. It is not required, and absence/quiet telemetry cannot create thesis decay.
- Audit: final result cannot be used as evidence that was supposedly known at the earlier decision epoch.

Any backward information leakage is a QA FAIL.

---

## 5. Precedence audit

Build an ordered map of all active files touching each decision surface.

For every overlap, answer:

1. which file is earlier;
2. which file is later;
3. whether the later file explicitly overrides the earlier one;
4. whether a prompt/procedure still repeats the superseded behavior;
5. whether the runtime can plausibly execute the stale wording before reaching the override.

If yes to #5, classify:

`ACTIVE-LOOKING STALE AUTHORITY — CONSISTENCY RISK`

Load-order precedence alone is not sufficient if production prompts/procedures still contain conflicting executable instructions.

---

## 6. Negative-space audit

Search for decision-changing language whose threshold is missing.

Examples:

- "recent";
- "strong";
- "material";
- "meaningful";
- "relevant";
- "clean";
- "preserved";
- "suppressed";
- "extreme";
- "elite";
- "comparable";
- "mechanism-compatible";
- "low urgency";
- "current form";
- "same-venue";
- "stronger failure-resistance".

For each such term, determine whether another active authority gives a deterministic operational definition.

If not, classify:

`UNDER-SPECIFIED DECISION THRESHOLD`

and identify the exact outputs it can change.

This gate is specifically intended to catch important inputs such as H2H that may be present everywhere yet never given a deterministic protocol.

---

## 7. H2H / matchup-history audit — mandatory when totals are assessed

H2H must always receive its own row in the decision-surface matrix whenever the active model can use it for burden, suppression, upper-tail, B+ veto, or O3.0+ execution.

Audit:

- same-venue H2H;
- recent all-venue H2H;
- long-run H2H;
- sample size;
- recency;
- manager/personnel/competition-class transferability;
- scoreline vs mechanism evidence;
- interaction with current tactical/chance evidence;
- exact burden/verdict effect;
- independent corroboration required for a HARD VETO.

QA must fail if H2H can change LOCK/WAIT/HOLD without deterministic recency/transferability/effect semantics.

---

## 8. Research-input completeness audit

For every mandatory research gate, distinguish:

- evidence **attempted**;
- evidence **found**;
- evidence **limited**;
- evidence **unavailable**;
- evidence **waived explicitly**.

Then map missing-data behavior.

A mandatory research attempt may be process-complete even when evidence is unavailable, but an unavailable input must not be silently replaced by inference.

Market-history research and football research remain separate decision surfaces.

---

## 9. Execution-state taxonomy audit

List every output state the stage can emit.

For Step 2 this normally includes:

- OFFICIAL LOCK;
- WAIT — LIVE DECAY;
- WAIT — PRICE BELOW FLOOR;
- STRUCTURAL HOLD;
- PASS;
- any active carrier-market/current-PRE subtype;
- any explicit B+ exact-burden subtype;
- provisional just-started verdict state if used.

For each state define:

- required preconditions;
- mutually exclusive blockers;
- whether it is final/provisional;
- whether it can be published;
- whether Website Picks should exist;
- what event terminates/replaces it.

If two active files permit different output states from the same complete input state, QA fails.

---

## 10. Deterministic replay suite

A production audit must include synthetic/replay branches covering at least:

1. exact supported burden, price clears;
2. exact supported burden, price below floor;
3. market +0.25 above burden;
4. market +0.50 or more above burden;
5. severe market undercut;
6. B+ exact protected burden;
7. B+ +0.25 carrier case;
8. ELITE/EXTREME carrier decomposition;
9. high total + weak frozen PRE;
10. intact XI vs damaged XI;
11. mandatory research unavailable after attempted search;
12. recent suppressive same-venue H2H with current corroboration;
13. suppressive H2H without current corroboration;
14. open H2H but current football suppression;
15. just-started time-sensitive quote;
16. score change before finalization;
17. persistence first-write succeeds / second-write fails;
18. duplicate official pick attempt.

For each branch, run the active authority order and record one expected canonical state.

If more than one legitimate outcome remains, the system is under-specified.

---

## 11. Stale-text and expired-override audit

Search current production prompts, procedures, persistence contracts, launchers and handoffs for:

- expired temporary overrides;
- superseded model-version declarations;
- removed execution states;
- removed priority/exposure gates;
- historical examples written as current instructions;
- shadow-only rules presented as official;
- hard-coded old board IDs or dates.

A stale historical document is acceptable only when clearly marked historical and loaded after current authority.

A stale production document that can steer execution is a QA finding.

---

## 12. Persistence-schema audit

For each material execution state, verify that persistence can represent:

- frozen PRE separately from current/post-XI state;
- current model version;
- evidence epoch;
- current burden vs frozen burden;
- market alignment;
- carrier/current-PRE state;
- H2H classification where material;
- research statuses;
- exact line/odds;
- final execution state;
- timestamps;
- publication state.

If the schema cannot distinguish two materially different states, classify:

`PERSISTENCE SEMANTIC COLLISION`

Do not solve semantic collision by overwriting frozen history.

---

## 13. Audit result format

Every decision-surface audit must report:

- stage audited;
- active authority files;
- number of material inputs inventoried;
- number fully traced;
- number explicitly non-material;
- untraced inputs;
- contradiction findings;
- under-specified-threshold findings;
- stale-authority findings;
- persistence-semantic findings;
- deterministic replay failures;
- overall result.

Overall result is one of:

- `QA PASS — DECISION SURFACE COMPLETE`
- `QA FAIL — CONTRADICTORY AUTHORITY`
- `QA FAIL — UNDER-SPECIFIED DECISION SURFACE`
- `QA FAIL — PERSISTENCE SEMANTIC COLLISION`
- `QA INCOMPLETE — DECISION SURFACE GAP`

A PASS requires zero material untraced inputs and zero unresolved deterministic replay failures.

---

## 14. Repair classification

Every repair must be classified as exactly one:

- `PROCESS COMPLIANCE FIX` — compiles/enforces already active intent;
- `RISK-TIGHTENING QUARANTINE` — temporary conservative restriction pending evidence;
- `MODEL CHALLENGER REQUIRED` — changes predictive threshold/exposure eligibility.

Do not disguise a model change as QA cleanup.

---

## 15. Audit-history rule

When QA misses a later-discovered material input:

1. reopen the prior QA result;
2. mark it incomplete;
3. add the missed input to the decision-surface inventory;
4. update the QA procedure if the miss reveals a framework gap;
5. rerun the affected stage from the full active authority stack.

Do not simply append the new finding and leave the original audit labelled complete.
