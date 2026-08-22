# LoL Duration Over & Underdog +Kills Execution Hardening — 2026-08-23

**Status:** ACTIVE CANONICAL v0.3.58 IN-PLACE AMENDMENT  
**Effective:** 2026-08-23 UTC+7  
**Model version:** unchanged — LoL v0.3.58  
**Authorization:** user instruction “Adjust accordingly.” after the 2026-08-23 session review  
**Reference review:** `models/lol/reviews/LEC_FNC_SHFT_SK_MKOI_SESSION_REVIEW_2026-08-23.md`

This procedure is narrow enforcement hardening. It does not restore v0.3.59/v0.3.60 and does not create a new analytical model version.

It augments and, where stricter, supersedes the Duration Over and underdog +kills execution signatures in:

- `models/lol/rules/MODEL_RULES_LOL_V0.3.58.md`
- `models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`
- `models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`

---

## 1. Duration Over — DOVC hard gate

Every model-certified Duration Over candidate must build a **DOVC — Duration Over Verification Certificate** before PRE_TAKE_CERT can pass.

Required fields:

`CONVERSION_CLASS | POSITIVE_CLOCK_MECH_1 | POSITIVE_CLOCK_MECH_2 | FAILED_CONVERSION_OR_EQUIVALENT | OBSERVED_STALL_EVIDENCE_ID | CLOCK_CAUSALITY | STRUCTURE_SUBSTITUTION | SHORTEST_CASCADE_TEST | SURVIVAL_HORIZON | PRICE`

Allowed terminal values must be explicit and evidence-grounded. Narrative implication is not enough.

### 1.1 Conversion class is mandatory

Classify current conversion evidence:

- `FAILED CONVERSION`
- `EQUIVALENT REPEATED DENIAL`
- `ABSENT CONVERSION`
- `UNRESOLVED`

Only the first two are eligible to satisfy the mandatory observed-stall component.

`ABSENT CONVERSION` or `UNRESOLVED` => **DOVC FAIL => HOLD/PASS**.

Examples of `ABSENT CONVERSION`:

- 0–0 towers because neither team has created a real conversion window;
- low tower count with no meaningful siege/tempo denial observed;
- low kills while objective/structure progress remains normal;
- close gold or neutral dragons without a demonstrated failed conversion.

### 1.2 Theoretical delay tools are not observed delay

Champion-kit or composition traits such as:

- waveclear;
- disengage;
- peel;
- range;
- scaling;
- side-lane pressure;

may explain *how* delay could occur, but they cannot satisfy `FAILED_CONVERSION_OR_EQUIVALENT` unless the live evidence actually shows that mechanism consuming clock under meaningful pressure.

“The team has Taliyah/Tristana waveclear” is not a positive clock mechanism until a real siege/tempo/Baron-pressure window is demonstrably delayed or denied by that waveclear.

### 1.3 Two positive clock mechanisms remain mandatory

`POSITIVE_CLOCK_MECH_1` and `POSITIVE_CLOCK_MECH_2` must be independent future-relevant mechanisms.

At least one must be tied to `FAILED CONVERSION` or `EQUIVALENT REPEATED DENIAL`.

The following can never count as either mechanism by themselves:

- low kills;
- 0–0 towers;
- low tower count;
- no inhibitor;
- quiet elapsed time;
- close gold;
- tied dragons;
- attractive Over price.

The second mechanism may be another demonstrated denial/reset route, a genuinely clock-consuming objective-spacing constraint, repeated safe concession that prevents serial structures, or another evidence-grounded delay path. It cannot be the same mechanism restated in different words.

### 1.4 OBSERVED_STALL_EVIDENCE_ID is compulsory

Every Duration Over certificate must identify the actual live event/window used as observed stall proof.

Valid forms include a clock/window plus a concise event description, for example:

`22:10–23:05 Baron pressure -> defended; no tower/inhibitor conversion; reset forced`

Invalid:

- “good waveclear”;
- “game is slow”;
- “towers still standing”;
- “they should be able to stall.”

Missing or narrative-only `OBSERVED_STALL_EVIDENCE_ID` => **DOVC FAIL**.

### 1.5 CLOCK_CAUSALITY test

For each claimed positive mechanism, answer:

**“Why does this mechanism consume future clock rather than merely describe the current state?”**

If the causal answer is not explicit, the mechanism does not count.

### 1.6 Structure Substitution and shortest-cascade stress remain mandatory

Explicitly test:

`next compulsory fight/objective -> serial structures -> base access -> Nexus`

A quiet history does not protect the Over if one realistic next-cycle loss can compress the map inside the survival horizon.

If the shortest plausible cascade ends materially before the Over threshold and there is no demonstrated independent delay that survives that branch, `SHORTEST_CASCADE_TEST = FAIL`.

### 1.7 Duration Over PRE_TAKE_CERT extension

The family signature is now:

`LOCK | MODEL | EXEC | ODDS | FAMILY | POSBLIND | CONVERSION_CLASS | POSITIVE_CLOCK_MECH_1 | POSITIVE_CLOCK_MECH_2 | FAILED_CONVERSION_OR_EQUIVALENT | OBSERVED_STALL_EVIDENCE_ID | CLOCK_CAUSALITY | STRUCTURE_SUBSTITUTION | SHORTEST_CASCADE_TEST | SURVIVAL_HORIZON | PRICE`

Every field must be populated and pass before visible `TAKE`.

There is no price-based override.

---

## 2. Underdog +kills — LAC hard gate

A draft-only UDKC `STABLE` certificate means the underdog has a theoretically viable fallback profile. It does **not** prove that the fallback is preserved in the current live regime.

Every underdog +kills candidate therefore requires separate **LAC — Live Anti-Cascade Confirmation**.

Required terminal values:

- `LAC = PASS`
- `LAC = FAIL`
- `LAC = UNRESOLVED`

Only `PASS` is TAKE-eligible.

### 2.1 Core LAC question

Before every underdog +kills TAKE answer:

**“Has the current live regime demonstrated that the underdog can suppress repeated favorite net kill-margin expansion, rather than merely owning a numerical cushion right now?”**

### 2.2 Positive LAC evidence

LAC must be supported by live evidence from the current synchronized regime, not draft theory alone.

Strong support includes one or more of the following, with role-leverage context:

1. **Demonstrated suppression cycle** — the favorite obtained meaningful pressure/contact leverage but the underdog reset, disengaged, returned kills, traded safely, or otherwise prevented the expected net kill-margin expansion.
2. **Repeated preservation** — across more than one meaningful live contact/objective window, the favorite failed to convert pressure into accelerating net kill-margin growth.
3. **Structural restraint** — real tower/wave/objective control or side-lane pressure materially reduces the favorite's ability to force serial grouped fights.
4. **Multi-role live resilience** — economy/levels and survival tools are distributed in a way that preserves multiple actual reset/return-kill channels, not one isolated lane asset.

A single favorable event can support LAC only if it demonstrates the exact anti-cascade mechanism strongly enough and no contradictory trend is present. When ambiguous, fail closed.

### 2.3 Explicit non-evidence

The following are not sufficient by themselves and cannot be used to upgrade LAC:

- current kill lead;
- one dragon;
- small gold lead;
- 0–0 towers;
- large displayed +kills cushion;
- exact NKB arithmetic;
- attractive odds;
- theoretical scaling;
- theoretical waveclear/peel;
- safe marksman play;
- one isolated top-side economy lead;
- grubs.

These may be context, but they are not live anti-cascade proof.

### 2.4 Shallow-lead false-preservation guard

If all are true:

- underdog live edge is shallow or concentrated in kills/one objective;
- no meaningful tower/tempo/control advantage exists;
- favorite has repeatable engage, pick, zone, siege, or continuation routes;
- underdog has not demonstrated a real reset/return-kill/denial cycle;

then `LAC = FAIL` regardless of the displayed +kills buffer.

This guard directly blocks the failure pattern seen in SHFT +5.5 versus FNC.

### 2.5 LAC is downstream of draft proof, not a replacement for it

Required order:

`DIM -> UDKC draft-only STABLE -> live preservation -> LAC -> UCS -> exact signed-margin/NKB -> price`

LAC cannot create missing DIM/TAM/CAS/KMS/RLD proof.

Likewise, a draft-certified STABLE profile cannot substitute for LAC.

### 2.6 Underdog +kills PRE_TAKE_CERT extension

The family signature is now:

`LOCK | MODEL | EXEC | ODDS | FAMILY | POSBLIND | 2SNAP | DIM | TAM | CAS | UDKC_STABLE | KPA | KMS | RLD | FALSE_STABLE_INACTIVE | LIVE_PRESERVATION | LAC | UCS | SIGNED_MARGIN | EXACT_NKB`

Missing, implied, `FAIL`, `UNRESOLVED`, or narrative-only `LAC` => **HOLD/PASS**.

---

## 3. Live Moneyline — no broad hardening

Do not import DOVC or LAC into Live ML.

The session's successful ML decisions support retaining the existing framework:

- synchronized live evidence;
- two-snapshot eligibility unless LRO requires more;
- Lead Decomposition;
- current-state CFC;
- neutral-fight stress;
- Draft Prior State;
- LRO only when opposing CLEAR/STRONG draft prior;
- minimum odds 1.60.

A failure in Duration or underdog +kills does not justify generic ML conservatism.

---

## 4. Verdict latency — enforce existing state-change expiry

No new analytical gate is added.

Operational order remains:

`evidence -> PRE_TAKE_CERT -> validation -> visible verdict -> Airtable logging -> exact verification`

Nonessential connector work must not occur before the visible verdict.

If state or price materially changes while analysis is pending, the certificate expires and must be rebuilt from zero.

If the synchronized state and executable price remain unchanged, the same decision window remains valid.

---

## 5. Anti-overfit / anti-outcome guard

This amendment must not be interpreted as:

- an elapsed-time minimum for Duration bets;
- a blanket ban on Duration Over;
- a mandatory tower lead for every underdog +kills TAKE;
- a reason to raise the 1.60 global odds floor;
- a reason to suppress qualified live ML entries;
- permission to rewrite historical losses as retrospective non-bets.

The goal is exact proof enforcement, not lower betting frequency for its own sake.

---

## 6. Activation under Session Authority Lock

This file is active only when included in the frozen `authority_commit` of the applicable session lock.

The user explicitly authorized adjustment on 2026-08-23 UTC+7, so a new authority epoch may include this amendment immediately.
