# LoL Live Execution Calibration — 2026-08-15

## Purpose

This procedure corrects cross-chat execution drift: the same analytical model must not become more conservative merely because safeguards are summarized more prominently after handoff.

This is an **execution-calibration procedure only**. It does not independently change the active analytical model, pricing thresholds, stake policy, hard vetoes, or market eligibility. The currently active analytical rules are defined by `models/lol/CURRENT_MODEL.md` and its rule stack.

## Core principle

**Be conservative about invalid evidence, not conservative about qualified bets.**

The written gates are the safety margin. Do not add an unwritten second safety margin after they pass.

## Mandatory TAKE discipline

When a market is visibly executable and:

1. the market is live-eligible under the active rules;
2. all mandatory evidence/gates for that market are satisfied;
3. no active hard veto, stale-line block, no-duplicate block, or active v0.3.60 re-certification block applies;
4. the exact executable odds clear the active minimum and retained pricing/edge requirement;

then the verdict should be **TAKE**.

Do not convert a qualified TAKE into HOLD/PASS merely because:

- another snapshot would feel more comfortable;
- Baron/inhibitor/first tower has not occurred unless an active rule explicitly requires it;
- the favorite has not yet produced a visually dominant state;
- the underdog still has a generic comeback path already priced by the framework;
- the model has ordinary probabilistic uncertainty after required uncertainty tests pass;
- the previous map lost;
- the user switched chats.

## No extra confirmation rule

Do **not** require a third synchronized snapshot for ML/KH/TK once the retained two-snapshot gate and all market-specific gates are satisfied, unless a separate active rule explicitly requires mechanism-relevant evidence.

v0.3.60's FRP / FCR / CFC / SMR gates are **not** discretionary requests for more comfort. They are named analytical requirements. If one fails, PASS/HOLD. If one passes, do not then invent another confirmation layer.

Do not invent generic confirmation such as “one more objective,” “one more fight,” “one more tower,” or “wait for Baron” when the written framework has already qualified the position.

## HOLD/PASS accountability

A HOLD or PASS after live eligibility must identify a **specific named reason** from the active framework, such as:

- two-snapshot gate not satisfied;
- fallback certification incomplete;
- hard draft-collapse veto active;
- FFD insufficient;
- RNE unsupported;
- Structure Substitution negates margin expansion;
- Total Kills FRP / recurrence/contact gate not satisfied;
- next compulsory-contact cycle too dangerous for a TK Under;
- Duration FAILED-CONVERSION requirement absent;
- LCH too high for an Over;
- Duration FCR not ROBUST for an Under;
- live ML RL/SL/OSC/CFC decomposition fails the control-lead test;
- Same-Mechanism Re-certification fails;
- pricing/odds below threshold;
- line stale/non-executable;
- market family already used under the no-duplicate policy;
- correlation prevents the additional cross-family position.

Avoid generic reasons such as “not enough confidence,” “would like more confirmation,” or “safer to wait” when no written gate is failing.

## Position-blind reassessment

Position-blind reassessment must be allowed to move the live probability materially.

Do not preserve a pregame/draft lean merely because it was the initial view. Live evidence can reverse the preferred side when active rules allow it.

Exception: draft-locked hard vetoes/classifications and other rules explicitly made non-upgradable remain binding unless the underlying input itself was wrong.

## v0.3.60 execution interpretation

### Total Kills Under — FRP

Do not promote passive quiet into future quiet.

A low kill count or quiet interval may support CRR suppression, but an Under TAKE also requires `FRP = PASS` under the next compulsory-contact schedule.

If a recurrence burst has already broken the prior regime, a later quiet patch does not restore FRP by itself. Restoration requires mechanism-relevant evidence as defined by v0.3.60.

### Duration Under — FCR

Do not convert a plausible fastest close route into a TAKE unless `FCR = ROBUST` or the retained terminal exception independently applies.

The one-disruption stress test is mandatory. If the Under requires every conversion step to succeed cleanly, PASS/HOLD.

### Live ML — control lead

Do not treat resource lead as control lead.

When ML depends on a live advantage, explicitly decompose RL / SL / OSC / CFC and run the neutral-setup compulsory-fight stress test.

A candidate can be richer and still fail the ML control gate if the opponent has materially easier first contact/re-engage and there is no independent control evidence.

### Same-Mechanism Re-certification

A previous loss is never an automatic veto.

But if the previous map's failure has been mechanistically diagnosed and the next same-series TAKE relies on the same structural assumption, SMR must explicitly pass. Repeating a similar scoreboard state is not re-certification.

Once SMR passes, do not add another discretionary penalty merely because the previous map lost.

## Underdog +kills certification lock — mandatory fail-closed procedure

This remains a hard execution requirement for every underdog +kills evaluation under v0.3.57+ and exists specifically to prevent a repeat of the SK +7.5 vs FNC Game 1 execution error on 2026-08-15.

The v0.3.57 fallback certification is **draft-locked**. Position-blind live reassessment may change pricing, RIT, signed-margin outlook, NKB/RFI/KCV, and Structure Substitution, but it may **not** upgrade an underdog's fallback certification.

Before any underdog +kills TAKE can be considered, explicitly carry forward the draft-time certification state through this exact gate:

1. `FER` — positively certified PASS at draft classification;
2. `PDC` — positively certified PASS at draft classification;
3. `PST` — positively certified PASS at draft classification;
4. `ARI` — positively certified PASS at draft classification;
5. `False-Stable Guard` — INACTIVE;
6. `FF` — positively certified `STABLE`;
7. v0.3.56 hard Draft-Collapse Veto — inactive;
8. only then may live RIT and signed-margin/pricing analysis proceed.

If any of FER/PDC/PST/ARI was failed, unresolved, unavailable, or never explicitly certified; if False-Stable Guard was active/unresolved; or if FF was `FRAGILE`, `ABSENT`, or `UNCERTIFIED`, then underdog +kills is **TAKE-INELIGIBLE FOR THE ENTIRE MAP** unless the underlying draft input itself is corrected.

Ordinary live evidence can never reopen this gate. Prohibited upgrade evidence includes:

- kill parity or return kills;
- temporary gold/role-gold improvement;
- objective parity or an objective win;
- larger live handicap cushion;
- successful live engages/disengages/resets;
- two synchronized snapshots becoming available;
- range, poke, scaling, waveclear, multiple engage/CC buttons or generic peel;
- improved live price.

These facts may affect pricing only if draft-time FF was already STABLE.

### Mandatory pre-TAKE self-check for underdog +kills

Immediately before issuing an underdog +kills TAKE, all answers must be explicit YES:

- `FER = PASS?`
- `PDC = PASS?`
- `PST = PASS?`
- `ARI = PASS?`
- `False-Stable Guard = INACTIVE?`
- `FF = STABLE?`
- `Hard Draft-Collapse Veto = INACTIVE?`

If any answer is not YES, verdict is PASS/HOLD and the failed gate must be named.

A two-snapshot gate becoming satisfied is not permission to revisit fallback certification. “Now certifies STABLE” or equivalent reasoning is prohibited absent genuine draft-input correction.

### SK +7.5 vs FNC Game 1 reference error

At 7:34, SK +7.5 @2.041 was incorrectly taken after live evidence was used to say SK “now certifies STABLE.” That was procedurally invalid. Correct verdict was `PASS — SK +7.5 @2.041 — 0u.`

The lesson is exact rule obedience, not generic conservatism.

## Positive-evidence symmetry

Safeguards must not create an automatic anti-favorite, anti-underdog, anti-Over, anti-Under or anti-ML bias.

Examples:

- Blocking underdog +kills does not create favorite -kills, but once favorite -kills independently passes FFD/RNE and pricing, TAKE it.
- HIGH LCH can block an Over without creating an Under; if an Under independently passes acceleration + FCR, TAKE it.
- FRP can block a TK Under without creating a TK Over; the Over still needs its own gates.
- A control-lead failure can block one ML side without automatically qualifying the opponent.
- SMR can block a repeated same-mechanism thesis without making the opposite side a TAKE.

## Cross-chat handoff rule

When loading the project in a new chat, preserve the same decision posture as the originating chat:

**same rules + same thresholds + same qualifying evidence = same verdict tendency.**

A new chat must not default toward HOLD/PASS because compressed context emphasizes safeguards.

## Mandatory compact-output companion rule

`models/lol/procedures/LOL_COMPACT_OUTPUT_FULL_ANALYSIS_RULE_2026-08-15.md` is mandatory whenever this file is loaded.

Brief visible output never permits brief or partial analysis. Full applicable model/rules/procedure stack must be completed before every verdict.

## Live output

The verdict-first requirement remains unchanged. First visible line must be TAKE / PASS / HOLD before connector or logging work.

This procedure governs execution posture only and does not independently authorize a model-version increment.