# LoL Live Execution Calibration — 2026-08-15

## Purpose

This procedure corrects a cross-chat execution drift observed by the user: after handoff, the same analytical model became more conservative because safeguards were being treated as reasons to wait beyond the written qualification threshold.

This is an **execution-calibration procedure only**. It does **not** change LoL v0.3.59 analytical rules, pricing thresholds, stake policy, hard vetoes, or market eligibility.

## Core principle

**Be conservative about invalid evidence, not conservative about qualified bets.**

The written gates are the safety margin. Do not add an unwritten second safety margin after they pass.

## Mandatory TAKE discipline

When a market is visibly executable and:

1. the market is live-eligible under the active rules;
2. all mandatory evidence/gates for that market are satisfied;
3. no active hard veto or stale-line block applies;
4. the exact executable odds clear the active minimum and any retained pricing/edge requirement;

then the verdict should be **TAKE**.

Do not convert a qualified TAKE into HOLD/PASS merely because:

- another snapshot would feel more comfortable;
- Baron/inhibitor/first tower has not occurred unless an active rule explicitly requires it;
- the favorite has not yet produced a visually dominant state;
- the underdog still has some generic comeback path that is already accounted for by the active framework;
- the model is uncertain in the ordinary probabilistic sense after the required uncertainty tests have passed;
- the previous map lost;
- the user switched chats.

## No extra confirmation rule

Do **not** require a third synchronized snapshot for ML/KH/TK once the retained two-snapshot gate and all market-specific gates are satisfied, unless a separate active rule explicitly requires additional evidence.

Do not invent extra confirmation such as “one more objective,” “one more fight,” “one more tower,” or “wait for Baron” when the written framework has already qualified the position.

## HOLD/PASS accountability

A HOLD or PASS after live eligibility should identify a **specific named reason** from the active framework, such as:

- two-snapshot gate not yet satisfied;
- fallback certification incomplete;
- hard draft-collapse veto active;
- FFD insufficient;
- RNE unsupported;
- Structure Substitution negates margin expansion;
- Total Kills recurrence/contact gate not satisfied;
- Duration FAILED-CONVERSION requirement absent;
- LCH too high for an Over;
- acceleration/persistence gate absent for an Under;
- pricing/odds below threshold;
- line stale/non-executable;
- correlation prevents add-on.

Avoid generic reasons such as “not enough confidence,” “would like more confirmation,” or “safer to wait” when no written gate is actually failing.

## Position-blind reassessment

Position-blind reassessment must be allowed to move the live probability materially.

Do not preserve a pregame or draft lean merely because it was the initial view. Live evidence can reverse the preferred side when the active rules allow it.

Exception: draft-locked hard vetoes and classifications that the active rules explicitly make non-upgradable remain binding unless the underlying draft input itself was wrong.

## Positive-evidence symmetry

Safeguards must not create an automatic anti-favorite, anti-underdog, anti-Over, or anti-Under bias.

Examples:

- Blocking underdog +kills does not automatically create favorite -kills, but once favorite -kills independently passes FFD/RNE and pricing, TAKE it without additional discretionary delay.
- A high LCH blocks an Over when required, but does not create an Under unless the Under acceleration gates pass; conversely, when a Duration market independently passes all active gates, do not keep waiting because Duration has historically been difficult.
- A large cushion does not itself qualify underdog +kills, but when fallback certification and signed-margin pricing both pass, do not demand extra resilience evidence beyond the written rules.

## Cross-chat handoff rule

When loading the project in a new chat, preserve the same decision posture as the originating chat:

**same rules + same thresholds + same qualifying evidence = same verdict tendency.**

A new chat must not default toward HOLD/PASS simply because compressed context emphasizes safeguards.

## Live output

The existing verdict-first requirement remains unchanged. First visible line must be TAKE / PASS / HOLD before any connector or logging work.

This procedure governs execution posture only and does not authorize any model-version increment.