"""Deterministic DeepEval metric for SlipTrace Football process contracts.

This module deliberately uses no LLM judge.  It lets the core QA suite run in
CI without an API key while still using DeepEval's test-case/metric machinery.
LLM-as-a-judge metrics can be layered on later for semantic checks that cannot
be represented as explicit process invariants.
"""

from __future__ import annotations

import re
from typing import Any

from deepeval.metrics import BaseMetric
from deepeval.test_case import LLMTestCase


class FootballContractMetric(BaseMetric):
    """Score a saved football-model output against explicit QA invariants.

    Expectations are read from ``test_case.metadata["contract"]``.

    Supported contract keys:
      - required_all: every string must appear in the output.
      - forbidden_any: none of the strings may appear in the output.
      - required_any: list of string groups; at least one string in every group
        must appear.
      - required_regex: every regular expression must match.
      - forbidden_regex: no regular expression may match.

    Text checks are case-insensitive.  Regex checks use IGNORECASE | MULTILINE.
    """

    threshold = 1.0
    async_mode = False
    verbose_mode = False
    include_reason = True

    def __init__(self, threshold: float = 1.0):
        self.threshold = threshold
        self.score = None
        self.reason = None
        self.success = None

    @property
    def __name__(self) -> str:
        return "Football process contract"

    @staticmethod
    def _norm(value: str) -> str:
        return " ".join(value.casefold().split())

    @staticmethod
    def _contract(test_case: LLMTestCase) -> dict[str, Any]:
        metadata = test_case.metadata or {}
        contract = metadata.get("contract")
        if not isinstance(contract, dict):
            raise ValueError(
                "LLMTestCase.metadata must contain a 'contract' object"
            )
        return contract

    def measure(self, test_case: LLMTestCase, *args, **kwargs) -> float:
        output = test_case.actual_output or ""
        normalized = self._norm(output)
        contract = self._contract(test_case)

        checks: list[tuple[str, bool]] = []

        for phrase in contract.get("required_all", []):
            checks.append((f"required: {phrase}", self._norm(phrase) in normalized))

        for phrase in contract.get("forbidden_any", []):
            checks.append((f"forbidden: {phrase}", self._norm(phrase) not in normalized))

        for index, group in enumerate(contract.get("required_any", []), start=1):
            if not isinstance(group, list) or not group:
                raise ValueError(f"required_any group {index} must be a non-empty list")
            passed = any(self._norm(phrase) in normalized for phrase in group)
            checks.append((f"required_any[{index}]: {' | '.join(group)}", passed))

        flags = re.IGNORECASE | re.MULTILINE
        for pattern in contract.get("required_regex", []):
            checks.append((f"required_regex: {pattern}", re.search(pattern, output, flags) is not None))

        for pattern in contract.get("forbidden_regex", []):
            checks.append((f"forbidden_regex: {pattern}", re.search(pattern, output, flags) is None))

        if not checks:
            raise ValueError("football contract contains no checks")

        passed = sum(1 for _, ok in checks if ok)
        self.score = passed / len(checks)
        failures = [name for name, ok in checks if not ok]
        self.reason = (
            "all contract checks passed"
            if not failures
            else "failed checks: " + "; ".join(failures)
        )
        self.success = self.score >= self.threshold
        return self.score

    async def a_measure(self, test_case: LLMTestCase, *args, **kwargs) -> float:
        return self.measure(test_case, *args, **kwargs)
