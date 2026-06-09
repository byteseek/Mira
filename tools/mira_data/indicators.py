"""Pure-stdlib technical indicators over OHLCV lists.

No numpy/pandas: the data is a few hundred to a few thousand daily bars per
ticker, computed on demand, so ``math`` + ``statistics`` are the right tool
(architecture/data-acquisition-upgrade.md — single-name scope, no storage stack).

Every function returns ``None`` on insufficient data so callers degrade to a
``source_gap`` token instead of fabricating a number. Inputs are plain lists
ordered oldest -> newest.

Convention: price *levels* (MA, ATR, 52w range) use raw ``close``; *returns* use
``adjclose`` (total return). Callers pass the right series.
"""

from __future__ import annotations

import math
import statistics
from typing import Optional, Sequence

# Trading-day windows for calendar-month lookbacks.
TD = {"1m": 21, "3m": 63, "6m": 126, "12m": 252}


def sma(values: Sequence[float], n: int) -> Optional[float]:
    vals = _clean(values)
    if len(vals) < n:
        return None
    return statistics.fmean(vals[-n:])


def pct_return(series: Sequence[float], lookback: int) -> Optional[float]:
    vals = _clean(series)
    if len(vals) <= lookback or vals[-1 - lookback] == 0:
        return None
    return vals[-1] / vals[-1 - lookback] - 1.0


def zscore(values: Sequence[float], n: int) -> Optional[float]:
    vals = _clean(values)
    if len(vals) < n:
        return None
    window = vals[-n:]
    sd = statistics.pstdev(window)
    if sd == 0:
        return None
    return (vals[-1] - statistics.fmean(window)) / sd


def realized_vol(closes: Sequence[float], n: int, periods: int = 252) -> Optional[float]:
    vals = _clean(closes)
    if len(vals) < n + 1:
        return None
    logrets = [math.log(vals[i] / vals[i - 1]) for i in range(1, len(vals)) if vals[i - 1] > 0]
    if len(logrets) < n:
        return None
    return statistics.pstdev(logrets[-n:]) * math.sqrt(periods)


def atr(highs: Sequence[float], lows: Sequence[float], closes: Sequence[float],
        n: int = 14) -> Optional[float]:
    if min(len(highs), len(lows), len(closes)) < n + 1:
        return None
    trs = []
    for i in range(1, len(closes)):
        h, low, pc = highs[i], lows[i], closes[i - 1]
        if None in (h, low, pc):
            continue
        trs.append(max(h - low, abs(h - pc), abs(low - pc)))
    if len(trs) < n:
        return None
    return statistics.fmean(trs[-n:])


def max_drawdown(closes: Sequence[float]) -> Optional[float]:
    vals = _clean(closes)
    if not vals:
        return None
    peak, mdd = vals[0], 0.0
    for c in vals:
        peak = max(peak, c)
        if peak > 0:
            mdd = min(mdd, c / peak - 1.0)
    return mdd


def high_low_position(close: float, highs: Sequence[float], lows: Sequence[float],
                      n: int = 252) -> tuple[Optional[float], Optional[float]]:
    hs, ls = _clean(highs)[-n:], _clean(lows)[-n:]
    if not hs or not ls:
        return None, None
    hi, lo = max(hs), min(ls)
    vs_high = close / hi - 1.0 if hi else None      # <= 0, distance below 52w high
    vs_low = close / lo - 1.0 if lo else None        # >= 0, distance above 52w low
    return vs_high, vs_low


def ratio_to_avg(values: Sequence[float], n: int) -> Optional[float]:
    vals = _clean(values)
    if len(vals) < n:
        return None
    avg = statistics.fmean(vals[-n:])
    if avg == 0:
        return None
    return vals[-1] / avg - 1.0


def avg_daily_value_traded(closes: Sequence[float], volumes: Sequence[float],
                           n: int = 20) -> Optional[float]:
    pairs = [(c, v) for c, v in zip(closes, volumes) if c is not None and v is not None]
    if len(pairs) < n:
        return None
    return statistics.fmean([c * v for c, v in pairs[-n:]])


def _clean(values: Sequence[float]) -> list:
    return [v for v in values if v is not None]


def _selftest() -> None:
    closes = [float(i) for i in range(1, 261)]  # strictly rising 1..260
    assert sma(closes, 20) == statistics.fmean(closes[-20:])
    assert abs(pct_return(closes, 252) - (260 / 8 - 1)) < 1e-9
    assert max_drawdown(closes) == 0.0           # never declines
    assert max_drawdown([10, 5, 8]) == -0.5      # 10 -> 5
    vh, vl = high_low_position(closes[-1], closes, closes, 252)
    assert abs(vh) < 1e-9 and vl > 0             # at the high
    assert zscore([1, 1, 1, 1], 4) is None       # zero variance
    assert sma([1, 2], 5) is None                # insufficient
    assert realized_vol(closes, 20) is not None
    assert atr(closes, closes, closes, 14) is not None
    print("indicators self-test: OK")


if __name__ == "__main__":
    _selftest()
