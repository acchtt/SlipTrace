---
name: football-model-qa
description: >
  Independent QA and promotion workflow for SlipTrace Football. Use whenever a
  permanent football rule, threshold, ranking rule, execution rule, live-decay
  rule, market overlay, league exception, or model version is proposed,
  modified, promoted, retired, or compared against the current champion.
  Separates discovery evidence from prospective holdout evidence, freezes
  experiments before outcomes, compares champion vs challenger on the same
  opportunity universe, quantifies uncertainty, and blocks anecdotal rule
  promotion. Do not use for ordinary match-by-match execution unless the user
  is explicitly evaluating the model itself.
---

# Football Model QA

Use this skill as the independent validation layer for `models/football`.

The active betting model remains governed by `models/football/CURRENT_MODEL.md`.
This skill governs **how model changes earn promotion**. It does not alter a
live/prematch verdict by itself.

Authoritative procedure:
`models/football/procedures/FOOTBALL_MODEL_QA_AND_PROMOTION.md`

Experiment template:
`models/football/trials/FOOTBALL_MODEL_QA_EXPERIMENT_TEMPLATE.md`

## Non-negotiables

1. **Discovery is not validation.** Matches that motivated a rule belong to the
   discovery set and may not be counted as proof that the rule works.
2. **Freeze before outcomes.** Hypothesis, challenger logic, eligible universe,
   primary metrics, guardrails, and stop conditions must be written before the
   prospective test begins.
3. **One material change per challenger.** If several rules change together,
   attribution is lost. Split them unless they are inseparable by construction.
4. **Same information clock.** Champion and challenger must see the same
   fixture identity, PRE evidence, XI state, market snapshot, timestamp, and
   source availability for each comparison.
5. **No hindsight reconstruction.** Never rebuild a PRE state after the result
   is known. Preserve the exact frozen state that existed at decision time.
6. **No sample-size theatre.** Report counts for eligible fixtures, qualified
   fixtures, executable quotes, exposures, pushes, wins, and losses separately.
7. **No ROI-only promotion.** Yield can be dominated by variance. Pair it with
   coverage, line quality, drawdown, route/regime stability, and uncertainty.
8. **No fabricated calibration.** Brier/log loss require explicit model
   probabilities. Do not convert A1/A2/B+ grades into fake probabilities.
9. **Subgroup results are exploratory unless predeclared.** League, grade,
   carrier/two-sided, odds, total, and live-decay slices must be labeled
   exploratory unless included in the frozen plan.
10. **Tightening rules may ship as safety quarantine; expansion rules may not.**
    A rule that only blocks exposure can be adopted provisionally with an
    explicit review date. A rule that creates new exposure must earn
    prospective evidence.

## Experiment contract

Before running a challenger, record:

- champion version/commit;
- challenger identifier and exact changed rule;
- hypothesis and expected failure mode addressed;
- discovery matches that motivated it;
- prospective start timestamp and minimum observation window;
- eligible fixture definition;
- information snapshot / quote epoch rules;
- primary metric;
- secondary metrics;
- harm guardrails;
- predeclared subgroup cuts;
- minimum evidence target;
- stop / quarantine conditions.

Use the experiment template. A result without a frozen contract is a
retrospective analysis, not promotion evidence.

## Football-specific evaluation dimensions

Always preserve enough fields to evaluate:

- Structural Rank and grade: A1 / A2 / B+ / B / PASS;
- execution class and exposure decision;
- route type: two-sided / carrier-led / fragile / other;
- carrier verification state;
- supported burden and selected line;
- offered odds and market center;
- prematch vs live-decay execution;
- decay target, whether it became available, and whether a goal invalidated the
  quote first;
- league / competition regime;
- XI preservation / downgrade state;
- market alignment / undercut / high-market conflict state;
- final score and settlement result;
- closing line/price when available.

## Primary metrics

Choose **one** before the test. Good defaults:

- unit-return / yield delta on the frozen eligible opportunity universe;
- protected-line settlement value at a fixed execution policy;
- decision-quality delta for a specific rule (for example, avoided bad
  exposures minus missed good exposures).

Always report alongside it:

- number of eligible opportunities;
- number of actual exposures;
- win / half-win / push / half-loss / loss counts where relevant;
- average odds and total line;
- maximum drawdown for the experiment sequence;
- coverage change vs champion;
- paired champion-vs-challenger outcome table;
- bootstrap interval for the primary delta when sample size permits.

If closing-market data exists, report closing-line/price value as an additional
signal. Never invent it from later screenshots or memory.

If explicit probabilities are introduced later, add Brier score, log loss and
reliability curves; until then, use grade/rank monotonicity instead of fake
probability calibration.

## Structural calibration checks

The model should become more selective in a useful direction, not merely more
complex. Check:

- Does A1 outperform A2, and A2 outperform B+/lower states on the chosen
  decision metric over enough observations?
- Do `VERIFIED` carriers outperform `CANDIDATE/UNVERIFIED` carriers?
- Does the practical-ceiling rank ordering show monotonic value?
- Are two-sided and carrier-led lanes stable across time rather than driven by
  one league or one weekend?
- Are B+ rescue and protected-line lanes actually adding value after accounting
  for extra exposure?
- Do live-decay plans reach the frozen target often enough to justify waiting,
  and how often does an early goal invalidate the plan first?
- Are high-market / market-decomposition overrides improving decisions or only
  rationalizing higher burdens?

## Evidence stages

Use these as governance stages, not magic significance thresholds:

### 1. Discovery
Rule idea may be written. No promotion claim.

### 2. Shadow
Run prospectively with no official exposure created by the challenger.
Preferred minimum: at least 40 eligible decisions and 20 settled exposure
differences before drawing even a provisional performance conclusion.

### 3. Provisional
At least 75 eligible decisions and 40 settled exposure differences, across
multiple dates and more than one competition regime where the rule claims to
generalize. Primary result must not show material harm and guardrails must hold.

### 4. Promotion candidate
Normally target at least 150 eligible decisions and 75 settled exposure
differences, or a longer time-window equivalent for sparse rules. Require
stable direction across time blocks and no single league/regime dominating the
effect. If the rule is narrower than this sample target can support, keep it
narrow rather than extrapolating.

These counts can be raised when variance is high. They may be lowered only for
a **risk-tightening quarantine rule**, never to justify new exposure.

## Promotion gate

A challenger may be recommended for permanent promotion only when all are true:

- experiment was frozen prospectively;
- discovery cases are excluded from holdout evidence;
- no data leakage or hindsight reconstruction is found;
- champion/challenger comparison is reproducible;
- minimum evidence stage appropriate to the rule is met;
- primary metric improves materially or removes a predeclared failure mode
  without unacceptable opportunity cost;
- bootstrap/interval analysis does not show a plausible material-harm region
  large enough to invalidate the change;
- drawdown / coverage / burden / execution guardrails remain within the frozen
  limits;
- effect is not carried by one anomalous league, odds bucket, or date block;
- known regressions are documented;
- the exact proposed permanent rule is the rule that was tested.

Otherwise: **KEEP SHADOW**, **NARROW AND RETEST**, or **REJECT**.

## Workflow

1. Read `CURRENT_MODEL.md` and the exact rules touched.
2. Identify whether the request is ordinary execution or model change.
3. For model change, create/fill a frozen experiment contract.
4. Separate discovery examples from prospective holdout.
5. Run champion and challenger from identical frozen inputs.
6. Record every eligible case, including non-bets and blocked cases.
7. Settle without changing the original decision state.
8. Produce aggregate and predeclared subgroup metrics.
9. Run an adversarial failure review: find where the apparent gain could be
   selection bias, regime concentration, quote timing, or rule leakage.
10. Issue one governance result: `PROMOTE`, `KEEP SHADOW`,
    `NARROW AND RETEST`, or `REJECT`.
11. Only after approval, edit permanent model rules and version metadata.

## Output format

For QA work, report:

- **Change under test**
- **Frozen hypothesis**
- **Discovery set**
- **Prospective holdout window**
- **Champion vs challenger counts**
- **Primary result + uncertainty**
- **Guardrails**
- **Predeclared subgroup results**
- **Exploratory findings**
- **Failure analysis**
- **Governance result**
- **Exact next action**

Never call a change proven from a handful of memorable wins/losses.
