# NIP vs WBG Game 1 — Draft Collapse Risk / Fallback Floor Review

**Date:** 2026-08-13 UTC+7  
**Series:** LPL 2026 Split 3 — NIP vs WBG  
**Map:** Game 1  
**Model at decision:** LoL v0.3.55  
**Purpose:** correct a repeated underdog +kills process failure caused by underweighting draft collapse risk.

## Settled shadow position

- Selection: WBG +8.5 kills
- Odds: 1.961
- Shadow stake: 0.25u
- Actual exposure: 0u
- Entry clock: 15:05
- Entry score: WBG led 5-3
- Entry objectives: dragons 1-1, towers 0-0
- Final kill score supplied by user: NIP 22-10 WBG
- Result: LOSS (-0.25u)
- Final NIP kill margin: +12

## Draft

NIP:
- Olaf
- Qiyana
- Ryze
- Jhin
- Nautilus

WBG:
- Ambessa
- Naafiri
- Ahri
- Xerath
- Camille support

## What the model got wrong

The model correctly leaned NIP on TEAM and draft execution reliability, but classified the WBG +kills cover branch as live-resilient after WBG produced a favorable return-kill sequence and led 5-3 at 15:05.

That was the process error.

WBG's composition had **HIGH Draft Collapse Risk** and a **FRAGILE/ABSENT Fallback Floor** relative to NIP:

- no conventional durable front line;
- limited reliable peel for Xerath;
- several melee access champions whose value depends on obtaining angle/target access first;
- dive/pick and long-range poke plans pull the composition into different spacing requirements;
- failed first contact exposes multiple melee champions at once;
- objective setup becomes difficult when forced to enter NIP-controlled terrain;
- once behind, WBG cannot reliably stabilize by front-to-back, disengage, or protected DPS;
- NIP has repeatable independent first contact through Nautilus, terrain/choke conversion through Qiyana, Olaf continuation, and ranged follow-up through Ryze/Jhin.

The key error was treating live return kills as proof that WBG's margin-saving resilience had become reliable. They had not changed the underlying failure topology: the same coupled access/spacing conditions still controlled whether WBG could avoid clustered deaths.

## Correct draft classification

### NIP
- Draft Execution Reliability: LOW/MEDIUM burden
- Independent forcing: strong
- Continuation/re-engage: strong
- Objective-fight setup: strong
- Fallback floor: STABLE
- Collapse risk when ahead/even: LOW

### WBG
- Draft Execution Reliability: HIGH burden
- Independent forcing: limited/coupled
- Carry protection: weak
- Objective-fight setup from neutral/behind: fragile
- Fallback floor: FRAGILE/ABSENT
- Collapse risk: HIGH

## Correct market conclusion at 15:05

Despite WBG leading 5-3 and receiving +8.5 kills, the correct verdict should have been:

**PASS — WBG +8.5 kills @1.961 — 0u.**

The visible cushion was arithmetic, not mechanism safety. A HIGH-collapse-risk underdog can move from a favorable current margin to a double-digit final deficit in one or two failed forced sequences.

## Required correction

For underdog +kills, introduce **Draft Collapse Risk (DCR)** and **Fallback Floor (FF)**.

Classify DCR:
- LOW
- MEDIUM
- HIGH

Classify FF:
- STABLE
- FRAGILE
- ABSENT

A **HARD DRAFT-COLLAPSE VETO** activates when all are true at draft lock / first full post-draft assessment:

1. the side is the pregame/draft underdog by MKT/TEAM anchor;
2. DCR = HIGH;
3. FF = FRAGILE or ABSENT;
4. opponent has materially lower execution burden and at least one reliable independent forcing route plus continuation/re-engage or a second independent forcing route;
5. at least one scheduled objective/base-pressure sequence is expected to remain relevant if the favorite gains control.

When active, **underdog +kills is TAKE-INELIGIBLE FOR THE ENTIRE MAP.**

No exception may be created from:
- current kill lead/parity;
- current gold lead/parity;
- current tower/dragon parity;
- a widened +kills cushion;
- one or multiple return kills;
- two-snapshot temporal eligibility;
- temporary role-gold improvement;
- live odds movement;
- generic 'resilience proven' language.

The only permitted way to remove the hard veto is a **draft-input correction** that changes champion identity, role assignment, or the original matchup-functional DCR/FF classification. Ordinary live events do not remove it.

This hard veto applies only to the underdog +kills entry. It does not automatically qualify favorite -kills; the favorite handicap still requires signed-margin/NKB/RFI/KCV/Structure Substitution/probability qualification.

## Why this is a process-enforcement correction

v0.3.55 allowed sufficiently strong live mechanism proof to downgrade a draft-burden veto. NIP-WBG G1 shows that this is unsafe when the underdog's failure topology is fundamentally collapse-prone: successful return kills can occur without changing the composition's fallback floor.

Therefore v0.3.56 must supersede the live-proof override **for HIGH DCR + FRAGILE/ABSENT FF underdog +kills cases.**
