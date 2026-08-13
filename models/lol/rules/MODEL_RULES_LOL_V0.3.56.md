# MODEL RULES — LEAGUE OF LEGENDS v0.3.56

**Status:** Active delta  
**Effective date:** 2026-08-13 UTC+7  
**Supersedes:** v0.3.55 only where stated

## Purpose

Make draft-collapse risk a **strict, non-overridable underdog +kills gate** after NIP vs WBG Game 1 exposed a second failure of the same class.

Reference review:
`models/lol/reviews/NIP_WBG_G1_DRAFT_COLLAPSE_RISK_REVIEW_2026-08-13.md`

Settled reference position:
- WBG +8.5 kills @1.961
- shadow 0.25u
- final NIP 22-10 WBG
- result LOSS (-0.25u)

Official betting remains paused. Shadow calibration remains active.

---

## 1. Draft Collapse Risk (DCR) — Mandatory

After draft lock, classify each composition's matchup-relative **Draft Collapse Risk**:

- `LOW`
- `MEDIUM`
- `HIGH`

DCR answers:

> If this composition loses first contact or loses map control, how likely is one failed sequence to create clustered deaths, repeated forced defenses, or a rapidly widening kill margin?

Mandatory inputs:

1. frontline durability and ability to absorb first contact;
2. reliable disengage after a failed engage;
3. protected sustained damage source;
4. ability to contest objectives without face-checking or perfect setup;
5. ability to defend waves/base while behind;
6. whether failed engage exposes one champion or several simultaneously;
7. whether the composition can reset and re-form after losing the first spell cycle;
8. whether poke, dive, pick and front-to-back requirements demand incompatible spacing;
9. whether the opponent has repeatable forcing into the same shared-failure cluster;
10. how scheduled dragon/Baron/base windows change the failure tail.

DCR is separate from map-win probability. A team can retain meaningful win equity while still having HIGH blowout / kill-margin collapse risk.

---

## 2. Fallback Floor (FF) — Mandatory

Classify each composition's **Fallback Floor**:

- `STABLE` — still has a repeatable lower-variance plan when first choice fails or when behind;
- `FRAGILE` — fallback exists but depends on narrow spacing/setup/tempo conditions;
- `ABSENT` — no credible repeatable fallback once the preferred engage/poke/access sequence is denied.

Fallback examples include:

- durable front-to-back with protected DPS;
- reliable disengage/reset;
- waveclear/base defense that functions under pressure;
- side-lane/global trade that does not require winning the same contested terrain;
- safe long-range damage with credible peel.

Generic champion labels do not count; the fallback must survive opponent-route testing.

---

## 3. HARD DRAFT-COLLAPSE VETO — NO EXCEPTIONS

For **underdog +kills**, activate a HARD VETO when all are true at draft lock / first complete post-draft assessment:

1. the side is the underdog by the pregame/draft `MKT + TEAM` anchor;
2. `DCR = HIGH`;
3. `FF = FRAGILE` or `ABSENT`;
4. opponent has materially lower execution burden and either:
   - at least two meaningfully independent forcing routes, or
   - one highly reliable forcing route plus strong continuation/re-engage;
5. at least one meaningful scheduled objective/base-pressure sequence is expected to matter if the opponent gains control.

When active:

**UNDERDOG +KILLS IS TAKE-INELIGIBLE FOR THE ENTIRE MAP.**

This is a hard eligibility rule, not a probability penalty.

### No live override

The hard veto **must not** be removed, softened, or bypassed because of:

- current kill lead or parity;
- current gold lead or parity;
- tower/dragon parity;
- a widened positive handicap;
- one return kill;
- multiple return kills;
- two-snapshot temporal eligibility;
- temporary role-gold improvement;
- live odds movement;
- apparent short-term fight success;
- generic 'resilience proven' language;
- mechanism-valid live proof under v0.3.55.

v0.3.56 explicitly supersedes the v0.3.55 live-proof override **for HIGH DCR + FRAGILE/ABSENT FF underdog +kills cases.**

The only permitted removal is a **draft-input correction** that changes champion identity, role assignment, or the original matchup-functional DCR/FF classification. Ordinary live game events do not remove the hard veto.

---

## 4. Draft classification is locked before market temptation

DCR and FF must be classified **before** using the displayed +kills cushion as supporting evidence.

Do not let a large line such as +8.5 / +10.5 / +12.5 change the draft-collapse classification.

The handicap is arithmetic. DCR/FF determines whether the cover branch has a credible mechanism floor.

If DCR/FF were not classified before the candidate +kills market is evaluated, verdict defaults to:

**PASS/HOLD.**

---

## 5. Favorite negative handicap remains independent

A hard veto on underdog +kills does **not** automatically qualify favorite -kills.

Favorite -kills still requires all retained controls:

- signed kill-margin distribution;
- NKB;
- RFI;
- KCV;
- Structure Substitution;
- lower-bound surcharge;
- DED/DDC where applicable;
- RWE/TEI when visible/relevant;
- exact executable line and odds >=1.60.

Do not mechanically reverse a blocked +kills position.

---

## 6. ML and Total Kills interaction

### Moneyline

HIGH DCR / weak FF is a material draft-conversion downgrade and widens the opponent's clean-conversion tail, but it is not by itself a hard ML veto. ML still uses MKT + TEAM, draft mechanisms, live state, RWE/TEI and retained probability gates.

### Total Kills

HIGH DCR can increase clustered-death tails **conditional on contact**, but it does not automatically imply Over. CRR / RKS / KPW / Structure Substitution and future-window deletion still control.

---

## 7. Mandatory live checklist insertion

Before every underdog +kills verdict, internally record:

1. MKT/TEAM underdog identity at draft lock;
2. DER for both teams;
3. DCR for both teams;
4. FF for both teams;
5. forcing-cluster independence;
6. anti-cascade / survival-cluster independence;
7. objective-schedule interaction;
8. HARD DRAFT-COLLAPSE VETO: `ACTIVE / INACTIVE`;
9. RIT only if the hard veto is INACTIVE;
10. signed-margin/NKB/RFI/KCV/SS pricing only if the candidate remains eligible.

If `HARD DRAFT-COLLAPSE VETO = ACTIVE`, stop the underdog +kills evaluation and return PASS/HOLD. Do not continue searching for an exception.

---

## 8. Reference correction — NIP vs WBG G1

NIP:
- Olaf / Qiyana / Ryze / Jhin / Nautilus

WBG:
- Ambessa / Naafiri / Ahri / Xerath / Camille support

Correct draft classification:

### NIP
- DER: LOW/MEDIUM burden
- DCR: LOW
- FF: STABLE
- reliable independent first contact / continuation
- strong scheduled-objective conversion

### WBG
- DER: HIGH burden
- DCR: HIGH
- FF: FRAGILE/ABSENT
- weak conventional frontline/peel
- dive/pick and poke plans require incompatible spacing
- failed first contact can expose multiple melee champions simultaneously
- poor objective entry when behind

At 15:05 WBG led 5-3 and received +8.5 @1.961.

Under v0.3.56 the correct process is immediate:

**PASS — WBG +8.5 kills @1.961 — 0u.**

The current kill lead does not matter because the hard draft-collapse veto was already active from draft structure.

---

## 9. Retained v0.3.55 controls

All non-conflicting v0.3.55 controls remain active:

- Draft Execution Reliability;
- shared-failure clusters;
- objective-schedule x execution burden;
- Draft Correction Trigger;
- RIT for underdog +kills **only when the v0.3.56 hard veto is inactive**;
- scoreboard parity is not mechanism proof.

Where v0.3.55 says repeated live mechanism proof may downgrade an underdog +kills draft-burden veto, **v0.3.56 controls** for HIGH DCR + weak FF cases: there is no live exception.

---

## 10. Retained earlier controls

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

---

## 11. Operating state

- Active model: **LoL v0.3.56**
- Official betting: **PAUSED**
- Shadow mode: ACTIVE
- Default shadow stake: 0.25u
- Actual exposure: 0u
- Minimum odds: 1.60
- Pregame/immediate post-draft ML/KH/Total Kills TAKE: DISABLED unless separately promoted by a future rule
- Live ML/KH/TK: retained two-snapshot gate plus v0.3.56 draft-mechanism gates
- Duration restrictions: unchanged
- Same-game multiple shadow positions: enabled only when each independently qualifies

Shadow TAKEs that are visibly executable and qualify are auto-recorded after the user-facing verdict; no placement confirmation is required in shadow mode.

Where this delta conflicts with v0.3.55 or earlier interpretation, **v0.3.56 controls**.
