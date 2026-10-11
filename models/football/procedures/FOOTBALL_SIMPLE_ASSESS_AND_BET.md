# /xi — one match assessment, as before

**Single user command:** `/xi` (or `/xi exception`) handles the
football assessment and, when a genuinely current price is ALREADY
available, the betting-price comparison. The user does **not** need
to choose between `/assess` and `/bet`. Those old aliases may still
work for backward compatibility, but are not required or advertised.

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

## Internal execution — automatically choose, no extra user step

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
