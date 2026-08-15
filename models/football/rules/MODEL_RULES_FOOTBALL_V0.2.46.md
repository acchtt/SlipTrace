# Football Model Rules v0.2.46 — Pre-Goal Pressure Inflection and Late-Half Acceleration

**Effective date:** 2026-08-15  
**Status:** Active audit rule  
**Supersedes:** v0.2.45 only where the Willem II vs NEC process error was framed primarily as a halftime/terminal-goal problem. v0.2.45 remains active as a fallback after a genuinely terminal goal. v0.2.46 does **not** weaken synchronization, settlement, style, provider-quality, no-retrofit, or post-goal reset controls.

## Trigger correction

The user corrected the Willem II vs NEC sequence: the important missed decision window was **before halftime**, around 42', while the score was still 0-0 and NEC had already increased pressure. The later 45+2 goal and halftime 0-1 state were downstream of that missed pre-goal inflection.

The synchronized board around 42' showed a protected low total in the region of **Over 1.75 @ 1.84**. The model did not issue a prospective shadow verdict in that state.

Therefore the primary process error is reclassified as:

`LATE — PRE-GOAL PRESSURE INFLECTION NOT CONVERTED TO DECISION`

The later 0-4 score remains a process diagnostic only. It does **not** create a retrospective shadow win.

## 1. Late-half pressure-acceleration scan

From approximately 35:00 to halftime, every material live checkpoint must explicitly compare the **recent interval** with the previous synchronized state.

Do not rely only on cumulative match totals. Ask:

`Has either team's forward threat materially accelerated in the last 5-10 minutes?`

Classify:

- `PRESSURE INFLECTION: YES`
- `PRESSURE INFLECTION: POSSIBLE / UNRESOLVED`
- `PRESSURE INFLECTION: NO`

A late-half inflection is not itself a bet, but it forces an immediate fresh totals scan under v0.2.44.

## 2. Inflection evidence must be forward-looking

A valid pressure inflection normally requires at least two independent primary changes in the recent interval, with at least one from each group below.

### Direct threat channel

Examples:

- new shot(s) on target;
- big chance or clear high-quality chance;
- repeated shots from inside the box;
- repeated dangerous box entries/touches;
- dangerous set-piece sequence;
- repeated transition entries ending in shots or final actions.

### Structural / territorial channel

Examples:

- sustained final-third occupation;
- repeated high recoveries or counterpress wins;
- opponent pinned into repeated clearances;
- recurring wide/central overload producing entries;
- defensive spacing visibly deteriorating;
- possession becoming materially more advanced rather than merely sterile.

A specific, contemporaneous user live observation such as `NEC pressure has clearly increased` may support the structural channel when it is consistent with the synchronized event/stat feed, but it cannot be the sole evidence channel.

xG/xGOT remain secondary only.

## 3. Pre-goal attacker-driven Over

At 0-0 or another tied score, the model must not wait for a future `trailing-team chase` condition that does not yet exist.

If one team has developed a credible multi-goal attacking route before the first goal, an Over may be assessed as:

`ATTACKER-DRIVEN PRE-GOAL OVER`

The opponent's scoring route is then classified as:

- `ESSENTIAL`
- `HELPFUL`
- `OPTIONAL`

For low protected totals, the opponent may be `OPTIONAL` if the attacking team can plausibly supply the required goal budget itself.

This is the pre-goal analogue of v0.2.45's leader-driven Over principle.

## 4. No goal-confirmation tax

When a pre-goal pressure inflection is already synchronized and the total candidate clears all applicable gates, deliver immediately under v0.2.44.

Do **not** wait for:

- the first goal;
- halftime;
- proof that the opponent will chase after conceding;
- an extra snapshot used only for reassurance.

If the goal arrives before delivery, record:

`STATE-CHANGE RACE — NOT COUNTED`

Then reset and reprice. If the goal is terminal-half, v0.2.45 may then become relevant as the post-goal fallback.

## 5. Protected boundary selection becomes more important in one-team surges

When one team is driving the Over and the opponent contribution is weak or uncertain, compare adjacent low totals carefully.

At minimum inspect the nearest eligible combinations such as:

- Over 1.5
- Over 1.75
- Over 2.0
- Over 2.25

Prefer the line that best preserves settlement value if the attacking team produces only one or two additional goals.

A quarter-goal line may be superior to a higher half/full line even when the latter offers a larger price.

The candidate must still clear the 1.70 minimum-price reference and the normal NO-BET comparator.

## 6. Interval acceleration may override stale cumulative appearance

A match can look quiet cumulatively while becoming dangerous rapidly.

If the last 5-10 minutes show a genuine forward acceleration, do not let earlier sterile minutes dominate the current-state assessment.

Conversely, a high cumulative shot count is insufficient if the current interval has gone flat.

The required question is:

`What is the current regime doing now?`

not merely:

`What has the whole match averaged so far?`

## 7. Required late-half fields

For any serious live assessment from 35:00 to halftime, include:

- `Recent interval:` brief delta from prior snapshot
- `Pressure inflection:` YES / POSSIBLE / NO
- `Primary acceleration channels:` list
- `Attacker-driven goal route:` STRONG / MODERATE / WEAK / N/A
- `Opponent contribution:` ESSENTIAL / HELPFUL / OPTIONAL
- `Best protected total:` exact line and odds if available
- `Timing status:` ON TIME / VALID HOLD / LATE / STATE-CHANGE RACE

If `PRESSURE INFLECTION: YES` and all candidate gates are complete, verdict-first delivery is mandatory.

## 8. Arm A / Arm B

### Arm A — Current audit model

A pre-goal pressure inflection may support `SHADOW LEAN — DO NOT PLACE` only when the full validator, style, synchronization, settlement, market-family and audit gates pass.

### Arm B — Early totals benchmark

Arm B should explicitly test whether the pressure-inflection state supports a protected live Over before waiting for a goal.

If exact line/odds, two independent primary channels, adjacent-line protection, adverse-branch test and NO-BET comparator all pass, output:

`BENCHMARK SHADOW — DO NOT PLACE`

immediately in the pre-goal state.

## 9. Willem II vs NEC corrected process lesson

The key missed window was around 42' at 0-0, not only the halftime 0-1 state.

NEC's pressure had begun to increase before the goal. The model should have treated that as a fresh pre-goal regime and immediately rescanned the protected totals board rather than waiting for NEC to score or for Willem II to become a trailer.

The around-42' Over 1.75 price is retained only as a **missed synchronized decision state** for process review. Because no prospective verdict was delivered, it is not a winning shadow and contributes no P/L.

The halftime bridge from v0.2.45 remains useful after a terminal goal, but it is now explicitly secondary to the earlier requirement: **detect and act on the pre-goal acceleration first.**

## Operating principle

Detect the regime shift before the scoreboard confirms it. When late-half pressure accelerates and the protected total already clears the gates, decide in the pre-goal state. Do not wait for a goal to create a chase narrative that the current evidence does not need.