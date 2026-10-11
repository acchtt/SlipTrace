# Unified Step0 → Step1 production pipeline V3

**Authority:** Current /sweep and /rank for NEW source epochs. Historical
COMPLETE and terminal BLOCKED/ABANDONED artifacts retain their original
semantics. The existing deterministic step0 handoff, package, women's
bounded coverage, required competition manifest, C+C2 board pair and active
Airtable reconciliation remain authoritative validators.

## Why this replaces the old two-chat choreography

A verified fixture and a **verified complete production-scope audit** are
different things. The old pipeline forced all research to wait until full
worldwide discovery, an official ZIP, then another tool/chat stage; the
user repeatedly received no football work while up to 8+ source-backed
matches were already known. V3 makes candidate research a nonpublishing
parallel lane while strict final certification continues.

### Single state machine

`SOURCE_ACQUIRED → PREPARE_RESEARCH (UNOFFICIAL)
 → SEAL_OFFICIAL_STEP0_ZIP → RANK_EXECUTE_C+C2
 → INDEPENDENT_AIRTABLE_READBACK → RANK_VERIFIED`

Terminal source blocks go to `BLOCKED_WITH_EVIDENCE`, never a fake
COMPLETE or a retrospective official board. PREPARE does not bypass
the final source completeness check.

All commands share one script:
`python models/football/engine/sweep_rank_pipeline.py`

## /sweep: 3 bounded operations, no serial Work handoff

1. **Acquire** current senior fixtures using one exact provider/date
   universe or the allowed two-family BOUNDED discovery. Persist the
   source epoch and original start time exactly once in active Airtable.
   Include required competition checks, women's top-flight parity, known
   scope excludes and an explicit source-visible block inventory.
   `FAST_FINISH_V2` remains the 3/5/12/15 minute fail-closed budget.
2. **Prepare immediately after competition-local classification.** Provide
   `schema_version=football-sweep-rank-v3`, original
   `run_id`, `source_payload_hash`, `source_acquisition_state=ACQUIRED`,
   `run_status=RUNNING`, anchored UTC window and real current `at_utc`,
   `coverage_blockers` (explicit array), and the complete available,
   **source-backed canonical A/B queue** with immutable IDs/ranks, source
   URLs, zoned kickoffs, current fixture statuses and A/B grades.
   Invoke:

   `python models/football/engine/sweep_rank_pipeline.py prepare --input sweep_preview.json`

   Result `FOOTBALL_RESEARCH_PREPARED_UNOFFICIAL` gives all eligible
   fixture IDs in one research order, first 8 and standard 12 targets,
   remaining optional through the original 20 cap. The deterministic
   goal-first prescreen uses verified historical match results if present,
   never required bookmaker odds or live/FT data. An evidence-limited
   fixture stays available for research, not auto-PASS. Every preview
   has `official_rank_authorized=false` and `no_bet=true`.
   A source-ID mismatch, unverified provider URL/KO, incomplete candidate
   queue rank or already BLOCKED epoch causes an explicit error. No
   transition from a preview to a signed complete state is allowed.
3. **Seal only after all exact bounded source evidence is ready.**
   Construct the authoritative original
   `football-step0-handoff-v2` from source+coverage readback; call:

   `python models/football/engine/sweep_rank_pipeline.py seal --handoff STEP0_HANDOFF.json --run-proof sweep_run_proof.json --text AISCORE_FIXTURES_*.txt --output AISCORE_FIXTURES_*.zip`

   This invokes existing full `validate_step0_handoff(export)`,
   `validate_run_proof` and atomic canonical ZIP validation. The sweep
   operator must **separately refetch** Sweep Runs, Daily Coverage, the
   independent source/scope/required/women manifests, actual XI/market
   publication evidence where required, and zero-unresolved ledger.
   The seal step does not scrape provider pages or pretend that a
   caller-written run-proof JSON is a successful Airtable readback.
   Mark Airtable COMPLETE only after actual ZIP SHA256 and source
   inventory integrity are verified and saved.

## /rank: one invocation, two models

Use the same original ZIP (no rebuilding or changing Step0 ranks),
the **independently read-back** COMPLETE Sweep Runs row including exact
official ZIP SHA256, C/C2 football research payloads from the same common
evidence epoch and an explicit disposition reason for every A/B queue
member not researched (e.g. kickoff elapsed, budget exhausted or missing
real football evidence). Execute:

`python models/football/engine/sweep_rank_pipeline.py rank --zip AISCORE_FIXTURES_*.zip --sha256 <actual_zip_sha256> --sweep-readback sweep_complete.json --c c.json --c2 c2.json --unranked unranked_reasons.json --at <verified_utc>`

- Fails if ZIP bytes differ from independent saved SHA256, run not COMPLETE,
  any fixture not in frozen Step0 queue, a rewritten kickoff, a
  retrospective prematch rank, missing unranked reason, or more than
  20 matches. It never re-crawls the original source universe.
- C and C2 run **independently together** through
  `board_pair_cli.py`; mismatched common evidence, C-owned factors in C2
  or any execution failure blocks the pair. No C3/C4.
- Emits `C_C2_EXECUTED_AWAITING_INDEPENDENT_AIRTABLE_READBACK` with
  immutable execution digest and all official C FOLLOW/RESERVE/STOP
  results; C2 remains shadow. This is **not yet publication**.
- Use `FOOTBALL_ONLY` match-specific research if quotes are unavailable,
  but do not create executable odds or ask user to provide a price.
  Current /xi remains a single command automatically evaluating only
  genuine currently available prices.

Then persist by immutable Coverage ID into **active**
`appbzxqXYf0lKfD4P` (never archived base), refetch the stored
C/C2 rank, state, supported line, official C lane, immutable
Step0 rank and completed Sweep Runs record independently, and run:

`python models/football/engine/sweep_rank_pipeline.py publish --execution rank_execution.json --readback independent_airtable_readback.json`

Only `C_C2_RANKED_READBACK_VERIFIED` is the official result. The
comparison uses `rank_persistence_reconcile.py` and exact paired
execution hash; it does **not** invent a website push, actual wager,
betting P/L or made-up publication.

## Fail-fast and timing rules

Never delay initial football research for missing unrelated third-party
women's global-exact metadata when a legally bounded source scope and
verified in-scope candidate already exist. Equally, do not certify a
complete global senior source universe from snippets, ignore source-visible
top-flight women's fixtures, drop protected/required competition blocks,
or classify unverified plausible A/B competition blocks as negative
prediction outcomes. A BLOCKED sweep can retain a previously prepared
UNOFFICIAL research schedule but **cannot** be sealed or published.
Expired fixtures stay in the audit ledger and cannot become retroactive
official prematch picks.

The V3 coordinator is deterministic and self-contained for local model
validation; source acquisition and persistence still require the current
provider/Airtable tools in the invoking session. It does not claim
a background scheduler or remote web runner. No auto-restart of an
abandoned or terminal sweep. A new run uses the real current clock
and fresh source epochs.
