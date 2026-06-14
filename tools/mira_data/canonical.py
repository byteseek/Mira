"""Canonical data contract + evidence-tier postures.

The canonical families mirror ``templates/ingestion-layer/field-map.yaml``. Every
adapter returns :class:`CanonicalRecord` objects already stamped with the
registry posture for its source, so downstream emit/evidence code never has to
guess an evidence tier (architecture/data-acquisition-upgrade.md §7).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

# Canonical families — must stay in sync with field-map.yaml's enum.
CANONICAL_FAMILIES = frozenset(
    {
        "company_financials",
        "market_price",
        "valuation_snapshot",
        "consensus_estimate",
        "estimate_revision",
        "transcript_claim",
        "ownership_short_interest",
        "options_surface",
        "portfolio_position",
        "macro_series",
    }
)


@dataclass(frozen=True)
class Posture:
    """The fixed evidence posture a source confers on every datum it yields."""

    source_id: str           # must exist in data/source-registry.csv
    source_class: str        # taxonomy bucket (data/source-class-map.csv)
    authority_level: str     # L1-L6
    claim_type: str          # data/claim-taxonomy.md
    evidence_category: str   # data/evidence-posture-taxonomy.md
    access_method: str       # public_api / web_read / ...
    acquisition_mode: str    # free / free_with_key / paid / manual
    latency_class: str       # live / delayed / filing_cycle / archival


# Posture presets keyed by a short adapter id. This is the single place that
# encodes "Yahoo is L5 market_pricing, SEC/BLS are official fact-grade".
POSTURES: dict[str, Posture] = {
    "sec_companyfacts": Posture(
        source_id="sec_companyfacts_api",
        source_class="regulatory_and_exchange",
        authority_level="L2",
        claim_type="reported_metric",
        evidence_category="reported_fact",
        access_method="public_api",
        acquisition_mode="free",
        latency_class="filing_cycle",
    ),
    "yahoo_chart": Posture(
        source_id="yahoo_chart_api_v8",
        source_class="market_price_and_trading",
        authority_level="L5",
        claim_type="market_pricing",
        evidence_category="market_pricing",
        access_method="public_api",
        acquisition_mode="free",
        latency_class="delayed",
    ),
    "bls": Posture(
        source_id="bls_public_data_api",
        source_class="official_macro_and_industry",
        authority_level="L2",
        claim_type="fact",
        evidence_category="reported_fact",
        access_method="public_api",
        acquisition_mode="free",
        latency_class="delayed",
    ),
    "ibkr_gateway": Posture(
        source_id="ibkr_gateway_local",
        source_class="market_price_and_trading",
        authority_level="L5",
        claim_type="market_pricing",
        evidence_category="market_pricing",
        access_method="local_gateway",
        acquisition_mode="authorized_provider",
        latency_class="live",
    ),
    "ibkr_gateway_positions": Posture(
        source_id="ibkr_gateway_local",
        source_class="market_price_and_trading",
        authority_level="L5",
        claim_type="fact",
        evidence_category="reported_fact",
        access_method="local_gateway",
        acquisition_mode="authorized_provider",
        latency_class="live",
    ),
}


@dataclass
class FetchResult:
    """What an adapter returns: claim-level records + an optional bulk series.

    ``records`` become evidence-log rows (a handful of point claims). ``series``
    is an optional time-series dataset (e.g. full OHLCV) too large for the
    evidence log — it is written as a side CSV that the manifest points at.
    Shape: ``{"name": str, "columns": list[str], "rows": list[dict]}``.
    """

    records: list["CanonicalRecord"]
    series: Optional[dict] = None


def derived_posture(base: Posture) -> Posture:
    """Posture for a Mira-computed number: derived_calculation / L6 / derived."""
    return Posture(
        source_id=base.source_id,
        source_class="mira_derived_analysis",
        authority_level="L6",
        claim_type="derived_calculation",
        evidence_category="inference",
        access_method=base.access_method,
        acquisition_mode="derived",
        latency_class=base.latency_class,
    )


@dataclass
class CanonicalRecord:
    """One canonical datum, carrying everything emit/evidence code needs.

    ``derived`` is the hinge for the ledger rule (arch doc §8): issuer-disclosed
    values are ``derived=False`` (reported, no ledger); only numbers Mira itself
    computes and that affect a judgment are ``derived=True`` (ledger required).
    """

    family: str
    research_object: str
    market_scope: str
    metric: str                       # canonical field / claim_area
    value: Any
    unit: str
    period: str                       # e.g. "FY2025" or "2026-03-31"
    period_type: str                  # point_in_time | fiscal_period | ...
    as_of_date: str                   # retrieval as-of (YYYY-MM-DD)
    source_date: str                  # filing / observation date (YYYY-MM-DD)
    posture: Posture
    url_or_path: str
    currency: Optional[str] = None
    claim_text: str = ""
    confidence: str = "medium"
    freshness_status: str = "current"  # current/acceptable_for_period/preliminary/stale/unknown
    # Derived-only fields (ignored unless derived=True):
    derived: bool = False
    upstream_sources: str = ""         # ";"-joined source_ids feeding the calc
    formula: str = ""
    cross_check: str = ""
    provenance: dict = field(default_factory=dict)  # raw vendor tag/form/fy/fp

    def __post_init__(self) -> None:
        if self.family not in CANONICAL_FAMILIES:
            raise ValueError(f"unknown canonical family: {self.family!r}")
        if self.derived and self.posture.claim_type != "derived_calculation":
            # A Mira-computed, judgment-affecting number must be claim-typed
            # derived_calculation so validate_repo.py:678 (Formula/ledger
            # requirement) actually fires. Promote the posture as a safety net.
            self.posture = derived_posture(self.posture)
        if not self.claim_text:
            self.claim_text = (
                f"{self.research_object} {self.metric} = "
                f"{self.value} {self.unit} ({self.period})"
            )

    @property
    def claim_type(self) -> str:
        return self.posture.claim_type
