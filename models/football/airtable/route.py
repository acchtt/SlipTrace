"""RETIRED Airtable router.

Google Sheets became the active Football v2 operational store on 2026-10-15.
Airtable is historical read-only. New football workflows must import
models/football/google_sheets/route.py instead.
"""

from __future__ import annotations


class AirtableRouteError(ValueError):
    pass


def _configuration():
    return {
        "schema_version": "football-airtable-routing-retired-v1",
        "active": False,
        "policy": "HISTORICAL_READ_ONLY_NO_NEW_WRITES",
        "redirect": "models/football/google_sheets/ACTIVE_STORE_ROUTING.json",
    }


def resolve_table(*args, **kwargs):
    raise AirtableRouteError(
        "AIRTABLE_RETIRED: new Football v2 writes/readbacks use Google Sheets"
    )


def verify_receipt(*args, **kwargs):
    raise AirtableRouteError(
        "AIRTABLE_RETIRED: active persistence receipts must come from Google Sheets"
    )
