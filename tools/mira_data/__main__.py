"""CLI: fetch a canonical family for a symbol and emit the artifact bundle.

Usage:
    PYTHONPATH=tools python3 -m mira_data fetch company_financials AAPL --out private/data-smoke

Families wired in P1:
    company_financials   SEC companyfacts (US, fact/L2)
"""

from __future__ import annotations

import argparse
import sys

from . import config, net, technical
from .adapters import bls, sec_companyfacts, yahoo_chart
from .emit import emit_bundle

FETCHERS = {
    "company_financials": ("SEC companyfacts", sec_companyfacts.fetch_company_financials,
                           sec_companyfacts.COMPANYFACTS_URL),
    "market_price": ("Yahoo v8 chart", yahoo_chart.fetch_market_price,
                     yahoo_chart.CHART_URL),
    "macro_series": ("BLS public data", bls.fetch_macro_series, bls.SERIES_URL),
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="mira_data", description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fetch", help="fetch a canonical family and emit artifacts")
    f.add_argument("family", choices=sorted(FETCHERS))
    f.add_argument("symbol")
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

    sub.add_parser("config", help="show resolved data-substrate configuration")

    v = sub.add_parser("validate", help="validate an emitted artifact bundle")
    v.add_argument("dir")

    args = parser.parse_args(argv)
    if args.cmd == "fetch":
        return _do_fetch(args)
    if args.cmd == "technical":
        return _do_technical(args)
    if args.cmd == "config":
        return _do_config(args)
    if args.cmd == "validate":
        return _do_validate(args)
    parser.error("unknown command")
    return 2


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


def _do_config(_args) -> int:
    ua, configured = config.contact_ua()
    print("# mira_data config")
    print(f"  contact_configured : {configured}")
    print(f"  user_agent         : {ua}")
    for key in ("MIRA_CONTACT_EMAIL", "MIRA_CONTACT_NAME", "FRED_API_KEY", "BEA_API_KEY"):
        print(f"  {key:<18} : {'set' if config.get(key) else '—'}")
    print(f"  searched files     : {', '.join(config._candidate_paths())}")
    if not configured:
        print("\n" + config.config_hint())
    return 0


def _do_fetch(args) -> int:
    label, fetcher, endpoint_tmpl = FETCHERS[args.family]
    try:
        res = fetcher(args.symbol, as_of=args.as_of, market_scope=args.market_scope)
    except net.FetchError as exc:
        print(f"source_gap: could not fetch {args.family} for {args.symbol}: {exc}", file=sys.stderr)
        return 1

    records = res.records
    print(f"# {args.symbol.upper()} {args.family} via {label}  ({len(records)} claims)")
    print(f"{'metric':<22}{'value':>20}  {'unit':<12}{'period':<12}{'tier'}")
    for r in records:
        tier = f"{r.posture.claim_type}/{r.posture.authority_level}"
        print(f"{r.metric:<22}{_fmt(r.value):>20}  {r.unit:<12}{r.period:<12}{tier}")
    if res.series:
        print(f"  + series '{res.series['name']}' ({len(res.series['rows'])} rows)")

    if args.no_emit:
        return 0

    endpoint = endpoint_tmpl.format(symbol=args.symbol.upper(), cik10="<cik>", series_id=args.symbol)
    result = emit_bundle(
        records, out_dir=args.out, research_object=args.symbol.upper(),
        market_scope=args.market_scope, endpoint=endpoint,
        params=f"symbol={args.symbol.upper()}", series=res.series,
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
