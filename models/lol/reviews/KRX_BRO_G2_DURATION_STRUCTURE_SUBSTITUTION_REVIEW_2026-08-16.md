# KRX vs BRO Game 2 — Duration Structure-Substitution Review

**Date:** 2026-08-16 UTC+7  
**Model at entry:** LoL v0.3.58 temporary override  
**Market:** Over 33 minutes @1.690  
**Shadow stake:** 0.25u  
**Result:** LOSS -0.25u

## Entry state

At 14:52:

- BRO 1-0 KRX kills;
- KRX approximately +860 gold;
- KRX 1-0 towers;
- KRX 1-0 dragons;
- Baron 0-0;
- Over 33 minutes @1.690.

The live verdict treated the low kill count and limited absolute structure count as evidence that the map was consuming clock slowly.

## Review verdict

**The TAKE was analytically invalid. Correct verdict: PASS.**

The core error was equating low combat volume / low absolute tower count with low terminal velocity.

KRX were already progressing the map through **Structure Substitution**: they held the gold lead, first tower and first dragon without needing kills. That is not observed stall. It is evidence that map state can advance while combat remains quiet.

## Primary error — Structure Substitution misread

The relevant distinction is:

- **ABSENT CONVERSION:** few structures have fallen because a meaningful conversion window has not occurred or has not been tested. This is neutral for an Over.
- **FAILED CONVERSION:** a team earned a real tempo/fight/objective/wave-access window and the opponent demonstrably denied expected structural/base progress. This can support an Over.

At 14:52 there was no demonstrated failed conversion. KRX had instead already converted into a tower and dragon.

Therefore the low structure count could not be used as positive Over evidence.

## Secondary error — low kills used as stall evidence

One total kill at 14:52 described the combat history, not the future game-ending path.

At 17:52 the game still had only one total kill, yet KRX had progressed to:

- 2-0 dragons;
- 2-1 towers;
- approximately even gold.

This confirms that **low kills did not imply low map progression**. Objective and structure conversion continued independently of combat volume.

## Mandatory correction for v0.3.58

For Duration Over analysis:

1. Low kills, 0-0 towers, no first tower, or a low absolute tower count are neutral state descriptors by default.
2. They may not count as stall mechanisms without observed denial of a meaningful conversion opportunity.
3. Explicitly classify structural evidence as `ABSENT CONVERSION` or `FAILED CONVERSION`.
4. Structure Substitution must be checked: objective/tower progress with low kills can indicate clock compression rather than stall.
5. Before an Over, test the shortest plausible cascade:
   `next compulsory fight/objective -> first/next tower -> serial structures -> base access -> Nexus`.
6. If the Over thesis is primarily "little has happened so far" rather than "real conversion attempts are repeatedly being denied," verdict must be HOLD/PASS.
7. Low kill pace cannot independently satisfy a Duration stall mechanism; Total Kills and Duration remain separate distributions.

## Reference correction

At 14:52, with KRX +860 gold, 1-0 towers, 1-0 dragons and only one total kill:

**Correct verdict: PASS — Over 33 minutes @1.690 — 0u.**

This is a model/application correction, not variance attribution.
