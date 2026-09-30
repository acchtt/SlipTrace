# 02 — Normal Chat: Football C XI + Odds

Read upstream `models/football/CURRENT_MODEL.md` first, then load `models/football/production/FOOTBALL_C.md`.

Football C is the active official model.

The user normally supplies confirmed XI and current executable Asian-total odds. Treat that supplied quote as the executable evidence for the current epoch; do not ask for a second price confirmation.

## Intake

For each supplied match:
1. retrieve the frozen Football C board state only;
2. verify identity/status;
3. inspect the confirmed XI and map changes to route functions;
4. run **MANDATORY FRESH POST-XI FOOTBALL WEB RESEARCH** for the current XI epoch;
5. perform/recheck relevant H2H/matchup context;
6. interpret the current executable market;
7. issue exactly one final action:
   - `C-BET`
   - `C-WAIT`
   - `C-PASS`

Do not run Football A's PRE compiler or Step-2 compiler.

## Mandatory research invariant

A final prematch `C-BET` requires a fresh fixture-specific public-web football research attempt after the XI first pass.

Persist one of:
- `POST-XI RESEARCH = FOUND`
- `POST-XI RESEARCH = LIMITED`
- `POST-XI RESEARCH = UNAVAILABLE — ATTEMPTED`

Odds/history lookup does **not** satisfy the football-research gate.

Research should target football information that can change the mechanism: current form with context, chance quality, role/absence effects, tactical/incentive state, current lineup news and transferable matchup evidence.

## Integrated decision

Use the C-supported burden as the anchor.

### Market above burden
Do not buy unsupported extra burden. WAIT only if the protected target can realistically arrive without requiring thesis deterioration; otherwise PASS.

### Market below burden
Treat the undercut as a warning. Look for a football reason. If a current mechanism supports the pessimism, downgrade/PASS. If not, the lower line may be valuable protection.

### Price
- >=1.65 normal zone;
- 1.60–1.64 soft zone only for top-ranked C-FOCUS at/below supported burden with no material football veto;
- <1.60 normally WAIT/PASS.

## C-WAIT

Every WAIT must state:
- target line;
- minimum odds;
- cancellation event;
- thesis-health evidence required at target.

Do not create a wait plan that is expected to become executable only after the match supplies negative football information.

## Output

Use:

`#<rank> MATCH — C-BET / C-WAIT / C-PASS`

Then:
- XI: PRESERVED / DEGRADED / BROKEN
- POST-XI RESEARCH status
- H2H: compact material state
- Supported line
- Current line/odds
- Integrated reason
- WAIT target/cancellation/thesis-health requirement if applicable

## Persistence

Model identifier: `Football C`.

Every material C decision goes to Decision States.

For `C-BET`:
1. persist Decision State;
2. publish Website Pick;
3. reconcile fixture/model/line/odds/stake/timestamp/evidence epoch;
4. verify no duplicate active official pick.

For C-WAIT/C-PASS: Decision State only.

Do not modify historical Football A records.

If persistence surfaces disagree after a C-BET, report:
`PERSISTENCE SYNC FAULT — EXPOSURE STATE UNCERTAIN`

Actual user bet slips remain authoritative for what was physically placed.


## Deterministic engine comparison — mandatory shadow validation

After XI/research/H2H judgments and the current quote are frozen, serialize the same match into:

`models/football/engine/schema.json`

Use:
- `schema_version = football-engine-v1`
- `stage = decision`
- `model = c`

The `match` object must use the same structured football fields frozen by the research layer.

The `context` object must contain:
- board_state
- thesis_state = PRESERVED / DEGRADED / BROKEN
- quote.line
- quote.odds
- top_ranked_focus
- primary_mechanism_intact
- wait_reachable
- wait_requires_negative_info
- material_veto

The research layer decides these football/context inputs. The code only applies deterministic execution rules.

When a Python/runtime surface is available, execute:

`python models/football/engine/cli.py decision --input <decision_input.json>`

Then compare:
- prose action: C-BET / C-WAIT / C-PASS
- coded action: BET / WAIT / PASS

If they disagree, do **not** silently make them agree. Report:

`ENGINE DISAGREEMENT — TEXT=<...> CODE=<...>`

and preserve the exact structured input for audit.

During this initial validation phase, the coded result is a shadow validator. The active text Football C decision remains the production decision until a separate promotion decision explicitly changes authority.

### Required machine-readable appendix

For every Step-2 assessment include:

`FOOTBALL_ENGINE_DECISION_INPUT`

and, when executed:

`FOOTBALL_ENGINE_DECISION_RESULT`

If runtime execution is unavailable:

`ENGINE NOT EXECUTED — STRUCTURED INPUT PRESERVED`
