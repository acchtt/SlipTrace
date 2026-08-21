# NS vs T1A Game 1 — Live ML Draft-Prior Anchoring Review — 2026-08-21

**Status:** calibration review  
**Model:** LoL v0.3.58  
**Scope:** Live Moneyline decision process only  
**Historical position:** none; no retrospective bet is created

## 1. Problem

The post-draft read classified T1A as a CLEAR draft favorite. That read then carried too much veto weight into the live ML process after repeated live evidence showed that the mechanisms supporting the draft edge were not functioning at the current role/economy state.

The issue was not that the draft should be ignored. The issue was **anchoring**: the live model kept asking whether NS could overcome T1A's theoretical draft geometry rather than asking whether that geometry was still operational with the current items, levels, role leverage and objective schedule.

## 2. Evidence used for the review

To avoid outcome-driven hindsight, the eligibility review stops at the 10:33 snapshot.

### 4:13

- NS 2-1 T1A;
- NS about +553g;
- towers 0-0;
- dragons 0-0;
- barons 0-0.

Correct live verdict: HOLD. This is only one snapshot and the lead is too early to override the draft prior.

### 7:34

- NS 3-2 T1A;
- NS about +895g;
- NS first dragon;
- towers 0-0;
- role leverage already favors NS in several relevant positions, especially the bot/support side relative to the T1A post-draft control thesis.

Historical live verdict: HOLD.

Review verdict remains HOLD. Two snapshots are not enough to take ML against a CLEAR draft prior under the new safeguard.

### 10:33

- NS 4-3 T1A;
- NS about +1.4k;
- NS 1-0 dragons;
- towers 0-0;
- visible role-economy advantages support NS across jungle, mid, ADC and support rather than one isolated lane;
- T1A's claimed Xayah/Rakan protected-DPS / Jarvan-Rakan control engine has not materialized as the dominant objective/fight mechanism;
- executable NS ML: 2.094.

This is the first point where the contrary live regime has persisted across three snapshots and multiple meaningful cycles.

## 3. Mechanism diagnosis

The original draft thesis for T1A relied heavily on:

- Jarvan/Rakan initiation and first-contact control;
- Xayah's protected DPS / anti-dive reliability;
- Ryze follow-up and objective-fight continuation;
- Olaf creating front-line space.

By 10:33, the relevant question was no longer which composition wins at equal economy. The correct live question was whether those mechanisms were functioning with the current state preserved.

They were not functioning strongly enough to remain a permanent ML veto:

- the T1A bot lane was materially behind relative to the role that needed to anchor protected DPS;
- NS held the first dragon and repeated bot-side/role leverage;
- NS's advantage was distributed across multiple fight-relevant roles;
- the lead persisted and expanded from +553 -> +895 -> +1.4k instead of immediately reverting.

The historical reasoning over-weighted the original draft edge and under-weighted **mechanism degradation**.

## 4. Corrected process

The correction is not a generic `underdog ahead -> bet underdog` rule.

For Live ML against a CLEAR/STRONG draft prior, require the new Live Regime Override certificate:

- three usable snapshots;
- at least two meaningful contact/objective cycles;
- persistent coherent regime;
- multi-role leverage;
- exact original draft mechanism failure;
- current-state CFC PASS;
- next-cycle stress PASS using current items/levels/economy;
- no low-friction draft recovery path.

Mandatory procedure:
`models/lol/procedures/LOL_LIVE_ML_DRAFT_PRIOR_DEGRADATION_AND_REGIME_OVERRIDE_2026-08-21.md`

## 5. Counterfactual decision

Using only evidence available at 10:33, the intended corrected classification is:

- `DPS = BROKEN` for the original CLEAR T1A prior at the current live state;
- `LRO = PASS` if the synchronized next-cycle/CFC checks are resolved consistently with the observed role and objective leverage;
- **TAKE — NS ML @2.094 — 0.25u shadow / 0u actual**.

This is a missed-window calibration finding only. It does not create or settle a historical position.

## 6. Anti-overfit note

The later game result is not needed to justify the change and must not be used as a gate input. The fix is grounded in the repeated pre-10:33 live mechanism evidence and in the structural problem of treating a draft prior as a hidden permanent veto.
