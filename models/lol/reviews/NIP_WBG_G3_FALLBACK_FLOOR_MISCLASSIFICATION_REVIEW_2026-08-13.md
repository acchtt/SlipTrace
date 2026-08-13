# NIP vs WBG Game 3 — False-Stable Fallback Review

**Date:** 2026-08-13 UTC+7
**Model at error:** LoL v0.3.56

## Error

At 20:12 the model took WBG +8.5 kills @1.951 after classifying WBG Gnar / Lee Sin / Annie / Mel / Rell as low-collapse with a STABLE fallback.

That classification was wrong. It confused **forcing redundancy** with **survival/fallback redundancy**.

NIP draft: Tristana / Xin Zhao / Twisted Fate / Ashe / Seraphine.

At entry NIP led 4-3 kills, +2.7k gold, 2-1 towers, dragons 1-1.

## Correct classification

WBG had several ways to initiate, but those routes largely shared the same forward-commit failure cluster. Multiple engage/CC options did not prove that WBG could reset after failed contact, preserve a protected damage source, defend pressured space, and re-contest without repeating the same all-in dependency.

Correct underdog +kills classification:

- FRI: meaningful;
- SRI: insufficient;
- DCR: HIGH for handicap eligibility;
- FF: FRAGILE;
- False-Stable Guard: ACTIVE;
- v0.3.56 hard underdog +kills veto: ACTIVE.

Correct verdict at 20:12:

`PASS — WBG +8.5 kills @1.951 — 0u.`

## Root cause

v0.3.56 made HIGH-DCR/weak-FF vetoes strict but did not make `STABLE` difficult enough to award. The model could still credit:

- another engage button as fallback;
- peel carried by the same resources required to initiate;
- generic waveclear/range without testing whether it functions while behind;
- live parity as implicit resilience support.

## Correction

LoL v0.3.57 makes STABLE a positive certification requiring four matchup-relative PASS tests: Failed-Engage Reset, Protected-DPS Continuation, Pressured Space, and Alternative Route Independence. It also separates Forcing Route Independence from Survival Route Independence and fails closed whenever certification is incomplete.

Rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.57.md`

Procedure: `models/lol/procedures/LOL_FALLBACK_FLOOR_CERTIFICATION_2026-08-13.md`
