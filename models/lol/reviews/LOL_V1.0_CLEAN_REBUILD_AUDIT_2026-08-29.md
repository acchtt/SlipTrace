# LoL v1.0 Clean Rebuild Audit — 2026-08-29

**Status:** CANONICAL REBUILD RECORD  
**Purpose:** document what is retained, merged, and retired when moving from LoL v0.3.58 to **LoL v1.0 — Moneyline Core**.

## Rebuild principle

This is a clean major-generation rebuild, not an in-place simplification of v0.3.58. The old architecture remains immutable historical/audit material. Historical GitHub files, Airtable maps, snapshots, positions, screenshots, reviews, settlements and P/L are not deleted or relabeled.

## Historical evidence used

### EDG–NIP Game 1 — structural overreaction

At ~22:47 EDG had broad role economy and a 3–1 tower lead, but NIP still owned the 3–0 dragon/Soul-point schedule and the easier compulsory 5v5. The analytical error was treating improved structures/resource state as proof that the earlier objective-control failure had been repaired. The useful lesson is not another structure gate: **structures are context unless they change forward map control, and a prior thesis should reverse only after a genuine causal change.**

Reference: `models/lol/reviews/EDG_NIP_G1_ML_STRUCTURAL_CONTEXT_REVIEW_2026-08-28.md`.

### BRO–BFX Game 2 — derivative expression miss

At 8:26 BRO led 4–0 and ~+2.3k. The analysis correctly recognized BFX collapse sensitivity but failed to evaluate the favorite kill-handicap expression that the user later took and won. The important rebuild lesson is that a directional read and a final kill-margin forecast are different problems. v1.0 removes this derivative translation layer and asks only whether the current state creates enough win-probability edge for ML.

Airtable historical position: `LCK-2026-08-28-BRO-BFX-G2-P01-KH-BRO-11.5`.

### TH–SHFT Game 2 — map control was not kill-margin persistence

At ~12:00 TH led 2–1 kills, ~+1.5k gold and 2–0 dragons with no towers taken. TH -7.5 @1.788 was confirmed and lost; SHFT won 13–7. The analytical miss was extending legitimate early map control into a much stronger claim about final kill-margin expansion against SHFT's Vi/Taliyah/Shen re-entry and pick tools. v1.0 removes that extra projection problem.

Airtable historical position: `LEC-2026-08-28-TH-SHFT-G2-P01-KH-TH-M7.5`.

### NS–BFX — ML opportunity leakage

The series review found that Game 2 ML value was delayed until repricing, while Game 4 BFX ML @2.943 was recognized despite a 3–5 kill deficit because BFX had positive role-weighted economy and a functioning live mechanism. This supports **ML-first, role-weighted state, and fewer fixed confirmation-count gates.**

Reference: `models/lol/reviews/NS_BFX_2026-08-27_SERIES_CALIBRATION_REVIEW.md`.

---

# RETAINED

These concepts survive because they protect data quality, execution integrity, or directly improve win-probability estimation.

1. **GitHub authority + frozen session lock governance.**
2. **Airtable as canonical map/snapshot/position ledger.**
3. **Historical anti-hindsight accounting:** never rewrite old verdicts, positions, results or P/L.
4. **Synchronized live evidence** and fail-closed handling of stale/contradictory state.
5. **Executable-market requirement** and stale/greyed market rejection.
6. **Minimum accepted decimal odds 1.60** for the initial v1.0 sample.
7. **Position-blind reassessment.** Existing/open historical positions must not bias a fresh model estimate.
8. **No chasing, martingale, rescue, or stake escalation.**
9. **Actual exposure remains 0u.** Shadow tracking only unless explicitly changed by the user.
10. **User line-existence confirmation before Position creation.** TAKE CANDIDATE is not a Position.
11. **Draft as a prior, not a permanent veto.**
12. **Professional draft context:** exact roles, patch/format, player fit, lane/map access, Fearless/restricted-pool state where relevant, and a concrete professional win mechanism.
13. **Role-weighted live resources** rather than raw gold or kill score alone.
14. **Realized fight/contact execution.** What the compositions have actually demonstrated matters.
15. **Objective access/control and the next compulsory cycle.**
16. **Composition trajectory/scaling conditioned on whether the mechanism is functioning.**
17. **Towers/structures as context by default.** They matter only when they change forward control.
18. **Causal state-change discipline.** A prior PASS/HOLD or side preference should reverse only because the underlying mechanism changed, weakened, broke, or was replaced.

# MERGED

Useful ideas from the old stack are absorbed into simpler v1.0 concepts. Their legacy acronyms are not active gates.

1. **DIM + PDRL + PML -> DRAFT PRIOR.**
   - Keep exact-role interaction, lane/map access, pro execution fit, format/Fearless context, and archetype scarcity where material.
   - Output only `SIDE A / EVEN / SIDE B`, confidence, and the concrete win mechanism.

2. **Lead Decomposition + CFC + DPS + LRO -> LIVE STATE + MECHANISM CONTRADICTION.**
   - Resource distribution, fight execution, objective access, and trajectory replace the gate tree.
   - Contradiction is explicitly `INTACT / WEAKENING / BROKEN / REPLACED`.

3. **Structural Context + objective-schedule offset -> OBJECTIVE ACCESS/CONTROL.**
   - Structures have value only through their effect on first move, vision entry, side-lane pressure, cross-map threat or terminal access.

4. **HOLD expiry + opportunity decay -> FRESHNESS + PRICE DISCIPLINE.**
   - No fixed minute bands. A stale state/price pair is unusable. A live opportunity can disappear; the model should estimate probability on the freshest synchronized state instead of waiting for arbitrary counts.

5. **PRE_TAKE_CERT + gate signatures -> ML EXECUTION CHECK.**
   - Keep only authority, synchronization, executable line, minimum odds, position-blind estimate, fixed probability buffer, user confirmation and 0u exposure controls.

# RETIRED FROM ACTIVE ANALYTICAL AUTHORITY

The following remain in the repository and historical records but are not active v1.0 model gates.

## Entire betting families temporarily retired

- Kill Handicap
- Total Kills
- Duration

No TAKE CANDIDATE may be issued for those families under v1.0.

## Legacy derivative machinery retired

- KHMC, KH margin distribution/sign selection, WMS, RNE/NKB, FFD, UDKC, KPA, KMS, RLD, UCS, LAC and small-H asymmetry.
- FRP, FCR, DOVC and family-specific TK/Duration recurrence/stall/fast-close gates.
- KH/TK/Duration PRE_TAKE extensions and signatures.

## Legacy ML hard-count machinery retired

- mandatory 2SNAP as a universal count gate;
- contrary-draft 3SNAP/2CYCLE/LRO certification;
- named CFC/DPS/LRO gate tree;
- same-side PASS->TAKE repair as a separate named gate;
- fixed late-game +3pp/+5pp time-band buffers.

The underlying useful causal ideas are merged into the simpler mechanism-contradiction and fixed probability-buffer process.

## Pro-draft acronym tree retired as active output

PDRL/PML/DIM remain historical reference material. v1.0 may use their useful analytical content, but it does not require or emit their long certificates.

---

# Why Moneyline only

Moneyline asks the question the live evidence most directly supports: **who is more likely to win from this state?**

The recent errors show that translating a valid directional read into kill margin, total kills, or duration creates extra distributional assumptions. Those assumptions may be reintroduced in a future generation only after ML calibration is stable and only as separately validated models.

# Activation rule

This audit does not itself activate v1.0. Activation occurs only when:

1. the v1.0 rules file exists;
2. the v1.0 live procedure exists;
3. the v1.0 validation protocol exists;
4. session/bootstrap governance is internally compatible with v1.0;
5. `models/lol/CURRENT_MODEL.md` is updated to declare v1.0 active;
6. a fresh session authority lock freezes the completed stack.
