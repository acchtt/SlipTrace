# Football Model Rules v0.2.47 — High-Scoring Halftime Compression and Goal-Saturation Gate

**Effective date:** 2026-08-16  
**Status:** Active audit rule  
**Supersedes:** v0.2.46 only where post-halftime Over continuation was allowed to lean too heavily on first-half openness or generic second-half pressure persistence. All synchronization, reset, style, settlement, provider-quality, no-retrofit, v0.2.44 timeliness, v0.2.45 fallback and v0.2.46 pre-goal inflection controls remain active.

## Trigger and process correction

The Racing Santander vs Villarreal live audit exposed a recurring failure mode already noticed by the user in other matches, including an Ajax example:

`HIGH-SCORING FIRST HALF -> SECOND-HALF PRESSURE STILL LOOKS OPEN -> MODEL TREATS PRESSURE PERSISTENCE AS GOAL PERSISTENCE -> SECOND-HALF GOALS FAIL TO FOLLOW`

This is not yet treated as a universal statistical law. It is treated as a **model-risk condition** that requires a stricter second-half proof standard.

The core correction is:

**Pressure persistence is not the same as scoring-hazard persistence.**

A high-scoring first half can be followed by continued shots, possession, corners and box touches while the actual conversion-quality regime compresses after halftime because of tactical repair, more selective risk-taking, finishing regression, balanced-score incentives, fatigue, substitutions or improved defensive spacing.

Therefore halftime after a high-scoring first half is now a **hard scoring-regime reset**.

## 1. Halftime goal-count trigger

Classify the halftime score by total first-half goals:

- **0-2 HT goals:** normal halftime reset; no special saturation burden beyond existing rules.
- **3 HT goals:** `HT COMPRESSION GATE — MODERATE`.
- **4+ HT goals:** `HT GOAL-SATURATION GATE — STRONG`.

The gate applies to any post-halftime full-match Over, second-half Over, or Over add-on whose thesis depends materially on continued scoring.

The trigger is a caution burden, not an automatic Under signal.

## 2. First-half openness cannot satisfy second-half promotion evidence

After a 3+ goal first half:

- first-half goals;
- first-half shot volume;
- first-half SOT;
- first-half corners;
- first-half box touches;
- first-half pressure inflections;
- first-half xG/xGOT;
- first-half attacking style execution

may be retained as **context/prior information only**.

They cannot satisfy the minimum primary-evidence count for a new second-half Over promotion.

The second-half candidate must stand on **second-half-only forward-looking evidence** after the halftime reset.

Ask:

`If every first-half event were hidden, would the current second-half evidence still justify the remaining goal budget?`

If no, result = `NO BET — HOLD` or `NO BET`.

## 3. Conversion-quality channel becomes mandatory

For any 3+ goal HT Over promotion, generic pressure channels are insufficient by themselves.

Raw or cumulative versions of the following do **not** establish renewed scoring hazard:

- possession;
- pass volume;
- raw shots;
- raw SOT count without location/context;
- corners;
- territory;
- box touches without chance quality;
- cumulative first-half + second-half totals.

A promoted second-half Over must include at least one fresh **conversion-quality channel**, such as:

- a genuine big/clear chance;
- repeated central or high-value inside-box attempts;
- a one-v-one, cutback, free header, close-range chance or equivalent clear finishing situation;
- repeated threatening SOT that force meaningful goalkeeper interventions;
- a defensive error/degradation sequence directly producing a high-quality attempt;
- repeated transition entries ending in strong final actions rather than merely entries;
- a dangerous set-piece sequence producing a clear shot/chance rather than only a corner count.

xG/xGOT remain secondary only and cannot substitute for this channel.

## 4. Strong gate for 4+ HT goals

When halftime contains **4 or more goals**, a new second-half Over candidate normally requires all of the following:

1. the halftime reset is explicitly resolved;
2. a score-stable second-half sample has developed, normally about **6-10 minutes**, unless an earlier high-quality event cluster clearly establishes the new regime;
3. at least **two independent second-half primary channels** support renewed scoring;
4. at least one of those channels is a conversion-quality channel from Section 3;
5. the current interval, not merely the cumulative match, shows continuing or increasing threat;
6. the exact remaining goal budget is plausible from the new second-half evidence alone;
7. adjacent protected totals are compared explicitly;
8. the NO-BET comparator is passed.

For a tied high-scoring halftime state such as 2-2 or 3-3, apply an additional:

`HIGH-SCORE EQUILIBRIUM MODIFIER`

A tied game can remain territorially active while both teams become more selective about exposing the decisive transition. Territory alone cannot clear the gate. Require evidence that at least one team is still accepting meaningful defensive risk or repeatedly creating high-quality finishing situations.

## 5. Remaining-goal budget burden

After a high-scoring halftime, do not treat a lower-looking live total as automatically attractive simply because many goals have already occurred.

For the exact candidate, state:

- current total goals;
- goals needed for full win;
- goals needed for push/half-win/half-loss where applicable;
- whether the second-half-only evidence supports **one more goal**, **two more goals**, or a true multi-goal sequence.

The proof burden rises with the remaining goal budget.

### Practical rule

- If only **one additional goal** is needed for a full win, a strong single-team route may be enough when all other gates pass.
- If **two or more additional goals** are needed for a full win, the candidate must show a credible multi-goal second-half route. Generic persistence is not enough.
- Quarter-goal protection remains valuable, but protection cannot rescue an unsupported multi-goal thesis.

## 6. Score-stable decay after a high-scoring halftime

When 3+ goals were scored before halftime and the second half remains score-stable for a meaningful interval, the model must not keep carrying an `OPEN` label merely because the cumulative match still looks open.

At approximately every 8-10 score-stable minutes, compare the recent interval with the previous second-half snapshot.

If 15+ second-half minutes pass without a goal, require a fresh current-interval quality check before any new Over or re-entry.

Classify:

- `SECOND-HALF HAZARD: RE-ACCELERATING`
- `SECOND-HALF HAZARD: PERSISTENT BUT UNPROVEN`
- `SECOND-HALF HAZARD: COMPRESSING`

`PERSISTENT BUT UNPROVEN` cannot by itself produce a shadow/executable Over.

## 7. Add-on restriction after high-scoring halftime

A post-halftime add-on after a 3+ goal first half must be justified as a **new independent decision**.

Do not add because:

- the first-half Over thesis was correct;
- the match has already produced many goals;
- the base position remains live;
- the new line looks lower relative to the score;
- first-half pressure was strong;
- cumulative second-half stats still look active.

The add-on must independently clear the compression/saturation gate using second-half-only evidence and its own remaining-goal budget.

## 8. Racing Santander vs Villarreal process audit

Observed sequence:

- HT score: **2-2**.
- The first half was genuinely high-event and both teams had demonstrated scoring routes.
- Around 55:51 the model promoted `SHADOW LEAN — DO NOT PLACE: Over 5.25 @1.88` after second-half shots, box touches and a Racing big chance increased.
- Around 63:57 the game was still 2-2 while both teams had added SOT and Villarreal had added a big chance; the current protected reference improved to Over 5 @1.86.
- By 82' the score was still 2-2.

Under v0.2.47, the **55:51 Over 5.25 promotion would remain HOLD** unless the second-half sample showed stronger repeated conversion-quality evidence sufficient to justify a two-goal remaining full-win budget.

The observed second-half activity was enough to say the game remained active, but not enough to equate activity with a renewed multi-goal scoring regime.

This is a **process correction only**. The original 55:51 shadow selection remains recorded exactly as issued. Do not rewrite its timestamp, line, verdict or eventual settlement.

## 9. Ajax corroboration note

The user separately identified an Ajax match with the same qualitative direction: a high-scoring first half, continued-looking second-half pressure, but materially fewer second-half goals than the pressure suggested.

Because the exact synchronized Ajax state is not reconstructed here, it is retained as **qualitative corroboration only**, not counted evidence or shadow P/L.

Future reviews should explicitly test whether this failure mode repeats across a larger sample before converting the gate into a fixed empirical scoring penalty.

## 10. Required user-facing fields after 3+ HT goals

For any serious post-halftime Over assessment after 3+ first-half goals, include compactly:

- `HT saturation gate:` MODERATE / STRONG
- `Second-half-only sample:` brief interval/deltas
- `Conversion-quality channel:` PASS / UNRESOLVED / FAIL
- `Second-half hazard:` RE-ACCELERATING / PERSISTENT BUT UNPROVEN / COMPRESSING
- `Remaining goal budget:` exact settlement requirement
- `Best protected total:` exact line/odds
- `Validator status:` PASS / HOLD / FAIL

If the conversion-quality channel or remaining-goal budget is unresolved, output `NO BET — HOLD`.

## 11. Arm A / Arm B

### Arm A — current audit model

This gate is mandatory. A high-scoring first half can no longer promote a post-HT Over through cumulative openness plus generic pressure persistence.

### Arm B — early totals benchmark

Arm B must also separate first-half context from second-half promotion evidence after a 3+ goal halftime. It may remain more permissive about protected boundaries, but it cannot count first-half pressure as one of the fresh second-half primary channels.

This preserves benchmark usefulness without allowing the same first-half carryover error to contaminate both arms.

## 12. Relationship to v0.2.44-v0.2.46

This rule does **not** make the model generally slower or more conservative.

- v0.2.44 still requires immediate delivery when the current state genuinely clears all gates.
- v0.2.45 still handles terminal-goal halftime bridges.
- v0.2.46 still requires pre-goal pressure-inflection detection and immediate action before a goal when the protected total qualifies.
- v0.2.47 specifically prevents a different error: **carrying first-half scoring intensity through halftime without proving that the second-half scoring regime survived the reset.**

If high-quality second-half evidence appears quickly, promote quickly. Do not delay for reassurance. The stricter requirement is about **evidence type**, not arbitrary waiting.

## Operating principle

After a high-scoring first half, reset the scoring process—not just the scoreboard state. Treat first-half goals as history. Demand fresh second-half conversion-quality evidence for the exact remaining goal budget. Continued pressure without renewed finishing-quality evidence is `PERSISTENT BUT UNPROVEN`, not an Over signal.