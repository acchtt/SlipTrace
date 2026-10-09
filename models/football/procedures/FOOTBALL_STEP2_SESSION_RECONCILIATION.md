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

## Current-session attestation (v2)

Every **new** Step-2 session uses `schema_version = football-step2-reconcile-v2`. The v1 schema is accepted only for an explicitly labelled, historical, non-production replay with `historical_replay = true`; a v1 pass does not authorize a current completed session.

**Do not equate an engine response with persisted Decision State.** After writing a decision, independently read back the Airtable `Decision States` record and populate the `DECISION_STATE_PERSISTED` outcome with `decision_state_snapshot` from the stored fields:

- `match_id`: exact frozen due-set identifier (linked to the Airtable match/fixture identity);
- `record_id`: actual read-back Airtable ID;
- `engine_execution_status = EXECUTED_C_C2_PAIR`;
- `engine_source_revision`: exact 40-hex source commit used for execution;
- `c_action`: stored `C-BET / C-WAIT / C-PASS`;
- `c2_shadow_action`: stored C2 shadow BET/WAIT/PASS action;
- `c_supported_line` and `c2_supported_line`: independently saved quarter-goal burdens;
- `engine_c_result` and `engine_c2_result`: stored JSON result payloads.

The reconciliation validator cross-checks engine actions and supported burdens against those persisted fields. Missing or mismatched C2 results, provisional/incomplete actions, source revision or record IDs are a **hard failure**. A snapshot must be derived from the *actual post-write Airtable read-back*, never merely repeated from the proposed write payload. The deterministic validator checks the supplied snapshot's consistency; the caller remains responsible for proving that the read-back occurred.

For non-decision dispositions use a non-empty `blocker_reason`; `ENGINE_FAILED_AFTER_ATTEMPT` additionally requires `engine_failure_reason`; `LIVE_REROUTED` requires a `live_handoff_reference` to the live workflow. Do not assign `DECISION_STATE_PERSISTED` to an incomplete record merely because its provisional research notes were written.

The v2 result reports both `persisted_decision_count` and `verified_decision_count`. Current completion requires that they match, and that every due fixture is accounted for. No v1 replay result may substitute for this gate.

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
