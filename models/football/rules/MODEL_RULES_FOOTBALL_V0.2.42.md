# MODEL RULES — FOOTBALL v0.2.42

Effective: 2026-08-11

This version supplements v0.2.41 and all active football procedures. All earlier staking, minimum-odds, synchronization, reset, market-scan, xG, exposure, settlement, circuit-breaker, Airtable and ledger controls remain active unless strengthened below.

## 1. Directional superiority versus event-generation superiority

A team can be clearly superior in territory, shot volume, box access and aggregate chance creation without the evidence being strong enough to identify which team scores the next decisive goal.

For live side candidates, explicitly distinguish:

- **directional superiority**: evidence that one team is materially more likely than the opponent to produce the decisive scoring event required by the side bet; and
- **event-generation superiority**: evidence that the current state is likely to produce another goal or major event, regardless of which team produces it.

Do not promote a side merely because the dominant team has more xG, shots, shots on target, box touches, corners or possession. Those signals can support event generation while leaving material two-way transition risk.

## 2. Mandatory side-versus-live-total comparator

When all of the following are true:

1. the match is tied or separated by no more than one goal;
2. one team has sustained attacking/territorial superiority;
3. the opponent has demonstrated a credible scoring route, transition route, set-piece route or prior dangerous sequence;
4. an eligible live total at odds >=1.70 is available;
5. the proposed side requires the dominant team to produce the decisive goal rather than merely benefit from another goal occurring;

then the model must compare the side against the best eligible live total expression before verdict promotion.

The comparison must include:

- exact settlement paths for both markets;
- remaining event budget;
- whether one additional goal benefits one market regardless of scorer;
- whether the opponent's credible scoring route weakens the side more than it weakens the total;
- whether the side has an additional independent directional channel beyond general pressure/event generation;
- price and implied break-even difference.

If the total captures the same forward-looking evidence with less directional dependence and an acceptable price, prefer the total.

If the evidence supports another goal but not sufficiently which team scores it, the side candidate fails the best-expression test.

## 3. Quarter-goal total preference when exactly one further goal is the central branch

When exactly one additional goal is the modal or central live branch and the market offers a quarter-goal total such as Over 2.25, Over 2.75 or Over 3.25 at eligible odds, explicitly account for half-win/half-loss protection.

Do not reject the total family merely because the nearest half-goal line is below the minimum-odds floor if an adjacent quarter-goal line at >=1.70 provides a valid expression.

Example: if Over 2.5 is 1.59 but Over 2.75 is 1.88, the total family remains eligible through Over 2.75 and must be compared against the side.

## 4. Credible opponent threat cannot be erased by low aggregate xG

If an opponent has already scored, had a goal disallowed, produced a clear transition, forced a high-quality save, repeatedly accessed dangerous transition space, or otherwise demonstrated a credible scoring mechanism, low aggregate xG cannot by itself classify that opponent as non-threatening.

The model must document whether the threat is:

- isolated/non-repeatable;
- structurally repeatable;
- score-state dependent;
- likely to increase as the dominant side commits numbers forward.

A side candidate that depends on the opponent remaining harmless requires affirmative evidence for that assumption.

## 5. Live side promotion burden in aggressive-pressure states

When the dominant team is pushing aggressively in a tied or one-goal game, a live side bet may pass only if there is at least one independent **directional separator** in addition to the existing two-channel primary-evidence minimum.

Directional separators can include:

- repeated central/box access that the opponent cannot match;
- materially superior big-chance generation across multiple sequences;
- clear opponent defensive degradation without a corresponding transition outlet;
- personnel/tactical asymmetry specifically increasing the dominant team's scoring probability;
- sustained opponent inability to progress or counter despite opportunities;
- a market dislocation specifically favoring the side rather than merely the goal environment.

Raw xG, SOT, possession, aggregate shots and corners do not count as the directional separator by themselves.

Without a directional separator, prefer an eligible total when the evidence is primarily event-generating; otherwise return NO BET.

## 6. Deportivo Cuenca vs Manta review

At 61:05 with the score 1-1, Deportivo Cuenca -0.5 @2.45 was selected as CB3 under Football v0.2.41. Cuenca led 1.72-0.11 xG, 19-6 shots, 7-2 SOT, 17-7 opposition-box touches and 6-1 corners. Manta ultimately won 2-1.

The model error was market expression, not the recognition of Cuenca pressure. Manta had already demonstrated a scoring route and remained capable of benefiting from Cuenca's aggressive posture. The evidence therefore supported additional event probability more cleanly than Cuenca-specific win probability.

At the same snapshot, Over 2.5 @1.59 was ineligible, but Over 2.75 @1.88 was eligible. One additional goal would have produced a half-win on Over 2.75 regardless of scorer, while Cuenca -0.5 required Cuenca to win.

Correct non-hindsight hierarchy: Over 2.75 @1.88 > Cuenca -0.5 @2.45, absent an additional directional separator establishing that Cuenca were materially more likely than Manta to score the decisive goal.

## 7. Existing controls remain active

- 1u = 1,000,000 VND.
- Minimum accepted odds = 1.70.
- Every executable or shadow LEAN uses exactly 0.25u.
- Same-state accepted-odds drift tolerance remains 0.08.
- Official football betting remains paused under the four-match circuit breaker.
- One best expression remains mandatory at each reassessment.
- xG/xGOT remain supporting evidence only.
- A wager becomes official only after confirmed placement and only when official betting is enabled.
- Ledger writes remain on hold until explicitly approved.