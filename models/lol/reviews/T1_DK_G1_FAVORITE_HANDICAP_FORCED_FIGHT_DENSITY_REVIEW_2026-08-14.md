# T1 vs DK G1 — Favorite Handicap Forced-Fight Density Review

**Date:** 2026-08-14 UTC+7  
**Map:** LCK 2026 Rounds 3–4 — Dplus KIA vs T1, Game 1  
**Model at decision:** LoL v0.3.57  
**Review status:** Batch-revision evidence

## Decision point

At 20:27:

- T1 led 16–8 kills, signed kill margin `+8`;
- T1 held approximately +5.4k gold;
- T1 led towers 3–1;
- T1 led dragons 3–0;
- Baron: 0–0;
- inhibitors: 0–0;
- market: T1 -15.5 kills @1.617 / DK +15.5 @2.213.

The live verdict was PASS on T1 -15.5 because the model required too much additional proof of terminal conversion and operationally treated Baron/inhibitor control as necessary confirmation.

Final: T1 won 30–11 at 31:10, final kill margin `+19`. T1 -15.5 would have covered.

## Primary error

**Favorite -kills false PASS caused by under-translating terminal pressure into future forced-fight density.**

The model correctly recognized that T1 had terminal pressure, but it did not convert the combination of Soul-point pressure, imminent Baron pressure, large economy edge and superior initiation/access into a sufficiently high probability of repeated compulsory fights.

The remaining fights were not fully optional for DK. At 0–3 dragons, DK faced scheduled Soul defense; once Baron became available, map control and base pressure created additional forced-entry windows. T1's Vi/Camille/Olaf access made those contests asymmetric.

## Correction principle

Existing Baron ownership or an inhibitor taken must **not** be mandatory prerequisites for favorite -kills.

They remain strong supporting evidence, but waiting for them can move the market from a still-playable favorite handicap to a much larger, value-depleted line.

Favorite -kills should instead evaluate whether the current state already implies **high future forced-fight density** before terminal structures are taken.

Key inputs:

1. current signed kill margin;
2. additional net margin required by the executable handicap;
3. role-weighted economy / TEI and lead quality;
4. dragon/Soul/Baron/base-pressure schedule;
5. whether the underdog can avoid contests by cross-mapping, waveclear or safe concession;
6. favorite initiation/access reliability and continuation;
7. underdog reset/survival quality under pressured entry;
8. Structure Substitution — whether the favorite can close without generating enough additional fights.

## Reference regrade

At 20:27, T1 -15.5 @1.617 should be treated as **eligible for a TAKE under the revised favorite-handicap framework**, because the 3–0 dragon schedule, +5.4k economy, superior access and limited DK ability to avoid future contests created a high forced-fight-density branch before any Baron or inhibitor had already been secured.

This correction does **not** mean every large favorite lead at Soul point qualifies. The handicap still requires signed-margin distribution, expected remaining fight count, net-kill expansion, KCV/NKB/RFI/Structure Substitution and exact executable odds.
