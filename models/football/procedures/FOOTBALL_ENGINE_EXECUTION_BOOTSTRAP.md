# Football Step-2 Engine Execution Bootstrap

**Status:** MANDATORY STEP-2 EXECUTION PRECHECK  
**Applies to:** `/xi` deterministic validation  
**Common runtime precheck:** `models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md`  
**Models:** Football C, C2, C3  
**Engine authority:** shadow validator only

## 1. Core rule

Before this Step-2-specific procedure, complete the common runtime bootstrap with stage=`xi` and preserve its `FOOTBALL_RUNTIME_EXECUTION_RECORD`.

A completed Step-2 decision requires deterministic execution for all three tracks:

- `model=c`
- `model=c2`
- `model=c3`

Primary execution surface:
`models/football/engine/xi_portable.py`

Fetch the exact-current portable bundle and run:

`python xi_portable.py self-check`

Required:
`XI PORTABLE RUNTIME: PASS`

Then use the same file for triplet execution and session reconciliation. The portable bundle embeds the exact C/C2/C3 Step-2 modules, so a missing checkout or missing local import tree cannot block the normal XI path.

The multi-file engine path below is fallback only when the exact-current portable bundle itself fails self-check. A payload/contract rejection from the portable runner is **not** a Python/runtime failure.

Lack of an already-existing local repository checkout is **not** engine unavailability.

If the current engine source is accessible through GitHub/files/connectors and a Python runtime is available, the assistant must first create a runnable temporary workspace from the exact current engine source, then execute the validators.

Do not choose a fallback merely because setup has not yet been performed.

## 2. Required source set

Primary Step-2 source:
- `models/football/engine/xi_portable.py`

Only if the portable self-check fails after exact-current retrieval, materialize the fallback exact current revision of:

- `models/football/engine/cli.py`
- `models/football/engine/adapter.py`
- `models/football/engine/core.py`
- `models/football/engine/competition_reliability.py`
- `models/football/engine/schema.json`
- `models/football/engine/decision_triplet_cli.py`

into one runnable workspace preserving the relative `models/football/engine/` layout.

If a full repository checkout is already available at the same current revision, use it instead.

## 3. Revision integrity

Before execution, record the current repository revision/commit used for:
- `CURRENT_MODEL.md`;
- the current `/xi` launcher;
- the engine source.

The engine source and launcher must come from the same current authority revision whenever practical.

If revisions differ materially:

`ENGINE EXECUTION FAILED — ATTEMPTED — REVISION MISMATCH`

Do not silently run a stale local engine against a newer launcher.

## 4. Required payload set

Freeze the common Step-2 evidence first.

Then create three immutable payloads:

- `FOOTBALL_ENGINE_C_DECISION_INPUT`
- `FOOTBALL_ENGINE_C2_DECISION_INPUT`
- `FOOTBALL_ENGINE_C3_DECISION_INPUT`

The payloads must share the same common factual evidence epoch while preserving each model's independently owned state/line/policy fields.

Never edit a payload after seeing an engine result.

## 5. Preferred execution

Preferred one-command execution:

`python xi_portable.py triplet --c <c.json> --c2 <c2.json> --c3 <c3.json>`

Preferred session reconciliation:

`python xi_portable.py reconcile --input <step2_reconcile.json>`

Multi-file fallback only:

`python models/football/engine/decision_triplet_cli.py --c <c.json> --c2 <c2.json> --c3 <c3.json>`

The triplet runner must:
- require all three files;
- verify payload model names are exactly c / c2 / c3;
- execute all three through the deterministic adapter;
- fail non-zero if any payload is missing, malformed or rejected;
- emit all three results together.

Direct individual CLI calls are acceptable only when both the portable runner and multi-file triplet runner cannot be used:

`python models/football/engine/cli.py decision --input <c.json>`

`python models/football/engine/cli.py decision --input <c2.json>`

`python models/football/engine/cli.py decision --input <c3.json>`

## 6. What counts as genuine execution unavailability

Fallback is permitted only after the common runtime bootstrap proves an actual setup/execution attempt failed for a technical reason that cannot be resolved in the current turn. A failure claim without `FOOTBALL_RUNTIME_EXECUTION_RECORD` is invalid.

Examples, each requiring recorded actual probes:
- all available Python execution probes failed;
- exact-current `xi_portable.py` failed self-check and the repaired multi-file fallback also failed;
- the connected GitHub/current Project source probe failed and no exact-current source can be retrieved/materialized;
- required engine source is corrupt/unreadable;
- runtime dependency/import failure remains after reasonable setup;
- exact current revision cannot be established safely.

The following are **not** valid unavailability reasons:
- container `git clone` / DNS / raw-network failure while GitHub connector source remains accessible;
- "the repo is only visible through GitHub";
- "there is no local checkout yet";
- "the engine files have not been downloaded/materialized yet";
- "running it would take extra setup";
- "text decisions are already available".

## 7. Fail-closed fallback

The old generic fallback is forbidden:

`ENGINE NOT EXECUTED — STRUCTURED INPUT PRESERVED`

If execution genuinely fails after an attempted setup, report:

`ENGINE EXECUTION FAILED — ATTEMPTED — <exact technical reason>`

Also preserve:
- the `FOOTBALL_RUNTIME_EXECUTION_RECORD`;
- all three structured payloads;
- source revision;
- attempted command/setup path;
- any error message available.

A completed Step-2 decision with no engine result and no explicit failed-attempt record is a workflow execution failure.

## 8. Output status

Every completed `/xi` assessment must show one of:

`ENGINE EXECUTION STATUS: EXECUTED_ALL_THREE`

or

`ENGINE EXECUTION STATUS: FAILED_AFTER_ATTEMPT — <exact technical reason>`

When execution succeeds, show:
- Engine C result
- Engine C2 result
- Engine C3 result

If text and engine disagree:

`ENGINE DISAGREEMENT — PRESERVE BOTH`

Python remains shadow validation; Football C text remains production authority.

## 9. New-chat behavior

A fresh chat must not treat lack of local files as a reason to skip validation.

After the handoff freshness bootstrap:
1. retrieve exact-current `xi_portable.py`;
2. run `xi_portable.py self-check`;
3. write the three frozen payloads;
4. run `xi_portable.py triplet`;
5. preserve results;
6. use multi-file materialization only if the portable self-check itself fails.

This requirement applies whether the user typed `/xi` explicitly or clearly requested the equivalent XI/odds reassessment.
