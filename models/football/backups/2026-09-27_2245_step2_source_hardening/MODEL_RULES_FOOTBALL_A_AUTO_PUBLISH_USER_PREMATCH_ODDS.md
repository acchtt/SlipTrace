# Football A — Auto-Publish User-Supplied Prematch Odds

**Status:** ACTIVE OFFICIAL PATCH  
**Effective:** 2026-09-19 20:50 ICT  
**Scope:** Normal Chat prematch XI/odds execution and Website Picks persistence  
**Prospective:** Yes, except the immediately preceding still-prematch KR Reykjavík–Víkingur Reykjavík assessment is published under the same evidence epoch because kickoff had not occurred at activation.

---

## 1. User-supplied prematch odds are executable by default

When the user sends a prematch odds screenshot/text for a fixture, treat the displayed line(s)/price(s) as **currently available and executable at that evidence epoch**.

Do **not** ask for a second confirmation that the quoted prematch price is still available.

Do **not** require a separate message such as:

- "take it";
- "publish it";
- "lock it";
- "yes";
- "still available".

The supplied prematch odds themselves are the execution-price authority for that assessment epoch.

---

## 2. Automatic OFFICIAL LOCK publication

When all active Football A gates clear and the final exposure decision is affirmative:

`OFFICIAL LOCK`

or any official subtype such as:

- `OFFICIAL LOCK — HIGH-MARKET ACCEPTANCE`;
- `OFFICIAL LOCK — LIVE DECAY PLAN` where the user has supplied the qualifying current live odds under an active plan/exception;

Normal Chat must immediately:

1. persist the final Decision State;
2. create/upsert the corresponding Website Picks record;
3. use the selected line, user-supplied price, stake, model version, kickoff and assessment timestamp;
4. return the published lock to the user.

No extra authorization step exists.

If the assessment returns only `DIRECT LOCK ELIGIBLE` and no exposure blocker remains, convert the final exposure decision to `OFFICIAL LOCK` in the same assessment and publish immediately.

---

## 3. Prematch only assumption

This automatic availability assumption applies when the user presents the odds as **prematch** or in the normal prematch XI/odds workflow.

If the screenshot is clearly live/in-play, apply the live-state / predeclared-plan / exception rules instead. Do not pretend a live quote is prematch.

If a score, red card, kickoff, or materially different line state is already visible, that creates the relevant live evidence epoch.

---

## 4. No retroactive result-fitting

Do not backfill historical Website Picks after kickoff merely because an earlier assessment would have qualified.

A missed publication caused by the former confirmation step may be repaired only when the match is **still prematch** at the moment this patch activates and the user-supplied quote remains the current evidence epoch.

Historical already-live/finished matches remain audit-only unless the user explicitly asks for a bookkeeping correction that is clearly labelled non-official.

---

## 5. Stake

Unless the user specifies otherwise, use the active standard stake of **1u** for an official lock.

One-exposure-per-match remains active.

---

## 6. Persistence authority

For qualifying prematch decisions:

`USER ODDS SUPPLIED → ASSESS → OFFICIAL LOCK → WEBSITE PICK`

not:

`USER ODDS SUPPLIED → ASSESS → WAIT FOR SECOND CONFIRMATION → WEBSITE PICK`

Required note where useful:

`AUTO-PUBLISHED FROM USER-SUPPLIED PREMATCH ODDS — NO SECOND CONFIRMATION REQUIRED`

---

## 7. Authority

This patch overrides any conflicting wording in:

- `CURRENT_MODEL.md`;
- `02_NORMAL_CHAT_XI_ODDS.md`;
- `FOOTBALL_BETTING_PROCEDURE.md`;
- `FOOTBALL_DECISION_STATE_AIRTABLE.md`.

All football-quality, market-alignment, HMA, upper-tail, B+, exception, live-state, and one-exposure-per-match rules remain unchanged.
