# Football C4 — Structured Evidence Step-1 Challenger

**Status:** PROSPECTIVE STEP-1 SHADOW CHALLENGER  
**Champion:** Football C  
**Parallel challengers:** Football C2 and Football C3 remain frozen and unchanged  
**Scope:** Step 1 `/rank` only. C4 has no Step-2, live, Website Pick or real-exposure authority.

## 1. Purpose

C4 tests one hypothesis:

> Step-1 selection becomes more reproducible when semantic grades are compiled from a small set of explicit evidence anchors rather than assigned directly as free-form WEAK/USABLE/STRONG or LOW/MEDIUM/HIGH judgments.

C4 exists because the 2026-10-04 Step-1 decision-surface QA found multiple material predictive surfaces whose downstream engine effects were deterministic but whose upstream classifications were under-specified.

C4 is not a rewrite of Football C. It is a separate prospective challenger.

## 2. Fair-comparison boundary

C4 receives the same admitted ranked-eligible fixture universe and the same contemporaneous Step-1 research epoch as C/C2/C3.

C4 must not read:
- Football C/C2/C3 rank;
- Football C/C2/C3 board state;
- Football C/C2/C3 supported burden;
- any result/FT information.

C4 may reuse factual evidence discovered in the common research pass, but it freezes its own structured evidence anchors before any C4 output is calculated.

Historical matches may motivate the rules but have zero confirmatory weight.

## 3. Structured evidence anchors

For each side freeze exactly one state for each route component:

### Creation repeatability
- `VERIFIED` — current evidence shows a repeatable creation mechanism, not merely recent scoreline output.
- `PARTIAL` — mechanism is visible but sample/role continuity is incomplete.
- `NONE` — no credible repeatable current creation mechanism is established.

### Dangerous access
- `VERIFIED` — repeatable central/box/high-value access is established.
- `PARTIAL` — access exists but is inconsistent or largely low-volume.
- `NONE` — no credible high-value access is established.

### Service / finishing continuity
- `VERIFIED` — current personnel/roles support conversion of the route.
- `PARTIAL` — route remains possible but one material service/finishing dependency is uncertain.
- `NONE` — current personnel/role state materially breaks the route.

### Matched opponent leakage
- `VERIFIED` — opponent repeatedly concedes the same mechanism C4 is evaluating.
- `PARTIAL` — leakage exists but the mechanism match is incomplete.
- `NONE` — no relevant current leakage support is established.

### Personnel integrity
- `INTACT`
- `PARTIAL`
- `DAMAGED`

### Route-specific suppression
- `VERIFIED`
- `PARTIAL`
- `NONE`

Every anchor requires a short non-empty basis. Scorelines alone cannot create a VERIFIED anchor.

## 4. Deterministic route compiler

For each side, C4 compiles `STRONG / USABLE / WEAK`.

### STRONG
All must hold:
- creation repeatability = VERIFIED;
- personnel integrity != DAMAGED;
- route-specific suppression != VERIFIED;
- at least one of dangerous access or matched opponent leakage = VERIFIED;
- service/finishing continuity != NONE.

### USABLE
Use when STRONG does not clear and all hold:
- personnel integrity != DAMAGED;
- route-specific suppression != VERIFIED;
- at least two of creation repeatability, dangerous access, service/finishing continuity, matched opponent leakage are PARTIAL or VERIFIED;
- at least one of those four is VERIFIED.

### WEAK
Otherwise.

This compiler is deterministic and has no weighted score.

## 5. Carrier compiler

For each side also freeze:
- `multi_goal_repeatability = VERIFIED / PARTIAL / NONE`.

C4 carrier is:

### STRONG
At least one side:
- compiled route = STRONG;
- multi-goal repeatability = VERIFIED.

### USABLE
If STRONG does not clear and at least one side:
- compiled route >= USABLE;
- multi-goal repeatability = PARTIAL or VERIFIED.

### NONE
Otherwise.

Carrier side is recorded as `HOME / AWAY / BOTH / NONE`.

## 6. Chance-quality compiler

C4 chance quality:

### HIGH
At least one side has:
- creation repeatability = VERIFIED;
- dangerous access = VERIFIED;
- personnel integrity != DAMAGED.

### MEDIUM
HIGH does not clear, but at least one side compiles to USABLE/STRONG.

### LOW
Otherwise.

## 7. Evidence-confidence compiler

Freeze three coverage anchors:
- `mechanism_evidence_coverage = COMPLETE / PARTIAL / MISSING`;
- `team_news_coverage = COMPLETE / PARTIAL / MISSING`;
- `competition_context_coverage = COMPLETE / PARTIAL / MISSING`.

C4 evidence confidence:

- HIGH — all three COMPLETE;
- MEDIUM — none MISSING and at least one PARTIAL;
- LOW — any MISSING.

Coverage quality is not football quality. It only controls confidence.

## 8. Continuation and control

Freeze:
- `continuation_after_first_goal = VERIFIED / PARTIAL / NONE`;
- `lead_control_tendency = VERIFIED / PARTIAL / NONE`;
- `draw_utility = VERIFIED / NOT_APPLICABLE / NONE`.

C4 control-endpoint risk:

- HIGH — lead-control tendency = VERIFIED, or draw utility = VERIFIED while continuation is not VERIFIED;
- MEDIUM — HIGH does not clear and either lead-control tendency = PARTIAL or continuation = PARTIAL;
- LOW — continuation = VERIFIED and lead-control tendency = NONE and draw utility != VERIFIED;
- otherwise MEDIUM.

C4 continuation quality:
- HIGH — continuation VERIFIED;
- MEDIUM — continuation PARTIAL;
- LOW — continuation NONE.

## 9. Suppression / failure compiler

Freeze:
- `mechanism_failure = VERIFIED / PARTIAL / NONE`;
- `match_suppression = VERIFIED / PARTIAL / NONE`.

C4 failure resistance:
- LOW — either is VERIFIED;
- MEDIUM — neither VERIFIED and at least one PARTIAL;
- HIGH — both NONE.

C4 material suppression = true only when `match_suppression=VERIFIED`.

C4 failure attacks route = true only when `mechanism_failure=VERIFIED`.

These are C4-owned declarations; they do not overwrite Football C fields.

## 10. Clearing-goal funding

### Goal 3 — VERIFIED
Any one:
1. STRONG carrier + continuation VERIFIED + no verified mechanism failure/suppression;
2. both compiled routes >= USABLE, at least one STRONG, continuation VERIFIED, and control risk != HIGH.

### Goal 3 — PARTIAL
VERIFIED does not clear and:
- at least one STRONG route; or
- two USABLE routes;
and:
- failure resistance != LOW;
- evidence confidence != LOW.

### Goal 3 — NONE
Otherwise.

### Goal 4 — VERIFIED
All:
- goal 3 = VERIFIED;
- carrier = STRONG;
- `upper_tail_repeatability = VERIFIED`;
- continuation VERIFIED;
- control risk = LOW.

### Goal 4 — PARTIAL
VERIFIED does not clear and:
- goal 3 = VERIFIED;
- upper-tail repeatability = PARTIAL or VERIFIED;
- continuation != NONE;
- control risk != HIGH.

### Goal 4 — NONE
Otherwise.

Freeze `upper_tail_repeatability = VERIFIED / PARTIAL / NONE` with a basis.

## 11. Supported burden compiler

C4 line is generated mechanically from funding:

- goal 3 = NONE -> `NO_SUPPORTED_LINE`;
- goal 3 = PARTIAL -> O2.0;
- goal 3 = VERIFIED, goal 4 = NONE -> O2.5;
- goal 3 = VERIFIED, goal 4 = PARTIAL -> O2.75;
- goal 4 = VERIFIED -> O3.0.

C4 never raises line for market price.

This mapping is a challenger hypothesis and must not be imported into Football C without prospective evidence.

## 12. C4 Step-1 state

### C4-FOCUS
All:
- goal 3 VERIFIED;
- control risk LOW;
- failure resistance >= MEDIUM;
- evidence confidence HIGH;
- no material suppression;
- supported line exists.

### C4-WATCH
FOCUS does not clear, supported line exists, and:
- goal 3 PARTIAL/VERIFIED;
- control risk != HIGH;
- failure resistance != LOW;
- evidence confidence != LOW.

### C4-PASS
Otherwise.

## 13. Ranking

Rank deterministically by:

1. C4 state: FOCUS > WATCH > PASS;
2. goal-3 funding: VERIFIED > PARTIAL > NONE;
3. goal-4 funding: VERIFIED > PARTIAL > NONE;
4. lower control-endpoint risk;
5. carrier: STRONG > USABLE > NONE;
6. chance quality: HIGH > MEDIUM > LOW;
7. failure resistance: HIGH > MEDIUM > LOW;
8. evidence confidence: HIGH > MEDIUM > LOW;
9. lower supported burden as a late comparator;
10. canonical `match_id` tie break.

No market term is allowed.

## 14. Output

For every ranked eligible fixture emit:

- C4 state/rank;
- home/away compiled route;
- carrier + carrier side;
- chance quality;
- evidence confidence;
- continuation quality;
- failure resistance;
- control-endpoint risk;
- goal-3 funding;
- goal-4 funding;
- C4 supported line;
- deterministic reason trace.

## 15. Operational boundary

C4 is Step-1 shadow only.

For any fixture that reaches `/xi`, the launcher must **display the prospectively frozen C4 Step-1 snapshot** when one exists:
- C4 state/rank;
- C4 supported line;
- route/carrier/funding/control summary;
- compiler revision;
- C4 Board N/5 status.

This visibility is read-only. It is not a C4 Step-2 assessment and must be labeled:
`SHADOW C4 (STEP1) — NO STEP2 ACTION`

C4 must never:
- create FOLLOW/RESERVE/STOP workload;
- create a Step-2 action or require extra `/xi` work;
- create a Website Pick;
- authorize real exposure;
- modify C/C2/C3 fields;
- affect C2/C3 prospective counters.

## 16. Prospective test

Run C4 on the next **5 complete clean Step-1 boards**.

Primary endpoints:
- C4 vs C rank inversion;
- C4 vs C supported-line disagreement;
- two-goal endpoint rate among C4-FOCUS vs C-FOCUS;
- C false negatives that C4 promotes;
- C false positives that C4 demotes;
- carrier-led wins retained by C4;
- percentage of fixtures whose C4 classification is reproducible from complete anchors.

Do not optimize C4 during the 5-board window.

If any predictive rule changes, increment C4 version and restart the five-board counter at zero.
