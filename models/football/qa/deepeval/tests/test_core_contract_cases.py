from __future__ import annotations

import json
from pathlib import Path

import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase

from football_contract_metric import FootballContractMetric


CASES = Path(__file__).parents[1] / "cases" / "core_contract_cases.json"


def load_cases() -> list[dict]:
    return json.loads(CASES.read_text(encoding="utf-8"))


@pytest.mark.parametrize("case", load_cases(), ids=lambda case: case["id"])
def test_core_football_contracts(case: dict) -> None:
    test_case = LLMTestCase(
        name=case["id"],
        input=case["input"],
        actual_output=case["actual_output"],
        metadata={"contract": case["contract"], "purpose": case["purpose"]},
    )
    assert_test(
        test_case,
        metrics=[FootballContractMetric()],
        run_async=False,
    )
