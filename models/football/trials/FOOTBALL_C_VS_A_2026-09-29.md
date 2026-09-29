# Football Model QA Experiment — Football C vs Football A

## Identity

- **Experiment ID:** FC-C-20260929-INTEGRATED-01
- **Created at (ICT):** 2026-09-29; exact freeze commit is authoritative
- **Champion:** Football A
- **Champion commit/version:** `e68011fe4146fa67f83c448db4c2e2e09a2596e6` / Football A
- **Challenger:** Football C — SHADOW
- **Owner:** SlipTrace football model
- **Status:** FROZEN

## Rule delta

- **Exact current rule:** Football A multi-stage production architecture defined by CURRENT_MODEL.md and its compiled PRE/Step-2 authorities.
- **Exact challenger rule:** integrated Football C architecture in `models/football/challengers/football-c/FOOTBALL_C_SPEC.md`.
- **Files touched if promoted:** not precommitted; promotion would require a separate migration plan.
- **One material change only:** NO
- **If NO, why the bundle is inseparable:** Football C explicitly tests architectural simplification as one bundled challenger. It is not designed to identify the causal effect of one threshold. Component-level attribution requires later narrower challengers.

## Hypothesis

- **Observed failure mode:** Football A has accumulated multiple screening, ranking, market, execution and decay stages. Historical diagnostics show reduced ordinary direct-lane performance relative to the v0.2.47 sample, plus operational latency/resumption/persistence failures and recent execution inversions.
- **Hypothesis:** a compact integrated football decision architecture can match or improve paired decision return while reducing operational stages and preventing price/market sub-gates from overriding the football thesis mechanically.
- **Expected benefit:** better selection coherence, fewer missed high-quality protected lines, fewer scoreless-decay adverse-selection entries, lower latency and fewer persistence corrections.
- **Expected cost / missed-opportunity risk:** C may be too permissive on market undercuts/soft-price cases or too coarse to catch failure modes that Football A's specialized gates block.
- **What result would falsify the hypothesis:** C materially underperforms A on paired exposure differences, shows worse drawdown/line protection, or requires comparable operational complexity to A.

## Discovery set

| Fixture / case | Date | Why it motivated the rule |
|---|---|---|
| Belgium vs France | 2026-09-29 slate | planned decay exposure lost |
| Central African Republic vs Burkina Faso | 2026-09-29 slate | target reached after thesis deterioration; actual execution diverged from model cancellation |
| Armenia vs Montenegro | 2026-09-29 slate | simple supported direct path won |
| Sweden vs Poland | 2026-09-29 slate | 0.03 price-floor hold; supported line later cleared |
| Zimbabwe vs DR Congo | 2026-09-29 slate | market-undercut hold on protected line; total later cleared |
| Northern Ireland vs Hungary | 2026-09-29 slate | undercut + corroborated suppression hold worked |
| Historical v47 vs Football A comparison | pre-freeze | architecture/performance diagnostic only |
| Sweep/Step-2 operational failures | pre-freeze | latency, resumptions, H2H/research/persistence regressions |

These have zero prospective validation weight.

## Prospective holdout

- **Start timestamp:** first complete board whose common AiScore handoff is created strictly after the Football C model-spec freeze commit recorded below.
- **Minimum end timestamp:** after 5 complete prospective boards for the initial checkpoint; continue if governance sample targets are not met.
- **Eligible universe:** all shared senior actionable fixtures in the common AiScore handoff after hard shared identity/scope exclusions.
- **Exclusions:** discovery cases; contaminated C decisions that saw A's final action first; unresolved identity/quote epochs; expired/finished evidence states.
- **Decision information clock:** same contemporaneous raw fixture, public research, confirmed XI and user executable odds epoch as champion.
- **Market/quote epoch rule:** exact user quote/time when supplied; no later quote substituted retroactively.
- **Minimum eligible decisions:** initial checkpoint = 5 complete boards; governance shadow preference >=40 eligible decisions.
- **Minimum settled exposure differences:** governance preference >=20.

## Frozen metrics

### Primary metric
- Flat-stake unit-return delta on settled A-vs-C exposure differences using exact contemporaneous selected lines/odds.

### Secondary metrics
- unit return / yield
- exposure-rate delta
- maximum drawdown
- average odds / line
- paired champion-vs-challenger decision table
- time-block stability
- direct vs WAIT outcome
- WAIT target reach/cancellation
- board-build and XI-decision latency
- stage/tool count
- resumptions/retries
- persistence corrections
- pre-kick verdict reversals

### Guardrails
- C remains shadow-only.
- C never reads FT/future evidence before freezing.
- C does not read A final action before freezing its own corresponding action.
- C keeps the single integrated-board + single XI-confirmation architecture.
- No C rule edits during the first 5 boards.
- No degradation in fixture/time identity safety.

### Predeclared subgroup cuts
- grade/rank: C-FOCUS / C-WATCH
- route class: two-route / carrier-led
- carrier verification: strong / usable / none
- odds buckets: <1.65 / 1.65–1.79 / >=1.80
- line/burden buckets: <=2.5 / 2.75–3.0 / >=3.25
- prematch/live-decay: direct / C-WAIT
- league/regime: senior club / senior international
- market relation: below / aligned / above C-supported burden
- H2H: suppressive-corroborated / other

## Event fields required

For every eligible case preserve fixture identity, decision timestamp, C rank/state, route class/carrier state, supported burden, XI state, market/current quote when available, offered line/odds, champion execution/exposure, challenger action, WAIT target/reach/cancel state, final score, settlement, and contemporaneously captured closing line/price if available.

## Freeze record

- **Football C model-spec freeze commit:** `7ac7ac1b69c0b741cd742b45481d88a04cdf0a08`
- **Rules may change after this commit:** NO for experiment FC-C-20260929-INTEGRATED-01
- **First five-board checkpoint:** boards beginning strictly after the freeze commit

## Results

Do not fill until prospective boards run.

## Failure analysis

Do not fill until prospective boards run.

## Governance result

- [ ] PROMOTE
- [x] KEEP SHADOW
- [ ] NARROW AND RETEST
- [ ] REJECT

### Reason
Initial state before prospective evidence.

### Exact next action
Freeze the challenger, then run the next 5 complete boards side-by-side with Football A.

### Proposed effective timestamp if promoted
Not applicable.
