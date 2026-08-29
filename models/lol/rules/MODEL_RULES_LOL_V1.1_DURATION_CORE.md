# MODEL RULES — LEAGUE OF LEGENDS v1.1 — DURATION CORE

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Generation:** v1.1 scope extension  
**Market scope:** LIVE DURATION OVER / UNDER

## 1. Objective

Estimate a central final game duration from the freshest synchronized live state **before using the offered Duration line or price as analytical evidence**, then convert the distance between that estimate and the offered line into Over/Under probabilities and compare those probabilities with executable prices.

This is a clean v1.x Duration model. It does **not** reactivate the v0.3.58 DOVC/FCR/FRP certificate tree or any historical Duration gate stack.

Moneyline remains governed by the unchanged v1.0 Moneyline Core module when `CURRENT_MODEL.md` declares both modules active.

---

# 2. Philosophy

- Estimate clock causality, not descriptive slowness.
- One transparent final-time estimate prices both Over and Under.
- Line and odds do not determine the state estimate.
- Low kills, tied gold, low towers or quiet elapsed time are not automatically slow-game evidence.
- Theoretical waveclear/disengage may inform trajectory only when it is actually usable from the current state; it is not equivalent to demonstrated delay.
- Structures matter directly for Duration only through the remaining terminal path to Nexus, not because tower count is intrinsically bullish for Over or Under.
- No rule is added because of one loss.

---

# 3. Calibration anchor

The initial neutral anchor is **31.0 minutes final duration**.

Calibration basis at activation: the available Airtable sample contained 31 completed LCK maps in August 2026 with usable duration fields. Their median was approximately **30:55**, mean approximately **31:59**, and standard deviation approximately **5.0 minutes**. The model uses 31.0 rather than the higher mean to reduce the influence of long-tail games.

This anchor is frozen for the initial v1.1 Duration validation sample.

For current game clock `t` in decimal minutes, define neutral remaining time:

`R0(t) = max(5.0, 31.0 - t)`

Interpretation:

- before 26:00, a neutral game points toward roughly 31:00 final duration;
- once a game has already survived beyond 26:00, neutral expectation moves with the observed clock and assumes at least about five further minutes absent strong terminal evidence.

There is no arbitrary elapsed-time minimum for Duration betting. Evidence sufficiency, not the clock alone, determines HOLD versus a usable estimate.

---

# 4. Live Duration state variables

Score four variables on `-2, -1, 0, +1, +2`.

Positive values generally add future clock except `V`, where positive means faster conversion and therefore subtracts future clock.

## 4.1 V — Net conversion velocity

How quickly meaningful pressure is currently becoming serial structures/base access/Nexus progress.

- `+2`: repeated or overwhelming conversion; a short terminal cascade is actively demonstrated.
- `+1`: meaningful conversion pressure with a credible near-term serial close path.
- `0`: mixed/inconclusive conversion velocity.
- `-1`: meaningful pressure has converted slowly or reset without terminal progress.
- `-2`: repeated meaningful pressure has been stalled/denied, materially consuming clock.

Do not infer negative `V` merely because nothing happened. **Absent conversion opportunity is neutral**, not demonstrated stall.

## 4.2 Q — Compulsory-cycle spacing

How much clock the next decision-forcing schedule naturally consumes.

- `+2`: meaningful forced reset/spacing before the next decisive neutral or terminal cycle; several minutes are structurally likely to pass.
- `+1`: some meaningful spacing/reset time before the next major forcing point.
- `0`: ordinary/unclear schedule.
- `-1`: decisive compulsory contact/objective is imminent.
- `-2`: a near-immediate compulsory event can plausibly open a terminal cascade.

Objective count alone does not set `Q`; use the actual next schedule.

## 4.3 H — Terminal path depth

How many real map layers remain between current control and a plausible Nexus finish.

- `+2`: deep terminal path; multiple structure/base layers and resets remain.
- `+1`: meaningful structure/base depth remains before a clean finish.
- `0`: mixed/ordinary terminal distance.
- `-1`: base access or a short serial-structure path is already available.
- `-2`: open/exposed base or one realistic conversion sequence can end the game.

Unlike ML, structures can directly affect Duration through `H` because they are literal terminal path length. Do not double-count the same structure effect in both `V` and `H`: `V` is conversion speed; `H` is remaining path depth.

## 4.4 T — Terminal trajectory

Whether current items/compositions/assignments make the next several minutes more likely to extend or compress the game.

- `+2`: strong, state-usable delay/reset/waveclear/disengage/side-pressure trajectory that materially resists terminal conversion.
- `+1`: modest credible clock-extending trajectory.
- `0`: balanced/unclear.
- `-1`: current composition/item state materially accelerates conversion.
- `-2`: strong terminal acceleration: pick/siege/side/engage tools plus state make repeated close attempts unusually easy.

Champion theory alone should not receive `+2`. The current state must make the delay/acceleration mechanism realistically usable.

---

# 5. Central final-time estimate

First calculate expected remaining minutes:

`ER = max(2.0, R0(t) - 1.5*V + 1.0*Q + 1.0*H + 0.75*T)`

Then:

`F = t + ER`

where `F` is the model's central final-duration estimate in minutes.

**Lock `F` before using the offered Duration line or odds as evidence.**

If the line is already visible in a screenshot, mentally bracket it while scoring `V/Q/H/T` and calculating `F`.

---

# 6. Convert final-time estimate to Over / Under probability

After `F` is locked, read the offered duration line `L` in minutes.

`M = F - L`

Then:

`P(OVER) = clamp(50% + 7*M percentage points, 15%, 85%)`

`P(UNDER) = 100% - P(OVER)`

Rationale for the initial `7pp per minute` slope:

- the activation Airtable LCK sample had roughly 5.0 minutes standard deviation;
- around the center of a broad normal-like duration distribution, one minute corresponds to roughly 8pp probability movement;
- 7pp/min is deliberately slightly flatter to avoid overconfidence in an uncalibrated screenshot-based model.

Displayed probabilities may be rounded to the nearest 1 percentage point, but edge arithmetic should use the unrounded estimate when practical.

If sportsbook settlement rules create a material push/void ambiguity at an exact time line and those rules are not known, use `HOLD` rather than pretending Over + Under = 100% under a materially different settlement rule.

---

# 7. Price decision

For decimal odds `O`:

`BOOK IMPLIED q = 1 / O`

Use raw implied probability during the initial v1.1 validation sample.

`EDGE = MODEL PROBABILITY - BOOK IMPLIED PROBABILITY`

Initial Duration TAKE requirements:

- decimal odds `>= 1.60`;
- selected-side edge `>= +7.5 percentage points`.

## Why +7.5pp

A one-step `Q` or `H` classification changes the probability by approximately 7pp; one `V` step changes it by approximately 10.5pp. A +7.5pp requirement therefore protects roughly against one ordinary state-classification step while the model is uncalibrated.

This single fixed buffer replaces the legacy Duration certificate/gate stack.

Price both executable Over and Under sides from the **same locked `F`**. Failure of one side is not evidence for the other; the opposite side qualifies only through its own probability/price comparison.

---

# 8. Evidence sufficiency and verdicts

## HOLD

Use when synchronized evidence is not sufficient to score current `V/Q/H/T`, the current clock/line is unclear, settlement/executability is unclear, or evidence is stale/contradictory.

HOLD is not an arbitrary extra-snapshot requirement.

## PASS

Use when state and market are usable but neither executable Duration side clears minimum odds plus the +7.5pp edge requirement, or an execution control fails.

## TAKE CANDIDATE

Use only when one Duration side clears all analytical and execution controls.

Then:

`USER_LINE_CONFIRMATION = PENDING`

No Position exists until the user confirms the exact Duration side, line and odds still exist.

---

# 9. State-change discipline

A later Duration reversal requires a real change in `V/Q/H/T`, current clock survival, or a newly observed terminal/delay mechanism.

Price movement alone does not change `F`.

If the game state is materially unchanged but only the offered Duration line or odds move, the already locked `F` may be re-used to calculate new Over/Under probabilities and edge for that same decision window.

If a fight, objective, structure/base event, meaningful resource swing, or material schedule change alters the terminal state, rebuild `V/Q/H/T` and `F` first.

---

# 10. Execution controls

Hard controls:

- active GitHub authority/session lock matches the loaded model;
- synchronized live evidence;
- executable live Duration market;
- central final-time estimate locked before line/price is used as analytical evidence;
- decimal odds >=1.60;
- selected Duration edge >=+7.5pp;
- position-blind reassessment;
- user line-existence confirmation before Position logging;
- actual exposure remains 0u;
- fixed shadow stake under current authority;
- no martingale, rescue, chasing, averaging down or stake escalation;
- no retroactive Position creation.

Kill Handicap and Total Kills remain retired unless a later explicit authority change activates them.

---

# 11. Compact internal record

Before a Duration `TAKE CANDIDATE`, resolve:

`DUR_CORE[t=...;V=...;Q=...;H=...;T=...;R0=...;ER=...;F=...;LINE=...;P_SIDE=...;BOOK=...;EDGE=...;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`

This is one audit record, not a legacy gate tree.
