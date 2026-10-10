# Football Tournament Format & Incentive Integrity

**Status:** MANDATORY COMMON-EVIDENCE PROCEDURE  
**Applies to:** Football C official and all shadow tracks using the common evidence state  
**Purpose:** prevent route/XI strength from being mistaken for sustained goal incentive when competition format makes parity, control, aggregate protection, penalties, or margin management strategically acceptable.

## 1. Trigger

Flag this check during discovery for every fixture in:
- knockout cups;
- two-legged ties;
- group-stage tournaments;
- qualifiers;
- placement/friendly tournaments with advancement or ranking consequences;
- final-round league/group matches with qualification, relegation, title, seeding, goal-difference or margin incentives;
- any user-declared tournament/cup exception.

If format or incentive may materially affect tempo, flag it at discovery/ranking and resolve it before any *actionable* supported burden is authorized or raised at Step 2.

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

## 2A. Stage-specific ranking versus executable decision requirements

**Stage 0 and Step 1 (discovery, ranking and research): non-blocking.**

Every fixture must explicitly set:
`tournament_incentive_required = true / false`.

- If false, all structured incentive fields must explicitly be `NOT_APPLICABLE`.
- If true, record all known facts and label unknown/missing facts `UNKNOWN`. Do **not** invent qualification, tiebreak or margin conclusions. A partial record can be ranked; the engine normalizes missing material fields to `UNKNOWN` only for the provisional board metadata.
- `LIMITED` / `UNKNOWN` format, qualification, simultaneous-results or incentive fields **never remove the match from Step 1 C or C2 scoring/ranking**. They yield `tournament_incentive_resolution = INCENTIVE_RECHECK_REQUIRED`, an explicit `tournament_incentive_unresolved_fields` array and `supported_line_status = PROVISIONAL_INCENTIVE`.
- C-FOCUS, C-WATCH, C-PASS and the normal operational FOLLOW/RESERVE/STOP workload lane may be produced to prioritize **research**, but they cannot be interpreted as authorization to bet. A provisional supported line is an **analysis target**, not a validated betting burden.
- Keep every unresolved tournament fixture on the research board, with its original source, identity, queue rank and flags. Do not place it on an independent hold lane that discards it from capacity. Do not fabricate tournament incentives to make a row look VERIFIED.

**Step 2 (/xi current assessment) and /live actionable epochs: hard gate.**

Before issuing **any C or C2 BET, WAIT, PASS or market/line authorization** on an applicable tournament match, the decision must contain fully resolved present-day incentive facts and independent `tournament_incentive_rechecked=true` with `tournament_incentive_recheck_status=VERIFIED`.

For an applicable fixture, resolution requires:
- `tournament_format_status = VERIFIED`, with competition stage, format, draw resolution and aggregate state properly verified;
- `qualification_state` and both teams' incentive states actually known;
- `tiebreak_margin_relevance = YES / NO`;
- `incentive_effect` resolved and no material UNKNOWN fields;
- `simultaneous_results_status = VERIFIED / NOT_APPLICABLE`, with real impact verified.

If unresolved at Step 2:

`DECISION BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED`

If the current recheck was omitted:

`DECISION BLOCKED — TOURNAMENT INCENTIVE RECHECK MISSING`

This is **a decision-specific integrity blocker only**, never justification for deleting or pre-emptively refusing the ranked fixture. The post-XI fresh verified state is a **new evidence epoch** and cannot rewrite the historical provisional Step 1 classification. User exceptions do not waive decision-stage safety.

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

- `draw_resolution`;
- `aggregate_state` when applicable;
- `qualification_state` — exact advancement/elimination/placement condition for each side;
- `tiebreak_margin_relevance = YES / NO / UNKNOWN`;
- `simultaneous_results_status = VERIFIED / NOT_APPLICABLE / LIMITED / UNKNOWN`;
- `simultaneous_results_note` — what other result(s) can change the incentive, or why none can;
- `incentive_effect = EXPANSIVE / NEUTRAL / SUPPRESSIVE / MIXED / UNKNOWN`.

For an applicable fixture, UNKNOWN/LIMITED in a material incentive field blocks action rather than merely reducing confidence.

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

If format/incentive is `LIMITED` or `UNKNOWN`, the fixture **remains eligible for Step 1 ranking and research** with a provisional burden and mandatory recheck flag. It is **not actionable** until verified at Step 2.

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

For an applicable fixture, the recheck must be VERIFIED before any final C/C2 action.

If the recheck was performed but remains LIMITED / UNKNOWN:

`DECISION BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED`

**A user-declared exception does not waive this gate.** It may reopen a STOP/RESERVE fixture for research, but the tournament state still must be resolved before an actionable verdict.

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

If the new live incentive epoch exists but qualification/tiebreak/margin/simultaneous-result consequences remain LIMITED / UNKNOWN:

`LIVE DECISION BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED`

Do not reuse the prior verified incentive epoch after a material state change.

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


## 12. Blooming-type failure guard

The following is explicitly invalid:

`tournament block provisional -> LIMITED/UNKNOWN -> bypass /xi recheck -> executable BET/WAIT/PASS`

Correct handling:

`LIMITED/UNKNOWN -> C/C2 provisional ranked board + INCENTIVE_RECHECK_REQUIRED -> resolve at /xi -> new verified evidence epoch -> C/C2 executable decision`

Do not interpret “we checked the tournament” as equivalent to “the tournament incentive is resolved.”
