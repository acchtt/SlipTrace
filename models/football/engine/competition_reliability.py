from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable


COUNTABLE_TYPES = {"STEP2_OBSERVED", "SCHEDULE_INTEGRITY"}
VALID_STATES = {"UNPROVEN", "TRUSTED", "NEUTRAL", "CAUTION", "DEMOTED"}
VALID_GRADES = {"A", "B", "C", "D"}


@dataclass(frozen=True)
class ReliabilitySummary:
    state: str
    rolling_sample: int
    xi_usable_rate: float | None
    market_usable_rate: float | None
    team_news_usable_rate: float | None
    step2_completion_rate: float | None
    identity_time_faults: int
    consecutive_critical_failures: int
    reasons: tuple[str, ...]


def _norm(value: Any) -> str:
    return str(value or "").strip().upper().replace("-", "_").replace(" ", "_")


def _rate(events: Iterable[dict[str, Any]], field: str, usable: set[str], checked: set[str]) -> tuple[float | None, int]:
    values = [_norm(event.get(field)) for event in events]
    values = [value for value in values if value in checked]
    if not values:
        return None, 0
    return sum(value in usable for value in values) / len(values), len(values)


def is_critical_failure(event: dict[str, Any]) -> bool:
    return (
        _norm(event.get("xi_outcome")) == "MISSING"
        or _norm(event.get("market_outcome")) in {"STALE_OR_VANISHED", "UNAVAILABLE"}
        or _norm(event.get("identity_time_outcome")) == "FAULT"
        or _norm(event.get("step2_outcome")) == "PROCESS_MISSING"
    )


def evaluate_competition_reliability(
    events: Iterable[dict[str, Any]],
    *,
    window: int = 10,
) -> ReliabilitySummary:
    countable = [
        dict(event)
        for event in events
        if _norm(event.get("observation_type")) in COUNTABLE_TYPES
    ]
    countable.sort(key=lambda event: str(event.get("observed_at") or ""), reverse=True)
    sample = countable[:window]

    xi_rate, xi_n = _rate(
        sample,
        "xi_outcome",
        {"USABLE"},
        {"USABLE", "LATE", "MISSING"},
    )
    market_rate, market_n = _rate(
        sample,
        "market_outcome",
        {"USABLE"},
        {"USABLE", "THIN", "STALE_OR_VANISHED", "UNAVAILABLE"},
    )
    news_rate, news_n = _rate(
        sample,
        "team_news_outcome",
        {"USABLE"},
        {"USABLE", "LIMITED", "UNAVAILABLE"},
    )
    step2_rate, step2_n = _rate(
        sample,
        "step2_outcome",
        {"COMPLETED"},
        {"COMPLETED", "BLOCKED_XI", "BLOCKED_MARKET", "PROCESS_MISSING"},
    )

    identity_faults = sum(
        _norm(event.get("identity_time_outcome")) == "FAULT" for event in sample
    )

    consecutive_critical = 0
    for event in sample:
        if is_critical_failure(event):
            consecutive_critical += 1
        else:
            break

    if len(sample) < 3:
        return ReliabilitySummary(
            state="UNPROVEN",
            rolling_sample=len(sample),
            xi_usable_rate=xi_rate,
            market_usable_rate=market_rate,
            team_news_usable_rate=news_rate,
            step2_completion_rate=step2_rate,
            identity_time_faults=identity_faults,
            consecutive_critical_failures=consecutive_critical,
            reasons=("fewer than 3 countable observations",),
        )

    demotion_reasons: list[str] = []
    if len(sample) >= 4:
        if xi_n >= 3 and xi_rate is not None and xi_rate < 0.50:
            demotion_reasons.append("XI usable rate below 50%")
        if market_n >= 3 and market_rate is not None and market_rate < 0.50:
            demotion_reasons.append("market usable rate below 50%")
        if step2_n >= 3 and step2_rate is not None and step2_rate < 0.50:
            demotion_reasons.append("Step-2 completion rate below 50%")
        if identity_faults >= 2:
            demotion_reasons.append("at least two identity/time faults")
        if consecutive_critical >= 3:
            demotion_reasons.append("at least three consecutive critical failures")

    if demotion_reasons:
        return ReliabilitySummary(
            "DEMOTED", len(sample), xi_rate, market_rate, news_rate, step2_rate,
            identity_faults, consecutive_critical, tuple(demotion_reasons)
        )

    caution_reasons: list[str] = []
    if xi_n >= 3 and xi_rate is not None and xi_rate < 0.75:
        caution_reasons.append("XI usable rate below 75%")
    if market_n >= 3 and market_rate is not None and market_rate < 0.75:
        caution_reasons.append("market usable rate below 75%")
    if news_n >= 3 and news_rate is not None and news_rate < 0.60:
        caution_reasons.append("team-news usable rate below 60%")
    if step2_n >= 3 and step2_rate is not None and step2_rate < 0.75:
        caution_reasons.append("Step-2 completion rate below 75%")
    if identity_faults >= 1:
        caution_reasons.append("identity/time fault present")
    if consecutive_critical >= 2:
        caution_reasons.append("at least two consecutive critical failures")

    if caution_reasons:
        return ReliabilitySummary(
            "CAUTION", len(sample), xi_rate, market_rate, news_rate, step2_rate,
            identity_faults, consecutive_critical, tuple(caution_reasons)
        )

    trusted = (
        len(sample) >= 5
        and xi_n >= 4
        and market_n >= 4
        and news_n >= 4
        and step2_n >= 4
        and xi_rate is not None and xi_rate >= 0.85
        and market_rate is not None and market_rate >= 0.85
        and news_rate is not None and news_rate >= 0.70
        and step2_rate is not None and step2_rate >= 0.85
        and identity_faults == 0
        and consecutive_critical == 0
    )
    if trusted:
        return ReliabilitySummary(
            "TRUSTED", len(sample), xi_rate, market_rate, news_rate, step2_rate,
            identity_faults, consecutive_critical, ("all trusted thresholds cleared",)
        )

    return ReliabilitySummary(
        "NEUTRAL", len(sample), xi_rate, market_rate, news_rate, step2_rate,
        identity_faults, consecutive_critical, ("no caution/demotion trigger",)
    )


def effective_state(state: str, manual_override: str = "NONE") -> str:
    state = _norm(state)
    override = _norm(manual_override)
    if override and override != "NONE":
        if override not in VALID_STATES:
            raise ValueError(f"invalid manual override: {manual_override!r}")
        return override
    if state not in VALID_STATES:
        raise ValueError(f"invalid reliability state: {state!r}")
    return state


def apply_reliability_cap(
    raw_grade: str,
    state: str,
    *,
    demoted_probation: bool = False,
) -> str:
    """Apply history only as a cap. Never promote the current raw grade."""

    grade = _norm(raw_grade)
    state = _norm(state)
    if grade not in VALID_GRADES:
        raise ValueError(f"invalid operational grade: {raw_grade!r}")
    if state not in VALID_STATES:
        raise ValueError(f"invalid reliability state: {state!r}")

    if state in {"UNPROVEN", "TRUSTED", "NEUTRAL"}:
        return grade

    if state == "CAUTION":
        return "B" if grade == "A" else grade

    if state == "DEMOTED":
        if demoted_probation and grade == "A":
            return "B"
        return "C" if grade in {"A", "B"} else grade

    raise AssertionError(state)
