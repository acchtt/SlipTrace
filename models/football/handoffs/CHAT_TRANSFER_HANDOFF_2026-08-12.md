# Football v1.0 — Cross-Chat Transfer Handoff — 2026-08-12

**Repository:** `acchtt/SlipTrace`  
**Canonical namespace:** `models/football/`  
**Active model:** **Football v0.2.43 — AUDIT MODE**  
**Official football betting:** PAUSED  
**Execution mode:** SHADOW CALIBRATION ONLY  
**Ledger writes:** ON HOLD until explicit user approval

## 1. Purpose

This file is the authoritative cross-chat continuation note for the current Football v1.0 work. It preserves the operational reasoning framework, audit discipline, recent model corrections, current shadow research state, and the latest user-directed workflow.

It does not preserve private hidden chain-of-thought. It preserves the explicit decision procedure, evidence hierarchy, state transitions, model lessons, and prospective rules needed to reproduce the same analysis in a new chat.

The accidental League of Legends message near the end of the prior chat is explicitly **DISCARDED** and must not affect football state, records, calibration, or model logic.

## 2. Mandatory startup

Load `models/football/CURRENT_MODEL.md` first and obey its current load order. Newer rule files override older conflicts. Do not rely on the 2026-08-06 handoff for active version, stake policy, or current audit status.

At startup, acknowledge the following before analyzing a match:

- FOOTBALL FILES LOADED
- active version and audit mode
- canonical namespace `models/football/`
- official football betting paused
- ledger writes on hold
- strict v0.2.43 team-style layer active
- early-totals benchmark active as a separate research arm

If canonical context is incomplete, use `NO BET — MODEL CONTEXT INCOMPLETE`.

## 3. Core operating controls

Preserve these controls strictly:

- 1u = 1,000,000 VND.
- Minimum odds reference = 1.70.
- Normal shadow small-test stake used in the current audit examples = 0.125u = 125,000 VND unless a newer canonical rule supersedes this.
- Official football betting remains paused until audit exit criteria are met and the user explicitly approves resumption.
- A wager is never official merely because the model likes it; confirmed placement is required when official mode is eventually restored.
- Directional AH/DNB/ML selections remain quarantined from official promotion.
- Ledger writes remain on hold until explicitly authorized.
- xG/xGOT are secondary only and may be discarded when provider quality is unreliable.
- Every material assessment must preserve exact score/minute/line/odds synchronization.
- Competition format, venue, aggregate state, qualification incentives, and market settlement scope must be verified when material.
- One best expression per assessment; do not stack correlated positions.
- Invalidating one side does not validate the opposite side.
- Do not retrofit rules after results. Record genuine misses as misses.

## 4. Mandatory verdict language during audit

While audit mode is active, use only research-safe verdicts:

- `SHADOW LEAN — DO NOT PLACE`
- `BENCHMARK SHADOW — DO NOT PLACE`
- `NO BET`
- `NO BET — HOLD`

Do not issue `OFFICIAL BET` while audit mode is active.

When a market is merely interesting but not qualified, say `WATCH` or `NO BET — HOLD`, not an executable instruction.

## 5. Strict team-style requirement — v0.2.43

Before every serious match preview, and before the first live recommendation in a match, profile both teams using verifiable current evidence.

For each team include:

- base build-up style;
- main attacking routes;
- tempo;
- defensive block/press;
- transition behaviour;
- chance-generation signature;
- typical behaviour after taking a lead;
- typical behaviour after falling behind;
- expected matchup-specific adaptation;
- confidence level / sample caveat.

Do not use generic labels from reputation alone. Distinguish base style from expected matchup style.

The style profile must be opponent-adjusted. A possession-dominant domestic favorite may become transition-oriented against a stronger opponent. A low-block team may press more aggressively when elimination utility requires it.

If the style profile cannot be adequately verified, mark `STYLE PROFILE INCOMPLETE` and cap the prematch verdict at `NO BET — HOLD`.

## 6. Strict post-goal requirement

Every goal causes a tactical/state reset. A future chat may not justify a live Over merely by saying the trailing team must chase or the leader will have counters.

After a goal, explicitly assess:

- `Prematch style expectation:`
- `Leader post-goal behaviour:`
- `Trailer post-goal behaviour:`
- `Style deviation:` AS EXPECTED / MORE OPEN THAN EXPECTED / MORE CLOSED THAN EXPECTED / STYLE BREAK-UNRESOLVED
- `Post-goal persistence:`
- `Market implication:`

Normally require two comparable post-goal observations, or one observation plus strong event-level evidence across a meaningful interval, before promoting a new shadow candidate.

For Overs, verify real chase/transition production through actual box access, shots, SOT, set pieces, substitutions, defensive degradation, or independent scoring routes. For Unders, verify actual suppression/sterility rather than elapsed time alone.

Post-goal behavior should eventually be modeled as a team characteristic, not only a generic score-state effect. Useful categories include front-foot leader, control leader, low-block protector, counter leader, aggressive chaser, sterile chaser, collapse-prone, and resilient/resetting team. These are descriptive buckets only; evidence must support the classification.

## 7. Evidence hierarchy and live synchronization

At every live checkpoint:

1. Confirm exact score and clock.
2. Identify every material event since the prior snapshot: goal, penalty, red card, substitution cluster, injury, tactical shift, weather/pitch change.
3. If a material event occurred, reset the state.
4. Separate cumulative match data from the most recent interval when possible.
5. Use non-xG forward-looking evidence first.
6. Compare actual play with the prematch style expectation.
7. Evaluate both scoring and conceding routes.
8. Scan all major available market families, not just the previously discussed line.
9. Compare adjacent Asian-total lines and settlement protection.
10. Reprice after material line movement, odds movement, stale timestamps, or a major event.

Primary live channels include shots/SOT, box access, independent attacking sequences, big chances when provider quality is credible, corners/set pieces, transitions, defensive spacing/errors, substitutions, goalkeeper workload, fatigue/cards, and score/competition utility.

xG/xGOT are secondary diagnostics. If a provider feed is visibly bugged or internally inconsistent, discard it rather than trying to force it into the verdict.

## 8. Current audit research design

The model is testing two parallel research arms:

### Arm A — Current audit model

Football v0.2.43 with the full validator, strict style profile, post-goal reset, market-family scan, and directional quarantine.

### Arm B — Early-totals benchmark

A reconstructed v0.2.6-v0.2.9 live-total philosophy using current synchronization and provider-quality controls. It focuses on:

- live totals only;
- remaining-goal branches;
- adjacent total lines;
- Asian-total boundary protection;
- state resets;
- competition utility;
- forward evidence rather than clock decay;
- both Over and Under, with no automatic bias.

The benchmark does **not** mean the model has reverted to v0.2.6 or v0.2.9. Historical samples were tiny. It is a controlled comparison arm.

## 9. Current benchmark philosophy

Recent work suggests the potentially useful historical idea was not a particular old version number, but a narrower market discipline:

- prefer live totals when the match state is synchronized;
- compare adjacent lines rather than selecting a raw Over/Under in isolation;
- use quarter-goal protection when price/value justifies it;
- avoid directional AH exposure when the decisive-event branch for the opponent remains credible;
- do not mistake elapsed scoreless time for an Under signal;
- do not mistake a trailing team for an automatic Over signal;
- evaluate whether actual post-goal behavior supports the expected opening of the game.

## 10. Recent prospective shadow-total sample from the prior chat

These were prospectively identified in the prior chat and should remain in the audit sample. Do not retrospectively remove failures.

1. Adelaide United vs Cong An Ha Noi — Over 1.75 @1.97, 0.125u shadow — FT 0-2 — **HALF WIN**, approximately +0.0606u.
2. Bolivar vs Sao Paulo — Over 2.5 @1.98, 0.125u shadow — FT 1-1 — **FULL LOSS**, -0.125u.
3. Charlotte FC vs Pachuca — Over 2.25 @1.98, 0.125u shadow — FT 0-0 — **FULL LOSS**, -0.125u.
4. Minnesota United vs Atlante — Over 2.5 @1.90, 0.125u shadow — FT 3-1 — **FULL WIN**, +0.1125u.
5. FC Cincinnati vs Atlas — Over 2.25 @2.08, 0.125u shadow — FT 1-2 — **FULL WIN**, +0.135u.
6. Real Salt Lake vs Juarez — Over 2.5 @1.98, 0.125u shadow — score reached 3-0 by 65' — **FULL WIN**, +0.1225u.
7. Tigres UANL vs Vancouver Whitecaps — Over 2.5 @2.05, 0.125u shadow — FT 1-1 — **FULL LOSS**, -0.125u.

Net for these seven settled shadows as calculated in-chat: approximately **+0.0556u**.

This sample is far too small to establish edge. Treat it as calibration only.

## 11. Lessons from recent shadow results

### Adelaide–CAHN

The 1.75 line provided useful settlement protection. One additional goal after entry produced only a half win rather than requiring a full 3-goal match. Do not confuse correct direction with full validation of the process.

### Bolivar–Sao Paulo

Possession/game-state pressure did not produce enough additional goals. A trailing home team, altitude, and apparent transition routes were insufficient by themselves. This reinforces the need for observed post-goal chase quality.

### Charlotte–Pachuca

A strong-looking first-half event profile still finished 0-0. Do not explain away the failure. It is a direct warning against overrating SOT/big-chance snapshots without style persistence and matchup context.

### Minnesota–Atlante

The trailing-team chase plus pre-existing attacking production did convert into a high-scoring second half. Preserve as a positive example, not proof of a universal rule.

### Cincinnati–Atlas

A leader with dominant territorial indicators plus a trailing team with increasing incentive produced enough additional goals. Again, the relevant question is whether the leader remains dangerous and the trailer can create, not merely the score state.

### RSL–Juarez

The Over succeeded strongly, but first-half xG was penalty-inflated. The better reasoning was the total shot/big-chance structure and Juarez's need to open up, not raw xG alone.

### Tigres–Vancouver

This is an especially important miss. At HT Vancouver had substantial first-half xG/box involvement and Tigres led 1-0, but the match ended 1-1. The prior reasoning assumed Vancouver would chase and Tigres would gain transition opportunities. v0.2.43 now requires evidence of each team's actual historical and observed post-goal behavior before making that inference.

## 12. Team-style and post-goal research direction

The user explicitly wants the model to evaluate **how each team normally plays before every match** and **how each team usually behaves after scoring or conceding**.

This is now a strict workflow requirement, not an optional narrative section.

Where data permits, future research should estimate post-goal changes in:

- possession;
- shots/min;
- SOT/min;
- box entries / box shots;
- xG/min as a secondary metric;
- corners/set-piece pressure;
- transition frequency;
- next-goal probability;
- additional-goal rate;
- opponent production.

Condition by score state and, where sample size supports it, by goal timing bands such as 0-30, 31-60, 61-75, 76+.

Small samples must be shrunk toward broader team/league priors rather than treated as deterministic tendencies.

## 13. Match-prep workflow from now on

When the user names a match:

1. Verify competition, venue, kickoff in Vietnam time, format, and relevant qualification/aggregate utility.
2. Verify likely/confirmed lineups and meaningful absences when available.
3. Build the two-team style profile before market analysis.
4. State the expected matchup script and the key ways it could break.
5. Describe each team's historical/typical response after scoring first and after conceding first, with confidence caveats.
6. Only then scan prematch markets.
7. If live, compare actual play with the style expectation before discussing a bet.
8. After a goal, apply the strict post-goal reset before any new shadow verdict.

Do not jump straight from a screenshot to a bet when the style layer has not been established.

## 14. Records and discipline

The user cares explicitly about record keeping and decision discipline.

- `ledger.json` remains authoritative for official accounting when writes are authorized.
- Ledger updates are currently on hold.
- Shadow decisions must be tracked prospectively and not rewritten after results.
- Distinguish a `WATCH`, a `SHADOW LEAN`, and a confirmed official wager.
- Never imply a shadow was placed.
- Never convert a user result report into a model success unless there was a prospective recorded model selection.
- Preserve exact line and odds for settlement.
- Asian-quarter settlement must be graded correctly.

## 15. Current status at transfer

- Active football model: **v0.2.43 AUDIT MODE**.
- Official football betting: **paused**.
- Ledger writes: **on hold**.
- Strict team-style and post-goal behavior layer: **active**.
- Early-totals benchmark: **active, research only**.
- Recent seven-bet benchmark net: approximately **+0.0556u**, not statistically meaningful.
- No LoL state belongs in this handoff; the accidental DK vs KT message was discarded.
- No current football bet should be assumed open solely from this handoff. Reconfirm any live/open state from the user's newest message or authoritative record.

## 16. Bootstrap prompt for a new chat

Use the following when starting the next football chat:

`Continue the Football v1.0 SlipTrace project from repository acchtt/SlipTrace. Load models/football/CURRENT_MODEL.md first and follow its canonical load order. Load the current 2026-08-12 cross-chat handoff. Active mode is Football v0.2.43 AUDIT MODE: official football betting paused, ledger writes on hold, shadow calibration only. Preserve the strict v0.2.43 team-style layer before every serious match preview and the mandatory post-goal behavior reset after every goal. Maintain Arm A current-model analysis and Arm B early-totals benchmark separately. Preserve prospective shadow records exactly and do not retrofit failures. Ignore/discard the accidental League of Legends message from the prior chat. After loading, acknowledge the active version, audit status, style/post-goal requirements, benchmark status, and ledger-write status.`
