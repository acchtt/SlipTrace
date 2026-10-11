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

## 3A. User-directed exclusion on resume (standing policy from 2026-10-09)

Before selecting further external verification blocks on `/sweep resume`, apply the explicit scope filter in `models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md`, section **2A**. It excludes domestic competitions from Israel, Kenya, Iraq, Wales and Kuwait, plus **Germany 3. Liga only**, without removing official senior national-team or cross-border continental competitions.

For all discovered rows covered by the user filter, persist existing Airtable `EXCLUDED` scope/screen selections and a `USER_SCOPE_EXCLUDED — 2026-10-09` reason, retaining source IDs, clocks, original research, raw grades and other provenance. These are not operationally unresolved candidates. No additional external verification is needed for their kickoff/ID/market/XI conflicts. Remove entire verification blocks from the pending/retry list only when all **in-scope** rows under that block are user-excluded; if a broad block mixes excluded with retained competitions, keep the retained portion, including non-3. Liga German fixtures. Preserve order for all retained blocks and keep terminal reconciliation last.

Write distinct `user_excluded_verification_blocks` (plus fixture identifiers/counts when available) in the live Resume Cursor and recompute `pending_verification_count` before moving on. User-excluded blocks **do not** count as `completed_verification_blocks` and do not use external verification budget. Do not move their old provisional A/B or C grades into the Work capacity queue, and do not count their known time conflicts as unresolved **actionable** integrity defects. Audit counters still include their source-visible discovery records. The standing user rule applies to **future fresh** sweeps as well as this resumed run.

### Prospective tighter XI/market admission when resuming the paused Oct-09 sweep

The user requested fixing the intake quality of the still-unfinished `SWEEP-20261009-1300-20261010-0300`, but instructed the sweep to remain paused for now. **No present Airtable mutation or source reacquisition.** On explicit next resume, preserve the source epoch/hash, completed/pending verification blocks, original historical grades and the LEGACY initial/replenishment budget. Before global Work capacity is frozen, run `FOOTBALL_XI_MARKET_FIRST_INTAKE.md` on every plausible A/B fixture and persist `strict_intake_policy=XI_MARKET_FIRST_V1` in final Step0 handoff. No upcoming matchday XI confirmation is required during an entire-day /sweep. Instead, require verifiable future XI publishing channels, near-KO recheck, and current fixture-specific Asian total; B/UNCERTAIN is conditional when properly evidenced. Unsupported channels are excluded after bounded screening, not invented into B. This is prospective pre-handoff correction, not retroactive frozen-board reclassification.

## 4. Phase model

### A. SOURCE_ACQUISITION

Apply `FOOTBALL_AISCORE_SOURCE_ACQUISITION.md`.

On `ACQUIRED`:
- persist `Run Status = RUNNING` and `Source Acquisition State = ACQUIRED`;
- persist `source_scope = EXACT_DATE_UNIVERSE / BOUNDED_PRODUCTION_DISCOVERY`;
- persist source transport/hash/attempt state immediately;
- for `BOUNDED_PRODUCTION_DISCOVERY`, persist the full frozen `discovery_seed_manifest` in the Resume Cursor and dedicated Sweep Runs field before leaving SOURCE_ACQUISITION;
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

### New 15-minute fast sweep default (prospective 2026-10-11)

**Fresh production runs must use `verification_policy=FAST_FINISH_V2`.**
All existing FAST_FINISH_V1 runs keep their original 60-minute clock
and two-attempt budget; the paused non-fast legacy run remains unchanged.
Do not change an in-progress source epoch's original start/deadline.

Operational stage budget measured ONLY from the initial frozen UTC start:
- 0–3 minutes: acquire exact source or freeze two independent bounded families;
- 3–5 minutes: classify and persist fixture evidence & required/protected/women block inventory;
- 5–12 minutes: verify outstanding source-backed identity, KO, expected league publication, required/protected and women scopes; at most eight logical blocks per selector call, batched up to four concurrent independent lookups, one bounded source verification attempt per failed block;
- 12–15 minutes: offline completeness reconciliation, independently read back Airtable, run native Step0 validators and package only if all mandatory evidence truly exists.

The budgets are **maximum stage gates**, not permission to skip validation,
promise that an incomplete sweep will be accepted, or hold the user
for fifteen minutes. Stop as soon as enough verifiable evidence exists.
Cache evidence by **source epoch, competition, season, source family, and
evidence fingerprint**. Read historical league-channel profile/source
from the existing evidence cache once; if it is stale or unrelated, fetch
only the missing competition/date fact. Do not use the source hash as a
cache key across different epochs and do not pretend reuse proves today's
fixture KO/current status.

At every stage entrance, before/after each web batch, on every resume,
and immediately before publishing RUNNING or COMPLETE, run:

`python models/football/engine/sweep_checkpoint_cli.py deadline --input RESUME_CURSOR.json --now CURRENT_ATTESTED_UTC`

For `select` and `advance`, the CLI enforces `--now CURRENT_ATTESTED_UTC`
for FAST_FINISH_V2 and blocks attempts when the stage budget expired.
If it returns a deadline receipt, **persist it**; do not simply abandon
the underlying RUNNING Airtable row. Persist RUNNING/phase/Updated At
after each material stage and batch. At `BLOCKED_TIME_BUDGET_UNVERIFIED`:
persist Run Status BLOCKED, zero pending, the original source/candidate
ledger intact, terminal exact unresolved source/global/required/women/
fixture inventory/validator evidence and a clear reason. No false Work ZIP,
A/B promotion, hidden women's omission, repeated global search, or /resume
loop. If local offline packaging is already fully proven, status
`PACKAGE_VERIFIED_OFFLINE_ONLY` allows only deterministic ZIP validation,
not new external lookups. Terminal closure needs explicit Airtable mutation;
the checkpoint calculator cannot monitor or change database rows while
no sweep invocation is executing.

Only source-backed fixture identities, dates and publications count as
independent verification. A reused scan of nine women's schedules is **not**
proof of the complete in-window AiScore-visible women's universe. If the
provider cannot establish that universe within budget, expose
`GLOBAL_SENIOR_WOMENS_TOPFLIGHT_AISCORE_SCOPE_ATTESTATION` immediately
as an evidence blocker instead of serially opening dozens more leagues.

### Historical 60-minute policy (V1; existing runs only)

### Fast-finish policy for historical FAST_FINISH_V1 runs (2026-10-09)

- Existing V1 cursors retain `verification_policy=FAST_FINISH_V1` and their already frozen `verification_attempt_counts`/`terminal_unresolved_verification_blocks`; V2 is used for brand-new runs only.
- The machine selector allows at most **24 logical externally verified competition/date blocks in one invocation**. Batch independent public-web lookups in groups of at most six concurrent blocks; process their saved outcomes without requesting a separate user `/resume` between groups. This increases logical work capacity, not the number of sequential web calls required.
- Only inspect blocks still plausibly A/B, protected/required, or senior women's domestic top-flight. Close user exclusions, obvious nonoperational C/D and verified empty/out-of-window blocks from the existing source/official evidence without external fixture-by-fixture research. Never invent unsupported C/D judgments or skip known in-scope candidates.
- Persist each completed verification block and corresponding evidence; unsuccessful block attempts must be explicitly returned through `retry_blocks`. On the second recorded unsuccessful attempt, close that verification path as **terminal unresolved**, NOT completed/verified. `RECONCILIATION` with any terminal unresolved in-scope requirement is **blocked**: no `work_ready=true`, no ZIP, no /rank authority, no automatic repeated source search. Give the exact remaining blocker/source conflict instead of a generic resume request.
- Retain the frozen two-family source seed and re-use verified candidate timestamps/IDs. Terminal-window scans search only the unverified part of the requested interval; do not restart broad discovery merely to repeat the sentinel.
- Do not force 24 external blocks when the actual scoped candidate list is smaller; finish classification/reconciliation within the same invocation whenever the requisite evidence exists.

### Hard 60-minute deadline / stale-run closure (2026-10-11)

**Mandatory for existing `FAST_FINISH_V1` checkpoints, including already-saved RUNNING cursors.** This is a wall-clock bound from the original persisted `requested_window.start_utc` or `sweep_started_at_utc`; it is NOT reset by another /resume, URL search, source hash mutation or checkpoint attempt. Check immediately on `/sweep resume`, before the first external source call and after every independent block batch:

```sh
python models/football/engine/sweep_checkpoint_cli.py deadline --input RESUME_CURSOR.json --now CURRENT_ATTESTED_UTC
```

If status is `WITHIN_BUDGET`, process only the bounded finite pending blocks, checkpoint and retry each unresolved block at most twice as already specified. Do not clear/pad missing evidence merely to meet the deadline.

If status is `BLOCKED_TIME_BUDGET_UNVERIFIED`, **stop this sweep immediately**. Persist the returned complete cursor unchanged, with `Run Status=BLOCKED`, `Current Stage=RECONCILIATION`, `Pending Verification Blocks=0`, `Run Status notes=TIME_BUDGET_EXCEEDED_UNVERIFIED`, and original raw Daily Coverage rows/ids/KO, all source URLs, user-scope exclusions, completed profiles and diagnostic hashes **untouched**. The returned terminal unresolved list includes every pending/retried block, including global protected/women coverage and official export validation; it must not be mistaken for verified dispositions. Do not set `complete`, `actionable_complete`, `work_ready`, source scope complete, final frozen source hash, or `Run Status=COMPLETE`. A provisional B-grade fixture does not become an officially ranked A/B fixture just because it was in the first eight. Do not produce or recycle a QA ZIP as the official /rank input. **No further /resume loop** for this source epoch; use a clean fresh source sweep with strictly current KO if future production is needed.

If status is `RECONCILE_NOW`, no pending/unresolved source blocks remain; continue directly to independent Airtable source/required/women/fixture and handoff validation, even when the 60-minute clock has elapsed. If any mandatory proof is absent, report **BLOCKED WITH EXACT EVIDENCE**, not an invented green completion; never restart global source discovery to clear export.

This deadline closes *verification work*, not the 85-row audit ledger or the raw league discovery scope. It is not a blanket 8-match raw cap, and it never authorizes a C/C2 BET/PASS or edits a historical frozen board. If an incoming source contains more than a viable proof budget, prioritize earliest genuine future kickoff and current source verifiability; unresolved source leads are raw-only.

### Legacy verification (existing RUNNING checkpoint)

- Without `FAST_FINISH_V1` or `FAST_FINISH_V2`, verify at most `MAX_EXTERNAL_VERIFICATION_BLOCKS_PER_CHUNK = 6`;
- process in frozen order, persist every completed block, and pause after six if more remain;
- this includes the **user-paused Oct 9 sweep**, which must not be resumed, reset, or silently reclassified by this patch.

A block may contain many fixtures; it consumes one logical slot, not one per fixture. Evidence resolved without a new external lookup does not consume a slot.

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
- set `Resume Cursor` to a COMPLETE terminal record **without dropping source provenance**;
- for bounded-production runs, carry forward `source_scope`, `source_transport`, `source_payload_hash`, `coverage_mode`, `global_raw_exact`, `production_scope_complete`, and the full `discovery_seed_manifest`;
- mirror bounded provenance to dedicated Sweep Runs fields: `Source Scope`, `Production Scope Complete`, and `Discovery Seed Manifest`;
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
