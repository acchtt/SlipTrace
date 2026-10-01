# Football Tournament Format & Incentive Integrity

**Status:** MANDATORY COMMON-EVIDENCE PROCEDURE  
**Applies to:** Football C official and all shadow tracks using the common evidence state  
**Purpose:** prevent route/XI strength from being mistaken for sustained goal incentive when competition format makes parity, control, aggregate protection, penalties, or margin management strategically acceptable.

## 1. Trigger

Run this check for every fixture in:
- knockout cups;
- two-legged ties;
- group-stage tournaments;
- qualifiers;
- placement/friendly tournaments with advancement or ranking consequences;
- final-round league/group matches with qualification, relegation, title, seeding, goal-difference or margin incentives;
- any user-declared tournament/cup exception.

If format or incentive may materially affect tempo, this check is mandatory before supported burden is frozen or raised.

## 2. PRE format facts — mandatory

Establish from a current authoritative source when available:

1. competition stage and format;
2. single match vs two-legged tie;
3. aggregate score if applicable;
4. whether a draw after 90 minutes leads to:
   - extra time;
   - direct penalties;
   - replay;
   - acceptable group/league outcome;
5. advancement/elimination conditions for each team;
6. relevant table/points/tiebreak state;
7. whether goal difference, goals scored, seeding, or winning margin matters;
8. whether either side is already qualified/eliminated or in a dead-rubber state;
9. whether a placement match/final/next-round path changes risk tolerance.

Do not infer "must win" from tournament branding. Verify the actual state.

## 2A. Assessment completion hard gate

Every fixture must explicitly set:

`tournament_incentive_required = true / false`

before Football C/C2 can classify it.

- If false, the structured incentive fields must explicitly be `NOT_APPLICABLE`.
- If true, the complete format/incentive block in Sections 2–3 must be present.
- Unknown facts are recorded as `UNKNOWN`; they are never silently omitted.

At Step 1, if an applicable fixture is missing the block:

`ASSESSMENT INCOMPLETE — TOURNAMENT INCENTIVE CHECK MISSING`

Do not issue C-PASS / C-WATCH / C-FOCUS or C2 state for that fixture until the block exists.

At Step 2, an applicable fixture must explicitly record:

`tournament_incentive_rechecked = true`

after the fresh post-XI/current-table recheck. Otherwise:

`DECISION BLOCKED — TOURNAMENT INCENTIVE RECHECK MISSING`

Do not issue C-BET/C-WAIT/C-PASS or C2-BET/C2-WAIT/C2-PASS from an incomplete epoch.

At live state, every goal/red card/material simultaneous-table change creates a new incentive epoch. If the incentive epoch cannot be recomputed:

`LIVE DECISION BLOCKED — TOURNAMENT INCENTIVE EPOCH MISSING`

No live Over execution is allowed from the stale incentive state.

These are evidence-completeness gates, not predictive threshold changes.

## 3. Freeze incentive state

Record for each team one or more:

- `MUST_WIN`
- `WIN_PREFERRED`
- `DRAW_ACCEPTABLE`
- `MARGIN_NEEDED`
- `PROTECT_AGGREGATE`
- `PROTECT_RESULT`
- `DEAD_RUBBER`
- `PLACEMENT_ONLY`
- `UNKNOWN`

Also freeze:

- `draw_resolution`
- `aggregate_state` when applicable;
- `tiebreak_margin_relevance = YES / NO / UNKNOWN`;
- `incentive_effect = EXPANSIVE / NEUTRAL / SUPPRESSIVE / MIXED / UNKNOWN`.

## 4. Route strength is not incentive strength

Keep these concepts separate:

- **route quality** = ability to create/finish;
- **incentive** = reason to continue taking risk at the current state;
- **persistence** = likelihood the attacking route remains active after the first goal/equaliser/lead.

A strong XI may improve route quality without improving persistence.

Do not raise supported burden merely because:
- star attackers return;
- both XIs look strong;
- the market total is high;
- a first-half goal path appears obvious.

## 5. Burden-upgrade veto

If post-XI evidence would raise the supported total above the frozen PRE burden, the upgrade is allowed only when:

1. the XI/mechanism evidence independently supports the higher burden; **and**
2. tournament incentive is not materially suppressive at the relevant likely score states; **and**
3. there is credible persistence beyond the first scoring exchange.

If `DRAW_ACCEPTABLE`, `PROTECT_AGGREGATE`, direct-penalty access, or another control state is materially relevant, do not upgrade burden solely from XI strength.

If format/incentive is `UNKNOWN`, no aggressive burden upgrade is allowed. Reduce evidence confidence or keep the prior protected burden.

## 6. Score-state matrix

Before BET/WAIT, explicitly ask:

> At 0-0, 1-0, 0-1 and 1-1, which team is actually forced to chase?

For two-leg ties also evaluate the corresponding aggregate states.

Examples:
- level score + direct penalties available -> neither team is automatically forced to chase;
- team trailing aggregate -> chase incentive may be expansive;
- team leading aggregate -> protection incentive may be suppressive;
- final group match where draw qualifies both -> strong suppression risk;
- goal-difference race -> lead may remain expansive because margin still matters.

The current score must be interpreted through competition state, not in isolation.

## 7. Step-2 requirement

Fresh post-XI research must verify whether the PRE format/incentive state has changed because of:
- other simultaneous group results;
- confirmed qualification/elimination;
- lineup rotation consistent with lower priority;
- manager statements materially changing objectives.

Persist:
- `TOURNAMENT FORMAT = VERIFIED / LIMITED / UNKNOWN`
- `INCENTIVE STATE = <home> / <away>`
- `INCENTIVE EFFECT = EXPANSIVE / NEUTRAL / SUPPRESSIVE / MIXED / UNKNOWN`

No final official BET in a tournament exception without this check unless the user explicitly overrides the missing-format uncertainty.

## 8. Live requirement

Every goal, red card, or material simultaneous-table change creates a new incentive epoch.

Recompute:
- score/aggregate;
- qualification state;
- whether a draw is now acceptable;
- whether penalties/extra time are reachable;
- whether margin is still needed;
- who is genuinely forced to chase.

A live Over target is not executable merely because the line decays. The incentive state must still support persistence.

## 9. H2H boundary

Tournament incentive does not replace H2H, and H2H does not prove incentive.

Use:
`CURRENT MECHANISM + CURRENT FORMAT/INCENTIVE -> TRANSFERABLE H2H -> OLD BACKGROUND`

## 10. Audit

On a miss, classify separately:
- `ROUTE MISS`
- `FINISHING VARIANCE`
- `PERSISTENCE MISS`
- `TOURNAMENT INCENTIVE MISS`
- `FORMAT DATA MISSING`

Never retro-change the frozen PRE state after FT.

## 11. C2 trial integrity

This procedure is an evidence-completeness requirement for the already-existing matchup/incentive concept. It does **not** change C2 selection thresholds, bridge caps, price rules, or shadow-only authority.

Any future change to C2 predictive thresholds still requires the normal challenger-version rule.
