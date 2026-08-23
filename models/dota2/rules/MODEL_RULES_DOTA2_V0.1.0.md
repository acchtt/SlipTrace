# Dota 2 v0.1.0-experimental — Core Model Rules

**Status:** Experimental, shadow only  
**Actual exposure:** 0u  
**Default simulated stake:** 0.25u  
**Default minimum odds:** 1.60

## 1. Scope

Supported pregame market families:

- Match Moneyline
- Match Handicap (series map handicap)
- Total Maps

Supported live market families remain:

- Moneyline
- Kill Handicap
- Total Kills
- Duration

Pregame TAKEs are enabled only for Match Moneyline, Match Handicap, and Total Maps. Other pregame markets remain observation-only until a dedicated rule is added.

Live markets remain governed by the live gates below when executable live betting is available. Current pregame authorization does not weaken or bypass any live gate.

## 2. Universal pregame gates

Every pregame TAKE requires:

1. exact current match line and odds, readable and executable;
2. confirmed match format (Bo3/Bo5 or other explicit series format);
3. current expected lineup, including any material stand-ins/substitutions;
4. current patch and tournament rules known, or explicitly judged non-material to the thesis;
5. matchup analysis that separates recent form, direct head-to-head, opponent quality, roster continuity, and tournament context rather than treating any one factor as decisive;
6. explicit probability estimate for the selected outcome;
7. explicit price-implied probability calculation;
8. a conservative probability edge of at least **5 percentage points** over the offered price-implied probability;
9. model confidence of at least **MEDIUM** after unresolved draft uncertainty is discounted;
10. no unresolved decision-critical fact treated as favorable by default;
11. offered odds at or above the model minimum accepted odds of **1.60**;
12. no greyed, suspended, stale, or materially changed pregame price treated as executable.

**Pregame execution window:** a sportsbook or feed label such as `Live`, `In Play`, or equivalent does **not** by itself terminate pregame eligibility when Map 1 has not started and ban/pick has not begun. A clearly pre-ban/pick, pre-Map-1 state remains a pregame state for Match Moneyline, Match Handicap, and Total Maps execution if the exact price is open and executable. Pregame eligibility ends at the **first draft action or Map 1 game start, whichever occurs first**. After that point, the pregame certificate cannot be used and any decision must satisfy the applicable live authority.

If both sides of a market are available, prefer a no-vig market estimate as additional context. If only the selected-side price is available, use raw implied probability `1 / decimal_odds`; the 5 percentage-point edge must clear that more conservative benchmark.

Exact draft is normally unknown pregame. Missing exact draft is therefore not itself a veto, but draft/side-selection variance must be explicitly discounted rather than assumed favorable.

Maximum pregame exposure remains one TAKE per match per market family. No rescue, martingale, chasing, or stake escalation.

## 3. Pregame Match Moneyline certificate

A Match Moneyline TAKE requires all universal pregame gates plus:

- **Series Win Mechanism:** identify why the selected team is more likely to win the series across multiple plausible drafts rather than only in one ideal draft.
- **Adaptation Test:** consider whether the opponent has credible map-to-map drafting, side-selection, or strategic adaptation routes.
- **Loss Path:** state the most realistic way the selected team loses the series.
- **Format Robustness:** account for Bo3/Bo5 length, recovery after a lost map, and whether the edge is robust to one poor draft or lane outcome.
- **Price Test:** compare model series-win probability with the exact offered Moneyline price.

Team reputation, a recent streak, or historical head-to-head alone cannot certify a Match Moneyline TAKE.

## 4. Pregame Match Handicap certificate

Match Handicap means **series map handicap**, not live kill handicap.

Use exact signed map-margin arithmetic from the selected team's perspective:

`signed_map_margin = selected_team_maps - opponent_maps`

Evaluate the exact terminal series-score paths that cover or fail the offered handicap. Examples:

- Bo3 selected team -1.5: only a 2-0 series win covers.
- Bo3 selected team +1.5: every result except a 0-2 series loss covers.
- Bo5 selected team -1.5: 3-0 or 3-1 covers; 3-2 does not.
- Bo5 selected team +1.5: every result except a 0-3 series loss covers.

A Match Handicap TAKE requires all universal pregame gates plus:

- explicit probability of the exact covering score set;
- map-to-map variance and adaptation risk;
- likelihood of a competitive loss versus a sweep;
- whether the favorite's advantage is strong enough to produce margin, not merely series victory;
- whether the underdog has at least one repeatable draft/game-state path that makes +maps materially safer than its Moneyline;
- exact offered handicap and odds.

Do not infer handicap value from Moneyline preference alone.

## 5. Pregame Total Maps certificate

Total Maps means the number of maps actually required to finish the series. Evaluate the exact terminal score paths that make the offered total win or lose.

Examples:

- Bo3 Over 2.5: only a 2-1 series in either direction wins.
- Bo3 Under 2.5: only a 2-0 series in either direction wins.
- Bo5 Over 3.5: 3-1 or 3-2 in either direction wins.
- Bo5 Under 3.5: only a 3-0 series wins.
- Bo5 Over 4.5: only a 3-2 series wins.
- Bo5 Under 4.5: every result except 3-2 wins.

A Total Maps TAKE requires all universal pregame gates plus:

- **Exact Score-Path Probability:** explicitly estimate the combined probability of all series scores that win the selected total;
- **Sweep Resistance / Sweep Pressure:** identify whether the underdog has repeatable map-winning paths or whether the favorite has a robust mechanism for repeated map control;
- **Map-to-Map Adaptation:** assess drafting adaptation, side-selection effects, and whether a Game 1 result materially changes later-map probabilities;
- **Competitive-Loss Test:** distinguish a team that can lose the series competitively from one whose only realistic path is an upset series win;
- **Draft Variance Discount:** do not assume every map is an independent replay of the pregame matchup; account for changing drafts and side selection;
- **Format Robustness:** evaluate how Bo3 versus Bo5 structure changes the number of paths to the selected total;
- **Price Test:** compare the modeled Total Maps probability with the exact offered total and odds.

Do not infer Total Maps value from Moneyline preference alone. A close Moneyline is supporting context, not proof of an Over, and a strong favorite is not proof of an Under. The certificate must be grounded in explicit sweep versus competitive-series probabilities.

## 6. Universal live gates

Every live TAKE requires:

1. at least two usable synchronized snapshots;
2. exact current line and odds;
3. current patch assumptions either known or non-material to the thesis;
4. position-blind reassessment;
5. explicit next compulsory contact/objective window;
6. explicit comeback/throw path test;
7. buyback state considered whenever material;
8. Roshan/Aegis state considered whenever material;
9. high-ground and structure-conversion state considered whenever material;
10. no unresolved decision-critical fact treated as favorable by default.

A large net-worth lead, kill lead, team reputation, draft label, or low/high current kill count is context only. None is a standalone TAKE gate.

## 7. Draft prior

Draft is a prior, not a permanent live veto. When exact draft is available, classify at minimum:

- initiation / counter-initiation;
- save / dispel / reset;
- burst and sustained damage;
- catch and mobility;
- waveclear;
- building damage;
- Roshan speed/control;
- high-ground offense;
- high-ground defense;
- split-push / rat pressure;
- scaling and late-game reliability;
- dependence on long cooldown ultimates.

Live state may degrade or break a draft prior when itemization, levels, buybacks, Aegis, structure state, or repeated observed fight outcomes make the original mechanism no longer representative.

## 8. Moneyline hard gates

A live Moneyline TAKE requires all universal live gates plus:

- **Lead Decomposition:** distinguish reusable lead from fragile lead. Identify which heroes hold the net worth and whether that economy converts into the next fight/objective.
- **Conversion Route:** name the realistic path from current advantage to Roshan, high ground, barracks, megas, or Ancient.
- **Comeback Route:** name the opponent's realistic swing mechanisms: smoke/pickoff, buyback fight, high-ground defense, Aegis loss, core death without buyback, split push, or scaling breakpoint.
- **Current Fight Control:** evaluate current items/levels/cooldowns/positioning, not an equalized draft fantasy.
- **Buyback Asymmetry:** a lead that disappears after one core death plus opposing buybacks is fragile.
- **High-Ground Robustness:** if the favorite must break high ground, test whether one ordinary failed siege can materially reset the game.

If the thesis requires a clean high-ground conversion but no demonstrated breach mechanism exists, HOLD.

## 9. Kill Handicap hard gates

For any live kill spread, compute exact signed margin from the selected team's perspective.

`signed_margin = selected_team_kills - opponent_kills`

Then compute the exact additional net kills required to cover the offered line. Do not use approximate language when exact arithmetic is possible.

A Kill Handicap TAKE additionally requires:

- remaining forced-fight schedule;
- expected death-timer/buyback interaction;
- whether Aegis creates extra kill opportunities or suppresses net kill gain;
- whether save/reset tools cap repeated kill conversion;
- whether high-ground/fountain proximity creates misleading late kills;
- whether split push/safe-concede routes can end or prolong the map without enough net kills.

A cushion or current kill lead alone never proves future margin expansion/suppression.

## 10. Total Kills hard gates

### Under

A Total Kills Under TAKE requires positive evidence that the future regime should remain kill-suppressing. Low current kills or passive elapsed time is insufficient.

Evaluate:

- next Roshan/Tormentor/high-ground contact requirements;
- whether one side can concede objectives safely;
- buyback-driven second-life fight multiplication;
- long death timers that can end the map with fewer extra kills;
- split-push routes that reduce direct contact;
- save/disengage/reset tools actually demonstrated under pressure;
- whether structure conversion removes future fight requirements.

### Over

A Total Kills Over TAKE requires at least two independent positive kill-producing mechanisms, such as repeated contested objectives, buyback-enabled multi-stage fights, failed high-ground sieges with resets, or demonstrated re-engage/chase loops.

Theoretical teamfight buttons alone are not enough; at least one mechanism should be observed in the live regime unless the active authority later creates a certified exception.

## 11. Duration hard gates

### Under

Name the shortest realistic close route and test it against one ordinary disruption.

Check:

- current tower/barracks access;
- Roshan/Aegis timing;
- building damage;
- glyph;
- defender buybacks;
- wave position and creep access;
- whether the lead-holding heroes can actually hit buildings safely;
- whether one failed siege pushes the clock beyond the line.

### Over

Quiet time, low kills, or intact barracks are neutral descriptors by default. A Duration Over requires at least two independent positive clock-consuming mechanisms, with at least one grounded in observed resistance, failed conversion, repeated reset, split-push delay, or another real delay mechanism.

Always test the shortest plausible sequence from next decisive fight/objective -> Roshan/high ground -> barracks/Ancient. If that route can plausibly beat the line without requiring an unusual event, the Over is not certified.

## 12. High-ground / buyback anti-simplification rule

Dota 2 high ground and buybacks must not be reduced to generic 'comeback potential.' For any decision where they matter, specify the actual mechanism:

- who can buy back;
- whether TP/rejoin is possible in time;
- which core death changes damage/control;
- whether glyph or waveclear prevents building conversion;
- whether the attacker has Aegis or a second life;
- whether a failed siege exposes Roshan/map control;
- whether barracks loss meaningfully changes future lane pressure.

If this mechanism cannot be resolved from available evidence, HOLD rather than inventing it.

## 13. Evidence hierarchy

For pregame price and context:

1. readable user-supplied current sportsbook evidence;
2. user-supplied exact current odds/line;
3. official tournament/team/roster sources;
4. reputable match/statistics sources;
5. generic web pages for secondary context.

For live state and price:

1. readable user-supplied current scoreboard/sportsbook evidence;
2. user-supplied exact text synchronized to that state;
3. official/primary data source when needed;
4. reputable secondary source;
5. generic web pages only for non-live context.

Do not replace readable current user evidence with a slower generic web source simply to duplicate-confirm it.

## 14. Execution discipline

- Pregame verdict first when an executable pregame market is supplied.
- HOLD/PASS creates no Position.
- Pregame TAKE creates one shadow Position only if all pregame gates and the active Session Authority Lock pass.
- Verdict first on active maps.
- Airtable live snapshot logging immediately after a live verdict.
- Live HOLD/PASS creates no Position.
- Live TAKE creates one shadow Position after the verdict only if executable.
- Verify every write before claiming success.
- Ordinary wins/losses do not mutate rules mid-slate.
- Postgame reviews may recommend changes but may not rewrite historical verdicts.