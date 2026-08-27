# LoL Post NS–BFX Market Priority & Execution Calibration — 2026-08-27

**Status:** ACTIVE canonical v0.3.58 in-place amendment for future slates  
**Effective:** 2026-08-27 after completion of LCK 2026 Play-In — Nongshim RedForce vs BNK FEARX  
**Historical rewrite:** FORBIDDEN  
**User authorization:** “Adjust the model accordingly.”

## Purpose

The NS–BFX series exposed two distinct problems that must not be conflated:

1. live Moneyline opportunities were sometimes allowed to decay while the process waited for redundant confirmation; and
2. Total Kills Over was loosened too aggressively when draft contact inventory plus one early contact sequence were treated as sufficient recurrence proof.

This amendment preserves mechanism-first analysis while making market selection and execution more time-aware.

---

## 1. Market-family triage order — ML first

At every meaningful synchronized live state, evaluate candidate families in this order unless a family is unavailable/greyed:

1. **Moneyline**
2. **Kill Handicap**
3. **Total Kills**
4. **Duration**

This is a triage priority, not a quota and not positive evidence for ML.

Rationale: when the model has a side-win edge but final kill-margin or kill-recurrence distributions remain uncertain, ML is often the cleanest expression. Do not abandon a still-executable ML merely because a derivative market offers a larger displayed price.

Required field:
`MARKET_TRIAGE = ML_FIRST / N-A`

---

## 2. Live ML evidence path — earlier causal permission

For ordinary live ML where the contemplated side aligns with a CLEAR/STRONG draft prior, or the original draft was SLIGHT/EVEN/UNCLEAR, replace the formal two-live-snapshot requirement with:

`ML_EVIDENCE_COUNT >= 2` using causally independent evidence.

Eligible Path A:

- evidence 1 = certified exact-role draft mechanism with DIM + PDRL + PML where applicable;
- evidence 2 = first meaningful synchronized live state that directly confirms the mechanism through role-weighted economy, first move, map access, objective conversion, fight access, or multi-role leverage.

Eligible Path B:

- two distinct synchronized live states with a meaningful state transition.

The following are not independent evidence by themselves:

- kill lead + gold lead created by the same isolated event;
- one objective + one structure from the same uncontested macro sequence;
- one fed role + team gold lead when the team lead is mostly that role;
- market movement + the game event causing it.

No pregame or immediate-postdraft ML TAKE is permitted.

### Contrary CLEAR/STRONG draft prior

The retained LRO procedure remains mandatory when taking ML against an original CLEAR/STRONG draft edge. This amendment does **not** reduce the LRO 3SNAP / 2CYCLE override floor.

Required fields:
`ML_EVIDENCE_1 | ML_EVIDENCE_2 | ML_INDEPENDENCE | DRAFT_PRIOR_STATE | LRO`

---

## 3. ML state weighting — mechanism and role economy over raw kills

For live ML, raw kill score is descriptive, not dominant.

Lead Decomposition must explicitly weight:

- multi-role economy;
- primary carry/facilitator leverage;
- first-move access;
- structure/objective conversion;
- current item/level timing;
- whether the advantaged role is the composition’s demonstrated conversion engine.

A team may be down in kills yet be the correct ML side if it has superior role-weighted economy and a coherent current conversion route.

A single dragon or tower may reduce confidence but must not automatically veto repeated mechanism realization.

Required fields:
`ROLE_WEIGHTED_STATE | MULTI_ROLE_LEVERAGE | CONVERSION_ENGINE_FIT | OBJECTIVE_OFFSET`

---

## 4. HOLD expiry

HOLD is temporary. For the same candidate/family, it expires at the first of:

1. next meaningful synchronized state;
2. next major objective/contact/conversion cycle;
3. material line/price change.

At expiry resolve to TAKE or PASS unless the market has materially transformed into a new candidate.

Repeated HOLD with substantially the same missing item is prohibited.

Required fields:
`HOLD_MISSING_ITEM | HOLD_EXPIRY_TRIGGER | EXPIRY_RESOLUTION`

---

## 5. Opportunity decay — canonicalized

Prefer causal entries before terminal-event sensitivity dominates settlement.

### Preferred window — approximately 8:00–20:00

Normal price buffers apply. Once a valid ML mechanism is certified and live-confirmed, do not wait for redundant confidence while price deteriorates.

### 20:00–24:00

Normal gates apply plus terminal-event scan: Baron access, soul timing, death timers, immediate base/structure access.

### 24:00–27:00

Apply `LATE_ENTRY_BUFFER = +3pp` where probability pricing is used. New positions must remain mechanism-driven rather than one-event-driven.

### >=27:00

- new TK and Duration are presumptive PASS unless exceptional and demonstrably non-terminal;
- ML/KH require +5pp buffer plus CLEAR non-fragile mechanism;
- candidates dominated by “one more fight” / “one clean end” settlement branches must PASS.

Clock bands are guides; structural phase overrides clock when the map is unusually accelerated or undeveloped.

Required fields:
`CLOCK_PHASE | STRUCTURAL_PHASE | TERMINAL_EVENT_SENSITIVITY | LATE_ENTRY_BUFFER`

---

## 6. Total Kills Over — stricter recurrence standard

The NS–BFX Game 3 loss showed that **CONTACT INVENTORY is not CONTACT RECURRENCE**.

For TK Over:

- draft engage/pick/contact tools are contextual evidence only;
- a single early fight, first blood sequence, or first dragon fight is not sufficient recurrence proof;
- at least **two distinct observed contact realizations/cycles** are required before TK Over can certify, unless one synchronized state contains independently verifiable evidence of multiple distinct contacts separated by map progression;
- the second realization must show persistence or renewed compulsory contact, not merely cleanup from the first event;
- identify the next compulsory or highly probable contact source and why it remains live.

Resolve:
`CONTACT_INVENTORY | CONTACT_REALIZATION_1 | CONTACT_REALIZATION_2 | RECURRENCE_PERSISTENCE | NEXT_CONTACT_SOURCE | TERMINAL_SENSITIVITY | PRICE`

No draft+single-live shortcut is permitted for TK Over.

TK Under retains FRP and all existing gates.

---

## 7. Kill Handicap — do not loosen from the speed calibration

The recent KH sample remains weak and the side-neutral KHMC parent gate remains fully intact.

- KH still requires the side-neutral signed final-margin distribution;
- sign selection remains after distribution lock;
- WMS, cover-before-close, cushion/asymmetry, and sign-specific downstream gates remain mandatory;
- this amendment does not allow draft+single-live evidence to bypass KH distribution or anti-cascade requirements.

Do not shift from unresolved ML into KH merely because the handicap price is larger.

---

## 8. Fearless / restricted-pool draft inventory

For Game 2+ Fearless/restricted-pool series, PDRL + PML must treat remaining **functional archetypes** as first-class state.

Track at minimum:

- reliable engage;
- disengage/reset;
- front line;
- lane-priority access;
- jungle/support coupling;
- mid/jungle first move;
- bot stability/carry protection;
- waveclear;
- objective DPS;
- side pressure;
- pick threat;
- backline access.

Do not infer depth from remaining champion count alone. Player-specific execution burden and pocket-pick tax become more important as archetype scarcity increases.

---

## 9. User line-existence confirmation gate — canonical execution rule

A visible `TAKE` is an analytical candidate until the user confirms the quoted executable market still exists.

Required state:
`USER_LINE_CONFIRMATION = PENDING / CONFIRMED / FAILED`

Rules:

- `PENDING`: do not create a Positions record; do not count W/L or P/L.
- `CONFIRMED`: the exact quoted line/odds may become an accepted shadow position, subject to active logging/batching governance.
- `FAILED`: line disappeared, materially moved, or was not confirmed before becoming non-executable; no position exists.
- if the line/price changes materially, reassess the new line before acceptance.
- an unconfirmed TAKE may remain in Snapshot/audit evidence as an unexecuted analytical candidate.

This rule applies prospectively to successor LoL session locks unless the user explicitly revokes it.

---

## 10. Fast visible output

Live responses remain verdict-first and compact:

`TAKE <market> @<odds> — <stake> — CONFIRM IF STILL THERE`

or

`HOLD — <specific missing item>`

or

`PASS — <specific failed gate>`

Deep certification remains internal and mandatory.

---

## 11. PRE_TAKE wiring

For future applicable TAKES, add:

`POST_NS_BFX_CAL = PASS`

and family-specific fields above.

For ML Path A add:
`ML_EVIDENCE_COUNT>=2; ML_INDEPENDENCE=P; MARKET_TRIAGE=ML_FIRST`

For TK Over add:
`CONTACT_REALIZATION_1=P; CONTACT_REALIZATION_2=P; RECURRENCE_PERSISTENCE=P`

For any accepted position add:
`USER_LINE_CONFIRMATION=CONFIRMED`

A candidate may be analytically valid but is not a Position until user confirmation passes.

---

## 12. Historical integrity

Do not rewrite NS–BFX historical positions or verdicts.

- Game 2 O39.5 @2.086 remains a valid loss under its original authority.
- Game 3 O29.5 @1.863 remains a valid logged loss if it was previously logged/accepted under the authority then in force; this calibration does not outcome-fit it into a fictional PASS.
- Game 4 BFX ML @2.943 remains a valid confirmed win and serves as supporting process evidence, not proof by outcome alone.

The amendment is prospective only.
