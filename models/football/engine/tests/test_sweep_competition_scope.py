import pathlib
import sys
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))
from sweep_competition_scope import classify_competition, screen_competitions


def c(name, country, kind="DOMESTIC_LEAGUE", **overrides):
    return {"competition_name":name,"country":country,"competition_kind":kind,**overrides}


class ScopeFirstTests(unittest.TestCase):
    def test_bangladesh_all_domestic_unlisted_or_premier_league_blocked(self):
        for name in ("Bangladesh Premier League","Premier League","Bangladesh Championship"):
            with self.subTest(name=name):
                self.assertEqual(classify_competition(c(name,"Bangladesh"))["lane"],"SCOPE_EXCLUDED")

    def test_indonesia_second_tier_does_not_get_unlimited_verification(self):
        self.assertEqual(classify_competition(c("Liga 2","Indonesia"))["lane"],"SCOPE_EXCLUDED")

    def test_explicit_major_leagues_and_eerste_still_considered(self):
        for name,country in (("Bundesliga","Germany"),("Premier League","England"),
                             ("Eerste Divisie","Netherlands"),("Eliteserien","Norway")):
            self.assertEqual(classify_competition(c(name,country))["lane"],"ROUTINE_LEAGUE_PROFILE")

    def test_explicit_user_domestic_exclusions_stronger_than_market_channels(self):
        for name,country in (("J1 League","Japan"),("K League 1","South Korea"),
                             ("3. Liga","Germany"),("Premier League","Wales"),
                             ("Premier League","Israel")):
            self.assertEqual(classify_competition(c(name,country))["lane"],"SCOPE_EXCLUDED")

    def test_cups_protected_and_womens_raw_coverage_separate(self):
        rows=[
            c("Australia Cup","Australia","DOMESTIC_CUP"),
            c("UEFA Champions League","Europe","CONTINENTAL"),
            c("Chinese Women's Super League","China","WOMENS_TOP_FLIGHT"),
            c("Indonesian Liga 2","Indonesia"),
        ]
        q=screen_competitions(rows)
        self.assertEqual(q["routine_verification_count"],3)
        self.assertEqual(len(q["blocks"]["SCOPE_EXCLUDED"]),1)
        self.assertEqual(q["blocks"]["CUP_CHANNEL_REVIEW"][0]["competition_name"],"Australia Cup")
        self.assertEqual(q["blocks"]["COVERAGE_AUDIT_PROOF_REQUIRED"][0]["country"],"China")

    def test_user_named_override_does_not_create_a_new_registered_league(self):
        result=classify_competition(c("Bangladesh Premier League","Bangladesh",user_one_run_override=True))
        self.assertEqual(result["lane"],"SCOPE_EXCLUDED")

    def test_malformed_unknown_league_does_not_get_auto_tier1(self):
        self.assertEqual(classify_competition(c("", "Bangladesh"))["lane"],"SCOPE_UNRESOLVED")
        self.assertEqual(classify_competition(c("Unknown", "Unknown", "DOMESTIC_LEAGUE"))["lane"],"SCOPE_EXCLUDED")

    def test_no_duplicate_competition_deep_crawls(self):
        with self.assertRaisesRegex(ValueError,"duplicate competition"):
            screen_competitions([c("Bundesliga","Germany"),c("Bundesliga","Germany")])


if __name__=="__main__":
    unittest.main()
