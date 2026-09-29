"""Optional LLM-judge metrics for Football A historical semantic QA.

These metrics deliberately receive no final score or settlement result.
They are intended for manual DeepEval runs after a judge API key is configured.
"""

from __future__ import annotations

import json
import os
from typing import Any

from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams


POLICY_CONTEXT = """Football A semantic QA principles:
- judge only from evidence available at the decision epoch; do not use hindsight;
- frozen PRE history must remain distinct from current XI/market interpretation;
- market price alone cannot create a scoring route or justify extra burden;
- live official exposure requires a predeclared plan or active match-specific exception;
- post-XI football research is distinct from market-history research;
- H2H is supporting/matchup evidence and should not create a route by itself;
- XI analysis should reason about mechanism preservation/degradation, not headcount alone;
- stated verdict/execution class must be supported by the supplied evidence and blockers.
"""


def _metric_kwargs() -> dict[str, Any]:
    model = os.getenv("DEEPEVAL_JUDGE_MODEL", "").strip()
    return {"model": model} if model else {}


def evidence_verdict_consistency() -> GEval:
    return GEval(
        name="Football evidence-verdict consistency",
        evaluation_steps=[
            "Use only the decision-time INPUT, CONTEXT and ACTUAL OUTPUT. Final result is intentionally absent.",
            "Check whether the verdict and execution state are logically supported by the frozen PRE, supplied market state, and decision-time football reasoning.",
            "Penalize internal contradictions, hidden burden escalation, or a conclusion that is stronger than the evidence described.",
            "Penalize reasoning that treats price or market height as sufficient by itself to create football structure.",
            "Do not reward or punish the decision based on what might have happened after the quote.",
        ],
        evaluation_params=[
            SingleTurnParams.INPUT,
            SingleTurnParams.CONTEXT,
            SingleTurnParams.ACTUAL_OUTPUT,
        ],
        threshold=0.7,
        **_metric_kwargs(),
    )


def plan_adherence() -> GEval:
    return GEval(
        name="Football live-plan adherence",
        evaluation_steps=[
            "Determine whether the ACTUAL OUTPUT respects the live eligibility stated in the INPUT and CONTEXT.",
            "Official live exposure requires evidence of a predeclared plan or active match-specific exception.",
            "If there is no such authority, the output should remain hold/shadow/non-official rather than creating a fresh official live thesis.",
            "If material state damage is described, a previously qualified plan must not execute merely because the target line or price is available.",
        ],
        evaluation_params=[
            SingleTurnParams.INPUT,
            SingleTurnParams.CONTEXT,
            SingleTurnParams.ACTUAL_OUTPUT,
        ],
        threshold=0.8,
        **_metric_kwargs(),
    )


def h2h_discipline() -> GEval:
    return GEval(
        name="Football H2H discipline",
        evaluation_steps=[
            "Check that H2H is treated as supporting or matchup evidence rather than as a scoring route by itself.",
            "When H2H is used to suppress an O3.0+ route, look for a transferable matchup mechanism and an independent current negative channel rather than scoreline counting alone.",
            "When H2H is old or context has materially changed, reward explicit low-transferability treatment.",
            "Penalize both automatic H2H vetoes and automatic H2H upgrades unsupported by current mechanisms.",
        ],
        evaluation_params=[
            SingleTurnParams.CONTEXT,
            SingleTurnParams.ACTUAL_OUTPUT,
        ],
        threshold=0.7,
        **_metric_kwargs(),
    )


def xi_mechanism_reasoning() -> GEval:
    return GEval(
        name="Football XI mechanism reasoning",
        evaluation_steps=[
            "Check whether lineup reasoning explains what attacking or defensive functions are preserved, replaced, degraded, broken, or unresolved.",
            "Reward mechanism-level reasoning about creation, finishing, service, sustainment or resistance.",
            "Penalize conclusions based mainly on counting starters/rotation without explaining the affected scoring mechanism.",
            "Check that a materially broken required mechanism is not rescued solely by price or market movement.",
        ],
        evaluation_params=[
            SingleTurnParams.CONTEXT,
            SingleTurnParams.ACTUAL_OUTPUT,
        ],
        threshold=0.7,
        **_metric_kwargs(),
    )


def build_test_case(case: dict[str, Any]) -> LLMTestCase:
    decision = case["decision"]
    frozen = case.get("frozen_pre") or {}

    input_parts = [
        f"Match: {case.get('match')}",
        f"Competition: {case.get('competition')}",
        f"Assessment time UTC: {case.get('assessment_time_utc')}",
        f"Epoch: {case.get('evidence_epoch')}",
        f"Period/minute: {case.get('assessment_period')} / {case.get('minute')}",
        f"Score at assessment: {case.get('score_at_assessment')}",
        f"Supplied line: {decision.get('supplied_line')}",
        f"Supplied odds: {decision.get('supplied_odds')}",
        f"Supported target: {decision.get('supported_target_line')}",
        f"Minimum odds: {decision.get('target_min_odds')}",
    ]

    actual_parts = [
        f"Verdict: {decision.get('verdict')}",
        f"Candidate: {decision.get('candidate')}",
        f"Execution class: {decision.get('execution_class')}",
        f"Decision-time reasoning: {decision.get('decision_evidence')}",
    ]

    context = [
        POLICY_CONTEXT,
        "Frozen PRE / board state:\n" + json.dumps(frozen, ensure_ascii=False, indent=2),
    ]

    return LLMTestCase(
        name=case["assessment_id"],
        input="\n".join(input_parts),
        actual_output="\n".join(actual_parts),
        context=context,
        metadata={
            "assessment_id": case["assessment_id"],
            "model_version": case.get("model_version"),
            "audit_outcome_intentionally_excluded": True,
        },
    )


def metric_set_for_case(case: dict[str, Any]) -> list[GEval]:
    metrics = [evidence_verdict_consistency()]
    text = (
        str((case.get("decision") or {}).get("decision_evidence") or "")
        + " "
        + str(case.get("assessment_period") or "")
    ).upper()

    if case.get("evidence_epoch") == "LIVE_OR_JUST_STARTED":
        metrics.append(plan_adherence())
    if "H2H" in text:
        metrics.append(h2h_discipline())
    if "XI" in text:
        metrics.append(xi_mechanism_reasoning())
    return metrics
