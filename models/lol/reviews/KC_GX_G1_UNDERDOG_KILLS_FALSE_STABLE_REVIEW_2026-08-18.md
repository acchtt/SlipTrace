# KC vs GIANTX Game 1 — Underdog +Kills False-Stable Review

**Date:** 2026-08-18 UTC+7  
**Model:** LoL v0.3.58 canonical  
**Status:** Retained in-place amendment review; no version bump

## Decision reviewed

Post-draft market:

- KC blue: Rumble / Jarvan IV / Orianna / Caitlyn / Bard
- GX red: Ornn / Xin Zhao / Annie / Ezreal / Karma
- KC ML 1.287
- GX +9.5 kills @1.780

Historical visible verdict:

**TAKE — GX +9.5 kills @1.780 — shadow 0.25u.**

Final:

- KC won
- kills 16-5 KC
- final signed kill margin: KC +11
- GX +9.5 lost

## Primary execution breach — the TAKE was not eligible post-draft

Canonical v0.3.58 governance already states:

- pregame/immediate post-draft ML/KH/TK TAKEs are disabled;
- live ML/KH/TK require the two-snapshot eligibility gate.

Therefore the historical visible post-draft `TAKE` was procedurally invalid **before** any discussion of whether the GX fallback was analytically good or bad.

Correct immediate post-draft action under the written procedure was:

**HOLD/PASS — no position — wait for two clean synchronized live snapshots.**

This review must not let analytical debate hide the execution error. Future compact output must preserve full procedure: a strong draft opinion may identify a preferred live target, but it cannot bypass the two-snapshot gate.

## Analytical error — false-STABLE fallback

Separately from the execution breach, the underdog fallback was incorrectly certified from the existence of theoretical survival and return-kill tools.

The analysis emphasized:

- Ornn frontline/scaling;
- Xin Zhao counter-engage;
- Annie pick threat;
- Ezreal safety/waveclear;
- Karma disengage/utility.

Those features can help GX **produce some kills while losing**, but they did not establish that GX could **suppress KC's net kill-margin expansion**.

That distinction was the core analytical miss.

## Draft interaction that should have blocked STABLE

KC had multiple independent, repeatable routes that attacked the same GX failure cluster:

1. **Range and zone control:** Rumble Equalizer, Caitlyn range/traps and Orianna ball control made GX entry paths expensive.
2. **Layered first contact:** Jarvan, Bard and Orianna could start or extend fights from several angles.
3. **Siege conversion:** Caitlyn allowed KC to turn control into structures without requiring reckless dives.
4. **Repeatable continuation:** after first contact, KC retained damage and chase/zone tools rather than spending every resource on initiation.
5. **GX kill access was conditional:** Annie required access, Xin had to enter controlled melee space, and Ezreal was safer than he was decisive against KC's frontline/zone shell.
6. **Team-strength prior mattered:** KC were the stronger execution baseline. Team strength alone is never a veto, but when the stronger favorite also owns the cleaner repeatable control/siege routes, theoretical underdog fallback requires stronger proof.

The correct post-draft classification should therefore have been:

- underdog kill-production ability: PRESENT but CONDITIONAL;
- favorite kill-margin suppression by underdog: UNRESOLVED/INSUFFICIENT;
- False-Stable Guard: ACTIVE;
- fallback floor: FRAGILE / UNCERTIFIED, not STABLE;
- GX +9.5: not a valid post-draft TAKE and not a preferred future +kills target absent genuine draft-input correction.

This review does **not** imply KC -9.5 should have been an automatic TAKE. Favorite -kills still requires its own live FFD/RNE gates.

## Live diagnostic miss

Later, at displayed 17:12 with the map-specific clock bug of -4:00, the corrected time was 13:12:

- KC 3-0 kills;
- KC approximately +3.2k gold;
- towers 0-0;
- GX 2-0 dragons.

The live reassessment over-weighted 0-0 towers and GX's two dragons as resistance.

Under canonical v0.3.58 Duration rules, 0-0 towers are neutral. The same neutrality principle must also prevent zero towers from being used as an implicit **anti-control** signal in kill-margin analysis.

At corrected 13:12, the combination of stronger-team prior, clean kill lead, material economy lead, lane/role pressure and a draft with superior range/zone/siege should have been treated as a **pre-structure control signal**. Towers can lag the control state.

This is not a rule that +3k gold automatically means favorite domination. It is a requirement to evaluate whether the favorite already possesses repeatable control and conversion routes before structures appear.

## Canonical correction

For underdog +kills fallback certification, explicitly separate:

### A. Kill Production

Can the underdog still generate kills from behind?

### B. Kill-Margin Suppression

Can the underdog plausibly prevent the favorite from repeatedly converting advantages into **net kill-margin expansion**?

`STABLE` requires both.

A composition may have engage, scaling, waveclear or return-kill tools and still fail Kill-Margin Suppression.

When the favorite has multiple repeatable range/pick/zone/siege/continuation routes and the underdog's kill routes depend on entering the same controlled space, the False-Stable Guard must be ACTIVE unless there is an independent demonstrated reset/survival route.

Team-strength prior is a modifier, not a standalone veto. A stronger favorite plus superior repeatable control routes raises the burden of proof for underdog STABLE; it does not automatically authorize favorite -kills.

## Anti-overfit guard

Do not reverse the old error by treating every strong favorite as an automatic underdog +kills veto.

The veto is mechanism-based:

- repeatable favorite access/control;
- underdog shared failure cluster;
- insufficient independent survival/reset;
- conditional rather than reliable underdog kill production;
- inability to suppress net margin expansion.

If the underdog genuinely passes FER/PDC/PST/ARI and also demonstrates independent margin-suppression routes, STABLE remains available and qualified bets should still be taken.

## Correct retrospective verdict

**HOLD/PASS post-draft — GX +9.5 kills @1.780 — 0u.**

The model should have waited for the mandatory two synchronized live snapshots. Independently, the draft fallback should have been classified FRAGILE/UNCERTIFIED, so the GX +kills thesis should not have become a preferred live target absent a genuine draft-input correction.

No change to historical P/L. The original position remains a recorded loss under v0.3.58; this review changes future execution/certification, not history.
