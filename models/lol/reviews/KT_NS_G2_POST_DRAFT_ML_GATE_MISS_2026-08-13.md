# KT.C vs NS.EA Game 2 — Post-Draft ML Gate Miss Review

Date: 2026-08-13
Model at time: LoL v0.3.55
Status: review note / candidate process correction only; not yet an active rule change

## What happened

Game 2 draft:

- NS blue: Jayce / Jarvan IV / Ryze / Yunara / Lulu
- KT red: Rumble / Wukong / Viktor / Jhin / Shen

The post-draft read correctly favored KT on Draft Execution Reliability (DER): KT had cleaner, lower-burden 5v5 execution, more deterministic objective/choke control, and more independent forcing/continuation than NS.

Post-draft prices supplied by the user included:

- NS ML 1.757
- KT ML 2.037
- NS -3.5 kills 1.894
- KT +3.5 kills 1.861

Under v0.3.55, immediate post-draft ML/KH/TK TAKEs were disabled, so KT ML @2.037 could not be taken. By the first live state (about 4:07), KT had already moved to 1.289 after leading 4-1 and about +1.6k. The two-snapshot gate therefore protected against early noise but also removed the only materially attractive KT ML price.

KT subsequently rolled the map with the easier-to-execute draft. The user correctly identified this as a missed easy ML opportunity.

## Process lesson

The draft evaluation itself was not the failure. The failure was a blanket timing gate that treated a strong post-lock mechanism edge the same as a speculative draft lean.

Candidate correction for later validation:

### Post-Draft ML Mispricing Override — ML only

Allow an immediate post-draft ML TAKE before the live two-snapshot gate only when all of the following are true:

1. The Draft Function Matrix is complete.
2. DER gap is material and clearly favors one side.
3. The lower-burden side has at least two independent forcing/continuation mechanisms or one reliable forcing route plus robust continuation/re-engage.
4. The opposing draft has materially higher shared-failure/coupling burden.
5. The edge is based on fight/objective execution reliability, not speculative lane snowball assumptions.
6. The market prices the lower-burden side as an underdog or near-coinflip at >=1.60.
7. TEAM/MKT anchoring does not strongly contradict the draft conclusion.
8. No known roster/role/champion uncertainty remains.

This override, if ever promoted, should apply to **Moneyline only**. Kill Handicap and Total Kills should retain live confirmation requirements because signed-margin and kill-environment distributions need observed state.

## Change-control status

Do not promote from this map alone. Treat as a candidate exception to the two-snapshot ML gate and validate against additional maps where a strong DER edge was available at post-draft underdog pricing but disappeared before live eligibility.

Reference context: v0.3.55 DER/shared-failure enforcement remains active and unchanged.
