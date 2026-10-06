# Football Step-1 Board Reconciliation

**Status:** ACTIVE PROCESS COMPLIANCE CONTROL  
**Scope:** `/rank` Football C official + Football C2 shadow boards  
**Active roster:** C + C2 only

## Purpose

Step 1 freezes one common football-fact evidence state, then lets Football C and Football C2 apply different model-owned policy. The board comparison is valid only when both active models receive the same ranked eligible universe and the same common evidence epoch.

This procedure protects comparison integrity. It does not change either model's predictive policy.

## Required frozen fields

Every ranked fixture must carry one shared factual evidence block including:
- `common_evidence_basis`;
- operational viability/reliability snapshot;
- route/carrier/chance/failure evidence;
- H2H materiality/basis;
- tournament-incentive fields when applicable;
- kickoff identity.

Model-owned fields remain separate:

Football C owns:
- `board_state`;
- `board_state_basis`;
- `supported_line`;
- `supported_line_basis`;
- completion mode;
- burden-completion quality;
- continuation quality;
- opponent leakage;
- burden stall risk.

Football C2 owns:
- `board_state`;
- `board_state_basis`;
- `supported_line`;
- `supported_line_basis`;
- its route-quality ranking/selection-floor policy.

C2 must never inherit Football C's supported line or Football C's completion-policy fields.

## Deterministic pair reconciliation

Run:

`python models/football/engine/board_pair_cli.py --c <c.json> --c2 <c2.json>`

Required success:

`BOARD ENGINE EXECUTION STATUS: EXECUTED_C_C2_BOARDS`

and:

`common_evidence_reconciled = true`

The pair runner must require:

1. the same ranked eligible match IDs in C and C2;
2. the same shared factual evidence for each match;
3. complete model-owned semantic trace for each model;
4. no Football C completion-policy fields in the C2 payload.

Fail closed on:

- `BOARD PAIR FAILED — RANKED ELIGIBLE UNIVERSE MISMATCH`
- `BOARD PAIR FAILED — COMMON EVIDENCE DRIFT`
- `BOARD PAIR FAILED — C POLICY FIELD LEAK INTO C2 PAYLOAD`
- incomplete common evidence;
- incomplete model semantic trace.

A failed pair means the active C-vs-C2 comparison is contaminated. Preserve the prospectively frozen source evidence, fix only the evidence/payload plumbing, and rerun. Do not manufacture a C2 board from C.

## Ranking authority

Football C remains the only official production board. Football C2 is shadow-only.

The pair runner validates both boards but does not authorize:
- a C2 Website Pick;
- a C2 official exposure;
- extra Step-2 workload from C2.

Routine Step-2 workload is selected only from Football C's official FOLLOW/RESERVE/STOP lane.

## Clearing-goal funding and FOLLOW

Football C's current ranking/follow-through policy must distinguish broad FOCUS classification from harder FOLLOW certification.

For a supported burden that requires a third goal, especially O2.5/O2.75:
- strong carrier production alone does not prove the clearing third goal;
- a weak/merely usable second route does not automatically fund goal three;
- continuation and burden-completion grades must be supported by explicit frozen evidence;
- carrier-led candidates without independently credible clearing-goal funding can remain C-FOCUS while being RESERVE/STOP.

This is the current Football C selection architecture, not a reactivation of retired C3 policy.

## Persistence

Persist for every ranked active fixture:
- common evidence basis;
- C board state/rank;
- C board state basis;
- C supported line + supported line basis;
- C2 board state/rank;
- C2 board state basis;
- C2 supported line + supported line basis;
- board pair reconciliation status;
- engine/source revision;
- official C lane.

Historical C3/C4 fields may remain in old records. They are not required, executed, or populated for new boards.

## Historical fidelity

Old board-triplet/C3/C4 records remain immutable historical audit data. Do not rewrite them merely because the active roster changed.

For new boards, `board_triplet_cli.py` and C4 compilation are retired execution paths.
