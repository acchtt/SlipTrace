from __future__ import annotations

from dataclasses import dataclass
from typing import Any


WATCH_ASSUMED_ODDS = 1.65
DEFAULT_STAKE_U = 1.0
ACTIVE_MODELS = ("c", "c2")
HISTORICAL_MODELS = ("c", "c2", "c3", "c4")
MODELS = set(HISTORICAL_MODELS)


class ModelBetAccountingError(ValueError):
    pass


@dataclass(frozen=True)
class BetTerms:
    basis: str
    line: float | None
    odds: float | None
    stake_u: float
    scope: str
    synthetic_price: bool
    creates_website_pick: bool
    source_stage: str


def _is_watch(state: str | None) -> bool:
    return isinstance(state, str) and state.upper().endswith("-WATCH")


def _action_suffix(action: str | None) -> str | None:
    if not isinstance(action, str) or not action.strip():
        return None
    action = action.upper().strip()
    if action.endswith("-BET"):
        return "BET"
    if action.endswith("-WAIT"):
        return "WAIT"
    if action.endswith("-PASS"):
        return "PASS"
    raise ModelBetAccountingError(f"unsupported Step-2 action {action!r}")


def _line(value: Any, field: str) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ModelBetAccountingError(f"{field} must be numeric or null")
    value = float(value)
    if value < 0 or abs(value * 4 - round(value * 4)) > 1e-9:
        raise ModelBetAccountingError(f"{field} must be a non-negative quarter line")
    return value


def _odds(value: Any, field: str) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ModelBetAccountingError(f"{field} must be numeric or null")
    value = float(value)
    if value <= 1:
        raise ModelBetAccountingError(f"{field} must be > 1")
    return value


def _stake(value: Any) -> float:
    if value is None:
        return DEFAULT_STAKE_U
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ModelBetAccountingError("stake_u must be numeric")
    value = float(value)
    if value <= 0:
        raise ModelBetAccountingError("stake_u must be > 0")
    return value


def compile_model_bet(row: dict[str, Any]) -> BetTerms:
    if not isinstance(row, dict):
        raise ModelBetAccountingError("model row must be an object")

    model = str(row.get("model", "")).lower().strip()
    if model not in MODELS:
        raise ModelBetAccountingError(f"model must be one of {sorted(MODELS)}")

    board_state = row.get("board_state")
    supported_line = _line(row.get("supported_line"), "supported_line")
    action = _action_suffix(row.get("step2_action"))

    direct_line = _line(row.get("direct_line"), "direct_line")
    direct_odds = _odds(row.get("direct_odds"), "direct_odds")
    wait_target_line = _line(row.get("wait_target_line"), "wait_target_line")
    wait_min_odds = _odds(row.get("wait_min_odds"), "wait_min_odds")
    wait_resolution = row.get("wait_resolution") or "ASSUMED_REACHED"
    stake_u = _stake(row.get("stake_u"))

    scope = "OFFICIAL_MODEL_ACCOUNTING" if model == "c" else "SHADOW_MODEL_ACCOUNTING"

    # Highest-resolution direct bet always wins.
    if action == "BET":
        if direct_line is None or direct_odds is None:
            raise ModelBetAccountingError(
                f"{model}: direct BET requires direct_line and direct_odds"
            )
        return BetTerms(
            basis="DIRECT_BET" if model == "c" else "SHADOW_DIRECT_BET",
            line=direct_line,
            odds=direct_odds,
            stake_u=stake_u,
            scope=scope,
            synthetic_price=False,
            creates_website_pick=model == "c",
            source_stage="STEP2",
        )

    # WAIT replaces WATCH when it is a countable WAIT. If the user explicitly
    # says the line never reached, the WAIT is removed and the frozen WATCH,
    # when present, remains independently countable under the user's policy.
    if action == "WAIT" and wait_resolution != "USER_DECLARED_NOT_REACHED":
        if wait_resolution == "USER_CONFIRMED":
            if model != "c":
                raise ModelBetAccountingError(
                    "USER_CONFIRMED WAIT reconciliation is only valid for official Football C"
                )
            actual_line = _line(row.get("user_confirmed_line"), "user_confirmed_line")
            actual_odds = _odds(row.get("user_confirmed_odds"), "user_confirmed_odds")
            if actual_line is None or actual_odds is None:
                raise ModelBetAccountingError(
                    "USER_CONFIRMED WAIT requires user_confirmed_line and user_confirmed_odds"
                )
            return BetTerms(
                basis="WAIT_USER_CONFIRMED",
                line=actual_line,
                odds=actual_odds,
                stake_u=_stake(row.get("user_confirmed_stake_u")),
                scope=scope,
                synthetic_price=False,
                creates_website_pick=True,
                source_stage="STEP2",
            )

        if wait_target_line is None or wait_min_odds is None:
            raise ModelBetAccountingError(
                f"{model}: WAIT requires wait_target_line and wait_min_odds"
            )
        return BetTerms(
            basis="WAIT_ASSUMED" if model == "c" else "SHADOW_WAIT_ASSUMED",
            line=wait_target_line,
            odds=wait_min_odds,
            stake_u=stake_u,
            scope=scope,
            synthetic_price=False,
            creates_website_pick=model == "c",
            source_stage="STEP2",
        )

    # WATCH is an audit/accounting bet for every model. It never creates a
    # Website Pick or real/user exposure by itself.
    if _is_watch(board_state):
        if supported_line is None:
            raise ModelBetAccountingError(
                f"{model}: WATCH accounting requires supported_line"
            )
        return BetTerms(
            basis="WATCH_ASSUMED" if model == "c" else "SHADOW_WATCH_ASSUMED",
            line=supported_line,
            odds=WATCH_ASSUMED_ODDS,
            stake_u=DEFAULT_STAKE_U,
            scope=scope,
            synthetic_price=True,
            creates_website_pick=False,
            source_stage="STEP1",
        )

    return BetTerms(
        basis="NONE",
        line=None,
        odds=None,
        stake_u=0.0,
        scope=scope,
        synthetic_price=False,
        creates_website_pick=False,
        source_stage="NONE",
    )


def _money(value: float) -> float:
    """Keep deterministic accounting output free of binary-float artifacts."""
    return round(float(value), 6)


def _single_over_pnl(total_goals: int, line: float, odds: float, stake: float) -> tuple[str, float]:
    if total_goals > line:
        return "WIN", _money(stake * (odds - 1.0))
    if total_goals == line:
        return "PUSH", 0.0
    return "LOSS", _money(-stake)


def settle_over(total_goals: int, line: float, odds: float, stake_u: float) -> tuple[str, float]:
    if isinstance(total_goals, bool) or not isinstance(total_goals, int) or total_goals < 0:
        raise ModelBetAccountingError("total_goals must be a non-negative integer")

    quarter = int(round(line * 4)) % 4
    if quarter in {0, 2}:
        return _single_over_pnl(total_goals, line, odds, stake_u)

    lower = line - 0.25
    upper = line + 0.25
    low_result, low_pnl = _single_over_pnl(total_goals, lower, odds, stake_u / 2.0)
    high_result, high_pnl = _single_over_pnl(total_goals, upper, odds, stake_u / 2.0)

    pair = (low_result, high_result)
    if pair == ("WIN", "WIN"):
        settlement = "WIN"
    elif set(pair) == {"WIN", "PUSH"}:
        settlement = "HALF_WIN"
    elif pair == ("PUSH", "PUSH"):
        settlement = "PUSH"
    elif set(pair) == {"LOSS", "PUSH"}:
        settlement = "HALF_LOSS"
    elif pair == ("LOSS", "LOSS"):
        settlement = "LOSS"
    else:
        # This should be unreachable for adjacent quarter components.
        raise ModelBetAccountingError(f"unexpected split settlement {pair}")

    return settlement, _money(low_pnl + high_pnl)


def compile_fixture_accounting(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ModelBetAccountingError("payload must be an object")

    match_id = payload.get("match_id")
    if not isinstance(match_id, str) or not match_id.strip():
        raise ModelBetAccountingError("match_id must be non-empty")

    historical_roster = payload.get("historical_roster", False)
    if not isinstance(historical_roster, bool):
        raise ModelBetAccountingError("historical_roster must be boolean")
    required_models = HISTORICAL_MODELS if historical_roster else ACTIVE_MODELS

    rows = payload.get("models")
    if not isinstance(rows, list) or not rows:
        raise ModelBetAccountingError("models must be a non-empty array")

    by_model: dict[str, dict[str, Any]] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise ModelBetAccountingError("models entries must be objects")
        model = str(row.get("model", "")).lower().strip()
        if model in by_model:
            raise ModelBetAccountingError(f"duplicate model row {model!r}")
        by_model[model] = row

    extra = set(by_model) - set(required_models)
    if extra:
        if historical_roster:
            raise ModelBetAccountingError(
                f"historical accounting has unsupported model rows: {sorted(extra)}"
            )
        raise ModelBetAccountingError(
            "active accounting permits C/C2 only; "
            f"retired/unsupported rows={sorted(extra)}"
        )

    missing = set(required_models) - set(by_model)
    if missing:
        roster = "C/C2/C3/C4" if historical_roster else "C/C2"
        raise ModelBetAccountingError(
            f"{roster} accounting requires complete roster; missing={sorted(missing)}"
        )

    total_goals = payload.get("total_goals")
    if total_goals is not None:
        if isinstance(total_goals, bool) or not isinstance(total_goals, int) or total_goals < 0:
            raise ModelBetAccountingError("total_goals must be null or a non-negative integer")

    results: list[dict[str, Any]] = []
    for model in required_models:
        terms = compile_model_bet(by_model[model])
        settlement = "PENDING" if terms.basis != "NONE" else "NO_BET"
        pnl_u: float | None = None if terms.basis != "NONE" else 0.0
        if total_goals is not None and terms.basis != "NONE":
            settlement, pnl_u = settle_over(
                total_goals,
                terms.line,
                terms.odds,
                terms.stake_u,
            )

        results.append(
            {
                "model": model,
                "basis": terms.basis,
                "line": terms.line,
                "odds": terms.odds,
                "stake_u": terms.stake_u,
                "scope": terms.scope,
                "synthetic_price": terms.synthetic_price,
                "creates_website_pick": terms.creates_website_pick,
                "source_stage": terms.source_stage,
                "settlement": settlement,
                "pnl_u": pnl_u,
            }
        )

    return {
        "schema_version": "football-model-accounting-v1",
        "stage": "model_accounting_result",
        "match_id": match_id.strip(),
        "roster": (
            "HISTORICAL_C_C2_C3_C4"
            if historical_roster
            else "ACTIVE_C_C2"
        ),
        "watch_assumed_odds": WATCH_ASSUMED_ODDS,
        "models": results,
    }
