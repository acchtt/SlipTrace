# Football Runtime Execution Bootstrap

**Status:** MANDATORY EXECUTION PRECHECK  
**Applies to:** any football stage that requires deterministic Python execution, including `/rank`, `/xi`, and `/audit`  
**Repository:** `acchtt/SlipTrace`  
**Purpose:** prevent false "Python unavailable" / "GitHub unavailable" / "engine unavailable" claims

## 1. Core rule

Do not infer tool or repository unavailability from environment shape.

The following are **not** evidence that execution is unavailable:
- no repository checkout is already present;
- `git clone` fails inside a network-isolated container;
- the engine is only visible through the connected GitHub source;
- source files have not yet been materialized locally;
- execution requires setup;
- a previous chat reported the runtime unavailable;
- a handoff says the engine was not executed.

Availability must be established **in the current turn** by actual probes.

## 2. Required preflight order

For an execution-required stage, perform these steps in order.

### A. Python probe

Attempt a real Python runtime call.

Preferred probes:
- existing Python execution tool; or
- container `python3 --version`; then
- container `python --version` if needed.

Record:

`PYTHON PROBE: PASS — <runtime/version>`

or the exact attempted command/tool error.

Do not write "Python unavailable" before a real probe fails.

### B. Repository-source probe

Resolve the current `main` revision from the connected GitHub source for `acchtt/SlipTrace`.

Preferred source order:
1. connected GitHub connector/API;
2. current Project/Files source if it contains the exact current revision;
3. already-materialized checkout only when its revision matches current authority.

Record:

`REPOSITORY PROBE: PASS — acchtt/SlipTrace@<sha> via <source>`

A container's inability to reach github.com is **not** a failed repository probe when the GitHub connector remains available.

If `git clone`, `curl`, DNS, or raw-network access fails in the container, classify it:

`CONTAINER NETWORK UNAVAILABLE — NOT REPOSITORY UNAVAILABLE`

and continue through the GitHub connector/source path.

Do not write "GitHub unavailable" unless the actual GitHub connector/source call itself failed and no exact-current Project/Files source is available.

### C. Source materialization

For stage=`xi`, use the portable fast path first:

1. fetch only `models/football/engine/xi_portable.py` from the exact current repository revision;
2. write it to a temporary runnable workspace;
3. run `python xi_portable.py self-check` (or the available Python execution surface);
4. if it passes, use the same file for both triplet execution and Step-2 reconciliation;
5. do **not** materialize the full engine tree or run the multi-file XI runtime probe on a successful portable path.

Required portable success:

`XI PORTABLE RUNTIME: PASS`

The portable bundle embeds the exact current C/C2/C3 Step-2 engine modules and is source-freshness guarded by CI. This is the preferred XI path because it removes the common missing-checkout / missing-import failure mode.

Only if the portable bundle itself fails self-check after exact-current retrieval may XI fall back to the generic multi-file materialization path below.

For `rank` / `audit`, or XI portable fallback, if a matching local checkout is absent, fetch the exact current stage-required files through the repository source and write them into a temporary runnable workspace while preserving relative paths.

### Concrete connector-to-runtime recipe

When operating in ChatGPT with a connected GitHub source and a separate Python/container runtime:

1. query the connected GitHub source for `acchtt/SlipTrace` current `main` SHA;
2. for XI, fetch/write `xi_portable.py` first and run its self-check;
3. for rank/audit or XI portable fallback, fetch each required source file from that exact SHA through the GitHub connector/API;
4. create the destination directories in the local Python/container workspace;
5. write the connector-returned file text **verbatim** to the corresponding local path;
6. do not require the GitHub connector itself to create a local file;
7. run the relevant portable self-check or `runtime_probe.py`;
8. materialize payload JSON;
9. run the actual stage command.

A connector returning source text is sufficient source access. "The GitHub tool does not automatically download into the container" is a setup detail, not unavailability.

Do **not** use container `git clone` as the primary availability test. Raw container networking may be intentionally isolated even while the connected GitHub source is healthy.

Do not treat "files not local yet" as failure.

Recommended workspace:
`/mnt/data/sliptrace-runtime/<sha>/`

After writing, run:

`python models/football/engine/runtime_probe.py --stage <rank|xi|audit>`

Required success:

`RUNTIME SOURCE PROBE: PASS`

### D. Payload materialization

Write the already-frozen structured payloads into the same workspace.

Payload creation is execution plumbing only. Never change semantic inputs merely to make Python pass.

### E. Actual command attempt

Run the stage command.

Examples:

Rank:
`python models/football/engine/board_triplet_cli.py --c <c.json> --c2 <c2.json> --c3 <c3.json>`

then:
`python models/football/engine/c4_semantic_cli.py --input <c4.json> --c-board <c.json>`

then after replenishment reaches a stop condition:
`python models/football/engine/rank_terminal_status_cli.py --input <rank_terminal.json>`

XI primary:
`python xi_portable.py triplet --c <c.json> --c2 <c2.json> --c3 <c3.json>`

XI session reconciliation primary:
`python xi_portable.py reconcile --input <step2_reconcile.json>`

XI all-model accounting primary:
`python xi_portable.py accounting --input <model_accounting.json>`

XI multi-file fallback only:
`python models/football/engine/decision_triplet_cli.py --c <c.json> --c2 <c2.json> --c3 <c3.json>`

Audit:
`python models/football/engine/cli.py audit --input <audit.json>`

All-model accounting:
`python models/football/engine/model_bet_accounting_cli.py --input <model_accounting.json>`

and when factor calibration is due:
`python models/football/engine/factor_calibration_cli.py --input <observations.json>`

## 3. Stage source manifests

### Rank

Materialize:
- `models/football/engine/cli.py`
- `models/football/engine/adapter.py`
- `models/football/engine/core.py`
- `models/football/engine/competition_reliability.py`
- `models/football/engine/schema.json`
- `models/football/engine/board_triplet_cli.py`
- `models/football/engine/c4_semantic.py`
- `models/football/engine/c4_semantic_cli.py`
- `models/football/engine/c4_schema.json`
- `models/football/engine/capacity_replenishment.py`
- `models/football/engine/capacity_replenishment_cli.py`
- `models/football/engine/rank_terminal_status.py`
- `models/football/engine/rank_terminal_status_cli.py`
- `models/football/engine/model_bet_accounting.py`
- `models/football/engine/model_bet_accounting_cli.py`
- `models/football/engine/runtime_probe.py`

### XI

Primary source:
- `models/football/engine/xi_portable.py` (includes Step-2 triplet, reconciliation, and all-model accounting)

Only if portable self-check fails after exact-current retrieval, materialize fallback files:
- `models/football/engine/cli.py`
- `models/football/engine/adapter.py`
- `models/football/engine/core.py`
- `models/football/engine/competition_reliability.py`
- `models/football/engine/schema.json`
- `models/football/engine/decision_triplet_cli.py`
- `models/football/engine/step2_reconcile.py`
- `models/football/engine/step2_reconcile_cli.py`
- `models/football/engine/model_bet_accounting.py`
- `models/football/engine/model_bet_accounting_cli.py`
- `models/football/engine/runtime_probe.py`

### Audit

Materialize:
- `models/football/engine/cli.py`
- `models/football/engine/adapter.py`
- `models/football/engine/core.py`
- `models/football/engine/competition_reliability.py`
- `models/football/engine/schema.json`
- `models/football/engine/factor_calibration.py`
- `models/football/engine/factor_calibration_cli.py`
- `models/football/engine/model_bet_accounting.py`
- `models/football/engine/model_bet_accounting_cli.py`
- `models/football/engine/runtime_probe.py`

Materialize additional imported files if the current revision adds a dependency. A missing import after materialization is a setup task first, not immediate proof of unavailability.

## 4. Failure-claim evidence gate

A user-visible runtime failure claim is allowed only with a structured record.

Use:

`FOOTBALL_RUNTIME_EXECUTION_RECORD`

with:
- stage;
- repository revision;
- Python probe result;
- repository-source probe result;
- local materialization result;
- XI portable self-check result when stage=xi;
- runtime source probe result when the multi-file path is used;
- exact execution command;
- exact exit code/error;
- remediation attempted.

Examples of valid terminal failure states:
- Python tool and both container Python executables actually failed;
- GitHub connector/source call actually failed and no exact-current Project/Files source exists;
- current source was materialized but remains corrupt/unreadable;
- imports remain unresolved after fetching the missing current-revision dependency;
- exact current revision cannot be established after source probe.

The statement:

`ENGINE EXECUTION FAILED — ATTEMPTED — <exact reason>`

is valid only when the record above exists.

The following user-visible claims are forbidden without that record:
- "Python is unavailable";
- "GitHub is unavailable";
- "the repo is unavailable";
- "the engine cannot be run";
- "I only have GitHub access";
- "there is no local checkout";
- `ENGINE NOT EXECUTED — STRUCTURED INPUT PRESERVED`.

## 5. Recovery before failure

When a command fails:

1. inspect exact stderr;
2. distinguish payload rejection from runtime/setup failure;
3. for XI, if the portable command reports `XI ENGINE CONTRACT REJECTED`, report that exact rejected field/rule — do **not** call it a Python error and do not use runtime-failure fallback wording;
4. for XI, only switch to full multi-file materialization when `xi_portable.py self-check` itself fails after exact-current retrieval;
5. if a fallback source/import file is missing, fetch the exact current-revision file and retry;
4. if `python` command is missing, try the available Python execution surface or `python3`;
5. if container network fails, use the GitHub connector source rather than retrying raw network;
6. if payload validation fails, fix only serialization/contract omissions that are already supported by frozen evidence; never invent evidence;
7. rerun.

A deterministic payload rejection is **not** "Python failed". Report the actual contract rejection.

## 6. Success record

When execution succeeds, record:

`FOOTBALL_RUNTIME_EXECUTION_RECORD`
- `python_probe = PASS`
- `repository_probe = PASS @ <sha>`
- `materialization = PASS`
- `xi_portable_self_check = PASS` for stage=xi, otherwise `runtime_source_probe = PASS`
- `command_execution = PASS`

Then report the stage-specific engine status normally.

## 7. Handoff behavior

Runtime/tool availability is never inherited from a prior chat.

A new chat must re-probe current availability.

A previous:
- Python failure;
- GitHub failure;
- missing checkout;
- engine-not-executed note;

is historical process context only and cannot justify skipping current execution.

## 8. Production authority

This bootstrap changes execution plumbing only.

It does not:
- change Football C predictive rules;
- change C2/C3/C4 rules;
- change existing prospective counters;
- create exposure;
- make Python production authority.
