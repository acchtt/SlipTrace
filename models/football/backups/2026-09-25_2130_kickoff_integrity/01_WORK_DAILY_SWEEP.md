# 01 — Work High Daily Sweep

Read the **upstream/default-branch** `models/football/CURRENT_MODEL.md` from `acchtt/SlipTrace` first and treat it as the version authority. Follow the current official load order and the stage-relevant procedures/rules it declares. Never infer the active model version from this file or from a locally cached repository copy.

## Upstream authority preflight

Before any football research:

1. read upstream `CURRENT_MODEL.md` once;
2. if a local/cached copy disagrees with upstream, **upstream wins immediately**;
3. do not spend Work usage investigating, diffing, or trying to rehabilitate the stale local cache;
4. load only the current upstream stage-relevant files and continue.

A stale local model is a cache fault, not a reason to run on old rules.

Use the attached `AISCORE_FIXTURES_*.zip` as the already-screened, **scope-pruned Work handoff package** produced by Step 0. Do not rebuild the raw fixture universe.

## ZIP handoff intake — mandatory

Before validating football coverage, validate the archive itself.

Required package contract:

- input is a ZIP archive named `AISCORE_FIXTURES_*.zip`;
- the archive contains exactly one canonical `AISCORE_FIXTURES_*.txt` handoff at archive root;
- no nested copy of the canonical handoff may compete with the root file;
- ignore harmless non-handoff metadata only if present, but the normal producer should not create `__MACOSX`, `.DS_Store`, hidden temp files, or duplicate handoffs;
- extract/read the canonical text handoff and treat that inner text as the semantic authority for the board;
- do not treat the ZIP filename itself as proof of date, window, count, or completeness;
- do not research any match until both archive validation and the actionable-completeness preflight pass.

If the ZIP is unreadable, contains zero canonical handoffs, or contains more than one competing `AISCORE_FIXTURES_*.txt` handoff, stop with:

`HANDOFF PACKAGE INVALID — RERUN NORMAL CHAT STEP 0`

Legacy loose `.txt` handoffs are no longer the normal production input. Accept one only when the user explicitly requests legacy compatibility; otherwise request/rerun the ZIP-producing Step 0 flow.

## HARD PRE-FLIGHT GATE — ACTIONABLE COMPLETENESS

Validate the extracted handoff **before any match research or broad web search**.

The handoff must explicitly show all of the following:

- `source = AiScore`;
- requested ICT window/slate is present and coherent;
- `complete = true`;
- `actionable_complete = true`;
- `work_ready = true`;
- actionable senior block audit passed;
- terminal AiScore interval/date verification passed;
- scope/registry audit passed;
- no schedule-integrity unresolved fixture appears in the Work fixture array;
- admitted fixture count matches the actual Work fixture array.

### Raw-audit exception

`raw_audit_complete=false` is **not a Work blocker by itself**.

AiScore may expose youth/reserve/lower/amateur/regional/hard-excluded fixtures through fragmented dynamic snapshots. If Step 0 explicitly records:

- `raw_audit_complete=false`;
- `raw_count_mode=lower_bound`;
- `nonblocking_raw_gaps=[...]`;

and every listed gap is confined to categories already excluded from Work, accept the handoff without trying to enumerate those fixtures yourself.

Work must **not** spend usage investigating non-blocking raw gaps.

### Netherlands Eerste Divisie Jong/U21 intake exception

Effective 2026-09-19 ICT, an admitted official Netherlands Eerste Divisie league fixture must **not** be rejected merely because one or both participants are Jong/U21/reserve-branded. These fixtures are valid NORMAL-lane Work inputs under the competition-scoped sweep exception. This does not admit separate youth/U21/reserve/development competitions, cups, or friendlies.

### Blocking handoff fault

STOP immediately only when the handoff has an **actionable coverage fault**, such as:

- `actionable_complete=false` or missing;
- `work_ready=false`;
- an unverified PRIORITY/NORMAL senior league block;
- an unverified eligible senior continental/cup block;
- an unresolved senior CONDITIONAL block/cheap gate;
- terminal interval/date not checked;
- known potentially actionable senior fixture unresolved;
- scope/count mismatch inside the Work array.

Return only a compact failure such as:

`HANDOFF INCOMPLETE — ACTIONABLE COVERAGE GAP — RERUN NORMAL CHAT STEP 0`

or, where appropriate:

`HANDOFF SCOPE FAULT — RERUN NORMAL CHAT STEP 0`

Do **not**:

- research only part of an actionable senior block;
- publish a provisional Work board when an actionable gap is known;
- search the web for omitted fixtures;
- traverse AiScore yourself;
- try to backfill the missing actionable universe;
- create PRE grades before the gate passes;
- touch Decision States or Website Picks.

## Published board identity — mandatory

After the actionable pre-flight gate passes and **before structural research begins**, assign one stable identity to the entire Work board.

Use a deterministic time-window ID instead of a manually incremented counter so board references remain unambiguous across chats, reruns, and cross-midnight windows.

### Board ID

Format:

`B-STARTDATE-STARTTIME-ENDDATE-ENDTIME`

where dates/times are the exact requested **ICT** window in compact form:

- date = `YYYYMMDD`;
- time = `HHMM` (24-hour ICT).

Example:

`B-20260915-0300-20260915-1200`

Cross-midnight example:

`B-20260915-1800-20260916-0300`

### Board Name

Also create a human-readable display name from the same window:

`15 Sep 2026 · 03:00–12:00 ICT`

For a cross-midnight board, show both dates:

`15 Sep 18:00 – 16 Sep 03:00 ICT`

### Identity rules

- The same exact ICT window always keeps the same Board ID. A rerun/correction of that window updates the same board identity; it does **not** create a new board.
- A materially different requested window gets a different Board ID.
- Do not derive Board ID from model version, fixture count, Airtable record count, chat title, ZIP filename, or archive metadata.
- Board ID identifies the published slate/window; `Coverage ID` continues to identify an individual fixture. Never replace or overload `Coverage ID` with Board ID.
- Freeze Board ID + Board Name into the PRE artifact before Airtable publication.
- Every Airtable row written by this Work board must preserve the Board ID and Board Name. Until dedicated Airtable board fields exist, prefix `Coverage Notes` (or the equivalent non-destructive notes field) with:

  `[BOARD: <Board ID>] [BOARD NAME: <Board Name>]`

  Preserve existing notes after that prefix; do not erase structural evidence.
- Every Work final response must begin with the Board ID and Board Name so later Normal Chat/XI/audit requests can refer to the board directly.

Preferred shorthand in later conversation is the Board ID, e.g. `load B-20260915-0300-20260915-1200`.

## Hard Work-usage boundary

Step 0 Normal Chat owns fixture discovery, scope filtering, cheap league admission, coverage skeleton publication, and ZIP packaging.

Therefore Work must **not**:
- traverse AiScore date pages again;
- run a second fixture sweep;
- search for fixtures omitted from the handoff;
- reconsider low-goal/Finnish/conditional-no-pass/model-quality exclusions;
- fetch opening odds, prematch odds, confirmed XI, or current bookmaker prices;
- spend deep-research usage on matches that Step 0 already filtered out;
- repair `raw_audit_complete=false` when the gaps are explicitly non-blocking;
- infer additional fixtures from filenames or other files in the archive.

Only after the ZIP intake gate and actionable pre-flight gate pass, treat the admitted fixture array as the complete **Work research universe for the model's actionable scope**.

The handoff should already have removed model-quality exclusions, low-goal domestic leagues, Finnish domestic leagues, and conditional-league fixtures that failed/no-data'd the cheap admission gate. **Do not reintroduce those fixtures and do not spend deep research usage reconsidering them.**

Process every fixture that survived into the valid Work handoff with full deep structural research under the current model. Produce and rank the current PRE states, including route-quality and CC+/carrier-ceiling auditing required by the active model.

When the Practical Ceiling Ranking patch is active, every carrier-priority candidate must be explicitly classified as `PRACTICAL CARRIER CEILING — VERIFIED`, `CANDIDATE`, or `UNVERIFIED`. `CARRIER-LED` alone is not rank-positive. Only `VERIFIED` may receive first-order practical 3+ ceiling credit or cross-grade B+ > A2 ranking authority. Persist the carrier-verification label and supporting mechanism in the frozen PRE summary.

Before freezing any `B / PASS`, apply the active PASS Rescue Screen. If at least one route is PROVEN/SUPPORTED, or a plausible class-gap/carrier route exists, explicitly test whether a VERIFIED self-funded 3+ carrier plus compatible opponent failure rescues the fixture to `B+ WATCHLIST / CARRIER-LED`. If only CANDIDATE/UNVERIFIED evidence exists, or a strong current suppression veto remains, keep PASS and persist the specific PASS label from the rescue patch. Do not send a fixture to PASS solely because the second route is weak.

Assign a stable same-window structural rank and supported burden/range to every surviving FOCUS/WATCHLIST candidate, then freeze the PRE artifact and batch-publish the exact frozen state to Airtable Daily Coverage Ledger `tblcl1UAyMqZT6Ub0` in base `appWyZJjitSBATXAU`.

The frozen PRE artifact and every Airtable row written from it must carry the Board ID + Board Name assigned above. Publication remains a copy/upsert of the frozen state; board identity must not trigger a second structural screen.

This stage is price/XI/market-history blind. Do not use downstream Decision States or Website Picks. Do not run opening-odds watch, confirmed-XI review, live, settlement, post-slate audit, or shadow comparison work here.

If the current model contains a later post-XI goal-environment/regime gate, preserve the structural evidence needed for it but do not classify that later regime during PRE unless `CURRENT_MODEL.md` explicitly moves the gate earlier.

Reconcile the complete **Work-admitted actionable universe** once at the end. Publishing is a copy/upsert, not a second structural screen. If Airtable differs from the frozen Work artifact, preserve the Work artifact and report a persistence sync fault.

## Final response

If ZIP intake fails, stop with `HANDOFF PACKAGE INVALID — RERUN NORMAL CHAT STEP 0` and **zero fixtures researched**.

If actionable pre-flight fails, stop with the applicable handoff failure code and **zero fixtures researched**.

If both gates pass, begin with:

`BOARD: <Board ID> — <Board Name>`

Then return: current official model version, number of Work-admitted fixtures processed, PRE counts, ranked FOCUS/WATCHLIST with structural rank + route pair + supported burden, Airtable publish PASS/FAIL, Board ID persistence PASS/FAIL, actionable reconciliation PASS/FAIL, and note `raw_audit_complete=false — NONBLOCKING` when applicable.

Under the current official model, Work remains price-blind and does not assign final execution class unless `CURRENT_MODEL.md` explicitly changes that stage boundary. It must preserve the ranked candidate pool so Step 2 can distinguish `QUALIFIED — WAIT FOR DECAY` from `STRUCTURAL HOLD` without reconstructing PRE or burying a high-ranked qualified candidate.