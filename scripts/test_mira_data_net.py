#!/usr/bin/env python3
"""Regression tests for transient HTTP response failures."""

from __future__ import annotations

import http.client
import sys
import tempfile
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.mira_data import net
from tools.mira_data.adapters import sec_companyfacts


class FakeResponse:
    def __init__(self, body_or_error, headers=None):
        self.body_or_error = body_or_error
        self.headers = headers or {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self):
        if isinstance(self.body_or_error, Exception):
            raise self.body_or_error
        return self.body_or_error


def test_incomplete_read_retries() -> None:
    responses = [
        FakeResponse(http.client.IncompleteRead(b'{"partial":', 8)),
        FakeResponse(b'{"ok": true}'),
    ]
    with (
        mock.patch.object(net.urllib.request, "urlopen", side_effect=responses) as urlopen,
        mock.patch.object(net, "_sleep"),
    ):
        result = net.get_json("https://example.test/data", retries=1)

    assert result == {"ok": True}
    assert urlopen.call_count == 2
    print("ok incomplete response is retried")


def test_incomplete_read_exhaustion_is_fetch_error() -> None:
    responses = [
        FakeResponse(http.client.IncompleteRead(b"partial", 4)),
        FakeResponse(http.client.IncompleteRead(b"partial", 4)),
    ]
    with (
        mock.patch.object(net.urllib.request, "urlopen", side_effect=responses),
        mock.patch.object(net, "_sleep"),
    ):
        try:
            net.get("https://example.test/data", retries=1)
        except net.FetchError as exc:
            assert exc.url == "https://example.test/data"
            assert isinstance(exc.__cause__, http.client.IncompleteRead)
        else:
            raise AssertionError("expected FetchError after retry exhaustion")

    print("ok exhausted incomplete responses become FetchError")


def test_complete_json_with_missing_chunk_terminator_is_accepted() -> None:
    response = FakeResponse(
        http.client.IncompleteRead(b'{"complete": true}'),
        headers={"Content-Type": "application/json"},
    )
    with mock.patch.object(net.urllib.request, "urlopen", return_value=response) as urlopen:
        result = net.get_json("https://example.test/data.json")

    assert result == {"complete": True}
    assert urlopen.call_count == 1
    print("ok complete JSON survives a missing chunk terminator")


def test_sec_ticker_map_uses_compact_exchange_payload() -> None:
    payload = {
        "fields": ["cik", "name", "ticker", "exchange"],
        "data": [[320193, "Apple Inc.", "AAPL", "Nasdaq"]],
    }
    with tempfile.TemporaryDirectory() as tmp:
        cache_path = Path(tmp) / "ticker-map.json"
        with (
            mock.patch.object(sec_companyfacts, "_require_contact"),
            mock.patch.object(sec_companyfacts, "_TICKER_CACHE_PATH", cache_path),
            mock.patch.object(sec_companyfacts.net, "get_json", return_value=payload) as get_json,
        ):
            result = sec_companyfacts.load_ticker_cik_map()
            assert cache_path.exists()

    assert result == {"AAPL": "0000320193"}
    assert get_json.call_args.args[0] == sec_companyfacts.TICKER_EXCHANGE_URL
    assert get_json.call_args.kwargs["retries"] == sec_companyfacts.SEC_MAP_RETRIES
    print("ok SEC ticker map prefers compact exchange payload")


def test_sec_ticker_map_falls_back_to_legacy_payload() -> None:
    payload = {"0": {"cik_str": 320193, "ticker": "AAPL", "title": "Apple Inc."}}
    with tempfile.TemporaryDirectory() as tmp:
        with (
            mock.patch.object(sec_companyfacts, "_require_contact"),
            mock.patch.object(sec_companyfacts, "_TICKER_CACHE_PATH", Path(tmp) / "ticker-map.json"),
            mock.patch.object(
                sec_companyfacts.net,
                "get_json",
                side_effect=[net.FetchError("truncated"), payload],
            ) as get_json,
        ):
            result = sec_companyfacts.load_ticker_cik_map()

    assert result == {"AAPL": "0000320193"}
    assert get_json.call_count == 2
    print("ok SEC ticker map falls back to legacy payload")


def test_sec_ticker_map_reuses_fresh_cache() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        cache_path = Path(tmp) / "ticker-map.json"
        cache_path.write_text('{"AAPL": "0000320193"}', encoding="utf-8")
        with (
            mock.patch.object(sec_companyfacts, "_require_contact"),
            mock.patch.object(sec_companyfacts, "_TICKER_CACHE_PATH", cache_path),
            mock.patch.object(sec_companyfacts.net, "get_json") as get_json,
        ):
            result = sec_companyfacts.load_ticker_cik_map()

    assert result == {"AAPL": "0000320193"}
    get_json.assert_not_called()
    print("ok SEC ticker map reuses fresh local cache")


def test_sec_companyfacts_uses_bounded_retries() -> None:
    with (
        mock.patch.object(sec_companyfacts, "_require_contact"),
        mock.patch.object(
            sec_companyfacts.net,
            "get_json",
            return_value={"facts": {"us-gaap": {}}},
        ) as get_json,
    ):
        cik, facts, _ = sec_companyfacts.load_facts("AAPL", cik="0000320193")

    assert cik == "0000320193"
    assert facts == {"us-gaap": {}}
    assert get_json.call_args.kwargs["retries"] == sec_companyfacts.SEC_FACT_RETRIES
    print("ok SEC companyfacts uses bounded retries")


def main() -> int:
    test_incomplete_read_retries()
    test_incomplete_read_exhaustion_is_fetch_error()
    test_complete_json_with_missing_chunk_terminator_is_accepted()
    test_sec_ticker_map_uses_compact_exchange_payload()
    test_sec_ticker_map_falls_back_to_legacy_payload()
    test_sec_ticker_map_reuses_fresh_cache()
    test_sec_companyfacts_uses_bounded_retries()
    print("mira_data_net_tests: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
