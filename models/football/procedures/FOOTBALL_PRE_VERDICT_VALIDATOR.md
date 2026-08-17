# FOOTBALL PRE-VERDICT VALIDATOR

Effective with Football v0.2.40; strengthened by Football v0.2.41 and Football v0.2.42. Enforcement clarified on 2026-08-18 under Football v0.2.47 after the Nõmme/Kalju and settlement reviews.

This procedure is mandatory before any `SHADOW LEAN — DO NOT PLACE`, `LEAN`, or `OFFICIAL BET` output. It is an enforcement layer over all active football rules, not a replacement for them.

## Result semantics

- `PASS`: every mandatory gate is satisfied. The candidate may proceed subject to circuit-breaker mode and execution rules.
- `HOLD`: the thesis may remain plausible but one or more required states are unresolved, stale or awaiting persistence. Output `NO BET — HOLD`.
- `FAIL`: one or more mandatory gates are contradicted or violated. Output `NO BET`.

No candidate may be promoted around a `HOLD` or `FAIL` result.

## Gate 1 — synchronized state

Confirm from current evidence:

- match identity;
- score;
- minute/phase;
- material events since the prior snapshot;
- current line and odds for the candidate;
- settlement scope of the market.

If any of these are assumed rather than synchronized, result = `HOLD`.

## Gate 2 — reset epoch

Check for goals, penalties, red cards, substitution clusters, injuries, tactical changes, weather/pitch changes or other material events.

If a material reset has occurred, establish a new reset epoch. Do not carry the old directional or goal-environment classification through the reset without fresh evidence.

If post-reset evidence is insufficient, set `Goal Environment = Unresolved`, `Reset Resolved = false`, and result = `HOLD`.

## Gate 3 — competition format and utility

Verify the competition format whenever motivation or result utility matters.

Explicitly separate and apply:

- regulation-win utility;
- regulation-draw utility;
- shootout utility;
- margin/goal-difference utility;
- loss-avoidance utility;
- conservation utility.

Verify the **exact order** of relevant standings or qualification tiebreakers. Do not merely note that goal difference exists.

If a margin-sensitive tiebreaker applies, do not assume conservation from a lead without accounting for the value and priority of additional margin. Do not overstate goal-difference value if another criterion ranks ahead of it.

**Utility is context, not proof of current behaviour.** A team having little need for another goal, holding a large aggregate lead, or being able to conserve cannot by itself establish a closed/decaying goal regime or justify a live Under. When conservation materially supports an Under, require affirmative current evidence that the team is actually reducing attacking risk or suppressing the opponent.

When competition incentives materially affect the candidate, `Margin Incentive Propagated` must be true in Airtable.

If format, tiebreak order or utility propagation is unresolved, result = `HOLD`.

## Gate 4 — xG/xGOT role

Set `xG Role` to exactly one of:

- `Secondary Only`;
- `Not Used`;
- `Violation`.

Ask the counterfactual: **If xG/xGOT were removed from this assessment, would the primary thesis still stand?**

If no, set `Violation` and result = `FAIL`.

xG/xGOT may never independently establish scoring superiority, goal environment, regression, pressure, urgency or a side/total selection.

## Gate 5 — primary evidence

For any live candidate, identify at least two independent primary forward-looking channels, subject to stricter active rules.

Valid channels include:

- box/central access;
- big/clear chances;
- dangerous transitions/cutbacks;
- sustained set-piece pressure;
- defensive degradation;
- shot-location/chance structure independent of xG;
- persistent territory/box touches;
- tempo/persistence;
- relevant scoring/conceding profile;
- materially predictive lineup/availability evidence.

Possession, pass volume, raw shots, SOT, xG and xGOT cannot by themselves satisfy the minimum.

### 2026-08-18 evidence-independence enforcement

Apply all of the following literally:

1. **Raw SOT is not `Shot Quality/Locations`.** A shot being on target does not establish strong location or chance structure. Location, inside-box context, big/clear-chance context, meaningful keeper intervention, cutback/one-v-one/free-header context, or equivalent structural evidence is required.
2. **One event cluster cannot satisfy two channels.** If the same few attacks/shots are the substantive basis for both labels, count them as one channel. Do not manufacture independence by renaming the same evidence.
3. **`Tempo/Persistence` must be demonstrated.** Require at least two comparable score-stable snapshots showing continuing/repeated threat, or a clearly timestamped repeated event sequence over the interval. Kickoff-zero to one cumulative snapshot is not persistence by itself.
4. **Shallow provider coverage raises uncertainty.** Missing box-access/chance-location/big-chance data does not permit raw SOT or possession to substitute for those channels.
5. **Evidence must match the candidate burden.** For unusually high live totals or any candidate requiring several additional goals for a full win, an efficient short burst is insufficient unless independent structural/chance-quality evidence supports a credible multi-goal route.

If fewer than two genuinely independent primary channels support the candidate, result = `FAIL` or `HOLD` depending on whether more evidence can reasonably resolve the state.

## Gate 6 — directional persistence and regime consistency

For live directional switches, favourite fades or goal-environment changes, require persistence across comparable evidence windows as required by active rules.

A single high-value event can trigger a reset but cannot alone prove the post-reset regime.

Check that:

- the stated `Goal Environment` matches the evidence;
- the `Reset Resolved` state is consistent with the classification;
- a prior Neutral/Closed/Open classification has not been retrospectively rewritten because of one later event;
- directional switches have persistent post-reset support.

### Live Under deceleration sub-gate

When a live Under thesis depends materially on conservation, aggregate safety, a comfortable lead, or reduced need to attack, require affirmative evidence of **actual current-regime deceleration or suppression**, such as:

- declining high-value box/central entries across comparable windows;
- fewer dangerous transitions or fewer bodies committed forward;
- attack-dampening substitutions or an observable shape change;
- repeated harmless possession replacing penetrative possession;
- declining chance quality/locations independent of xG;
- opponent attacks repeatedly suppressed before dangerous final actions;
- a score-stable interval showing sustained threat decay rather than merely no goal.

If the leader still shows repeatable high-value creation, strong attacking depth, or a credible multi-goal route, conservation language cannot override that evidence. `They do not need another goal` is not equivalent to `they have stopped creating`.

Any contradiction = `HOLD` or `FAIL`.

## Gate 7 — favourite and margin gates

When fading a material favourite or taking a protected underdog:

- apply v0.2.38 live favourite-fade requirements;
- apply v0.2.39 prematch deep-favourite and margin-risk requirements;
- apply v0.2.41 protected-underdog burden escalation and favourite-first-goal branch requirements;
- preserve the exact protected line rather than moving to a worse settlement line merely to meet the odds floor.

### Prematch protected-underdog sub-gate

When the candidate is approximately +1.0, +1.25, +1.5 or larger against a material/deep favourite:

1. identify at least two independent affirmative **margin-suppression** channels under v0.2.41;
2. write `Underdog Suppression Evidence Count` to Airtable and require value >= 2;
3. at least one suppression channel must address the favourite's repeated high-value creation/conversion or multi-goal-margin weakness;
4. at least one suppression channel must address underdog adverse-state resistance or a credible scoring route to restore protection;
5. run the favourite-first-goal branch and require `Favorite First-Goal Branch = Pass`;
6. reject defensive formation labels, generic counterattack narratives, friendly H2H, isolated close losses and the existence of the large handicap itself as standalone suppression evidence;
7. when competition margin incentives matter, require `Margin Incentive Propagated = true`.

If `Underdog Suppression Evidence Count < 2`, `Favorite First-Goal Branch = Fail/Unresolved`, or applicable margin incentive propagation is false, result = `FAIL`.

If the applicable favourite-fade gate is otherwise unresolved or failed, validation cannot pass.

## Gate 8 — market-family scan and best-expression test

Reassess all currently available major market families relevant to the state, including sides/Asian handicaps, totals and any material derivatives supplied by the user.

Compare the candidate against the best alternative expression.

Do not anchor to the previously discussed market. Invalidating one candidate does not confirm another.

When a totals thesis passes, prefer the **lowest eligible protected boundary** that preserves acceptable price quality and reduces unnecessary event-budget burden. Quarter-goal protection is valuable, but it cannot rescue an unsupported thesis.

### v0.2.42 live side-versus-total sub-gate

When the match is tied or separated by no more than one goal, one team has sustained attacking/territorial superiority, and the opponent has demonstrated a credible scoring/transition/set-piece route, any proposed live side must be explicitly compared with the best eligible live total at odds >=1.70.

For the comparison:

1. state the exact settlement path of the side;
2. state the exact settlement path and remaining event budget of the best eligible total;
3. determine whether one further goal benefits the total regardless of scorer;
4. classify the opponent threat as isolated/non-repeatable, structurally repeatable, score-state dependent, or likely to increase as the dominant team commits numbers;
5. identify at least one independent **directional separator** for the side beyond generic pressure/event-generation evidence;
6. inspect adjacent quarter-goal totals if the nearest half-goal total is below 1.70.

Raw xG, xGOT, SOT, shots, possession and corners do not count as the directional separator by themselves.

If the evidence supports another goal more clearly than it supports which team scores the decisive goal, and an eligible total captures that evidence with less directional dependence, the side fails the best-expression test.

If the major-market scan or applicable side-versus-total comparison is incomplete, result = `HOLD`.

## Gate 9 — settlement and event-budget integrity

For the exact candidate:

- state what outcomes win, push/half-win/half-loss where applicable, and lose;
- for totals, compute the remaining event budget at the current score;
- for handicaps, distinguish current-match score from remaining-segment settlement when relevant;
- verify minimum odds >= 1.70;
- verify accepted-odds drift <= 0.08 only when the score, minute, line, settlement scope and material state are unchanged and acceptance is within 120 seconds.

### Goal-budget proportionality

For totals, state explicitly how many **additional goals** are required for:

- full win;
- push;
- half-win;
- half-loss;
- full loss boundary where useful.

The proof burden rises with the full-win requirement. If the candidate needs two or more additional goals for a full win, the current evidence must support a credible multi-goal route. If it needs four or five additional goals, a short efficient SOT burst or historical scoring profile is not enough without strong independent current-regime support.

Any settlement misunderstanding, unsupported event budget, or unresolved line movement = `FAIL` or `HOLD`.

## Gate 10 — circuit-breaker and output mode

If the four-match circuit breaker is active:

- `PASS` may output only `SHADOW LEAN — DO NOT PLACE`;
- exactly one primary shadow selection may count per match;
- simulated stake follows the active `CURRENT_MODEL.md` convention (currently **0.125u** unless a newer explicit user instruction supersedes it);
- the shadow selection must be written to the Airtable `Circuit Breaker` table;
- `NO BET` / `NO BET — HOLD` do not consume a slot;
- a later process audit may mark a historical sample `Invalid` without rewriting the original Decision State; invalid samples remain visible but are excluded from valid edge estimation.

Official execution cannot resume after 4/4 until the four-match review is complete and the user explicitly restores official betting.

## Gate 11 — Airtable write lock

Before emitting a shadow or executable verdict, write the material assessment to the Airtable `Decision States` table documented in `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`.

Required fields include at minimum:

- Assessment ID;
- Match;
- Model Version;
- minute/score/reset epoch/assessment period;
- verdict/candidate/line/odds if applicable;
- goal environment;
- synchronization and reset status;
- competition-format and utility verification;
- margin-incentive propagation when applicable;
- xG role;
- primary channels and count;
- favourite-fade and directional-persistence states where applicable;
- underdog suppression evidence count and favourite-first-goal branch when applicable;
- major-market scan status;
- circuit-breaker mode;
- validator result and fail reasons.

A candidate verdict cannot be `SHADOW LEAN — DO NOT PLACE`, `LEAN`, or `OFFICIAL BET` unless the corresponding record has `Validator Result = PASS`.

If Airtable is unavailable, execution validation is unavailable; output `NO BET — HOLD — decision-state validation unavailable`.

## Compact response behavior

The user-facing live response remains brief and decision-first. Do not print the full validator checklist unless requested.

When validation fails or holds, mention only the decisive failed/unresolved gates and the unlock condition.
