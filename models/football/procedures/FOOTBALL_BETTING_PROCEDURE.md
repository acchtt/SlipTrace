# Football Betting Procedure — v0.2.47 CLEAN + v0.2.48 SHADOW

**Status:** Active operational procedure  
**Timezone:** Asia/Ho_Chi_Minh / ICT (UTC+7)  
**Official model:** Football v0.2.47 CLEAN  
**Shadow model:** Football v0.2.48-SHADOW  
**Applies to:** Daily slate coverage, prematch ranking, confirmed-XI rerank, Asian-total selection, live validation, settlement, and process review.

This procedure operates the clean `MODEL_RULES_FOOTBALL_V0.2.47.md` as the official model and runs `MODEL_RULES_FOOTBALL_V0.2.48-SHADOW.md` in parallel. `MODEL_RULES_FOOTBALL_V0.2.47-R.md` is archived and is not part of the active workflow.

`FOOTBALL_COVERAGE_CONTROLLER.md` is a mandatory precondition before ranking or publishing a daily/upcoming board.

> **Safeguard:** Do not silently reactivate the Sep 1, 2026 hardened gates. Only the explicit v0.2.48 shadow patches are active on the shadow track.

---

## 1. Daily slate workflow

### Phase A — coverage first

1. Run `FOOTBALL_COVERAGE_CONTROLLER.md` for the requested time window.
2. Build the union of fixture sources, normalize to ICT, and persist the universe to Airtable `Daily Coverage Ledger`.
3. Apply competition eligibility and hard exclusions.
4. Do **not** prefilter by attractiveness, team reputation, market odds, or convenience.
5. Give every eligible fixture a PRE structural disposition.
6. Assign FOCUS / WATCHLIST / PASS / UNRESOLVED.
7. Reconcile coverage counts before claiming the board is complete.
8. If counts do not reconcile, use `COVERAGE INCOMPLETE — board provisional`.

### Phase B — structural ranking

For every eligible fixture, assess as available:

- team GF/GA profile;
- recent GF/GA;
- 2+/3+ scoring and conceding frequency;
- home/away context;
- carrier ceiling;
- secondary contribution route;
- opponent resistance/suppression;
- competition/format incentives;
- recent-total/leakage dependence;
- chance-quality support where required/available;
- primary failure mode.

Assign official clean PRE grade:

- A1
- A2
- B+
- B / PASS
- DATA INCOMPLETE

Record both model PRE dispositions in the coverage ledger.

### Phase C — display

Only after all eligible fixtures are screened:

- show the best FOCUS matches prominently;
- optionally show WATCHLIST compactly;
- keep PASS fixtures out of the normal visible board unless the user requests full coverage;
- preserve FOCUS and WATCHLIST internally.

**Display shortening is not screening shortening.**

Recommended visible columns:

`Rank | ICT kickoff | Match | v0.2.47 PRE | v0.2.48 PRE | Structural type | Tier`

Include a coverage line:

`Coverage: Universe | Eligible | Screened | Focus | Watch | Pass | Unresolved`

---

## 2. Competition eligibility

Retain:

- league fixtures except hard-excluded leagues;
- English domestic cups: FA Cup and EFL/Carabao Cup;
- DFB-Pokal;
- North American Leagues Cup (MLS/Liga MX).

Exclude:

- K League;
- Belgian Pro League / Jupiler Pro League;
- all other domestic/continental/League Cup competitions unless explicitly added later.

The North American **Leagues Cup** is an explicit exception and must not be removed by a generic “League Cup” filter.

Excluded fixtures remain in the coverage ledger with an explicit reason. Exclusion is not omission.

---

## 3. Structural assessment

For every eligible fixture, establish:

- primary goal route;
- whether one side has a credible solo 3+ route;
- opponent resistance;
- secondary contribution route;
- competition/format incentives;
- major failure modes.

Do not use odds to determine structural rank.

### Mandatory team profile

Inspect as available:

- season goals for and against;
- recent GF/GA;
- scoring 2+ frequency;
- scoring 3+ frequency when carrier status matters;
- conceding 2+ frequency;
- conceding 3+ frequency when relevant;
- clean-sheet / one-goal suppression tendency;
- home/away splits;
- competition-specific profile where useful;
- post-lead behavior where reliable evidence exists.

Short early-season samples are usable but provisional; they do not impose automatic grade caps.

### Recent-total / leakage confirmation

If a candidate is being promoted mainly because of an extreme recent run of high totals or repeated multi-goal concessions:

1. mark the thesis as scoreline/leakage-driven;
2. identify which scoring routes are required for the proposed total;
3. seek supporting evidence that those routes are producing repeatable good chances: multi-match big chances, central/box access, box touches, SOT quality, xG/xGOT trend, or stable multi-goal frequencies beyond one anomalous match;
4. if one required secondary route has weak or unproven creation, do not let recent totals alone complete the promotion;
5. if detailed chance-quality data is unavailable, lower confidence rather than inventing evidence.

On the official v0.2.47 track this remains a narrow confirmation rule, not a general hard cap.

The shadow v0.2.48 track applies its explicit stronger recent-total/leakage patch separately after receiving the same evidence state.

### Chance quality

Where available, inspect big chances, central/box access, box touches, SOT quality, and xG/xGOT as supporting evidence. Do not let raw possession or raw shot volume substitute for actual threat.

---

## 4. Prematch freeze

For every FOCUS and relevant WATCHLIST match, freeze the PRE state before XI.

Store:

- match;
- competition;
- evidence timestamp;
- coverage status;
- official model version `v0.2.47`;
- shadow model version `v0.2.48-SHADOW`;
- frozen structural grade/type;
- board tier;
- primary carrier/route;
- secondary route;
- whether the case is materially scoreline/leakage-driven;
- profile summary;
- chance-quality support where relevant;
- failure modes.

Later XI, market, live, or FT information must not rewrite the frozen PRE state.

---

## 5. Same-window rerank / anti-sunk-cost

Before confirmed XI and again after confirmed XI:

1. collect all surviving FOCUS + WATCHLIST matches in the practical kickoff window;
2. compare them head-to-head by structure;
3. preserve each frozen PRE state;
4. rerank from XI without rebuilding from scratch;
5. if the previous top match is downgraded, promote the next strongest surviving match immediately;
6. do not keep a weakened candidate on top simply because monitoring already started.

A WATCHLIST match remains alive until explicit downgrade, kickoff, or exclusion.

This step is mandatory when multiple plausible matches overlap.

---

## 6. Confirmed-XI rerank

Once confirmed lineups are supplied or reliably available:

1. compare starters with expected/strongest personnel;
2. identify creators and finishers starting vs benched;
3. check defensive absences and role changes;
4. check formation/shape;
5. check rotation and cohesion;
6. check bench attacking depth;
7. reassess the original failure mode;
8. if the match was scoreline/leakage-driven, do not let lineup names substitute for missing repeatable chance-quality evidence;
9. assign the post-XI official grade;
10. run the v0.2.48 shadow delta on the same XI state;
11. update XI Status in the coverage ledger.

Normal official XI promotion is capped at one structural band unless a genuine role/shape change removes a known failure mode.

Recognizable attackers, new starters, or opponent defensive absences may materially improve a route when the overall XI and matchup support it. There is no active official hard prohibition against XI creating or strengthening a route.

---

## 7. Odds and goal-burden selection

Only after structure and XI are resolved should the Asian total be chosen.

For every candidate line:

- state the full-win requirement;
- state push/half-win/half-loss protection where applicable;
- compare adjacent lines;
- identify whether extra odds justify extra goal burden.

Official v0.2.47 principle:

**Strong structure + sensible protection > slightly higher odds at an unnecessarily stretched line.**

There is no official A2 O3.5+ hard prohibition and no official O3.75 hard gate.

The shadow v0.2.48 track separately applies its no-rescue and carrier-led O2.75+ hardening patches.

Use the exact same market snapshot for both tracks.

---

## 8. Dual-model verdict

For a match that reaches final evaluation, output both tracks.

### Official v0.2.47 CLEAN

If all official gates clear:

`OFFICIAL LOCK — O<line> @ <odds>`

Otherwise:

- `NO BET — HOLD`
- `PASS`

Any affirmative official selection is immediately an official lock and must be logged to `Website Picks` / decision-state control according to the active Airtable contract.

### v0.2.48-SHADOW

If the shadow candidate clears:

`SHADOW LOCK — O<line> @ <odds> — DO NOT PLACE`

Otherwise:

- `SHADOW HOLD`
- `SHADOW PASS`

Shadow outcomes do not enter official P/L.

Do not let one track's verdict suppress the other track's output.

---

## 9. Airtable logging

### Coverage

Use `Daily Coverage Ledger` for:

- fixture-universe membership;
- eligibility/exclusion;
- coverage status;
- PRE grade/type;
- FOCUS/WATCHLIST/PASS state;
- v0.2.47 PRE disposition;
- v0.2.48 PRE disposition;
- XI/market stage status.

### Decision States

Use `Decision States` for material model states.

Official rows use model version:

`v0.2.47`

Shadow rows use:

`v0.2.48-SHADOW`

For a shadow lock use verdict `SHADOW LEAN — DO NOT PLACE` in Airtable while user-facing wording remains `SHADOW LOCK — ... — DO NOT PLACE`.

For a shadow hold use `NO BET — HOLD` with model version `v0.2.48-SHADOW`.

Do not rewrite historical `v0.2.47-R` records.

---

## 10. Screenshot workflow

When the user submits lineup/odds screenshots:

1. confirm match identity and competition;
2. verify it exists in the coverage ledger or immediately classify it as late-discovered;
3. confirm competition eligibility;
4. read visible lineup, bench, absences, formation, and total/odds precisely;
5. do not infer invisible names or numbers;
6. match extracted information to frozen PRE;
7. run XI rerank;
8. rerank same-window surviving FOCUS/WATCHLIST candidates if relevant;
9. re-run team-profile/failure-mode checks if XI changes a route;
10. compare available Asian totals and protection;
11. issue both official and shadow verdicts;
12. log both material states.

Do not run or revive Sep 1 hardened gates as hidden official checks.

---

## 11. `What's next?` workflow

When the user asks `what's next?`, `upcoming matches`, or similar after a daily slate was already screened:

1. read the persisted `Daily Coverage Ledger` for that slate;
2. select the earliest future FOCUS match;
3. if no FOCUS match remains, surface the strongest future WATCHLIST match;
4. include other same-window FOCUS/WATCHLIST candidates that remain relevant;
5. do not rebuild a fresh partial fixture list from memory;
6. if the ledger is stale or coverage-incomplete, reconcile the affected window before answering.

---

## 12. Late discovery

If a new eligible fixture appears before kickoff:

`LATE-DISCOVERED BUT SCREENED`

Screen it immediately and insert it normally into FOCUS/WATCHLIST/PASS.

If first discovered after kickoff and it was never properly assessed before kickoff:

`TRUE MISSED SCREEN`

Do not retroactively pretend it was screened.

A just-kicked grace or explicit manual-live override remains a separate betting-state rule; late discovery does not automatically authorize a live bet.

---

## 13. Live validation

Normal live analysis validates or invalidates the frozen prematch thesis; it is not free-form opportunity creation.

At each material checkpoint record:

- score;
- minute/phase;
- substitutions/cards/material events;
- current chance quality;
- current total and odds if supplied;
- whether the frozen thesis is validating or failing.

What can validate:

- repeated dangerous box/central access;
- big chances;
- meaningful post-sub attacking improvement;
- high-value transitions/cutbacks;
- defensive degradation;
- score-stable persistence when supported by quality.

What cannot validate by itself:

- “must chase”;
- possession;
- raw shots;
- raw SOT;
- corners;
- attacker names entering;
- a favourable live score alone.

After a goal, red card, major injury, or significant tactical shift, reassess the current state.

### Just-kicked grace

A just-started match may still be treated as a normal prematch lock only while:

- score remains 0-0;
- no material event has occurred;
- no meaningful live evidence has accumulated;
- the market remains effectively pre-kick.

### Manual live override

If the user explicitly activates an already-live match that was not frozen, label it `MANUAL LIVE OVERRIDE` and keep it separate from normal prematch-led accounting/process review.

Competition exclusions still apply.

### v0.2.47 halftime compression

The clean v0.2.47 high-scoring halftime compression / goal-saturation rule remains active for relevant post-HT decisions.

The v0.2.48 shadow track inherits that clean rule and then applies its own explicit shadow deltas.

---

## 14. H2H handling

Historical H2H may be used as normal supporting or warning evidence. There is no active official mandatory de-weighting rule and no automatic veto.

Judge whether the matchup mechanism remains relevant to the current teams and XI.

---

## 15. Settlement

For standard full-match Asian totals, use 90 minutes plus stoppage time only unless the market explicitly includes extra time.

Settle correctly as:

- WIN
- HALF WIN
- PUSH
- HALF LOSS
- LOSS
- VOID when applicable

Do not double-count multiple decision-state rows for one official bet.

Shadow settlement is tracked separately for model comparison and never enters official P/L.

---

## 16. Process review

Audit three separate layers:

### Coverage

- Was every eligible fixture discovered?
- Did counts reconcile?
- Was a worthwhile match lost before PRE?
- Was a WATCHLIST candidate forgotten when the top choice weakened?

### Ranking / model

- Was structural rank correct at the time?
- Did GF/GA support the burden?
- Was the thesis overly dependent on recent totals/leakage?
- Was chance quality used appropriately?
- Did XI rerank overreact or underreact?
- Was the failure mode identified and resolved?
- Was the line expression appropriate?

### Result

- Did the bet win or lose?
- Was outcome variance consistent with the prematch process?

Use these labels:

- SCREENED
- LATE-DISCOVERED BUT SCREENED
- TRUE MISSED SCREEN
- RANKING MISS
- FALSE-NEGATIVE HOLD
- BAD LOCK
- CORRECT HOLD, OVER LANDED

Do not call a HOLD wrong solely because the match later went Over. Do not call poor process good solely because the bet won.

---

## 17. Counterfactual simulations

If simulating a prematch decision after kickoff or FT:

- label it `SIMULATION` / `SIM-PRE`;
- use only information that would have been available at the simulated timestamp;
- keep post-kick observations out of the simulated verdict;
- never include the simulated result in official P/L;
- keep official and shadow simulated tracks distinct.

---

## 18. Data-quality fallback

If required fixture reconciliation, lineup, profile, odds, or competition information is materially incomplete, do not invent it.

Use one of:

- `COVERAGE INCOMPLETE — board provisional`
- `NO BET — HOLD — data incomplete`

as appropriate.

---

## Operating principle

**Coverage first. Every eligible fixture gets a disposition. Shorten the display, not the screened universe. Persist FOCUS and WATCHLIST. Rerank same-window survivors at XI. Use identical evidence snapshots for v0.2.47 CLEAN and v0.2.48-SHADOW. Keep official P/L separate from shadow comparison.**