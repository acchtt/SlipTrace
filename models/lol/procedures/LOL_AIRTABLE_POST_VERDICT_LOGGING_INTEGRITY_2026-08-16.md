# LoL Airtable Post-Verdict Logging Integrity — 2026-08-16

**Status:** Mandatory active execution procedure  
**Applies to:** LoL v0.3.58 canonical live/shadow workflow  
**Authority:** User instruction after NAVI vs Movistar KOI Game 1 logging omission

## Purpose

Prevent live analysis from silently continuing while the canonical Airtable map/snapshot/position ledger is missing current-map evidence.

This is an execution/data-integrity rule only. It does **not** create a new analytical model version, change any betting threshold, or authorize extra conservatism.

## 1. Verdict remains first

On an active map, the visible verdict must still come before all GitHub, Airtable, or other connector work.

Order:

1. run the full applicable analytical procedure internally;
2. output the compact visible verdict first;
3. only then perform Airtable logging;
4. do not let logging delay the verdict.

No connector call is permitted before the visible active-map verdict.

## 2. Mandatory post-verdict Airtable write

Immediately after each valid live verdict, log the synchronized state to Airtable:

- ensure the current map record exists;
- create the current snapshot record with the observed clock/state/odds and the visible verdict;
- if the verdict is a qualified executable `TAKE`, create the corresponding shadow position immediately after the verdict, subject to the one-TAKE-per-market-family ledger check;
- if the verdict is `PASS` or `HOLD`, **do not create a position**, but still log the snapshot.

A map/snapshot log is not optional merely because no bet was taken.

## 3. Verify that logging actually succeeded

Do not assume a connector call or prior chat successfully logged the evidence.

After the write, verify that the expected Airtable record exists and matches at minimum:

- Map ID;
- snapshot clock;
- kill score/orientation;
- material gold/objective/structure state when available;
- quoted live markets used in the verdict;
- verdict text;
- for a TAKE, exact market family / selection / odds / simulated stake / actual exposure.

Logging is complete only when the expected record is present in Airtable.

## 4. Missing-log recovery

If a later check reveals that a map or synchronized snapshot was not logged:

- backfill the missing map/snapshot from the original user-provided synchronized evidence and original visible verdict;
- preserve the original clock, odds, state and verdict rather than substituting the current state;
- never convert a historical `PASS`/`HOLD` into a position;
- never invent a TAKE, odds, timestamp, result or position that was not actually produced under the live workflow;
- if a valid TAKE was visibly issued and executable but its auto-record write failed, restore only that exact already-issued shadow position after confirming the original line/price/evidence from the chat/ledger context.

Backfill is data-integrity repair, not a new decision.

## 5. Fight-mid-verdict discard

If a material fight/state change occurs while the verdict is being formed and the user says the verdict is discarded:

- the discarded verdict is void;
- do not create a position from it;
- do not log the discarded verdict as the valid decision snapshot;
- wait for a fresh synchronized state/price and reassess from scratch.

## 6. Finals

On a user-confirmed final:

1. settle every open position first;
2. update the final map state/winner/duration/final kills;
3. verify settlement and final-map records exist.

User correction remains authoritative over buggy `Live` / `Final` feed labels.

## 7. Failure handling

Airtable logging failure must not alter analytical thresholds, create an extra confirmation requirement, or delay a qualified TAKE.

Correct principle:

**Verdict first; log immediately after; verify the log; repair omissions faithfully.**
