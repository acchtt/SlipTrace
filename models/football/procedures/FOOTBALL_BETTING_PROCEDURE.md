# Football Betting Procedure — v0.2.47-R

**Status:** Active operational procedure  
**Operating profile:** **PRE-HARDENING**  
**Timezone:** Asia/Ho_Chi_Minh / ICT (UTC+7)  
**Applies to:** Daily slate ranking, prematch totals, confirmed-XI rerank, live validation, settlement, and process review.

This procedure implements `MODEL_RULES_FOOTBALL_V0.2.47-R.md`.

> **Safeguard:** Do not apply the Sep 1, 2026 hardened gates in official selection. Hardened analysis is shadow-only unless the model is explicitly changed again.

---

## 1. Daily slate workflow

1. Collect the full relevant-day fixture slate.
2. Convert kickoff times to ICT.
3. Retain league fixtures plus these approved cup exceptions: **English domestic cups** (including FA Cup and EFL/Carabao Cup), Germany's **DFB-Pokal**, and the **North American Leagues Cup (MLS/Liga MX)**.
4. Remove all other cup / knockout competitions, including other domestic League Cup formats and European/continental cups.
5. Remove other hard exclusions, including K League.
6. Build the mandatory team profile for credible candidates.
7. Evaluate Two-Sided and Elite Carrier routes.
8. Use chance quality and failure modes as supporting evidence.
9. Apply the **recent-total / leakage confirmation rule** to candidates whose apparent strength is driven heavily by extreme recent totals or repeated defensive leakage.
10. Assign structural band: A1 / A2 / B+ / B-PASS.
11. Rank by structural quality, not price and not kickoff time.
12. Aggressively shorten the board to the best few matches worth focusing on.
13. Freeze that shortlist and its structural grades before confirmed XI or live information.

When the user asks for today's/upcoming matches, show only the focused Over-friendly board and do not omit earlier kickoff blocks.

Competition exclusions are applied **before ranking**. The North American **Leagues Cup** is an explicit approved exception and must not be removed by a generic “League Cup” filter. Do not surface other excluded cup fixtures as backups or rescue them later because of lineup, odds, or live evidence.

Recommended board columns:

`Rank | ICT kickoff | Match | Frozen grade | Structural type`

There is no active reserve/youth hard ceiling. Development-team matches are judged from their actual profile, with sample size treated as normal confidence context.

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

Inspect as available:

- season GF/GA;
- recent GF/GA;
- 2+ scoring frequency;
- 2+ conceding frequency;
- 3+ frequency when carrier classification requires it;
- clean-sheet / suppression tendency;
- home/away splits;
- competition-specific profile where useful.

Short early-season samples are usable but provisional; they do not impose automatic grade caps.

### Recent-total / leakage confirmation

If a candidate is being promoted mainly because of an extreme recent run of high totals or repeated multi-goal concessions:

1. Mark the thesis as **scoreline/leakage-driven**.
2. Identify which scoring routes are actually required for the proposed total.
3. Seek supporting evidence that those routes are producing repeatable good chances: multi-match big chances, central/box access, box touches, SOT quality, xG/xGOT trend, or stable multi-goal scoring/conceding frequency beyond one anomalous match.
4. If one required secondary route has weak or unproven chance creation, do not let the recent totals alone promote the match into top focus.
5. Respond by reducing priority, choosing a more protected total, or using `NO BET — HOLD`.
6. If detailed chance-quality data is unavailable, lower confidence rather than assuming the high-total run will persist.

This is a narrow confirmation rule only. It does **not** revive the Sep 1 hardened youth cap, burden gates, XI prohibition, H2H rule, or any general short-sample cap.

### Chance quality

Where available, inspect big chances, central/box access, box touches, SOT quality, and xG/xGOT as modifiers. Do not let raw possession or shot volume substitute for actual threat.

---

## 3. Prematch freeze

Store:

- match;
- competition;
- model version `v0.2.47-R`;
- operating profile `PRE-HARDENING`;
- frozen structural grade/type;
- primary carrier/route;
- whether the case is materially scoreline/leakage-driven;
- profile summary;
- chance-quality confirmation when the recent-total/leakage rule is triggered;
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
8. If the match was scoreline/leakage-driven, verify that XI changes do not substitute for missing evidence of repeatable chance creation.
9. Assign the post-XI grade.

Normal promotion cap is one structural band unless a genuine role/shape change removes a known failure mode.

Recognizable attackers, new starters, or opponent defensive absences may materially improve a route when the overall XI and matchup support it. There is no active hard prohibition against XI creating or strengthening a scoring route.

---

## 5. Odds and goal-burden selection

Only after structure and XI are resolved should the Asian total be chosen.

For every candidate line:

- state full-win requirement;
- state push/half-win/half-loss protection where applicable;
- compare adjacent lines;
- identify whether the extra odds justify the extra goal burden.

Prefer a protected boundary when it reasonably expresses the thesis, but do not impose a mandatory A2 ceiling or O3.75 ban.

Higher totals remain eligible when structure, carrier/two-sided route, XI, failure modes, and price justify them.

For a scoreline/leakage-driven candidate with incomplete chance-quality confirmation, prefer more protection or HOLD rather than stretching the burden based on recent totals alone.

---

## 6. Final verdict

If all active gates clear and the response gives an affirmative final betting selection, it is immediately an **OFFICIAL LOCK**.

Preferred output:

`OFFICIAL LOCK — O<line> @ <odds>`

Log it immediately to Airtable.

If one or more important gates do not clear:

`NO BET — HOLD`

or

`PASS`

A conditional price threshold is not an official lock until the current market reaches it and the state is reassessed.

---

## 7. Screenshot workflow

When the user submits lineup/odds screenshots:

1. Confirm match identity and competition.
2. Confirm the competition is either a league fixture or one of the approved cup exceptions: English domestic cups, DFB-Pokal, or North American Leagues Cup. If not, stop the normal betting workflow and mark it excluded.
3. Read visible lineup, bench, absences, formation, and total/odds.
4. Do not infer invisible names or numbers.
5. Match the extracted information to the frozen assessment.
6. Run XI rerank.
7. Re-run team-profile and failure-mode checks if the XI changes the route.
8. If the frozen case was recent-total/leakage-driven, confirm the supporting chance-quality evidence before final promotion.
9. Compare available Asian totals and protection.
10. Issue LOCK or HOLD.
11. Log the material state.

Do **not** run or revive the Sep 1 hardened gates as hidden checks.

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

What can validate: repeated dangerous box/central access, big chances, meaningful post-sub attacking improvement, high-value transitions/cutbacks, defensive degradation, score-stable persistence.

What cannot validate by itself: “must chase”, possession, raw shots, raw SOT, corners, attacker names entering, or a favourable live score alone.

After a goal, red card, major injury, or significant tactical shift, reassess the current state.

### Just-kicked grace

A just-started match may still be treated as a normal prematch lock only while it is 0-0, no material event has occurred, no meaningful live evidence has accumulated, and the market remains effectively pre-kick.

### Manual live override

If the user explicitly asks to activate an already-live match that was not frozen, label it `MANUAL LIVE OVERRIDE` and keep it separate from normal prematch-led accounting/process review.

The manual-live mechanism does **not** override the competition exclusion. Only league fixtures and the approved cup exceptions remain eligible.

---

## 9. H2H handling

Historical H2H may be used as normal supporting or warning evidence. There is no active mandatory de-weighting rule and no automatic veto.

Judge whether the matchup mechanism remains relevant to the current teams and XI.

---

## 10. Settlement

For standard full-match Asian totals, use 90 minutes plus stoppage time only.

Extra time is excluded unless the market explicitly states otherwise.

Settle correctly as WIN, HALF WIN, PUSH, HALF LOSS, or LOSS.

Do not double-count multiple decision-state rows for one official bet.

A user-confirmed final score may be used for settlement unless reliable evidence shows a conflict.

---

## 11. Process review

After settlement, evaluate process separately from result:

- Was structural rank correct at the time?
- Did the GF/GA profile support the burden?
- Was the candidate overly dependent on an extreme recent total/leakage run?
- If so, was there enough evidence of repeatable good chance creation for every necessary route?
- Was chance quality used appropriately?
- Did the XI rerank overreact or underreact?
- Was the failure mode identified?
- Was too much line protection surrendered?
- Did live evidence actually validate the thesis at the decision point?

Do not call a HOLD wrong solely because the match later went Over. Do not call poor process good solely because the bet won.

Hardened-model comparisons may be recorded only as **SHADOW** observations and must not retroactively alter official decisions.

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

Use `NO BET — HOLD — data incomplete` when appropriate.

---

## 14. Shadow hardening benchmark

If we continue studying the hardened framework, it must be kept explicitly separate:

- label all rows / outputs `SHADOW — HARDENED`;
- no official locks from that framework;
- no influence on official shortlist ordering;
- no hidden rerank penalties;
- no automatic reactivation from past audits;
- only reactivate through an explicit future model change.
