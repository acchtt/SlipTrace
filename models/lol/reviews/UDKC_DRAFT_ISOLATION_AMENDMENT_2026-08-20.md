# UDKC Draft-Isolation Amendment — 2026-08-20

**Canonical model:** LoL v0.3.58  
**Status:** in-place governance amendment; no new analytical version.

## User correction

The user clarified that underdog +kills eligibility should depend on how accurately the model reads the locked draft and subsequent game states, not on whether the draft screenshot happened to arrive before or after the game clock started.

That correction is accepted.

## Problem with the prior guard

The 2026-08-19 UDKC guard correctly addressed a real failure: live score/gold/line-buffer evidence had been used to invent KMS/RLD proof that had not been established from the draft.

However, the first implementation over-corrected by making **pre-live timestamp/persistence** itself a hard eligibility requirement. That could lock out a valid market solely because the exact draft was first received inside a live screenshot or a new chat began mid-map.

That is not analytically necessary. The relevant protection is **draft isolation**, not wall-clock timing.

## Canonical correction

UDKC remains mandatory and fail-closed, but it is now a **draft-only certificate rather than a pre-live timestamp certificate**.

A UDKC may be completed after live play begins if the exact locked draft is known and the analyst runs a strict Draft-Isolation Pass:

1. identify the exact ten champions, sides, and underdog independently of current live results;
2. ignore current kills, gold, objectives, structures, odds movement, handicap size, and current kill margin while certifying;
3. fully resolve DER / FRI / SRI / FER / PDC / PST / ARI / KPA / KMS / RLD / False-Stable Guard / DCR / FF / hard Draft-Collapse Veto;
4. persist the completed certificate before any +kills TAKE;
5. only then apply live snapshots and exact line arithmetic.

If the exact draft cannot be established, or any mandatory certificate field is unresolved, the market remains HOLD/PASS.

## What did not change

- KMS still requires actual suppression of the favorite's repeatable margin-expansion routes.
- Safe ADC, peel, waveclear, scaling, a large +kills buffer, small current margin, 0-0 towers, grubs, or isolated lane gold are not standalone KMS proof.
- Live evidence cannot be used inside the draft certificate.
- Live evidence may preserve or downgrade a STABLE draft certificate; it cannot repair a draft that is genuinely FRAGILE/ABSENT.
- Two clean live snapshots, exact signed margin arithmetic, price/executability checks, and all other market-family gates remain mandatory.

## New-chat behavior

A new chat starting mid-map should first search for a persisted UDKC. If none exists but the exact locked draft is available from saved evidence or the user's screenshot, it may reconstruct the UDKC using Draft Isolation. Missing persistence alone is no longer a map-long veto.

The fail-closed condition is now **missing/ambiguous draft or incomplete mechanism certification**, not screenshot timing.
