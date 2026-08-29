# LoL v1.0 Moneyline Live Procedure — 2026-08-29

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Model:** LoL v1.0 — Moneyline Core  
**Market scope:** live Moneyline only

## Purpose

Turn synchronized professional League of Legends live evidence into one transparent Moneyline probability estimate and a price decision without restoring the legacy v0.3.58 gate tree.

This procedure implements:
`models/lol/rules/MODEL_RULES_LOL_V1.0_MONEYLINE_CORE.md`.

---

# 1. Before live betting — draft prior only

Once exact draft/roles and material competition context are known:

1. classify `DRAFT PRIOR = SIDE A / EVEN / SIDE B`;
2. state the concrete professional win mechanism for both teams;
3. include Fearless/restricted-pool context where relevant;
4. do not issue a pregame or immediate-postdraft betting TAKE.

The draft prior is compact. Do not emit DIM/PDRL/PML certificates or legacy derivative gates.

---

# 2. Evidence intake

A live assessment needs a usable synchronized game state and an executable Moneyline price from the same decision window.

Preferred evidence can include:

- scoreboard screenshot;
- role CS/items/levels or readable resource distribution;
- kills and assists as context;
- towers/structures;
- dragons/Soul/Elder/Baron schedule;
- current live Moneyline screenshot;
- user confirmation that paired screenshots represent the same live state.

When the user explicitly confirms paired scoreboard/market images are synchronized, capture-time/header/device-clock differences alone do not invalidate synchronization. Internal game-state contradictions still fail closed.

If the state is stale, contradictory, missing decision-critical information, or the market is greyed/non-executable:

`HOLD`

Do not use HOLD merely to ask for arbitrary extra confirmation when the current state is already sufficient to score the model responsibly.

---

# 3. Price-blind probability pass

Even when odds are visible in the same screenshot, complete the analytical estimate without treating price, favorite status, line movement or payout as evidence.

From Team A's perspective resolve:

`D | R | X | O | T | MECHANISM CONTRADICTION`

where:

- `D` = draft prior unit;
- `R` = role-weighted resource state;
- `X` = realized fight/contact execution;
- `O` = objective access/control and next compulsory cycle;
- `T` = composition trajectory;
- mechanism state = `INTACT / WEAKENING / BROKEN / REPLACED`.

Then calculate:

`S = 1.0*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`

`P(A) = clamp(50% + 3*S pp, 15%, 85%)`

`P(B) = 100% - P(A)`

Lock these probabilities before price comparison.

---

# 4. State interpretation

## Role-weighted resources

Ask where the useful gold, levels and completed items sit and whether those roles are the current conversion engines.

Do not allow aggregate gold or current kill count to dominate when the resource distribution says otherwise.

## Realized execution

Ask what has actually happened in meaningful fights, picks, objective turns, defensive resets and first-contact sequences.

One event is evidence; repeated cleanup from that same event is not several independent mechanisms.

## Objective access/control

Identify the next compulsory map cycle and who has the easier path to first move, vision entry, turn, contest, concession, trade or cross-map pressure.

Objective count is not enough by itself.

## Composition trajectory

Ask whether current item/level timings, scaling, side assignments and damage/access geometry make the demonstrated mechanism easier or harder going forward.

Theoretical scaling receives little credit if the team has no credible route to reach or use it.

## Structures

Towers are context by default. Only credit them when they alter forward control: first move, vision depth, side-lane pressure, cross-map terminal threat, base access or an equivalent causal mechanism.

---

# 5. Mechanism contradiction and stable reassessment

For the original draft thesis classify:

- `INTACT`
- `WEAKENING`
- `BROKEN`
- `REPLACED`

A later reassessment may change side or verdict only because a genuine causal state change occurred in `R/X/O/T` or the mechanism state.

Examples of real state change:

- a carry/facilitator obtains a decisive item/level/resource swing;
- a second meaningful fight demonstrates that the original access/defense mechanism is failing;
- Soul/Baron schedule or side-lane state materially changes objective entry control;
- a structure creates actual first-move or terminal cross-map leverage;
- a new live mechanism repeatedly succeeds and becomes more explanatory than the draft prior.

Not sufficient alone:

- attractive price;
- raw tower count;
- one duplicated gold observation;
- one kill without mechanism consequence;
- bookmaker reprice.

This is the v1.0 replacement for HOLD->PASS->opposite HOLD->TAKE oscillation and the legacy LRO/PASS-repair gate tree.

---

# 6. Price pass

After probabilities are locked:

`BOOK IMPLIED q = 1 / decimal_odds`

`EDGE = MODEL WIN PROBABILITY - BOOK IMPLIED PROBABILITY`

Initial frozen requirements:

- decimal odds `>= 1.60`;
- edge `>= +5.0pp`.

Use raw implied probability. Do not add vig-removal machinery during the initial sample.

---

# 7. Verdict

## HOLD

Use only when evidence/market cannot yet support a responsible current-state probability estimate.

Compact form:

`HOLD — [specific missing/contradictory state reason]`

## PASS

Use when the state is usable but neither executable side clears the fixed price rule, or an execution control fails.

Compact form:

`PASS — best ML edge [team] +X.Xpp, below +5.0pp requirement.`

## TAKE CANDIDATE

Use when one side clears every v1.0 ML rule.

Compact form:

`TAKE CANDIDATE — [TEAM] ML @ [ODDS] — model [P]% vs book [Q]%, edge +[E]pp.`

Immediately set:

`USER_LINE_CONFIRMATION = PENDING`

Ask the user to confirm the exact quoted Moneyline/odds still exist.

A TAKE CANDIDATE is not an accepted Position and creates no W/L or P/L.

---

# 8. User line confirmation

### PENDING

No Position record.

### CONFIRMED

If the user explicitly confirms the exact line/odds still exist and no material state change occurred, create the accepted shadow Position under current logging governance.

Default shadow stake during the initial v1.0 validation sample: `0.25u`.

Actual exposure: `0u`.

### FAILED / MOVED

If the line disappeared or materially changed, no Position exists at the old quote.

For a new quote:

1. keep the already locked game-state probability only if no material live state change occurred;
2. recompute book implied probability and edge at the new quote;
3. if the game state changed materially, rebuild the full `D/R/X/O/T/MC` estimate first.

---

# 9. Compact live output format

Use this default visible output:

`ML — [TEAM A vs TEAM B]`

`Draft: [A / EVEN / B] — [one-sentence win mechanism]`

`Live: R [score] | X [score] | O [score] | T [score] | Mechanism [state]`

`Model: A [xx]% / B [yy]%`

`Price: [selection] @[odds] -> book [qq.q]% | edge [±e.e]pp`

`Verdict: HOLD / PASS / TAKE CANDIDATE — [short causal reason]`

For a TAKE CANDIDATE add:

`USER_LINE_CONFIRMATION=PENDING — confirm [TEAM] ML @[ODDS] still exists.`

Keep visible prose compact. The internal `ML_CORE[...]` audit record remains available for logging/review.

---

# 10. Retired markets

Under v1.0, do not issue betting verdicts for:

- Kill Handicap;
- Total Kills;
- Duration.

If those markets appear in a screenshot, they may be ignored as sportsbook context. Do not evaluate them as betting candidates and do not import their old gates into ML.

---

# 11. Position-blind rule

Every new state estimate must be made without trying to defend an existing historical/open shadow selection.

If a v1.0 Position already exists on the same map, reassessment may describe the current state for audit but must not increase stake, rescue, martingale, average down or create a chasing position.

---

# 12. Airtable recording

GitHub controls rules. Airtable remains the canonical historical map/snapshot/position ledger.

- HOLD/PASS may be recorded as snapshots when useful for audit.
- TAKE CANDIDATE with line confirmation PENDING may be recorded only as snapshot/audit evidence, not a Position.
- Only explicit line confirmation creates a v1.0 Position.
- Record `Model = LoL v1.0 — Moneyline Core` for new v1.0 maps/positions.
- Preserve all historical v0.x labels and records unchanged.

For accepted v1.0 Positions, Entry Evidence should include the compact probability record:

`ML_CORE[D=...;MC=...;R=...;X=...;O=...;T=...;S=...;P=...;BOOK=...;EDGE=...;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`

and the user line-confirmation fact.

---

# 13. Rebuild safety

Until `CURRENT_MODEL.md` activates v1.0 and a fresh authority lock freezes the completed stack, no live TAKE may be issued.

Visible status during that interval:

`MODEL REBUILD IN PROGRESS — HOLD`
