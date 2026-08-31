# MODEL RULES — FOOTBALL v0.2.47-R

**Status:** Active  
**Scope:** Football Asian-total Over selection, prematch ranking, XI rerank, live validation, and settlement review.

This file is the consolidated source of truth for the current Football v1.0 model. It supersedes the old incremental football rule chain in the active directory.

---

## 1. Decision hierarchy

Evaluate in this order:

1. Structural quality
2. Carrier ceiling
3. Failure-mode resistance
4. Team scoring/conceding profile
5. Repeatable chance-quality profile
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
Use when the environment is good but materially dependent on one or more of:

- opponent contribution;
- rotation or cohesion;
- game state;
- uncertain finishing/creation quality;
- another identifiable failure mode.

### B / PASS
Use when the route is fragile, opponent resistance is too strong, cohesion is poor, chance quality is weak, or the required goal burden is excessive.

Two-Sided A and Elite Carrier A are peers. Do not automatically rank a balanced two-sided game above a superior one-team carrier.

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
- whether multi-goal results are repeatable or outlier-driven;
- post-lead behavior where reliable evidence exists.

Explicitly compare:

1. primary carrier GF vs opponent GA;
2. opponent GF vs primary carrier GA;
3. carrier multi-goal frequency vs opponent multi-goal concession frequency;
4. one-team carrier route vs two-sided contribution route.

League stereotype, competition reputation, or team names cannot override the actual profile.

If required profile data is unavailable or materially unreliable, cap confidence or return `NO BET — HOLD`.

---

## 5. Chance-quality gate

GF/GA and scorelines alone are not sufficient for A1.

Where data exists, inspect repeatable high-quality creation using:

- big chances;
- central / penalty-area access;
- opposition-box touches;
- cutbacks, one-v-ones, free headers, and other clear chance structures;
- shots on target quality rather than count alone;
- xG / xGOT as supporting evidence;
- repeated high-value sequences over time.

Raw shots, raw SOT, corners, possession, or a recent high-scoring result cannot independently establish an elite Over environment.

### xG rule

xG/xGOT are modifiers, not the primary engine and not automatic vetoes. The thesis should remain intelligible if xG is removed.

### Independence rule

Do not count the same attacking sequence multiple times under different labels. A single chance cannot simultaneously become several independent evidence channels merely because it produced a box touch, shot, SOT, and xG.

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

Normal XI promotion is capped at **one structural band** unless a genuine role/shape change clearly removes the original failure mode.

Heavy rotation and poor cohesion are active penalties, especially in cups and congested schedules.

Do not over-promote because recognizable attacking names start. Evaluate how the XI creates and finishes chances as a unit.

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
- attacking names start but service/shape is weak;
- dead-rubber or qualification incentives allow game management.

A structurally attractive match can remain HOLD if the failure mode is too strong.

Game-state slowdown risk should influence **goal burden**. It does not automatically disqualify an otherwise valid carrier.

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

Do not stretch to O3.25 / O3.5 / O3.75 / O4 merely for a small price increase.

Preferred principle:

**Strong structure + protected line > slightly higher odds at an unnecessarily stretched line.**

The higher the full-win goal burden, the stronger the required team profile, chance quality, and failure-mode resistance.

---

## 9. Verdict semantics / auto-lock

Final affirmative selection syntax:

`OFFICIAL LOCK — <line> @ <odds>`

Equivalent affirmative final wording that clearly selects a bet is also treated as an official lock.

The user does **not** need to separately say “lock”.

Non-bet syntax:

- `NO BET — HOLD`
- `PASS`

A conditional future threshold such as “O2.75 would clear at >=1.90” is not an official lock until the shown/current market actually meets the condition and the state is reassessed.

Never rewrite a verdict after the result.

---

## 10. Live validation

Normal live analysis validates or invalidates the **frozen prematch thesis**.

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

Prefer evidence such as:

- repeated dangerous box/central access;
- big chances;
- meaningful attacking substitutions plus actual post-sub improvement;
- repeated high-value transitions/cutbacks;
- defensive degradation;
- score-stable persistence.

Possession without penetration is not enough.

A substitution cluster is a rerank trigger, not automatic validation. Require actual post-sub chance-quality improvement before promotion.

### Goal/reset rule

After a goal, red card, major injury, or material tactical shift, reassess the current state. Do not blindly carry the previous live conclusion through a reset.

---

## 11. Incentive / dead-rubber rule

**Dead rubber:** the result has little or no effect on qualification/progression.

**Incentive uncertainty:** it is unclear whether both teams need to attack or can manage a draw, lead, rotation, or qualification state.

Do not automatically upgrade a match because attackers start or because one side “must win”.

An early goal can reduce rather than increase sustained urgency.

---

## 12. Competition exclusion

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
- apply the hard exclusions and structural filters;
- show only the filtered Over-friendly board;
- do not omit earlier kickoff blocks;
- rank by structural quality before kickoff time;
- preserve the frozen prematch rank/grade before XI or live data.

The next chronological match can be highlighted separately without changing structural rank.

---

## 14. Settlement

Full-match Asian totals settle on **90 minutes plus stoppage time only**, unless the market explicitly states that extra time is included.

Track:

- full win;
- half win;
- push;
- half loss;
- full loss.

Do not use extra-time goals to settle a standard full-match Asian total.

---

## 15. Simulations and official accounting

Counterfactual / prematch simulations performed after kickoff or after the result is known must be clearly labelled as simulations.

They may be used for process learning but must never be added to official P/L.

A missed winner after a prospective HOLD is a process observation, not a betting win.

---

## 16. Data-quality rule

Never invent missing statistics, lineups, odds, or injuries.

If a mandatory gate cannot be evaluated reliably, prefer:

`NO BET — HOLD — data incomplete`

over false precision.

---

## 17. Operating principle

**Rank structure first. Respect elite carrier ceiling. Verify the GF/GA route. Demand repeatable chance quality. Let XI change the grade, not erase the freeze. Identify the failure mode. Minimize unnecessary goal burden. Use price last. Lock automatically only when the current state actually clears.**