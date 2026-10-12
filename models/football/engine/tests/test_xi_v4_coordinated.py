"""Regression for /xi V4 native authority, football-first and Airtable readback."""
from __future__ import annotations
import copy
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

HERE=pathlib.Path(__file__).resolve().parent
ENGINE=HERE.parent
sys.path.insert(0,str(ENGINE))
from step2_queue_guard import freeze_queue,Step2QueueError
from xi_v4_queue import _digest
from xi_assessment_reconcile import verify_football_assessment,XIAssessmentReadbackError
from test_football_assessment_pair import football
from test_adapter import pair_payload
from decision_pair_cli import run_football_pair


def native_v4_case():
    run="V4-20261012-1300"
    original_source={
        "schema_version":"football-stages-v4",
        "run_id":run,
        "source_name":"verified-provider",
        "source_url":"https://sports.example.org/window",
        "window_start_ict":"2026-10-12T20:00:00+07:00",
        "window_end_ict":"2026-10-12T23:00:00+07:00",
        "observed_at_utc":"2026-10-12T12:59:00Z",
        "fixtures":[{"match_id":"fixture-1","kickoff_utc":"2026-10-12T14:00:00Z"}],
    }
    source={
        "schema_version":"football-stages-v4",
        "status":"V4_SWEEP_READY",
        "run_id":run,
        "eligible_queue":[{"match_id":"fixture-1","kickoff_utc":"2026-10-12T14:00:00Z"}],
        "source_ledger_hash":"verified-fixture-provider-source-hash",
    }
    source["integrity_sha256"]=_digest(source)
    status_refresh={
        "schema_version":"football-v4-rank-status-refresh-v1",
        "run_id":run,
        "sweep_integrity_sha256":source["integrity_sha256"],
        "checked_at_utc":"2026-10-12T13:05:00Z",
        "matches":[{"match_id":"fixture-1","fixture_status":"PREMATCH_CONFIRMED",
                    "kickoff_utc":"2026-10-12T14:00:00Z",
                    "source_url":"https://sports.example.org/fixture/1",
                    "observed_at_utc":"2026-10-12T13:05:00Z"}],
    }
    c={"match_id":"fixture-1","board_state":"FOCUS","follow_lane":"FOLLOW",
       "supported_line":2.5}
    c2={"match_id":"fixture-1","board_state":"WATCH","supported_line":2.75}
    rank={
        "schema_version":"football-stages-v4",
        "status":"V4_RANK_EXECUTED_AWAITING_AIRTABLE_READBACK",
        "run_id":run,
        "sweep_integrity_sha256":source["integrity_sha256"],
        "ranked_count":1,
        "source_replayed":True,
        "current_fixture_status_checked":True,
        "original_source_sha256":_digest(original_source),
        "status_refresh_sha256":_digest(status_refresh),
        "board_pair":{"board_engine_execution_status":"EXECUTED_C_C2_BOARDS",
                      "common_evidence_reconciled":True,
                      "results":{"c":{"matches":[c]},"c2":{"matches":[c2]}}},
    }
    rank["integrity_sha256"]=_digest(rank)
    verified={"schema_version":"football-stages-v4",
              "status":"V4_RANK_PERSISTENCE_VERIFIED",
              "run_id":run,"rank_sha256":rank["integrity_sha256"],
              "ranked_count":1,"c2_shadow_only":True,
              "source_replayed":True,
              "current_fixture_status_checked":True,
              "original_source_sha256":rank["original_source_sha256"],
              "status_refresh_sha256":rank["status_refresh_sha256"]}
    row={"match_id":"fixture-1",
         "coverage_id":run+"|fixture-1",
         "kickoff_utc":"2026-10-12T14:00:00Z",
         "kickoff_ict":"2026-10-12T21:00:00+07:00",
         "official_follow_lane":"FOLLOW",
         "xi_window_open":True,
         "xi_window_basis":"Live provider verified XI window currently open",
         "c_board_state":"C-FOCUS",
         "c2_shadow_state":"C2-WATCH",
         "c_supported_line":2.5,"c2_supported_line":2.75,
         "c2_supported_line_basis":"Actual independently frozen C2 burden"}
    return {
        "schema_version":"football-step2-queue-v1",
        "session_id":"XI-V4-TEST","mode":"V4_ROUTINE",
        "board":[row],"user_exceptions":[],"activated_reserves":[],
        "v4_sweep_receipt":source,"v4_rank_receipt":rank,
        "v4_persistence_receipt":verified,
        "v4_original_source":original_source,
        "v4_status_refresh":status_refresh,
    }


def call_xi(fc,fs,pc=None,ps=None):
    with tempfile.TemporaryDirectory() as tmp:
        root=pathlib.Path(tmp)
        files={}
        for name,data in (("fc",fc),("fs",fs),("pc",pc),("ps",ps)):
            if data is None:continue
            fp=root/(name+".json")
            fp.write_text(json.dumps(data),encoding="utf-8")
            files[name]=str(fp)
        args=[sys.executable,str(ENGINE/"xi_portable.py"),"xi",
              "--c",files["fc"],"--c2",files["fs"]]
        if "pc" in files:
            args+=["--price-c",files["pc"],"--price-c2",files["ps"]]
        return subprocess.run(args,text=True,capture_output=True,timeout=20)


class V4QueueBridgeTests(unittest.TestCase):
    def test_genuine_v4_rank_authorizes_routine_c_not_c2(self):
        actual=freeze_queue(native_v4_case())
        self.assertTrue(actual["v4_provenance_chain_verified"])
        self.assertNotIn("v4_source_attested", actual)
        self.assertEqual(actual["source_run_id"],"V4-20261012-1300")
        self.assertEqual(actual["due_count"],1)
        self.assertEqual(actual["due"][0]["step2_authorization"],"ROUTINE_FOLLOW")

    def test_old_or_synthetic_rank_without_hardened_provenance_is_rejected(self):
        for target,field in (
            ("v4_rank_receipt","source_replayed"),
            ("v4_rank_receipt","current_fixture_status_checked"),
            ("v4_rank_receipt","original_source_sha256"),
            ("v4_rank_receipt","status_refresh_sha256"),
            ("v4_persistence_receipt","source_replayed"),
            ("v4_persistence_receipt","current_fixture_status_checked"),
            ("v4_persistence_receipt","original_source_sha256"),
            ("v4_persistence_receipt","status_refresh_sha256"),
        ):
            with self.subTest(target=target,field=field):
                case=native_v4_case()
                case[target].pop(field)
                if target=="v4_rank_receipt":
                    case[target]["integrity_sha256"]=_digest({k:v for k,v in case[target].items() if k!="integrity_sha256"})
                    case["v4_persistence_receipt"]["rank_sha256"]=case[target]["integrity_sha256"]
                with self.assertRaisesRegex(Step2QueueError,"provenance|source|status|sha256|proof"):
                    freeze_queue(case)

    def test_original_source_or_status_payload_mismatch_is_rejected(self):
        for target in ("v4_original_source","v4_status_refresh"):
            with self.subTest(target=target):
                case=native_v4_case()
                case[target]["tampered"]=True
                with self.assertRaisesRegex(Step2QueueError,"original source|status-refresh"):
                    freeze_queue(case)

    def test_sealed_source_rank_and_lane_cannot_be_forged(self):
        for target,field,new in (
            ("v4_sweep_receipt","run_id","SWEEP-OLD"),
            ("v4_rank_receipt","ranked_count",3),
            ("v4_persistence_receipt","rank_sha256","false"),
            ("board","official_follow_lane","STOP"),
            ("board","c2_supported_line",3.0),
        ):
            with self.subTest(target=target,field=field):
                case=native_v4_case()
                if target=="board":case["board"][0][field]=new
                else:case[target][field]=new
                with self.assertRaisesRegex(Step2QueueError,"V4|integrity"):
                    freeze_queue(case)

    def test_exception_still_authorized_without_board(self):
        case={"schema_version":"football-step2-queue-v1",
              "session_id":"TEST-EXCEPTION","mode":"EXCEPTION_ONLY",
              "board":[],"activated_reserves":[],
              "user_exceptions":[{"match_id":"new-exception",
                "user_authorization_reference":"user explicitly requested /xi exception"}]}
        result=freeze_queue(case)
        self.assertEqual(result["due_count"],1)
        self.assertEqual(result["due"][0]["step2_authorization"],"USER_EXCEPTION")


class FootballFirstExecutionTests(unittest.TestCase):
    def test_no_quote_prematch_early_late_and_halftime(self):
        for state,minute,score in (
            ("PREMATCH_CONFIRMED",None,None),
            ("STARTED",3,"0-0"),("STARTED",17,"1-0"),
            ("HALFTIME",45,"2-1")
        ):
            with self.subTest(state=state):
                r=call_xi(football("c",status=state,minute=minute,score=score),
                          football("c2",status=state,minute=minute,score=score))
                self.assertEqual(r.returncode,0,r.stderr[-500:])
                out=json.loads(r.stdout)
                self.assertEqual(out["engine_execution_status"],"EXECUTED_C_C2_FOOTBALL_ONLY")
                self.assertFalse(out["model_bets_created"])

    def test_stale_price_does_not_erase_true_football(self):
        fc=football("c",status="PREMATCH_CONFIRMED",minute=None,score=None)
        fs=football("c2",status="PREMATCH_CONFIRMED",minute=None,score=None)
        pc,ps=pair_payload("c"),pair_payload("c2")
        pc["evidence_epoch_id"]=ps["evidence_epoch_id"]=fc["evidence_epoch_id"]
        for x in (pc,ps):x["context"]["quote_revalidated"]=False
        r=call_xi(fc,fs,pc,ps)
        self.assertEqual(r.returncode,0,r.stderr[-900:])
        out=json.loads(r.stdout)
        self.assertEqual(out["xi_mode"],"FOOTBALL_ASSESSED_PRICE_CHECK_BLOCKED")
        self.assertEqual(out["price_check"]["status"],"PRICE_CHECK_BLOCKED")
        self.assertFalse(out["price_check"]["bet_authorized"])
        self.assertEqual(set(out["results"]),{"c","c2"})
        self.assertFalse(out["model_bets_created"])

    def test_real_prematch_quote_checked_in_same_one_command(self):
        fc=football("c",status="PREMATCH_CONFIRMED",minute=None,score=None)
        fs=football("c2",status="PREMATCH_CONFIRMED",minute=None,score=None)
        pc,ps=pair_payload("c"),pair_payload("c2")
        pc["evidence_epoch_id"]=ps["evidence_epoch_id"]=fc["evidence_epoch_id"]
        r=call_xi(fc,fs,pc,ps)
        self.assertEqual(r.returncode,0,r.stderr[-900:])
        out=json.loads(r.stdout)
        self.assertEqual(out["xi_mode"],"FOOTBALL_AND_PRICE_CHECK")
        self.assertTrue(out["price_check"]["ok"])
        self.assertEqual(out["price_check"]["receipt"]["engine_execution_status"],"EXECUTED_C_C2_PAIR")
        self.assertEqual(out["engine_execution_status"],"EXECUTED_C_C2_FOOTBALL_ONLY")

    def test_started_quote_must_go_through_live_not_prematch_pair(self):
        fc=football("c",status="STARTED",minute=4,score="0-0")
        fs=football("c2",status="STARTED",minute=4,score="0-0")
        pc,ps=pair_payload("c"),pair_payload("c2")
        pc["evidence_epoch_id"]=ps["evidence_epoch_id"]=fc["evidence_epoch_id"]
        r=call_xi(fc,fs,pc,ps)
        self.assertEqual(r.returncode,0,r.stderr[-900:])
        out=json.loads(r.stdout)
        self.assertIn("STARTED/HALFTIME",out["price_check"]["reason"])
        self.assertEqual(out["engine_execution_status"],"EXECUTED_C_C2_FOOTBALL_ONLY")


class XIStoredFootballStatusTests(unittest.TestCase):
    def test_real_pair_readback_and_price_blocked_labels(self):
        from xi_assessment_reconcile import STATUS_FIELD_ID
        pair=run_football_pair(football("c"),football("c2"))
        for priced,expected in (
            (None,"EXECUTED_C_C2_FOOTBALL_ONLY"),
            ({"ok":False,"status":"PRICE_CHECK_BLOCKED"},"EXECUTED_C_C2_FOOTBALL_PRICE_BLOCKED"),
            ({"ok":True,"status":"PRICE_CHECK_EXECUTED"},"EXECUTED_C_C2_FOOTBALL_AND_PRICE"),
        ):
            with self.subTest(expected=expected):
                receipt={"ok":True,**pair}
                if priced is not None:receipt["price_check"]=priced
                readback={"base_id":"appbzxqXYf0lKfD4P",
                          "record_id":"rec1234567890ABCDE",
                          "assessment_id":"XI-C2-EXAMPLE",
                          "match_id":pair["results"]["c"]["match_id"],
                          "readback_method":"INDEPENDENT_AIRTABLE_REFETCH",
                          "xi_status_field_id":STATUS_FIELD_ID,
                          "xi_assessment_execution_status":expected,
                          "engine_c_result":json.dumps(pair["results"]["c"]),
                          "engine_c2_result":pair["results"]["c2"]}
                result=verify_football_assessment(receipt,readback)
                self.assertTrue(result["football_pair_verified"])
                self.assertFalse(result["actual_bet_created"])
                tampered=copy.deepcopy(readback)
                tampered["xi_assessment_execution_status"]="ENGINE_FAILED_AFTER_ATTEMPT"
                with self.assertRaisesRegex(XIAssessmentReadbackError,"status"):
                    verify_football_assessment(receipt,tampered)
                tampered=copy.deepcopy(readback)
                tampered["engine_c2_result"]={"made_up":"shadow"}
                with self.assertRaisesRegex(XIAssessmentReadbackError,"C/C2 result differs"):
                    verify_football_assessment(receipt,tampered)


if __name__=="__main__":
    unittest.main()
