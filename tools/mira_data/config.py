"""Local config loader for the data substrate (stdlib only).

Resolution order (first hit wins):

1. environment variables
2. an explicit file named by ``MIRA_DATA_CONFIG``
3. ``private/mira-data.env`` (gitignored — the standard user location)
4. ``~/.config/mira/mira-data.env``

The file is a simple ``KEY=value`` env format (``#`` comments allowed), so no
third-party parser is needed. User-specific contact + API keys live in
gitignored ``private/`` per the repo's private-state boundary — never tracked.

SEC's access policy requires a contactable User-Agent. Official-data adapters
therefore gate on :func:`is_contact_configured`; users opt in by setting their
real contact, exactly as ``templates/mira-data-config.example`` documents.
"""

from __future__ import annotations

import os

CONFIG_ENV = "MIRA_DATA_CONFIG"
DEFAULT_PATHS = [
    "private/mira-data.env",
    os.path.expanduser("~/.config/mira/mira-data.env"),
]
# Shipped placeholder: works for sources that don't require identification, but
# is_contact_configured() treats it as "not configured" so SEC stays gated.
PLACEHOLDER_UA = "Mira-market-research-agents contact@example.com"

_file_cache: dict | None = None


def _candidate_paths() -> list[str]:
    paths = []
    explicit = os.environ.get(CONFIG_ENV)
    if explicit:
        paths.append(explicit)
    paths.extend(DEFAULT_PATHS)
    return paths


def _load_file(path: str) -> dict:
    data: dict[str, str] = {}
    try:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, val = line.split("=", 1)
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if key:
                    data[key] = val
    except OSError:
        pass
    return data


def _file_config() -> dict:
    global _file_cache
    if _file_cache is None:
        merged: dict[str, str] = {}
        # later paths are lower priority: load them first, let earlier overwrite.
        for path in reversed(_candidate_paths()):
            merged.update(_load_file(path))
        _file_cache = merged
    return _file_cache


def reset_cache() -> None:
    """Drop the cached file config (used by tests / after writing the file)."""
    global _file_cache
    _file_cache = None


def get(key: str, default: str | None = None) -> str | None:
    """Resolve ``key`` from env first, then the config file."""
    if key in os.environ:
        return os.environ[key]
    return _file_config().get(key, default)


def contact_ua() -> tuple[str, bool]:
    """Return ``(user_agent, configured)``.

    ``configured`` is False only when we fall back to the shipped placeholder.
    """
    ua = get("MIRA_HTTP_UA")
    if ua:
        return ua, True
    email = get("MIRA_CONTACT_EMAIL")
    if email:
        name = get("MIRA_CONTACT_NAME", "Mira-market-research-agents")
        return f"{name} {email}", True
    return PLACEHOLDER_UA, False


def is_contact_configured() -> bool:
    return contact_ua()[1]


def config_hint() -> str:
    """One-line instruction for configuring a contact."""
    return (
        "Set your contact in private/mira-data.env "
        "(MIRA_CONTACT_EMAIL=you@domain.com) - see templates/mira-data-config.example."
    )
