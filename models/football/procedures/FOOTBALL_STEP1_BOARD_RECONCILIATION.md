# Football Step-1 Board Reconciliation

**Status:** ACTIVE PROCESS COMPLIANCE CONTROL  
**Scope:** `/rank` Football C official + C2/C3 shadow boards  
**Predictive effect:** none

## Purpose

Step 1 freezes one common football-fact evidence state, then lets C, C2 and C3 apply different model-owned policy.

Three independent `board` engine calls are not sufficient proof that the same common evidence was used. This procedure makes the comparison fail closed on research drift or ranked-universe mismatch.

## Required evidence bases

Every ranked fixture must carry:

- `common_evidence_basis` — a non-empty summary of the shared Step-1 football research used to freeze route/carrier/chance/failure/evidence-quality grades;
- `supported_line_basis` — model-owned explanation for why that model's supported burden is the highest burden justified without an optimistic tail;
- for C/C2: `board_state_basis` — explanation for the frozen PASS/WATCH/FOCUS classification;
- C3: `c3_second_route_role_basis` and `c3_forced_chaos_basis` in addition to the existing funding/control bases.

These basis fields have zero ranking weight.

## Mandatory three-board runner

Use:

`python models/football/engine/board_triplet_cli.py --c <c.json> --c2 <c2.json> --c3 <c3.json>`

The runner requires:

1. the same ranked eligible match IDs in C/C2/C3;
2. exact equality of the common factual fields for every match;
3. no Football C completion-policy fields in C2/C3 payloads;
4. no C3-only funding/control fields in C/C2 payloads;
5. all three individual board engines to pass.

Success:

`BOARD ENGINE EXECUTION STATUS: EXECUTED_ALL_THREE_BOARDS`

and:

`COMMON EVIDENCE RECONCILED: true`

Failure examples:

- `BOARD TRIPLET FAILED — RANKED ELIGIBLE UNIVERSE MISMATCH`
- `BOARD TRIPLET FAILED — COMMON EVIDENCE DRIFT`
- `BOARD TRIPLET FAILED — C POLICY FIELD LEAK INTO SHADOW PAYLOAD`
- `BOARD TRIPLET FAILED — C3 POLICY FIELD LEAK INTO C/C2 PAYLOAD`

A failed triplet means the C2/C3 comparison is contaminated. Preserve the official semantic C board, fix the payload/evidence plumbing, and rerun. Do not advance prospective challenger counters from a contaminated board.

## Model-owned fields

The following may differ across payloads because they are policy, not common facts:

- `board_state` and `board_state_basis` for C/C2;
- `supported_line` and `supported_line_basis`;
- Football C completion mode/quality, continuation, opponent leakage and stall risk;
- C3 second-route, funding, control and forced-chaos fields.

Independent model-owned lines may coincidentally be equal. Equality alone is not proof of copying; the independent basis must be present.

## Board-state boundary

This control does **not** invent a new deterministic C/C2 FOCUS/WATCH/PASS threshold.

The active C and C2 texts still own those semantic classifications. Because those states can affect downstream action/workload, their basis must be persisted and auditable.

Any proposal to replace the current semantic C/C2 state boundary with a new numerical/deterministic classifier is a model-rule change and must be versioned/tested separately rather than silently introduced by QA.

C3 is different: its board state is already generated deterministically from its frozen funding/control policy.

## Persistence

Daily Coverage must preserve:
- common evidence basis;
- model-specific supported-line basis;
- C/C2 board-state basis;
- engine board result/revision;
- common-evidence reconciliation status.

Publishing remains an exact copy of the frozen board. Airtable publication must not re-screen or reconstruct these bases.
