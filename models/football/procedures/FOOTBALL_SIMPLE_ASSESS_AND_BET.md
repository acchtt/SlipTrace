# Football v2 — Simple /xi assess-and-price procedure

This is the operational procedure behind the one user-facing /xi command.

## Principle

Football comes first. Price is optional.

A match can be fully assessed by C and C2 without bookmaker odds. If an
observed price already exists, compare it. If a genuinely executable current
price also satisfies the strict execution contract, authorize that separately.

Do not make price availability a prerequisite for football assessment.

## Routine authority

For a routine V4 board match, verify:

- sealed V4 rank receipt;
- V4_RANK_PERSISTENCE_VERIFIED receipt;
- exact board row.

That is enough Step-1 provenance for /xi. Do not replay source.json or the
rank-time status payload again at Step 2.

For an explicit /xi exception, use current independent C/C2 football evidence
without routine board authority.

## Football assessment

Freeze the current factual match state once and run C and C2 independently.

Required factual work includes fixture state, current team/XI/mechanism
information where available, routes/carrier/chance/failure evidence, relevant
H2H, and competition incentive state where applicable.

Odds are not required.

After kickoff, include current score/minute/material events and continue the
football assessment. Never create a retrospective prematch action.

## One quote policy

The active model has one price-policy implementation:

- core.evaluate_c_quote()
- core.evaluate_c2_quote()

Strict run_decision() uses those same functions after validating execution
requirements.

Observed/screenshot comparisons use adapter.evaluate_observed_quote(), which
also uses those same functions but explicitly has no execution authority.

There must not be a second screenshot-specific ACT/WAIT/PASS rule.

## User screenshot

Treat the exact screenshot as the quote observation.

- Do not search for another price.
- Do not re-time the screenshot.
- Do not infer that the offer is still open.
- Do not ask for another screenshot merely because the analysis took time.

A screenshot can produce a conditional model ACT, WAIT or PASS, but never an
executable C bet by itself.

Persist its evaluated line/odds using the normal Decision State fields. No
special Evidence Summary JSON marker is required.

## WAIT

WAIT must be researched, not manufactured.

The football payload should state for each model whether the target is
reachable and why. A healthy WAIT requires:

- wait_reachable=true;
- a real reachability basis;
- wait_requires_negative_info=false;
- intact football thesis/mechanism;
- no material veto.

There is no fixed +0.75 or other wrapper-only market-gap rule.

The core returns the model target/minimum:

- normal minimum 1.65;
- top-ranked FOCUS soft-zone minimum 1.60 where the model policy permits.

WAIT creates no exposure merely by being declared. WATCH also creates no
synthetic exposure.

If the match changes materially before the target is reached, reassess.

## Strict executable price

A strict current price decision is allowed only when the stage=decision
contract has real current execution evidence.

The strict result may be C-BET, C-WAIT or C-PASS and an independent C2 shadow
action.

If strict pricing fails, keep the completed football assessment and state the
price blocker. Do not downgrade the football engine to failed.

A strict result is not published until its exact Decision State is independently
read back and the final quote/fixture/evidence epoch remains current.

## Persistence

Use one Decision State write/readback for the assessment.

For observed-price assessments, refetch the ordinary evaluated line/odds and
the exact C/C2 football results.

For strict decisions, persist the strict pair results and verify them once
before publication.

C2 never creates a Website Pick.

## Accounting

Prospective active accounting uses actual observed terms only.

- WATCH -> no exposure.
- unresolved WAIT -> no exposure.
- strict direct BET -> model accounting may use the actual line/odds.
- confirmed reached WAIT -> may be reconciled from the confirmed reached terms.

This model accounting is separate from the user's physical betting ledger.

User P/L is authoritative only from user-confirmed Actual Bets — Current rows.

## User-facing output

Give the verdict first.

If an observed quote exists:
- ACT — line/price acceptable under model policy;
- WAIT — target + minimum price + reachability basis;
- PASS — current quote/model state does not qualify.

Then clearly label whether the result is:
- observed/conditional only;
- strict executable-price decision awaiting/finalizing persistence;
- football-only with No bet price checked.

Do not expose internal workflow labels unless they explain a real blocker.
