# HLE.C vs GGA Game 2 — Under Skirmish-Recurrence Review

**Date:** 2026-08-10  
**Model at entry:** LoL v0.3.50  
**Market:** Total Kills  
**Confirmed position:** Under 33.5 kills @1.690, 0.25u shadow  
**Entry clock:** 7:47  
**Entry state:** GGA 2-1 HLE.C, GGA +1.0k gold, towers 0-0, HLE.C 1-0 dragons, Barons 0-0  
**Final:** GGA won 20-15 at 30:30, 35 total kills  
**Result:** LOSS -0.25u

Companion same-map position: GGA +7.5 kills @2.082 — WIN +0.2705u. Net Game 2 shadow P/L +0.0205u.

## Draft

GGA: Jayce / Skarner / Syndra / Varus / Leona  
HLE.C: Yorick / Lee Sin / Annie / Jhin / Alistar

## What the entry read got right

- Current kill count was low: only 3 kills at 7:47.
- GGA had ranged poke/choke tools capable of producing concession or zoning around some objective windows.
- The Under line had a large arithmetic cushion: 30 additional kills could occur and the final would still land at 33.
- GGA +7.5 and Under 33.5 were not nested; the final itself proved the one-win/one-loss branch was real: GGA won by 5 while total kills reached 35.

## What the entry read got wrong

### 1. It violated the retained quiet-start confirmation gate

v0.3.49 already required an early Under upgrade to have at least one of:

- two synchronized live snapshots showing both low OKP and declining/limited FCI/CRR;
- repeated realized contact with low CL because disengage/peel is functioning;
- a clean structure-only/terminal branch that removes future contact windows.

At 7:47 there was only one meaningful live confirmation snapshot for the Under thesis, no demonstrated low-CL contact pattern, and no terminal structure-only branch.

The correct process verdict under the retained rule should therefore have been HOLD/PASS, not TAKE.

### 2. Objective-window de-duplication suppressed between-objective skirmish recurrence

v0.3.50 correctly prevents counting every engage champion as a separate future fight. The error here was the opposite: after de-duplication, the projection became too event-centric.

Both drafts had repeatable, independent ways to create fights outside formal objective contests:

- GGA: Skarner displacement/catch plus Leona first contact, with Syndra follow-up and Jayce/Varus pressure;
- HLE.C: Lee Sin access plus Annie/Alistar hard engage and counter-engage.

These tools did not create five independent objective windows, but they did create a persistent **between-window skirmish reserve** through vision contests, lane transitions, side-lane collapses, jungle entrances and post-reset re-engages.

User settlement note: **many skirmishes happened**. The final 35 kills confirm that the recurrent-contact branch was materially underweighted.

### 3. Threat Deterrence was over-applied

GGA poke/choke could deter some direct contests, but Threat Deterrence was treated as if it broadly lowered contact realization.

That was too strong because HLE.C had reliable hard access that did not require voluntarily walking into GGA's zone. Lee Sin, Annie and Alistar could start contact from flank, fog or transition states. GGA also had its own hard engage.

When both teams possess repeatable, matchup-functional hard access, one side's poke/zone control cannot automatically be converted into a global CRR discount.

### 4. The Under cushion was not stress-tested against a high-contact branch

From 3 current kills, Under 33.5 loses at 34+, requiring 31 additional kills.

The analysis focused on the size of the cushion rather than asking whether the high-contact branch could plausibly generate 31+ kills through repeated 2-4 kill skirmishes plus one or two larger objective/base fights.

A large cushion is not sufficient if the draft supports many recurrent contacts with medium/high CL.

### 5. The same-map joint matrix underweighted high-T / low-M

The companion GGA +7.5 position was strong because GGA could win or lose narrowly on kill margin. That same mechanism increased the probability of a **high total / modest margin** branch: traded skirmishes keep M compressed while T rises.

Final outcome: GGA 20-15. This is exactly the high-T / low-M branch.

The joint distribution should have assigned materially more weight to `GGA +7.5 wins / Under 33.5 loses`.

## Corrected interpretation at 7:47

- OKP: LOW, but one snapshot only.
- Objective FCI: medium.
- Between-window skirmish recurrence: HIGH.
- CRR: medium/high overall once neutral skirmish cycles are included.
- CL: medium/high; both sides had reliable hard engage and limited clean disengage once caught.
- Threat Deterrence: local, not global.
- Loser return-kill floor: medium/high because both sides could initiate and trade kills.
- Under 33.5 @1.690: **HOLD/PASS**, primarily due failed early-confirmation gate and high recurrent-contact reserve.

## Model correction

Promote to v0.3.51:

1. hard-enforce the early-live Under confirmation gate;
2. add explicit **Skirmish Recurrence Reserve (SRR)** for repeatable between-objective contact;
3. add **Bidirectional Forcing** as an Under risk multiplier when both teams have independent reliable engage/pick mechanisms;
4. require Threat Deterrence to survive an opponent hard-access override test;
5. require a high-contact branch stress test against the remaining kill cushion;
6. require same-map T/M joint matrices to explicitly price the high-T / low-M branch when +kills survival and mutual engage coexist.

This correction is additive to v0.3.50. It does not reverse event-window de-duplication or concession logic.
