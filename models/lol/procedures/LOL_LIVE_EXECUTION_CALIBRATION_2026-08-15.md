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

## Underdog +kills certification lock — mandatory fail-closed procedure

This section is a **hard execution requirement** for every underdog +kills evaluation under v0.3.57+ and exists specifically to prevent a repeat of the SK +7.5 vs FNC Game 1 execution error on 2026-08-15.

The v0.3.57 fallback certification is **draft-locked**. Position-blind live reassessment may change pricing, RIT, signed-margin outlook, NKB/RFI/KCV, and Structure Substitution, but it may **not** upgrade an underdog's fallback certification.

Before any underdog +kills TAKE can be considered, explicitly carry forward the draft-time certification state through this exact gate:

1. `FER` — must already be positively certified PASS at draft classification;
2. `PDC` — must already be positively certified PASS at draft classification;
3. `PST` — must already be positively certified PASS at draft classification;
4. `ARI` — must already be positively certified PASS at draft classification;
5. `False-Stable Guard` — must already be INACTIVE;
6. `FF` — must already be positively certified `STABLE`;
7. v0.3.56 hard Draft-Collapse Veto — must be inactive;
8. only then may live RIT and signed-margin/pricing analysis proceed.

If any of FER/PDC/PST/ARI was failed, unresolved, unavailable, or never explicitly certified; if the False-Stable Guard was active or unresolved; or if FF was `FRAGILE`, `ABSENT`, or `UNCERTIFIED`, then the underdog +kills market is **TAKE-INELIGIBLE FOR THE ENTIRE MAP** unless the underlying draft input itself is corrected.

**Ordinary live evidence can never reopen this gate.** The following must never be used to create or justify a live upgrade to `STABLE`:

- kill parity or return kills;
- a temporary gold lead or role-gold improvement;
- objective parity or an objective win;
- a larger live handicap cushion;
- successful live engages, disengages, or isolated resets;
- two synchronized snapshots becoming available;
- visible range, poke, scaling, waveclear, multiple engage buttons, multiple CC champions, or generic peel;
- a live observation that a champion can sometimes engage or peel;
- improved price/value on the +kills line.

These live facts may affect pricing **only if draft-time FF was already STABLE**. They are never certification evidence.

### Mandatory pre-TAKE self-check for underdog +kills

Immediately before issuing an underdog +kills TAKE, the execution process must be able to answer all of the following from the draft-locked state:

- `FER = PASS?`
- `PDC = PASS?`
- `PST = PASS?`
- `ARI = PASS?`
- `False-Stable Guard = INACTIVE?`
- `FF = STABLE?`
- `Hard Draft-Collapse Veto = INACTIVE?`

If any answer is not an explicit **YES**, verdict must be **PASS/HOLD**, with the failed named gate stated. Do not proceed to cushion, RNE, or price as though eligibility existed.

A two-snapshot gate becoming satisfied is **not** permission to revisit fallback certification. “Now certifies STABLE,” “live evidence proves STABLE,” or equivalent reasoning is prohibited unless a genuine draft-input correction has occurred.

### SK +7.5 vs FNC Game 1 reference error

At 7:34, SK +7.5 @2.041 was incorrectly taken after live evidence was used to say SK “now certifies STABLE.” That was procedurally invalid. SK's range/forcing inventory and the availability of Lee Sin/Rell plus Jayce/Corki/Syndra were not sufficient to establish survival redundancy; FER/PDC and the False-Stable Guard were not positively cleared at draft time. Correct verdict was `PASS — SK +7.5 @2.041 — 0u.`

This reference is an **execution-error example, not a model change**. The lesson is to obey the existing v0.3.57 fail-closed certification exactly, not to become generally more conservative.

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