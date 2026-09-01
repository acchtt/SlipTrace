# Football Betting Procedure — v0.2.47-R

**Status:** Active operational procedure  
**Timezone:** Asia/Ho_Chi_Minh / ICT (UTC+7)  
**Applies to:** Daily slate ranking, prematch totals, confirmed-XI rerank, live validation, settlement, and process review.

This procedure implements `MODEL_RULES_FOOTBALL_V0.2.47-R.md`.

---

## 1. Daily slate workflow

Run the full fixture slate before ranking individual matches.

1. Collect the relevant day's fixtures.
2. Convert kickoff times to ICT.
3. Remove hard exclusions, including K League.
4. Build the mandatory team profile for credible candidates.
5. Evaluate Two-Sided and Elite Carrier routes.
6. Apply chance-quality and failure-mode priors where available.
7. Assign structural band: A1 / A2 / B+ / B-PASS.
8. Apply the reserve/youth cap before finalizing A1.
9. Rank by structural quality, not price and not kickoff time.
10. Freeze the shortlist and its structural grades before confirmed XI or live information.

When the user asks for today's/upcoming matches, display only the filtered Over-friendly board. Do not dump the full fixture list and do not omit earlier kickoff blocks.

Recommended board columns:

`Rank | ICT kickoff | Match | Frozen grade | Structural type`

Structural type should distinguish at least:

- Two-Sided
- Elite Carrier
- Elite Carrier / secondary route

### Reserve / youth handling

For Jong, U21, reserve, B-team, academy, or comparable development-team matches:

- do not promote to A1 from four-match GF/GA, recent high-total rates, or league stereotype alone;
- require stable chance-quality evidence plus XI/role continuity;
- if that evidence is missing or shallow, cap at A2;
- treat unusually large recent scorelines as possible outliers until supported by repeatable creation.

---

## 2. Structural assessment

For each shortlisted match, establish:

- primary goal route;
- whether one side has a credible solo 3+ route;
- opponent resistance;
- secondary contribution route;
- competition/format incentives;
- major failure modes.

Do not use odds to determine structural rank.

### Mandatory team profile

Before final promotion, inspect as available:

- season GF/GA;
- recent GF/GA;
- 2+ scoring frequency;
- 2+ conceding frequency;
- 3+ frequency when carrier classification requires it;
- clean-sheet / suppression tendency;
- home/away splits;
- competition-specific profile where useful.

If the profile materially conflicts with the proposed total, cap the grade or HOLD.

Short early-season samples are provisional. Do not treat four-match GF/GA as a complete profile.

### Chance quality

Before A1 promotion, inspect repeatable high-quality creation where data exists: big chances, central/box access, box touches, SOT quality, xG/xGOT as modifiers, and repeated high-value sequences.

Raw shot count is not enough.

---

## 3. Prematch freeze

A frozen assessment records what was knowable before the XI/market decision.

Store:

- match;
- competition;
- model version `v0.2.47-R`;
- frozen structural grade/type;
- primary carrier/route;
- profile summary;
- failure modes;
- evidence timestamp.

Later lineup, live, or final-score information must not rewrite the frozen state.

---

## 4. Confirmed-XI rerank

Once confirmed lineups are supplied or reliably available:

1. Compare starters with expected/strongest personnel.
2. Identify creators and finishers starting vs benched.
3. Check defensive absences and role changes.
4. Check formation/shape.
5. Check rotation and cohesion.
6. Check bench attacking depth.
7. Reassess the original failure modes.
8. Assign the post-XI grade.

Normal promotion cap is one structural band unless a genuine role/shape change removes a known failure mode.

Heavy rotation can downgrade a carrier even if the overall team remains stronger.

If a screenshot is ambiguous, state uncertainty rather than guessing.

### XI evidence enforcement

Do not create a new scoring route solely because:

- a recognizable/new striker starts;
- a defensive starter is absent for the opponent;
- attacking names appear on the bench;
- the formation looks more aggressive on paper.

An XI upgrade must strengthen a route already supported by underlying creation, or show a credible tactical/role change that directly removes the prior failure mode.

For a previously weak secondary route, require evidence of service structure, box access, repeatable creation, or comparable-role production before materially promoting it.

---

## 5. Odds and goal-burden selection

Only after structure and XI are resolved should the Asian total be chosen.

For every candidate line:

- state full-win requirement;
- state push/half-win/half-loss protection where applicable;
- compare adjacent lines;
- identify whether the extra odds justify the extra goal burden.

Prefer the lowest protected boundary that still represents the thesis at an acceptable price.

Do not stretch a total solely for a small odds gain.

Price can break a tie between similarly sound expressions; it cannot rescue weak structure.

### A2 burden enforcement

If the match is A2 and the secondary scoring route is weak/uncertain:

- do not lock O3.5+ simply because the price looks good;
- prefer O3 or O3.25 if those lines still clear;
- if protected alternatives do not clear, HOLD.

A2 may clear O3.5 only when the carrier has an exceptional independent 4+ route and failure-mode resistance is unusually strong.

### O3.75 hard gate

Before locking O3.75, explicitly answer:

1. How likely is exactly four goals?
2. How likely is five or more?
3. Can one carrier plausibly fund four/five, or is there a stable two-sided route?
4. Does confirmed XI support the full burden?
5. Is a lower protected line available for a reasonable price sacrifice?

O3.75 should normally require exceptional A1 evidence. If four looks plausible but five is not strongly supported, choose O3.5/O3.25 or HOLD.

Reserve/youth matches cannot clear O3.75 unless they first satisfy the stricter A1 stability and XI-continuity requirements.

---

## 6. Final verdict

### Official selection

If all active gates clear and the response gives an affirmative final betting selection, the selection is immediately an **OFFICIAL LOCK**.

Preferred output:

`OFFICIAL LOCK — O<line> @ <odds>`

Log it immediately to Airtable.

The user does not need to separately confirm “lock”.

### No bet

If one or more important gates do not clear:

`NO BET — HOLD`

or

`PASS`

No official P/L exposure is created.

### Conditional price threshold

A statement such as `O2.75 clears at >=1.90` is conditional only. It becomes an official lock only after the current/showed price reaches the threshold and no adverse material information invalidates the state.

---

## 7. Screenshot workflow

When the user submits lineup/odds screenshots:

1. Confirm match identity.
2. Read visible lineup, bench, absences, formation, and total/odds.
3. Do not infer invisible names or numbers.
4. Match the extracted information to the frozen assessment.
5. Run XI rerank.
6. Re-run team-profile and failure-mode checks if the XI changes the route.
7. Apply XI evidence enforcement: names/absences may strengthen demonstrated routes, not invent unsupported ones.
8. Compare available protected totals.
9. Apply A2 burden and O3.75 hard gates where relevant.
10. Issue LOCK or HOLD.
11. Log the material state.

For future website automation, vision extraction should return structured data plus confidence and permit manual correction before the verdict engine runs.

---

## 8. Live validation

Normal live analysis is prematch-thesis validation, not free-form opportunity creation.

At each material checkpoint record:

- score;
- minute/phase;
- substitutions/cards/material events;
- current chance quality;
- current total and odds if supplied;
- whether the frozen thesis is validating or failing.

### What can validate

Examples:

- repeated dangerous central/box access;
- big chances;
- meaningful post-sub attacking improvement;
- repeated high-value transitions/cutbacks;
- defensive degradation;
- score-stable persistence.

### What cannot validate by itself

- “must chase”;
- possession;
- raw shots;
- raw SOT;
- corners;
- attacker names entering;
- a favourable live score alone.

If possession is sterile or chance quality is poor, HOLD even when the score state appears Over-friendly.

### Material reset

After a goal, red card, major injury, or significant substitution/tactical cluster, reassess rather than carrying the previous verdict forward automatically.

### Just-kicked grace

A just-started match may still be treated as a normal prematch lock only while it is 0-0, no material event has occurred, no meaningful live evidence has accumulated, and the market remains effectively pre-kick.

### Manual live override

If the user explicitly asks to activate an already-live match that was not frozen, label it `MANUAL LIVE OVERRIDE` and keep it separate from normal prematch-led accounting/process review.

---

## 9. H2H handling

Historical H2H suppression is secondary evidence.

Use it to identify a persistent matchup mechanism, but do not let old low-scoring meetings veto a materially stronger current structural case when:

- current XI differs substantially;
- tactical identity has changed;
- defensive personnel/resistance has changed;
- the present carrier is demonstrably stronger.

Current structure and current chance quality take precedence. H2H is a modifier, not a default veto.

---

## 10. Settlement

For standard full-match Asian totals, use 90 minutes plus stoppage time only.

Extra time is excluded unless the market explicitly states otherwise.

Settle correctly as:

- WIN
- HALF WIN
- PUSH
- HALF LOSS
- LOSS

Do not double-count multiple decision-state rows for one official bet.

A user-confirmed final score may be used for settlement unless reliable evidence shows a conflict.

---

## 11. Process review

After settlement, evaluate the process separately from the result.

Questions:

- Was structural rank correct at the time?
- Did the GF/GA profile support the burden?
- Was chance quality correctly assessed?
- Did the XI rerank overreact or underreact?
- Did we accidentally manufacture a secondary route from names/absences?
- Was the failure mode identified?
- Was too much line protection surrendered?
- If O3.75 was selected, did the explicit 4/5-goal burden test actually clear?
- Did live evidence actually validate the thesis at the decision point?
- Was H2H used only as a modifier rather than a veto?

Do not call a HOLD wrong solely because the match later went Over.

Do not call a poor process good solely because the bet won.

---

## 12. Counterfactual simulations

If simulating a prematch decision after kickoff or after FT:

- clearly label it `SIMULATION` / `SIM-PRE`;
- use only information that would have been available at the simulated timestamp;
- keep post-kick observations out of the simulated verdict;
- never include the simulated result in official P/L.

---

## 13. Data-quality fallback

If required lineup, profile, odds, or competition information is materially incomplete, do not invent it.

Use:

`NO BET — HOLD — data incomplete`

Selectivity is a feature of the model.