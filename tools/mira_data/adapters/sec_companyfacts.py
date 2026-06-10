"""SEC EDGAR companyfacts adapter -> canonical ``company_financials``.

Official, keyless (a descriptive User-Agent is required). Values are
issuer-disclosed reported metrics: ``derived=False``, so no calculation ledger
is required (arch doc §8). Mira-computed ratios/deltas are a separate, later
concern that must be emitted as ``derived_calculation`` rows.
"""

from __future__ import annotations

import datetime as _dt
from typing import Optional

from .. import config, net
from ..canonical import POSTURES, CanonicalRecord, FetchResult

TICKER_MAP_URL = "https://www.sec.gov/files/company_tickers.json"
COMPANYFACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik10}.json"


def _require_contact() -> None:
    """SEC requires a real contact User-Agent; refuse to fetch under a placeholder."""
    if not config.is_contact_configured():
        raise net.FetchError(
            "SEC official-data fetch needs a real contact. " + config.config_hint()
        )

# Curated snapshot tags: (canonical_metric, taxonomy, kind, [candidate tags]).
# kind drives period selection: "instant" = balance-sheet point-in-time (pick
# latest end); "duration" = flow metric (pick latest clean QUARTER, else annual,
# explicitly skipping 6-/9-month YTD rows that share the same tag).
# Among present candidate tags, the one with the most recent observation wins,
# so issuer tag drift is tolerated and an abandoned tag never shadows the live one.
CURATED_TAGS: list[tuple[str, str, str, list[str]]] = [
    ("revenue", "us-gaap", "duration", ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet"]),
    ("gross_profit", "us-gaap", "duration", ["GrossProfit"]),
    ("operating_income", "us-gaap", "duration", ["OperatingIncomeLoss"]),
    ("net_income", "us-gaap", "duration", ["NetIncomeLoss"]),
    ("rnd_expense", "us-gaap", "duration", ["ResearchAndDevelopmentExpense"]),
    ("operating_cash_flow", "us-gaap", "duration", ["NetCashProvidedByUsedInOperatingActivities"]),
    ("capex", "us-gaap", "duration", ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"]),
    ("total_assets", "us-gaap", "instant", ["Assets"]),
    ("total_liabilities", "us-gaap", "instant", ["Liabilities"]),
    ("stockholders_equity", "us-gaap", "instant", ["StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"]),
    ("cash_and_equivalents", "us-gaap", "instant", ["CashAndCashEquivalentsAtCarryingValue"]),
    ("long_term_debt", "us-gaap", "instant", ["LongTermDebtNoncurrent", "LongTermDebt"]),
    ("shares_outstanding", "dei", "instant", ["EntityCommonStockSharesOutstanding"]),
]


def resolve_cik(ticker: str) -> str:
    """Return the 10-digit zero-padded CIK for ``ticker`` (case-insensitive)."""
    _require_contact()
    data = net.get_json(TICKER_MAP_URL)
    want = ticker.strip().upper()
    for row in data.values():
        if str(row.get("ticker", "")).upper() == want:
            return f"{int(row['cik_str']):010d}"
    raise net.FetchError(f"ticker not found in SEC company_tickers.json: {ticker}")


def load_facts(ticker: str, cik: Optional[str] = None) -> tuple[str, dict, str]:
    """Fetch raw companyfacts: returns ``(cik10, facts, url)``. Gated on contact."""
    _require_contact()
    cik10 = cik or resolve_cik(ticker)
    url = COMPANYFACTS_URL.format(cik10=cik10)
    facts = net.get_json(url).get("facts", {})
    return cik10, facts, url


def metric_observations(facts: dict, metric: str) -> list[dict]:
    """All observations for a curated metric, sorted by period end then filed.

    Each obs carries ``_unit``, ``_span`` (days, or None for instant) and ``_tag``.
    Lets callers build YoY / QoQ / CAGR from a real series, not just the latest.
    """
    spec = next((s for s in CURATED_TAGS if s[0] == metric), None)
    if spec is None:
        return []
    _, taxonomy, _kind, candidates = spec
    block = _first_present(facts.get(taxonomy, {}), candidates)
    if block is None:
        return []
    obs = []
    for unit, rows in block["units"].items():
        for row in rows:
            if "end" not in row or "val" not in row:
                continue
            obs.append({**row, "_unit": unit, "_span": _span_days(row.get("start"), row.get("end")),
                        "_tag": block["_tag"]})
    return sorted(obs, key=lambda r: (r.get("end", ""), r.get("filed", "")))


def fetch_company_financials(
    ticker: str,
    *,
    as_of: Optional[str] = None,
    market_scope: str = "US",
    cik: Optional[str] = None,
) -> FetchResult:
    """Fetch a curated financial snapshot as canonical reported metrics."""
    as_of = as_of or _dt.date.today().isoformat()
    cik10, facts, url = load_facts(ticker, cik)
    posture = POSTURES["sec_companyfacts"]

    records: list[CanonicalRecord] = []
    for metric, taxonomy, kind, candidates in CURATED_TAGS:
        tagblock = _first_present(facts.get(taxonomy, {}), candidates)
        if tagblock is None:
            continue
        unit, obs = _select_observation(tagblock, kind)
        if obs is None:
            continue
        records.append(
            CanonicalRecord(
                family="company_financials",
                research_object=ticker.upper(),
                market_scope=market_scope,
                metric=metric,
                value=obs["val"],
                unit=unit,
                currency="USD" if unit == "USD" else None,
                period=_period_label(obs),
                period_type="fiscal_period",
                as_of_date=as_of,
                source_date=obs.get("filed", as_of),
                posture=posture,
                url_or_path=url,
                provenance={
                    "cik": cik10,
                    "tag": obs["_tag"],
                    "taxonomy": taxonomy,
                    "fy": obs.get("fy"),
                    "fp": obs.get("fp"),
                    "form": obs.get("form"),
                    "accn": obs.get("accn"),
                    "period_end": obs.get("end"),
                },
            )
        )
    if not records:
        raise net.FetchError(f"no curated facts extracted for {ticker} ({cik10})")
    return FetchResult(records)


def _first_present(taxonomy_block: dict, candidates: list[str]) -> Optional[dict]:
    """Pick the candidate tag with the most recent observation end.

    Issuers drift between tags over time (e.g. NVDA stopped filing
    PaymentsToAcquirePropertyPlantAndEquipment in 2011 and now uses
    PaymentsToAcquireProductiveAssets); candidate order alone would let the
    abandoned tag shadow the live one and surface decade-old values as latest.
    """
    best: Optional[dict] = None
    best_end = ""
    for tag in candidates:
        block = taxonomy_block.get(tag)
        if not (block and block.get("units")):
            continue
        last_end = max((row.get("end", "") for rows in block["units"].values()
                        for row in rows), default="")
        if last_end > best_end:
            best = dict(block)
            best["_tag"] = tag
            best_end = last_end
    return best


def _select_observation(tagblock: dict, kind: str) -> tuple[str, Optional[dict]]:
    """Pick the right observation for ``kind`` (period-aware).

    instant  -> latest by period end (balance-sheet point-in-time).
    duration -> latest clean quarter (~3-month span), else latest annual
                (~12-month). 6-/9-month YTD rows are skipped so a cumulative
                value is never mislabeled as a quarter.
    """
    candidates: list[tuple[str, dict]] = []
    for unit, rows in tagblock["units"].items():
        for row in rows:
            if "end" not in row or "val" not in row:
                continue
            if kind == "duration":
                span = _span_days(row.get("start"), row.get("end"))
                if span is None or not (_is_quarter(span) or _is_annual(span)):
                    continue
            candidates.append((unit, row))
    if not candidates:
        return "", None

    if kind == "duration":
        # prefer a clean quarter; within the chosen pool, latest end then filed.
        quarters = [c for c in candidates if _is_quarter(_span_days(c[1].get("start"), c[1].get("end")) or 0)]
        pool = quarters or candidates
        unit, row = max(pool, key=lambda c: (c[1].get("end", ""), c[1].get("filed", "")))
    else:
        unit, row = max(candidates, key=lambda c: (c[1].get("end", ""), c[1].get("filed", "")))

    obs = dict(row)
    obs["_tag"] = tagblock["_tag"]
    obs["_kind"] = kind
    return unit, obs


def _span_days(start: Optional[str], end: Optional[str]) -> Optional[int]:
    if not start or not end:
        return None
    try:
        d0 = _dt.date.fromisoformat(start)
        d1 = _dt.date.fromisoformat(end)
    except ValueError:
        return None
    return (d1 - d0).days


def _is_quarter(span: int) -> bool:
    return 80 <= span <= 100


def _is_annual(span: int) -> bool:
    return 350 <= span <= 380


def _period_label(obs: dict) -> str:
    fy, fp = obs.get("fy"), obs.get("fp")
    if fy and fp == "FY":
        return f"FY{fy}"
    if fy and fp:
        return f"FY{fy} {fp}"
    return obs.get("end", "unknown")
