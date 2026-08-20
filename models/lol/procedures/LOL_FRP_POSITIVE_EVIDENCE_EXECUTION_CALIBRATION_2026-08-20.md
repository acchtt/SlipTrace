# LoL Total Kills Under — FRP Positive-Evidence Execution Calibration

**Effective:** 2026-08-20 UTC+7  
**Canonical model:** LoL v0.3.58  
**Type:** execution calibration only; no new analytical model version

## Purpose

Prevent FRP — Forward Regime Persistence — from becoming a generic HOLD bias.

Canonical v0.3.58 still requires `FRP = PASS` before any Total Kills Under TAKE. This procedure clarifies how to positively recognize PASS using the evidence already authorized by the model.

## Mandatory principle

**FRP is a mechanism test, not a request for one more confirmation event.**

Once the two-snapshot gate is satisfied, the analyst must positively adjudicate the next compulsory-contact regime. Do not default to `UNCERTAIN` merely because future fights remain possible.

## Positive FRP evidence

The following can materially support `FRP = PASS` when jointly coherent:

1. **Repeated bounded recurrence across real objective/contact cycles** — multiple dragons, Herald/grub windows, tower-defense windows or other meaningful contact schedules occur without a kill-recurrence burst.
2. **Safe-concede / cross-map routes** — the trailing side can give an objective, trade sides, waveclear, range-defend or otherwise avoid converting every scheduled window into a full fight.
3. **Structure Substitution that removes future fights** — the controlling side can advance through objectives/structures so that fewer future contests are required. This supports TK Under only when it reduces future fight count; merely replacing past fights is insufficient.
4. **Demonstrated bounded lethality after actual contact** — real contact occurs but does not chain into chase, reset kills, objective-turn kills or serial base-defense kills.
5. **Low re-engage necessity** — even if first contact is available, the state does not compel repeated re-entry after the first exchange.

Passive quiet by itself remains insufficient.

## Objective-cycle rule

A completed objective cycle can count as **suppressed compulsory contact** even if no dramatic teamfight occurred.

The question is not whether a fight visibly failed. The question is whether a real contest window existed and the map progressed with bounded kill production because of concession, zoning, cross-map play, range defense, or low-risk objective control.

After **two distinct meaningful objective/contact cycles** with bounded recurrence, the analyst must explicitly test whether that repeated pattern is likely to persist. Do not automatically demand a third cycle.

This is not a numeric auto-TAKE rule; it is an anti-default-HOLD calibration.

## Engage-button guard

Do not classify next-cycle contact pressure `HIGH` solely because one or both drafts contain engage champions.

Also test:

- whether the trailing side actually must contest;
- whether the leading side can secure the objective without deep chase;
- whether ranged defense / disengage / cross-map exists;
- whether re-engage is incentivized after the first exchange;
- whether objective/structure progress can end the contact without additional kills.

Engage availability is an input, not the conclusion.

## FRP output discipline

For every executable TK Under after the two-snapshot gate, state internally:

- next compulsory contact cycle;
- contact pressure LOW / MEDIUM / HIGH;
- observed evidence type: PASSIVE QUIET or SUPPRESSED COMPULSORY CONTACT;
- safe-concede/cross-map route;
- Structure Substitution effect on **future fight count**;
- recurrence-burst status;
- `FRP = PASS / FAIL / UNCERTAIN`.

If `FRP = PASS` and all retained Total Kills gates and pricing requirements also pass, default to TAKE. Do not add a discretionary third-snapshot, extra-objective, or extra-fight requirement.

## Reference calibration — TT vs JDG G2, 2026-08-20

At 10:05, HOLD on Under 28.5 remained defensible because repeated compulsory-contact suppression had not yet been sufficiently established.

At 13:09, JDG led 5-2 with approximately +1.8k gold, two dragons and three grubs, towers 0-0, and Under 28.5 was 1.845. A second dragon cycle had completed with only bounded kill recurrence, JDG possessed non-fight progression routes, and TT retained credible safe-concede/cross-map/ranged-defense routes.

Retrospective canonical verdict at 13:09:

**TAKE — Under 28.5 @1.845 — shadow 0.25u; actual 0u.**

No retrospective position is created because the visible historical verdict was HOLD.

Reference review:
`models/lol/reviews/TT_JDG_G2_TOTAL_KILLS_FRP_EXECUTION_REVIEW_2026-08-20.md`
