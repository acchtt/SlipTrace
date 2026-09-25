# Football Model QA Experiment

> Copy this file for each challenger. Freeze this record before prospective
> holdout outcomes are known.

## Identity

- **Experiment ID:**
- **Created at (ICT):**
- **Champion:**
- **Champion commit/version:**
- **Challenger:**
- **Owner:**
- **Status:** DRAFT / FROZEN / RUNNING / COMPLETE / INVALIDATED

## Rule delta

- **Exact current rule:**
- **Exact challenger rule:**
- **Files touched if promoted:**
- **One material change only:** YES / NO
- If NO, why the bundle is inseparable:

## Hypothesis

- **Observed failure mode:**
- **Hypothesis:**
- **Expected benefit:**
- **Expected cost / missed-opportunity risk:**
- **What result would falsify the hypothesis:**

## Discovery set

List every match/example that motivated the change. These are **not holdout
evidence**.

| Fixture / case | Date | Why it motivated the rule |
|---|---|---|

## Prospective holdout

- **Start timestamp:**
- **Minimum end timestamp:**
- **Eligible universe:**
- **Exclusions:**
- **Decision information clock:**
- **Market/quote epoch rule:**
- **Minimum eligible decisions:**
- **Minimum settled exposure differences:**

## Frozen metrics

### Primary metric
-

### Secondary metrics
- unit return / yield
- exposure-rate delta
- maximum drawdown
- average odds / line
- paired champion-vs-challenger decision table
- time-block stability

### Guardrails
-

### Predeclared subgroup cuts
- grade/rank:
- route class:
- carrier verification:
- odds buckets:
- line/burden buckets:
- prematch/live-decay:
- league/regime:

## Event fields required

For every eligible case preserve:

- fixture identity;
- decision timestamp;
- structural rank/grade;
- route class / carrier state;
- supported burden;
- XI state;
- market center;
- offered line and odds;
- champion execution/exposure;
- challenger execution/exposure;
- live-decay target and reach/invalidated state if applicable;
- final score;
- settlement;
- closing line/price if contemporaneously captured.

## Results

Do not fill until the frozen window is running/complete.

- **Eligible opportunities:**
- **Settled exposure differences:**
- **Champion W/HW/P/HL/L:**
- **Challenger W/HW/P/HL/L:**
- **Champion unit return / yield:**
- **Challenger unit return / yield:**
- **Primary delta:**
- **Uncertainty interval / bootstrap summary:**
- **Champion max drawdown:**
- **Challenger max drawdown:**
- **Coverage delta:**
- **Regime concentration check:**
- **Time-block stability:**

## Failure analysis

- Could discovery leakage explain the gain?
- Could one league/date block explain the gain?
- Did quote timing differ?
- Did the challenger use information unavailable to the champion?
- Did the rule merely increase exposure to higher-variance lines?
- Did any subgroup reverse the aggregate result?
- What is the strongest argument against promotion?

## Governance result

Choose exactly one:

- [ ] PROMOTE
- [ ] KEEP SHADOW
- [ ] NARROW AND RETEST
- [ ] REJECT

### Reason

### Exact next action

### Proposed effective timestamp if promoted
