# Football A/B — Decay-First Execution / Burden Protection

**Status:** ACTIVE OFFICIAL PATCH  
**Effective:** 2026-09-20 ICT, prospective from commit  
**Applies to:** Football A official track and Model B side-by-side/shadow execution  
**Purpose:** restore the original purpose of predeclared live decay: structural strength identifies the match, but does not grant permission to absorb a worse goal burden.

This patch is prospective. It does not rewrite or backfill earlier bets, settlements, P/L, or completed decisions.

---

## 1. Core invariant

The frozen supported burden is the execution anchor.

`STRUCTURAL QUALITY → SUPPORTED BURDEN → MARKET EXECUTION`

Never reverse this into:

`STRUCTURAL QUALITY → ACCEPT HIGHER MARKET BURDEN`

A stronger A1/A2/CC+ rating means the fixture may remain qualified to wait longer and survive a wider monitoring state. It does **not** automatically justify entering a higher total.

---

## 2. Direct prematch exposure

A direct prematch official exposure is allowed only when:

1. the football/XI thesis remains qualified;
2. market alignment is clear or a football-led override is documented;
3. the selected line is **at or below the chosen supported execution burden**;
4. price clears the active floor;
5. all fixture-specific exposure gates clear;
6. no suppression/compression veto remains.

Line selection remains:

`LOWEST MODEL-SUPPORTED BURDEN → PRICE FLOOR → PRICE AS TIE-BREAKER`

A higher payout never compensates for a higher goal burden.

---

## 3. Current line above supported burden = WAIT, not HMA lock

When the current prematch line is above the supported execution burden:

`QUALIFIED — LIVE DECAY PLAN`

Freeze before kickoff:

- supported execution burden / target line;
- minimum acceptable price;
- current offered line and price;
- dominant failure mode;
- state-integrity cancellation triggers.

The default live-decay target is the **lowest acceptable line inside the frozen supported burden/range**. Do not move the target upward merely because the market is high.

Examples:

- frozen support O2.75, current O3.25 → WAIT O2.75;
- frozen support O3.0, current O3.5 → WAIT O3.0;
- frozen support O3.0–3.25, current O3.75 → target the lowest independently supported line in that range, normally O3.0 unless the frozen record explicitly makes O3.25 the only valid burden.

---

## 4. HMA is no longer an automatic prematch burden-expansion lane

The earlier Football A HMA patch remains useful as an **audit / monitoring-tolerance overlay**, but it may no longer create an automatic prematch official lock above frozen supported burden.

Therefore:

- `DIRECT LOCK ELIGIBLE — HIGH-MARKET ACCEPTANCE` is disabled for automatic prematch exposure;
- +0.25 / +0.50 HMA may document how far a strong fixture can remain monitored without being structurally discarded;
- HMA does **not** change the official entry target;
- if the market stays above supported burden, continue to WAIT;
- if the supported burden appears at a valid price in a clean state, execute;
- if a goal/state change occurs first, the old 0-0 decay target expires and the score epoch must be re-priced under the active state-integrity / early-conversion rules.

High structural confidence keeps the candidate alive. It does not buy a worse line.

---

## 5. Model B participation expansion is also decay-first

When Model B is run side-by-side:

- its +0.25 / +0.50 / +0.75 participation allowances may not create direct prematch exposure above frozen supported burden;
- above-burden Model B candidates become `MODEL B — QUALIFIED LIVE DECAY`;
- they wait for the supported burden rather than consuming exposure at the expanded line.

Model B's exposure cap, when active, applies only to **actual executable exposures**, not to a preallocated rank-first shortlist.

Do not reserve all Model B slots for high-ranked fixtures whose markets are still above burden. Qualified lower-ranked fixtures with supported, protected lines remain independently executable.

Structural Rank orders review. It does not grant burden permission and does not pre-consume an exposure slot.

---

## 6. Price-only wait

If the supported line is already available but price is below the hard floor:

`QUALIFIED — PRICE BELOW FLOOR`

Freeze:

- exact supported line;
- minimum price;
- current price.

If the same line clears the floor before kickoff, it may execute immediately. If kickoff occurs first, a predeclared live price/decay plan may continue only if state-integrity rules allow.

---

## 7. Mandatory suppression re-screen before high-burden execution

Before any supported burden of O3.0+ is executed, explicitly re-screen:

1. recent same-opponent H2H;
2. recent **same-venue** H2H;
3. whether the observed low-total history matches the current failure mechanism;
4. recent conversion stability / route independence.

A suppression signal is not an automatic PASS, but it may:

- reduce the executable burden;
- convert direct exposure into WAIT;
- or produce STRUCTURAL HOLD when it matches the live football failure mechanism strongly enough.

Do not use long-run H2H averages to wash out a recent same-venue suppression pattern.

---

## 8. Interaction with the Sep 19–20 temporary O2.5/O2.75 relaxation

The temporary burden-specific upper-tail relaxation remains active through its declared expiry.

It affects **whether a protected O2.5/O2.75 burden is football-qualified**:

- O2.5 → quality-proven 3+ path;
- O2.75 → robust 3+ path + non-trivial fourth-goal support.

It does not permit entering O3.0+ merely because the market is higher.

Thus the temporary relaxation and this decay-first patch are complementary:

`QUALIFY LOWER BURDEN → WAIT IF MARKET IS HIGHER → EXECUTE WHEN PROTECTED BURDEN APPEARS`

---

## 9. User-facing output requirement

Every Step-2 assessment must show exactly one of:

- `OFFICIAL LOCK`;
- `WAIT — LIVE DECAY`;
- `WAIT — PRICE BELOW FLOOR`;
- `STRUCTURAL HOLD`;
- `PASS`.

For every WAIT, display:

- target line;
- minimum price;
- current line/price;
- cancellation condition.

A WAIT must not silently disappear before kickoff.

---

## 10. Authority / precedence

This patch overrides conflicting language in:

- `MODEL_RULES_FOOTBALL_A_HIGH_MARKET_ACCEPTANCE.md`;
- `MODEL_RULES_FOOTBALL_A_LIVE_DECAY.md`;
- `CURRENT_MODEL.md`;
- the XI/odds prompt;
- the betting procedure;
- Model B participation logic;

only where those sources allowed a stronger structural grade or participation band to justify **direct exposure above the frozen supported burden** or preallocated Model B exposure slots by rank.

All structural grading, market-alignment, price-floor, XI, suppression, early-conversion, one-exposure-per-match, and auto-publish rules remain active unless explicitly overridden here.
