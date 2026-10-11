# Football v2 — active Airtable model routing (2026-10-11)

**New model base:** `Football v2 — Active Operations 2026-10-11` (`appbzxqXYf0lKfD4P`).
**Scope:** `/rank`, `/xi`, `/live`, `/audit`, `/report`, Football C and C2 QA, user Actual Bets accounting, website-pick publication, and competition reliability/event updates from the model/audit workflow.

**Exception: /sweep is NOT rerouted.** Preserve the sweep launcher's existing Airtable connection and Step0 tracking, run IDs, checkpoint and original package writes. Do not migrate its Sweep Runs row or change any `00_NORMAL_CHAT_AISCORE_FETCH.md`, sweep CLI, workflow or Step0 transport code as part of this migration. This contract **does not decide** which base the sweep already uses. At the time of verification, sweep run `SWEEP-20261011-0858-20261011-1200` and its fixture coverage records are already in the new base: never force the sweep back to the old one.

## New Step1 lane readback field (2026-10-11)

The existing active `Daily Coverage Ledger` (`tbl20jBW5dfgNnTV6`) now contains
`Step1 C Follow Lane` — field ID `fldR8p7zmjLAvE5bh`, choices
`FOLLOW`, `RESERVE`, `STOP`. Only official C's **executed** paired-board
`follow_lane` is written. For each newly ranked fixture, independently
read this exact cell back alongside the original Coverage ID, immutable
Step0 Capacity Queue Rank and both C/C2 results before a new /rank
publication can be marked complete. Missing lane is a persistence fault;
do not infer it from C FOCUS/WATCH or C2 shadow. Historical frozen records
are not backfilled or reinterpreted.

## Canonical model table routing

| Model/audit table | New table ID | Common operations |
|---|---|---|
| Daily Coverage Ledger | `tbl20jBW5dfgNnTV6` | /rank C+C2 board, ranks/lanes and frozen evidence; /audit reads |
| Decision States | `tblzMyYuDTi1UMd66` | /xi and /live frozen evidence, paired decisions, readback |
| Website Picks | `tblmGd7XwTYbceIiL` | C official pick/WAIT assumptions only, website/readbacks |
| Factor Calibration Observations | `tblCfYuxmc1FfHS76` | /audit source-pinned prospective analysis |
| Competition Reliability | `tbl8ZRExZfMce7lqY` | /audit/model read/write memory; does not reconfigure /sweep |
| Competition Reliability Events | `tblg3uz2Bvz6bcCm9` | /audit append events; /report read |
| Circuit Breaker | `tbl9dGdMToW8shIL5` | C2 shadow/trial circuit breaker (historical shadow-only) |
| Manual Scores | `tbliGfSwMacpnmauM` | /audit and /report verified score read/write |
| Actual Bets — Current | `tblGsnU4Ht0OpmdH8` | actual user bets/P&L authoritative, only confirmed user slips |

**No /rank, /xi, /live, /audit, /report or website/model publisher may write to the old base** `appWyZJjitSBATXAU` or its `tbl...` IDs. That base is historic **read-only** when comparison is explicitly requested. Do not silently fall back to old data on empty new tables. **Sweep Runs** is *not* a model-owned target; use the actual sweep handoff for evidence and do not change the sweep publisher.

The table **field names and types** were compared live between old and new bases. All target tables contain matching named fields/types except that `Actual Bets — Current` has formula-result columns for `Profit VND` and `ROI %`, which must never be directly written by the model. Field IDs differ in every base: **lookup target field IDs dynamically or write by exact target field names; never reuse old field IDs.** Bind `baseId` and `tableId` together from `ACTIVE_MODEL_ROUTING.json`.

## Handoff bridge and safe state transition

1. **/sweep owns Step0**: original source fixtures, rank/identity/disposition and source hash are immutable. Consume its official ZIP plus independent Step0 Airtable/readback proof from the **sweep's own current source**, whichever base that workflow uses. Do not create or modify Sweep Runs from /rank.
2. **/rank writes to the NEW model base**: reconcile by original `Coverage ID` and original `Run ID`/source hash. If a matching `Daily Coverage Ledger` record already exists in the new base, update that **new-base record ID** only. If no matching record exists there, copy the minimum immutable Step0 fixture identity/provenance from the official package to a **new** coverage row and then add C/C2 Step1 output. Do not update a record in the old base just because its Coverage ID matches. Retain original A/B order and deferred evidence. Do not change Step0 status retroactively.
3. **/xi, /live**: resolve current board against the NEW `Daily Coverage Ledger` before assessing; persist paired C official/C2 independent evidence and outcomes to NEW `Decision States`. Use real new-base record IDs and verify the saved assessment/evidence epoch by separate readback. Never use old Decision States record IDs as update targets.
4. **/audit, /report, accounting**: use the NEW Decision States, Website Picks, calibration, reliability and Actual Bets tables. Historical table migration is not implicit; report `NO_NEW_BASE_CALIBRATION_ROWS` if the table is empty instead of claiming no historical model results. The old base can be consulted only for explicitly labeled historical comparisons, with no writes.
5. **User actual-bet P/L**: two original reset-era verified slips are already present in the new Actual Bets table: Shabab Al Ahli–Dubai United −200,000 VND; Al Ain–Al Ittihad Kalba +184,000 VND, total **−16,000 VND**. Do not create duplicate slips, or interpret Website Picks or shadow decisions as actual user placements.
6. **Strict write/readback**: use `airtable/route.py` `resolve_table()` to select the new base and table; for any model/audit write verify target base, target table, new record ID and `Coverage ID` / `Assessment ID` / `Pick ID` / `Actual Bet ID` identity after reading from Airtable. If write/readback is not verified, say `PERSISTENCE_UNVERIFIED`, not `COMPLETE`.
7. **C/C2 only**: C official model, C2 shadow only. C3/C4 fields in the cloned schema are deprecated history and never populated for new live or prospective decisions.

## Operating guardrails and validation

- Active mapping: `models/football/airtable/ACTIVE_MODEL_ROUTING.json`.
- Executable route validator: `models/football/airtable/route.py`. `resolve_table("sweep", ...)` and `resolve_table("rank", "Sweep Runs")` intentionally reject routing.
- Deterministic regressions: `models/football/engine/tests/test_model_airtable_routing.py` ensures all non-sweep endpoints target this base, verifies strict receipt/identity checking, excludes old-base writes and requires user-verified actual bets.
- Active model commands must load and respect this contract **before their first Airtable call**. Recheck table names/schema when Airtable changes; do not treat matching cloned field names as proof that old record IDs exist in new base.
- Audit state recorded 2026-10-11: new base already contains Step0 sweep `SWEEP-20261011-0858-20261011-1200`, Decision States, and the two verified Actual Bets. At initial switch, Website Picks and Factor Calibration Observations in the new base contained no records; this is **not** a mandate to automatically backfill old, unlabeled history.
