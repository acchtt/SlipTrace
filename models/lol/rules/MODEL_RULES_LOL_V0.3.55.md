# MODEL RULES — LEAGUE OF LEGENDS v0.3.55

**Status:** Active delta  
**Effective date:** 2026-08-13 UTC+7  
**Supersedes:** v0.3.54 only where stated

## Purpose

Correct a deterministic process-enforcement failure exposed by KT Challengers vs NS Challengers Game 1.

Confirmed shadow position:

- NS.EA +8.5 kills @1.943 — LOSS (-0.25u)

At entry (15:28), KT led 3-2 kills and 2-0 dragons while overall gold was approximately even. The model over-credited NS's Gnar / Anivia / Blitzcrank / Xin Zhao / Ezreal tools as independent handicap resilience and underweighted the relative execution simplicity of KT's Olaf / Vi / Cassiopeia / Ashe / Seraphine composition.

Reference review:
`models/lol/reviews/KT_NS_G1_DRAFT_EXECUTION_BURDEN_REVIEW_2026-08-13.md`

This update is a **process-enforcement correction**, not a one-map directional heuristic. v0.3.47 already established Draft Primacy and execution burden; v0.3.53 already required shared-failure testing. v0.3.55 makes those requirements explicit vetoes where the prior process failed to enforce them.

Official betting remains paused. Shadow calibration remains active.

---

## 1. Draft Execution Reliability (DER) — Mandatory

After draft lock and before every live ML / Kill Handicap / Total Kills TAKE, classify the matchup-relative **Draft Execution Reliability** for each side.

Use:

- `LOW BURDEN` — preferred sequence is repeatable, direct, and does not require several precise conditions to align;
- `MEDIUM BURDEN` — some conditional steps, but at least one reliable fallback or alternate forcing path exists;
- `HIGH BURDEN` — preferred fight requires several timing/terrain/angle/first-spell conditions to align, with weak fallback if the first sequence fails.

DER is not champion difficulty and is not a player-skill rating. It measures how many matchup-specific conditions must succeed for the composition to produce its preferred fight.

Mandatory questions:

1. Who can start the fight without flank/terrain dependence?
2. How many **independent** first-contact routes exist?
3. What happens if the first engage spell misses or is denied?
4. Which side can still deal damage after the first spell cycle?
5. Which side requires multiple champions to be correctly staged before contact?
6. Which side gets easier to execute in standard dragon/Baron setup?
7. Which side has a credible reset/re-engage path?

Do not call a draft `easy` or `hard` from champion identity alone. The classification must be matchup-functional.

---

## 2. Shared-Failure Cluster Count — Enforced

Retain v0.3.53 Mechanism Independence, but make the counting rule explicit.

When evaluating resilience, forcing, peel or comeback tools, count **shared-failure clusters**, not champion abilities.

Examples of one shared cluster:

- several tools all require winning fog/angle first;
- several defensive spells all require the carry to preserve spacing before the engage lands;
- Gnar rage + Anivia terrain + Blitz hook all depend on being set first at the objective;
- multiple follow-up spells that only function if one initial engage succeeds.

If three nominal tools fail under the same tempo/terrain/first-spell condition, they are not three independent answers.

Before a TAKE, record internally:

- number of meaningful forcing clusters for Team A;
- number for Team B;
- number of meaningful survival/anti-cascade clusters for each side;
- whether the key mechanisms are `INDEPENDENT`, `PARTIALLY COUPLED`, or `COUPLED`.

---

## 3. Positive-Handicap Draft-Burden Veto

For an underdog `+kills` TAKE against a favorite, default **PASS/HOLD** when all are true:

1. favorite has a material edge in reliable first contact or direct target access;
2. favorite has at least two meaningfully independent forcing layers or one highly reliable forcing layer plus a strong continuation/re-engage path;
3. underdog margin-saving mechanisms are `HIGH BURDEN` and/or materially `COUPLED`;
4. at least two meaningful future pressure/fight windows remain, especially scheduled dragon/Baron/base-defense windows;
5. no repeated live evidence shows the underdog's exact anti-cascade mechanisms functioning against the favorite's actual engage routes.

This is a **veto on the underdog resilience thesis**, not an automatic favorite -kills signal.

The favorite negative handicap must still independently clear:

- signed-margin distribution;
- NKB;
- RFI;
- KCV;
- Structure Substitution;
- lower-bound probability surcharge.

Do not mirror a blocked +kills bet into a -kills TAKE without separate qualification.

---

## 4. Scoreboard Parity Is Not Draft-Mechanism Proof

Two synchronized snapshots satisfy the temporal live gate, but they do **not** automatically prove that a high-burden draft is resilient.

Near-even:

- team gold;
- kill score;
- tower count;
- role-gold mixture

cannot by themselves override a material DER/shared-failure asymmetry.

To downgrade a draft-burden veto, require **mechanism-valid live proof**, for example:

- the underdog repeatedly disengages the favorite's primary engage;
- the underdog repeatedly returns kills after first contact;
- objective setups repeatedly resolve without the favorite obtaining target access;
- waveclear/base defense remains functional under actual pressure;
- the favorite's nominal forcing layer repeatedly fails across more than one meaningful window.

Scoreboard persistence without mechanism proof => keep the draft uncertainty penalty / veto active.

---

## 5. Objective-Schedule x Execution-Burden Interaction

Dragon and Baron alignment must be combined with DER.

When one side has the easier objective-fight draft and also controls the objective schedule — examples:

- 2-0 dragons approaching soul-point windows;
- 3-0 dragons approaching soul;
- Baron setup with vision/terrain control;
- inhibitor/base-defense windows —

the harder-execution side receives a further downgrade because future fights are increasingly likely to occur in **scheduled, prepared terrain** rather than random skirmishes.

This interaction affects markets differently:

- **ML:** raises clean conversion probability for the lower-burden side;
- **Kill Handicap:** can widen the favorite multi-kill/cascade tail when contact is forced and Structure Substitution is not dominant;
- **Total Kills:** does not automatically imply Over; apply CRR/RKS/KPW because superior control may also force concessions and delete windows;
- **Duration:** still requires observed live acceleration/stall under retained restrictions.

---

## 6. Draft Correction Trigger

A user correction that materially changes champion identity, role assignment, or draft interpretation triggers an immediate **full position-blind Draft Function Matrix + DER + shared-failure rerun**.

Do not respond to a material draft correction with a cosmetic `slight upgrade/downgrade` unless the rerun genuinely supports only a slight change.

For any open position, after the rerun set thesis:

- `ACTIVE`;
- `DEGRADED`;
- `INVALIDATED`;
- `CONFIRMED`.

If the corrected draft would have failed the current entry gate, mark the thesis `DEGRADED` or `INVALIDATED` immediately and record the process error for review.

---

## 7. Kill-Handicap Resilience Independence Test (RIT)

Before every underdog +kills TAKE, explicitly answer:

1. What exact mechanisms save kill margin if the underdog loses the map?
2. Are those mechanisms independent or coupled?
3. Do they function under Baron/dragon/base pressure, not just neutral-lane states?
4. Can the underdog prevent cleanup after losing first contact?
5. Can the underdog generate return kills without first winning the setup condition?
6. Has at least one of those mechanisms been observed functioning live against the actual opponent draft?

If the answer set is mostly theoretical/conditional, lower `P(cover | map loss)` materially.

Generic labels such as `waveclear`, `zone control`, `pick`, `kite`, or `scaling` are insufficient unless mapped to the opponent's exact forcing route.

---

## 8. KT.C vs NS.EA G1 Reference Correction

Draft:

KT.C: Olaf / Vi / Cassiopeia / Ashe / Seraphine  
NS.EA: Gnar / Xin Zhao / Anivia / Ezreal / Blitzcrank

At 15:28:

- KT 3-2 kills;
- NS approximately +108g;
- towers 0-0;
- KT 2-0 dragons;
- NS +8.5 @1.943;
- KT -8.5 @1.816.

### Old read

- near-even economy;
- NS Gnar/Anivia/Blitz viewed as enough pick/disengage/stall to bound margin;
- TAKE NS +8.5.

### Corrected read

KT:
- lower execution burden;
- highly reliable Ashe/Vi first contact;
- independent Olaf continuation;
- Cassiopeia objective-space punishment;
- Seraphine follow-up/re-engage value;
- 2-0 dragons scheduling future prepared fights.

NS:
- Gnar requires rage timing;
- Anivia requires prepared space;
- Blitz is pick-first and not reliable broad peel;
- Xin disruption is close-range/conditional;
- several defensive answers depend on the same setup/spacing state.

Shared-failure classification: materially coupled/high-burden relative to KT.

Correct process verdict at 15:28:

**PASS/HOLD — NS +8.5 kills @1.943.**

Do not infer that KT -8.5 automatically qualifies; it still requires its own signed-margin edge.

---

## 9. Mandatory Internals Update

Before any live ML / KH / TK TAKE, add to the retained checklist:

1. Draft Function Matrix completed;
2. DER for both teams;
3. forcing-cluster independence count;
4. survival/anti-cascade cluster independence count;
5. objective-schedule x DER interaction;
6. for +kills: RIT result;
7. whether scoreboard evidence is mechanism-valid or merely state persistence;
8. whether any Draft-Burden Veto is active.

Missing DER/shared-failure/RIT on an underdog +kills decision => **PASS/HOLD**.

---

## 10. Retained Controls

All non-conflicting v0.3.54 and earlier controls remain active, including:

- Role-Weighted Economy / TEI;
- two-snapshot live eligibility;
- MKT + TEAM anchoring;
- anti-favorite guard;
- Draft Primacy 14-function matrix;
- TTA / EBG / lead quality;
- side-neutral signed kill-margin distribution;
- NKB / RFI / KCV / Structure Substitution;
- Handicap Buffer Retention;
- OKP / FCI / CRR / SRR / BF / CL / RKS / KPW;
- position-blind reassessment;
- stale-line gate;
- same-game correlation decomposition;
- Duration restrictions;
- no rescue/martingale/loss chasing.

Where draft execution reliability or shared-failure interpretation conflicts with older generic resilience language, **v0.3.55 controls**.

---

## 11. Operating State

- Active model: **LoL v0.3.55**
- Official betting: **PAUSED**
- Shadow mode: ACTIVE
- Default shadow stake: 0.25u
- Actual exposure: 0u
- Minimum odds: 1.60
- Pregame/immediate post-draft ML/KH/Total Kills TAKE: DISABLED
- Live ML/KH/TK: retained two-snapshot gate plus v0.3.55 draft-mechanism gates
- Duration restrictions: unchanged
- Same-game multiple shadow positions: enabled only when each independently qualifies

Shadow TAKEs that are visibly executable and qualify are auto-recorded after the user-facing verdict; no placement confirmation is required in shadow mode. Official wager confirmation rules apply only if official betting is explicitly restored.

Where this delta conflicts with v0.3.54 or earlier interpretation, **v0.3.55 controls**.
