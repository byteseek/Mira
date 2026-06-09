"""Fundamental deltas (YoY / CAGR) as Mira-derived, ledgered records.

Consumes SEC companyfacts series and computes growth metrics. These are
Mira-computed numbers that affect judgment, so each emits a
``derived_calculation`` evidence row + calculation-ledger row (§8) — unlike the
issuer-disclosed snapshot values, which are reported and need no ledger.

QoQ is deliberately omitted: companyfacts files Q2/Q3 flow metrics on a
year-to-date basis, so a naive consecutive-period ratio would be wrong. YoY
matches the same fiscal period across years (same span), which is correct.
"""

from __future__ import annotations

import datetime as _dt
from typing import Optional

from . import net
from .adapters import sec_companyfacts as scf
from .canonical import POSTURES, CanonicalRecord

_ANNUAL = (350, 380)


def compute_deltas(ticker: str, *, as_of: Optional[str] = None,
                   market_scope: str = "US") -> list[CanonicalRecord]:
    as_of = as_of or _dt.date.today().isoformat()
    _, facts, _url = scf.load_facts(ticker)
    rev = scf.metric_observations(facts, "revenue")
    ni = scf.metric_observations(facts, "net_income")

    out: list[CanonicalRecord] = []
    out += _yoy_record(ticker, as_of, market_scope, "revenue", rev)
    out += _yoy_record(ticker, as_of, market_scope, "net_income", ni)
    out += _cagr_record(ticker, as_of, market_scope, "revenue", rev, years=3)
    if not out:
        raise net.FetchError(f"source_gap: insufficient companyfacts history for {ticker} deltas")
    return out


def _yoy_record(ticker, as_of, market_scope, metric, obs) -> list:
    res = _yoy(obs)
    if res is None:
        return []
    value, latest, base = res
    period = f"FY{latest.get('fy')} {latest.get('fp')}"
    base_period = f"FY{base.get('fy')} {base.get('fp')}"
    return [_derived(
        ticker, as_of, market_scope, f"{metric}_yoy", value,
        formula=f"{metric}({period}) / {metric}({base_period}) - 1",
        note=f"{period} vs {base_period}, same-period basis",
    )]


def _cagr_record(ticker, as_of, market_scope, metric, obs, years) -> list:
    res = _cagr(obs, years)
    if res is None:
        return []
    value, latest, base = res
    period = f"FY{latest.get('fy')}"
    base_period = f"FY{base.get('fy')}"
    return [_derived(
        ticker, as_of, market_scope, f"{metric}_cagr_{years}y", value,
        formula=f"({metric}({period}) / {metric}({base_period}))^(1/{years}) - 1",
        note=f"{years}-year annual CAGR {base_period}->{period}",
    )]


def _yoy(obs: list):
    if len(obs) < 2:
        return None
    latest = obs[-1]
    fp, span, fy = latest.get("fp"), latest.get("_span"), latest.get("fy")
    if fy is None or not latest.get("val"):
        return None
    for r in reversed(obs[:-1]):
        if (r.get("fp") == fp and r.get("fy") == fy - 1
                and _similar_span(r.get("_span"), span) and r.get("val")):
            return latest["val"] / r["val"] - 1.0, latest, r
    return None


def _cagr(obs: list, years: int):
    by_fy = {}
    for r in obs:
        span = r.get("_span")
        if span and _ANNUAL[0] <= span <= _ANNUAL[1] and r.get("fy") is not None:
            by_fy[r["fy"]] = r  # sorted asc, so latest filing for the fy wins
    series = [by_fy[k] for k in sorted(by_fy)]
    if len(series) <= years:
        return None
    latest, base = series[-1], series[-1 - years]
    if base.get("val", 0) > 0 and latest.get("val", 0) > 0:
        return (latest["val"] / base["val"]) ** (1.0 / years) - 1.0, latest, base
    return None


def _similar_span(a, b) -> bool:
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return abs(a - b) <= 10


def _derived(ticker, as_of, market_scope, metric, value, *, formula, note) -> CanonicalRecord:
    return CanonicalRecord(
        family="company_financials", research_object=ticker.upper(), market_scope=market_scope,
        metric=metric, value=round(value, 6), unit="ratio", period=as_of,
        period_type="point_in_time", as_of_date=as_of, source_date=as_of,
        posture=POSTURES["sec_companyfacts"], url_or_path="derived://tools/mira_data/fundamentals",
        derived=True, upstream_sources="sec_companyfacts_api", formula=formula,
        cross_check=note,
        claim_text=f"{ticker.upper()} {metric} = {round(value, 6)} (derived from SEC companyfacts; {note})",
    )
