# Football Model Rules v0.2.48 — Dominant Goal-Carrier Slate Priority and Monitoring Allocation

**Effective date:** 2026-08-21  
**Status:** Active audit rule  
**Supersedes:** v0.2.47 only for pre-match slate ranking, match-monitoring priority, and one-team goal-carrier classification. All live synchronization, reset, style, provider-quality, settlement, timeliness, validator, audit-mode, halftime-compression and goal-budget controls remain active.

## Trigger and process correction

The 2026-08-20 European slate review exposed a selection-allocation error:

`GOOD/NOTABLE TEAM -> RANKED HIGH FOR OVER MONITORING`

was being treated too similarly to:

`ELITE OR NEAR-ELITE ATTACKING FAVORITE VS CLEARLY WEAKER OPPOSITION -> CAN FUND THE TOTAL ALONE`.

Those are not the same profile.

The model spent too much monitoring attention on Tier-2/3 matches while stronger one-team blowout routes existed elsewhere on the slate. This rule corrects **which matches receive first attention**. It does not create automatic bets.

## 1. Separate club stature from goal-carrier class

Before ranking a slate, classify the strongest attacking side in each match by **goal-carrier capacity**, not simply reputation or league status.

### Tier 1 — Dominant Goal Carrier

A Tier-1 goal carrier is a side that can plausibly produce **3+ goals by itself** in the current matchup.

The classification should normally be supported by several of the following:

- elite or near-elite attacking quality relative to the opponent;
- clear squad/talent mismatch;
- strong attacking starters actually available or expected to start;
- opponent defensive weakness, depth disadvantage, or lower competition level;
- tactical matchup that permits sustained territorial occupation, transition access, or repeated box entries;
- competitive incentive that does not strongly suppress attacking intent;
- a market total/handicap consistent with meaningful mismatch rather than a merely famous badge.

Examples of the **profile**, not permanent hard-coded membership: Ajax-, Benfica-, Beşiktaş-type mismatches against materially weaker opposition.

A famous name alone is insufficient. Tier assignment is matchup-specific and must be made prospectively.

### Tier 2 — Strong Attacking Side / Secondary Carrier

A good European or domestic side with meaningful attacking quality but a less reliable 3+ goal solo path in the current matchup.

Examples of the profile may include Salzburg-, Copenhagen-, Midtjylland-, Nordsjælland-type situations when the mismatch or attacking ceiling is less decisive.

Tier 2 can still rank first when no Tier-1 candidate exists.

### Tier 3 — Two-Sided / Shared-Route Over

The Over case depends materially on both teams contributing, game-state exchange, transition openness, or balanced chance generation rather than one dominant carrier.

Tier 3 can be an excellent live betting environment, but it receives lower **initial monitoring priority** than a strong Tier-1 mismatch unless live evidence later promotes it.

## 2. One-team Over route is fully valid

A total does not require both teams to contribute.

If one team has a credible route to fund the required goal budget by itself, opponent attacking weakness does not invalidate the Over thesis.

For slate ranking, explicitly ask:

`Can the stronger side reasonably score enough by itself to cash the target total?`

This question must be answered before penalizing a match because the underdog may contribute little.

Live promotion still requires evidence appropriate to the exact remaining goal budget. One-team carrier status is a prior, not a substitute for live proof.

## 3. Slate ranking order

When preparing a multi-match slate, rank in this order unless matchup-specific evidence clearly overrides it:

1. **Tier-1 dominant goal-carrier mismatches** with strong lineups and acceptable format/incentive.
2. Tier-1 profiles with one material uncertainty, such as rotation or first-leg suppression risk.
3. Tier-2 strong attacking favorites with a credible but less reliable solo route.
4. High-quality Tier-3 two-sided open matches.
5. Lower-information or lower-provider-quality matches.

Do not rank a Tier-2/3 match above a clear Tier-1 carrier merely because the Tier-2/3 game looks more balanced or theoretically open.

## 4. Monitoring allocation rule

Ranking must control attention, not just produce a list.

When several matches overlap:

- Tier-1 carrier matches receive the **first live checkpoint and primary monitoring slot**.
- If a Tier-2/3 match remains unproven while a Tier-1 match is starting, do not keep the Tier-2/3 match as primary merely because more time has already been invested in it.
- A Tier-2/3 match may retain priority only if it has already reached a materially stronger synchronized live state than the incoming Tier-1 candidate.
- Do not spend repeated checkpoints trying to rescue a weakly converting Tier-2/3 thesis while higher-priority carrier matches are going unmonitored.

This is an anti-sunk-cost rule for slate coverage.

## 5. Tier-1 does not mean automatic Over

Tier classification affects **which match is watched first**, not whether a bet is issued.

All existing live gates remain mandatory:

- current score/minute/line/odds synchronization;
- style and personnel verification;
- provider quality;
- primary-evidence independence;
- conversion quality;
- exact remaining-goal budget;
- protected-line comparison;
- NO-BET comparator;
- reset handling;
- v0.2.47 halftime compression where applicable;
- Airtable Decision State and Validator PASS in audit mode.

A Tier-1 match can still be `NO BET — HOLD` or `NO BET` if live threat does not materialize.

## 6. Prematch ranking fields

For each serious Over-ranking candidate, record compactly:

- `Goal-carrier tier:` T1 / T2 / T3
- `Primary carrier:` team or shared
- `Solo 3+ route:` STRONG / PLAUSIBLE / WEAK
- `Opponent mismatch:` STRONG / MODERATE / LOW
- `Lineup attack status:` FULL / ACCEPTABLE / ROTATED / UNKNOWN
- `Format/incentive drag:` LOW / MODERATE / HIGH
- `Initial monitoring priority:` rank number

These are ranking fields, not live evidence channels.

## 7. Separate ranking performance from entry performance

Track two independent audit outputs:

### A. Match-selection / ranking tracker

For the pre-match ranked slate, record at minimum:

- final total goals;
- whether O2.5 would have won;
- Tier-1 carrier team final goals where applicable;
- whether the match produced 3+ and 4+ total goals;
- the prospectively assigned tier and rank.

This measures whether the model is selecting the right **goal environments**, even if no live bet is issued.

### B. Shadow-entry tracker

Continue to track only prospectively issued PASS entries with exact line, odds, stake, timing and settlement.

Do not merge missed high-scoring matches into shadow P/L. A correct ranking with no valid entry is a selection success and an execution miss, not a betting win.

## 8. Anti-hindsight control

Tier labels must be assigned before kickoff or before the result is known.

Do not upgrade a team to Tier 1 because it later scored 4-6 goals. Do not downgrade a Tier-1 carrier solely because one match finished 1-0.

Review tier quality over a sample, not one outcome.

## 9. Interaction with v0.2.45 and one-team funding

v0.2.45 already established that a leader may fund the remaining Over budget itself in appropriate live states.

v0.2.48 extends that logic **upstream to slate selection**:

- a credible one-team funding route should raise monitoring priority;
- lack of opponent contribution should not automatically demote the match;
- the stronger the solo goal-carrier route, the less necessary a two-sided prematch narrative becomes.

This does not reduce the live evidence standard.

## 10. Operating principle

**Rank goal carriers, not badges. Allocate attention to the strongest prospective 3+ goal route first. A one-team blowout path is a first-class Over environment. Balanced openness is secondary when a materially stronger solo carrier exists. Then let the live validator decide whether the market is actually playable.**