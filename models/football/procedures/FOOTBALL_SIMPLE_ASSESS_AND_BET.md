# Football C + C2 — two simple user actions

**Active from 2026-10-11.** This is the user-facing command authority for
`/xi`, `/xi exception`, `/live`, `/assess`, and `/bet`.
It supersedes contradictory older XI, price, execution and reporting text
**only regarding whether odds are mandatory to analyze football**.

## Assess (DEFAULT; no odds)

ASSESS is the default whenever the user asks to assess a match.

- User says `/xi`, `/xi exception`, `/live`, `/assess`, or
  “assess/reassess/rate/analyze this match”: **ASSESS**.
- Assess C official football and independently C2 shadow football **without
  requesting any bookmaker quote, price, current total or odds screenshot**.
  This applies before kickoff, after kickoff, after goals, and at halftime.
- First use facts already supplied and current verified football status. Use
  original independent C and C2 model evidence; do not manufacture missing
  factors or treat pre-KO hypothetical burdens as live tradable prices.
  If an essential football fact is unknown, still give a qualified football
  read and identify only *that specific football fact*, never odds.
- Execute the pinned engine's `assess` command (alias of
  `football-pair`) with stage=`football_assessment` and no market fields.
  If source factors or engine are genuinely unavailable, state the exact
  limitation, and still give a plainly labeled non-executable qualitative
  read when justified. Never fake paired execution.
- **User-visible output:** quick `C: Promising / Caution / Avoid / Insufficient
  football evidence`; `C2: ...`; brief why; supported goal estimate
  (clearly frozen or current, never an invented price); remaining goal
  burden after a real goal; and status `Football assessed — no bet checked`.
  Explain unresolved rechecks only when material. Do not show internal gate
  jargon, code status, hashes, replay counters or bookkeeping terms by
  default. `Promising` means football evidence only, NOT a BET.
- An assessment is not incomplete merely because prices are missing.
  No user-bet accounting, assumed odds, synthetic WAIT or Website Pick
  is created in ASSESS mode.

## Bet check (ONLY when explicitly requested)

- User explicitly asks `/bet`, `/xi bet`, `bet check`, `can I bet this
  price`, or an equivalent executable price/entry decision: **BET CHECK**.
  Attach a current Asian goal-total line and offered odds (user-supplied or
  independently verified) to authorize a priced decision. Show C official
  BET/WAIT/PASS and independent C2 shadow where engine inputs justify them.
- Start with the football assessment first; **never refuse the football
  analysis** if the price is unavailable. Report:
  `Football assessed. Bet check unavailable — current odds needed.`
  Request only the missing current total/odds to finish BET CHECK.
- Quoted, stale, or invented odds are never silently reused. No retrospective
  prematch bet after kickoff. The old priced portable `pair` remains
  strict and can never substitute for ASSESS, especially after kickoff.
- A BET CHECK result does not mean an actual user wager was placed. Actual
  P/L comes solely from confirmed slips in Actual Bets — Current.

## Internal names (do not show to users unless troubleshooting)

- `xi_portable.py assess` -> existing pinned quote-free `football-pair`.
- `xi_portable.py bet-check` -> existing prematch priced `pair`.
- `EXECUTED_C_C2_FOOTBALL_ONLY` means ASSESS, not BET CHECK.
- Engine evidence, safety, C official / C2 shadow separation and source
  provenance are unchanged. Other specialised tools may retain their names,
  but may not impose priced-decision gates on ASSESS.

## Precedence and QA

1. Route by user's requested **action**, not by the presence of bookmaker
   screenshots or the old “Step 2/XI” launcher name.
2. Current live score/clock is useful football evidence, not a price trigger.
3. Even if a previously frozen match includes a FOLLOW lane, ASSESS is
   still not a BET; continue directly without searching for odds.
4. Test that the old XI phrases `revalidate quote`, `run priced pair`,
   `mandatory current quote` do not override this default. The old
   priced decision requirements remain intact only for BET CHECK.
