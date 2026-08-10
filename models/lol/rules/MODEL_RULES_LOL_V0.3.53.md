# MODEL RULES — LEAGUE OF LEGENDS v0.3.53

**Status:** Active delta  
**Effective date:** 2026-08-11 UTC+7  
**Supersedes:** v0.3.52 only where stated

## Purpose

Correct the aggregate anti-favorite, line-selection, mechanism-independence and Total Kills conversion failures identified through `POSTCB-SHADOW-25-P01`.

Reference review:
`models/lol/reviews/AGGREGATE_ANTI_FAVORITE_FADE_BIAS_REVIEW_2026-08-11.md`

Post-circuit-breaker sample at promotion:

- settled positions: 26
- record: **10-16**
- net: **-1.5255u**
- recent five positions: **0-5, -1.25u**
- exact-price fade benchmark on those five: approximately **+1.16775u**

The core correction is:

> **Draft mechanisms are not allowed to erase persistent team-strength and market information. Champion-level tools must be tested for shared failure, buffered handicap protection must not be casually surrendered, and contact availability must be separated from kill production.**

Official betting remains paused. v0.3.53 operates in shadow calibration mode only.

---

## 1. Aggregate Bias Circuit Breaker

A model-bias circuit breaker is ACTIVE because the recent aggregate sample shows materially negative calibration and a profitable opposite-side benchmark over the latest five confirmed positions.

While active:

- official betting remains paused;
- actual exposure remains 0u;
- default shadow stake remains 0.25u;
- minimum odds remain 1.60;
- no stake escalation, rescue, martingale or loss chasing;
- same-game multiple shadow bets remain allowed only after the live eligibility gate in Section 2;
- correlated shadow bets must be grouped and may not be treated as independent evidence.

The circuit breaker may be removed only after a fresh review based on a materially larger sample, not one winning map.

---

## 2. Live Eligibility Gate — No Immediate Post-Draft TAKE

Effective v0.3.53, **Moneyline, Kill Handicap and Total Kills are analysis-only pregame and immediately post-draft.**

A TAKE in those markets requires:

1. at least **two synchronized live snapshots**;
2. snapshots separated by approximately **90 seconds or more** when feasible;
3. exact executable odds at the decision point;
4. observed evidence that the relevant draft mechanism is functioning or failing in practice;
5. current structures/objectives/gold/kills sufficient to distinguish map conversion from scoreboard noise.

This rule overrides earlier post-draft TAKE permissions.

Duration restrictions from prior versions remain stricter and continue to control.

---

## 3. Market + Team-Strength Anchor

Every live probability estimate starts from two persistent anchors:

### `MKT` — market anchor
Use the current two-sided market when available, de-vigged conceptually rather than reading one raw price in isolation.

### `TEAM` — persistent team-strength / execution prior
Includes:

- player/lane strength;
- objective setup quality;
- range management;
- vision discipline;
- engage timing;
- conversion quality;
- ability to avoid low-value fights;
- same-series demonstrated execution.

Fearless Draft changes champion mechanisms but **does not reset TEAM to neutral**.

A fresh draft may modify the prior, but it may not erase persistent team-level evidence merely because the underdog has several attractive theoretical tools.

### Market-deviation discipline
If the model's live estimate requires a large departure from the current market, the burden of proof rises.

A large disagreement must be supported by repeated observed live evidence, not by champion-kit narrative alone.

If the edge exists only because the model discounts the favorite's team/market prior without observed proof, verdict defaults HOLD/PASS.

---

## 4. Anti-Favorite Bias Guard

Before any underdog ML or +kills TAKE against a clear market/team-strength favorite, explicitly answer:

1. What observed mechanism is preventing the favorite from converting its baseline skill edge?
2. Is that mechanism currently functioning across more than one snapshot?
3. Does it survive if the underdog loses tempo, vision or first engage?
4. Is the underdog's cover/win branch genuinely independent of one narrow execution sequence?
5. Has the favorite's collapse tail actually fallen, or are we merely reacting to temporary underdog success?

If the answers are weak or theoretical, do not TAKE the underdog simply because the price/handicap looks generous.

This guard is directional only in response to the detected calibration bias; it does **not** create an automatic favorite bet.

---

## 5. Mechanism Independence / Shared-Failure Penalty

Every major draft/live survival, comeback or forcing mechanism must be classified:

- `INDEPENDENT`
- `PARTIALLY COUPLED`
- `COUPLED`

Mechanisms are COUPLED when they depend materially on the same:

- tempo state;
- engage angle;
- vision/fog access;
- jungle/support access;
- first-spell success;
- resource threshold;
- target access path;
- objective/choke entry.

Several champion buttons inside one coupled cluster do **not** count as several independent answers.

### Shared-failure penalty
When a +kills or comeback thesis relies mostly on PARTIALLY COUPLED/COUPLED mechanisms:

- widen the favorite blowout tail;
- reduce the underdog's lower-bound cover probability;
- downgrade TTA/resilience confidence;
- raise PASS/HOLD frequency.

This rule directly addresses the SK-VIT G2 and NAVI-G2 failures.

---

## 6. Handicap Buffer Retention Rule

When the underdog +kills thesis is fundamentally **margin survival rather than map superiority**, handicap buffer has independent value.

Do not replace a previously attractive buffered +H line with a much narrower live line merely because the underdog temporarily leads.

A compressed +H line may be taken only if repeated live evidence shows that:

- the favorite's wide-margin tail has materially shrunk;
- the underdog mechanisms are functioning under pressure, not only while ahead;
- the favorite's TEAM/range/late-control edge has been structurally impaired;
- the narrower line still clears the live lower-bound buffer on its own.

### Buffer-loss veto
If most of the original protection has disappeared and the model's thesis is still "underdog can lose but keep it close," default PASS rather than chase the compressed handicap.

NAVI-G2 G1 is the reference failure: +6.5 would have covered while the later +1.5 line lost.

---

## 7. Structure Substitution Becomes Two-Sided

Structure Substitution is no longer assumed to compress favorite kill margins.

Classify the current structural regime:

- `MARGIN-COMPRESSING` — favorite can take towers/objectives safely without needing extra kills;
- `MARGIN-EXPANDING` — structural pressure forces repeated low-quality defense/base fights and can increase kill margin;
- `MIXED/NEUTRAL` — both branches remain meaningful.

A strong team/range mismatch may produce both structure dominance and a widening kill margin.

Therefore, for +kills positions, structure acceleration is protective only when the map can close without repeated forced defense.

---

## 8. Total Kills — Contact Availability Is Not Kill Production

v0.3.51 OKP/FCI/CRR/SRR/BF remains active, but v0.3.53 adds two mandatory layers:

### `RKS` — Return-Kill Suppression
Classify the weaker side's ability to return kills after contact:

- `LOW SUPPRESSION` — loser reliably trades kills back;
- `MEDIUM SUPPRESSION`;
- `HIGH SUPPRESSION` — stronger side can repeatedly win contact cleanly or near-cleanly.

### `KPW` — Kills Per Realized Window
For each meaningful contact window, estimate not only whether contact occurs, but the expected kill count conditional on contact.

High BF/SRR with HIGH RKS can produce repeated **2-0 / 3-0** sequences rather than 3-2 / 4-3 exchanges.

### Window deletion by structure acceleration
After a clean fight, test whether the winner can convert directly into:

- tower chain;
- Baron;
- inhibitor;
- base access;
- end threat.

If yes, reduce the number of remaining future fight windows.

Therefore:

> **High BF/SRR raises contact inventory, not automatically final kill total.**

G2-NAVI G2 is the reference failure: many engage tools existed, but G2 won 15-7 while simultaneously creating an 11-2 tower, Baron and inhibitor stomp.

---

## 9. Fade Benchmark Audit

For every future confirmed shadow TAKE, when the opposite-side executable price is visible at entry, record it in the position notes as a **fade benchmark**.

The benchmark is counterfactual only and does not create a second official shadow position.

Track over rolling samples:

- model-side result / ROI;
- opposite-side fade result / ROI;
- market family;
- favorite/underdog direction;
- pregame/post-draft/live phase;
- whether the model disagreed materially with MKT/TEAM.

If the fade benchmark remains materially positive while model ROI remains negative over a larger sample, the next review must test whether a systematic sign inversion or selection filter is warranted.

Do **not** blindly invert the model yet.

---

## 10. Same-Game Multiple Shadow Bets

User-requested same-game shadow testing remains enabled.

After the Section 2 live eligibility gate:

- multiple ML/KH/Total Kills/Duration positions may be taken on the same map when each independently qualifies;
- correlation must be explicitly tagged;
- correlated outcomes remain separate P/L entries but one evidence cluster for calibration;
- duplicate line ladders on the same thesis should be avoided unless explicitly marked as a calibration experiment;
- no position may be added merely to increase sample count.

---

## 11. Change-Control Rule

A single settled map may no longer promote a new model version unless it exposes a deterministic correctness bug independent of outcome.

Ordinary performance-driven model promotion requires either:

- at least **5 settled positions across at least 3 maps** showing the same failure mechanism; or
- a larger aggregate review demonstrating statistically/materially persistent bias.

Single-map findings may be written as review notes or probationary hypotheses but cannot immediately become strong active confidence rules.

v0.3.53 qualifies because it is based on the 26-position post-CB ledger plus a five-position consecutive opposite-side benchmark cluster.

---

## 12. Retained v0.3.52 Controls

The following remain active unless directly superseded:

- Terminal Threat Answerability (TTA);
- Execution Burden Gradient (EBG);
- terminal vs non-terminal lead quality;
- early-live ML hard veto;
- live ML lower-bound buffers;
- Comeback Conversion Reserve;
- Draft Primacy functional matrix;
- signed Kill Handicap distribution, NKB, RFI and KCV;
- position-blind reassessment;
- user scoreboard corrections and settlement authority;
- item-verification suspension;
- no martingale/rescue/loss chasing.

Under v0.3.53, TTA and draft mechanisms must also pass the TEAM/MKT anchor and mechanism-independence tests.

---

## 13. Mandatory Internals Before Any TAKE

### All ML / KH / Total Kills

1. exact clock and executable odds;
2. at least two synchronized live snapshots;
3. current kills / gold / towers / dragons / Grubs-Herald / Baron / inhibitors;
4. MKT anchor;
5. TEAM prior;
6. draft mechanism state observed live;
7. mechanism-independence classification;
8. current structural regime;
9. lower-bound edge after uncertainty;
10. opposite-side fade benchmark price when visible.

### Kill Handicap additionally

- signed kill-margin distribution;
- NKB;
- RFI;
- KCV;
- Structure Substitution class: MARGIN-COMPRESSING / MARGIN-EXPANDING / MIXED;
- Buffer Retention Rule status.

### Total Kills additionally

- OKP;
- FCI;
- CRR;
- SRR;
- BF;
- CL;
- RKS;
- KPW;
- structure-driven future-window deletion.

Missing a decision-critical layer => HOLD/PASS.

---

## 14. Next-Session Operating Protocol

1. Pregame: analysis only.
2. Post-draft: analysis only; record TEAM/MKT/draft/TTA/EBG/mechanism coupling.
3. Snapshot 1: approximately 5-7 minutes when available.
4. Snapshot 2: approximately 8-10 minutes or >=90 seconds later.
5. Only then scan ML, Kill Handicap and Total Kills for TAKE eligibility.
6. Duration follows its existing later clock restrictions.
7. Same-game multiple shadow bets are allowed after eligibility.
8. Record opposite-price fade benchmark on every confirmed TAKE when visible.
9. Reassess all open positions position-blind after material state changes.

---

## 15. Operating State

- Active model: **LoL v0.3.53**
- Official betting: **PAUSED**
- Official probation: unchanged at 13/20, 7-6, -0.16425u
- Shadow mode: ACTIVE
- Default shadow stake: 0.25u
- Actual exposure: 0u
- Minimum odds: 1.60
- Same-game multiple shadow positions: ENABLED after live eligibility
- Pregame/immediate post-draft ML/KH/Total Kills TAKE: DISABLED
- Duration restrictions: unchanged

Where this delta conflicts with v0.3.52 or earlier interpretation, **v0.3.53 controls**.
