# /xi — one match assessment, as before

**Single user command:** `/xi` (or `/xi exception`) handles the
football assessment and, when a genuinely current price is ALREADY
available, the betting-price comparison. The user does **not** need
to choose between `/assess` and `/bet`. Those old aliases may still
work for backward compatibility, but are not required or advertised.


**No extra user step:** one /xi performs both paired football analysis and any supported current prematch price check. Neither an odds request nor a second /bet is required.

## Screenshot-only fixed-quote contract (user override 2026-10-12)

When /xi includes the user's odds screenshot, use its **exact** Asian
total and odds — no bookmaker search for updated/replacement quotes.
The screenshot's actual observation time and the assessment execution
time are **different fields**; do not invent capture time or stamp the
screenshot with execution time. Preserve the original screenshot reference,
bookmaker where shown, score and match minute. Screenshot pricing is a
fixed observation, not continuous real-time availability.

Run C official and C2 shadow independently first, then use
`xi_portable.py xi --c c_football.json --c2 c2_football.json
--screenshot-quote user_screenshot.json`. If complete separately sourced
C/C2 decision contexts already exist, add both `--price-c` and `--price-c2`
to apply the **unchanged** model price rules to the screenshot's quote.
A price-action result on a stale or untimed screenshot is explicitly
`CONDITIONAL ACT/WAIT/PASS`, not a currently executable instruction.
If context is missing, report exact supported lines and no evaluated price
action. For live screenshots use displayed score/minute and no retrospective
prematch pricing. Never request fresh bookmaker odds to finish an /xi.
For executable prematch pricing the observed open offer, capture instant,
assessment instant and both genuine revalidated model contexts must align;
normal strict price gates remain mandatory.

Every screenshot assessment sets `model_bets_created=false`. Airtable
`XI Assessment Execution Status` uses existing `EXECUTED_C_C2_FOOTBALL_PRICE_BLOCKED`
for conditional/blocked screenshot pricing, or
`EXECUTED_C_C2_FOOTBALL_AND_PRICE` for strictly verified execution.
Append the exact `USER_SCREENSHOT_ONLY_JSON=` evidence receipt to the existing Airtable `Evidence Summary` field (`fldzt02UGXPWnzqgT`), retaining other football notes. `xi_assessment_reconcile.py` independently verifies the refetched `evidence_summary` and its field ID against the actual screenshot quote, capture time, assessment epoch, bookmaker, score/minute, source reference and limitations. Independently read back the original C/C2 results and quote evidence;
never create Actual Bets from the model's ACT.

## What the user sees

Immediately give the model-specific football read, C official and C2
shadow: `FOCUS` / `CAUTION` / `AVOID` (or `NOT ENOUGH FOOTBALL
EVIDENCE` when the football basis truly is absent), a short why,
and current goal-burden/continuation risks as supported.

If a current, source-backed Asian Over line AND odds were supplied or
independently verified **for this exact match and current epoch**, also
evaluate that **actual offered price automatically within the same
/xi response**. Give the familiar `ACT`, `WAIT`, or `PASS` price
verdict where deterministic C/C2 rules authorize one. C2 is always
shadow-only; ACT never means a bet was placed.

If no genuine usable bookmaker quote is available, **do not ask the
user to get a quote**. Finish the football read and simply say
`No bet price checked`. Do not invent a line, odds, ACT or reachable
WAIT target. Do not chase current bookmaker screenshots or block the
football assessment on price research.

For a match already STARTED, apply the same immediate football-first
behavior using score, minute and material events; a current live
quote is optional. If present, a live actionable price requires the
separate existing live-bet authorization (never reuse a pre-KO
decision or stale price). Missing live quotes never block the read.

## Current V4 /xi execution — football ALWAYS first

For every current /xi, independently freeze C and C2 football inputs
(`stage=football_assessment`) from the same real fixture/clock/event epoch.
Run:

```bash
python models/football/engine/xi_portable.py xi --c c_football.json --c2 c2_football.json
```

If real, current prematch offered odds **already** exist and the strict
XI/tournament/price facts are independently verified, add
`--price-c c_priced.json --price-c2 c2_priced.json` to the same /xi run.
A failed priced pair returns `FOOTBALL_ASSESSED_PRICE_CHECK_BLOCKED`
**without erasing** the independent executed C and C2 football results.
The old `stage=decision` entrypoint without separate football inputs
is a LEGACY_PRICE_ONLY path and must never be presented as an executed
football-first read. Started/HT fixtures assess football first; their
prematch price path is explicitly blocked and live betting requires
a fresh authorized live epoch.

Routine V4 eligibility takes actual original
`V4_SWEEP_READY` plus executed C/C2 rank and independently
read-back `V4_RANK_PERSISTENCE_VERIFIED` into
`step2_queue_guard.py` mode `V4_ROUTINE`. No V1–V3 ZIP/work_ready
requirements. A user-declared exception may use `EXCEPTION_ONLY`
without a V4 board but still requires genuine **independent**
C and C2 football evidence. Missing C2 is INCOMPLETE, not made up.

New active Airtable `Decision States` field
`XI Assessment Execution Status` (`fldkjs6Sykivp0fag`)
records quote-free C/C2 success explicitly without changing the
historic `Engine Execution Status` enum. Independently re-fetch BOTH
`Engine C Result` and `Engine C2 Result` and verify with
`xi_assessment_reconcile.py`. The old priced publication guard remains
mandatory for executable priced decisions; it is NOT a football-only
read requirement. User Actual Bets remain confirmed-slips only.

See current concise launcher `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md`
for exact workflow; former long Step-2 coordinator is audit-only.

## Historical compatibility aliases (non-authoritative for new /xi)

Run `python models/football/engine/xi_portable.py xi --c <c.json>
--c2 <c2.json>`.

- `stage=football_assessment`: ordinary quote-free C+C2 football.
  No quote fields, no accounting, no Website Pick; valid before and
  after kickoff.
- `stage=decision`: existing **prematch only**, strict paired C+C2
  price evaluation; requires real current quote and independently
  verified XI, market, incentive, and publication facts.
- Both inputs must use the same stage, same match, frozen source and
  current evidence epoch. Never copy C's model factors into C2.
- If valid current odds are supplied but the price/market/lineup
  execution gate cannot be proven, still deliver the quote-free
  football result and explain briefly that no executable bet has been
  verified. Do not force users to supply another price to complete
  their requested football read.

The original `football-pair`, `assess`, `pair`, and `bet-check`
engine subcommands remain backward-compatible implementation aliases.
They are not additional commands users need to learn.

## Response style

Lead with a short answer such as:

`C: FOCUS — two goal routes intact. C2: CAUTION — third-goal
continuation less reliable. No bet price checked.`

Or, when genuinely current odds exist:

`C: ACT O2.75 @1.80 (price verified). C2: PASS (shadow).
Both football reads: ...`

Use these as formatting EXAMPLES, never as invented fixtures, goal
claims, prices, approvals or outcomes. Full frozen provenance and
engine status remain available for technical/audit views, not default
user-facing clutter. No extra form, jargon or mandatory screenshots.

**Scope:** workflow routing only. No changes to C/C2 model thresholds,
frozen historical boards, sweep, source checks, user Actual Bets or P/L.
