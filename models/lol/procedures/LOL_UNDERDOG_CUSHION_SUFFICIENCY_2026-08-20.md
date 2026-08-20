# LoL Underdog +Kills Cushion Sufficiency (UCS) — 2026-08-20

**Status:** MANDATORY v0.3.58 EXECUTION GUARD  
**Scope:** every underdog +kills live TAKE  
**Purpose:** prevent a draft-certified underdog fallback from being mistaken for sufficient handicap protection.

This is downstream of UDKC. It does not alter the draft-only UDKC certificate and does not create a new analytical model version.

## 1. Order of operations

For underdog +kills, run in this order:

1. exact locked draft available;
2. complete draft-only UDKC;
3. UDKC must be `STABLE` with all mandatory fields passing;
4. two live snapshots must satisfy the normal live eligibility gate;
5. exact signed current kill margin;
6. exact handicap failure threshold;
7. exact NKB to failure;
8. **UCS — Underdog Cushion Sufficiency**;
9. price/execution checks.

If UDKC is not STABLE, stop. UCS cannot rescue a failed draft certificate.

If UDKC is STABLE, that only makes the line eligible to inspect. It is never itself a TAKE signal.

## 2. Exact NKB definition

Let the favorite's signed current kill margin be:

`M = favorite kills - underdog kills`.

For an underdog line `+H.5`, the ticket loses if the favorite finishes with a kill margin of at least:

`F = H + 1`.

Define:

`NKB = F - M`

where NKB is the additional net kills the favorite needs from the current state to make the underdog +kills ticket lose.

Examples:

- current margin 0, underdog +3.5 -> failure margin +4 -> `NKB = 4`;
- favorite currently trails by 2, underdog +1.5 -> failure margin +2 -> `NKB = 4`;
- favorite currently leads by 1, underdog +8.5 -> failure margin +9 -> `NKB = 8`.

Use exact signed arithmetic. Do not reason from the displayed line alone.

## 3. Cushion bands

Use these as execution classifications, not standalone value signals:

- `THIN`: `NKB <= 4`
- `STANDARD`: `NKB = 5-6`
- `DEEP`: `NKB >= 7`

A deeper cushion is not automatically good; UDKC/KMS/RLD and live preservation still matter.

## 4. THIN hard guard

`THIN` is **HOLD by default**.

A THIN underdog +kills line may only reach `UCS = PASS` when all of the following are positively observed:

1. at least two distinct meaningful live contact/objective cycles have occurred after the game entered a representative fighting regime;
2. across those cycles, the underdog demonstrated actual anti-cascade behavior — reset, disengage, protected continuation, bounded cleanup, or otherwise prevented ordinary contact from becoming large net kill-margin expansion;
3. the observed suppression is produced by at least one independent mechanism that remains available for the next compulsory cycle;
4. the mechanism is not merely current gold parity, small current margin, safe ADC play, waveclear, grubs, isolated top gold, or theoretical draft utility;
5. the ordinary-fight stress test below passes.

If those observations do not exist, `UCS = FAIL/UNRESOLVED -> HOLD/PASS`.

This means an early +3.5 line generally cannot TAKE merely because UDKC is STABLE.

## 5. Ordinary-fight + continuation stress test

Before any underdog +kills TAKE, model one plausible ordinary adverse sequence from the current state:

`next compulsory contact -> primary fight -> normal continuation/cleanup -> reset or structure/objective transition`.

Ask:

- how many net kills can the favorite plausibly gain without requiring a miracle or terminal ace?
- does one normal lost fight plus realistic continuation reach or cross the handicap failure threshold?
- after first contact, does the underdog retain a genuine reset/suppression mechanism, or does the same failure cluster remain exposed?

Hard rule:

**If one ordinary fight + continuation can plausibly cross the failure threshold, UCS cannot PASS.**

Do not require the favorite to prove a full-game snowball; this gate is specifically testing whether the offered cushion can absorb ordinary variance.

## 6. STANDARD / DEEP interpretation

For `NKB >= 5`, still run the ordinary-fight stress test.

`STANDARD` or `DEEP` may pass only when:

- UDKC remains STABLE live;
- KMS/RLD mechanisms remain intact;
- the favorite does not have an obvious repeatable cascade route that makes the remaining NKB ordinary rather than demanding;
- the cushion survives one plausible adverse fight + continuation;
- no live downgrade has already locked the underdog fallback out.

No NKB band is an automatic TAKE.

## 7. Forbidden substitutions

The following cannot establish UCS by themselves:

- UDKC STABLE;
- large displayed +kills number;
- attractive odds;
- current 0-0 or small kill margin;
- gold parity;
- 0-0 towers;
- grubs;
- isolated top-side advantage;
- safe marksman range;
- theoretical peel/disengage not demonstrated under pressure;
- team-strength narrative.

## 8. Mandatory output for TAKE gate signature

Before any underdog +kills TAKE, resolve internally:

- `UDKC = STABLE`;
- `SIGNED_MARGIN = exact`;
- `FAILURE_THRESHOLD = exact`;
- `NKB = exact`;
- `UCS_BAND = THIN/STANDARD/DEEP`;
- `ANTI_CASCADE_OBS = PASS/FAIL/UNRESOLVED`;
- `ORDINARY_FIGHT_STRESS = PASS/FAIL`;
- `UCS = PASS/FAIL/UNRESOLVED`.

Any `FAIL/UNRESOLVED` decision-critical field forces HOLD/PASS.

Persist this inside the mandatory `GATE_SIG[...]` block defined by:
`models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`

## 9. Reference incident

KRX +3.5 kills @1.909 on 2026-08-20 was issued after UDKC was treated as sufficient evidence. At an even current kill margin, the favorite needed only four additional net kills to defeat the ticket — an ordinary fight-plus-cleanup swing. The position was later audit-invalidated.

The correct lesson is not that +3.5 is universally impossible. The lesson is that a thin cushion needs independent observed anti-cascade proof and must survive an ordinary adverse fight stress test.

Reference review:
`models/lol/reviews/CHAT_TRANSITION_EXECUTION_DRIFT_AND_SESSION_LOCK_REVIEW_2026-08-20.md`
