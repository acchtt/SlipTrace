# 02 — Normal Chat: XI + Market Review

Use Normal Chat with high reasoning.

## Authority
Read `models/football/CURRENT_MODEL.md` first. It defines the active official model, active patches, canonical time rules, and load order. Never infer the current version from this prompt.

Then load the current stage-relevant execution files declared by `CURRENT_MODEL.md`, including the betting procedure, active official rule files, time/schedule integrity, coverage contract, and Decision States contract. If an older procedure contains an older version label, `CURRENT_MODEL.md` has higher authority.

## Airtable
Base ID `appWyZJjitSBATXAU`.
Daily Coverage Ledger `tblcl1UAyMqZT6Ub0`.
Decision States `tblQmUpd5WjBLQ38X`.
Website Picks `tblg3J5sbJYbzuTYD`.
Use the direct IDs unless one fails.

## Input
The user normally supplies the confirmed XI and current Asian-total line(s)/price(s). Do not automatically search for missing XI or price unless the user explicitly asks.

If required final input is missing, return the current model's waiting state and do not create a material final Decision State.

## Targeted read
Identify the fixture, then retrieve only that fixture's frozen PRE from Daily Coverage Ledger. Read the fields needed to preserve the original grade, structural type, board tier, scoring routes, failure mode, XI sensitivity, frozen burden, and time/status context.

Do not read the entire day's board unless the user asks for ranking/next-best comparison or the current procedure requires same-window comparison.

Near kickoff, follow the current time/schedule integrity procedure and revalidate fixture state when required.

## Decision sequence
Do not rebuild Work PRE from scratch. Start from frozen PRE and follow the current official execution order from `CURRENT_MODEL.md`.

At XI, assess creators/finishers, shape, defensive absences, rotation/cohesion, starter/bench quality, route survival, and failure-mode changes. Apply the current model's rotation interpretation rather than treating all rotation as negative.

After XI, classify whatever goal-burden/regime system the current official model declares. For any EGE/high-environment regime currently active, preserve the frozen PRE burden, document the new supported post-XI burden, state the independent structural/team/XI reasons, evaluate the failure mode, and only then compare the supplied market line/price. A high market line by itself cannot create the regime.

For STANDARD/normal states, keep the protected-line principle. Never move to a higher total merely to improve price.

Apply the current price policy from `CURRENT_MODEL.md` only after the supported burden/regime is fixed.

Run official and shadow comparisons only to the extent the current model/procedure requires for a material final assessment, keeping each track version-faithful.

## Persistence
For a material final assessment, update only the later-stage coverage status fields that belong there and write the current Decision State(s) according to the active Decision States contract. Do not rewrite frozen PRE history.

Use Website Picks only when an actual official final selection needs to be persisted under the current workflow. Do not touch it for simple waiting states.

## Output
Compactly return: match, frozen PRE, XI rerank, current goal regime/burden, best supported supplied line, price class, final action, concise reason, and Airtable persistence PASS/FAIL.