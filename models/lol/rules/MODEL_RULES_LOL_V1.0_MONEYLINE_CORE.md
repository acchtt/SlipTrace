# MODEL RULES — LEAGUE OF LEGENDS v1.0 — MONEYLINE CORE

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Generation:** clean major rebuild  
**Market scope:** LIVE MONEYLINE ONLY

## 1. Objective

Estimate the probability that each team wins the current map from the freshest synchronized live state, then compare that probability with the executable live Moneyline price.

The model intentionally does **not** forecast Kill Handicap, Total Kills or Duration.

## 2. Non-negotiable philosophy

- Simple causal state variables beat a large named-gate tree.
- Draft is a prior, not a permanent veto.
- Price is never evidence for the game-state probability estimate.
- Raw kills, total gold, towers, dragons or champion labels are not standalone conclusions.
- Structures are context by default and matter only through demonstrable forward control.
- A loss does not create a new rule.
- Historical records are never rewritten.

---

# 3. Draft Prior

Before using live price, resolve the professional draft prior:

`DRAFT PRIOR = SIDE A / EVEN / SIDE B`

Also state one concrete professional win mechanism for each side.

Use only decision-relevant concepts:

- exact roles and current competitive patch;
- lane priority and jungle/support access;
- first-move/objective setup;
- engage/disengage, target access, protected damage, waveclear and side pressure;
- player-specific professional execution fit where known;
- composition timing/scaling;
- Fearless/restricted-pool context where applicable;
- remaining functional archetypes in restricted-pool Game 2+ states.

Do not emit DIM/PDRL/PML certificates. Their useful content is absorbed here.

Forbidden standalone draft conclusions:

- more scaling;
- more engage;
- more tanks;
- three winning lanes;
- more meta champions;
- generic solo-queue win/pick rate.

## Draft numeric prior

For probability calculation from Team A's perspective:

- `D = +1` if draft prior favors Team A;
- `D = 0` if EVEN;
- `D = -1` if draft prior favors Team B.

Draft is deliberately capped at one small unit so live evidence can override it.

---

# 4. Live State

Score the current synchronized state from Team A's perspective on four continuous variables.

Each variable is one of `-2, -1, 0, +1, +2`.

## 4.1 R — Role-weighted resources

Judge where the useful gold/levels/items are, not only aggregate gold.

- `+2`: broad or decision-critical carry/facilitator advantage that materially changes fights/map access;
- `+1`: meaningful but not dominant role-weighted advantage;
- `0`: mixed/roughly balanced or not decision-relevant;
- `-1/-2`: symmetric opponent advantage.

A kill lead is descriptive unless it created useful role leverage.

## 4.2 X — Realized fight/contact execution

Judge what the teams have actually demonstrated when meaningful contact occurred.

- `+2`: repeated or very strong realization of Team A's fight/pick/turn mechanism;
- `+1`: one clear meaningful realization or consistent execution edge;
- `0`: inconclusive, traded, or insufficient contact;
- `-1/-2`: symmetric opponent execution edge.

Do not count cleanup from the same event as multiple independent mechanisms.

## 4.3 O — Objective access/control

Judge the next compulsory cycle, not objective count by itself.

Include:

- first move;
- vision entry safety;
- objective turn quality/speed;
- dragon/Soul/Elder/Baron schedule;
- side-lane numbers/timing;
- safe-concede/cross-map options;
- whether one side can force the other into bad entry geometry.

`+2` means Team A clearly controls the next compulsory schedule; `-2` means Team B does.

## 4.4 T — Composition trajectory

Judge whether the composition's current timing and future curve make the demonstrated mechanism easier or harder from this state.

Include:

- item/level spikes;
- scaling that is actually reachable;
- side-lane assignment;
- damage/access balance;
- whether the draft's intended mechanism is functioning under current state.

`+2` means Team A's current state plus trajectory materially improves its win path; `-2` means Team B's does.

## Towers/structures

Tower count and tower gold are **context only by default**.

They may influence `R`, `O`, or `T` only if the structure state demonstrably changes forward control through first move, safer vision, side-lane pressure, cross-map terminal threat, base access or equivalent causal effect.

---

# 5. Mechanism Contradiction

Resolve the original draft thesis as exactly one:

- `INTACT`
- `WEAKENING`
- `BROKEN`
- `REPLACED`

Definitions:

- **INTACT:** the original mechanism is still materially functioning.
- **WEAKENING:** evidence has reduced its reliability but not invalidated it.
- **BROKEN:** the expected mechanism is not controlling the game and there is no equivalent replacement for that side.
- **REPLACED:** a clearly demonstrated live mechanism now explains the game better than the original draft thesis.

For the numeric prior use:

- `D_eff = D` when INTACT;
- `D_eff = 0.5 * D` when WEAKENING;
- `D_eff = 0` when BROKEN or REPLACED.

REPLACED does not invert the old draft prior. The new side must earn its probability through live `R/X/O/T` evidence.

## Stable state-change rule

Do not flip a completed-state verdict merely because a later price is attractive or one descriptive statistic moved.

A directional reversal requires a genuine causal change in at least one of `R/X/O/T` or the mechanism-contradiction state.

This replaces the old named PASS-repair/LRO tree.

---

# 6. Probability Engine

From Team A's perspective calculate:

`STATE SCORE S = 1.0*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`

Then:

`MODEL WIN PROBABILITY(A) = clamp(50% + 3*S percentage points, 15%, 85%)`

`MODEL WIN PROBABILITY(B) = 100% - MODEL WIN PROBABILITY(A)`

Round displayed probabilities to the nearest 1 percentage point.

This formula is intentionally small and transparent. It is frozen for the initial validation sample.

## Interpretation

Approximate score map:

- `S = 0` -> 50%
- `S = +2` -> 56%
- `S = +4` -> 62%
- `S = +6` -> 68%
- `S = +8` -> 74%
- `S = +10` -> 80%

The 15–85% clamp acknowledges that screenshot-based live inference should not claim near-certainty.

---

# 7. Probability must be locked before price

Required order:

1. resolve draft prior;
2. resolve synchronized live `R/X/O/T`;
3. resolve mechanism contradiction;
4. calculate both teams' model win probabilities;
5. **only then** inspect/use the offered Moneyline price for value comparison.

If the price was already visible in the screenshot, mentally bracket it and complete the probability estimate without using price movement, favorite/underdog status or payout attractiveness as state evidence.

---

# 8. Price Decision

For decimal odds `O`:

`BOOK IMPLIED PROBABILITY q = 1 / O`

Use raw implied probability for the TAKE rule. This is conservative when the book has margin.

`MODEL EDGE = p_model - q`

## Fixed initial uncertainty buffer

`REQUIRED EDGE = +5.0 percentage points`

Derivation: one meaningful classification step in the live scoring engine changes win probability by roughly 3–4.5pp depending on the variable. A fixed 5pp requirement is therefore approximately one major state-classification error of protection while v1.0 is uncalibrated.

This single buffer replaces legacy family/phase/late-game gate stacks.

## TAKE CANDIDATE rule

A team is TAKE-eligible only when all are true:

1. live Moneyline market is executable and synchronized to the assessed state;
2. decimal odds `>= 1.60`;
3. model probability was estimated before price was used as evidence;
4. `MODEL EDGE >= +5.0pp`;
5. position-blind reassessment completed;
6. evidence is fresh and internally consistent;
7. actual exposure remains 0u;
8. no chasing/martingale/rescue/stake escalation.

If both sides are shown, price both only after both probabilities are locked.

## Examples

- odds 1.60 -> book implied 62.5%; model must be at least 67.5%.
- odds 2.00 -> book implied 50.0%; model must be at least 55.0%.
- odds 2.94 -> book implied ~34.0%; model must be at least ~39.0%.

---

# 9. Verdict Semantics

Use only:

### `HOLD`

Evidence/market state is incomplete, unsynchronized, stale, contradictory, or not yet sufficient to score responsibly.

HOLD is **not** a discretionary extra-confirmation layer.

### `PASS`

The state is usable, but no executable side clears the fixed price/edge requirement, or a hard execution control fails.

### `TAKE CANDIDATE`

A side clears the model and price rule. It is not yet a Position.

Then set:

`USER_LINE_CONFIRMATION = PENDING`

Only explicit user confirmation that the quoted line/odds still exist may create a Position.

If the price materially changes, recompute implied probability and re-evaluate before acceptance.

---

# 10. Live-only scope

v1.0 does not issue pregame or immediate-postdraft Moneyline TAKES.

Draft-only analysis may produce a prior and mechanism, but a betting verdict requires synchronized live state.

There is no universal 2-snapshot or 3-snapshot count gate. A single live state can be usable when it contains enough causal information to score `R/X/O/T`; conversely, many screenshots do not help if they add no meaningful causal information.

---

# 11. Execution controls

Hard controls retained:

- active GitHub authority/session lock matches loaded model;
- synchronized evidence;
- executable Moneyline only;
- minimum odds 1.60;
- position-blind reassessment;
- fixed +5pp edge requirement;
- user line-existence confirmation before Position logging;
- shadow testing only, actual exposure 0u;
- no martingale/chasing/rescue/stake escalation;
- no retroactive Position creation without contemporaneous user execution confirmation;
- historical outcome and process validity remain separate.

Kill Handicap, Total Kills and Duration are `RETIRED_FROM_BETTING` under v1.0.

---

# 12. Compact internal certificate

Before `TAKE CANDIDATE`, resolve:

`ML_CORE[D=...;MC=...;R=...;X=...;O=...;T=...;S=...;P=...;BOOK=...;EDGE=...;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`

This is a compact audit record, not a new gate tree.
