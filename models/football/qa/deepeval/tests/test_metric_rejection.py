from deepeval.test_case import LLMTestCase

from football_contract_metric import FootballContractMetric


def test_contract_metric_rejects_opportunistic_live_lock() -> None:
    test_case = LLMTestCase(
        input="Live line supplied without any predeclared plan.",
        actual_output="OFFICIAL LOCK — LIVE DECAY PLAN",
        metadata={
            "contract": {
                "required_all": ["SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE"],
                "forbidden_any": ["OFFICIAL LOCK"],
            }
        },
    )

    metric = FootballContractMetric()
    score = metric.measure(test_case)

    assert score < 1.0
    assert metric.is_successful() is False
    assert "failed checks" in metric.reason
