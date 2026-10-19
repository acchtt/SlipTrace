"""Shared registry scope at runtime boundaries; explicit overrides are analysis only."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'stages_v4'))
from league_registry import classify

POLICY = 'FOOTBALL_C_SCOPE_V1'


def scope_profile(match, context=None):
    context = context or {}
    fields = ('country', 'competition', 'competition_kind')
    if not all(isinstance(match.get(k), str) and match[k].strip() for k in fields):
        return {'policy': POLICY, 'status': 'SCOPE_UNVERIFIED', 'reason': 'COUNTRY_COMPETITION_KIND_REQUIRED', 'production_allowed': False}
    decision = classify(match)
    allowed = decision['lane'] not in {'EXCLUDED', 'UNVERIFIED'}
    override = context.get('scope_override')
    explicit = (isinstance(override, dict) and override.get('match_id') == match.get('match_id')
                and override.get('policy') == POLICY and override.get('authorization') == 'EXPLICIT_USER_SCOPE_EXCEPTION'
                and all(isinstance(override.get(k), str) and override[k].strip() for k in ('user_instruction_reference', 'basis')))
    return {'policy': POLICY, 'status': 'IN_SCOPE' if allowed else 'EXPLICIT_OUT_OF_SCOPE_ANALYSIS' if explicit else 'SCOPE_EXCLUDED',
            'reason': decision['reason'], 'production_allowed': allowed,
            'override': override if explicit and not allowed else None}
