# Football C + C2 Active Pair Contract

**Status:** ACTIVE — supersedes every C3/C4 workflow surface
**Effective:** 2026-10-06
**Official model:** Football C
**Only challenger:** Football C2 — SHADOW

## 1. Active roster

Football C3 and Football C4 are retired. They must not be executed, displayed, persisted for new decisions, counted in new board/accounting windows, or required by /rank, /xi, /live, /audit, /report, runtime bootstrap, reconciliation, or CI.

Historical C3/C4 records remain immutable audit history. Never delete or rewrite historical rows merely because the models are retired.

## 2. Common evidence, independent policy

C and C2 receive the same prospectively frozen factual evidence epoch. Their model-owned fields, supported burdens, board states and actions remain independent. Never manufacture a missing C2 state from C.

## 3. Atomic exception rule

Every user-declared /xi exception is a C+C2 assessment. "all models" now means the active roster: C + C2.

Before issuing any verdict:
1. freeze the common prematch/XI/research/market/tournament evidence;
2. freeze both C and C2 model-owned inputs and supported lines;
3. persist the frozen pair inputs;
4. execute deterministic C and C2 validation from that same epoch;
5. persist both outputs;
6. only then publish the combined verdict.

The pair is fail-closed for completion. If C2 cannot be lawfully frozen or executed, do not present the exception as a completed C-only verdict. Persist:
`C+C2 EXCEPTION INCOMPLETE — <exact reason>`
and preserve the frozen evidence for resume.

Never reconstruct C2 after kickoff or FT from later information.

## 4. Runtime

Primary XI runtime:
`python xi_portable.py pair --c <c.json> --c2 <c2.json>`

A completed Step-2 decision requires both validators to execute. C remains the only official exposure authority; C2 remains shadow-only.

## 5. Persistence and accounting

New Decision State rows must persist C Action, C Supported Line, C2 Shadow Action and C2 Supported Line together for completed assessments. C2 may never create a Website Pick.

New model accounting includes C and C2 only. Historical C3/C4 accounting is retained as historical data but excluded from active-roster forward metrics.

## 6. Precedence

If any older file says C3/C4 are active, requires a triplet, requires C4 visibility, or defines "all models" as including C3/C4, this contract overrides it until that stale text is removed.
