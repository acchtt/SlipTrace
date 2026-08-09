# MODEL RULES — LEAGUE OF LEGENDS v0.3.45

**Status:** Active delta  
**Effective date:** 2026-08-09 16:30 UTC+7  
**Supersedes:** v0.3.44 only where stated

## Purpose

Rebuild the duration market after a six-position review showed a repeated process failure rather than isolated variance.

Tracked duration record at activation:

- Over 29 minutes — LOSS; final 28:24;
- Over 34 minutes — WIN; final 36:57, supported by observed Baron-expiry/stall evidence;
- Under 31 minutes — LOSS; pregame/draft-only thesis, exact final clock unavailable;
- Over 32 minutes — LOSS; final 31:02;
- Over 32 minutes — LOSS; final 30:43;
- Over 33 minutes — LOSS; DK vs KT Game 1, finished below 33.

Known settled record: **1-5, -1.03425u**.

The dominant errors were:

1. treating quiet-state observations as independent stall evidence;
2. projecting pre-break pace linearly through nonlinear first-structure cascades;
3. betting too close to the model's own central finish uncertainty;
4. using draft theory as if it were observed duration evidence;
5. transferring low kill/activity expectations into long-duration expectations;
6. failing to distinguish fight frequency from post-fight conversion efficiency.

This delta makes Duration a **specialized live-only market** until a future explicit revision restores pregame eligibility.

All v0.3.44 handicap controls, v0.3.43 latent-conversion concepts, and v0.3.42 team-strength/draft controls remain active unless superseded below.

---

## 1. Duration Is Live-Only

**No pregame / 0:00 duration TAKE is permitted under v0.3.45.**

Pregame duration lines may be analyzed for calibration, but the executable verdict is `PASS/HOLD`.

Before **12:00**, duration is `HOLD` by default and no TAKE is permitted.

From **12:00 through 13:59**, a TAKE is high-friction and requires all normal v0.3.45 evidence plus at least two synchronized snapshots separated by at least 90 seconds that demonstrate the same observed pace mechanism.

From **14:00 onward**, duration may qualify only through the evidence gates below.

---

## 2. Predict Conversion Efficiency, Not Historical Quietness

Duration is not inferred from whether the opening has been quiet.

The model must forecast the rate at which future won fights/tempo convert into:

`pick/fight -> objective -> tower -> vision -> second pick -> base access -> Nexus`

Current low kills, 0-0 towers, even gold, split dragons and unclaimed objectives are often correlated manifestations of one latent quiet state. They do **not** count as separate independent duration signals.

### Correlated Quiet-State Collapse

The following observed at the same snapshot count as at most **one** generic quiet-state signal unless separate mechanisms are demonstrated:

- low kills;
- 0-0 or low towers;
- near-even gold;
- split/low neutral-objective count;
- no Baron/inhibitor yet.

A duration edge requires evidence about **future conversion**, not a count of correlated past inactivity descriptors.

---

## 3. Over Requires Observed Stall

A duration **Over** requires observed evidence that the map is consuming clock without converting decisive tempo into structures/base access.

Qualifying observed stall mechanisms include:

- at least two meaningful pushes neutralized without material structure loss;
- repeated successful waveclear after the opponent wins tempo;
- repeated engage/pick attempts that fail to generate objective or structural conversion;
- a leader's gold advantage staying stable/shrinking across synchronized snapshots despite initiative;
- repeatable disengage/reset preventing second-wave chase;
- successful cross-map compensation after local priority is lost;
- Herald/Baron/major objective buff producing little or no structural gain;
- side-lane setup repeatedly failing to create tower access.

Theoretical waveclear, peel, scaling, disengage, side-lane potential or 'they can stall' language is not enough.

For an Over TAKE, at least **two independent observed stall mechanisms** must be present, and at least one must be confirmed across temporally separate snapshots unless the map is already after 25:00 and a major objective conversion failure has just been observed.

---

## 4. Under Requires Observed Acceleration

A duration **Under** requires observed acceleration, not merely an aggressive draft.

Qualifying acceleration mechanisms include:

- repeated pick/fight wins that immediately create structures;
- first tower unlocking two or more additional structures in the same/next conversion cycle;
- rapidly widening gold lead plus repeatable structure access;
- Herald/Baron/soul pressure creating forced base access;
- deep vision causing repeat picks and denied resets;
- side-lane pressure forcing multiple simultaneous defensive assignments;
- inhibitor/base access with the defender unable to reset the map;
- demonstrated high Latent Conversion Potential functioning on the current map.

Pregame engage, dive, siege, global or pick tools are only hypotheses until observed functioning.

For an Under TAKE, at least **two independent observed acceleration mechanisms** must be present, with one confirmed across temporally separate snapshots unless a post-25:00 terminal-state exception applies.

---

## 5. Two-Snapshot Persistence Gate

Except for the terminal-state exception in Section 6, every duration TAKE requires at least **two synchronized live snapshots** separated by at least 90 seconds.

The same claimed mechanism must persist or strengthen across the snapshots.

Examples:

- Over: two pushes denied, then another tempo win produces no tower;
- Under: first tower falls, then the next snapshot shows additional structure/base access and widening control.

A single quiet or explosive screenshot is insufficient before 25:00.

If the mechanism reverses between snapshots, widen uncertainty and `HOLD`.

---

## 6. Terminal-State Exception After 25:00

After **25:00**, a single synchronized snapshot may support a duration Under without the two-snapshot persistence requirement only when the state is already structurally terminal or near-terminal.

Examples require multiple aligned features such as:

- inhibitor/base access;
- Baron/Elder/soul plus major gold/structure lead;
- exposed Nexus towers;
- defender has no credible reset/waveclear window;
- leader has reliable first contact and safe follow-up;
- shortest realistic structure-to-Nexus route is inside the market survival horizon.

This exception does not apply to Overs. An Over still requires actual evidence that terminal conversion is being denied.

---

## 7. Forecast Dead Zone

Duration errors of 36, 58 and 77 seconds showed that the model was betting inside its own timing uncertainty.

For every duration market, estimate:

- fast-close interval;
- central closing interval;
- extension interval;
- central expected finish `C`;
- market line `L`.

A duration TAKE is automatically `HOLD/PASS` if either is true:

1. `L` lies inside the model's central closing interval; or
2. `|L - C| < 2.0 minutes`.

The two-minute dead zone is a minimum. If uncertainty is wider, use the wider uncertainty band.

A central estimate barely beyond the line is not an edge.

---

## 8. Regime-Change Repricing

The duration forecast must be recomputed immediately after any of these regime-change events:

- first tower;
- Herald charge that materially opens structures;
- first Baron;
- first inhibitor;
- soul/Elder acquisition;
- >=2-tower swing in one conversion cycle;
- >=3k meaningful gold swing over a short interval;
- repeated demonstrated conversion failure after a major objective.

Do not carry a pre-break finish forecast through a first-structure or Baron cascade.

First tower is not just one tower; it may alter side-lane access, vision depth, objective setup and subsequent structure hazard.

---

## 9. Retained Survival-Horizon and Latent Conversion Concepts

Retain the v0.3.43 definition:

`R = duration line L - current game clock t`

Price `P(game survives R more minutes)` rather than generic pace.

Retain Latent Conversion Potential (LCP): reliable first contact, numbers creation, safe follow-up/chase, wave/structure access, objective leverage and functional suppression of defender stall tools.

But under v0.3.45, **LCP is a mechanism prior, not sufficient observed evidence by itself** before 25:00.

A high-LCP composition must demonstrate acceleration on the current map for an Under TAKE; a low-LCP opponent does not automatically justify an Over.

---

## 10. Duration Probability and Market-Divergence Gate

Retain break-even calculation and probability ranges.

For a duration TAKE, the lower end of the modeled probability range must clear break-even by:

- **+6pp** from 12:00 through 17:59;
- **+5pp** from 18:00 through 24:59;
- **+4pp** from 25:00 onward.

These are stricter than v0.3.43 because the market family is in rebuild mode.

Market-divergence sanity check:

- central model vs break-even difference 0-5pp: normal;
- >5-9pp: require at least two independent observed current-map mechanisms;
- >9pp: require at least three independent current-map mechanisms, including one temporally persistent stall/acceleration mechanism.

Unsupported disagreement => shrink toward market, widen uncertainty and `PASS/HOLD`.

---

## 11. Total Kills and Duration Are Orthogonal

Do not infer duration from total-kill projection.

A game may have:

- few kills and finish quickly through efficient conversion;
- many kills and last long through poor conversion/resets;
- high fight density with low structural efficiency;
- low fight density with one decisive fight-to-Nexus cascade.

Total Kills models **fight inventory and kill generation**.

Duration models **clock survival and structural conversion efficiency**.

A Total Kills TAKE does not support a Duration TAKE unless independent duration evidence also qualifies.

---

## 12. Mandatory Duration Output Discipline

Before any duration TAKE, internally lock:

1. current clock `t`;
2. line `L` and survival horizon `R`;
3. fast / central / extension finish intervals;
4. central expected finish `C`;
5. dead-zone test;
6. two-snapshot persistence status;
7. correlated quiet-state collapse;
8. observed stall mechanisms;
9. observed acceleration mechanisms;
10. current LCP and whether it is actually functioning;
11. first-break / Baron / base regime-change status;
12. shortest realistic structure-to-Nexus route;
13. break-even probability;
14. model probability range and rebuild buffer;
15. market-divergence test;
16. confirmation that Total Kills reasoning was not transferred into duration.

Missing a decision-critical item => `PASS/HOLD`.

---

## 13. Duration Rebuild Review Window

Duration remains in rebuild mode until a future explicit revision.

Review after the next **10 settled v0.3.45 duration positions** if that many qualify. Track:

- Over/Under split;
- pre-25 vs post-25 entry;
- line minus central expected finish at entry;
- whether the two-snapshot gate was satisfied;
- number/type of observed stall or acceleration mechanisms;
- first-break/Baron regime changes after entry;
- closing-time calibration error;
- win/loss and ROI.

Do not loosen gates merely because too few bets qualify. Low frequency is acceptable.

---

## 14. Retained Controls

All v0.3.44 symmetric kill-handicap controls remain active.

All v0.3.42 verified-team-strength, market-divergence, matchup-adjusted draft, functional-counter, execution-burden and damage-access controls remain active.

All v0.3.41 position-blind reassessment and structural vetoes remain active.

Where this delta conflicts with v0.3.43 duration rules, **v0.3.45 controls**.
