"""Interactive Brokers Gateway adapter.

This adapter is optional and private-first:

- it requires the user to run a local TWS/IB Gateway session;
- it imports ``ib_insync`` only at runtime;
- outputs should normally be emitted under ``private/`` because they may contain
  account, entitlement or licensed market-data details.

It does not place orders. It only reads market snapshots and account positions.
"""

from __future__ import annotations

import datetime as _dt
import csv
import math
import os
from typing import Optional

from .. import config, net
from ..canonical import POSTURES, CanonicalRecord, FetchResult

GATEWAY_ENDPOINT = "ibkr-gateway://{host}:{port}"


def fetch_market_price(
    symbol: str,
    *,
    as_of: Optional[str] = None,
    market_scope: str = "US",
) -> FetchResult:
    """Fetch a point-in-time market snapshot for ``symbol`` from local IBKR."""
    as_of = as_of or _dt.date.today().isoformat()
    ib, endpoint = _connect()
    try:
        ib.reqMarketDataType(_int_cfg("MIRA_IBKR_MARKET_DATA_TYPE", 3))
        contract = _stock_contract(symbol)
        qualified = ib.qualifyContracts(contract)
        if qualified:
            contract = qualified[0]
        ticker = ib.reqMktData(contract, "", False, False)
        _wait_for_market_data(ib, ticker)

        quote_time = _quote_date(ticker) or as_of
        currency = getattr(contract, "currency", None) or config.get("MIRA_IBKR_CURRENCY", "USD")
        records = []
        for metric, value, unit in (
            ("last_price", _price(getattr(ticker, "last", None)), currency),
            ("market_price", _price(ticker.marketPrice()), currency),
            ("bid", _price(getattr(ticker, "bid", None)), currency),
            ("ask", _price(getattr(ticker, "ask", None)), currency),
            ("previous_close", _price(getattr(ticker, "close", None)), currency),
            ("volume", _nonnegative(getattr(ticker, "volume", None)), "shares"),
        ):
            if value is None:
                continue
            records.append(
                CanonicalRecord(
                    family="market_price",
                    research_object=symbol.upper(),
                    market_scope=market_scope,
                    metric=metric,
                    value=value,
                    unit=unit,
                    currency=currency if unit == currency else None,
                    period=quote_time,
                    period_type="point_in_time",
                    as_of_date=as_of,
                    source_date=quote_time,
                    posture=POSTURES["ibkr_gateway"],
                    url_or_path=endpoint,
                    confidence="medium",
                    freshness_status="current",
                    provenance={
                        "exchange": getattr(contract, "exchange", None),
                        "primary_exchange": getattr(contract, "primaryExchange", None),
                        "market_data_type": config.get("MIRA_IBKR_MARKET_DATA_TYPE", "3"),
                    },
                )
            )
        if not records:
            raise net.FetchError(f"ibkr_source_gap: no usable market fields for {symbol}")
        return FetchResult(records)
    finally:
        ib.disconnect()


def fetch_historical_bars(
    symbol: str,
    *,
    as_of: Optional[str] = None,
    market_scope: str = "US",
    duration: str | None = None,
    bar_size: str | None = None,
    what_to_show: str | None = None,
    use_rth: bool | None = None,
) -> FetchResult:
    """Fetch historical bars from local IBKR as a private market-price series."""
    as_of = as_of or _dt.date.today().isoformat()
    duration = duration or config.get("MIRA_IBKR_HIST_DURATION", "1 Y") or "1 Y"
    bar_size = bar_size or config.get("MIRA_IBKR_HIST_BAR_SIZE", "1 day") or "1 day"
    what_to_show = what_to_show or config.get("MIRA_IBKR_HIST_WHAT", "TRADES") or "TRADES"
    use_rth = _bool_cfg("MIRA_IBKR_HIST_USE_RTH", True) if use_rth is None else use_rth

    ib, endpoint = _connect()
    try:
        contract = _stock_contract(symbol)
        qualified = ib.qualifyContracts(contract)
        if qualified:
            contract = qualified[0]
        bars = ib.reqHistoricalData(
            contract,
            endDateTime="",
            durationStr=duration,
            barSizeSetting=bar_size,
            whatToShow=what_to_show,
            useRTH=use_rth,
            formatDate=1,
        )
        rows = [_bar_row(b) for b in bars]
        if not rows:
            raise net.FetchError(f"ibkr_source_gap: no historical bars for {symbol}")

        currency = getattr(contract, "currency", None) or config.get("MIRA_IBKR_CURRENCY", "USD")
        last = rows[-1]
        posture = POSTURES["ibkr_gateway"]
        records = [
            CanonicalRecord(
                family="market_price",
                research_object=symbol.upper(),
                market_scope=market_scope,
                metric="last_close",
                value=last["close"],
                unit=currency,
                currency=currency,
                period=last["date"],
                period_type="point_in_time",
                as_of_date=as_of,
                source_date=last["date"],
                posture=posture,
                url_or_path=endpoint,
                freshness_status="current",
                provenance={
                    "duration": duration,
                    "bar_size": bar_size,
                    "what_to_show": what_to_show,
                    "use_rth": str(use_rth).lower(),
                },
            ),
            CanonicalRecord(
                family="market_price",
                research_object=symbol.upper(),
                market_scope=market_scope,
                metric="last_volume",
                value=last["volume"],
                unit="shares",
                period=last["date"],
                period_type="point_in_time",
                as_of_date=as_of,
                source_date=last["date"],
                posture=posture,
                url_or_path=endpoint,
                freshness_status="current",
                provenance={
                    "duration": duration,
                    "bar_size": bar_size,
                    "what_to_show": what_to_show,
                    "use_rth": str(use_rth).lower(),
                },
            ),
        ]
        series = {
            "name": f"ibkr_historical_bars-{symbol.upper()}",
            "columns": ["date", "open", "high", "low", "close", "volume", "average", "bar_count"],
            "rows": rows,
        }
        return FetchResult(records, series=series)
    finally:
        ib.disconnect()


def fetch_positions(
    account: str | None = None,
    *,
    as_of: Optional[str] = None,
    market_scope: str = "multi",
) -> FetchResult:
    """Fetch account positions.

    ``account=None`` uses ``MIRA_IBKR_ACCOUNT`` when configured. ``ALL`` keeps
    the account filter off.
    """
    as_of = as_of or _dt.date.today().isoformat()
    account = account or config.get("MIRA_IBKR_ACCOUNT", "ALL") or "ALL"
    ib, endpoint = _connect()
    try:
        account_filter = None if account.upper() == "ALL" else account
        positions = [
            p for p in ib.positions()
            if account_filter is None or getattr(p, "account", None) == account_filter
        ]
        records = []
        for pos in positions:
            contract = pos.contract
            symbol = getattr(contract, "symbol", "") or getattr(contract, "localSymbol", "")
            if not symbol:
                continue
            currency = getattr(contract, "currency", None) or "not_applicable"
            for metric, value, unit in (
                ("position_quantity", _num(getattr(pos, "position", None)), "units"),
                ("average_cost", _num(getattr(pos, "avgCost", None)), currency),
            ):
                if value is None:
                    continue
                records.append(
                    CanonicalRecord(
                        family="portfolio_position",
                        research_object=symbol.upper(),
                        market_scope=market_scope,
                        metric=metric,
                        value=value,
                        unit=unit,
                        currency=currency if unit == currency else None,
                        period=as_of,
                        period_type="point_in_time",
                        as_of_date=as_of,
                        source_date=as_of,
                        posture=POSTURES["ibkr_gateway_positions"],
                        url_or_path=endpoint,
                        confidence="medium",
                        freshness_status="current",
                        provenance={
                            "secType": getattr(contract, "secType", None),
                            "exchange": getattr(contract, "exchange", None),
                            "account_scope": "filtered" if account_filter else "all",
                        },
                    )
                )
        if not records:
            raise net.FetchError("ibkr_source_gap: no positions returned for requested account scope")
        return FetchResult(records)
    finally:
        ib.disconnect()


def fetch_account_summary(
    account: str | None = None,
    *,
    as_of: Optional[str] = None,
    market_scope: str = "multi",
) -> FetchResult:
    """Fetch selected account summary metrics from local IBKR."""
    as_of = as_of or _dt.date.today().isoformat()
    account = account or config.get("MIRA_IBKR_ACCOUNT", "All") or "All"
    ib, endpoint = _connect()
    try:
        rows = ib.accountSummary(account if account.upper() != "ALL" else "All")
        wanted = {
            "NetLiquidation",
            "TotalCashValue",
            "BuyingPower",
            "AvailableFunds",
            "ExcessLiquidity",
            "GrossPositionValue",
            "InitMarginReq",
            "MaintMarginReq",
            "Cushion",
        }
        records = []
        for row in rows:
            tag = getattr(row, "tag", "")
            if tag not in wanted:
                continue
            value = _num(getattr(row, "value", None))
            if value is None:
                continue
            currency = getattr(row, "currency", "") or "not_applicable"
            records.append(
                CanonicalRecord(
                    family="portfolio_position",
                    research_object="IBKR_ACCOUNT_SUMMARY",
                    market_scope=market_scope,
                    metric=_snake(tag),
                    value=value,
                    unit=currency,
                    currency=currency if currency != "not_applicable" else None,
                    period=as_of,
                    period_type="point_in_time",
                    as_of_date=as_of,
                    source_date=as_of,
                    posture=POSTURES["ibkr_gateway_positions"],
                    url_or_path=endpoint,
                    confidence="medium",
                    freshness_status="current",
                    provenance={"account_scope": "filtered" if account.upper() != "ALL" else "all"},
                )
            )
        if not records:
            raise net.FetchError("ibkr_source_gap: no account summary rows returned")
        return FetchResult(records)
    finally:
        ib.disconnect()


def managed_accounts(*, mask: bool = True) -> list[str]:
    """Return managed accounts. Mask by default for console-safe output."""
    ib, _endpoint = _connect()
    try:
        accounts = [a for a in ib.managedAccounts() if a]
    finally:
        ib.disconnect()
    if mask:
        return [_mask_account(a) for a in accounts]
    return accounts


def emit_position_snapshot(
    out_dir: str,
    *,
    account: str | None = None,
    as_of: Optional[str] = None,
) -> str:
    """Write a private IBKR position snapshot CSV and return its path."""
    as_of = as_of or _dt.date.today().isoformat()
    account = account or config.get("MIRA_IBKR_ACCOUNT", "ALL") or "ALL"
    ib, endpoint = _connect()
    try:
        account_filter = None if account.upper() == "ALL" else account
        positions = [
            p for p in ib.positions()
            if account_filter is None or getattr(p, "account", None) == account_filter
        ]
    finally:
        ib.disconnect()

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "ibkr-position-snapshot.csv")
    columns = [
        "snapshot_date", "portfolio_id", "account_id", "symbol", "local_symbol",
        "sec_type", "exchange", "currency", "position_quantity", "average_cost",
        "source_id", "source_date", "url_or_path", "notes",
    ]
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns)
        writer.writeheader()
        for pos in positions:
            contract = pos.contract
            writer.writerow({
                "snapshot_date": as_of,
                "portfolio_id": config.get("MIRA_IBKR_PORTFOLIO_ID", "ibkr_default"),
                "account_id": getattr(pos, "account", ""),
                "symbol": getattr(contract, "symbol", ""),
                "local_symbol": getattr(contract, "localSymbol", ""),
                "sec_type": getattr(contract, "secType", ""),
                "exchange": getattr(contract, "exchange", ""),
                "currency": getattr(contract, "currency", ""),
                "position_quantity": getattr(pos, "position", ""),
                "average_cost": getattr(pos, "avgCost", ""),
                "source_id": "ibkr_gateway_local",
                "source_date": as_of,
                "url_or_path": endpoint,
                "notes": "Private broker position snapshot; do not commit.",
            })
    return path


def _connect():
    try:
        from ib_insync import IB  # type: ignore
    except ImportError as exc:
        raise net.FetchError(
            "ibkr_dependency_gap: install optional dependency 'ib_insync' to use IBKR Gateway"
        ) from exc

    host = config.get("MIRA_IBKR_HOST", "127.0.0.1") or "127.0.0.1"
    port = _int_cfg("MIRA_IBKR_PORT", 7497)
    client_id = _int_cfg("MIRA_IBKR_CLIENT_ID", 19)
    if _bool_cfg("MIRA_IBKR_CLIENT_ID_AUTO", True):
        client_id += os.getpid() % 1000
    retries = max(_int_cfg("MIRA_IBKR_CLIENT_ID_RETRIES", 5), 0)
    timeout = _float_cfg("MIRA_IBKR_TIMEOUT", 10.0)
    readonly = _bool_cfg("MIRA_IBKR_READONLY", True)
    endpoint = GATEWAY_ENDPOINT.format(host=host, port=port)
    last_exc: Exception | None = None
    for offset in range(retries + 1):
        ib = IB()
        try:
            ib.connect(host, port, clientId=client_id + offset, timeout=timeout, readonly=readonly)
            return ib, endpoint
        except Exception as exc:
            last_exc = exc
            if ib.isConnected():
                ib.disconnect()
            continue
    raise net.FetchError(f"ibkr_connection_gap: could not connect to {endpoint}: {last_exc}") from last_exc


def _stock_contract(symbol: str):
    try:
        from ib_insync import Stock  # type: ignore
    except ImportError as exc:
        raise net.FetchError(
            "ibkr_dependency_gap: install optional dependency 'ib_insync' to use IBKR Gateway"
        ) from exc

    exchange = config.get("MIRA_IBKR_EXCHANGE", "SMART") or "SMART"
    currency = config.get("MIRA_IBKR_CURRENCY", "USD") or "USD"
    primary = config.get("MIRA_IBKR_PRIMARY_EXCHANGE")
    return Stock(symbol.upper(), exchange, currency, primaryExchange=primary or "")


def _bar_row(bar) -> dict:
    date = getattr(bar, "date", "")
    if hasattr(date, "date"):
        date = date.date().isoformat()
    else:
        date = str(date)
    return {
        "date": date,
        "open": _num(getattr(bar, "open", None)),
        "high": _num(getattr(bar, "high", None)),
        "low": _num(getattr(bar, "low", None)),
        "close": _num(getattr(bar, "close", None)),
        "volume": _nonnegative(getattr(bar, "volume", None)),
        "average": _num(getattr(bar, "average", None)),
        "bar_count": _nonnegative(getattr(bar, "barCount", None)),
    }


def _wait_for_market_data(ib, ticker) -> None:
    timeout = _float_cfg("MIRA_IBKR_TIMEOUT", 10.0)
    deadline = _dt.datetime.now().timestamp() + timeout
    while _dt.datetime.now().timestamp() < deadline:
        if any(_num(v) is not None for v in (
            getattr(ticker, "last", None),
            ticker.marketPrice(),
            getattr(ticker, "bid", None),
            getattr(ticker, "ask", None),
            getattr(ticker, "close", None),
        )):
            return
        ib.sleep(0.25)


def _quote_date(ticker) -> str | None:
    ts = getattr(ticker, "time", None)
    if ts is None:
        return None
    if hasattr(ts, "date"):
        return ts.date().isoformat()
    return None


def _num(value):
    if value is None:
        return None
    try:
        f = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(f) or math.isinf(f):
        return None
    return f


def _price(value):
    f = _num(value)
    if f is None or f < 0:
        return None
    return f


def _nonnegative(value):
    f = _num(value)
    if f is None or f < 0:
        return None
    return f


def _int_cfg(key: str, default: int) -> int:
    try:
        return int(config.get(key, str(default)) or default)
    except ValueError:
        return default


def _float_cfg(key: str, default: float) -> float:
    try:
        return float(config.get(key, str(default)) or default)
    except ValueError:
        return default


def _bool_cfg(key: str, default: bool) -> bool:
    raw = config.get(key)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def _mask_account(account: str) -> str:
    if len(account) <= 4:
        return "*" * len(account)
    return account[:2] + "*" * (len(account) - 4) + account[-2:]


def _snake(tag: str) -> str:
    out = []
    for i, ch in enumerate(tag):
        if ch.isupper() and i and not tag[i - 1].isupper():
            out.append("_")
        out.append(ch.lower())
    return "".join(out)
