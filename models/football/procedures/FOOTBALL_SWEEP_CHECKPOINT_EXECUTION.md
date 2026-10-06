# Football Sweep Checkpoint / Resume Control

**Status:** ACTIVE STEP-0 RUNTIME CONTROL  
**Applies to:** fresh `/sweep` and `/sweep resume`  
**Purpose:** prevent long Step-0 sweeps from timing out while preserving complete coverage and deterministic queue construction  
**Checkpoint version:** `football-sweep-checkpoint-v1`

## 1. Core rule

A fresh sweep is a persisted multi-chunk job, not one indivisible chat turn.

Step 0 must preserve exactly the same coverage/integrity requirements, but it must not attempt unlimited external verification before returning.

The execution shape is:

`SOURCE ACQUISITION -> SOURCE-LOCAL DISCOVERY/CLASSIFICATION -> TARGETED VERIFICATION CHUNK(S) -> RECONCILIATION -> PACKAGING`

Every material phase boundary is persisted to the existing `Sweep Runs` row.

If more external verification remains after the current bounded chunk, return:

`SWEEP CHECKPOINT SAVED — /sweep resume`

This is a normal non-terminal state, not a failure and not an incomplete repair.

## 2. Fresh-run checkpoint creation

Immediately after resolving the requested window and stable Run ID:

1. create/update exactly one `Sweep Runs` row;
2. set `Run Status = RUNNING`;
3. set `Checkpoint Version = football-sweep-checkpoint-v1`;
4. set `Sweep Chunk Number = 1`;
5. persist the resolved ICT/UTC window;
6. initialize `Resume Cursor` before expensive acquisition/research;
7. update `Updated At`.

This initialization is the **first side effect of a fresh /sweep**. It must happen before source acquisition, web search, provider probing, or any user-facing progress response.

Do not wait until the final ZIP to create the run record. Do not say that acquisition/reconciliation is pending unless the RUNNING row and initial cursor have already been persisted successfully.

The first cursor is mandatory and must be valid under `sweep_checkpoint.py` with `source_acquisition_state = UNTRIED`. It should identify:

- run_id;
- checkpoint_version;
- phase = `SOURCE_ACQUISITION`;
- source_acquisition_state;
- requested window;
- listing dates;
- source payload hash when known;
- ordered pending verification blocks when known;
- pending verification count;
- retry queue;
- last completed block.

## 2A. Initialization failure / orphan prevention

If the RUNNING row or initial Resume Cursor cannot be persisted, stop immediately with:

`SWEEP START FAILED — CHECKPOINT NOT PERSISTED`

Do not perform acquisition and do not tell the user to `resume`.

If acquisition work somehow begins and a later check discovers that the current invocation has no persisted RUNNING row/cursor, persist the current run/window as RUNNING with the best truthful SOURCE_ACQUISITION cursor **before returning control**. Never leave a fresh sweep in a conversational "continue later" state without a resumable cursor.

A fresh /sweep invocation that returns while work remains must satisfy exactly one of:
- RUNNING + valid Resume Cursor, with `SWEEP CHECKPOINT SAVED — /sweep resume`;
- SOURCE_BLOCKED persisted with its bounded recovery lease;
- COMPLETE persisted;
- explicit `SWEEP START FAILED — CHECKPOINT NOT PERSISTED` before acquisition.

## 3. Resume authority

When the command is `/sweep resume`:

- load the matching `Sweep Runs` row first;
- accept a normal `RUNNING` row or a `BLOCKED` row only when its Resume Cursor is `SOURCE_ACQUISITION / SOURCE_BLOCKED`;
- for a blocked source row, run the deterministic source-recovery lease decision before returning the stored blocker;
- if recovery retry is authorized, set `Run Status = RUNNING` before any provider/source call; if the bounded recovery pass fails, persist `Run Status = BLOCKED` and `Source Acquisition State = SOURCE_BLOCKED` with a fresh lease. **Never write `SOURCE_BLOCKED` into the Run Status single-select.**
- `Resume Cursor` is authoritative for the next unfinished stage/block;
- read persisted Daily Coverage rows for completed work;
- reuse an `ACQUIRED` source epoch when its hash/window is unchanged;
- reuse all completed competition-block preflights from the same source epoch;
- do not reconstruct progress from chat history;
- do not restart broad discovery;
- do not repeat already-completed public-web searches;
- do not allocate a new Run ID.

If more than one resumable sweep exists and no window/Run ID disambiguates, prefer the most recently updated matching `RUNNING` sweep, otherwise the most recently updated matching recoverable `BLOCKED / SOURCE_BLOCKED` sweep. If ambiguity remains material, report the candidate Run IDs instead of merging them.

A plain `resume` in the project should also continue the most recent resumable Step-0 sweep when the preceding active task is clearly Step 0, including a recoverable `BLOCKED / SOURCE_BLOCKED` run whose lease permits a retry.

## 4. Phase model

### A. SOURCE_ACQUISITION

Apply `FOOTBALL_AISCORE_SOURCE_ACQUISITION.md`.

On `ACQUIRED`:
- persist `Run Status = RUNNING` and `Source Acquisition State = ACQUIRED`;
- persist `source_scope = EXACT_DATE_UNIVERSE / BOUNDED_PRODUCTION_DISCOVERY`;
- persist source transport/hash/attempt state immediately;
- set cursor phase = `DISCOVERY_CLASSIFICATION`;
- do not reacquire this source epoch on resume.

If exact carriers fail in FAST_PRODUCTION but the minimum two-source discovery seed is available, persist `ACQUIRED / BOUNDED_PRODUCTION_DISCOVERY` and continue. Do not enter SOURCE_BLOCKED or the recovery lease merely because the exact date page could not be fetched.

On `SOURCE_BLOCKED`:
- use this state only when neither exact acquisition nor the minimum bounded two-source production-discovery seed is available;
- persist `Run Status = BLOCKED` and `Source Acquisition State = SOURCE_BLOCKED`;
- never use `SOURCE_BLOCKED` as the Run Status value;
- persist the blocker/fingerprint;
- persist the source last-attempt timestamp and retry-not-before lease from `FOOTBALL_AISCORE_SOURCE_ACQUISITION.md`;
- return source-blocked for the current invocation.

On a later resume, evaluate the deterministic source-recovery lease before returning the stored blocker. A legacy blocked checkpoint without lease metadata receives one immediate recovery probe; an unchanged blocker may receive one new bounded acquisition pass after the 30-minute lease expires.

### B. DISCOVERY_CLASSIFICATION

This phase is source-local and should be cheap.

From the acquired source scope / discovery seed:
- enumerate senior blocks;
- apply hard-scope exclusions;
- identify protected/required/women blocks;
- group surviving fixtures by stable competition/date block key;
- read Competition Reliability once per unique competition key;
- classify obvious C/D/non-operational blocks where the source + persisted operational evidence already proves they are below A/B;
- build an ordered list of blocks that still require external operational/researchability verification.

Do not perform team-by-team web research during this source-local pass.

Persist the ordered pending block list before external research starts.

### C. TARGETED_VERIFICATION

External research is bounded per invocation.

One **verification block** is one stable competition/date block requiring public-web evidence beyond the acquired date feed.

Per chat invocation:
- verify at most `MAX_EXTERNAL_VERIFICATION_BLOCKS_PER_CHUNK = 6`;
- process blocks in the frozen pending order;
- after block 6, stop even if more remain;
- persist each completed block before opening the next block;
- never start block 7 in the same invocation.

A block may contain many fixtures. The block consumes one chunk slot, not one slot per fixture.

If a block is resolved from source/persisted evidence with no external lookup, it does not consume the six-block external budget.

### D. RECONCILIATION

Enter only when no pending external verification block remains.

Then:
- freeze complete A/B candidate pool;
- assign global `Step0 Capacity Queue Rank`;
- reconcile required competition manifest;
- reconcile women's top-flight manifest/counters;
- run timestamp-collision/boundary checks only where triggered;
- reconcile all normal Step-0 counts;
- verify unresolved=0 for work readiness.

### E. PACKAGING

Create the canonical ZIP only after reconciliation passes.

Then:
- `Run Status = COMPLETE`;
- `Current Stage = COMPLETE`;
- clear `Resume Cursor` or set it to a compact `COMPLETE` terminal record;
- `Pending Verification Blocks = 0`;
- persist final handoff filename/hash/status.

## 5. Competition-block evidence reuse

Evidence acquisition is **competition-block shared**.

The current researchability/operational checks are fixture decisions, but repeated evidence acquisition must be shared inside one competition block.

For one competition/date block, fetch the minimum evidence surfaces needed to establish:
- current competition context;
- recent team evidence for the involved teams;
- mechanism/statistical evidence;
- XI/team-news observability;
- market observability.

Reuse those same fetched surfaces for every fixture in that block when they actually cover those teams.

Do **not** run the same competition standings/form/news search separately for each fixture.

Open a fixture/team-specific source only when the shared block evidence does not cover that fixture's required A/B/C evidence.

The underlying fixture must still receive its own final Step-0 disposition. Evidence reuse changes acquisition cost, not the admission standard.

## 6. Search batching

When multiple pending blocks can be queried independently, batch their public-web searches in the same tool call where supported.

Do not serialize independent searches one-by-one merely because the blocks are processed in a deterministic order.

The six-block budget is a logical verification budget, not a requirement to use six separate tool calls.

## 7. Immediate persistence

After each externally verified block, write enough state that a timeout immediately after that write loses at most the current not-yet-persisted block.

Persist:
- completed fixture dispositions/operational fields;
- block evidence summary/provenance;
- competition reliability snapshot used;
- women/required manifest additions if applicable;
- `Last Completed Block`;
- remaining ordered pending blocks in `Resume Cursor`;
- `Pending Verification Blocks`;
- `Sweep Chunk Number`;
- `Retry Queue`;
- `Checkpoint Notes`;
- `Updated At`.

Do not keep the only copy of a completed block in the assistant's transient context.

## 8. Retry behavior

A transiently failed block goes to `Retry Queue` with compact reason and attempt count.

Do not retry that block repeatedly in the same invocation after the normal per-block verification budget is exhausted.

On the next `/sweep resume`:
- process retry items before new pending blocks when the failure was transient;
- preserve the global two-authoritative-attempt principle where applicable;
- if the block remains unresolved after its allowed attempts, mark the affected fixture/block UNRESOLVED and proceed to reconciliation failure rather than wandering the web indefinitely.

## 9. Chunk completion output

When work remains, return compactly:

`SWEEP CHECKPOINT SAVED — /sweep resume`

Include:
- Run ID;
- chunk number completed;
- phase;
- completed verification blocks this chunk;
- pending verification block count;
- retry queue count;
- current discovered/admitted/excluded/deferred/unresolved counts when available;
- next block key;
- source state/transport.

Do not generate a provisional Work ZIP.

Do not label the sweep BLOCKED merely because it reached the normal chunk boundary.

## 10. Coverage is not weakened

Chunking must not:
- skip women's top-flight fixture accounting;
- skip required competition blocks;
- promote a block based on familiarity alone;
- use predictive attractiveness to choose which blocks are verified;
- let the first 15 discovered fixtures permanently consume capacity;
- package before the full plausible A/B candidate queue is frozen;
- silently drop a pending block because its kickoff is later.

All existing Step-0 completeness rules still apply before `work_ready=true`.

## 11. Time-sensitive pruning

At the start of every chunk/resume, establish current ICT once.

Before external research on a pending fixture/block:
- if every fixture in that pending block has already left the prematch window, close those fixture rows with the appropriate prematch-closed operational disposition;
- do not spend external verification budget on already-started/finished fixtures;
- if only part of the block remains prematch, research only the remaining relevant fixtures while preserving closed rows in coverage accounting.

This prevents a long sweep from wasting later chunks on matches that became unusable while the sweep was running.

## 12. Airtable fields

Table: `Sweep Runs` (`tblUnGHHe0MVaalDL`)

The existing `Current Stage` single-select uses legacy broad stage names. Map the checkpoint phase without changing its option set:
- `SOURCE_ACQUISITION` / `DISCOVERY_CLASSIFICATION` -> `CORE DISCOVERY`;
- `TARGETED_VERIFICATION` -> `CONDITIONAL GATES`;
- `RECONCILIATION` -> `RECONCILIATION`;
- `PACKAGING` -> `PACKAGING`;
- `COMPLETE` -> `COMPLETE`.

The exact modern phase always lives in `Resume Cursor`; do not invent new single-select values.

Existing checkpoint fields:
- `Run Status` — `fldm0iEQqUrfsTqKS`
- `Current Stage` — `fldUT0GEsWas15Ljt`
- `Checkpoint Notes` — `fldjaQNJnFYbaPFqd`
- `Resume Cursor` — `fldNjU7wHklM7T0Bf`
- `Retry Queue` — `fldQyCygdjxIfSk5B`
- `Updated At` — `fldTXdSN9d161pHgM`

Dedicated bounded-execution fields:
- `Checkpoint Version` — `fldtIbv2ppGzwUExs`
- `Sweep Chunk Number` — `flduqxh9DOKdV1A06`
- `Pending Verification Blocks` — `flduhyM3Thjwj3Bqs`
- `Last Completed Block` — `fld8jr7wAWGLhXqXe`

## 13. Cursor shape

Use compact JSON equivalent to:

```json
{
  "checkpoint_version": "football-sweep-checkpoint-v1",
  "run_id": "SWEEP-...",
  "phase": "TARGETED_VERIFICATION",
  "chunk_number": 2,
  "source_acquisition_state": "ACQUIRED",
  "source_payload_hash": "...",
  "source_blocker_fingerprint": null,
  "source_last_attempt_at": null,
  "source_retry_not_before": null,
  "source_recovery_attempt_count": 0,
  "pending_verification_blocks": [
    "competition-key|2026-10-05",
    "next-competition-key|2026-10-05"
  ],
  "retry_queue": [],
  "last_completed_block": "previous-key|2026-10-05"
}
```

The cursor is operational state, not predictive football evidence.
