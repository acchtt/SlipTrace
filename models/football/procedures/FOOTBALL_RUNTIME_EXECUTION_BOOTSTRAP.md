# Football runtime execution

The active football runtime is a **thin shared runtime**.

## Active execution

- V4 /sweep and /rank execute models/football/stages_v4/stage.py.
- /xi executes models/football/engine/xi_portable.py, which imports the real
  core.py, adapter.py and decision_pair_cli.py.
- C is official; C2 is shadow-only.

Normal /xi command:

python models/football/engine/xi_portable.py xi --c c_football.json --c2 c2_football.json

Optional strict price inputs may be added only when they are genuine current
stage=decision payloads.

## No transport bootstrap

No source-transport bootstrap, embedded source bundle, Git-blob repinning or
preflight staging ceremony is part of the active command path.

The GitHub Actions artifact may package the thin runner beside its ordinary
Python dependencies for transfer, but it does not create a second copy of
model source.

## Failure behavior

Attempt the actual required deterministic command.

- If it succeeds, use the result.
- If the structured input is incomplete, report the exact model/input blocker.
- If the actual runtime call fails, report that concrete failure.

Do not infer model results and do not claim runtime unavailability without an
actual failed execution attempt.
