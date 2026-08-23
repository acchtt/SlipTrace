# Dota 2 v0.1.0-experimental — Core Model Rules

**Status:** Experimental, shadow only  
**Actual exposure:** 0u  
**Default simulated stake:** 0.25u  
**Default minimum odds:** 1.60

## 1. Scope

Initial supported live market families:

- Moneyline
- Kill Handicap
- Total Kills
- Duration

Pregame TAKEs are disabled during initial calibration. Other markets are observation-only until a dedicated rule is added.

## 2. Universal live gates

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

## 3. Draft prior

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

## 4. Moneyline hard gates

A Moneyline TAKE requires all universal gates plus:

- **Lead Decomposition:** distinguish reusable lead from fragile lead. Identify which heroes hold the net worth and whether that economy converts into the next fight/objective.
- **Conversion Route:** name the realistic path from current advantage to Roshan, high ground, barracks, megas, or Ancient.
- **Comeback Route:** name the opponent's realistic swing mechanisms: smoke/pickoff, buyback fight, high-ground defense, Aegis loss, core death without buyback, split push, or scaling breakpoint.
- **Current Fight Control:** evaluate current items/levels/cooldowns/positioning, not an equalized draft fantasy.
- **Buyback Asymmetry:** a lead that disappears after one core death plus opposing buybacks is fragile.
- **High-Ground Robustness:** if the favorite must break high ground, test whether one ordinary failed siege can materially reset the game.

If the thesis requires a clean high-ground conversion but no demonstrated breach mechanism exists, HOLD.

## 5. Kill Handicap hard gates

For any kill spread, compute exact signed margin from the selected team's perspective.

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

## 6. Total Kills hard gates

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

## 7. Duration hard gates

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

## 8. High-ground / buyback anti-simplification rule

Dota 2 high ground and buybacks must not be reduced to generic 'comeback potential.' For any decision where they matter, specify the actual mechanism:

- who can buy back;
- whether TP/rejoin is possible in time;
- which core death changes damage/control;
- whether glyph or waveclear prevents building conversion;
- whether the attacker has Aegis or a second life;
- whether a failed siege exposes Roshan/map control;
- whether barracks loss meaningfully changes future lane pressure.

If this mechanism cannot be resolved from available evidence, HOLD rather than inventing it.

## 9. Evidence hierarchy

For live state and price:

1. readable user-supplied current scoreboard/sportsbook evidence;
2. user-supplied exact text synchronized to that state;
3. official/primary data source when needed;
4. reputable secondary source;
5. generic web pages only for non-live context.

Do not replace a readable current user screenshot with a slower generic web source simply to duplicate-confirm it.

## 10. Execution discipline

- Verdict first on active maps.
- Airtable logging immediately after verdict.
- HOLD/PASS creates no Position.
- TAKE creates one shadow Position after the verdict only if executable.
- Verify every write before claiming success.
- Ordinary wins/losses do not mutate rules mid-slate.
- Postgame reviews may recommend changes but may not rewrite historical verdicts.