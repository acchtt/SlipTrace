# Football C4 — Prospective Test Protocol

**Status:** ACTIVE PROSPECTIVE SHADOW TEST  
**Model:** Football C4 structured-evidence Step-1 challenger  
**Champion:** Football C  
**Window:** next 5 complete clean Step-1 boards after the C4 activation merge

## 1. Authority

C4 is Step-1 shadow only.

It has zero authority over:
- Football C official state/rank/lane;
- Step-2 workload;
- Website Picks;
- user exposure;
- C2/C3 outputs or counters.

## 2. Board eligibility

A board advances the C4 counter only when:

- the normal Step-0 universe/coverage reconciliation is complete;
- the C/C2/C3 Step-1 board triplet passes common-evidence reconciliation;
- every ranked eligible fixture receives a complete C4 anchor payload before any result knowledge;
- every required anchor has a non-empty evidence basis;
- the C4 compiler executes successfully for the full ranked eligible universe;
- no C4 field is backfilled after result knowledge.

If any ranked eligible fixture lacks the required C4 anchors:

`C4 TEST BOARD INELIGIBLE — STRUCTURED EVIDENCE INCOMPLETE`

If the ranked universe differs:

`C4 TEST BOARD INELIGIBLE — RANKED UNIVERSE MISMATCH`

If any C4 rule is changed during the test window:
- version the change;
- reset the counter to 0/5.

## 3. Counter

Maintain:
- `C4 Test Board Number = 1..5`;
- `C4 Test Board Eligible = true/false`;
- `C4 Contamination Reason`.

Historical boards have zero confirmatory weight.

C2 and C3 counters are independent and remain unchanged.

## 4. Required prospective outputs

Per ranked eligible fixture freeze:

- C4 state;
- C4 rank;
- home/away compiled route;
- C4 carrier and side;
- C4 chance quality;
- C4 evidence confidence;
- C4 continuation quality;
- C4 failure resistance;
- C4 control-endpoint risk;
- C4 goal-3 funding;
- C4 goal-4 funding;
- C4 supported line;
- C4 reason trace;
- compiler version/revision.

## 5. Primary comparison endpoints

At post-slate audit measure:

1. C4 vs C ordinal rank inversion;
2. C4 vs C FOCUS/WATCH/PASS disagreement;
3. C4 vs C supported-line disagreement;
4. C4-FOCUS two-goal endpoint rate;
5. C-FOCUS -> C4-WATCH/PASS false-positive candidate rate;
6. C-PASS/WATCH -> C4-FOCUS false-negative candidate rate;
7. carrier-led winners retained vs lost;
8. exact structured-input replay reproducibility.

Do not optimize on individual match outcomes.

## 6. Promotion boundary

After Board 5/5, produce a comparison audit.

C4 may continue only if it demonstrates useful prospective separation with acceptable process completeness.

C4 may not become Step-2-capable merely because the compiler is deterministic. A separate promotion decision is required.

Any import of C4 thresholds into Football C is a production model change and requires explicit versioning/promotion evidence.
