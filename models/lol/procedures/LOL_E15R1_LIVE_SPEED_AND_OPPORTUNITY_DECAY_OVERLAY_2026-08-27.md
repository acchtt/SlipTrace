# LOL E15R1 — Live Speed and Opportunity-Decay Overlay

**Effective:** 2026-08-27 16:41 UTC+7  
**Scope:** LCK 2026 Play-In — Nongshim RedForce vs BNK FEARX — Games 3–5 only  
**Base analytical model:** LoL v0.3.58  
**Status:** ACTIVE session-scoped prospective override  
**Historical rewrite:** FORBIDDEN

## Purpose

The user identified a live-execution failure mode after Game 2: the model was waiting for excessive confirmation, allowing the market to reprice and pushing entries into late, terminal-event-sensitive states. This overlay is intended to move valid entries earlier without relaxing synchronization, price, position-blindness, signed-margin arithmetic, market-family mechanics, or anti-chasing controls.

The target execution path is:

`DRAFT MECHANISM -> FIRST MEANINGFUL LIVE CONFIRMATION -> IMMEDIATE VERDICT`

not:

`DRAFT -> MULTIPLE REDUNDANT SNAPSHOTS -> OBJECTIVE -> MARKET REPRICE -> LATE ENTRY`.

---

## 1. Two independent evidence points replace hard 2SNAP for live ML / KH / TK

For this series from Game 3 onward, the canonical requirement that live ML/KH/TK require two usable synchronized live snapshots is replaced by:

`EVIDENCE_COUNT >= 2`, where the two points must be causally independent.

### Eligible path A — strong draft mechanism + live confirmation

Evidence point 1 may be a **certified professional draft mechanism** only when all of the following are true:

- exact roles are reconstructed;
- DIM = PASS;
- PDRL = PASS;
- PML = PASS;
- the mechanism is explicit and causal, not a generic draft-grade label;
- the mechanism names the expected lane/jungle-support/first-move/objective/fight route;
- the mechanism has a defined break condition;
- no immediate-postdraft TAKE is issued.

Evidence point 2 may then be the **first meaningful synchronized live snapshot** if that snapshot directly confirms the same mechanism through observable state such as first-move access, multi-role economy, repeated pick access, objective conversion, fight-shape realization, bounded counter-engage, or margin expansion.

When Path A passes, ML/KH/TK are TAKE-eligible immediately at that live snapshot. A second live screenshot is not required merely for formality.

### Eligible path B — two live synchronized states

Two usable synchronized live snapshots remain sufficient when draft evidence is weak, ambiguous, unavailable, or contradicted.

### Ineligible evidence duplication

The following do not count as two independent points by themselves:

- kill lead + gold lead from the same isolated event;
- one dragon + one tower from the same uncontested macro sequence;
- one fed player + team gold lead when the team lead is mostly that same player;
- market movement + the game event that caused it;
- two screenshots that show no meaningful state transition.

Required internal fields for ML/KH/TK candidates:

`EVIDENCE_1 | EVIDENCE_2 | INDEPENDENCE_CHECK | DRAFT_MECH_STATUS | LIVE_CONFIRM_STATUS`.

---

## 2. HOLD expiry — HOLD is temporary, not a parking state

A HOLD means a specific missing confirmation remains reachable. It may not be repeated indefinitely.

For the same market family, a HOLD expires at the first of:

1. the next meaningful synchronized live snapshot;
2. the next major objective/contact/conversion cycle;
3. a material market-line reprice that changes the required mechanism or threshold.

At expiry, the verdict must resolve to **TAKE** or **PASS** unless the market itself has transformed into a materially different candidate.

Repeated HOLD with substantially the same rationale is forbidden.

Required field:

`HOLD_MISSING_ITEM | HOLD_EXPIRY_TRIGGER | EXPIRY_RESOLUTION`.

---

## 3. Opportunity-decay clock

Information edge decays as League maps approach terminal objective / death-timer / base-access states. The model must prefer earlier causal entries over late boundary bets.

### Phase A — preferred entry window

Approx. **8:00–20:00**.

- Normal retained pricing buffers apply.
- A Path-A draft+live confirmation TAKE is explicitly encouraged when all market-specific gates pass.
- Do not wait for an additional snapshot solely to increase confidence after the mechanism is already live-confirmed.

### Phase B — normal but decaying

Approx. **20:00–24:00**.

- Normal gates remain active.
- Require a brief terminal-event scan: Baron spawn/access, soul-point timing, death-timer leverage, immediate structure access.
- If the candidate remains primarily mechanism-driven rather than one-event-driven, ordinary TAKE remains allowed.

### Phase C — late / terminal sensitivity rising

Approx. **24:00–27:00**.

- New positions require a materially stronger edge than the ordinary phase.
- Apply `LATE_ENTRY_BUFFER = +3 percentage points` to the selected-side lower-bound probability threshold where probability pricing is used.
- For TK/Duration, explicitly test whether one Baron/ace/base push can determine settlement before expected recurrence/stall can express.
- If settlement is dominated by one terminal branch, PASS.

### Phase D — very late / boundary regime

Approx. **>=27:00**.

- New TK and Duration TAKES are presumptive PASS unless the edge is exceptional and demonstrably not dominated by one terminal event.
- New ML/KH TAKES require `LATE_ENTRY_BUFFER = +5 percentage points` and a CLEAR non-fragile mechanism.
- A candidate whose value depends mainly on “one more fight” or “one clean end” is treated as boundary/coinflip-sensitive and must PASS.

Time bands are execution guides, not substitutes for map state. An unusually accelerated map may enter a later terminal regime earlier; an unusually undeveloped map may remain in a prior regime longer. Record both clock and structural phase.

Required fields:

`CLOCK_PHASE | STRUCTURAL_PHASE | TERMINAL_EVENT_SENSITIVITY | LATE_ENTRY_BUFFER`.

---

## 4. Mechanism realization outranks isolated objective counters

Do not let a single dragon/tower count mechanically veto a candidate when the opposing side's actual draft/live mechanism is repeatedly realizing.

For ML/KH, weight the following above isolated objective possession when causally coherent:

- repeated first move;
- successful jungle/mid or jungle/support coupling;
- pick access repeatedly creating numbers advantage;
- multi-role margin expansion;
- forced objective access generated by fight wins;
- demonstrated ability to re-enter or deny the opponent's preferred fight shape.

Objective possession remains important, especially soul/Baron/elder pressure, but it is an input to CFC/transition quality rather than an automatic veto.

Game-2 calibration note: BFX's Ahri/Vi/Rumble mechanism was strongly realized while NS held two dragons. The two dragons should have reduced confidence, not erased the realized BFX pressure signal.

---

## 5. Concentrated leads — discount without erasing executable carry states

Retain lead decomposition. However, `EXTREME` concentration is not automatically weak if the fed role is the exact conversion engine of the composition and has demonstrated access.

Resolve:

`CONCENTRATION_CLASS | FED_ROLE_CONVERSION_FIT | ACCESS_REALIZED | REST_OF_MAP_STATE | OBJECTIVE_OFFSET`.

A fed Ahri, Zeri, Jinx, etc. may be highly actionable when the surrounding composition repeatedly enables the champion's conversion path. Concentration becomes a stronger discount when the fed role lacks access, is easily isolated, or the other four roles are materially losing map control.

---

## 6. Favorite kill handicap — earlier forward-margin permission

The side-neutral KH distribution remains mandatory and sign must still be selected after distribution lock.

For favorite -H, do not require the current kill margin to already approach the displayed handicap. A favorite -H may qualify earlier when:

- the favorite mechanism is live-confirmed;
- WMS shows repeated realistic expansion cycles;
- the forward signed-margin distribution supports cover;
- selected-side lower-bound cover probability clears break-even plus retained phase buffer;
- `COVER_BEFORE_CLOSE` is credible rather than merely theoretical.

Do not demand near-certainty. Conversely, one fed carry or one isolated 4–0 fight cannot alone certify a wide favorite handicap.

Underdog +H remains governed by the retained side-neutral / anti-cascade stack; this overlay does not restore automatic dog-cushion selection.

---

## 7. Total Kills and Duration — earlier causal evidence, stricter late entries

### Total Kills

TK may qualify earlier when contact recurrence is supported by two independent evidence points, including draft mechanism + first live confirmation.

For Over, distinguish:

`CONTACT_INVENTORY` from `CONTACT_REALIZATION`.

A draft with forced-contact tools is evidence only when live state confirms those tools are producing repeated executable contacts or compulsory objective fights.

For Under, FRP remains mandatory.

### Duration

DOVC/FCR remain mandatory. This overlay does **not** weaken DOVC/FCR.

However, the model should actively seek DOVC evidence in the 12–22 minute range rather than wait until 24+ minutes. Failed conversion, reset, denied structure sequence, split objective ownership, and repeatedly non-terminal fight outcomes are valuable earlier evidence.

After Phase C begins, terminal-event sensitivity must be explicitly added to DOVC/FCR.

---

## 8. Fast verdict presentation

For live screenshots, visible output must begin with one line:

`TAKE <market> @<odds> — <stake>`

or

`HOLD — <specific missing item>`

or

`PASS — <specific failed gate>`.

Then provide at most 2–4 short causal bullets unless the user asks for full detail.

All deeper certification remains mandatory internally. Speed of presentation does not waive PRE_TAKE_CERT, contradiction scan, mechanical validation, position-blindness, or arithmetic.

---

## 9. Controls explicitly unchanged

The following remain unchanged:

- minimum accepted odds = 1.60;
- official betting paused; shadow only;
- default shadow stake = 0.25u;
- actual exposure = 0u;
- no pregame/immediate-postdraft ML/KH/TK TAKE;
- user same-message scoreboard + market screenshots presumed synchronized unless state contradiction exists;
- position-blind reassessment mandatory;
- exact signed kill-margin arithmetic mandatory;
- KH side-neutral parent distribution mandatory;
- no dog +H default;
- DOVC / FCR / FRP retained;
- same-map one TAKE maximum per market family;
- greyed/stale markets non-executable;
- no rescue, chasing, martingale, or stake escalation;
- Airtable map-end batching/exact verification remains in force for this series.

---

## 10. PRE_TAKE wiring for this overlay

Every TAKE under this overlay must additionally record:

`E15R1_SPEED_OVERLAY = PASS`

`EVIDENCE_COUNT >= 2`

`EVIDENCE_1`

`EVIDENCE_2`

`INDEPENDENCE_CHECK = PASS`

`DRAFT_MECH_STATUS = PASS/NA`

`LIVE_CONFIRM_STATUS = PASS`

`CLOCK_PHASE`

`STRUCTURAL_PHASE`

`TERMINAL_EVENT_SENSITIVITY = LOW/MEDIUM/HIGH`

`LATE_ENTRY_BUFFER`

`HOLD_EXPIRY_STATUS = PASS/NA`

A TAKE is invalid if a candidate became eligible earlier under this overlay but was intentionally delayed solely to obtain redundant confidence while the line materially worsened. Record the earliest qualifying evidence point where reasonably identifiable.

---

## 11. Prospective-only calibration

This overlay applies only to Games 3–5 of NS–BFX on 2026-08-27.

Game 1 and Game 2 verdicts, positions and P/L remain frozen exactly as originally issued. Game 2 O39.5 @2.086 remains a valid model loss and is not reclassified.
