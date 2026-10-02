import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from competition_reliability import (  # noqa: E402
    apply_reliability_cap,
    evaluate_competition_reliability,
)


def event(
    day,
    *,
    xi="USABLE",
    market="USABLE",
    news="USABLE",
    identity="CLEAN",
    step2="COMPLETED",
    observation_type="STEP2_OBSERVED",
):
    return {
        "observed_at": f"2026-10-{day:02d}T12:00:00+07:00",
        "observation_type": observation_type,
        "xi_outcome": xi,
        "market_outcome": market,
        "team_news_outcome": news,
        "identity_time_outcome": identity,
        "step2_outcome": step2,
    }


class CompetitionReliabilityTests(unittest.TestCase):
    def test_two_clean_observations_are_unproven(self):
        result = evaluate_competition_reliability([event(1), event(2)])
        self.assertEqual(result.state, "UNPROVEN")

    def test_five_clean_observations_are_trusted(self):
        result = evaluate_competition_reliability([event(i) for i in range(1, 6)])
        self.assertEqual(result.state, "TRUSTED")

    def test_repeated_missing_xi_demotes(self):
        rows = [
            event(1, xi="MISSING", step2="BLOCKED_XI"),
            event(2, xi="MISSING", step2="BLOCKED_XI"),
            event(3, xi="MISSING", step2="BLOCKED_XI"),
            event(4, xi="USABLE"),
        ]
        result = evaluate_competition_reliability(rows)
        self.assertEqual(result.state, "DEMOTED")

    def test_partial_xi_reliability_is_caution(self):
        rows = [
            event(1, xi="USABLE"),
            event(2, xi="USABLE"),
            event(3, xi="MISSING", step2="BLOCKED_XI"),
        ]
        result = evaluate_competition_reliability(rows)
        self.assertEqual(result.state, "CAUTION")

    def test_prefight_event_does_not_change_sample(self):
        rows = [event(1), event(2), event(3, observation_type="PREFLIGHT_OBSERVED")]
        result = evaluate_competition_reliability(rows)
        self.assertEqual(result.rolling_sample, 2)
        self.assertEqual(result.state, "UNPROVEN")

    def test_caution_caps_a_to_b(self):
        self.assertEqual(apply_reliability_cap("A", "CAUTION"), "B")

    def test_history_never_promotes(self):
        self.assertEqual(apply_reliability_cap("B", "TRUSTED"), "B")
        self.assertEqual(apply_reliability_cap("C", "NEUTRAL"), "C")

    def test_demoted_is_c_by_default(self):
        self.assertEqual(apply_reliability_cap("A", "DEMOTED"), "C")
        self.assertEqual(apply_reliability_cap("B", "DEMOTED"), "C")

    def test_demoted_probation_is_b_only_for_raw_a(self):
        self.assertEqual(
            apply_reliability_cap("A", "DEMOTED", demoted_probation=True),
            "B",
        )
        self.assertEqual(
            apply_reliability_cap("B", "DEMOTED", demoted_probation=True),
            "C",
        )


if __name__ == "__main__":
    unittest.main()
