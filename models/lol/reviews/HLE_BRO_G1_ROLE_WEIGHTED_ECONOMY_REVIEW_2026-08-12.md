# HLE vs BRO G1 — Role-Weighted Economy Review — 2026-08-12

## Scope

Reference map: LCK CL, HLE Challengers vs BRO Challengers, Game 1.

Confirmed shadow entries:
- `POSTCB-SHADOW-29-P01` — Over 34 minutes @1.877 — WIN +0.21925u
- `POSTCB-SHADOW-30-P01` — HLE ML @5.952 — LOSS -0.25u

User settlement authority: **BRO won**.

## Decision-state error

At the 36:09 HLE ML entry, the model summarized the map as approximately team-gold neutral and over-weighted HLE's 13-7 kill lead / apparent comeback path.

That representation discarded important information already visible in the role-level economy:

- BRO K'Sante held a large top-side economy advantage (about +1.5k in the visible role comparison).
- BRO Corki held a large carry economy advantage (about +2.1k).
- HLE's largest advantage was concentrated on Vi (about +2.5k), with smaller advantages on utility/engage pieces.
- BRO simultaneously held 4 dragons and Baron.

The raw team-gold number therefore understated BRO's effective late-game control. BRO's economy was concentrated on champions with stronger terminal damage / side-lane conversion value, while a material share of HLE's advantage sat on engage/utility.

## Deterministic correctness issue

This is treated as a **state-representation bug**, not a one-map directional heuristic:

> When role-level gold is visible, collapsing the state to total team gold alone loses decision-relevant information.

The correction is therefore eligible under the deterministic correctness exception in v0.3.53 change control.

## Correction

Add mandatory **Role-Weighted Economy (RWE)** for live ML and late-game repricing.

RWE has three steps:

1. **Role Gold Vector (RGV)** — record the visible gold advantage by role/champion pair rather than only net team gold.
2. **Gold Leverage Class (GLC)** — classify where that gold sits:
   - `HIGH`: primary DPS/scaling carry, terminal side-lane threat, or champion whose extra economy directly increases objective/fight closing power;
   - `MEDIUM`: secondary carry/bruiser or mixed damage/utility;
   - `LOW`: primarily engage, tank, or utility where extra gold has lower marginal closing value.
3. **Gold Concentration Quality (GCQ)** — determine whether one side's economy is concentrated on HIGH-leverage champions while the opponent's is concentrated on MEDIUM/LOW-leverage champions.

No fixed universal numeric role weights are introduced yet; classification is champion/function specific to avoid overfitting static role labels.

## Mandatory late-game interaction

After 30:00, RWE must be combined with objective terminality.

A comeback ML against a side holding major terminal objective control (for example soul/4 dragons, Baron, inhibitor/base access) must be downgraded further when that side also has positive GCQ on HIGH-leverage champions.

Kill lead alone cannot offset this combination.

## Practical veto

For live ML after 30:00:

- if raw team gold is near even but RGV/GCQ materially favors one side, do **not** call the state economically neutral;
- if opponent has both terminal objective control and HIGH-leverage gold concentration, require explicit observed evidence that those threats are being suppressed before taking the comeback side;
- if role-level economy is visible and not parsed, ML TAKE is ineligible;
- if role-level economy is unavailable, do not invent it; apply an uncertainty penalty instead.

## Expected effect

This correction should reduce false longshot-comeback ML entries where:

- kills make the trailing side look healthier than it is;
- raw team gold is deceptively close;
- the leading side's gold is concentrated on the champions best positioned to convert the next fight/objective;
- objective control has already become terminal or near-terminal.
