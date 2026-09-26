# Football Model QA and Promotion Procedure

**Purpose:** provide a reproducible promotion gate for permanent changes to
SlipTrace Football.

This procedure is **model-governance only**. It is not part of normal
match-by-match decision latency and does not override
`models/football/CURRENT_MODEL.md` during execution.

## 1. Scope

Apply this procedure to any proposed permanent change to:

- structural grading or ranking;
- route classification;
- supported burden or line selection;
- market-alignment / market-decomposition logic;
- HMA or other execution overlays;
- live-decay rules;
- league/scope rules;
- exposure gates;
- PASS rescue / carrier reopen logic;
- model version promotion.

Temporary user-authorized session overrides remain temporary unless separately
tested here.

## 2. Champion / challenger rule

The current official Football model is the **champion**.

Every proposed change is a **challenger** and must be evaluated against the
champion using the same frozen information available at the original decision
epoch.

Do not compare a challenger built with hindsight to a champion built in real
time.

## 3. Discovery vs holdout

The matches that caused a rule idea are the **discovery set**. They are useful
for diagnosis and rule design but have zero weight as prospective validation.

Promotion evidence begins only after:

1. the challenger is written;
2. its hypothesis is frozen;
3. eligibility and metrics are frozen;
4. the prospective start time is recorded.

## 4. Frozen experiment record

Create one experiment record from
`models/football/trials/FOOTBALL_MODEL_QA_EXPERIMENT_TEMPLATE.md`.

At minimum freeze:

- champion ID;
- challenger ID;
- exact rule delta;
- intended failure mode;
- discovery cases;
- eligibility universe;
- information/quote epoch;
- primary metric;
- guardrails;
- subgroup cuts;
- minimum evidence target;
- stop conditions.

Changing these after outcomes begin invalidates confirmatory status. Continue
only as exploratory or restart a new challenger ID.

## 5. Required event ledger

For every eligible fixture preserve:

- fixture identity and decision timestamp;
- structural grade/rank;
- route class and carrier state;
- supported burden;
- XI state;
- market center, offered line, offered odds;
- execution class and exposure decision;
- live-decay target/price when applicable;
- champion action;
- challenger action;
- final score and settlement;
- closing line/price when actually captured.

Record non-exposures too. Evaluating only placed bets creates selection bias.

## 6. Metrics

### Required
- eligible opportunities;
- settled exposure differences;
- W/HW/P/HL/L counts where applicable;
- unit return and yield;
- average odds and line;
- maximum drawdown;
- coverage/exposure-rate delta;
- paired champion/challenger decision matrix;
- time-block stability.

### Football-specific
- A1/A2/B+/B/PASS performance;
- practical-rank monotonicity;
- two-sided vs carrier-led;
- VERIFIED vs CANDIDATE/UNVERIFIED carrier;
- burden bucket;
- odds bucket;
- prematch vs live-decay;
- decay target reached before score-epoch invalidation;
- market-under/over-alignment states;
- competition regime.

### Optional
- closing-line/price value when captured contemporaneously;
- bootstrap confidence intervals for return/decision deltas;
- explicit probability calibration only if the model later emits real
  probabilities.

Do not manufacture probabilities from qualitative grades.

## 7. Evidence stages

- **Discovery:** design only.
- **Shadow:** prospective, no challenger-created official exposure. Prefer >=40
  eligible decisions and >=20 settled exposure differences.
- **Provisional:** prefer >=75 eligible and >=40 settled differences across
  multiple dates/regimes.
- **Promotion candidate:** normally >=150 eligible and >=75 settled
  differences, or a longer sparse-rule window with equivalent evidence.

Counts are minimum governance targets, not substitutes for uncertainty
analysis. High-variance or broad rules may require more.

Only a pure risk-tightening quarantine may be adopted earlier, with an expiry
and mandatory review. Exposure-expanding rules may not bypass prospective
validation.

## 8. Promotion decision

A permanent rule change must satisfy all of the following:

- prospective contract existed before holdout outcomes;
- discovery cases excluded from confirmatory evidence;
- reproducible champion/challenger replay;
- no decision-time data leakage;
- appropriate evidence stage met;
- primary metric materially improved or predeclared failure mode materially
  reduced;
- no unacceptable deterioration in drawdown, exposure quality, burden
  protection, or coverage;
- effect stable enough across time and not dominated by one regime;
- exact tested rule matches exact proposed rule;
- known regressions and opportunity costs documented.

Valid outcomes:

- `PROMOTE`
- `KEEP SHADOW`
- `NARROW AND RETEST`
- `REJECT`

There is no "promote because recent examples look convincing" state.

## 9. Patch discipline

Prefer one material rule change per challenger.

If several changes are inseparable, freeze them as one bundle and do not claim
which component caused the result.

A failed challenger must not be silently rewritten and continue under the same
experiment ID. Create a new challenger and new prospective window.

## 10. Historical integrity

Never rewrite historical model decisions to match a newer rule.

Permanent promotion is prospective from its declared effective timestamp.
Historical records remain bound to the model/version that produced them.

## 11. Operational compliance fixes vs model changes

Not every QA failure requires a new model challenger.

A change that merely enforces an already-active authoritative rule is a **PROCESS COMPLIANCE FIX** and may be applied immediately without pretending it is a newly validated predictive edge. Examples:

- enforcing carrier-decomposition precedence that the current carrier patch already requires;
- distinguishing old-quote invalidation from predeclared-plan invalidation after a goal;
- enforcing the existing 1.65 price floor;
- enforcing near-kickoff AiScore identity checks;
- requiring complete synchronized persistence fields.

A change that alters a predictive threshold, expands exposure eligibility, changes a carrier trigger, lowers the price floor, changes supported burden, or materially changes promotion/exposure logic remains a **MODEL CHANGE** and must use the champion/challenger procedure above.

Operational QA should therefore classify every proposed repair as exactly one of:

- `PROCESS COMPLIANCE FIX`;
- `RISK-TIGHTENING QUARANTINE`;
- `MODEL CHALLENGER REQUIRED`.

### Deterministic execution-QA assertions

The active execution tester should fail process compliance when any of the following occurs:

- ELITE/EXTREME carrier + unreachable decay gap is sent to generic WAIT without the carrier override review;
- first goal mechanically voids the entire predeclared decay plan rather than triggering state-integrity recheck;
- official exposure is published with unresolved fixture/home-away/kickoff/status conflict;
- official line is below the active price floor;
- market strength creates structure without football/PRE support;
- Decision State or Website Pick lacks its required timestamp;
- Decision State and Website Pick disagree on fixture, model, line or odds;
- an exposure is backfilled after the executable quote/state has changed.

These assertions judge whether the active model was followed; they do not use final score as proof that a bet should or should not have been placed.

## 12. Live execution boundary

QA work must not delay a current live verdict. The active model's
`LIVE VERDICT-FIRST / EXECUTION LATENCY CONTROL` remains authoritative.

If QA is requested during a live decision, first complete the active verdict,
then perform model-governance analysis on the persisted state.
