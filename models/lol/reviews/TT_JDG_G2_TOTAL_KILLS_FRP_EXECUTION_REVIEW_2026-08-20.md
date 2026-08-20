# TT vs JDG Game 2 — Total Kills FRP Execution Review

**Date:** 2026-08-20 UTC+7  
**Canonical model:** LoL v0.3.58  
**Status:** EXECUTION / CALIBRATION REVIEW — NO MODEL VERSION CHANGE

## Incident

During TT vs JDG Game 2, Total Kills Under 28.5 remained visible and executable through multiple live states, but the live verdict repeatedly defaulted to `HOLD — FRP not passed` without fully resolving the positive FRP evidence already required by canonical v0.3.58.

The map later ended with 18 total kills. The result alone does not justify a correction; the review is based on the information available at each decision point.

## Window review

### 10:05

State:

- JDG 4-1 TT;
- JDG approximately +1.7k gold;
- JDG 1-0 dragons;
- JDG 3 grubs;
- towers 0-0;
- Under 28.5 @1.945.

Retrospective classification: **HOLD remains defensible.**

Only one clear dragon cycle had been completed, while both drafts still retained substantial first-contact and re-engage tools. The evidence for repeated suppression of compulsory contact was not yet strong enough to force `FRP = PASS`.

### 13:09

State:

- JDG 5-2 TT;
- JDG approximately +1.8k gold;
- JDG 2-0 dragons;
- JDG 3 grubs;
- towers 0-0;
- Under 28.5 @1.845.

Canonical retrospective classification: **TAKE — Under 28.5 @1.845 — shadow 0.25u; actual 0u.**

This is a missed qualifying window, not a historical position. The originally visible verdict was HOLD, so no retrospective position may be created.

## Why FRP should have passed at 13:09

Canonical v0.3.58 already says FRP can be supported by repeatable safe concession, demonstrated bounded lethality after real pressure, and Structure Substitution that removes future fights.

By 13:09:

1. **Repeated objective-cycle suppression existed.** A second dragon cycle had completed while total kills moved only from 5 to 7. This was no longer merely passive quiet.
2. **JDG had a non-fight progression route.** Two dragons plus three grubs gave JDG objective/structure leverage that could advance the map without requiring repeated kill-heavy contests.
3. **TT retained safe-concede / cross-map tools.** Camille side pressure plus Viktor/Ezreal range and Bard mobility created credible ways to avoid turning every objective into a full multi-kill fight.
4. **No recurrence burst had broken the regime.** The observed interval between the reviewed snapshots remained bounded rather than accelerating into repeated chase/reset kills.
5. **The next contact cycle was meaningful but not automatically HIGH-pressure.** Maokai/Akali/Olaf gave JDG access, but the presence of engage buttons alone does not establish a kill-heavy future regime when objective control also allows low-risk conversion and the opponent can concede or defend at range.

The execution mistake was treating `FRP = PASS` as if it required a visibly failed fight or another discretionary confirmation event. That is not what the written rule says.

## Duration Under review

Duration Under 31 also cashed, but the 13:09 HOLD remains canonical.

At 13:09 towers were still 0-0. The fastest close route was plausible but did not yet survive the mandatory one-ordinary-disruption FCR stress test with enough robustness.

By 24:05 JDG had 4-2 towers, 3-1 dragons and a large control lead, but the Duration row was no longer executable. Therefore there was no missed executable Duration Under TAKE in the reviewed evidence.

## Root cause

1. FRP was used as a generic conservatism veto instead of being positively adjudicated.
2. Repeated objective-cycle suppression was underweighted.
3. Structure Substitution was recognized for Duration but not correctly reused for TK Under when it **removed future fight requirements**.
4. The existence of engage/re-engage tools was overweighted without asking whether the opponent actually had to contest each future window.

## Corrective action

No new model version is warranted. The written v0.3.58 FRP rule already contains the needed concepts.

Add the execution-calibration procedure:

`models/lol/procedures/LOL_FRP_POSITIVE_EVIDENCE_EXECUTION_CALIBRATION_2026-08-20.md`

Core instruction:

- FRP is not a default HOLD gate;
- repeated bounded kill recurrence across real objective/contact cycles is positive evidence;
- Structure Substitution may support an Under only when it removes future fights rather than merely replacing past fights;
- engage composition alone does not make next-cycle pressure HIGH;
- once two-snapshot eligibility is satisfied and FRP positively passes, do not invent a third confirmation requirement.

## Audit treatment

Do **not** create a retrospective shadow position for the missed 13:09 TAKE. Historical ledger integrity preserves the verdict actually issued.

This review is a calibration artifact for future decisions only.
