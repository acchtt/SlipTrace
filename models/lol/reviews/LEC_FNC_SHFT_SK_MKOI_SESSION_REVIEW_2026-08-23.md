# LEC FNC–SHFT / SK–MKOI Session Execution Review — 2026-08-23

**Status:** CANONICAL REVIEW / v0.3.58 in-place enforcement input  
**Date:** 2026-08-23 UTC+7  
**Scope:** FNC vs SHFT Games 1–2 and SK vs MKOI Games 1–2  
**Model:** LoL v0.3.58  
**Historical positions:** preserve exactly as recorded; this review does not rewrite prior TAKEs, results, or P/L.

## 1. Executive finding

The session did not justify a broad model reset.

The strongest signal was **live Moneyline**, while the repeated failures were concentrated in two execution families:

1. **Duration Over** was certified from state descriptors and theoretical delay tools without sufficient observed clock-consuming evidence.
2. **Underdog +kills** was certified from a shallow live cushion without enough demonstrated live kill-margin suppression.

The correction is therefore narrow: retain the live-ML framework, harden Duration Over certificate enforcement, and add a mandatory live anti-cascade confirmation layer after draft-only underdog +kills stability.

## 2. FNC vs SHFT Game 1 — SHFT +5.5 kills @1.964

Historical verdict: TAKE.  
Result: LOSS.  
Final user-confirmed kill score: FNC 10–2 SHFT.

Entry state used by the decision was approximately:

- SHFT 1–0 kills;
- SHFT +137g;
- SHFT 1–0 dragons;
- towers 0–0.

### Error

The live read over-credited the numerical cushion and nominal early lead while under-crediting FNC's repeatable continuation through Jarvan IV / Rumble / Yone.

The state did **not** demonstrate enough live kill-margin suppression:

- no tower control;
- no meaningful structural control;
- no proven repeated reset/survival sequence after FNC gained pressure;
- no observed multi-cycle evidence that SHFT could prevent FNC from turning one successful engage into a second and third net kill-margin expansion.

A small gold lead, one dragon, a kill lead, theoretical peel/waveclear, or the displayed +kills buffer are not live anti-cascade proof.

### Required correction

After DIM + UDKC `STABLE` and the existing UCS arithmetic, an underdog +kills TAKE must also pass a separate **LAC — Live Anti-Cascade Confirmation** gate. Draft stability says the underdog *can* possess fallback mechanisms; LAC asks whether those mechanisms are actually preserved in the current live regime.

## 3. FNC vs SHFT Game 2 — FNC ML @1.918

Historical verdict: TAKE.  
Result: WIN.

At 9:11 SHFT led 5–3 kills and about +835g, but had no tower or objective conversion. FNC's Nocturne / Ryze / Rell access remained live, and the market price required only approximately coin-flip win probability.

### Finding

This is a **positive reference** for the current Live ML framework.

The decision correctly separated a resource lead from a control/terminal lead. No new conservative ML gate should be added because other families failed in the same session.

Retain:

- two-snapshot live eligibility;
- Lead Decomposition;
- current-state CFC;
- neutral-fight stress;
- Draft Prior State / LRO when required;
- minimum odds 1.60.

## 4. FNC vs SHFT Game 2 — Over 34 @2.269

Historical verdict: TAKE.  
Result: LOSS.  
Final user-confirmed duration: 33 minutes.

At 26:31 FNC led 14–12, about +3.1k, had Baron 1–0, towers were 3–3, inhibitors 0–0, and SHFT led dragons 2–1.

### Error

The decision treated SHFT's Taliyah + Tristana waveclear as if theoretical defensive capacity were equivalent to **observed conversion denial**.

No concrete failed-conversion sequence was identified before the TAKE. FNC then converted the Baron/lead faster than projected.

Under the already-existing canonical Duration Over rules, this should not have passed unless the PRE_TAKE_CERT contained two independent positive future clock-consuming mechanisms with at least one grounded in observed failed conversion or equivalent repeated denial.

### Required correction

Duration Over must record the concrete evidence identity for the failed conversion / repeated denial. Generic statements such as “they have waveclear,” “towers are still standing,” or “the map has been slow” are not enough.

## 5. SK vs MKOI Game 1 — Over 32 @2.128

Historical verdict: TAKE.  
Result: LOSS.

At 11:28 the map was 3–2 kills, MKOI +269g, towers 0–0, dragons 1–1.

### Error

This was a direct execution violation of the existing Duration Over amendment.

The analysis used:

- close gold;
- 0–0 towers;
- neutral objectives;
- a quiet early map;

as if these were positive stall evidence. They were only **ABSENT CONVERSION** descriptors. No meaningful conversion opportunity had yet been shown to fail.

Correct pre-entry classification under canonical v0.3.58 should have been `HOLD/PASS`.

### Required correction

The Duration Over PRE_TAKE_CERT must fail mechanically when the evidence remains `ABSENT CONVERSION`, regardless of attractive price.

## 6. SK vs MKOI Game 2 — no position

Observed live sequence included MKOI prices falling to 1.327, 1.162 and 1.125 while MKOI led early. The 1.60 minimum blocked favorite ML. SK +10.5 was also rejected because the large displayed cushion was not supported by anti-cascade evidence.

User later confirmed SK won the map.

### Finding

The eventual result is **not** used to retroactively claim a missed SK TAKE. The correct process lesson is that the existing minimum-odds floor and refusal to treat a large +kills buffer as self-certifying were both appropriate.

Do not loosen those controls because the underdog eventually won.

## 7. Mandatory enforcement changes

### 7.1 DOVC — Duration Over Verification Certificate

Every Duration Over candidate must explicitly resolve:

`CONVERSION_CLASS | POSITIVE_CLOCK_MECH_1 | POSITIVE_CLOCK_MECH_2 | FAILED_CONVERSION_OR_EQUIVALENT | OBSERVED_STALL_EVIDENCE_ID | CLOCK_CAUSALITY | STRUCTURE_SUBSTITUTION | SHORTEST_CASCADE_TEST | SURVIVAL_HORIZON | PRICE`

Hard rules:

- `CONVERSION_CLASS = ABSENT` => HOLD/PASS.
- Theoretical waveclear/peel/disengage is not `FAILED_CONVERSION_OR_EQUIVALENT` until pressure has actually been delayed/denied in live evidence.
- 0–0 towers, low tower count, low kills, close gold, neutral dragons or quiet elapsed time cannot count as a positive clock mechanism.
- `OBSERVED_STALL_EVIDENCE_ID` must identify the actual live event/window used as proof; narrative-only evidence fails.
- If the shortest plausible next compulsory fight/objective can open serial structures and base access inside the survival horizon, the Over must fail unless independent demonstrated delay still leaves sufficient buffer.

### 7.2 LAC — Live Anti-Cascade Confirmation for underdog +kills

After draft-only DIM + UDKC `STABLE`, live preservation and UCS, every underdog +kills candidate must also resolve `LAC = PASS`.

LAC asks:

**“Has the current live regime demonstrated that the underdog can suppress repeated favorite net kill-margin expansion, rather than merely owning a numerical cushion right now?”**

Positive support must include actual current-regime evidence such as:

- a meaningful favorite pressure/contact cycle that failed to expand the kill margin because the underdog reset, returned kills, disengaged or structurally denied continuation; and/or
- real structural/economy/objective control that directly reduces the favorite's forced-contact access, supported by role-leverage decomposition rather than one isolated asset.

The following are never sufficient by themselves:

- current kill lead;
- one dragon;
- small gold lead;
- 0–0 towers;
- large +kills line;
- theoretical scaling/waveclear/peel;
- safe marksman play;
- price attractiveness.

If the favorite has repeatable engage/continuation and the underdog's live edge is shallow/non-structural, `LAC = FAIL/UNRESOLVED` and +kills is HOLD.

## 8. Execution latency

The DK ML incident in the broader session showed that a correct verdict can arrive late even when the sportsbook price and game state remain unchanged.

No new analytical gate is required. Existing state-change expiry already handles this correctly:

- if state/price materially changes before verdict/entry, rebuild from zero;
- if the synchronized state and executable price are unchanged, the same decision window remains usable.

Operationally, preserve **verdict-first** behavior: no Airtable write, web research, or nonessential connector work may occur before the visible verdict.

## 9. Anti-overfit guard

Do not respond to this session by:

- suppressing Live ML frequency generally;
- raising the global minimum odds;
- adding arbitrary elapsed-time minimums for Duration;
- requiring tower leads mechanically for every underdog +kills bet;
- treating SK's eventual G2 win as proof that an SK bet was missed;
- rewriting historical positions as if they were never issued.

The correction is mechanism-specific and fail-closed only where the missing proof was identified.

## 10. Canonical action

User instruction on 2026-08-23 UTC+7: **“Adjust accordingly.”**

This explicitly authorizes an in-place v0.3.58 enforcement amendment and a new authority epoch for the 2026-08-23 slate. No v0.3.59/v0.3.60 restoration or new analytical version is authorized.
