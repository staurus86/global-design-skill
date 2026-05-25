# learning/gap_detector.py
"""Compare extracted patterns against static industry rules to detect gaps."""
import re
from pathlib import Path

INDUSTRIES_DIR = Path(__file__).parent.parent / "industries"

SIGNAL_KEYWORDS = {
    "certifications": ["certification", "iso", "ce ", "compliance", "licence", "as9100", "api q1"],
    "client-logos":   ["client", "logo", "customer", "partner"],
    "reviews-testimonials": ["testimonial", "review", "case stud", "social proof"],
    "security-badge": ["security", "ssl", "encrypt", "secure"],
    "guarantee":      ["guarantee", "money-back", "refund"],
}

COMPONENT_KEYWORDS = {
    "rfq-form":             ["rfq", "request quote", "quote form"],
    "product-configurator": ["configurator", "configure", "3d preview"],
    "booking":              ["booking", "calendar", "schedule", "appointment"],
    "pricing-table":        ["pricing", "price", "plan", "tier"],
    "file-upload-form":     ["cad", "drawing", "spec", "upload"],
    "testimonials":         ["testimonial", "review", "quote"],
    "search":               ["search", "filter", "find"],
}


def detect_gaps(sector: str, extracted: dict) -> dict:
    """Detect what is missing from extracted patterns vs static sector rules.

    Args:
        sector:    Sector ID (e.g. "b2b-products")
        extracted: Output from pattern_extractor.extract_patterns()

    Returns dict: {missing_trust_signals, missing_components, missing_conversion,
                   suspicion_flag, notes}
    """
    sector_file = INDUSTRIES_DIR / f"{sector}.md"
    if not sector_file.exists():
        return {"error": f"Sector file not found: {sector}.md"}

    text = sector_file.read_text(encoding="utf-8").replace('\r\n', '\n').lower()

    required_section = _get_section(text, "required elements")
    trust_section    = _get_section(text, "trust signals")

    missing_trust    = _find_missing(extracted.get("trust_signals", []),
                                      SIGNAL_KEYWORDS, trust_section)
    missing_comps    = _find_missing(extracted.get("components", []),
                                      COMPONENT_KEYWORDS, required_section)

    total_required = len([kw for kw in COMPONENT_KEYWORDS if any(k in required_section for k in COMPONENT_KEYWORDS[kw])])
    missing_count  = len(missing_comps)
    suspicion_flag = total_required > 0 and (missing_count / max(total_required, 1)) > 0.4

    return {
        "missing_trust_signals": missing_trust,
        "missing_components":    missing_comps,
        "suspicion_flag":        suspicion_flag,
        "notes": f"Checked against {sector}.md static rules",
    }


def _get_section(text: str, heading: str) -> str:
    match = re.search(rf"## {re.escape(heading)}\n(.*?)(?=\n##|\Z)", text, re.DOTALL)
    return match.group(1) if match else ""


def _find_missing(extracted_list: list[str], keyword_map: dict, section_text: str) -> list[str]:
    missing = []
    for name, keywords in keyword_map.items():
        required_in_static = any(kw in section_text for kw in keywords)
        present_in_extracted = name in extracted_list
        if required_in_static and not present_in_extracted:
            missing.append(name)
    return missing
