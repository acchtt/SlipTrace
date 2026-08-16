# Seven-Loss Streak Review — Regime Persistence / ML Control

**Date:** 2026-08-16 UTC+7  
**Audit boundary:** LoL v0.3.57+ shadow audit  
**Decision:** batch-review basis for user-authorized v0.3.60 correction

## Executive finding

The seven consecutive losses from the v0.3.59 high-water mark were **not seven unrelated misses**.

Immediately before the streak, the audit had reached approximately **+1.14925u** after DNS +10.5 kills @1.877 won. Seven consecutive 0.25u losses then moved the aggregate to approximately **-0.60075u**.

The sequence:

1. BFX vs DNS G2 — Under 34.5 kills @1.724 — LOSS
2. BLG vs WE G1 — Under 28 minutes @2.161 — LOSS
3. SK vs FNC G1 — SK +7.5 kills @2.041 — LOSS, but procedurally invalid TAKE
4. SK vs FNC G2 — Under 21.5 kills @1.860 — LOSS
5. G2 vs SHFT G1 — Under 26.5 kills @1.899 — LOSS
6. DNS vs T1A G2 — DNS ML @1.877 — LOSS
7. DNS vs T1A G3 — DNS ML @1.883 — LOSS

One loss, SK +7.5 vs FNC, was already identified as an **execution/application error**: draft-time fallback was never positively certified and ordinary live evidence illegally upgraded it. The correct verdict was PASS. Existing fallback fail-closed hardening remains correct and does not require a new analytical relaxation/tightening.

The remaining six legitimate model losses cluster into only two analytical mechanisms:

- **4 losses:** overconfidence that a currently observed game regime would persist into future objective cycles;
- **2 losses:** overpricing a modest resource/objective lead while underweighting the trailing team's easier compulsory-fight initiation/re-entry architecture.

This is a concentrated correction target, not evidence that all v0.3.58/v0.3.59 market families failed.

---

## 1. Total Kills Under — current quiet was promoted into future quiet

### BFX vs DNS G2 — Under 34.5 @1.724

Entry used a 16:55 -> 18:45 kill lull plus Structure Substitution as evidence of cooled CRR.

The error was not that the quiet interval was fake. The error was **forward persistence**: Baron-phase and dragon-phase compulsory contact remained ahead, and those future windows reactivated kill recurrence.

### SK vs FNC G2 — Under 21.5 @1.860

Only five kills had occurred by 18:11. The line still required seventeen more kills to lose.

Again, observed suppression was real. But the thesis did not sufficiently stress the remaining dragon/objective schedule and the fact that future contact density could increase materially once the game moved from lane/transition state into repeated neutral-objective contests.

### G2 vs SHFT G1 — Under 26.5 @1.899

This is the strongest recurrence example.

- 3:45: 2 total kills
- 9:55 entry: still 2 total kills
- 16:45: 3 total kills
- 20:15: 8 total kills
- 28:35: 15 total kills
- final: 35 total kills

The entry correctly observed extremely low early CRR. But it effectively priced:

`observed low CRR -> persistent low CRR`

without sufficiently proving:

`next compulsory objective cycle -> still low realized contact`

A quiet interval between objectives must not carry the same evidentiary weight as a successfully suppressed compulsory fight/objective window.

### Batch conclusion

For Total Kills Under, the model needs an explicit **forward regime persistence** gate. Past quiet alone cannot certify future suppression.

---

## 2. Duration Under — shortest plausible close route was treated as robust close probability

### BLG vs WE G1 — Under 28 minutes @2.161

At 20:04 BLG led 7-2, roughly +5.3k role-weighted economy, towers 3-1 and dragons 2-1 with Baron available. The route:

`fight/Baron -> serial structures -> base`

was credible.

But the Under needed the game to end inside roughly eight minutes. A **credible shortest route** is not the same as a route robust to one normal disruption: partial Baron conversion, defender waveclear, a reset, a failed push, a traded objective, or a delayed second structure.

The entry overestimated the probability that the fastest realistic branch would be the realized branch.

### Batch conclusion

Duration Under requires a **route-robustness / one-disruption stress test**, not only a shortest-path calculation. A route that only clears the line if every conversion succeeds cleanly is too fragile unless the retained terminal-state exception applies.

---

## 3. Live ML — resource lead was confused with control lead

### DNS vs T1A G2 — DNS ML @1.877

At 8:01 DNS had:

- approximately +967g;
- 1-1 kills;
- 1-0 dragons;
- 0-0 towers.

The resource/objective edge was real. But T1A retained easier hard-start access through Jarvan IV + Alistar, backed by Anivia/Sivir control and follow-up.

DNS had more resources; DNS did **not yet clearly control how the next important fights would begin**.

### DNS vs T1A G3 — DNS ML @1.883

At 12:45 DNS had:

- 5-4 kills;
- approximately +1.2k;
- 1-0 dragons;
- 0-0 towers.

The same mistake repeated one map later. T1A's Wukong + Bard + Sylas package had materially easier neutral-setup first contact, re-engage and backline access. Olaf also punished failed DNS forward commits.

The current lead was upgraded into win probability too aggressively even though the next two compulsory fights could still be dictated by T1A's draft.

### Batch conclusion

Live ML must explicitly separate:

- **Resource Lead** — gold/CS/role economy;
- **Structural Lead** — towers/base access/wave and vision depth;
- **Objective-Schedule Control** — who benefits from the next compulsory windows;
- **Fight-Control Lead** — who has easier first contact, re-engage, backline access, disengage/reset and objective turn.

A resource lead without structural separation is not automatically a control lead.

---

## 4. Same-mechanism repetition problem

DNS ML G3 occurred immediately after DNS ML G2 lost through a mechanism that remained materially relevant: T1A's easier compulsory-fight access could erase a modest DNS resource lead.

The prior loss alone should never create a blanket veto. However, once a loss has been **mechanistically diagnosed**, the next same-series TAKE relying on the same thesis is not independent evidence.

The failed mechanism must be explicitly re-tested. A materially different draft, structural state, objective schedule, or demonstrated answer to the prior forcing route can clear the re-certification. Merely seeing another +1k lead cannot.

---

## 5. What did NOT fail in this streak

The streak contains:

- no favorite -kills loss;
- no valid post-hardening underdog +kills loss;
- no wide-cushion fallback loss after the corrected certification procedure;
- no evidence that v0.3.58 FFD/RNE should be tightened globally.

The correction should therefore be narrow:

1. Total Kills Under forward persistence;
2. Duration Under route robustness;
3. ML resource-vs-control decomposition;
4. same-mechanism re-certification after a diagnosed same-series failure;
5. retain existing underdog +kills fail-closed execution lock.

Do **not** respond by adding a generic extra safety margin to all markets.

---

## 6. Authorized correction boundary

On 2026-08-16 the user reviewed the full audit and explicitly instructed: **"Ok implement the correction now"** after focusing on the seven-loss streak.

This is a batch-audit authorization under the existing freeze policy and authorizes a new narrow analytical delta.

The resulting model version is **LoL v0.3.60**.

Historical positions/P&L remain unchanged. SK +7.5 vs FNC remains a ledger loss but is marked diagnostically as an execution-invalid TAKE that should have been PASS.