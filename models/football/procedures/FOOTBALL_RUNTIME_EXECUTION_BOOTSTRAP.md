# Football Runtime Execution Bootstrap

**Status:** MANDATORY EXECUTION PRECHECK  
**Applies to:** any football stage that requires deterministic Python execution, including `/sweep`, `/rank`, `/xi`, and `/audit`  
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

For stage=`sweep`, use the portable Step-0 path first (fresh or
PACKAGING/REPAIR without an existing local checkout):

1. Resolve current GitHub `acchtt/SlipTrace@main` exact commit.
2. Fetch ONLY `models/football/engine/step0_portable.py` at that commit and
   preserve the actual Git blob SHA. Transfer those exact source bytes into
   the currently available Python runtime. No `git clone`, checkout, pip or
   local copy of other source files is necessary.
3. Run `python step0_portable.py self-check` (the embedded source's blob
   hashes and importability are checked against pinned original modules).
   Required success: `STEP0 PORTABLE SELF-CHECK PASS`.
4. For new scope preflight:
   `python step0_portable.py scope --input competition_blocks.json`.
   For a completed, current, externally read-back handoff:
   `python step0_portable.py validate --input STEP0_HANDOFF.json --consumer export`
   then
   `python step0_portable.py package --input STEP0_HANDOFF.json --text AISCORE_FIXTURES_<window>.txt --run-proof sweep_run_proof.json --output AISCORE_FIXTURES_<window>.zip`.
5. Pass only a validated archive to /rank. A provisional handoff, current
   evidence gap or unresolved required competition still blocks packaging
   regardless of portable runtime availability. Do not turn false status
   markers into true.
6. If GitHub connector source is readable but its bytes cannot reach the
   Python tool, the **exact** failure is `SOURCE_TRANSPORT_BLOCKED`. Offer
   the portable single Python file for attachment in the SAME normal chat.
   Never conclude that a ChatGPT Work-mode switch is inherently required.
   GitHub CI tests do **not** prove the current conversation transferred or
   executed source successfully.

### Default /xi source transport (no checkout, no Work switch)

When the active chat can read GitHub through its connector but its Python/container
runtime has no GitHub DNS, **do not retry git clone/curl** or declare the paired
models unavailable. Use the committed GitHub Actions workflow
`.github/workflows/xi-portable-artifact-transport.yml`:

1. Resolve `acchtt/SlipTrace@main` and fetch the current `xi_portable.py`
   and `step2_publication_guard.py` Git blob SHAs.
2. Find a **successful** `XI C+C2 portable verified runtime artifact`
   workflow run whose source blob hashes match current main (PR-head workflow
   artifacts are discoverable through `fetch_commit_workflow_runs`; a squash
   merge produces a different commit SHA, so compare **source blobs**, not only
   the PR head commit ID). Read its `xi-c-c2-portable-verified-source` artifact.
3. Download the artifact using connected GitHub's
   `download_workflow_artifact`. It produces a materialized file in
   `/mnt/data` without requiring direct container network access. Extract
   to a disposable workspace. Validate ZIP integrity, check the SHA-256
   manifests against extracted bytes, and cross-check the extracted XI runner
   and publication guard with the exact current GitHub blobs.
4. **Actually execute** `python models/football/engine/xi_portable.py self-check`
   in this chat's Python runtime. Required `XI PORTABLE RUNTIME: PASS`.
   One successful runtime preflight is reusable within the same pinned source
   revision and chat session. On a new revision recheck source freshness.
5. Run `python models/football/engine/xi_portable.py pair --c c.json --c2 c2.json`
   **once** against the same prospectively frozen input epoch. After an
   independent Airtable write/read-back plus executable quote/status recheck,
   run the exact-current bundled `step2_publication_guard.py` with the
   original pair inputs/receipt and read-back snapshot.
6. If no matching successful artifact exists, request/build a fresh
   source-verifying CI artifact via the existing repo workflow. A stale
   artifact must never become authority. `SOURCE_TRANSPORT_BLOCKED` is
   a technical blocker, NOT a football PASS and NOT permission to reconstruct
   a historical C2 result. Only genuine new data/quote evidence epochs justify
   recomputing the frozen pair; do not burn the available prematch window
   repeating unchanged source research.

The artifact is an executable **source transport**, not a completed decision
or proof of live XI/odds. C2 remains shadow-only; the publication gate, live
quote check and official exposure authorization are still mandatory.

For stage=`xi`, use the portable fast path first:

1. fetch only `models/football/engine/xi_portable.py` from the exact current repository revision;
2. write it to a temporary runnable workspace;
3. run `python xi_portable.py self-check` (or the available Python execution surface);
4. if it passes, use the same file for both atomic C+C2 pair execution and Step-2 reconciliation;
5. do **not** materialize the full engine tree or run the multi-file XI runtime probe on a successful portable path.

Required portable success:

`XI PORTABLE RUNTIME: PASS`

The portable bundle embeds the exact current C+C2 Step-2 engine modules and is source-freshness guarded by CI. This is the preferred XI path because it removes the common missing-checkout / missing-import failure mode.

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

### Verified connector-to-Python source handoff

Use the standalone `models/football/engine/xi_source_handoff.py` helper whenever an actual byte stream from the connected GitHub source can reach Python. Fetch `xi_portable.py` at the *pinned 40-hex main revision* and obtain its Git blob SHA from the same source response. Feed the retrieved UTF-8 file bytes unchanged to the helper's stdin:

```bash
python models/football/engine/xi_source_handoff.py \
  --revision <exact-main-commit-sha> \
  --blob-sha <git-blob-sha-from-fetch> \
  --output /mnt/data/sliptrace-runtime/xi_portable.py \
  < /path/to/exact-connector-source-bytes
```

The helper verifies the Git blob SHA, stages the source in a temporary file,
runs the portable C+C2 `self-check`, and atomically replaces the destination
only on success. Required receipt: `XI SOURCE HANDOFF: PASS`. A wrong SHA,
truncated stream, failed self-check, or unsupported model roster must not
activate a source file. The source's SHA check is a transport integrity check;
the upstream GitHub main revision must still be resolved and pinned separately.

**This helper does not access GitHub or move bytes across disconnected tools.**
First prove that the retrieved connector bytes can actually be fed to Python,
not merely that the connector can display the source text. When separate tools
cannot pass bytes and direct container networking is blocked, record:
`SOURCE_TRANSPORT_BLOCKED — connector source accessible, runtime input stream unavailable`.
Do not misreport `PYTHON UNAVAILABLE`, `GITHUB UNAVAILABLE`, or
`XI ENGINE CONTRACT REJECTED`. Preserve frozen input records and do not
publish a completed Step-2 decision. A GitHub Actions green run validates
the engine and staging implementation, but is not proof of this chat's
connector-to-Python transport.



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
`python models/football/engine/board_pair_cli.py --c <c.json> --c2 <c2.json>`

then after replenishment reaches a stop condition:
`python models/football/engine/rank_terminal_status_cli.py --input <rank_terminal.json>`

XI primary:
`python xi_portable.py pair --c <c.json> --c2 <c2.json>`

XI session reconciliation primary:
`python xi_portable.py reconcile --input <step2_reconcile.json>`

XI active-model accounting primary:
`python xi_portable.py accounting --input <model_accounting.json>`

XI multi-file fallback only:
`python models/football/engine/decision_pair_cli.py --c <c.json> --c2 <c2.json>`

Audit:
`python models/football/engine/cli.py audit --input <audit.json>`

Active-model accounting:
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
- `models/football/engine/board_pair_cli.py`
- `models/football/engine/sweep_intake_evidence.py`
- `models/football/engine/sweep_intake_evidence_cli.py`
- `models/football/engine/step0_handoff_cli.py`
- `models/football/engine/coverage_manifest.py`
- `models/football/engine/capacity_replenishment.py`
- `models/football/engine/capacity_replenishment_cli.py`
- `models/football/engine/rank_terminal_status.py`
- `models/football/engine/rank_terminal_status_cli.py`
- `models/football/engine/model_bet_accounting.py`
- `models/football/engine/model_bet_accounting_cli.py`
- `models/football/engine/runtime_probe.py`

### XI

Primary source:
- `models/football/engine/xi_portable.py` (includes atomic C+C2 Step-2 execution, reconciliation, and active-model accounting)

Only if portable self-check fails after exact-current retrieval, materialize fallback files:
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
- change Football C/C2 predictive rules;
- rewrite historical C3/C4 records;
- change existing prospective counters;
- create exposure;
- make Python production authority.
