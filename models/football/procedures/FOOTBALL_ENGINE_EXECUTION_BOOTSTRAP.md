# Football Step-2 Engine Execution Bootstrap

**Status:** MANDATORY STEP-2 EXECUTION PRECHECK  
**Applies to:** `/xi` deterministic validation  
**Common runtime precheck:** `models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md`  
**Active models:** Football C official + Football C2 shadow  
**Retired models:** C3/C4 — historical records only

## 1. Core rule

Before Step 2, complete the common runtime bootstrap with stage=`xi` and preserve its `FOOTBALL_RUNTIME_EXECUTION_RECORD`.

A completed Step-2 decision requires deterministic execution for both active tracks:

- `model=c`
- `model=c2`

Primary execution surface:

`models/football/engine/xi_portable.py`

Fetch the exact-current portable bundle and run:

`python xi_portable.py self-check`

Required:

`XI PORTABLE RUNTIME: PASS`

Then execute the active pair atomically:

`python xi_portable.py pair --c <c.json> --c2 <c2.json>`

Required success:

`ENGINE EXECUTION STATUS: EXECUTED_C_C2_PAIR`

The pair must come from the same frozen common evidence epoch. A mismatch is a contract rejection, not a Python/runtime failure.

## 2. Atomic completion rule

A user-declared exception or normal completed Step-2 assessment is incomplete unless both C and C2 execute and persist.

If either active model cannot be lawfully frozen or executed:

`C+C2 EXCEPTION INCOMPLETE — <exact reason>`

Do not publish a completed C-only exception verdict. Never reconstruct missing C2 after kickoff or FT.

C remains the only model that can create official exposure. C2 is shadow-only.

## 3. Portable runtime

The portable bundle embeds only the active Step-2 dependencies:

- `core.py`
- `competition_reliability.py`
- `adapter.py`
- `step2_reconcile.py`
- `model_bet_accounting.py`

It must not depend on `decision_triplet_cli.py`, C3 execution, or C4 execution.

A payload/model contract rejection from the portable runner must be reported as:

`XI ENGINE CONTRACT REJECTED — <exact rejected field/rule>`

Do not classify a deterministic contract rejection as Python/runtime unavailability.

## 4. Multi-file fallback

Only if the exact-current portable bundle itself fails self-check after retrieval, materialize:

- `models/football/engine/cli.py`
- `models/football/engine/adapter.py`
- `models/football/engine/core.py`
- `models/football/engine/competition_reliability.py`
- `models/football/engine/schema.json`
- `models/football/engine/decision_pair_cli.py`
- `models/football/engine/step2_reconcile.py`
- `models/football/engine/step2_reconcile_cli.py`
- `models/football/engine/model_bet_accounting.py`
- `models/football/engine/model_bet_accounting_cli.py`

Fallback pair command:

`python models/football/engine/decision_pair_cli.py --c <c.json> --c2 <c2.json>`

Direct individual decision CLI calls are diagnostic only and do not satisfy atomic C+C2 completion.

## 5. Required payload set

Freeze the common Step-2 evidence first, then create:

- `FOOTBALL_ENGINE_C_DECISION_INPUT`
- `FOOTBALL_ENGINE_C2_DECISION_INPUT`

The payloads must share the same factual evidence epoch while preserving independent model-owned board state, supported line and policy fields.

Never edit a frozen payload after seeing an engine result.

## 6. Reconciliation and accounting

After pair execution:

`python xi_portable.py reconcile --input <step2_reconcile.json>`

Then compile active-model accounting:

`python xi_portable.py accounting --input <model_accounting.json>`

New accounting payloads contain C and C2 only. Historical C3/C4 accounting remains immutable audit history and is excluded from new active-roster forward metrics.

## 7. Genuine execution unavailability

Fallback is permitted only after actual current-turn probes prove a technical execution failure. Lack of a local checkout, raw container network failure while GitHub connector access works, or extra setup work are not valid unavailability reasons.

If execution genuinely fails after attempted setup, report:

`ENGINE EXECUTION FAILED — ATTEMPTED — <exact technical reason>`

and preserve:
- `FOOTBALL_RUNTIME_EXECUTION_RECORD`;
- both frozen payloads;
- repository/source revision;
- attempted command;
- exact error.

The legacy fallback is forbidden:

`ENGINE NOT EXECUTED — STRUCTURED INPUT PRESERVED`

## 8. Output status

Every completed `/xi` assessment must show either:

`ENGINE EXECUTION STATUS: EXECUTED_C_C2_PAIR`

or

`ENGINE EXECUTION STATUS: FAILED_AFTER_ATTEMPT — <exact technical reason>`

When successful, show:
- Engine C result
- Engine C2 result

If text and engine disagree:

`ENGINE DISAGREEMENT — PRESERVE BOTH`

Python remains deterministic validation; Football C remains production authority.

## 9. New-chat behavior

A fresh chat must:
1. retrieve exact-current `xi_portable.py`;
2. run `xi_portable.py self-check`;
3. freeze C and C2 payloads from one evidence epoch;
4. run `xi_portable.py pair`;
5. run reconciliation and active-model accounting;
6. preserve both outputs.

C3/C4 are never required for new Step-2 completion.
