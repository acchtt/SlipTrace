import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from repaired_handoff_normalize import (  # noqa: E402
    RepairedHandoffNormalizationError,
    normalize_repaired_handoff,
)


def base_payload():
    return {
        "women_top_flight_disposition_manifest": [
            {
                "match_id": "w1",
                "match": "A - B",
                "final_step0_disposition": "ADMITTED_TO_C",
                "disposition": "OPERATIONAL_CAPACITY_DEFERRED",
            },
            {
                "match_id": "w2",
                "match": "C - D",
                "final_step0_disposition": "OPERATIONAL_CAPACITY_DEFERRED",
                "disposition": "ADMITTED_TO_C",
            },
        ],
        "women_top_flight_raw_count": 2,
        "women_top_flight_admitted_count": 0,
        "women_top_flight_operational_excluded_count": 1,
        "women_top_flight_researchability_excluded_count": 0,
        "women_top_flight_capacity_deferred_count": 0,
        "women_top_flight_unresolved_count": 1,
        "capacity_queue": [
            {
                "match_id": "w1",
                "final_step0_disposition": "ADMITTED_TO_C",
                "disposition": "OPERATIONAL_CAPACITY_DEFERRED",
                "women_top_flight": "senior women top flight",
                "operational_viability_grade": "A",
            },
            {
                "match_id": "m1",
                "final_step0_disposition": "ADMITTED_TO_C",
                "disposition": "ADMITTED_TO_C",
                "women_top_flight": "not women",
                "operational_viability_grade": "A",
            },
        ],
    }


class RepairedHandoffNormalizerTests(unittest.TestCase):
    def test_final_disposition_wins_and_counts_are_recomputed(self):
        payload = base_payload()
        payload["women_top_flight_unresolved_count"] = 0
        out, report = normalize_repaired_handoff(payload)
        self.assertEqual(out["women_top_flight_admitted_count"], 1)
        self.assertEqual(out["women_top_flight_capacity_deferred_count"], 1)
        self.assertEqual(out["women_top_flight_operational_excluded_count"], 0)
        self.assertEqual(
            out["capacity_queue"][0]["disposition"],
            "ADMITTED_TO_C",
        )
        self.assertGreater(report["fixture_disposition_conflicts_fixed"], 0)

    def test_women_boolean_is_derived_from_manifest_membership(self):
        payload = base_payload()
        payload["women_top_flight_unresolved_count"] = 0
        out, _ = normalize_repaired_handoff(payload)
        self.assertIs(out["capacity_queue"][0]["women_top_flight"], True)
        self.assertIs(out["capacity_queue"][1]["women_top_flight"], False)

    def test_unresolved_women_still_fails_closed(self):
        payload = base_payload()
        payload["women_top_flight_disposition_manifest"][1][
            "final_step0_disposition"
        ] = "UNRESOLVED"
        payload["women_top_flight_disposition_manifest"][1][
            "disposition"
        ] = "UNRESOLVED"
        with self.assertRaisesRegex(
            RepairedHandoffNormalizationError,
            "women_top_flight_unresolved_count must be 0",
        ):
            normalize_repaired_handoff(payload)


if __name__ == "__main__":
    unittest.main()
