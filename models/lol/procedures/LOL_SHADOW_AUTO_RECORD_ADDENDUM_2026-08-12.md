# LoL Shadow Auto-Record Addendum — 2026-08-12

**Status:** Active procedural override  
**Effective:** 2026-08-12 16:16 UTC+7  
**Scope:** Shadow calibration only while official betting is paused and actual exposure is 0u.

## Rule

A live verdict of:

`TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`

is now **immediately recorded as an open shadow position** when the exact quoted line is visibly active/executable and all normal eligibility/freshness/model gates have passed.

A separate user confirmation message is **not required** for shadow positions from the effective time onward.

## Execution integrity remains mandatory

Auto-record does not relax any execution gate:

- stale/frozen/expired/greyed/disabled/non-clickable lines are not executable;
- the stale-line freshness gate runs before every TAKE;
- exact line and odds shown in the TAKE are the recorded entry;
- if the newest evidence does not establish an active executable quote, default HOLD/PASS / 0u;
- user identification of a frozen/expired quote remains authoritative;
- do not backfill shadow positions from TAKE recommendations made before this addendum unless they were already explicitly confirmed.

## Official betting

This addendum changes **shadow calibration only**. Official/real-money execution remains paused. If official betting is restored, the pre-existing confirmation requirements remain in force unless the user explicitly changes them separately.

## Logging

- Default shadow stake: 0.25u.
- Actual exposure: 0u.
- Record the visible opposite-side price as a fade benchmark when available.
- Reassess open positions position-blind after material state changes.

## Precedence

For shadow-calibration execution, this addendum overrides older language stating that a TAKE is conditional/unrecorded until separate user confirmation.

## Map-end persistence override — 2026-08-26

**Status:** Active immediately for this project/user workflow and supersedes the earlier requirement to write Airtable immediately after a live TAKE.

A qualified `TAKE` still becomes a model-attributed shadow entry at the instant the verdict is issued, but the physical Airtable write is deferred until the map ends.

During the map:

- retain the exact entry in the live/session buffer;
- label it `BUFFERED SHADOW POSITION — pending map-end Airtable batch` when persistence status matters;
- do not call Airtable merely to create or update the entry;
- do not allow tracker work to delay any subsequent live verdict.

At verified map end, batch-write the position together with the material snapshots, final map state, and settlement, then verify the exact Airtable rows before clearing the buffer.

If the market disappears before a qualified TAKE is actually delivered, no shadow entry exists. Never backfill that line after the fact; record only the process/execution miss at map end when relevant.

For this user's live workflow, same-message scoreboard + sportsbook screenshots are presumed synchronized unless there is a substantive state contradiction or the user explicitly marks a frame stale. Bookmaker/header/feed clock differences alone do not invalidate the pair.