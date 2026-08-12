# Football Model Rules v0.2.43 — Mandatory Team Style and Post-Goal Behaviour

**Effective date:** 2026-08-12  
**Status:** Active audit rule  
**Supersedes:** prior football rules wherever they permit a prematch or live verdict without an explicit team-style and game-state-response assessment.

## Trigger

Recent live-total reviews showed that score state alone is too generic. A 1-0 lead does not have the same forward implication for every team. Some leaders continue to attack, some control possession, some retreat into a low block, and some remain dangerous only in transition. Likewise, trailing teams differ materially between aggressive chase, sterile possession, and structural collapse.

The model must therefore identify each team's expected style before kickoff and explicitly compare observed post-goal behaviour with that expectation after any goal.

## 1. Mandatory prematch style profile

Before any serious prematch recommendation, and before the first live recommendation in a match, create a profile for both teams using current, verifiable evidence.

For each team classify:

- build-up: short possession / mixed / direct;
- attacking route: central combinations / wide-overlap / crossing / transition / set-piece heavy / mixed;
- tempo: patient / balanced / high-tempo;
- defensive block: high press / mid-block / low block / mixed;
- transition behaviour: aggressive counterpress / fast counter / conservative recovery;
- chance-generation signature: sustained volume / selective high quality / low-volume efficiency / set-piece dependence;
- lead behaviour: front-foot leader / control leader / low-block protector / counter leader / unresolved;
- trailing behaviour: aggressive chaser / structured chaser / sterile chaser / collapse-prone / unresolved.

Do not infer these labels from club reputation alone. Use recent match evidence, tactical reporting, lineup/coach context and venue/opponent-strength splits where available.

## 2. Base style versus matchup style

Always distinguish:

- `Base style`: the team's normal structural behaviour;
- `Expected matchup style`: how that behaviour is likely to change against this opponent, at this venue, with these lineups and competition incentives.

A possession-dominant domestic favorite may become transition-oriented against stronger opposition. A low-block underdog may be forced into a higher-risk chase in a knockout tie. The matchup expectation controls the live baseline.

## 3. Mandatory post-goal profile

For each team, when evidence permits, summarize historical/recent response after:

1. scoring to take the lead;
2. scoring while already leading;
3. conceding to fall behind;
4. conceding while already behind.

Prioritize changes in:

- shots and shots on target per minute;
- box entries / inside-box attempts;
- possession and field tilt only as secondary context;
- transition frequency;
- corners/set-piece pressure;
- opponent shot/box production;
- next-goal direction;
- additional-goal frequency.

Where sample sizes are small, explicitly label the tendency `LOW CONFIDENCE` and shrink interpretation toward the team's broader seasonal/league baseline. Do not create a deterministic rule from a few matches.

## 4. Goal = mandatory style reset

Every goal triggers a full live reset.

After the goal, the first post-goal snapshot is observational unless the response is extreme and independently confirmed. The model must answer:

- Is the leader behaving as expected when ahead?
- Is the trailer chasing as expected?
- Is the leader still generating repeatable counter/positional threat?
- Is the trailer's increased possession producing actual attacking events, or only sterile circulation?
- Has either team materially deviated from its prematch style profile?

A live total or directional bet cannot be promoted solely from the generic statement that "the trailing team must chase" or "the leader will have counterattacks."

## 5. Post-goal persistence gate

After a goal, a new live shadow candidate normally requires at least two comparable post-goal observations or one observation plus clearly verified event-level evidence covering a meaningful interval.

For an Over candidate, require evidence for at least two of:

- trailing-team chase produces repeated box access or meaningful shots;
- leader continues to create transition or positional chances;
- defensive shape is visibly degrading;
- attacking substitutions reinforce the chase;
- set-piece pressure is repeatable;
- both teams retain independent scoring routes.

For an Under candidate, require evidence for at least two of:

- leader successfully suppresses central/box access;
- trailer's possession is sterile;
- transition frequency is low;
- both teams reduce attacking numbers/tempo;
- substitutions reinforce control rather than chase.

## 6. Style-deviation signal

Live behaviour that materially contradicts the prematch expectation is a first-class signal.

Examples:

- expected low-block protector remains aggressive at 1-0 -> positive Over deviation;
- expected aggressive chaser produces only harmless possession -> negative Over deviation;
- expected counter leader cannot escape or create transitions -> downgrade leader team total/Over;
- expected control leader becomes stretched and concedes repeated transitions -> upgrade volatility.

The model must state whether the observed behaviour is `AS EXPECTED`, `MORE OPEN THAN EXPECTED`, `MORE CLOSED THAN EXPECTED`, or `STYLE BREAK / UNRESOLVED`.

## 7. Strict prematch completion gate

A serious match preview is incomplete until both teams have:

- base style;
- expected matchup style;
- lead behaviour tendency;
- trailing behaviour tendency;
- confidence level and evidence caveat.

If this information cannot be verified adequately, output `STYLE PROFILE INCOMPLETE` and cap any prematch betting verdict at `NO BET — HOLD`. A later live verdict may proceed only if enough observed match evidence replaces the missing historical style information.

## 8. Strict live output fields

For every material live reassessment after a goal, include:

- `Prematch style expectation:`
- `Leader post-goal behaviour:`
- `Trailer post-goal behaviour:`
- `Style deviation:`
- `Post-goal persistence:`
- `Market implication:`

These fields are mandatory before any `SHADOW LEAN` or benchmark shadow is issued.

## 9. Interaction with xG/xGOT

xG and xGOT remain secondary diagnostics only. Team-style and post-goal behaviour must be supported primarily by actual sequences, shot/box access, transitions, set pieces, substitutions, defensive spacing and competition utility. If the xG provider is unreliable, discard it without weakening this rule.

## 10. Audit requirement

Track this layer prospectively. Do not backfill favorable style labels after seeing the result.

For every new shadow selection record:

- prematch style classifications;
- post-goal classification if applicable;
- whether the observed response matched expectation;
- whether the wager won/lost;
- whether style information improved or worsened the decision relative to a score-and-stats-only read.

Review after 20 qualifying live checkpoints with at least 10 post-goal states.

## Operating principle

Score state is not a tactical model. The model must know how these specific teams tend to react to the score state before converting that state into a betting thesis.
