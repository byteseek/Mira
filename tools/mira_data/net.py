"""Minimal stdlib HTTP helper for Mira data adapters.

No third-party dependencies: just ``urllib``. A descriptive User-Agent is
required by some official endpoints (notably SEC), so it is configurable via
``MIRA_HTTP_UA`` and defaults to a contactable string.
"""

from __future__ import annotations

import http.client
import json
import time
import urllib.error
import urllib.request

from . import config

DEFAULT_TIMEOUT = 30


class FetchError(RuntimeError):
    """Raised when an adapter cannot retrieve usable data.

    Adapters catch this and degrade the conclusion to a ``source_gap`` token
    rather than fabricating data.
    """

    def __init__(self, message: str, *, status: int | None = None, url: str | None = None):
        super().__init__(message)
        self.status = status
        self.url = url


def get(url: str, *, headers: dict | None = None, timeout: int = DEFAULT_TIMEOUT,
        retries: int = 2, backoff: float = 1.5) -> bytes:
    """GET ``url`` and return raw bytes, retrying transient failures.

    Retries on 429 and 5xx; raises :class:`FetchError` on a hard failure so the
    caller can degrade gracefully.
    """
    hdrs = {"User-Agent": config.contact_ua()[0], "Accept-Encoding": "gzip, deflate"}
    if headers:
        hdrs.update(headers)

    last_exc: Exception | None = None
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers=hdrs)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                try:
                    return _read_body(resp)
                except http.client.IncompleteRead as exc:
                    partial = _decode_body(exc.partial, resp.headers.get("Content-Encoding"))
                    if _is_complete_json(partial, url, resp.headers.get("Content-Type")):
                        return partial
                    raise
        except urllib.error.HTTPError as exc:
            last_exc = exc
            if exc.code in (429, 500, 502, 503, 504) and attempt < retries:
                _sleep(backoff * (attempt + 1))
                continue
            raise FetchError(f"HTTP {exc.code} for {url}", status=exc.code, url=url) from exc
        except urllib.error.URLError as exc:
            last_exc = exc
            if attempt < retries:
                _sleep(backoff * (attempt + 1))
                continue
            raise FetchError(f"network error for {url}: {exc.reason}", url=url) from exc
        except (http.client.HTTPException, OSError, EOFError) as exc:
            last_exc = exc
            if attempt < retries:
                _sleep(backoff * (attempt + 1))
                continue
            raise FetchError(f"incomplete or invalid response from {url}: {exc}", url=url) from exc

    raise FetchError(f"exhausted retries for {url}: {last_exc}", url=url)


def get_json(url: str, **kwargs) -> dict:
    """GET ``url`` and parse JSON, raising :class:`FetchError` on bad payloads."""
    raw = get(url, **kwargs)
    try:
        return json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        # A JS anti-bot challenge or HTML error page lands here (e.g. Stooq).
        raise FetchError(f"non-JSON response from {url}: {exc}", url=url) from exc


def _read_body(resp) -> bytes:
    body = resp.read()
    return _decode_body(body, resp.headers.get("Content-Encoding"))


def _decode_body(body: bytes, content_encoding: str | None) -> bytes:
    if content_encoding == "gzip":
        import gzip

        body = gzip.decompress(body)
    elif content_encoding == "deflate":
        import zlib

        body = zlib.decompress(body)
    return body


def _is_complete_json(body: bytes, url: str, content_type: str | None) -> bool:
    if "json" not in (content_type or "").lower() and not url.split("?", 1)[0].endswith(".json"):
        return False
    try:
        json.loads(body.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return False
    return True


def _sleep(seconds: float) -> None:
    # Wrapped so tests can monkeypatch; kept tiny and bounded.
    time.sleep(min(seconds, 10.0))
