"""CLI: fetch a canonical family for a symbol and emit the artifact bundle.

Usage:
    PYTHONPATH=tools python3 -m mira_data fetch company_financials AAPL --out private/data-smoke

Families wired in P1:
    company_financials   SEC companyfacts (US, fact/L2)
"""

from __future__ import annotations

import argparse
import sys

from . import config, fundamentals, net, screening, technical
from .adapters import bls, ibkr_gateway, sec_companyfacts, yahoo_chart
from .emit import emit_bundle

FETCHERS = {
    "company_financials": ("SEC companyfacts", sec_companyfacts.fetch_company_financials,
                           sec_companyfacts.COMPANYFACTS_URL),
    "market_price": ("Yahoo v8 chart", yahoo_chart.fetch_market_price,
                     yahoo_chart.CHART_URL),
    "macro_series": ("BLS public data", bls.fetch_macro_series, bls.SERIES_URL),
    "ibkr_market_price": ("IBKR local Gateway", ibkr_gateway.fetch_market_price,
                          ibkr_gateway.GATEWAY_ENDPOINT),
    "ibkr_positions": ("IBKR local Gateway positions", ibkr_gateway.fetch_positions,
                       ibkr_gateway.GATEWAY_ENDPOINT),
    "ibkr_account_summary": ("IBKR local Gateway account summary",
                             ibkr_gateway.fetch_account_summary,
                             ibkr_gateway.GATEWAY_ENDPOINT),
    "ibkr_historical_bars": ("IBKR local Gateway historical bars",
                             ibkr_gateway.fetch_historical_bars,
                             ibkr_gateway.GATEWAY_ENDPOINT),
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="mira_data", description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fetch", help="fetch a canonical family and emit artifacts")
    f.add_argument("family", choices=sorted(FETCHERS))
    f.add_argument("symbol", nargs="?")
    f.add_argument("--out", default="private/data-smoke", help="output directory")
    f.add_argument("--as-of", default=None, help="as-of date YYYY-MM-DD (default today)")
    f.add_argument("--market-scope", default="US")
    f.add_argument("--no-emit", action="store_true", help="print records only, don't write files")

    t = sub.add_parser("technical", help="compute technical context for a symbol")
    t.add_argument("symbol")
    t.add_argument("--benchmark", default="SPY")
    t.add_argument("--out", default="private/data-smoke")
    t.add_argument("--as-of", default=None)
    t.add_argument("--market-scope", default="US")
    t.add_argument("--no-emit", action="store_true", help="print summary only, don't write files")

    fd = sub.add_parser("fundamentals", help="compute fundamental deltas (YoY/CAGR) for a symbol")
    fd.add_argument("symbol")
    fd.add_argument("--out", default="private/data-smoke")
    fd.add_argument("--as-of", default=None)
    fd.add_argument("--market-scope", default="US")
    fd.add_argument("--no-emit", action="store_true", help="print deltas only, don't write files")

    sc = sub.add_parser(
        "screen",
        help="screen an explicit candidate list on fundamental criteria (bounded triage)")
    sc.add_argument("tickers",
                    help="comma-separated tickers, or @file with one ticker per line "
                         f"(max {screening.MAX_TICKERS})")
    sc.add_argument("--min-market-cap", type=float, default=None, help="USD floor")
    sc.add_argument("--min-fcf-yield", type=float, default=None,
                    help="(FY OCF - FY capex) / market cap floor, e.g. 0.04")
    sc.add_argument("--max-debt-to-equity", type=float, default=None,
                    help="long-term debt / equity ceiling, e.g. 1.0")
    sc.add_argument("--min-net-margin", type=float, default=None, help="FY net margin floor")
    sc.add_argument("--min-revenue-yoy", type=float, default=None,
                    help="latest same-period revenue YoY floor, e.g. 0.0")
    sc.add_argument("--out", default="private/data-smoke")
    sc.add_argument("--as-of", default=None)
    sc.add_argument("--market-scope", default="US")
    sc.add_argument("--no-emit", action="store_true", help="print results only, don't write files")

    sub.add_parser("config", help="show resolved data-substrate configuration")

    v = sub.add_parser("validate", help="validate an emitted artifact bundle")
    v.add_argument("dir")

    ib = sub.add_parser("ibkr", help="read-only IBKR Gateway utilities")
    ib_sub = ib.add_subparsers(dest="ibkr_cmd", required=True)

    acct = ib_sub.add_parser("accounts", help="list managed accounts, masked by default")
    acct.add_argument("--show-full", action="store_true",
                      help="print full account ids (console-sensitive)")

    snap = ib_sub.add_parser("position-snapshot", help="write a private position snapshot CSV")
    snap.add_argument("--account", default=None,
                      help="account id; default MIRA_IBKR_ACCOUNT, or ALL if unset")
    snap.add_argument("--out", default="private/portfolio",
                      help="private output directory")
    snap.add_argument("--as-of", default=None)

    args = parser.parse_args(argv)
    if args.cmd == "fetch":
        return _do_fetch(args)
    if args.cmd == "technical":
        return _do_technical(args)
    if args.cmd == "fundamentals":
        return _do_fundamentals(args)
    if args.cmd == "screen":
        return _do_screen(args)
    if args.cmd == "config":
        return _do_config(args)
    if args.cmd == "validate":
        return _do_validate(args)
    if args.cmd == "ibkr":
        return _do_ibkr(args)
    parser.error("unknown command")
    return 2


def _do_fundamentals(args) -> int:
    try:
        records = fundamentals.compute_deltas(
            args.symbol, as_of=args.as_of, market_scope=args.market_scope)
    except net.FetchError as exc:
        print(f"source_gap: could not compute deltas for {args.symbol}: {exc}", file=sys.stderr)
        return 1

    print(f"# {args.symbol.upper()} fundamental deltas (derived from SEC companyfacts)")
    print(f"{'metric':<24}{'value':>12}  tier")
    for r in records:
        print(f"{r.metric:<24}{_fmt(r.value):>12}  {r.posture.claim_type}/{r.posture.authority_level}")

    if args.no_emit:
        return 0

    result = emit_bundle(
        records, out_dir=args.out, research_object=args.symbol.upper(),
        market_scope=args.market_scope, endpoint="derived://tools/mira_data/fundamentals",
        params=f"symbol={args.symbol.upper()}",
    )
    print("\n# emitted")
    for key in ("evidence_log", "calculation_ledger", "manifest", "ingestion_log"):
        if result.get(key):
            print(f"  {key:<20} {result[key]}")
    print(f"  derived={result['n_records']} ledgered={result['n_ledgered']} "
          f"(Mira-computed -> ledger required, §8)")
    return 0


def _do_screen(args) -> int:
    criteria = {name: getattr(args, name) for name in screening.CRITERIA
                if getattr(args, name) is not None}
    try:
        tickers = _parse_tickers(args.tickers)
        res = screening.screen_candidates(
            tickers, criteria, as_of=args.as_of, market_scope=args.market_scope)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    except net.FetchError as exc:
        print(f"source_gap: screen could not run: {exc}", file=sys.stderr)
        return 1

    s = res.summary
    print(f"# screen {s['as_of']}: {s['n_candidates']} candidates -> "
          f"{s['pass']} pass / {s['fail']} fail / {s['data_gap']} data_gap")
    print(f"  criteria: {s['criteria']}")
    print(f"{'ticker':<12}{'status':<10}{'mkt_cap':>18}{'fcf_yld':>11}{'d/e':>11}"
          f"{'margin':>11}{'rev_yoy':>11}  gaps")
    for row in res.rows:
        print(f"{row['ticker']:<12}{row['screen_status']:<10}"
              f"{_fmt_metric(row['market_cap_usd']):>18}{_fmt_metric(row['fcf_yield']):>11}"
              f"{_fmt_metric(row['debt_to_equity']):>11}{_fmt_metric(row['net_margin']):>11}"
              f"{_fmt_metric(row['revenue_yoy']):>11}  {row['data_gaps']}")

    if args.no_emit:
        return 0

    watchlist = screening.emit_watchlist_rows(args.out, res.rows)
    print(f"\n# emitted\n  {'watchlist':<20} {watchlist}")
    if res.derived:
        result = emit_bundle(
            res.derived, out_dir=args.out,
            research_object=f"SCREEN_{s['as_of']}", market_scope=args.market_scope,
            endpoint="derived://tools/mira_data/screening", params=s["criteria"],
        )
        for key in ("evidence_log", "calculation_ledger", "manifest", "ingestion_log"):
            if result.get(key):
                print(f"  {key:<20} {result[key]}")
        print(f"  derived={result['n_records']} ledgered={result['n_ledgered']} "
              f"(Mira-computed -> ledger required, §8)")
    else:
        print("  no passing ticker -> no derived bundle (watchlist only)")
    return 0


def _parse_tickers(arg: str) -> list[str]:
    if arg.startswith("@"):
        with open(arg[1:], encoding="utf-8") as fh:
            return [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    return arg.split(",")


def _fmt_metric(v) -> str:
    if isinstance(v, float):
        return f"{v:,.0f}" if v > 1000 else f"{v:.4f}"
    return str(v)


def _do_technical(args) -> int:
    try:
        res = technical.compute_technical(
            args.symbol, benchmark=args.benchmark, as_of=args.as_of,
            market_scope=args.market_scope,
        )
    except net.FetchError as exc:
        print(f"source_gap: could not compute technical context for {args.symbol}: {exc}",
              file=sys.stderr)
        return 1

    s = res.summary
    print(f"# {args.symbol.upper()} technical context vs {args.benchmark.upper()} (as of {s['as_of']})")
    for key in ("trend_state", "ma_stack_state", "volume_state", "volatility_state",
                "positioning_risk", "technical_context_score"):
        print(f"  {key:<24}: {s[key]}")
    print(f"  {'relative_return_3m':<24}: {s['relative_return_3m']}")
    lv = s["key_levels"]
    print(f"  {'close / inval / trigger':<24}: {s['close_price']} / {lv['invalidation']} / {lv['trigger']}")

    if args.no_emit:
        return 0

    check_path = technical.emit_check_row(args.out, res.row)
    print(f"\n# emitted\n  {'technical_check':<20} {check_path}")
    if res.derived:
        result = emit_bundle(
            res.derived, out_dir=args.out, research_object=args.symbol.upper(),
            market_scope=args.market_scope, endpoint="derived://tools/mira_data/technical",
            params=f"symbol={args.symbol.upper()};benchmark={args.benchmark.upper()}",
        )
        for key in ("evidence_log", "calculation_ledger", "manifest", "ingestion_log"):
            if result.get(key):
                print(f"  {key:<20} {result[key]}")
        print(f"  derived={result['n_records']} ledgered={result['n_ledgered']} "
              f"(Mira-computed -> ledger required, §8)")
    return 0


def _do_validate(args) -> int:
    from .validate import validate_bundle

    issues = validate_bundle(args.dir)
    for issue in issues:
        print(f"  {issue.level}: {issue.msg}")
    errors = sum(1 for i in issues if i.level == "ERROR")
    warns = len(issues) - errors
    if not issues:
        print(f"OK: {args.dir} passed bundle validation")
    print(f"\n{errors} error(s), {warns} warning(s)")
    return 1 if errors else 0


def _do_ibkr(args) -> int:
    if args.ibkr_cmd == "accounts":
        try:
            accounts = ibkr_gateway.managed_accounts(mask=not args.show_full)
        except net.FetchError as exc:
            print(f"source_gap: could not list IBKR accounts: {exc}", file=sys.stderr)
            return 1
        print(f"# ibkr accounts ({len(accounts)})")
        for account in accounts:
            print(account)
        return 0

    if args.ibkr_cmd == "position-snapshot":
        try:
            path = ibkr_gateway.emit_position_snapshot(
                args.out, account=args.account, as_of=args.as_of)
        except net.FetchError as exc:
            print(f"source_gap: could not write IBKR position snapshot: {exc}", file=sys.stderr)
            return 1
        print("# emitted")
        print(f"  position_snapshot  {path}")
        print("  storage_scope      private")
        return 0

    print(f"error: unknown ibkr command {args.ibkr_cmd}", file=sys.stderr)
    return 2


def _do_config(_args) -> int:
    ua, configured = config.contact_ua()
    print("# mira_data config")
    print(f"  contact_configured : {configured}")
    print(f"  user_agent         : {ua}")
    for key in (
        "MIRA_CONTACT_EMAIL", "MIRA_CONTACT_NAME", "FRED_API_KEY", "BEA_API_KEY",
        "MIRA_IBKR_HOST", "MIRA_IBKR_PORT", "MIRA_IBKR_CLIENT_ID",
        "MIRA_IBKR_ACCOUNT", "MIRA_IBKR_READONLY", "MIRA_IBKR_MARKET_DATA_TYPE",
    ):
        print(f"  {key:<18} : {'set' if config.get(key) else '-'}")
    print(f"  searched files     : {', '.join(config._candidate_paths())}")
    if not configured:
        print("\n" + config.config_hint())
    return 0


def _do_fetch(args) -> int:
    label, fetcher, endpoint_tmpl = FETCHERS[args.family]
    symbol = args.symbol
    if args.family in {"ibkr_positions", "ibkr_account_summary"} and not symbol:
        symbol = config.get("MIRA_IBKR_ACCOUNT", "ALL") or "ALL"
    elif not symbol:
        print(f"error: fetch {args.family} requires a symbol", file=sys.stderr)
        return 2
    try:
        res = fetcher(symbol, as_of=args.as_of, market_scope=args.market_scope)
    except net.FetchError as exc:
        print(f"source_gap: could not fetch {args.family} for {symbol}: {exc}", file=sys.stderr)
        return 1

    records = res.records
    display_object = {
        "ibkr_positions": "IBKR_POSITIONS",
        "ibkr_account_summary": "IBKR_ACCOUNT_SUMMARY",
    }.get(args.family, symbol.upper())
    print(f"# {display_object} {args.family} via {label}  ({len(records)} claims)")
    print(f"{'metric':<22}{'value':>20}  {'unit':<12}{'period':<12}{'tier'}")
    for r in records:
        tier = f"{r.posture.claim_type}/{r.posture.authority_level}"
        print(f"{r.metric:<22}{_fmt(r.value):>20}  {r.unit:<12}{r.period:<12}{tier}")
    if res.series:
        print(f"  + series '{res.series['name']}' ({len(res.series['rows'])} rows)")

    if args.no_emit:
        return 0

    endpoint = endpoint_tmpl.format(
        symbol=symbol.upper(),
        cik10="<cik>",
        series_id=symbol,
        host=config.get("MIRA_IBKR_HOST", "127.0.0.1") or "127.0.0.1",
        port=config.get("MIRA_IBKR_PORT", "7497") or "7497",
    )
    ingestion_route = "authorized_provider" if args.family.startswith("ibkr_") else "public_on_demand"
    must_refresh_if = (
        "new broker snapshot, session reconnect, entitlement change, or position/account change"
        if args.family.startswith("ibkr_") else ""
    )
    result = emit_bundle(
        records, out_dir=args.out, research_object=display_object,
        market_scope=args.market_scope, endpoint=endpoint,
        params=f"symbol={display_object}", series=res.series,
        ingestion_route=ingestion_route, must_refresh_if=must_refresh_if,
    )
    print("\n# emitted")
    for key in ("manifest", "evidence_log", "ingestion_log", "calculation_ledger", "series"):
        if result.get(key):
            print(f"  {key:<20} {result[key]}")
    print(f"  claims={result['n_records']} series_rows={result['n_series_rows']} "
          f"ledgered={result['n_ledgered']} (disclosed/market values need no ledger)")
    return 0


def _fmt(v) -> str:
    if isinstance(v, (int, float)):
        return f"{v:,}"
    return str(v)


if __name__ == "__main__":
    raise SystemExit(main())
