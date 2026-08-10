# MODEL RULES — LEAGUE OF LEGENDS v0.3.51

**Status:** Active delta  
**Effective date:** 2026-08-10 20:37 UTC+7  
**Supersedes:** v0.3.50 only where stated

## Purpose

Correct the early-live Total Kills Under error from HLE Challengers vs Gen.G Global Academy Game 2.

Confirmed position under v0.3.50:

- Under 33.5 total kills @1.690 — LOSS (-0.25u)

Entry at 7:47: GGA 2-1 HLE.C, GGA +1.0k gold, 0-0 towers, HLE.C 1-0 dragons.  
Final: GGA won 20-15 at 30:30, 35 total kills.

Review: `models/lol/reviews/HLE_GGA_G2_UNDER_SKIRMISH_RECURRENCE_REVIEW_2026-08-10.md`.

The central correction is:

> **De-duplicating objective windows must not erase repeatable between-objective skirmish creation. A quiet early score cannot qualify an Under when both drafts retain persistent, independent ways to start contact.**

v0.3.50 OKP / FCI / CRR / CL, v0.3.49 quiet-start rules, v0.3.48 Kill Handicap conversion controls, v0.3.47 Draft Primacy, v0.3.45 Duration, v0.3.44 signed-margin symmetry and all retained execution controls remain active unless superseded below.

---

## 1. Early-Live Under Confirmation Is a Hard Gate

Before **12:00**, a Total Kills Under may not be TAKEN primarily from a low current kill count or a large remaining line cushion.

A pre-12:00 Under TAKE requires at least one of:

1. **two synchronized live snapshots >=90 seconds apart** showing low OKP **and** stable/declining realized-contact pressure;
2. meaningful contact has already occurred repeatedly and is resolving with demonstrably LOW CL because disengage/peel/resetting is functioning;
3. a near-terminal structure-only branch is already observed and is removing future contact windows faster than it creates them.

A draft-only claim that future fights will be conceded does not satisfy this gate.

If only one live snapshot exists and the draft retains repeatable hard-access mechanisms, verdict defaults **HOLD/PASS** regardless of how attractive the early Under line appears.

This hardens the retained v0.3.49 quiet-start non-persistence rule.

---

## 2. Skirmish Recurrence Reserve (SRR)

Total Kills projections must now include a separate **Skirmish Recurrence Reserve (SRR)** in addition to de-duplicated objective/event FCI.

SRR represents repeated contact opportunities that can occur **between** formal objective windows, including:

- river/jungle vision contests;
- lane-transition catches;
- side-lane collapses;
- support/jungle roam collisions;
- post-reset re-engages;
- repeated neutral picks after cooldown reset;
- flank attempts that do not require a major objective to be active.

SRR does **not** mean counting engage champions as independent fights.

Instead classify the matchup's recurrence capacity:

- `LOW SRR` — contact mostly tied to major objectives; weak repeat forcing between them;
- `MEDIUM SRR` — some repeatable pick/skirmish creation;
- `HIGH SRR` — multiple independent, matchup-functional contact triggers can create repeated fights between major objectives.

For every early-live Total Kills decision, SRR is mandatory.

---

## 3. Bidirectional Forcing

Flag **Bidirectional Forcing (BF)** when both teams have at least one independent, reliable way to initiate meaningful contact without waiting for the opponent to voluntarily enter an objective choke.

Typical structures include:

- hard-engage jungle + hard-engage support on one side versus dive/pick jungle + hard CC mid/support on the other;
- flank/point-click initiation on both teams;
- reliable catch plus immediate damage continuation on both teams;
- mutual engage where neither composition has dependable disengage after first contact.

When BF is active:

- raise SRR by one class unless strong live evidence suppresses it;
- do not globally discount CRR because one side has poke/zone control;
- raise the high-total branch probability;
- treat traded-fight / high-T low-M outcomes as materially live.

BF is especially Under-negative when both teams can re-engage after a first spell cycle or quickly reset cooldowns for another pick.

---

## 4. Threat Deterrence Requires a Hard-Access Override Test

v0.3.50 Threat Deterrence remains active, but before using TD to lower CRR ask:

**Can the opponent bypass the zone and start contact from flank, fog, displacement, dash, point-click engage or transition timing?**

If yes, TD may be only `LOCAL` rather than `GLOBAL`.

Classify TD:

- `GLOBAL TD` — most meaningful contact routes are genuinely denied; CRR may be reduced broadly;
- `LOCAL TD` — direct choke entry is deterred, but alternate hard-access routes remain functional;
- `NO TD` — zoning does not materially suppress contact.

Only GLOBAL TD can support a broad Under CRR discount.

---

## 5. Under Cushion Stress Test

For every Under, calculate:

- current kills;
- maximum additional kills that still win;
- additional kills required to lose;
- remaining estimated map time range;
- high-contact branch kill production.

Do not treat a large cushion as self-validating.

Explicitly test whether the Under can lose through a plausible sequence such as:

- several 2-4 kill skirmishes;
- one or two larger objective fights;
- terminal base-defense/cleanup kills.

If the required additional kills can be reached by a plausible HIGH-SRR / medium-high CL branch, widen uncertainty materially.

For early-live Under, a large cushion cannot substitute for the confirmation gate in Section 1.

---

## 6. SRR-Adjusted Projection

Total Kills projection becomes conceptually:

`Final Total Kills = Current Kills + CRR-weighted objective/event FCI kills + SRR kills + residual terminal/pick/chase kills`.

Avoid false precision. Use low / central / high branches.

For SRR, estimate:

- recurrence class LOW/MEDIUM/HIGH;
- which side can initiate;
- cooldown/reset repeatability;
- disengage quality after first contact;
- expected kills per realized skirmish;
- whether live evidence is suppressing or confirming recurrence.

---

## 7. Early Under Recurrent-Contact Surcharge

For pregame or early-live Under, add **+2pp** to the normal Total Kills lower-bound requirement when all are true:

- SRR is HIGH;
- BF is active;
- functional disengage is not clearly strong on both sides.

The total required cushion remains capped at **+9pp over break-even** across all applicable Total Kills surcharges.

If Section 1 hard gate fails, this surcharge cannot rescue the bet; verdict remains HOLD/PASS.

---

## 8. Same-Map T/M Joint Matrix — High-T / Low-M Emphasis

When a +kills handicap and an Under are considered on the same map, explicitly price the branch:

- **high T / low-to-moderate M** — repeated traded skirmishes or underdog outright win with return kills.

If BF or HIGH SRR is active, this branch must receive material probability unless there is direct live evidence of low CL or one-sided return-kill suppression.

Do not infer that a strong underdog +kills position supports an Under. In some matchups the same margin-survival mechanism increases Total Kills because both teams keep trading.

HLE.C vs GGA G2 final was exactly this branch:

- GGA +7.5 won;
- Under 33.5 lost;
- final GGA 20-15, 35 total kills.

---

## 9. HLE.C vs GGA G2 Calibration

Draft:

GGA Jayce / Skarner / Syndra / Varus / Leona  
HLE.C Yorick / Lee Sin / Annie / Jhin / Alistar

At 7:47:

- 3 total kills;
- GGA +1.0k gold;
- no towers;
- HLE.C 1-0 dragons.

Old v0.3.50 read:

- low OKP;
- large Under cushion;
- GGA poke/choke could create concession;
- projected ~25-29 final kills;
- Under 33.5 @1.690 TAKEN.

Correct v0.3.51 read:

- early confirmation gate: **FAILED** — one live snapshot only;
- objective FCI: medium;
- SRR: **HIGH**;
- BF: **ACTIVE**;
- TD: LOCAL only, because HLE.C could bypass direct choke entry with Lee/Annie/Alistar access;
- CL: medium/high;
- high-T / low-M branch: material;
- Under 33.5 @1.690: **HOLD/PASS**.

---

## 10. Mandatory Total Kills Internals — v0.3.51

Before every Total Kills TAKE, lock:

1. current kills / exact line / line-cross arithmetic;
2. OKP;
3. de-duplicated objective/event FCI;
4. CRR for each material FCI window;
5. Contest / Concede / Trade / Delay tree;
6. Contest Compulsion status;
7. Threat Deterrence class GLOBAL / LOCAL / NONE;
8. **SRR LOW / MEDIUM / HIGH**;
9. **Bidirectional Forcing ACTIVE / INACTIVE**;
10. CL conditional on contact;
11. winner kill-production mechanism;
12. loser return-kill floor;
13. Under cushion stress test or Over line-cross stress test;
14. low / central / high final-kill branches;
15. break-even and lower-bound probability after all surcharges;
16. for pre-12:00 Under, Section 1 confirmation gate status.

Missing SRR/BF on a material early Total Kills decision => widen uncertainty and PASS/HOLD.

---

## 11. Review Window

For the next **10 settled v0.3.51+ Total Kills positions**, record:

- entry clock;
- line and odds;
- number of synchronized live snapshots available at entry;
- OKP;
- FCI;
- CRR;
- SRR;
- BF status;
- TD class;
- CL;
- loser return-kill floor;
- low/central/high projection;
- final kills;
- realized objective fights;
- realized between-objective skirmishes;
- result / ROI.

Audit specifically for:

- quiet-start anchoring;
- failing the early-live confirmation gate;
- over-de-duplicating contact into only objective windows;
- underpricing repeated neutral skirmishes;
- over-applying Threat Deterrence;
- underweighting high-T / low-M branches.

---

## 12. Retained Controls

- v0.3.50 event-window de-duplication remains active.
- Engage champions are still not counted as independent future fights.
- Total Kills now uses **OKP + FCI + CRR + SRR + CL**.
- Base Total Kills lower-bound gates remain +5pp pregame, +4pp early live, +3pp mid/late, with applicable surcharges capped at +9pp over break-even.
- v0.3.48 Kill Handicap KCV / Structure Substitution / NKB / RFI remains active.
- v0.3.47 Draft Primacy remains active.
- v0.3.45 Duration restrictions remain active.
- Minimum odds remain 1.60.
- Default shadow stake remains 0.25u; actual exposure remains 0u while official betting is paused.
- Same-map add-ons remain enabled only when each independently qualifies and joint correlation is explicitly priced.
- No martingale, rescue, loss chasing or stake escalation.
- Missing decision-critical state => PASS/HOLD.

Where this delta conflicts with v0.3.50 Total Kills interpretation, **v0.3.51 controls**.
