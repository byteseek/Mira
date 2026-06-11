"""Generic equity screening over an explicit candidate list.

Fills the ``discovery_or_screening`` execution gap for "screen US equities on
fundamental criteria" (e.g. high FCF yield, low leverage). Deliberately lite
(architecture/data-acquisition-upgrade.md §0):

- universe = an explicit candidate list (≤ ``MAX_TICKERS``), never a
  whole-market crawl (DATA_POLICY: on-demand read, no bulk crawling);
- dimensions = only what the existing substrate already supports — SEC
  companyfacts flows/balances (L2) plus the Yahoo last close (L5) for
  market cap;
- flow metrics use the latest complete fiscal year, sidestepping the
  companyfacts Q2/Q3 year-to-date trap (see fundamentals.py);
- results are screening-grade: Mira-derived ratios are L6 ``derived_calculation``
  records (ledgered, per §8) over L2+L5 upstreams. Verify against filings
  before any durable use.

A ticker whose data cannot be fetched degrades to ``screen_status=data_gap``;
if every candidate degrades, the run raises ``FetchError`` so the caller falls
back to the routing rule (watchlist note + ``source_gap``, never an improvised
screen result).
"""

from __future__ import annotations

import csv
import datetime as _dt
import os
import time
from dataclasses import dataclass, field
from typing import Optional

from . import net
from .adapters import sec_companyfacts as scf
from .adapters import yahoo_chart
from .canonical import POSTURES, CanonicalRecord
from .fundamentals import _yoy

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_TEMPLATE = os.path.join(_REPO_ROOT, "templates", "screening-watchlist.csv")

MAX_TICKERS = 30      # bounded candidate triage, not a market crawl (DATA_POLICY)
_PAUSE_SECONDS = 0.4  # polite inter-ticker pacing (SEC fair-access cap is 10 req/s)
_STALE_DAYS = 550     # ~18 months: the latest complete FY can lag ~15 months; older
                      # observations must degrade to data_gap, not anchor a ratio
                      # against today's market cap (an issuer's discontinued metric
                      # would otherwise silently mix decade-old flows with a live price).

# criterion flag -> (metric column, direction). The metric set is exactly what
# the existing fundamentals + market_price adapters can compute — adding a
# criterion here must not require a new data channel.
CRITERIA: dict[str, tuple[str, str]] = {
    "min_market_cap": ("market_cap_usd", "min"),
    "min_fcf_yield": ("fcf_yield", "min"),
    "max_debt_to_equity": ("debt_to_equity", "max"),
    "min_net_margin": ("net_margin", "min"),
    "min_revenue_yoy": ("revenue_yoy", "min"),
}

_METRIC_COLUMNS = ("market_cap_usd", "fcf_yield", "debt_to_equity", "net_margin", "revenue_yoy")

_TIER_NOTE = ("screening_grade: SEC companyfacts L2 + Yahoo price L5; Mira-derived "
              "ratios L6 (ledgered); verify vs filings before durable use")

_NEXT_ACTION = {
    "pass": "single_equity_research_candidate",
    "fail": "rejected_by_screen",
    "data_gap": "source_gap_refresh",
}


@dataclass
class ScreenResult:
    rows: list            # watchlist rows (template schema), one per candidate
    derived: list = field(default_factory=list)  # ledgered records for passing tickers
    summary: dict = field(default_factory=dict)


def template_columns() -> list:
    with open(_TEMPLATE, encoding="utf-8") as fh:
        return next(csv.reader(fh))


def emit_watchlist_rows(out_dir: str, rows: list) -> str:
    """Append rows to ``<out_dir>/screening-watchlist.csv`` (template schema)."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "screening-watchlist.csv")
    cols = template_columns()
    exists = os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=cols)
        if not exists:
            writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return path


def screen_candidates(tickers: list, criteria: dict, *, as_of: Optional[str] = None,
                      market_scope: str = "US") -> ScreenResult:
    """Screen an explicit candidate list against fundamental criteria.

    ``criteria`` maps :data:`CRITERIA` flag names to thresholds. At least one
    criterion is required — a screen with no criteria is just a fetch.
    """
    if not criteria:
        raise ValueError("at least one screening criterion is required")
    unknown = sorted(set(criteria) - set(CRITERIA))
    if unknown:
        raise ValueError(f"unknown screening criteria: {unknown}")
    symbols = [t.strip().upper() for t in tickers if t and t.strip()]
    if not symbols:
        raise ValueError("empty candidate list")
    if len(symbols) > MAX_TICKERS:
        raise ValueError(
            f"candidate list too large ({len(symbols)} > {MAX_TICKERS}); screening is "
            "bounded candidate triage, not a market crawl — narrow the universe first")

    scf._require_contact()
    as_of = as_of or _dt.date.today().isoformat()
    cik_map = _cik_map(symbols)

    rows: list[dict] = []
    derived: list[CanonicalRecord] = []
    for i, sym in enumerate(symbols):
        if i:
            _pause()
        row, recs = _screen_one(sym, cik_map.get(sym), criteria, as_of, market_scope)
        rows.append(row)
        derived.extend(recs)

    if all(r["screen_status"] == "data_gap" for r in rows):
        raise net.FetchError(
            "source_gap: no candidate could be evaluated (all fetches failed or gated)")

    counts = {s: sum(1 for r in rows if r["screen_status"] == s)
              for s in ("pass", "fail", "data_gap")}
    summary = {"as_of": as_of, "criteria": _criteria_label(criteria),
               "n_candidates": len(rows), **counts}
    return ScreenResult(rows=rows, derived=derived, summary=summary)


# --- per-ticker evaluation ---------------------------------------------------

def _screen_one(sym: str, cik: Optional[str], criteria: dict, as_of: str,
                market_scope: str) -> tuple[dict, list]:
    if cik is None:
        return _row(sym, as_of, market_scope, "data_gap", criteria, {}, basis="",
                    price_as_of="source_gap", gaps=["sec_ticker_map"],
                    notes="not in SEC company_tickers.json (US registrants only)"), []
    try:
        _, facts, _url = scf.load_facts(sym, cik=cik)
    except net.FetchError as exc:
        return _row(sym, as_of, market_scope, "data_gap", criteria, {}, basis="",
                    price_as_of="source_gap", gaps=["companyfacts_fetch"],
                    notes=str(exc)[:160]), []

    obs = {m: scf.metric_observations(facts, m)
           for m in ("revenue", "net_income", "operating_cash_flow", "capex",
                     "long_term_debt", "stockholders_equity", "shares_outstanding")}

    gaps: list[str] = []
    price = price_date = None
    try:
        price, price_date = _last_close(sym)
    except net.FetchError:
        gaps.append("market_price")

    metrics: dict[str, float] = {}
    formulas: dict[str, tuple[str, str]] = {}  # metric -> (formula, upstream_kind)
    basis_bits: list[str] = []

    shares = _latest_instant(obs["shares_outstanding"])
    if price is not None and shares is not None and _fresh(shares, as_of):
        metrics["market_cap_usd"] = price * shares["val"]
        formulas["market_cap_usd"] = (
            f"last_close({price_date}) * shares_outstanding({shares['end']})", "sec+yahoo")

    fy, ocf, capex = _common_annual(obs["operating_cash_flow"], obs["capex"])
    if (ocf is not None and capex is not None and metrics.get("market_cap_usd")
            and _fresh(ocf, as_of)):
        metrics["fcf_yield"] = (ocf["val"] - capex["val"]) / metrics["market_cap_usd"]
        formulas["fcf_yield"] = (
            f"(operating_cash_flow(FY{fy}) - capex(FY{fy})) / market_cap_usd", "sec+yahoo")
        basis_bits.append(f"flows FY{fy}")

    debt = _latest_instant(obs["long_term_debt"])
    equity = _latest_instant(obs["stockholders_equity"])
    if (debt is not None and equity is not None and equity["val"]
            and _fresh(debt, as_of) and _fresh(equity, as_of)):
        metrics["debt_to_equity"] = debt["val"] / equity["val"]
        formulas["debt_to_equity"] = (
            f"long_term_debt({debt['end']}) / stockholders_equity({equity['end']})", "sec")
        basis_bits.append(f"balance {equity['end']}")

    fy_m, ni, rev = _common_annual(obs["net_income"], obs["revenue"])
    if ni is not None and rev is not None and rev["val"] and _fresh(rev, as_of):
        metrics["net_margin"] = ni["val"] / rev["val"]
        formulas["net_margin"] = (f"net_income(FY{fy_m}) / revenue(FY{fy_m})", "sec")

    yoy = _yoy(obs["revenue"])
    if yoy is not None and _fresh(yoy[1], as_of):
        value, latest, base = yoy
        metrics["revenue_yoy"] = value
        formulas["revenue_yoy"] = (
            f"revenue(FY{latest.get('fy')} {latest.get('fp')}) / "
            f"revenue(FY{base.get('fy')} {base.get('fp')}) - 1", "sec")

    if price_date:
        basis_bits.append(f"price {price_date}")

    status, gap_criteria = _evaluate(criteria, metrics)
    gaps.extend(gap_criteria)

    row = _row(sym, as_of, market_scope, status, criteria, metrics,
               basis="; ".join(basis_bits) or "source_gap",
               price_as_of=price_date or "source_gap", gaps=gaps)
    recs = _derived_records(sym, as_of, market_scope, metrics, formulas) if status == "pass" else []
    return row, recs


def _evaluate(criteria: dict, metrics: dict) -> tuple[str, list]:
    failed, gap = [], []
    for name, threshold in criteria.items():
        metric, direction = CRITERIA[name]
        value = metrics.get(metric)
        if value is None:
            gap.append(metric)
            continue
        ok = value >= threshold if direction == "min" else value <= threshold
        if not ok:
            failed.append(name)
    if failed:
        return "fail", gap
    if gap:
        return "data_gap", gap
    return "pass", gap


def _row(sym, as_of, market_scope, status, criteria, metrics, *, basis,
         price_as_of, gaps, notes="") -> dict:
    row = {
        "screened_date": as_of,
        "ticker": sym,
        "market_scope": market_scope,
        "screen_status": status,
        "criteria": _criteria_label(criteria),
        "fundamentals_basis": basis,
        "price_as_of": price_as_of,
        "data_gaps": ";".join(dict.fromkeys(gaps)) or "none",
        "upstream_sources": f"sec_companyfacts_api:{sym};yahoo_chart_api_v8:{sym}",
        "evidence_tier_note": _TIER_NOTE,
        "next_action": _NEXT_ACTION[status],
        "notes": notes,
    }
    for col in _METRIC_COLUMNS:
        value = metrics.get(col)
        row[col] = round(value, 6) if isinstance(value, float) else (
            value if value is not None else "source_gap")
    return row


def _derived_records(sym, as_of, market_scope, metrics, formulas) -> list:
    base = POSTURES["sec_companyfacts"]
    upstream = {
        "sec": f"sec_companyfacts_api:{sym}",
        "sec+yahoo": f"sec_companyfacts_api:{sym};yahoo_chart_api_v8:{sym}",
    }
    family = {"market_cap_usd": "valuation_snapshot", "fcf_yield": "valuation_snapshot"}
    out = []
    for metric in _METRIC_COLUMNS:
        value = metrics.get(metric)
        if value is None or metric not in formulas:
            continue
        formula, kind = formulas[metric]
        out.append(CanonicalRecord(
            family=family.get(metric, "company_financials"),
            research_object=sym, market_scope=market_scope,
            metric=metric, value=round(value, 6),
            unit="USD" if metric == "market_cap_usd" else "ratio",
            period=as_of, period_type="point_in_time", as_of_date=as_of,
            source_date=as_of, posture=base,
            url_or_path="derived://tools/mira_data/screening",
            derived=True, upstream_sources=upstream[kind], formula=formula,
            cross_check="screening_grade; verify vs filings before durable use",
            claim_text=f"{sym} {metric} = {round(value, 6)} (screen, {as_of})",
        ))
    return out


# --- observation selection ---------------------------------------------------

def _annual_by_fy(obs: list) -> dict:
    """Latest filed annual (~12-month span) observation per fiscal year."""
    by_fy = {}
    for r in obs:  # sorted asc by (end, filed): latest filing for the fy wins
        span = r.get("_span")
        if span is not None and scf._is_annual(span) and r.get("fy") is not None and r.get("val") is not None:
            by_fy[r["fy"]] = r
    return by_fy


def _common_annual(obs_a: list, obs_b: list):
    """Latest fiscal year where both metrics have an annual value."""
    a, b = _annual_by_fy(obs_a), _annual_by_fy(obs_b)
    common = sorted(set(a) & set(b))
    if not common:
        return None, None, None
    fy = common[-1]
    return fy, a[fy], b[fy]


def _latest_instant(obs: list) -> Optional[dict]:
    rows = [r for r in obs if r.get("_span") is None and r.get("val") is not None]
    return rows[-1] if rows else None


def _fresh(row: dict, as_of: str) -> bool:
    """True when the observation's period end is recent enough to screen on."""
    try:
        end = _dt.date.fromisoformat(row.get("end", ""))
        return (_dt.date.fromisoformat(as_of) - end).days <= _STALE_DAYS
    except ValueError:
        return False


def _last_close(sym: str) -> tuple[float, str]:
    res = yahoo_chart.fetch_market_price(sym, range_="1mo")
    rows = res.series["rows"]
    for rec in res.records:
        if rec.metric == "last_close" and rec.value is not None:
            return float(rec.value), rec.source_date
    return float(rows[-1]["close"]), rows[-1]["date"]


# --- helpers -----------------------------------------------------------------

def _cik_map(symbols: list) -> dict:
    """One ticker-map fetch resolves every candidate (vs one fetch per ticker)."""
    data = scf.load_ticker_cik_map()
    want = set(symbols)
    return {ticker: cik for ticker, cik in data.items() if ticker in want}


def _criteria_label(criteria: dict) -> str:
    return ";".join(f"{k}={v:g}" for k, v in sorted(criteria.items()))


def _pause() -> None:
    # Wrapped so tests can monkeypatch; keeps the run inside polite rate limits.
    time.sleep(_PAUSE_SECONDS)
