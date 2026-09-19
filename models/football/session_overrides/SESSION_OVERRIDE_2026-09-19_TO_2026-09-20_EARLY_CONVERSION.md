# Football A — Early-Conversion Execution Override — 2026-09-19 to 2026-09-20

**Status:** TEMPORARY TWO-DAY EXECUTION EXPERIMENT — NOT A PERMANENT MODEL PATCH  
**Model:** Football A  
**Valid from:** 2026-09-19 10:40 ICT (UTC+7)  
**Expires:** 2026-09-21 00:00 ICT (UTC+7), end-exclusive  
**Scope:** Normal Chat XI / odds / live execution on Saturday 2026-09-19 and Sunday 2026-09-20 only  
**Purpose:** Test the 3-day early-goal / decay-latency audit finding without changing permanent Football A structure.

This file does **not** increment the Football model version, rewrite frozen PRE, promote B+/PASS, or retroactively create exposure. Outside the validity window, ignore it completely.

All permanent Football A rules remain active except where this file explicitly changes post-goal execution handling for the eligible lane below.

---

## 1. EARLY-CONVERSION ELIGIBLE — narrow gate only

Tag a fixture **EARLY-CONVERSION ELIGIBLE** before or at the XI/market stage only when all are true:

1. frozen structure is **A1 FOCUS or A2 FOCUS**;
2. the match is either:
   - **TRUE CC+ / elite carrier** with an independently credible 3+ team-goal path; or
   - **elite two-sided** with strong route quality and failure resistance;
3. confirmed XI preserves the qualifying route(s);
4. market disagreement is high enough that the normal plan would otherwise wait for same-line price or live decay;
5. no material route damage, red card, major attacking injury, tactical suppression, or competition-incentive veto exists.

Do **not** grant this flag merely because a market is high, a favorite is short, or recent scores are large.

### Ineligible by default

No automatic EARLY-CONVERSION privilege for:

- A2 WATCHLIST;
- B+ / B / PASS;
- youth/Uxx or other exception-only lanes;
- weak one-route carrier profiles;
- fragile secondary-route cases;
- unresolved XI / structural states.

A user may still grant a separate match-specific exception, but that is not the same as this two-day flag and must be logged separately.

---

## 2. Goal before planned decay — immediate one-time reprice

If an EARLY-CONVERSION ELIGIBLE fixture scores **before** its frozen 0-0 trigger / live-decay target:

1. the old score-state trigger expires immediately;
2. perform one state-integrity check;
3. if the original thesis survives, **reprice immediately once** for the new score epoch;
4. use **remaining-goal burden**, not a mechanical +1 translation of the old total;
5. prefer the nearest protected total that does not demand an excessive number of additional goals;
6. freeze that new target and minimum price immediately;
7. do not move the target deeper again merely because time passes.

A further goal creates a new score epoch and permits one fresh recheck.

---

## 3. Remaining-goal burden rule

For this two-day test, the post-goal target should normally require roughly **two additional goals for useful protection**, rather than repeatedly preserving a three-more-goals requirement after early conversion.

Use these as execution guides, not automatic formulas:

- **1-0 / 0-1:** prefer roughly **O3.0**; **O3.25** only for exceptional A1 / TRUE CC+ continuation support.
- **1-1:** prefer roughly **O3.5–O3.75**; avoid reflexive O4.25+ chasing.
- **2-0 / 0-2:** prefer roughly **O4.0**; two further goals push and three further goals win.
- **2-1 / 1-2:** prefer roughly **O4.0–O4.25** depending on route quality and protection.

At every score epoch:

- lowest acceptable burden first;
- then price floor;
- price only as tie-breaker.

Do not stretch burden to obtain a prettier price.

---

## 4. Immediate post-goal direct execution

For an EARLY-CONVERSION ELIGIBLE fixture, the newly repriced score-epoch line may become immediately executable when:

- it is at or below the newly frozen remaining-goal burden;
- price is **>=1.65** (preferred **>=1.70**);
- the scoring event confirms or preserves the pre-identified route rather than destroying it;
- no negative state-change veto exists;
- applicable upper-tail / priority-inversion controls remain clear.

This is **not** permission to chase the sportsbook's goal-driven expansion.

If the only available board remains materially above the newly supported score-epoch burden, WAIT for the frozen target. Do not fabricate an unavailable line.

---

## 4A. Repeated-score escape hatch — stop waiting for an unavailable protected line

This section is active for the Sep 19–20 trial after the Monterrey W–Necaxa W audit showed that repeated carrier goals can outrun every protected decay trigger while the sportsbook total never returns to the frozen target.

For an **EARLY-CONVERSION ELIGIBLE** fixture only, activate **REPEATED-SCORE ESCAPE HATCH** when either condition occurs:

1. **two goals arrive before the first protected decay trigger can execute**; or
2. **two consecutive score-epoch triggers expire because another goal arrives before the target line is ever quoted**.

Once active, do **not** keep waiting indefinitely for a lower total that the market may never print.

At the next stable score epoch, a one-time **CURRENT-MARKET CONTINUATION ENTRY** may execute if all are true:

- the original A1/A2 FOCUS TRUE CC+ / elite two-sided thesis remains intact;
- the qualifying carrier / route has already converted at least twice, or both elite routes have activated;
- score time is normally **55' or earlier**; later use requires exceptional continuation evidence;
- no red card, major attacking injury, tactical shutdown, or route-damage veto exists;
- price is **>=1.65** (preferred **>=1.70**);
- the **lowest currently available Over line** requires **no more than three additional goals to avoid a full loss** from the current score state;
- the current line is not selected merely because it pays more than a lower protected alternative;
- one-exposure-per-match remains mandatory.

Examples:

- at **2-0**, O5.0 can qualify because three further goals produce a push; O5.25/O5.5 normally does not;
- at **3-0**, O6.0 can qualify because three further goals produce a push; prefer any lower available protected line first;
- at **4-0**, O7.0 can qualify on the same logic, but O7.25+ normally does not.

This is deliberately more aggressive than the normal protected-decay path and exists only for the two-day experiment. It is **not** a blanket permission to chase every expanding total.

If this escape hatch fires, persist:

- `REPEATED-SCORE ESCAPE HATCH = YES`;
- count of expired score-epoch triggers;
- current score/minute;
- lowest available Over line/price;
- additional goals required to avoid full loss;
- state-integrity result;
- final action.

A further goal after an escape-hatch entry does not create another exposure. If no qualifying current-market line exists, HOLD; do not fabricate one.

---

## 5. Route activation — useful but not sufficient

An early goal may improve state integrity when:

- the expected TRUE CC+ carrier scores first; or
- a previously fragile secondary route scores and forces the stronger route to chase.

However, **route activation alone is not continuation proof**.

Audit counterexample: Greuther Fürth–Magdeburg reached 1-1 with both routes active and still finished 1-1.

Therefore require the original A1/A2 FOCUS quality and failure resistance to remain intact.

---

## 6. Control/compression and red-card veto

Do not treat 2-0 as automatically bullish.

At 2-0 explicitly test:

- carrier control / game-management compression;
- opponent route viability;
- substitutions / tactical slowdown;
- red card or major injury;
- whether the qualifying carrier still has credible continuation depth.

A red card is a material state-change event and requires a fresh state-integrity review. It may cancel the trigger even if the pre-card score path was favorable.

Kuwait U23–Uzbekistan U23 and the Alianza 2-0 failure remain audit warnings against blind continuation.

---

## 7. Interaction with the Sep-18 execution-relaxation override

From this file's activation until **2026-09-19 12:00 ICT**, both temporary files may be active.

When both apply:

- structural PRE remains frozen;
- the Sep-18 execution-relaxation file governs its O2.5/O2.75, -0.25 undercut, frozen-trigger, and score-epoch relaxations;
- this file adds the narrower **EARLY-CONVERSION ELIGIBLE** immediate post-goal repricing rule for qualifying A1/A2 FOCUS profiles.

After **2026-09-19 12:00 ICT**, the Sep-18 execution-relaxation file expires. This Early-Conversion override remains active on its own through Sunday.

No other Sep-18 relaxation survives past noon unless separately authorized.

---

## 8. Persistence labels

For every decision affected by this file, persist:

- `SESSION EARLY-CONVERSION 2026-09-19/20`
- `EARLY-CONVERSION ELIGIBLE = YES/NO`
- original frozen PRE / structural ceiling;
- original 0-0 trigger;
- first goal score/minute;
- scorer route = expected carrier / secondary route / adverse route;
- `STATE INTEGRITY = CLEAR / DAMAGED / NEW THESIS`;
- new score-epoch target;
- remaining-goal burden;
- minimum price;
- execution decision;
- cancellation event if any.

Website Picks remain real official exposure only when the new frozen score-epoch target is actually available and accepted. Never backfill after another goal or price move.

---

## 9. Expiry and audit

At **2026-09-21 00:00 ICT**, this override expires automatically.

After expiry:

- stop applying EARLY-CONVERSION ELIGIBLE;
- revert to the permanent Football A stack;
- keep all Sep 19–20 decisions auditable;
- compare official results and counterfactual earlier-entry lines;
- do not promote this rule permanently without an explicit post-Sunday user decision.
