"""Technical-context orchestrator (P2).

Consumes P1's ``market_price`` series for a ticker + benchmark, computes the
daily-derivable subset of ``templates/technical-analysis-check.csv``, maps it to
the state tokens in ``memory/skills/technical-analysis.md``, and produces a
curated set of judgment-affecting ``derived`` records (each ledgered per §8).

Honest boundaries: options / short-interest / intraday fields stay ``source_gap``
(no free source); levels are simple swing/MA references, not fitted; indicators
are reproducible heuristics over delayed L5 data.
"""

from __future__ import annotations

import csv
import datetime as _dt
import os
from dataclasses import dataclass, field
from typing import Optional

from . import indicators as ind
from .adapters import yahoo_chart
from .canonical import POSTURES, CanonicalRecord

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_TEMPLATE = os.path.join(_REPO_ROOT, "templates", "technical-analysis-check.csv")
STALE_DAYS = 30


@dataclass
class TechnicalResult:
    row: dict
    derived: list = field(default_factory=list)
    summary: dict = field(default_factory=dict)


def template_columns() -> list:
    with open(_TEMPLATE, encoding="utf-8") as fh:
        return next(csv.reader(fh))


def emit_check_row(out_dir: str, row: dict) -> str:
    """Append a row to ``<out_dir>/technical-analysis-check.csv`` (template schema)."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "technical-analysis-check.csv")
    cols = template_columns()
    exists = os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=cols)
        if not exists:
            writer.writeheader()
        writer.writerow(row)
    return path


def compute_technical(ticker: str, *, benchmark: str = "SPY", as_of: Optional[str] = None,
                      market_scope: str = "US", lookback_days: int = 252) -> TechnicalResult:
    as_of = as_of or _dt.date.today().isoformat()
    tkr = yahoo_chart.fetch_market_price(ticker, range_="2y")
    rows = tkr.series["rows"]
    closes = [r["close"] for r in rows]
    highs = [r["high"] for r in rows]
    lows = [r["low"] for r in rows]
    vols = [r["volume"] for r in rows]
    adj = [r["adjclose"] if r["adjclose"] is not None else r["close"] for r in rows]

    bench_ret = _benchmark_returns(benchmark)

    close = closes[-1]
    ma20, ma50, ma100, ma200 = (ind.sma(closes, n) for n in (20, 50, 100, 200))
    ret = {k: ind.pct_return(adj, td) for k, td in ind.TD.items()}
    rel = {k: (ret[k] - bench_ret[k]) if (ret[k] is not None and bench_ret.get(k) is not None) else None
           for k in ind.TD}
    vs_high, vs_low = ind.high_low_position(close, highs, lows, 252)
    mdd = ind.max_drawdown(closes[-252:])
    vol20 = ind.ratio_to_avg(vols, 20)
    vol60 = ind.ratio_to_avg(vols, 60)
    vz = ind.zscore(vols, 20)
    rv20 = ind.realized_vol(closes, 20)
    rv60 = ind.realized_vol(closes, 60)
    atr14 = ind.atr(highs, lows, closes, 14)
    natr = atr14 / close if (atr14 and close) else None
    advt = ind.avg_daily_value_traded(closes, vols, 20)

    ma_stack = _ma_stack_state(close, ma20, ma50, ma100, ma200)
    trend = _trend_state(close, ma50, ma200, ma_stack, ret["3m"], vs_high)
    vol_state = _volume_state(vz)
    vty_state = _volatility_state(rv20, rv60)
    levels = _levels(highs, lows, close, ma20, ma50, ma200)
    actionability = _actionability_risk(close, ma20, levels)
    score = _context_score(trend, rel["3m"], vol_state)

    summary = {
        "trend_state": trend, "ma_stack_state": ma_stack, "volume_state": vol_state,
        "volatility_state": vty_state, "positioning_risk": "source_gap",
        "technical_context_score": score, "close_price": close,
        "relative_return_3m": rel["3m"],
        "key_levels": levels, "actionability": actionability, "as_of": as_of,
    }

    computed = {
        "case_id": "", "ticker": ticker.upper(), "market": market_scope, "as_of_date": as_of,
        "price_source_id": "yahoo_chart_api_v8", "benchmark": benchmark.upper(),
        "sector_or_peer_benchmark": "source_gap", "lookback_days": lookback_days,
        "close_price": _r(close), "avg_daily_value_traded": _r(advt),
        "return_1m": _r(ret["1m"]), "return_3m": _r(ret["3m"]), "return_6m": _r(ret["6m"]),
        "return_12m": _r(ret["12m"]), "relative_return_1m": _r(rel["1m"]),
        "relative_return_3m": _r(rel["3m"]), "relative_return_6m": _r(rel["6m"]),
        "relative_return_12m": _r(rel["12m"]), "ma20": _r(ma20), "ma50": _r(ma50),
        "ma100": _r(ma100), "ma200": _r(ma200), "ma_stack_state": ma_stack,
        "price_vs_52w_high_pct": _r(vs_high), "price_vs_52w_low_pct": _r(vs_low),
        "max_drawdown_from_recent_high_pct": _r(mdd), "trend_state": trend,
        "key_support_levels": levels["support"], "key_resistance_levels": levels["resistance"],
        "trigger_level": levels["trigger"], "invalidation_level": levels["invalidation"],
        "extension_from_ma20_pct": _r(actionability["extension_from_ma20_pct"]),
        "current_entry_rr": _r(actionability["current_entry_rr"]),
        "pullback_entry_rr": _r(actionability["pullback_entry_rr"]),
        "chase_risk_state": actionability["chase_risk_state"],
        "preferred_wait_zone": actionability["preferred_wait_zone"],
        "volume_vs_20d_avg": _r(vol20), "volume_vs_60d_avg": _r(vol60), "volume_zscore": _r(vz),
        "realized_vol_20d": _r(rv20), "realized_vol_60d": _r(rv60), "atr_14": _r(atr14),
        "normalized_atr_14": _r(natr), "positioning_risk": "source_gap",
        "technical_context_score": score,
        "evidence_limitations": "Daily delayed L5 market data; indicators are reproducible heuristics; "
                                "options/short-interest/intraday=source_gap; levels are swing/MA references, not fitted.",
        "upstream_sources": f"yahoo_chart_api_v8:{ticker.upper()};yahoo_chart_api_v8:{benchmark.upper()}",
        "stale_after": _stale_after(as_of),
        "must_refresh_if": "close below invalidation_level, next earnings/material event, or 20 trading days",
        "notes": "Generated by tools/mira_data technical (P2).",
    }
    row = _fill_row(computed)
    derived = _derived_records(ticker, benchmark, as_of, market_scope, ret, rel, rv20, mdd,
                               score, actionability)
    return TechnicalResult(row=row, derived=derived, summary=summary)


# --- state-token derivation (transparent heuristics) -----------------------

def _ma_stack_state(close, ma20, ma50, ma100, ma200) -> str:
    if None in (ma20, ma50, ma100, ma200):
        return "source_gap"
    if close > ma20 > ma50 > ma200:
        return "bullish_stack"
    if close < ma20 < ma50 < ma200:
        return "bearish_stack"
    return "mixed"


def _trend_state(close, ma50, ma200, ma_stack, r3, vs_high) -> str:
    if ma200 is None or r3 is None:
        return "technical_source_gap"
    above200 = close > ma200
    if ma_stack == "bullish_stack" and r3 > 0:
        if vs_high is not None and vs_high > -0.03 and ma50 and close > ma50 * 1.15:
            return "uptrend_extended"
        return "uptrend_confirmed"
    if ma_stack == "bearish_stack" and r3 < 0:
        return "downtrend_confirmed"
    if above200:
        return "range_constructive"
    if r3 > 0:
        return "reversal_attempt"
    return "range_distribution"


def _volume_state(vz) -> str:
    if vz is None:
        return "source_gap"
    if vz > 2:
        return "spike"
    if vz > 1:
        return "elevated"
    if vz < -1:
        return "light"
    return "normal"


def _volatility_state(rv20, rv60) -> str:
    if rv20 is None or rv60 is None or rv60 == 0:
        return "source_gap"
    ratio = rv20 / rv60
    if ratio > 1.25:
        return "expanding"
    if ratio < 0.8:
        return "compressing"
    return "normal"


def _levels(highs, lows, close, ma20, ma50, ma200) -> dict:
    swing_hi = max(_last(highs, 20)) if _last(highs, 20) else None
    swing_lo = min(_last(lows, 20)) if _last(lows, 20) else None
    support_candidates = [swing_lo, ma20, ma50, ma200]
    support = ";".join(_fmt_levels(support_candidates))
    resistance = ";".join(_fmt_levels([swing_hi]))
    lower_supports = sorted(
        [v for v in support_candidates if v is not None and v < close],
        reverse=True,
    )
    return {
        "support": support or "source_gap",
        "resistance": resistance or "source_gap",
        "trigger": _r(swing_hi) if swing_hi else "source_gap",
        "invalidation": _r(ma200) if ma200 else "source_gap",
        "nearest_support": lower_supports[0] if lower_supports else None,
        "next_support": lower_supports[1] if len(lower_supports) > 1 else None,
        "swing_high": swing_hi,
    }


def _actionability_risk(close, ma20, levels) -> dict:
    trigger = levels.get("swing_high")
    nearest = levels.get("nearest_support")
    next_support = levels.get("next_support")
    extension = (close / ma20 - 1) if ma20 else None
    current_rr = _rr(close, trigger, nearest)
    pullback_rr = _rr(nearest, trigger, next_support) if nearest and next_support else None
    return {
        "extension_from_ma20_pct": extension,
        "current_entry_rr": current_rr,
        "pullback_entry_rr": pullback_rr,
        "chase_risk_state": _chase_risk_state(extension, current_rr),
        "preferred_wait_zone": _preferred_wait_zone(close, nearest, ma20),
    }


def _rr(entry, target, stop, min_risk_pct=0.02):
    if None in (entry, target, stop):
        return None
    risk = entry - stop
    reward = target - entry
    if risk <= 0 or reward <= 0:
        return 0.0
    if risk / entry < min_risk_pct:
        return None
    return reward / risk


def _chase_risk_state(extension, current_rr) -> str:
    if current_rr is None:
        return "source_gap"
    if (extension is not None and extension >= 0.15) or (current_rr is not None and current_rr < 1):
        return "high"
    if (extension is not None and extension >= 0.08) or (current_rr is not None and current_rr < 2):
        return "medium"
    return "low"


def _preferred_wait_zone(close, nearest_support, ma20) -> str:
    vals = _fmt_levels([v for v in (nearest_support, ma20) if v is not None and v < close])
    if not vals:
        return "source_gap"
    return ";".join(dict.fromkeys(vals))


def _context_score(trend, rel3, vol_state) -> int:
    score = 50
    score += {"uptrend_confirmed": 20, "uptrend_extended": 12, "range_constructive": 6,
              "reversal_attempt": 0, "range_distribution": -10, "range_neutral": 0,
              "downtrend_confirmed": -20, "technical_source_gap": 0}.get(trend, 0)
    if rel3 is not None:
        score += 12 if rel3 > 0 else -12
    if vol_state in ("elevated", "spike"):
        score += 4
    return max(0, min(100, score))


# --- derived records (ledgered) --------------------------------------------

def _derived_records(ticker, benchmark, as_of, market_scope, ret, rel, rv20, mdd, score,
                     actionability) -> list:
    base = POSTURES["yahoo_chart"]
    up = f"yahoo_chart_api_v8:{ticker.upper()}"
    up_rel = f"{up};yahoo_chart_api_v8:{benchmark.upper()}"
    specs = [
        ("return_3m", ret["3m"], "ratio", f"adjclose[-1]/adjclose[-64] - 1", up),
        ("relative_return_3m", rel["3m"], "ratio",
         f"return_3m({ticker.upper()}) - return_3m({benchmark.upper()})", up_rel),
        ("realized_vol_20d", rv20, "annualized_stdev", "pstdev(logret[-20:]) * sqrt(252)", up),
        ("max_drawdown_from_recent_high_pct", mdd, "ratio", "min(close/running_peak - 1) over 252d", up),
        ("technical_context_score", score, "score_0_100", "50 + trend + rel3m_sign + volume_adj", up_rel),
        ("extension_from_ma20_pct", actionability["extension_from_ma20_pct"], "ratio",
         "close/ma20 - 1", up),
        ("current_entry_rr", actionability["current_entry_rr"], "reward_to_risk",
         "(20d_high - close) / (close - nearest_support_below_close); "
         "source_gap if risk distance < 2% of entry", up),
        ("pullback_entry_rr", actionability["pullback_entry_rr"], "reward_to_risk",
         "(20d_high - nearest_support_below_close) / "
         "(nearest_support_below_close - next_support_below_close); "
         "source_gap if risk distance < 2% of entry", up),
    ]
    out = []
    for metric, value, unit, formula, upstream in specs:
        if value is None:
            continue
        out.append(CanonicalRecord(
            family="market_price", research_object=ticker.upper(), market_scope=market_scope,
            metric=metric, value=round(value, 6) if isinstance(value, float) else value,
            unit=unit, period=as_of, period_type="point_in_time", as_of_date=as_of,
            source_date=as_of, posture=base, url_or_path="derived://tools/mira_data/technical",
            derived=True, upstream_sources=upstream, formula=formula,
            claim_text=f"{ticker.upper()} {metric} = {round(value, 6) if isinstance(value, float) else value} (derived, {as_of})",
        ))
    return out


# --- helpers ---------------------------------------------------------------

def _benchmark_returns(benchmark: str) -> dict:
    try:
        b = yahoo_chart.fetch_market_price(benchmark, range_="2y")
    except Exception:
        return {k: None for k in ind.TD}
    adj = [r["adjclose"] if r["adjclose"] is not None else r["close"] for r in b.series["rows"]]
    return {k: ind.pct_return(adj, td) for k, td in ind.TD.items()}


def _fill_row(computed: dict) -> dict:
    row = {col: computed.get(col, "source_gap") for col in template_columns()}
    return row


def _stale_after(as_of: str) -> str:
    d = _dt.date.fromisoformat(as_of) + _dt.timedelta(days=STALE_DAYS)
    return d.isoformat()


def _fmt_levels(values) -> list:
    return [f"{v:.2f}" for v in values if v is not None]


def _last(seq, n):
    vals = [v for v in seq if v is not None]
    return vals[-n:] if len(vals) >= n else vals


def _r(v, nd: int = 4):
    if v is None:
        return "source_gap"
    if isinstance(v, float):
        return round(v, nd)
    return v
