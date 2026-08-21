# Football Model Rules v0.2.49 — Team Goal/Concede Profile Weighting Gate

**Effective date:** 2026-08-21  
**Status:** Active audit rule  
**Supersedes:** v0.2.48 only where team scoring/conceding profile affects slate tier, remaining-goal burden, and live Over promotion. All synchronization, reset, provider-quality, style, settlement, timeliness, halftime-compression, protected-line, market-scan, Airtable and validator controls remain active.

## Trigger and process correction

The recent Salzburg, Nordsjælland–St. Gallen and Botafogo shadow losses exposed a recurring error:

`LIVE PRESSURE + MODERATE CHANCE QUALITY -> OVER PROMOTION`

was sometimes allowed to overpower a weaker underlying team scoring/conceding profile.

A team that is territorially dominant or producing shots is not automatically a strong multi-goal carrier. A matchup that looks active live is not automatically capable of funding a large remaining goal budget.

From v0.2.49 onward, **team goals-for and goals-against profile is a major prior and an explicit live promotion gate.**

## 1. Team profile must be established before serious Over promotion

For every serious slate candidate and every live Over candidate with meaningful remaining-goal burden, maintain a compact profile for both teams.

At minimum evaluate:

### Attacking profile

- recent goals scored per match;
- frequency of scoring 2+ goals;
- frequency of scoring 3+ goals;
- frequency of failing to score or being held to exactly one;
- home/away split where relevant;
- strength of opposition faced;
- competition/format context;
- current attacking lineup quality and missing scorers/creators;
- whether multi-goal output is repeatable or driven by a small number of outlier matches.

### Defensive profile

- recent goals conceded per match;
- frequency of conceding 2+ goals;
- frequency of conceding 3+ goals;
- clean-sheet / one-goal concession tendency;
- home/away split where relevant;
- strength of opposition faced;
- defensive lineup absences and goalkeeper quality/context;
- whether heavy concessions are repeatable or outlier-driven.

Do not use raw season averages without opponent/competition context when the matchup is materially different from the team's normal schedule.

## 2. Goal-route matrix

Before assigning or retaining an Over-friendly tier, explicitly compare four routes:

1. Stronger-team goals-for profile vs weaker-team goals-against profile.
2. Weaker-team goals-for profile vs stronger-team goals-against profile.
3. Stronger-team multi-goal frequency vs opponent multi-goal concession frequency.
4. Two-sided contribution probability vs one-team carrier probability.

A one-team route remains valid, but it must now be supported by **historical/structural multi-goal capacity**, not merely badge strength, possession, shot count or forced-chase incentive.

## 3. Revised T1 dominant-carrier gate

A team should not receive a strong T1 dominant-carrier classification unless its matchup profile supports a credible solo 3+ route.

T1 normally requires:

- strong recent multi-goal scoring frequency relative to opponent level;
- opponent with meaningful repeated 2+/3+ concession vulnerability, or a clearly exceptional talent/competition mismatch;
- attacking lineup capable of sustaining output;
- no major format/incentive drag;
- no strong evidence that the favorite commonly settles after taking the lead.

If the team's scoring profile is mostly 0-1 goal outcomes, or the opponent frequently limits stronger teams to 0-1, cap the matchup at **T2** unless extraordinary matchup evidence justifies otherwise.

A famous or strong team does not inherit T1 permanently.

## 4. Profile-support field for live Overs

Every serious live Over candidate must carry one of:

- `TEAM PROFILE SUPPORT: STRONG`
- `TEAM PROFILE SUPPORT: ACCEPTABLE`
- `TEAM PROFILE SUPPORT: CONFLICTING`
- `TEAM PROFILE SUPPORT: UNKNOWN`

### STRONG

Historical scoring/conceding tendencies materially support the exact remaining goal route.

### ACCEPTABLE

Profile does not strongly support the route but does not materially oppose it; live evidence may carry more weight.

### CONFLICTING

The required remaining goals materially exceed the teams' normal scoring/conceding behavior for this matchup class.

### UNKNOWN

Insufficient reliable profile information.

`CONFLICTING` or `UNKNOWN` cannot be ignored simply because live shots/SOT look strong.

## 5. Remaining-goal burden interaction

The larger the remaining goal burden, the more heavily profile support must weigh.

### One additional goal required

A strong current live state may be sufficient with ACCEPTABLE profile support.

### Two additional goals required

Normally require at least ACCEPTABLE profile support plus repeated live conversion-quality evidence.

If profile support is CONFLICTING, require exceptional live evidence and a protected line; otherwise HOLD.

### Three or more additional goals required

Normally require STRONG team-profile support plus a clearly re-accelerating live state. One upgraded snapshot is insufficient.

A forced-chase narrative, possession dominance or raw SOT volume cannot by itself justify a 3+ remaining-goal burden.

## 6. Post-goal interaction

After a goal, the normal reset still applies.

Team profile remains the structural prior, while post-goal behavior determines whether the live hazard is continuing, accelerating or compressing.

If the scoring team has a strong history of protecting one-goal leads or reducing attacking output after scoring, that must lower the Over promotion state unless fresh post-goal evidence clearly contradicts it.

If the trailing team has a strong chase/concede profile, that can support re-acceleration, but it is still not a substitute for current evidence.

## 7. Live evidence cannot fully erase profile conflict

Live evidence is still decisive for timing, but it must be interpreted through the structural profile.

Examples:

- 8 shots and 5 SOT from a team that rarely scores 2+ against comparable opponents should not be treated the same as 8 shots and 5 SOT from a proven multi-goal carrier.
- A big chance plus rising box entries may promote a STRONG-profile carrier quickly, but may only move a CONFLICTING-profile team from HOLD to closer watch.
- A weak defensive opponent that repeatedly concedes 2+/3+ can materially increase the value of the same attacking live evidence.

## 8. No fixed percentage weighting yet

Do not assign an arbitrary numeric percentage such as `40% profile / 60% live` until enough prospective audit data exists.

For now, profile is a **gating prior** whose burden increases with the number of remaining goals required.

This keeps the rule auditable without pretending an uncalibrated coefficient is statistically valid.

## 9. Required compact fields

For serious ranked or live Over candidates, add where data is available:

- `Team profile support:` STRONG / ACCEPTABLE / CONFLICTING / UNKNOWN
- `Primary carrier 2+ scoring tendency:` HIGH / MODERATE / LOW / UNKNOWN
- `Primary carrier 3+ scoring tendency:` HIGH / MODERATE / LOW / UNKNOWN
- `Opponent 2+ concession tendency:` HIGH / MODERATE / LOW / UNKNOWN
- `Opponent 3+ concession tendency:` HIGH / MODERATE / LOW / UNKNOWN
- `Opponent contribution route:` STRONG / PLAUSIBLE / WEAK / UNKNOWN
- `Post-lead behavior:` CONTINUES / MIXED / PROTECTS / UNKNOWN

These are structural priors, not independent live evidence channels.

## 10. Validator rule

For an Over PASS, the validator must now ask:

`Does the team goals-for / goals-against profile support the exact remaining goal burden?`

If the answer is materially conflicting and the live state is not exceptional enough to overcome that conflict, output:

`NO BET — HOLD — team-profile burden not cleared`

## 11. Operating principle

**Treat goals-for and goals-against profile as structural evidence, not decoration. A team's live pressure only matters in proportion to its demonstrated ability to turn that pressure into multiple goals, and the opponent's demonstrated tendency to allow them. The higher the remaining goal burden, the heavier the profile gate.**