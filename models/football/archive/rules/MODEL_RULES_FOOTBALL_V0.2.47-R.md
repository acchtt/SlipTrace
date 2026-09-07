# MODEL RULES — FOOTBALL v0.2.47-R

**Status:** Active  
**Operating profile:** **PRE-HARDENING**  
**Scope:** Football Asian-total Over selection, prematch ranking, XI rerank, live validation, and settlement review.

This file is the active source of truth for official football decisions.

> **Regime safeguard:** The Sep 1, 2026 hardened gates are inactive. They must not be silently reintroduced from old audits, memories, historical commits, or shadow analysis. Any hardened comparison must be explicitly labelled SHADOW and cannot affect official selections.

---

## 1. Decision hierarchy

Evaluate in this order:

1. Structural quality
2. Carrier ceiling
3. Failure-mode resistance
4. Team scoring/conceding profile
5. Chance-quality support
6. Confirmed XI
7. Goal burden / settlement protection
8. Price

**Price is a tiebreaker only.** Never promote a structurally weaker match because the odds are larger.

---

## 2. Structural ranking bands

### A1
Use for either:

- a genuine Two-Sided Tier A environment; or
- a proven Elite Carrier with a credible independent 3+ route, sustained attacking depth, repeatable creation, and acceptable opponent resistance.

### A2
Use for:

- a strong A- two-sided environment; or
- a strong carrier with one meaningful weakness.

### B+
Use when the environment is good but materially dependent on opponent contribution, rotation, game state, uncertain finishing/creation quality, or another identifiable failure mode.

### B / PASS
Use when the route is fragile, opponent resistance is too strong, cohesion is poor, chance quality is weak, or the required goal burden is excessive.

Two-Sided A and Elite Carrier A are peers. Do not automatically rank a balanced two-sided game above a superior one-team carrier.

There is **no active reserve/youth A1 hard cap**. Development-team matches may still be graded from their actual structural profile, with sample quality treated as a normal confidence consideration rather than a mandatory ceiling.

---

## 3. Elite Carrier ceiling

A favourite can rank near the top by itself when it has:

- credible independent 3+ scoring capacity;
- sustained attacking depth;
- repeatable chance creation;
- acceptable opponent resistance;
- a matchup that permits repeated access to dangerous areas.

Opponent scoring is a bonus, not a requirement.

Before penalizing weak underdog attack, ask whether the primary carrier can plausibly fund the target total alone.

Do not confuse badge/reputation with carrier capacity. The route must be supported by demonstrated production and matchup evidence.

---

## 4. Mandatory team-profile gate

For every serious candidate, evaluate as available:

- season goals for and goals against;
- relevant recent GF/GA;
- scoring 2+ frequency;
- scoring 3+ frequency when carrier status matters;
- conceding 2+ frequency;
- conceding 3+ frequency when relevant;
- clean-sheet / one-goal suppression tendency;
- home and away splits;
- competition-specific profile where useful;
- post-lead behavior where reliable evidence exists.

Explicitly compare:

1. primary carrier GF vs opponent GA;
2. opponent GF vs primary carrier GA;
3. carrier multi-goal frequency vs opponent multi-goal concession frequency;
4. one-team carrier route vs two-sided contribution route.

League stereotype, competition reputation, or team names cannot override the actual profile.

Short samples are allowed as evidence but should be identified as such. They do **not** impose an automatic grade cap.

### Recent-total / leakage confirmation rule

When a candidate's apparent A1/A2 case is driven heavily by an extreme recent sequence of high totals, repeated multi-goal concessions, or leakage-heavy scorelines:

- use those scorelines to **identify** the candidate, not to complete the proof;
- before top-board promotion or an official lock, require supporting evidence that every scoring route needed by the thesis is generating repeatable good chances;
- useful support can include multi-match big-chance production, central/box access, box touches, SOT quality, xG/xGOT trends, or stable multi-goal scoring/conceding frequencies that are not dependent on one anomalous match;
- if the secondary route is necessary for the selected burden but its chance creation is weak or unproven, reduce priority, choose a more protected line, or HOLD;
- if detailed chance-quality data is unavailable, do not invent it: treat the scoreline-driven grade with lower confidence rather than assuming the recent totals will repeat.

This is a **narrow calibration**, not a return to the Sep 1 hardened framework. It does not create a youth/reserve cap, short-sample hard cap, O3.75 gate, A2 burden prohibition, XI route-creation prohibition, or H2H override.

---

## 5. Chance quality

GF/GA and scorelines are the core profile; chance quality is a major supporting layer.

Where data exists, inspect:

- big chances;
- central / penalty-area access;
- opposition-box touches;
- cutbacks, one-v-ones, free headers, and other clear chance structures;
- shots on target quality rather than count alone;
- xG / xGOT as supporting evidence;
- repeated high-value sequences over time.

Raw shots, possession, corners, or one recent high-scoring result should not be mistaken for elite chance quality.

### xG rule

xG/xGOT are modifiers, not the primary engine and not automatic vetoes. The thesis should remain intelligible if xG is removed.

---

## 6. Confirmed-XI rerank

Confirmed XI is the first legitimate rerank gate after the structural freeze.

Check:

- creators;
- finishers;
- defensive absences;
- formation and role changes;
- starters vs bench;
- attacking depth;
- rotation;
- cohesion;
- likely substitution quality.

Normal XI promotion is capped at one structural band unless a genuine role/shape change clearly removes the original failure mode.

Heavy rotation and poor cohesion are active penalties, especially in cups and congested schedules.

Recognizable attacking names, new starters, or opponent defensive absences **can** materially improve the scoring route when the overall XI and matchup make that plausible. There is no active hard prohibition against XI creating or strengthening a route; judge it in context.

---

## 7. Failure-mode resistance

Before a final selection, state how the Over thesis can fail.

Common failure modes include:

- carrier reaches 2-0 and materially slows;
- opponent has almost no independent scoring route;
- favourite has sterile possession without central/box access;
- a team is forced to chase but still creates poor-quality chances;
- heavy rotation reduces cohesion;
- opponent can suppress central access;
- an early lead reduces urgency;
- thesis relies excessively on late goals;
- dead-rubber or qualification incentives allow game management.

A structurally attractive match can remain HOLD if the failure mode is too strong.

Historical H2H can be used normally as supporting or warning evidence. It is neither a mandatory veto nor subject to a special de-weighting rule.

---

## 8. Goal burden and protected Asian totals

Choose the Asian total only after structure, profile, chance quality, and XI.

Settlement protection matters:

- **O2.75:** exactly 3 = half win
- **O3:** exactly 3 = push
- **O3.25:** exactly 3 = half loss; 4+ = full win
- **O3.5:** 4+ = full win
- **O3.75:** exactly 4 = half win
- **O4:** exactly 4 = push

Do not stretch to a higher total merely for a small price increase.

Preferred principle:

**Strong structure + sensible protection > slightly higher odds at an unnecessarily stretched line.**

There is **no active A2 O3.5+ prohibition** and **no active O3.75 hard gate**. Higher totals remain eligible when the structural grade, carrier/two-sided route, XI, failure modes, and price collectively justify them.

---

## 9. Verdict semantics / auto-lock

Final affirmative selection syntax:

`OFFICIAL LOCK — <line> @ <odds>`

Equivalent affirmative final wording that clearly selects a bet is also treated as an official lock.

The user does not need to separately say “lock”.

Non-bet syntax:

- `NO BET — HOLD`
- `PASS`

A conditional future threshold is not an official lock until the shown/current market actually meets the condition and the state is reassessed.

Never rewrite a verdict after the result.

---

## 10. Live validation

Normal live analysis validates or invalidates the frozen prematch thesis.

It cannot create or promote an unfrozen match after kickoff merely because the live score or market looks attractive.

### Manual live override

If the user explicitly activates an already-live match, label it `MANUAL LIVE OVERRIDE` and keep it separate from the normal prematch-led workflow.

### Just-kicked grace

A just-started match may still receive a normal prematch lock when all are true:

- score remains 0-0;
- no material event has occurred;
- no meaningful live evidence has accumulated;
- the market is effectively still pre-kick.

### Live evidence rule

“Must chase” is not itself chance quality.

Prefer evidence such as repeated dangerous box/central access, big chances, meaningful attacking substitutions plus actual post-sub improvement, high-value transitions/cutbacks, defensive degradation, and score-stable persistence.

Possession without penetration is not enough.

After a goal, red card, major injury, or material tactical shift, reassess the current state.

---

## 11. Incentive / dead-rubber rule

Dead rubber means the result has little or no effect on qualification/progression.

Do not automatically upgrade a match because attackers start or because one side “must win”. An early goal can reduce rather than increase sustained urgency.

---

## 12. Competition exclusion

### Eligible cup competitions

Cup / knockout matches are excluded from the normal shortlist, XI workflow, live rescue, and official locks **unless they belong to one of these explicit exceptions**:

- **English domestic cups**, including the **FA Cup** and **EFL Cup / Carabao Cup**;
- Germany's **DFB-Pokal**;
- the **North American Leagues Cup (MLS/Liga MX)**.

The North American **Leagues Cup** is a named cross-border competition and is an explicit exception. Do **not** remove it with a generic “League Cup” exclusion rule.

### Other League Cup competitions

League Cup competitions outside the explicit English exception remain excluded, including:

- J.League / Levain Cup;
- Scottish League Cup;
- Portuguese League Cup;
- other domestic League Cup formats not explicitly approved above.

Other domestic cups and European/continental cup competitions also remain excluded unless explicitly added later. League fixtures are unaffected.

Do not re-add an excluded cup match because its scoring profile, lineup, price, or live state looks attractive.

### K League

Permanent hard exclusion.

Never rank, promote, rescue, or live-override K League matches in the normal model.

Reason: substitution, rotation, and tactical-management variance.

Do not imply integrity concerns.

---

## 13. Daily board behavior

When generating the daily/upcoming list:

- scan the full slate first;
- convert all times to ICT;
- retain league fixtures and the approved cup exceptions: English domestic cups, DFB-Pokal, and North American Leagues Cup;
- remove all other excluded cup competitions before structural ranking;
- apply other hard exclusions and structural filters;
- use the **pre-hardening** ranking logic only;
- apply the recent-total/leakage confirmation rule before promoting scoreline-driven candidates into the top focus group;
- aggressively shorten to the best few matches worth focusing on;
- do not omit earlier kickoff blocks;
- rank by structural quality before kickoff time;
- preserve the frozen prematch rank/grade before XI or live data.

A hardened comparison may be generated only as an explicitly labelled SHADOW board and must not influence official decisions.

---

## 14. Settlement

Full-match Asian totals settle on 90 minutes plus stoppage time only, unless the market explicitly states that extra time is included.

Track full win, half win, push, half loss, and full loss.

---

## 15. Simulations and official accounting

Counterfactual / prematch simulations performed after kickoff or after the result is known must be clearly labelled as simulations and never added to official P/L.

A missed winner after a prospective HOLD is a process observation, not a betting win.

---

## 16. Data-quality rule

Never invent missing statistics, lineups, odds, or injuries.

If required data is materially unreliable, reduce confidence or use `NO BET — HOLD — data incomplete`.

---

## 17. Operating principle

**Rank structure first. Respect elite carrier ceiling. Verify the GF/GA route. Use chance quality as support. Do not let extreme recent totals or leakage complete the proof by themselves. Let XI rerank the real route. Identify the failure mode. Choose the Asian total with sensible protection. Use price last. Retain English domestic cups, DFB-Pokal, and North American Leagues Cup; exclude other cup competitions before ranking. Keep the Sep 1 hardened gates inactive unless they are explicitly reactivated in a future model change.**
