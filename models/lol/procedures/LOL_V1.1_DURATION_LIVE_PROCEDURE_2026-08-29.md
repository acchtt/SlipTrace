# LoL v1.1 Duration Live Procedure — 2026-08-29

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Model family:** LoL v1.1 Duration Core  
**Market scope:** live Duration Over / Under

## Purpose

Implement `models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md` with a compact, symmetric live workflow.

Historical v0.x Duration procedures may be consulted for audit/research only. Do not execute DOVC/FCR/FRP or the old PRE_TAKE gate tree under v1.1.

---

# 1. Required evidence

A Duration assessment needs a synchronized current map state with enough information to estimate:

- current game clock `t`;
- net conversion velocity `V`;
- compulsory-cycle spacing `Q`;
- terminal path depth `H`;
- terminal trajectory `T`.

For a betting verdict it also needs an executable Duration side/line/price from the same decision window.

Useful evidence includes:

- scoreboard/current clock;
- current structures and inhibitors/base access;
- Baron/Elder/Soul and next objective timing;
- meaningful recent conversion attempts or failed conversion/reset windows;
- role/item state where it changes siege, engage, waveclear, disengage, side pressure or terminal defense;
- current Duration line and odds.

If the state is stale, contradictory, the clock/line is unclear, or the market is not executable:

`HOLD`

There is no fixed 2-snapshot requirement.

---

# 2. Final-time estimate comes first

Before using the offered line or odds as state evidence:

1. convert the current clock to decimal minutes `t`;
2. score `V/Q/H/T` on `-2..+2`;
3. calculate:

`R0(t) = max(5.0, 31.0 - t)`

`ER = max(2.0, R0 - 1.5*V + 1.0*Q + 1.0*H + 0.75*T)`

`F = t + ER`

4. lock `F`.

If a screenshot already displays the Duration line and odds, bracket them mentally until `F` is locked.

---

# 3. Score the four Duration variables

## V — Net conversion velocity

Ask: when meaningful pressure has existed, how quickly has it become serial map/base progress?

- positive = faster closure;
- negative = demonstrated slow/stalled conversion;
- zero = absent opportunity, mixed or inconclusive.

Do not score `V < 0` merely because kills/towers are low. There must be evidence that a meaningful conversion window actually consumed clock or reset without the expected terminal progress.

## Q — Compulsory-cycle spacing

Ask: how soon does the next forced decision point arrive and can it plausibly create a terminal branch?

Use actual dragon/Soul/Elder/Baron respawn/timing, resets, side assignments and map access rather than objective count alone.

## H — Terminal path depth

Ask: how many real layers remain before a plausible Nexus finish?

Count structures/base access causally, not cosmetically. A 0–0 tower state early can imply deeper terminal path through `H`, but it does not prove stalled conversion through `V`.

## T — Terminal trajectory

Ask: do current items/compositions/assignments make repeated close attempts easier or harder over the next several minutes?

Theoretical waveclear/disengage can inform `T`, but champion labels without state-supported usability should not receive maximum delay credit.

---

# 4. Convert estimate to line probability

After `F` is locked, read line `L`:

`M = F - L`

`P(OVER) = clamp(50% + 7*M pp, 15%, 85%)`

`P(UNDER) = 100% - P(OVER)`

Price both sides from this same estimate when both are executable.

If an exact-time settlement rule could produce a material push and the sportsbook rule is unclear, `HOLD` until settlement semantics are known.

---

# 5. Price pass

For selected decimal odds `O`:

`BOOK IMPLIED = 1/O`

`EDGE = P_SELECTED - BOOK IMPLIED`

Duration initial frozen requirements:

- odds `>=1.60`;
- edge `>=+7.5pp`.

Use raw implied probability during the initial validation sample.

---

# 6. Verdict format

## HOLD

`DUR — HOLD — [specific missing/stale/contradictory state reason]`

## PASS

`DUR — F [xx.x]m | line [L] | best side [OVER/UNDER] model [p]% vs book [q]%, edge [e]pp — PASS.`

## TAKE CANDIDATE

`DUR — TAKE CANDIDATE — [OVER/UNDER] [LINE] @[ODDS] — F [xx.x]m | model [p]% vs book [q]%, edge +[e]pp.`

Then:

`USER_LINE_CONFIRMATION=PENDING — confirm exact [OVER/UNDER] [LINE] @[ODDS] still exists.`

No Position exists while confirmation is pending.

---

# 7. Compact visible state line

When useful, show:

`Clock [t] | V [x] | Q [x] | H [x] | T [x] | F [xx.x]m`

Add one short causal sentence identifying the main clock driver, e.g. demonstrated serial conversion, delayed compulsory cycle, deep structure path, or usable defensive reset tools.

Avoid long certificates.

---

# 8. User confirmation and moved line

### CONFIRMED

If the user confirms the exact side/line/odds still exist and no material game-state change occurred, an accepted shadow Position may be logged under current governance.

### FAILED / MOVED

If the line disappears, no Position exists at the old quote.

If only line/odds move while state remains materially unchanged:

- retain locked `F`;
- recompute `P(OVER/UNDER)` for the new line;
- recompute implied probability/edge for the new odds.

If state changed materially, rebuild `V/Q/H/T` and `F` first.

---

# 9. Position-blind / anti-chasing

Every Duration estimate is fresh and position-blind.

An existing ML or Duration shadow Position on the same map cannot justify:

- rescue;
- averaging down;
- opposite-side revenge entry;
- martingale;
- stake escalation.

Actual exposure remains 0u under current policy.

---

# 10. Airtable recording

GitHub controls analytical rules. Airtable remains canonical historical map/snapshot/position ledger.

- HOLD/PASS can be stored as snapshots when useful;
- pending Duration TAKE CANDIDATE is not a Position;
- accepted Duration Position requires exact confirmed side, line, odds, entry clock, shadow stake, 0u actual exposure and `DUR_CORE[...]` entry record;
- preserve all historical v0.x Duration positions/results unchanged;
- never relabel a v0.x Duration position as v1.1.

---

# 11. Rebuild safety

Until `CURRENT_MODEL.md` activates the v1.1 stack and a fresh Session Authority Lock freezes an authority commit containing it, Duration betting status is:

`MODEL REBUILD IN PROGRESS — HOLD`
