# Football Step-2 Session Reconciliation

**Status:** ACTIVE — mandatory Step-2 completeness guard  
**Scope:** Football C official workload; C2 remains shadow-only

## Purpose

Prevent an authorized Step-2 fixture from silently disappearing between the frozen board, XI/odds assessment, deterministic execution and Decision State persistence.

This is a process-integrity guard only. It does not change any Football C/C2 predictive threshold.

## Step-1-to-Step-2 authority gate

Use `models/football/engine/step2_queue_guard.py` (input schema
`football-step2-queue-v1`) **before** Step-2 research, and preserve the
generated immutable due/not-due receipt.

Routine mode requires a genuinely COMPLETE and packaged Step-0 handoff,
`work_ready=true`, and terminal Step-1 `EXECUTED_C_C2_BOARDS`
with `common_evidence_reconciled=true`. A discovered or provisional
A/B fixture is **not** an official FOLLOW/RESERVE. In particular, a RUNNING
sweep with no frozen Step-1 board must produce
`QUEUE NOT FROZEN — SWEEP INCOMPLETE` rather than a guessed Step-2 queue.

Feed the entire frozen ranked eligible board, not a manually selected shortlist.
The guard derives due rows only from Football C's official lane. Routine
FOLLOW requires an explicitly open XI window; each activated RESERVE
requires a recorded authorization and a disposition even if its XI window
is not open yet. An explicitly authorized user exception is included
regardless of its board lane, with its exact user-authorization reference.
All STOP, later-window FOLLOW, and inactive RESERVE rows remain visible in
the returned `not_due` manifest.

While a routine sweep/rank is incomplete, `EXCEPTION_ONLY` mode is allowed
for specific user-authorized fixtures only. It must not borrow provisional
board rows, silently activate reserves, invent supported burdens, or claim
that the routine board was completed. The exception still needs independent
frozen C and C2 decision inputs under the separate XI rules.

Required command (source is pinned to the current model revision):

`python models/football/engine/step2_queue_guard.py --input <step2_queue_input.json>`

The queue receipt is an authorization manifest, **not** a betting decision,
not an automatically produced snapshot of Airtable, and not evidence that
an actual user exception has been completed. It must originate from current
source/board reads, with stable fixture IDs, explicit authorization records,
and immutable source/board snapshot references.

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

A started fixture is not a prematch Step-2 decision, **but may still
be assessed immediately**. Run the deterministic
`step2_fixture_transition.py` before sending a STARTED fixture to a
prematch-only C/C2 engine. For a started fixture, transition in the same
session to the live launcher, perform the live evidence/score/quote check
and deliver the appropriate current qualitative football analysis even
if a valid in-play bet cannot be authorized.

Use `LIVE_REROUTED` as the *prematch due-set accounting disposition* and
attach a reference to the actually opened live assessment (not a promised
or hypothetical one). Keep the live assessment's own completeness and
exposure status separate: an uncompleted or quote-pending live action
must never be reported as a completed C-BET/C2-BET, nor erased just
because a `LIVE_REROUTED` audit reference exists. Kickoff alone is never
a reason to refuse a qualitative live assessment.

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

## Prepublication guard for new C+C2 decisions

Session reconciliation remains mandatory after delivery, but does not itself
authorize publication. For all **new** /xi Step-2 decisions, do the following
after atomic C+C2 execution and before showing a final actionable verdict:

1. Persist the proposed Decision State with the exact frozen C and C2
   supported lines and engine results, plus the new Airtable
   `C+C2 Evidence Epoch ID` (field `fldx9NihOIf3Pl6Hn`).
2. Independently read back the record from Airtable and build the
   `decision_state_snapshot` from the stored record fields, **not** from
   the intended write or the raw engine return. Normalize stored C/C2 result
   objects with each model's own frozen `supported_line`.
3. Revalidate fixture status and executable quote, establish the latest
   evidence epoch, and search the new Airtable `C+C2 Publication Key`
   field (`fldrTcDQwCNgAKmgn`) for existing same-fixture/epoch keys.
4. Run `python models/football/engine/step2_publication_guard.py --input <publication_check.json>`.
   The input includes both original frozen model payloads, the exact paired
   engine receipt, source revision, current-epoch truth and the read-back
   snapshot. **Only** `STEP2 PUBLICATION ELIGIBLE` allows publication.
5. Persist `C+C2 Publication Key` from the guard's `publication_key` for
   deduplication, then proceed to user-facing verdict/Website Picks. A
   blocking response means no actionable publication; document the
   blocker/retry under the saved queue. Never backfill old historical rows.

The guard cannot itself confirm that supplied price/fixture flags or
Airtable snapshot actually came from current remote reads. The executing
agent must perform those external checks. If a goal/quote/lineup changes
before publication, abort the old epoch and re-assess lawfully; don't
label the old C2 action completed after the fact.

## Frozen-queue outcome coverage and open-item tracking

At the end of each current session, run the **queue-level** audit after
building the v2 Decision State read-back reconciliation. The audit input
`football-step2-queue-audit-v1` contains both:
- the exact `queue_receipt` returned by `step2_queue_guard.py`;
- the unmodified `reconciliation_input` used for `step2_reconcile.py`.

Run:

`python models/football/engine/step2_queue_audit.py --input <step2_queue_audit.json>`

The audit checks the *entire* frozen due universe against the reconciliation
due set and disposition set. A missing FOLLOW, activated RESERVE or user
exception fails even if a truncated reconciliation alone would pass.
Any changed lane/authorization also fails.

Distinguish three different claims:
- **ACCOUNTED**: every due match has a documented disposition and
  every persisted decision passed independent C+C2 read-back checks;
- **SESSION COMPLETE**: all due matches have verified persisted decisions,
  with zero open follow-ups;
- **ACCOUNTED WITH OPEN FOLLOW-UPS**: outstanding missing XI/odds, fixture
  status, unresolved integrity, engine failure or live handoff remains.
  These are *not* silently treated as completed model decisions.

A `LIVE_REROUTED` entry remains an open follow-up until the separate live
workflow's result can be independently checked; the presence of a handoff
reference alone is not proof of a completed live assessment. Never
retroactively fill missed C2 inputs from live or full-time data.

A current unfinished sweep cannot supply the routine due set. During such
periods only explicitly authorized `EXCEPTION_ONLY` receipts can be
audited, preserving all incomplete statuses. Do not reclassify old provisional
Airtable exceptions as new validated decisions.

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
