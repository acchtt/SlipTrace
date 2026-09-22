# Football A — B+ Protected-Line Execution Lane

**Status:** ACTIVE OFFICIAL PATCH  
**Track:** Football A only  
**Effective:** 2026-09-21 ICT, prospectively only  
**Scope:** B+ WATCHLIST fixtures at the exact frozen supported burden

## Purpose

The Sep 19–20 audit showed that Football A was frequently identifying useful B+ goal environments but Step 2 was demanding an extra positive hardener even when:

- the frozen PRE had already assigned a supported burden;
- the confirmed XI preserved the frozen scoring route(s);
- the exact frozen supported line was available at or above the hard price floor; and
- there was no strong mechanism-compatible negative veto.

This patch removes that extra proof requirement at the exact protected burden without promoting B+ structurally and without authorizing burden chasing.

## Core rule

For a frozen `B+ WATCHLIST` fixture, direct Football A exposure is allowed at the **exact frozen supported burden** when all of the following are true:

1. the fixture remains in scope and the frozen PRE is still valid;
2. confirmed XI materially preserves the frozen route construction;
3. the offered total is exactly the frozen supported burden;
4. decimal odds are **>= 1.65**;
5. the shared market-alignment gate is not unresolved/severely contradictory;
6. no strong current, mechanism-compatible negative veto is present.

When all six clear:

`B+ PROTECTED-LINE — DIRECT LOCK ELIGIBLE`

No additional positive hardener is required.

## Strong negative vetoes remain authoritative

A B+ protected line must still be held when there is strong current evidence of the frozen failure mode, including combinations such as:

- recent same-venue H2H suppression that matches the current tactical/control mechanism;
- carrier-control where the nominal route is repeatedly absent and the carrier lacks adequate self-funded ceiling;
- current low-urgency/control profile that directly matches the frozen failure branch;
- meaningful XI route damage;
- severe market undercut/conflict not resolved by football evidence;
- material fatigue/rotation/tactical factors that reduce the supported burden.

A historical H2H pattern alone is not sufficient. The suppression must be **recent/relevant and mechanism-compatible**.

## Burden discipline

This patch does **not** authorize automatic HMA for B+.

- Exact frozen supported burden: eligible under the core rule.
- `+0.25` above burden: allowed only for `CARRIER-LED / PROVEN+NOMINAL` when `PRACTICAL CARRIER CEILING — VERIFIED` is explicitly cleared under `MODEL_RULES_FOOTBALL_A_PRACTICAL_CEILING_RANKING.md` and no strong negative veto is present. `CANDIDATE` or generic `CARRIER-LED` is not enough.
- `+0.50` or more above burden: **never automatic** for B+; use WAIT/live-decay or HOLD.
- Price may never justify a higher burden.

## Execution states

Use:

- `B+ PROTECTED-LINE — DIRECT LOCK ELIGIBLE`
- `B+ PROTECTED-LINE — OFFICIAL LOCK`
- `B+ PROTECTED-LINE — HOLD — NEGATIVE VETO`
- `B+ ABOVE BURDEN — WAIT / LIVE DECAY`
- `B+ +0.25 CARRIER EXTENSION — DIRECT LOCK ELIGIBLE` only when the carrier-specific hardener clears

## Interaction with other Football A rules

This patch overrides earlier Football A wording that required a separate positive hardener for every B+ exposure **only at the exact frozen supported burden**.

It does not override:

- the shared A/B market-alignment gate;
- decay-first burden protection;
- the hard 1.65 odds floor;
- state-integrity requirements;
- no-retroactive-exposure rules;
- strong negative vetoes;
- the prohibition on automatic B+ HMA extension.

Structural ranking remains unchanged. B+ stays B+ WATCHLIST.

## Mandatory no-bet / wait reason taxonomy

Every B+ fixture that does not become an official exposure must persist **one primary execution reason**. Absence of a sportsbook ticket is never enough to infer why the bet was missed.

Use exactly one of:

1. `LINE NEVER REACHED — NO EXECUTION OPPORTUNITY`
   - the frozen/allowed target line at the required minimum price was not observed before the score epoch changed or the market closed;
   - use only when market-path evidence actually supports non-arrival.

2. `EXECUTABLE LINE AVAILABLE — MODEL HELD`
   - an exact supported or otherwise explicitly allowed line/price was observed, but the model withheld exposure for a structural/evidence rule;
   - this is the primary bucket for execution-policy false-negative auditing.

3. `+0.25 AVAILABLE — WAITED FOR LOWER BURDEN`
   - a +0.25 line was actually available at an acceptable price, but the model waited for the exact/lower burden;
   - record whether `PRACTICAL CARRIER CEILING — VERIFIED` was present. This is an opportunity-cost bucket, not automatic evidence that +0.25 should have been taken.

4. `STRONG VETO HOLD — EXECUTABLE PRICE REJECTED`
   - an otherwise executable line existed, but a current mechanism-compatible negative veto intentionally blocked exposure;
   - keep this separate from ordinary model-held cases so valid vetoes are not misclassified as missed bets.

5. `ABOVE BURDEN — NO QUALIFIED EXTENSION`
   - only +0.50 or larger, or an unqualified +0.25, was available;
   - do not call this a missed execution merely because the match later went Over.

When a goal or red card occurs before a waiting trigger, close the old score epoch and persist whether the target was reached **before** that state change.

## Audit

Track B+ protected-line exposures separately from A1/A2:

- exact supported-burden locks;
- negative-veto holds;
- carrier-specific +0.25 extensions;
- above-burden waits;
- outcomes and ROI versus A1/A2 groups.

Historical Sep 19–20 results remain audit evidence only and are not retroactively reclassified as official bets.
