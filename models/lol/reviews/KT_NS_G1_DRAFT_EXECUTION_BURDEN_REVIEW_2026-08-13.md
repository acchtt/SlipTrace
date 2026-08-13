# KT Challengers vs NS Challengers Game 1 — Draft Execution Burden Review

**Date:** 2026-08-13 UTC+7  
**Model at entry:** LoL v0.3.54  
**Market reviewed:** NS.EA +8.5 kills @1.943, shadow 0.25u  
**Result:** LOSS (-0.25u)  
**Final user-authoritative winner:** KT Challengers  
**Latest grading frame:** KT 19-5 NS at 29:50, KT +14k gold, 10-0 towers, 4-0 dragons, 1-0 Baron, 2-0 inhibitors

## 1. Draft

KT Challengers:
- Olaf
- Vi
- Cassiopeia
- Ashe
- Seraphine

NS Challengers:
- Gnar
- Xin Zhao
- Anivia
- Ezreal
- Blitzcrank

## 2. Entry state

At 15:28:
- KT 3-2 NS;
- NS approximately +108g overall;
- towers 0-0;
- KT 2-0 dragons;
- no Baron;
- role-gold was mixed: NS Gnar +780, NS Anivia +118, KT Vi +132, KT Ashe +531, KT Seraphine +127;
- market: NS +8.5 kills @1.943 / KT -8.5 kills @1.816.

The old verdict was TAKE NS +8.5. That was a process error.

## 3. What the draft matrix should have said

### KT — low-burden, repeatable forcing

KT had several matchup-functional ways to start and continue fights:

- Ashe provides long-range first contact and pick initiation;
- Vi provides highly reliable backline access and lockdown once a target is selected;
- Olaf can run through much of NS's control and sustain pressure after first contact;
- Cassiopeia converts compressed space and objective chokes into sustained damage and zone denial;
- Seraphine layers follow-up control, shielding/healing and extended-fight value.

The crucial point is not champion count. KT's sequence was **simple and repeatable**:

`Ashe/Vi contact -> forced target displacement/lockdown -> Olaf/Cass pressure -> Seraphine extension -> cleanup/objective`.

If Ashe misses, Vi can still start. If Vi starts, Ashe can follow. Olaf does not require the same first-spell success to remain useful. These are meaningfully independent forcing layers.

### NS — higher-burden, conditionally coupled survival

NS had useful tools, but they were over-credited as independent handicap resilience:

- Gnar needs rage timing and favorable terrain/spacing;
- Anivia needs prepared terrain and time to establish zone control;
- Blitzcrank is primarily pick-oriented and requires hook access rather than offering reliable broad peel;
- Xin Zhao provides close-range disruption but must already enter the fight successfully;
- Ezreal can kite safely but does not by himself stop KT's deterministic access onto other targets.

Several NS tools depended on the **same shared state**: being set first, having the correct terrain, preserving spacing, and landing the first important spell before KT's direct engage arrived. They were therefore PARTIALLY COUPLED / COUPLED rather than five independent defensive answers.

## 4. Objective schedule mattered

KT already led dragons 2-0 at entry. That did not merely add objective value; it scheduled future high-value setup windows in which KT's easier engage and zone-control sequence would be repeatedly tested against NS's harder execution.

Near-even gold therefore did not imply near-even future fight quality.

The 2-0 dragon state should have increased the weight on:
- prepared objective terrain;
- forced approach paths;
- first-contact reliability;
- repeat forcing after resets;
- the cost of NS needing correct Gnar/Anivia/Blitz conditions simultaneously.

## 5. Why the +8.5 thesis was invalid at entry

The old rationale was that NS's Anivia/Gnar/Blitz shell could disengage, pick and stall enough to bound the final kill margin.

That reasoning violated retained v0.3.47/v0.3.53 controls:

1. **Draft Primacy:** execution burden was scored too lightly.
2. **Mechanism Independence:** multiple conditional tools were counted as if independent.
3. **Underdog Resilience Must Be Mechanistic:** theoretical zone/pick tools were credited without proof they could stop KT's exact engage routes.
4. **Anti-favorite guard:** KT's baseline favorite/conversion edge had not been shown suppressed; KT already held 2-0 dragons.
5. **Two-snapshot gate misuse:** two synchronized scoreboards showed state persistence, but did not prove NS's high-burden defensive mechanisms were functioning in repeated forced objective fights.

The correct process at 15:28 was **PASS/HOLD NS +8.5**, not TAKE.

This review does **not** conclude that KT -8.5 was automatically a TAKE. At near-even gold and only a +1 current kill margin, the favorite negative handicap still needed its own signed-margin probability gate. The correction is to remove the false underdog-resilience edge, not to mirror every bad underdog bet into a favorite bet.

## 6. Later confirmation

At 26:18:
- KT 12-5 NS;
- KT +6.8k;
- towers 4-0;
- dragons 4-0;
- Baron 1-0;
- role economy strongly favored KT on Vi, Cassiopeia, Ashe and Seraphine.

At 29:50:
- KT 19-5 NS;
- KT +14k;
- towers 10-0;
- dragons 4-0;
- Baron 1-0;
- inhibitors 2-0.

The final margin confirms the failure mode, but the correction is justified by the **pre-existing deterministic draft requirements at entry**, not by hindsight alone.

## 7. Required correction

Promote a narrow process-enforcement delta:

- draft execution reliability must be explicitly classified before ML/KH/TK live TAKEs;
- shared-failure clusters must be counted as clusters, not ability count;
- underdog +kills receives a hard HOLD/PASS gate when its margin-saving mechanisms are high-burden/coupled against a favorite with repeatable independent forcing, unless live evidence proves those mechanisms are functioning;
- scoreboard parity and two synchronized snapshots do not constitute mechanism proof by themselves;
- objective scheduling must be combined with execution burden because repeated dragon/Baron setup can expose a harder draft even before a large gold lead appears;
- a user draft correction triggers a full position-blind Draft Function Matrix rerun, not a cosmetic probability adjustment.

Reference rule delta: `models/lol/rules/MODEL_RULES_LOL_V0.3.55.md`.
