# Football Step-2 Session Reconciliation

**Status:** ACTIVE — mandatory Step-2 completeness guard  
**Scope:** Football C official workload; C2 remains shadow-only

## Purpose

Prevent an authorized Step-2 fixture from silently disappearing between the frozen board, XI/odds assessment, deterministic execution and Decision State persistence.

This is a process-integrity guard only. It does not change any Football C/C2 predictive threshold.

## Due set

At the start of each Step-2 session, freeze the due set from the current official C board:

- every `FOLLOW` fixture whose XI/odds decision window is open;
- every `RESERVE` fixture explicitly activated for the session;
- every fixture explicitly reopened by the user as an exception.

C2 never adds fixtures to this due set.

For each due fixture persist:
- `match_id`;
- `official_follow_lane`;
- `step2_authorization = ROUTINE_FOLLOW / RESERVE_ACTIVATED / USER_EXCEPTION`.

## One disposition per due fixture

Every due fixture must end the session with exactly one status:

- `DECISION_STATE_PERSISTED`;
- `WAITING_FOR_USER_XI_ODDS`;
- `FIXTURE_STATUS_BLOCKED`;
- `INTEGRITY_BLOCKED`;
- `ENGINE_FAILED_AFTER_ATTEMPT`;
- `LIVE_REROUTED`.

A started fixture is not a prematch Step-2 decision. Record `LIVE_REROUTED` and continue under the live launcher.

No due fixture may be omitted merely because research, quote availability, timing, or another match consumed attention.

## Deterministic reconciliation

Run:

`python models/football/engine/step2_reconcile_cli.py --input <step2_reconcile.json>`

The session is complete only when:

`STEP2 RECONCILIATION STATUS: PASS`

Any missing due match is:

`STEP2 RECONCILIATION FAILED — SILENT OMISSION`

Any output for an unauthorized fixture is:

`STEP2 RECONCILIATION FAILED — OUTCOME WITHOUT AUTHORIZATION`

## Quote freshness

Immediately before finalizing a prematch Step-2 action, revalidate the user's executable quote.

Required engine field:

`quote_revalidated = true`

If the quote moved/disappeared, update to the new executable quote and rerun the decision. If no executable quote is available, do not publish C-BET.

## Fixture status

Immediately before deterministic decision execution:

`fixture_status = PREMATCH_CONFIRMED`

Started/postponed/cancelled/finished/unknown fixtures are blocked from the prematch Step-2 engine. Started fixtures route to the live workflow.

## Model-specific recheck ownership

The same factual research epoch is shared, but policy rechecks are separate:

- Football C: `completion_rechecked = true`;
- Football C2: `c2_route_quality_rechecked = true`;

Do not satisfy a shadow model by copying Football C's completion-recheck flag.

## Post-XI research trace

Every decision payload must include:

- `post_xi_research_status`;
- non-empty `post_xi_research_note`.

The note records what fresh football information was actually checked after XI confirmation. Market-history lookup does not substitute for this note.
