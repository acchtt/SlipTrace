# 2026-10-06 — Sweep SOURCE_BLOCKED permanent-latch incident

## User-visible failure

A Step-0 sweep remained:

`HANDOFF INCOMPLETE — AISCORE SOURCE BLOCKED`

across repeated resumes because the stored blocker fingerprint was unchanged.

Observed run:

`SWEEP-20261006-1145-20261007-0300`

The workflow correctly avoided repeating the same acquisition loop in one short interval, but the no-repeat rule had no expiry. That turned a transient provider/browser outage into a permanent blocked state even after external source conditions could have recovered.

## Root cause

The source-acquisition contract allowed retry only when a material fingerprint condition changed, such as:
- source window/date;
- procedure/config revision;
- connected browser transport;
- supplied complete payload/cache.

Elapsed time and source recovery were not represented. Therefore an unchanged fingerprint could remain blocked indefinitely.

## Required fix

The no-repeat rule is now a bounded **source-recovery lease**:
- blocked acquisition stores last attempt + retry-not-before;
- unchanged fingerprint is suppressed only for 30 minutes;
- after lease expiry, one bounded source-level recovery pass is allowed;
- changed fingerprint retries immediately;
- legacy blocked checkpoints without lease metadata retry immediately once;
- repeated competition-by-competition reconstruction remains forbidden.

This preserves anti-loop behavior while preventing a SOURCE_BLOCKED run from becoming a permanent latch.

## Regression requirement

Production QA must prove:
1. unchanged blocker inside lease -> no retry;
2. unchanged blocker after lease -> one retry;
3. changed blocker -> immediate retry;
4. legacy blocked checkpoint -> immediate one-time recovery probe;
5. failed recovery creates a new bounded lease.
