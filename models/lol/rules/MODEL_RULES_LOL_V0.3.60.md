# MODEL RULES — LEAGUE OF LEGENDS v0.3.60

**Status:** Active delta  
**Effective date:** 2026-08-16 UTC+7  
**Supersedes:** v0.3.59 only where stated

## Purpose

Implement the user-authorized batch correction from the seven-loss v0.3.59 streak review.

Reference review:
`models/lol/reviews/SEVEN_LOSS_STREAK_REGIME_PERSISTENCE_ML_CONTROL_REVIEW_2026-08-16.md`

This is a **narrow correction**, not a global tightening of TAKE thresholds.

The six legitimate model losses in the seven-loss streak concentrated into two analytical problems:

1. current game regime was extrapolated too confidently into future objective cycles;
2. modest live resource leads were priced too strongly relative to opponent compulsory-fight control.

The seventh loss, SK +7.5 vs FNC, was an execution-invalid TAKE already covered by the retained fail-closed fallback procedure.

All non-conflicting v0.3.59 and earlier rules remain active.

---

# 1. Total Kills Under — Forward Regime Persistence (FRP)

A Total Kills Under may not qualify merely because the current/elapsed game has been quiet.

Retain all existing OKP / FCI / CRR / SRR / BF / CL / RKS / KPW controls. v0.3.60 adds a mandatory **Forward Regime Persistence (FRP)** test.

Before every Total Kills Under TAKE, classify:

- `FRP = PASS`
- `FRP = FAIL`
- `FRP = UNCERTAIN`

Only `FRP = PASS` is eligible for TAKE.

## 1.1 Next Compulsory Contact Cycle (NCCC)

Explicitly identify the next meaningful compulsory-contact schedule, including as applicable:

1. next dragon and Soul/Elder proximity;
2. Baron/Herald availability or imminent spawn;
3. tower/base-defense windows;
4. objective vision entry and contest incentives;
5. side-lane pressure that forces grouped response;
6. current role-weighted economy / TEI and death-risk asymmetry;
7. first-contact reliability;
8. re-engage availability;
9. ability of either side to safely concede, cross-map or trade instead of contesting;
10. whether a single fight is likely to produce a second immediate fight through chase, respawn timing, objective turn or base defense.

Classify the next cycle's contact pressure qualitatively as `LOW / MEDIUM / HIGH`.

No single objective automatically makes contact pressure HIGH. The classification is matchup-relative.

## 1.2 Quiet-interval evidence discount

A quiet interval **between major objective windows** has reduced evidentiary value.

It may support observed low CRR, but it cannot by itself establish FRP.

The model must distinguish:

- **passive quiet:** nothing compelled either team to contact;
- **suppressed compulsory contact:** a real objective/fight window occurred and one or both teams successfully avoided or contained kill production.

Suppressed compulsory contact is materially stronger Under evidence than passive quiet.

Do not reason:

- “no kills for two minutes, therefore Under regime persists”;
- “only X kills through Y minutes, therefore future recurrence remains low”;

without separately proving the next compulsory-contact cycle is also suppressible.

## 1.3 Mandatory forward question

Before every Total Kills Under TAKE, explicitly answer:

**“Why should the next compulsory objective/contact cycle be at least as kill-suppressive as the interval already observed?”**

Acceptable FRP support can include, but is not limited to:

- a credible safe-concession route for the trailing side;
- repeatable disengage/waveclear that has already denied compulsory contact;
- objective ownership/state that materially reduces contest incentive;
- Structure Substitution that removes future fights rather than merely replacing past fights;
- low-access drafts where first contact remains difficult even at objectives;
- demonstrated low lethality after actual contact, not merely absence of contact;
- a lead so structurally advanced that the game can close without repeated kill windows, provided Duration/terminal interactions do not create a contradictory high-contact branch.

If the next contact cycle is HIGH pressure and no independent future-suppression mechanism is positively identified, `FRP = FAIL/UNCERTAIN` and the Under is PASS/HOLD.

## 1.4 Regime-break reset rule

After a material recurrence burst, prior low-CRR evidence is degraded.

A later quiet interval does **not** automatically restore FRP.

FRP can be restored only by new mechanism-relevant evidence, such as:

- successful suppression of a compulsory objective/contact window;
- a material objective-schedule change;
- a material structural-control change;
- a material change in safe-concession/cross-map availability;
- a genuine reduction in access/re-engage routes.

This is not an arbitrary extra-snapshot requirement. It is a requirement that the failed mechanism itself be re-certified.

---

# 2. Duration Under — Fast-Close Robustness (FCR)

Retain all v0.3.45 timing, acceleration, persistence, dead-zone and probability-buffer requirements and all v0.3.59 LCH/ABSENT-vs-FAILED conversion rules.

v0.3.60 adds mandatory **Fast-Close Robustness (FCR)** for Duration Under.

Classify:

- `FCR = ROBUST`
- `FCR = FRAGILE`
- `FCR = UNCERTAIN`

Only `FCR = ROBUST` is eligible for a normal Duration Under TAKE, except where the retained terminal-state exception independently applies.

## 2.1 Shortest path is not enough

The shortest realistic route:

`next fight/objective -> structures -> base -> Nexus`

remains mandatory, but it is not sufficient.

The model must also test whether the Under still has adequate clock room after **one plausible ordinary disruption**, such as:

- partial instead of full Baron conversion;
- one defender waveclear/reset cycle;
- a failed or traded push;
- a delayed second structure;
- one objective trade;
- a won fight that does not immediately yield base access;
- a reset forced by low health or poor wave state.

## 2.2 One-Disruption Stress Test

Before a Duration Under TAKE, ask:

**“If the fastest close route suffers one normal disruption, does the Under thesis still remain materially viable?”**

If the answer is no, `FCR = FRAGILE`.

A line that only clears when every conversion step succeeds cleanly is not a robust Under thesis.

This does not require inventing an extra fixed number of minutes. Use the actual market line, current clock, observed conversion speed and realistic reset/rotation costs.

## 2.3 Acceleration quality

Observed acceleration must be separated into:

- **route availability** — a fast route exists;
- **route persistence** — the game state repeatedly supports that route;
- **route robustness** — the route survives a normal disruption.

Duration Under requires all retained acceleration gates plus robust route quality. Do not equate “can finish before the line” with “is sufficiently likely to finish before the line.”

---

# 3. Live Moneyline — Resource Lead vs Control Lead

Live ML remains position-blind and requires the retained two-snapshot gate, pricing, MKT + TEAM, Draft Primacy, role-weighted economy / TEI, terminal-threat and all other active controls.

v0.3.60 adds mandatory **Lead Decomposition** and **Compulsory Fight Control (CFC)**.

## 3.1 Lead Decomposition

Before every live ML TAKE, separate the candidate side's current advantage into:

1. `RL` — Resource Lead: gold, CS, levels, role-weighted economy;
2. `SL` — Structural Lead: towers, inhibitors, wave depth, vision depth, base access;
3. `OSC` — Objective-Schedule Control: dragon/Soul/Elder/Baron timing and who benefits from the next forced windows;
4. `CFC` — Compulsory Fight Control: who has easier first contact, re-engage, backline access, disengage/reset and objective turn from approximately neutral setup.

A positive RL is **not** automatically a positive control lead.

## 3.2 Neutral-Setup Fight Stress Test

Before a live ML TAKE, explicitly ask:

**“If the next two major compulsory fights begin from approximately neutral setup, which side has the easier way to dictate first contact, survive the first exchange, re-engage, and reach the opposing carries?”**

Evaluate at minimum:

- initiation reliability;
- target access;
- re-engage;
- disengage/reset;
- objective turn speed/safety;
- wave state and arrival angles;
- protected DPS continuation;
- side-lane pressure and teleport/global access;
- terminal threat if one fight is lost.

## 3.3 Resource-only lead discount

When the candidate side has a resource/objective lead but **little or no structural separation**, and the opponent has materially easier neutral-setup first-contact/re-engage, the resource lead must be discounted in ML pricing.

The candidate ML cannot qualify if the TAKE justification relies primarily on:

- a modest gold/CS lead;
- one early dragon;
- a small current kill lead;
- lane economy advantages;

while failing to answer the opponent's easier compulsory-fight architecture.

To clear the ML edge gate in that state, the candidate side must show independent control evidence such as:

- meaningful structural conversion;
- objective schedule that forces fights on favorable terms for the candidate;
- reliable disengage/anti-engage that neutralizes opponent first contact;
- demonstrated ability to control neutral-objective setup rather than merely arrive richer;
- a material market misprice that remains after the compulsory-fight downside branch is explicitly included.

If `RL positive` but `CFC materially favors opponent` and independent control evidence is absent, verdict is PASS/HOLD.

This is a named analytical gate, not a discretionary extra safety margin.

---

# 4. Same-Mechanism Re-certification (SMR)

A previous loss does not create an automatic veto and must not cause generic conservatism.

However, when a settled loss has been **mechanistically diagnosed**, a later TAKE in the same series that relies on materially the same thesis must pass **Same-Mechanism Re-certification (SMR)**.

Before repeating the thesis, explicitly state:

1. the prior diagnosed failure mechanism;
2. whether the new draft materially changes that mechanism;
3. whether the new live state directly neutralizes that mechanism;
4. whether the market family is relying on the same structural assumption;
5. what new evidence makes the new case independent enough to qualify.

SMR passes only when at least one material input changes the failed mechanism, for example:

- different draft architecture;
- different first-contact/re-engage relationship;
- materially stronger structural control;
- materially different objective schedule;
- demonstrated answer to the prior forcing route;
- materially different price after the failed branch is included.

A repeated +1k gold lead, repeated low early kill count, or repeated 0-0 tower state is not by itself re-certification.

If the prior failure mechanism remains materially active and the new TAKE depends on the same assumption, `SMR = FAIL` and the market is PASS/HOLD.

SMR is strongest for consecutive maps in the same series because opponent style, execution and draft priorities are directly relevant. It may be used more broadly only when the mechanism is genuinely transferable; do not turn it into result-chasing.

---

# 5. SK +7.5 vs FNC execution-invalid reference remains unchanged

The seven-loss review includes SK +7.5 @2.041 vs FNC G1, but v0.3.60 does **not** add a new underdog +kills rule for that loss.

The retained mandatory draft-lock procedure already controls:

- FER;
- PDC;
- PST;
- ARI;
- False-Stable Guard;
- FF = STABLE;
- hard Draft-Collapse Veto.

Ordinary live evidence cannot upgrade an uncertified fallback.

Correct historical verdict remains:

`PASS — SK +7.5 kills @2.041 — 0u.`

Historical ledger P/L remains unchanged.

---

# 6. No blanket anti-Under / anti-ML correction

v0.3.60 must not be executed as “be more conservative after losses.”

The correction is:

- conservative about **unproven future regime persistence**;
- conservative about **resource leads that do not translate into control leads**;
- conservative about **repeating a diagnosed failed mechanism without re-certification**;
- not conservative about positions that actually pass the written gates.

When FRP/FCR/CFC/SMR and all retained market gates pass at executable qualifying odds, default execution posture remains TAKE.

Kill Handicap rules are unchanged except where SMR is genuinely relevant. Favorite -kills FFD/RNE remains fully active and must not be over-vetoed because the recent streak contained no favorite -kills loss.

---

# 7. Reference corrections

## 7.1 BFX vs DNS G2 — Under 34.5

Past lull was real but FRP should have failed/been uncertain because upcoming Baron/dragon forcing remained capable of reactivating high CRR.

## 7.2 SK vs FNC G2 — Under 21.5

Five kills through 18:11 did not prove future suppression. The next compulsory objective cycle retained enough contact density that FRP was not positively established.

## 7.3 G2 vs SHFT G1 — Under 26.5

Two kills at 9:55 and three kills at 16:45 were passive-quiet evidence. Later objective cycles produced 35 final kills. Under v0.3.60, passive quiet alone cannot certify FRP.

## 7.4 BLG vs WE G1 — Under 28 minutes

The shortest fast-close route was credible, but the line lacked enough robustness to one normal disruption. FCR should have been FRAGILE/UNCERTAIN.

## 7.5 DNS vs T1A G2/G3 — DNS ML

DNS held real resource/objective leads, but little structural separation. T1A retained materially easier compulsory-fight initiation/re-entry. RL was mistaken for CFC/overall control. G3 additionally should have faced SMR after the G2 failure mechanism was diagnosed.

---

# 8. Audit segmentation

Historical selections and P/L remain unchanged.

- v0.3.57 remains the pre-v0.3.58 sample.
- v0.3.58 remains the favorite-handicap-corrected / pre-v0.3.59 Duration sample.
- v0.3.59 remains the post-Duration-correction / pre-v0.3.60 batch-review sample.
- All new selections after this authorization are recorded under **v0.3.60**.

Do not retroactively regrade historical P/L from diagnostic reference corrections.

---

# 9. Retained controls

All non-conflicting v0.3.59 and earlier controls remain active, including:

- v0.3.59 ABSENT vs FAILED conversion and LCH;
- v0.3.58 favorite -kills FFD / RNE;
- v0.3.57 fallback-floor certification and False-Stable Guard;
- v0.3.56 hard underdog +kills Draft-Collapse Veto;
- DER and shared-failure clusters;
- Draft Correction Trigger;
- Draft Primacy and position-blind reassessment;
- MKT + TEAM anchoring;
- Role-Weighted Economy / TEI;
- TTA / EBG / lead quality;
- two-snapshot live eligibility for ML/KH/TK;
- exact signed kill-margin arithmetic;
- NKB / RFI / KCV / Structure Substitution;
- Handicap Buffer Retention;
- OKP / FCI / CRR / SRR / BF / CL / RKS / KPW;
- stale-line / greyed-market non-executability;
- same-game correlation decomposition;
- one TAKE maximum per market family per map under the active no-duplicate policy;
- all v0.3.45 Duration timing, observed stall/acceleration, persistence, dead-zone, probability-buffer and regime-change restrictions;
- no rescue/martingale/loss chasing.

Where this delta conflicts with earlier TK Under, Duration Under, or live-ML interpretation, **v0.3.60 controls**.