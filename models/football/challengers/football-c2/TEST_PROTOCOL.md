# Football C2 — Prospective Test Protocol

**Champion:** Football C
**Challenger:** Football C2 — SHADOW
**Parent:** Football C production
**Status:** RESTARTED prospective window after dual-track workflow correction.

## 1. Initial run

Run C2 for the next **5 complete boards** after the activation commit.

This is a feasibility checkpoint, not automatic promotion.

Do not edit C2 during the five-board window.

## 2. Shared universe

Football C and C2 must start from the same AiScore broad-senior handoff/window.

A single common semantic evidence state is frozen before either model applies ranking/selection policy. C2 then applies its own policy independently to that frozen evidence.

## 3. Information clock

At each epoch use only evidence available then.

For XI/odds:
- same confirmed-XI snapshot;
- same user odds;
- same public-information window.

If C2 has seen Football C's final judgment before freezing its own policy output:
`C2 CONTAMINATION RISK — EXCLUDE FROM CONFIRMATORY PAIRED DECISION METRIC`.

## 4. Exposure

C2 is shadow-only:
- C2-BET;
- C2-WAIT;
- C2-PASS.

No Website Pick or real exposure.

## 5. Primary metric

`FLAT-STAKE UNIT RETURN DELTA ON SETTLED C-vs-C2 EXPOSURE DIFFERENCES`

Use exact contemporaneous lines/odds.

## 6. Selection-specific diagnostics

In addition to standard yield/W-HW-P-HL-L metrics, track:

- C2-FOCUS count;
- C2-WATCH count;
- direct BETs from FOCUS;
- direct BETs from WATCH;
- WATCH->BET promotions;
- selection-floor failures;
- protected-line inversion blocks;
- Focus Market-Gap Bridge attempts;
- bridge +0.25 executions;
- bridge +0.50 executions;
- bridge wins/losses;
- WAITs with >=0.50 market gap;
- unreachable-WAIT blocks;
- WAIT targets reached;
- WAITs expired by goal before target;
- FOCUS missed-winner environments;
- WATCH direct-bet losses;
- average rank of exposures.

## 7. Operational guardrail

Normal architecture:
1. integrated screen/research/rank;
2. one XI/odds confirmation;
3. one selection-floor check;
4. optional Focus Market-Gap Bridge;
5. optional WAIT resolution.

If C2 recreates Football A's stage count:
`C2 SIMPLICITY GUARDRAIL FAIL`.

## 8. Discovery set — zero validation weight

The following are design/discovery cases only:
- Cape Verde vs Rwanda;
- Uganda vs Libya;
- Liberia vs Mali;
- Czechia vs England;
- Spain vs Croatia;
- Benin vs Mauritania;
- San Marino vs Albania;
- Luxembourg vs Iceland;
- Slovakia vs Kazakhstan;
- Scotland vs Switzerland;
- Lesotho vs Morocco;
- Puebla Women vs Monterrey Women;
- all Football C1 trial outcomes before this activation commit.

They may be used to explain the design, never to validate C2.

## 9. Stop / invalidation conditions

Stop confirmatory counting if:
- C2 rules are edited after first eligible result;
- C2 reads future/result evidence before freezing;
- C2 directly copies A;
- quote epoch cannot be reconstructed;
- fixture identity unresolved;
- C2 creates official exposure;
- same-board selection is retrospectively changed.

Any predictive change requires a new challenger ID.

## 10. Five-board report

Report:
- board-by-board Football C vs C2;
- C2 shadow P/L;
- FOCUS vs WATCH exposure quality;
- direct vs WAIT;
- bridge usage and outcome;
- missed-winner and avoided-loser counts using exact quoted lines;
- average exposure rank;
- processing/runtime burden;
- strongest C2 failure;
- strongest Football C failure;
- CONTINUE SHADOW / STOP-REJECT / RESTART NEW CHALLENGER.


## 11. Restart boundary

The prior C2 workflow was not a clean C-vs-C2 comparison because:
- Step 1 was C2-only;
- Step 2 remained Football C;
- the protocol incorrectly named Football A as champion.

Therefore all confirmatory C2 counting restarts from the dual-track fix commit.

Pre-fix C2 records may be used for debugging only and carry zero confirmatory weight in the restarted comparison.
