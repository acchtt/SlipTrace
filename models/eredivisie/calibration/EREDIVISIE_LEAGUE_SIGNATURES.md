# Eredivisie League Signatures — v0.1 Provisional Register

**Status:** Active calibration evidence register  
**Model:** Eredivisie v0.1  
**As of:** 2026-08-15 before the Saturday Round 2 slate  
**Scope:** Dutch Eredivisie only

## Purpose

Maintain observable league-specific signatures separately from hard model rules.

A signature is an empirical pattern worth monitoring. It is **not** a stable prior until sample size, data quality and repeated evidence justify promotion. Early v0.1 signatures must widen or organize uncertainty, never create false precision or bypass the frozen football core and Eredivisie validator.

## Evidence universe at this snapshot

Descriptive current-season result universe available before the 2026-08-15 Saturday slate:

- 9 completed Round 1 matches from 2026-08-07 through 2026-08-09;
- Telstar 0-0 Sparta Rotterdam on 2026-08-14;
- total descriptive sample = 10 completed 2026/27 Eredivisie matches.

This descriptive result universe is **not the same as the 50-match assessed-model denominator**. Only matches with material model assessments count toward the assessed calibration target.

Observed results in the descriptive sample:

- SC Cambuur 0-4 Excelsior;
- N.E.C. Nijmegen 1-2 Telstar;
- Go Ahead Eagles 4-1 Willem II;
- PSV 2-2 Fortuna Sittard;
- AZ 2-0 ADO Den Haag;
- Sparta Rotterdam 0-1 Feyenoord;
- FC Groningen 2-1 FC Utrecht;
- PEC Zwolle 0-2 Ajax;
- sc Heerenveen 1-0 FC Twente;
- Telstar 0-0 Sparta Rotterdam.

Descriptive arithmetic from those ten matches:

- 25 total goals = 2.50 goals per match;
- Over 2.5 in 5/10;
- BTTS Yes in 4/10;
- home wins 4, away wins 4, draws 2;
- at least one clean sheet in 6/10 matches.

These figures are observations only. Ten matches are far too few to establish stable Eredivisie scoring, home-field or totals priors.

## Signature S1 — Favourite win and favourite margin are visibly distinct

**Status:** Provisional, high operational relevance because it reinforces an inherited core rule.

Opening evidence includes major favourite failures or margin shortfalls: N.E.C. lost at home to Telstar, PSV drew Fortuna, while Feyenoord and Ajax won without producing an automatic deep-margin result.

Operational use:

- keep win probability separate from exactly-one-goal and 2+ margin probability;
- require a repeated multi-goal route before deep favourite AH exposure;
- do not promote a favourite handicap from possession, reputation or market strength alone.

Forbidden interpretation:

- do not infer that Eredivisie favourites are systematically poor against the spread from this sample.

## Signature S2 — Promoted-team stress is present, but not yet a stable promoted-team prior

**Status:** Provisional / tiny sample.

The three 2026/27 promoted clubs — ADO Den Haag, SC Cambuur and Willem II — all lost their first Eredivisie match, with a combined first-match score of 1-10.

Operational use:

- explicitly test top-flight defensive speed, box resistance and adverse-state behaviour for promoted sides;
- widen uncertainty around promoted-team strength rather than importing Eerste Divisie dominance directly into Eredivisie probabilities.

Forbidden interpretation:

- do not automatically fade a promoted side or assume repeated multi-goal losses.

## Signature S3 — The early league is mixed rather than an automatic Over environment

**Status:** Provisional.

The first ten completed matches produced 2.50 goals per game, only 5/10 Over 2.5 and 4/10 BTTS Yes. The same window contains 4-1 and 2-2 matches alongside 1-0 and 0-0 outcomes.

Operational use:

- classify each match by its own event budget and scoring routes;
- separate raw Over likelihood from executable Over value;
- preserve the protected total line;
- if the natural protected Over is below 1.70, treat the odds floor as a veto rather than moving mechanically to O3/O3.5.

Forbidden interpretation:

- never use 'Eredivisie is high scoring' as a standalone primary channel.

## Signature S4 — Low-event and 0-0 branches are material enough to respect

**Status:** Provisional.

The sample includes two 1-0 finals and one 0-0 final, plus multiple 0-0 halftime states in Round 1. A short pre-match total does not eliminate a persistent low-event branch.

Operational use:

- price 0-0 at 15/20/30/HT explicitly as the calibration sample grows;
- require observed regime change before switching from a closed state to an Over;
- retain late-event and stoppage reserve rather than assuming a quiet match must mean-revert.

## Signature S5 — Underdog resistance and conversion can dominate raw volume

**Status:** Provisional, process-reinforcing.

N.E.C.–Telstar supplied an early example in which the stronger side generated large territorial and shot volume but lost 1-2. This reinforces the rule that possession, raw shots, SOT and xG-style volume cannot govern a thesis without forward-looking chance structure and margin analysis.

Operational use:

- distinguish territory from productive scoring access;
- evaluate goalkeeper/box resistance, transition routes and adverse-state behaviour;
- do not count correlated volume indicators as separate evidence channels.

## Signature S6 — Home-field effect is unresolved

**Status:** Unresolved.

Through the ten-match descriptive snapshot the result split is 4 home wins, 4 away wins and 2 draws.

Operational use:

- do not install a numeric 2026/27 home-field adjustment yet;
- continue recording home/away scoring, conceding, win and margin data until the sample is adequate.

## Signature S7 — Red-card favourite siege can become a real late-goal regime, but only after persistence

**Status:** Single-match branch observation, not a league prior.

PEC Zwolle–Ajax provided the first assessed example: a PEC red card created a reset, but the model correctly waited for sustained post-red Ajax box pressure and attacking personnel refresh before validating a new open regime. The later full-match Over 1.0 shadow selection passed only after post-red persistence and settled as a win in the 0-2 final.

Operational use:

- red card = reset, never automatic Over;
- require post-card paired snapshots and fresh persistence;
- compare protected total versus favourite side after the new regime resolves.

## Signature S8 — A trailing stronger side does not automatically create an Open regime

**Status:** Single-match branch observation.

sc Heerenveen–FC Twente showed that a trailing side can fail to convert chase incentives into productive pressure. Twente remained sterile for a monitored post-goal interval and the model correctly invalidated the earlier Over direction rather than assuming 'trailing favourite = goals'.

Operational use:

- measure chase quality through box/central access, SOT/chance quality, transitions, substitutions and persistence;
- pressure or urgency without productive forward channels is insufficient.

## Signature governance

1. Keep every signature labeled `Unresolved`, `Provisional`, `Supported` or `Stable`.
2. Do not promote a signature to a numeric prior from one or two matches.
3. Review signatures at the 10/20/30/40/50 completed-assessed-match checkpoints.
4. A signature may reinforce an inherited rule immediately, but a new Eredivisie structural rule requires repeated evidence and explicit version discipline.
5. Record contradictions as carefully as confirmations.
6. Separate descriptive league-result samples from the assessed-model calibration denominator.
7. When a signature is used in a match assessment, state whether it is only contextual/supporting or sufficiently established to count as a primary channel.

## Source provenance for this snapshot

- Eredivisie official competition/schedule material confirms the 2026/27 competition field and promoted-club context.
- SoccerPunter 2026/27 season results snapshot supplied the nine Round 1 scores and halftime states used in the descriptive arithmetic.
- The 2026-08-14 Telstar 0-0 Sparta Rotterdam result was independently verified before this register was created.
- Match-specific SlipTrace/Airtable records supply the assessed PEC Zwolle–Ajax and sc Heerenveen–FC Twente process observations.

This register should be updated with evidence, not hindsight narratives.