# 03 — Normal Chat: Football C Official Live + C2 Shadow Wait

> **ACTIVE MODEL AIRTABLE ROUTING — 2026-10-11 (/live):** Before the first Airtable model read/write, load `models/football/airtable/ACTIVE_MODEL_ROUTING.md` and `ACTIVE_MODEL_ROUTING.json`. All new model board, C/C2 decision, live, audit, report, calibration, Website Picks and user-verified Actual Bets operations use base `appbzxqXYf0lKfD4P` and its mapped table IDs. Field names must be resolved against the new schema; old record/field/table IDs are never write targets. **The `/sweep` launcher and its Airtable routing are explicitly unchanged**, including existing Step0 handoff receipts. Do not reroute Sweep Runs or rewrite frozen Step0 rows. Model writes require same-base readback with original Coverage/Assessment/Pick/Actual Bet identity. No implicit fallback to legacy base.

> **ACTIVE ROSTER (2026-10-06):** Football C is official; Football C2 is the only shadow challenger. C3 and C4 are retired for new/current execution.

**Command alias:** `/live`

Read:
- `models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md`
- `models/football/procedures/FOOTBALL_C_C2_ACTIVE_PAIR.md`
- `models/football/CURRENT_MODEL.md`
- `models/football/production/FOOTBALL_C.md`
- `models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md`
- `models/football/procedures/FOOTBALL_TOURNAMENT_INCENTIVE_INTEGRITY.md`
- `models/football/procedures/FOOTBALL_MODEL_BET_ACCOUNTING.md`
- `models/football/procedures/FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`

Football C is official. C2 is shadow-only. C2 may never create Website Pick or real exposure.

## 1. Eligibility

Use this launcher when:
- a frozen C-WAIT reaches live state;
- a frozen C2 shadow WAIT exists and needs shadow resolution;
- a prematch Step-2 fixture has already started and was rerouted to live;
- the user explicitly requests a live exception.

Do not manufacture a C2 live state if no prospective/current C2 basis exists. A live exception does not authorize retrospective C2 reconstruction from later evidence.

### Actual paired football engine — no quote requested

For every /live or started /xi user assessment, execute the new
**quote-free** pinned runtime once with independently sourced C and C2
factors before discussing prices:

`python models/football/engine/xi_portable.py football-pair --c <c_football.json> --c2 <c2_football.json>`

Use `stage=football_assessment` with the same live score/minute,
material-event state, assessment clock and evidence epoch for both
models. Give each model its independent route/thesis assessment, using
`UNKNOWN` or null where the current event integrity is genuinely
unverified. Missing odds are **not a missing input field**, even if
the match is two, five, sixteen or forty-five minutes old.

Require `EXECUTED_C_C2_FOOTBALL_ONLY` when the paired engine actually
runs. Display C and C2 qualitative football outcomes with the
current completion/funding limitations; label the evaluation
`LIVE FOOTBALL ASSESSED — UNPRICED / NO EXECUTABLE BET` if no current
offer exists. Never demand a quote to run the football engine, and
never fall back to the price-bearing `xi_portable.py pair` to
complete an unpriced assessment. That older command remains only
for actual PREMATCH priced decisions, not started football reads.
A quote can be sought later for a separately requested betting
subdecision, but it is not the first response to a football request.

### Missing live odds is not an assessment blocker

The quote-free route in `step2_fixture_transition.py` returns
`CURRENT_LIVE_FOOTBALL_ASSESSMENT_READY` whenever the score/minute is
verified and no material mechanism recheck remains. It returns this
status with or without live odds. Quote validity is separate
(`executable_quote_status=UNPRICED_NO_EXECUTABLE_BET` when absent,
expired or prematch-only). Even when goal/event recheck is pending,
continue the football assessment and identify the exact uncertainty;
do not demand a new price to begin or complete that analysis. The
prematch-only portable decision engine must not be used on a STARTED
fixture; do not treat its quote rejection as the C/C2 football result.

### Automatic early-live takeover from /xi

**Started is not assessment blocked.** A normal /xi assessment can transition
directly into this launcher in the **same response** as soon as current
status says STARTED, without waiting for a second /live command. Invoke
`step2_fixture_transition.py` at the exact verified kickoff/current
timestamp. `EARLY_LIVE_FAST_PATH` covers the first 15 minutes;
`STANDARD_LIVE` covers later play, and **both allow assessment**.
The distinction is urgency only. A match 2, 9 or 16 minutes old is
not automatically PASS or NO BET because it started.

Carry forward the genuinely frozen, independent C and C2 research,
but freeze a **new live epoch** and verify current score/minute, any
goal/red card or material lineup/tactical change, and the live market
when available. At 0-0 with no material change, make a short check of
the existing scoring thesis rather than running the entire Step-1
research pipeline again. After any meaningful event, recompute
goal burden/continuation and relevant tournament incentives.

**Two independent levels of result:**
1. **Mandatory immediate, quote-free football assessment.** Deliver
   independent C official and C2 shadow football reads (scoring
   mechanism, frozen-thesis validity, remaining goal burden, third/
   fourth-goal continuation, stall risk, and current event context)
   without requiring, requesting or waiting for a new bookmaker quote.
   Score/minute and material football evidence determine its quality;
   neither a 2-minute nor a 16-minute kickoff delay blocks assessment.
   When no live price is independently verified, report
   `LIVE FOOTBALL ASSESSED — UNPRICED / NO EXECUTABLE BET`. This is
   a completed football read, **not** an incomplete or rejected model.
2. **Optional executable betting subdecision.** Only when actually
   considering a C BET or specific price-based WAIT, require independently
   verified **current in-play** totals and odds, current fixture/status,
   scorer/event integrity and required C/C2 live authorization and
   persistence/publication checks. No quote means no executable action.
   Do not invent a price, authorize C2 shadow as official, or use a
   previously frozen prematch price as if it were live.

An exact-prematch Step-2 engine rejection of STARTED remains a valid
protection; it must **trigger this handoff**, not terminate the user's
requested football assessment. Never claim an authorized C/C2 action
if the relevant deterministic live decision path was not run.

## 2. Common live evidence

Freeze one current live epoch for both active models:
- score and minute;
- current executable total/odds **only when an actionable BET is being evaluated**, never as a condition for football analysis;
- goals, cards, injuries, substitutions and other material events when known;
- verified tactical/mechanism changes;
- current tournament/aggregate/table state when applicable;
- draw utility;
- margin/GD/tiebreak relevance;
- which side is actually forced to chase.

A goal, red card, major injury, or material mechanism change creates a new epoch and invalidates the prior quote.

## 3. No live-stat gate

Assess the live match **regardless of provider live stats**.

Do not require or request as an execution prerequisite:
- shots / shots on target;
- xG / xGOT;
- big chances;
- dangerous attacks;
- possession;
- corners;
- box/final-third entries;
- momentum/pressure widgets.

positive live-stat confirmation is not required. The absence of positive telemetry is not negative evidence.

If the user supplies live stats, they may provide context, but they cannot by themselves approve, upgrade, downgrade, or cancel the decision.

The live football assessment must proceed from current score/minute, frozen separate C/C2 prematch/XI theses and concrete material events **even without any current quote**. New price research is solely for the optional executable betting subdecision.

## 4. Tournament incentive — every material live epoch

For a tournament/cup/qualification fixture, recompute:
- score + aggregate/table state;
- home incentive;
- away incentive;
- draw/extra-time/penalty consequence;
- margin/tiebreak relevance;
- simultaneous-result effects when relevant;
- side genuinely forced to chase;
- current incentive effect.

If the recomputation is missing:

`LIVE DECISION BLOCKED — TOURNAMENT INCENTIVE EPOCH MISSING`

If the material state remains LIMITED/UNKNOWN:

`LIVE DECISION BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED`

A user exception does not waive this integrity gate.

## 5. Football C official WAIT/live resolution

Retrieve the exact frozen C plan and its accounting state.

Core question:

`TARGET REACHED + PREMATCH/XI THESIS NOT MATERIALLY INVALIDATED?`

A target number alone never authorizes C-BET.

Clock/price decay without a goal is not thesis decay by itself.

Cancel or pass only when concrete current football information materially attacks the frozen mechanism, including:
- red card against the carrier;
- key attacking injury/substitution;
- verified tactical/mechanism deterioration;
- tournament incentive turning suppressive;
- current clearing-goal funding no longer credible.

Possible official outputs:
- `C-BET — <line> @ <odds>`
- `C-WAIT — TARGET NOT YET READY`
- `C-WAIT CANCELLED — THESIS DECAY`
- `C-PASS — NEW EPOCH INVALIDATES PLAN`

## 6. Football C2 shadow resolution

Use the same common live epoch, but apply C2's own frozen route-quality/supported-burden policy.

Possible shadow outputs:
- `C2-BET — <line> @ <odds> — SHADOW`
- `C2-WAIT — SHADOW`
- `C2-WAIT CANCELLED — SHADOW`
- `C2-PASS — SHADOW`

Do not copy C's line or action into C2.

C2 never creates a Website Pick or official exposure.

## 7. WAIT accounting integrity

Under `FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`, the frozen model-accounting state is not silently rewritten by later live observation.

For Football C:
- WAIT_ASSUMED remains the model exposure convention unless the user supplies a matching actual bet or explicitly says the target was not reached.
- a later recommendation change does not erase the already frozen accounting entry.

For C2:
- shadow WAIT accounting follows its own frozen supported target;
- it remains shadow-only.

User execution truth and model accounting remain separate.

## 8. Persistence

Persist material live changes without overwriting the frozen prematch/XI record:
- live epoch time;
- score/minute;
- current quote;
- material events;
- tournament-incentive state when applicable;
- C live action;
- C2 shadow live action;
- thesis/mechanism cancellation basis where relevant;
- user-declared target-not-reached or actual execution facts.

Do not create new C3/C4 current fields or actions.

## 9. User-facing output

Show:
- Match / score / minute
- Current line / odds
- C frozen plan
- C current official action + reason
- C2 frozen plan if available
- C2 current shadow action + reason
- tournament-incentive epoch when applicable
- exact blocker when unresolved
- accounting/user-execution distinction when relevant

Do not delay the verdict waiting for live-stat screenshots.
