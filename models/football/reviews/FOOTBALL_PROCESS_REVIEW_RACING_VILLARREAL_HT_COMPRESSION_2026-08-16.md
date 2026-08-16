# Football Process Review — Racing Santander vs Villarreal: High-Scoring Halftime Compression

**Date:** 2026-08-16  
**Status:** Active interim process review  
**Model at original decision:** Football v0.2.46 — AUDIT MODE  
**Resulting amendment:** Football v0.2.47 — High-Scoring Halftime Compression / Goal-Saturation Gate

## Scope

This review documents a process weakness identified prospectively during the Racing Santander vs Villarreal live audit.

It does **not** rewrite any historical shadow decision and does **not** assume a final match score beyond the latest user-confirmed state recorded here.

## Observed match sequence

Known synchronized/user-supplied states:

- 21': Racing 1-0 Villarreal, penalty.
- 34': Racing 2-0 Villarreal.
- 45': Villarreal 2-1.
- 45+1: Villarreal 2-2.
- HT: 2-2.
- 55:51: still 2-2; v0.2.46 issued `SHADOW LEAN — DO NOT PLACE: Over 5.25 @1.88`.
- 63:57: still 2-2; current protected reference improved to Over 5 @1.86; this was treated as continuation, not a second counted shadow ticket.
- 82': user reported still 2-2.

No later/final score is assumed in this review unless separately confirmed and appended later.

## HT evidence

The first half was genuinely high-event:

- 4 total goals;
- both teams demonstrated scoring routes;
- Racing produced substantial shot/box activity;
- Villarreal recovered from 2-0 to 2-2 before halftime;
- the match looked structurally open.

The error was **not** that the first-half openness was imaginary.

The error was carrying too much of that first-half scoring regime into the second-half Over decision.

## 55:51 original v0.2.46 promotion

At approximately 55:51, second-half activity had continued:

- Racing had added shots and inside-box activity;
- Racing had added a big chance;
- Villarreal had added some fresh threat;
- cumulative box touches and attacking events still looked open.

The model promoted:

`SHADOW LEAN — DO NOT PLACE: Over 5.25 @1.88`

The exact settlement burden at 2-2 was:

- one further goal: half-loss / half-push structure on O5.25;
- two further goals: full win.

Therefore the full-win thesis required a **two-goal second-half continuation**.

## Process weakness

The model treated:

`SECOND-HALF PRESSURE/ACTIVITY PERSISTENCE`

as too close a substitute for:

`SECOND-HALF SCORING-HAZARD PERSISTENCE`.

Those are not equivalent.

A high-scoring first half can be followed by:

- continued territory;
- continued shots;
- continued SOT;
- corners;
- box touches;
- transition entries;

while the actual finishing-quality regime compresses after halftime.

Possible mechanisms include tactical repair, more selective risk-taking, improved defensive spacing, score-equilibrium incentives, substitution effects, fatigue, goalkeeper response and natural finishing regression.

These mechanisms are hypotheses/risk factors, not treated as a universal empirical law.

## User pattern recognition

The user explicitly identified this broader pattern from watching many matches: a match can produce 2-3+ goals by halftime, retain apparently similar pressure after the break, yet produce at most one additional goal.

The user cited:

- Racing Santander vs Villarreal as one example;
- a separate Ajax match as the same-direction observation.

The Ajax example is not reconstructed here with synchronized data, so it is qualitative corroboration only.

## Corrected decision logic

The correct post-HT question after 3+ first-half goals is not:

`Does the match still look open?`

It is:

`Has the second-half scoring regime independently re-established enough conversion-quality evidence for the exact remaining goal budget?`

That leads to the v0.2.47 changes:

1. 3 HT goals trigger a moderate compression gate.
2. 4+ HT goals trigger a strong goal-saturation gate.
3. First-half openness becomes context only after the halftime reset.
4. Fresh second-half evidence must satisfy the new Over promotion independently.
5. At least one fresh conversion-quality channel is mandatory.
6. Generic shots/SOT/possession/corners/territory/box touches are insufficient by themselves.
7. A candidate needing two or more further goals for a full win must show a credible second-half multi-goal route.
8. Score-stable second-half intervals require repeated current-regime reassessment; the old `OPEN` label cannot persist indefinitely.

## Counterfactual classification at 55:51

Under Football v0.2.47, the 55:51 state would be classified:

- `HT Saturation Gate: STRONG`
- `Second-half-only sample: active but limited`
- `Conversion-quality channel: UNRESOLVED / insufficiently repeated for multi-goal budget`
- `Second-half hazard: PERSISTENT BUT UNPROVEN`
- `Remaining goal budget: two more goals for full win on O5.25`
- `Validator status: HOLD`

User-facing verdict:

`NO BET — HOLD`

This counterfactual is a process diagnostic only. The original v0.2.46 shadow selection remains historical and must settle exactly as issued once the final score is confirmed.

## Audit principle

Do not solve this failure mode by adding a blanket Under bias or by forcing arbitrary waiting.

The correction is **evidence-type specific**:

- before halftime, v0.2.46 still requires early recognition of genuine pressure acceleration;
- after a high-scoring halftime, v0.2.47 requires proof that scoring hazard itself survived the break.

If strong second-half conversion-quality evidence appears quickly, decide quickly under v0.2.44.

## Follow-up research

Track future 3+ goal halftime matches and record:

- HT goal count;
- second-half first 10-minute conversion-quality events;
- whether raw pressure persists;
- whether high-quality chance production persists;
- second-half goals;
- line/remaining-goal budget at candidate checkpoints;
- whether the compression gate correctly filters false Over continuations without suppressing genuine second-half re-acceleration.

Do not convert the qualitative pattern into a fixed statistical scoring penalty until a larger audited sample supports it.