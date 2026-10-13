# Football C + C2 Active Pair Contract

> **Active model Airtable route (Oct 11):** Load `models/football/airtable/ACTIVE_MODEL_ROUTING.md` and `ACTIVE_MODEL_ROUTING.json`. All model, accounting and reporting reads/writes go to `appbzxqXYf0lKfD4P` using the corresponding NEW table IDs and source-key readback. Do not use old-base IDs for writes. **Do not modify `/sweep` routing, source checkpoint or Step0 handoff.** Actual Bets are only from confirmed user slips; C official, C2 shadow.

**Status:** ACTIVE — supersedes every C3/C4 workflow surface
**Effective:** 2026-10-06
**Official model:** Football C
**Only challenger:** Football C2 — SHADOW

## 1. Active roster

Football C3 and Football C4 are retired. They must not be executed, displayed, persisted for new decisions, counted in new board/accounting windows, or required by /rank, /xi, /live, /audit, /report, runtime bootstrap, reconciliation, or CI.

Historical C3/C4 records remain immutable audit history. Never delete or rewrite historical rows merely because the models are retired.

## 2. Common evidence, independent policy

C and C2 receive the same prospectively frozen factual evidence epoch. Their model-owned fields, supported burdens, board states and actions remain independent. Never manufacture a missing C2 state from C.

C2 model-owned evidence now also includes the optional paired fields
`c2_opponent_leakage` and `c2_opponent_leakage_basis`. They must be
independently researched from current opponent-specific evidence and supplied
together; they are never aliases for C's `opponent_leakage` or
completion/continuation/stall diagnostics. Absence of both fields is lawful
but cannot activate the C2 O2.25 leakage certificate.

## V4 exception supersession for football-only reads

Explicit `/xi exception` can execute independently sourced quote-free C+C2 football without a V4 board or V1–V3 packaged Step0. Missing genuine C2 input is disclosed as incomplete; C is not copied into C2. The older pair-input persistence before **priced publication** remains mandatory for a genuine betting action, not a reason to refuse a football discussion or defer a paired quote-free result. See the new concise current `02_NORMAL_CHAT_XI_ODDS.md`. User quote not required for football-only analysis.

## 3. Atomic exception rule

Every user-declared /xi exception is a C+C2 assessment. "all models" now means the active roster: C + C2.

Before issuing any football verdict:
1. freeze the common fixture/XI/research/tournament evidence and current score/minute when live;
2. freeze both C and C2 model-owned football inputs and supported lines, including BOTH C2 leakage fields when independently evidenced;
3. execute deterministic quote-free C and C2 validation from that same epoch;
4. persist/read back both football outputs;
5. only then publish the combined football verdict.
A market quote is optional. If pricing is supplied, evaluate it as a separate
same-command subdecision under the current /xi screenshot/executability rules;
never make market data a prerequisite for the football pair.

The pair is fail-closed for completion. If C2 cannot be lawfully frozen or executed, do not present the exception as a completed C-only verdict. Persist:
`C+C2 EXCEPTION INCOMPLETE — <exact reason>`
and preserve the frozen evidence for resume.

Never reconstruct C2 after kickoff or FT from later information.

## 4. Runtime

Primary current XI runtime:
`python xi_portable.py xi --c <c_football.json> --c2 <c2_football.json>`

Required football success is `EXECUTED_C_C2_FOOTBALL_ONLY`. The legacy
priced `pair` command is not the primary /xi completion path; it may be used
only by the separate strict prematch executable-price channel with genuine
decision-stage payloads. A completed football assessment requires both
validators to execute. C remains the only official exposure authority; C2
remains shadow-only.

## 5. Persistence and accounting

New Decision State rows must persist C Action, C Supported Line, C2 Shadow Action and C2 Supported Line together for completed assessments. C2 may never create a Website Pick.

New model accounting includes C and C2 only. Historical C3/C4 accounting is retained as historical data but excluded from active-roster forward metrics.

## 6. Precedence

If any older file says C3/C4 are active, requires a triplet, requires C4 visibility, or defines "all models" as including C3/C4, this contract overrides it until that stale text is removed.
