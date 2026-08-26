# Underdog +Kills Directional Audit — 2026-08-26

**Status:** `PENDING_NEXT_SLATE CALIBRATION REVIEW`  
**Current locked slate:** E14 KT Rolster vs HANJIN BRION  
**Active locked model:** LoL v0.3.58 at `95af8bcde298772e28f963818a71f0653d602a69`  
**Current E14 execution status:** `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`

## Executive finding

The recent underdog +kills branch is not behaving like a calibrated market family.

Airtable audit of settled underdog +kills from the 2026-08-19 through 2026-08-26 guard era, including KT +9.5 vs BRO Game 3, gives:

- Wins: 4
- Losses: 12
- Voids excluded
- Total settled stake: 4.0u
- Net P/L: approximately -2.0665u
- ROI: approximately -51.7%

Several of the losses were already separately audit-invalidated for missing or misapplied hard gates. The remaining pattern still shows a repeated directional failure rather than independent random misses.

## Current incident — KT +9.5 vs BRO Game 3

Entry at 13:14:

- BRO 5-2 KT
- BRO +3.1k gold
- towers 0-0
- dragons BRO 1-0
- KT +9.5 @1.982
- current BRO kill margin +3
- line failed at final BRO margin +10
- exact required future net expansion from entry: +7

Original reasoning over-credited KT's Wukong/Bard/Sivir/Zoe/Yorick reset, engage, waveclear and side-route inventory as kill-margin suppression.

Final user-authoritative result:

- BRO 13-3 KT
- final margin BRO +10
- KT +9.5 lost by 0.5
- BRO expanded kill margin by exactly +7 net kills after entry

## Procedural finding

This TAKE was invalid under an already-active hard rule before the outcome was known.

The 2026-08-23 underdog +kills hardening requires `LAC — Live Anti-Cascade Confirmation = PASS` from observed current-regime evidence.

At 13:14 there was no qualifying observed suppression cycle:

- no meaningful favorite pressure/contact window had been clearly demonstrated and then denied/reset by KT;
- no repeated live preservation across more than one meaningful contact/objective window existed;
- KT had no structural restraint such as actual side-lane/tower control materially reducing BRO's ability to force grouped cycles;
- the argument relied mostly on theoretical champion-kit routes.

Therefore `LAC` should have been `FAIL/UNRESOLVED`, making the correct contemporaneous verdict `HOLD/PASS`.

The historical prediction result remains Loss -0.25u. Process validity is separately invalidated.

## Repeated mechanism failure

The recurring underdog +kills error is not simply 'cushion too small.' It is a mechanism mismatch.

### 1. Theoretical survival is being confused with favorite-route suppression

The branch repeatedly credits:

- waveclear;
- disengage;
- engage/counter-engage;
- return-kill access;
- side-lane pressure;
- scaling;
- one independent carry;

as evidence that the favorite cannot widen the final kill margin.

But those tools only matter if they directly answer the favorite's actual margin-expansion mechanism.

Examples of favorite mechanisms that have repeatedly broken the underdog branch:

- pre-contact poke -> zone -> pick -> continuation;
- range advantage that forces the underdog to enter controlled space;
- mobile pick threats that avoid committed 5v5 engage;
- one accelerated carry with repeatable cleanup/reset access;
- objective-cycle pressure that creates serial compulsory fights;
- broad multi-role economy that makes the next two ordinary fights increasingly asymmetric.

Generic anti-engage or side-route tools are not automatic answers to these mechanisms.

### 2. Exact NKB arithmetic is being treated as psychological safety

Statements such as 'favorite needs +7 more future net kills' have repeatedly sounded safer than they are.

Seven future net kills can be produced by two ordinary objective cycles, for example:

- 4-0 fight then 3-0 continuation;
- 3-0 objective fight then 4-0 base-defense cleanup;
- two 4-1 fights.

NKB is arithmetic only. Its risk class must depend on remaining compulsory cycles, favorite continuation shape, total-kill environment and map control.

### 3. Quiet structure state is being misread as protection

`0-0 towers` or low current structural conversion often entered the narrative as evidence against a wide final kill margin.

That is not reliable. A pro game can remain structurally quiet and then produce a decisive objective fight plus serial cleanup. Kill margin and structure margin are related but not interchangeable.

Observed failed conversion or actual structural restraint is required; mere absence of towers is not suppression evidence.

### 4. LAC enforcement has been too permissive in practice

The existing LAC rule is conceptually correct but has not been executed strictly enough.

Draft theory has repeatedly leaked into live LAC decisions. The branch needs an operationally harder definition of what counts as observed suppression.

### 5. Side-neutral KHMC has not eliminated sign-selection bias

The parent model requires a signed final-margin distribution before sign selection, but live verdicts still tend to narratively gravitate toward the underdog cushion after seeing a large positive number.

This indicates sign-selection bias remains in execution even when the formal parent distribution is nominally present.

## Recent warning sample

Recent settled underdog +kills losses include, among others:

- DNS +8.5 vs BRO — Loss; later audit-invalidated for false/uncertified fallback
- DNS +7.5 vs BRO — Loss; later audit-invalidated for missing complete draft lock proof
- KRX +3.5 vs NS — Loss; later audit-invalidated as thin cushion
- LGD +12.5 vs BLG — Loss; later audit-invalidated for wrong-mechanism KMS/False-Stable read
- KT +6.5 vs T1 — Loss
- GEN +9.5 vs DK — Loss; later audit-invalidated for missing DIM/TAM/CAS and wrong interaction read
- SHFT +5.5 vs FNC — Loss
- NS +5.5 vs BFX — Loss
- HLEC +4.5 vs BFXY — Loss
- FNC +11.5 vs NAVI — Loss
- KRX.C +5.5 vs BFXY — Loss
- KT +9.5 vs BRO — Loss; current LAC hard-gate violation

Recent wins exist, but the aggregate 4-12 settled result demonstrates that the branch is not acceptably calibrated.

## Proposed next-slate changes

These are proposals only. They are not active inside the frozen E14 slate without explicit user-authorized relock.

### A. Directional suspension

Default underdog +kills verdict should be `HOLD/PASS` until a new calibrated authority epoch explicitly re-enables the branch.

Favorite -kills remains analytically separate and should not be disabled merely because underdog +kills is suspended.

### B. Mechanism-specific LAC

LAC must identify:

`FAVORITE_PRIMARY_MARGIN_ROUTE -> UNDERDOG_DIRECT_SUPPRESSION_MECHANISM -> OBSERVED_LIVE_EVIDENCE`

If the underdog answer is generic or does not directly address the favorite route, LAC fails.

Examples:

- favorite pre-contact poke/pick cannot be answered by 'we have counter-engage' unless live evidence shows the counter-engage actually prevents the poke/pick cycle from producing net kills;
- side-lane pressure does not count until it demonstrably removes favorite grouped-fight access or creates structure/tempo restraint.

### C. Two meaningful suppression windows

For ordinary underdog +kills candidates, require at least two meaningful live pressure/contact/objective windows in which the favorite had a plausible expansion opportunity and failed to widen margin materially because of an observed underdog mechanism.

Quiet elapsed time is not a window.

A single window may qualify only under exceptional, explicit evidence.

### D. Forced-cycle adjusted NKB

Replace raw `EXACT_NKB` interpretation with:

`NKB_PER_REMAINING_FORCED_CYCLE`

A nominal +7 future-net-kill hurdle is not automatically DEEP when two or more compulsory high-leverage cycles remain and the favorite has multi-kill continuation.

### E. Broad-lead anti-dog guard

Presumptive PASS on underdog +kills when all are true:

- favorite leads economy across at least three roles or has one overwhelming carry plus supporting role control;
- favorite also owns objective/tempo initiative;
- underdog has no demonstrated structural restraint;
- favorite primary margin route is repeatable through the next compulsory cycle;
- LAC has not shown mechanism-specific suppression.

### F. Side-route evidence hardening

Side-lane potential is neutral until it is observed to create one of:

- tower/structure pressure that forces favorite resources away;
- wave state that prevents grouped objective setup;
- tempo trade that materially limits serial fights;
- actual kill-return or escape path during the favorite's pressure cycle.

### G. Empirical calibration requirement

Do not re-enable underdog +kills simply because a prose fix is written.

Require a retrospective re-score of the recent sample under the proposed gates and a fresh shadow validation set before next real-money readiness discussion.

## Current slate action

E14 is now under procedural circuit breaker because the KT +9.5 TAKE violated an active LAC hard gate.

No new TAKE in any market family is allowed under the existing lock. Analysis/HOLD may continue. Resume requires the next valid slate lock or explicit user authorization to relock now.