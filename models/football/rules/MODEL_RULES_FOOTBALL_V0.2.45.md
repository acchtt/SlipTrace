# Football Model Rules v0.2.45 — Terminal-Goal Bridge and Leader-Driven Over

**Effective date:** 2026-08-15  
**Status:** Active audit rule  
**Supersedes:** v0.2.43 and v0.2.44 only where a goal arrives too close to halftime for the normal post-goal persistence window to exist. It does **not** remove the mandatory state reset, synchronization, settlement, style, provider-quality, or no-retrofit controls.

## Trigger

Willem II vs NEC Nijmegen exposed a specific process error. NEC scored at 45+2 to lead 0-1 at halftime after already producing the stronger pre-goal attacking process. The halftime board showed Over 2.5 at approximately 1.73. The model stayed too conservative because it treated Willem's post-goal chase as a necessary confirmation source even though there was effectively no post-goal first-half observation window and NEC itself had already demonstrated a credible multi-goal continuation route.

The later score reaching 0-4 confirms that the process assumption was too restrictive, but the missed halftime Over is **not** a shadow win because no prospective shadow verdict was delivered in that synchronized state.

The objective of v0.2.45 is prospective: prevent an unavailable post-goal observation window from becoming an automatic HOLD when high-quality pre-goal evidence already supports a leader-driven total.

## 1. Terminal-goal definition

A **terminal-half goal** is a goal scored so late in the first half that the normal v0.2.43 post-goal persistence test cannot reasonably be completed before halftime.

Operationally, treat the goal as terminal when either:

- it is scored at 42:00 or later and fewer than roughly five minutes of comparable live play remain before halftime; or
- stoppage/VAR/injury timing leaves too little uninterrupted post-goal play to obtain the normal two comparable observations.

When this occurs, label:

`POST-GOAL OBSERVATION WINDOW UNAVAILABLE — HALFTIME BRIDGE`

Do not invent a failed persistence signal from an interval that did not exist.

## 2. Mandatory reset still occurs

The goal still creates a full v0.2.43 reset.

At halftime, explicitly report:

- `Prematch style expectation:`
- `Pre-goal process:`
- `Terminal-goal bridge:` PASS / FAIL / NOT APPLICABLE
- `Leader continuation route:` STRONG / MODERATE / WEAK
- `Trailer contribution requirement:` REQUIRED / OPTIONAL
- `Halftime tactical-change risk:` LOW / MODERATE / HIGH / UNRESOLVED
- `Market implication:`

The bridge replaces only the unavailable **post-goal persistence observation**, not the reset itself.

## 3. Pre-goal evidence may carry through halftime

A terminal goal does not erase valid pre-goal process evidence.

The pre-goal state may be carried into the halftime total assessment when all of the following are true:

1. the scoring team showed sustained attacking superiority before the goal rather than a single isolated event;
2. at least **three independent primary forward channels** support continuation;
3. at least one channel is a direct chance-quality/box-production channel such as shots on target, big chances, repeated box touches, shots inside the box, or repeated dangerous entries;
4. at least one separate channel is structural or territorial, such as sustained final-third occupation, repeated possession recoveries high up the pitch, transition access, matchup-specific overloads, or persistent defensive disorganization by the opponent;
5. the goal itself is **not** counted as one of the required independent channels;
6. no red card, unresolved penalty/VAR state, major injury, or tactical event makes the pre-goal regime non-comparable;
7. the halftime market is synchronized and the selected line/odds still clear the normal minimum-price and adjacent-line gates.

xG/xGOT remain secondary only and cannot supply the required primary channels.

## 4. One-team sufficiency for an Over

A live Over does **not** require both teams to have strong scoring routes.

If the current total requires `N` additional goals to win or materially profit, the candidate may qualify as a **LEADER-DRIVEN OVER** when the leading/scoring team has a credible route to producing those additional goals itself.

A weak or sterile trailer therefore becomes a confidence and price modifier, not an automatic veto.

For a leader-driven Over with a weak trailer route, require:

- at least three independent primary continuation channels for the leader;
- evidence that the leader's attacking process is repeatable rather than score-effect dependent;
- no strong verified reason to expect an immediate low-block shutdown;
- opponent defensive stress or matchup structure that leaves further leader chances credible;
- a settlement boundary that remains attractive after accounting for the possibility that the trailer contributes nothing.

The required question is:

`Can the current leader plausibly supply the remaining goal budget by itself?`

Do not replace this with:

`Will the trailing team definitely chase?`

## 5. Trailer chase is no longer a universal Over gate

For totals, classify the trailer's post-goal role as one of:

- `ESSENTIAL` — the Over needs material trailer contribution;
- `HELPFUL` — trailer pressure improves the Over but is not necessary;
- `OPTIONAL` — the leader's continuation route can carry the goal budget alone.

Only require proven trailer chase before an Over when the selected line actually depends on trailer contribution.

Do not HOLD merely because the trailer has not yet demonstrated chase if the leader-driven branch independently clears the remaining-goal budget.

## 6. Halftime tactical-change safeguard

The terminal-goal bridge is invalidated by a material halftime regime change.

If confirmed halftime substitutions, formation changes, injury replacements, weather/pitch deterioration, or explicit tactical reporting materially alter the leader's attacking structure, return to:

`NO BET — HOLD`

until the new state is observed and synchronized.

Absence of a known tactical change is not proof of no change; use the available lineup/substitution information and state the confidence level.

## 7. Halftime fast-path

When the terminal-goal bridge passes and the halftime market is already synchronized, do **not** automatically wait 5-10 second-half minutes for confirmation.

If all applicable gates are complete at halftime, the candidate may be delivered immediately under v0.2.44 verdict-first timing.

The opening second-half interval then becomes an **invalidation/repricing check**, not a mandatory confirmation tax.

If the market is unavailable or a halftime tactical change is unresolved, HOLD for the actual unresolved reason.

## 8. Arm A and Arm B treatment

### Arm A — Current audit model

A terminal-goal bridge may support `SHADOW LEAN — DO NOT PLACE` only if the full Arm A validator, style, synchronization, market-family, settlement, and audit gates pass.

### Arm B — Early totals benchmark

Arm B should give extra weight to the terminal-goal bridge because its purpose is to test whether the earlier totals framework identifies valid remaining-goal branches faster than the more conservative current stack.

Arm B may output `BENCHMARK SHADOW — DO NOT PLACE` at halftime without a second-half confirmation snapshot when the bridge, exact-line, two/three-channel requirement, adjacent-line comparison, adverse-branch test, and NO-BET comparator all pass.

## 9. Required live fields

For any halftime total assessment following a terminal goal, include:

- `Terminal-goal bridge:` PASS / FAIL / N/A
- `Leader continuation route:` STRONG / MODERATE / WEAK
- `Trailer role:` ESSENTIAL / HELPFUL / OPTIONAL
- `Remaining-goal budget:` exact number required for push / half-win / full-win where applicable
- `Halftime tactical-change risk:` LOW / MODERATE / HIGH / UNRESOLVED
- `Timing status:` ON TIME / VALID HOLD / LATE / STATE-CHANGE RACE

## 10. Willem II vs NEC process lesson

At halftime, NEC led 0-1 after a late 45+2 goal. The pre-goal process was already materially NEC-favored, including multiple shots on target, big chances, repeated box occupation and territorial control. The key model error was not simply failure to predict Willem's chase; it was treating Willem's chase as too central to the Over thesis when NEC itself had a credible continuation route.

The later move to 0-4 is retained only as a **process diagnostic**. It must never be recorded as a winning shadow selection unless a prospectively synchronized verdict existed before the relevant goals.

## Operating principle

When a late goal leaves no honest post-goal observation window, do not manufacture a confirmation requirement that cannot be satisfied. Carry forward strong pre-goal process through the halftime reset, test whether the leader can fund the remaining goal budget by itself, and decide on the synchronized halftime price. Trailer chase is evidence when needed, not a ritual prerequisite.