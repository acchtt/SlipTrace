# Football deterministic engine

**Active production roster:** Football C official + Football C2 shadow.

The engine validates structured football decisions deterministically. Football C remains production authority; Python never creates official exposure by itself.

## Active Step-1 board execution

Create independent C and C2 board payloads from one frozen common evidence epoch, then run:

`python models/football/engine/board_pair_cli.py --c c.json --c2 c2.json`

Required:
- `EXECUTED_C_C2_BOARDS`;
- same ranked eligible universe;
- `common_evidence_reconciled = true`;
- no Football C completion-policy leakage into C2.

Football C controls FOLLOW / RESERVE / STOP. C2 is comparison-only.

## Active Step-2 execution

Primary portable runtime:

`python xi_portable.py self-check`

then:

`python xi_portable.py pair --c c.json --c2 c2.json`

Required:

`EXECUTED_C_C2_PAIR`

The pair must share one frozen common evidence epoch while preserving independent model-owned supported line/state fields.

Multi-file fallback:

`python models/football/engine/decision_pair_cli.py --c c.json --c2 c2.json`

A C-only completed exception is invalid.

## Step-2 session reconciliation

Run:

`python xi_portable.py reconcile --input step2_reconcile.json`

or the documented multi-file fallback.

Every due FOLLOW, activated RESERVE and user exception must end with exactly one disposition.

## Active model accounting

Current new accounting payloads contain C and C2 only.

Run:

`python xi_portable.py accounting --input model_accounting.json`

or:

`python models/football/engine/model_bet_accounting_cli.py --input model_accounting.json`

Expected current roster:

`ACTIVE_C_C2`

Accounting precedence:

`DIRECT BET > COUNTABLE WAIT > WATCH > NONE`

Only Football C may create official exposure / Website Picks.

## Runtime probes

For execution-required stages run:

`python models/football/engine/runtime_probe.py --stage <rank|xi|audit>`

Do not infer engine/repository unavailability from a missing local checkout or raw container network failure.

## Football C selection layer

Football C ranks prospectively from the frozen evidence object. Current FOLLOW certification is stricter than FOCUS classification.

For burdens requiring a clearing third goal:
- strong carrier production alone is insufficient;
- a merely usable second route does not automatically fund goal three;
- continuation, completion and stall/control risk must support the burden.

C2 retains its independent route-quality ranking/selection-floor policy.

## Retired engine artifacts

C3 and C4 are retired from new/current execution.

Historical C3/C4 specifications and frozen records may remain in the repository as **historical source only**. The old triplet runners and C4 executable/compiler artifacts were removed from the active tree and remain recoverable from Git history:
- they are not imported by the active runtime;
- they are not in `runtime_probe.py` active manifests;
- they are not required by current CI;
- they must not be used to create a new decision;
- historical records must not be replayed/backfilled with FT/current evidence.

Git history preserves the exact executable source used during retired-model eras.

See:

`models/football/retired/RETIREMENT_MANIFEST.md`
