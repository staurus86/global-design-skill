# mcp-server/tools/industry_rules.py
"""Check design descriptions for sector-specific banned patterns."""
import json
import re
from pathlib import Path

INDUSTRIES_DIR = Path(__file__).parent.parent.parent / "industries"


def check_banned_patterns(sector: str, content: str) -> str:
    """Check plain-text design description for banned patterns.

    Args:
        sector: Sector ID (e.g. "b2b-products")
        content: Plain-text description of the design (not HTML)

    Returns JSON string: {"violations": list[str], "warnings": list[str]}
    """
    sector_file = INDUSTRIES_DIR / f"{sector}.md"
    if not sector_file.exists():
        return json.dumps({"error": f"Sector '{sector}' not found"})

    text = sector_file.read_text(encoding="utf-8")

    # Extract Banned Patterns section
    bp_match = re.search(r"## Banned Patterns\n(.*?)(?=\n##|\Z)", text, re.DOTALL)
    if not bp_match:
        return json.dumps({"violations": [], "warnings": [], "note": "No banned patterns defined"})

    banned_section = bp_match.group(1)
    # Each line starting with "- " is a banned pattern rule
    banned_rules = re.findall(r"^- (.+)$", banned_section, re.MULTILINE)

    content_lower = content.lower()
    violations = []
    warnings = []

    for rule in banned_rules:
        # Remove markdown formatting (bold, code)
        clean_rule = re.sub(r"\*\*(.+?)\*\*", r"\1", rule)
        clean_rule = re.sub(r"`(.+?)`", r"\1", clean_rule)

        # Extract multi-word phrases and single significant words for matching
        phrases = _extract_phrases(clean_rule)
        matched_phrases = [ph for ph in phrases if ph.lower() in content_lower]

        # Extract individual keywords as fallback
        keywords = _extract_keywords(clean_rule)
        matched_keywords = [kw for kw in keywords if kw.lower() in content_lower]

        if matched_phrases:
            # Any multi-word phrase match is a strong signal
            violations.append(f"{rule} (matched: {', '.join(matched_phrases)})")
        elif len(matched_keywords) >= 2:
            violations.append(f"{rule} (matched: {', '.join(matched_keywords)})")
        elif len(matched_keywords) == 1:
            warnings.append(f"Possible issue: {rule} (check for: {matched_keywords[0]})")

    return json.dumps({"violations": violations, "warnings": warnings})


def _extract_phrases(rule: str) -> list[str]:
    """Extract quoted or quoted-like multi-word phrases from a rule.

    Returns phrases like 'Buy Now', 'hidden pricing' that appear verbatim in rules.
    """
    phrases = []

    # Match content inside double quotes
    quoted = re.findall(r'"([^"]+)"', rule)
    phrases.extend(quoted)

    # Match content inside single quotes
    single_quoted = re.findall(r"'([^']+)'", rule)
    phrases.extend(single_quoted)

    # Also extract known compound terms (2-word combinations of significant words)
    stopwords = {
        "or", "and", "for", "the", "a", "an", "with", "without", "no", "not",
        "in", "on", "of", "to", "is", "are", "at", "by", "as", "from",
    }
    words = [w.strip(".,;:'\"()") for w in rule.split()]
    sig_words = [w for w in words if w.lower() not in stopwords and len(w) > 3]

    # Generate 2-word combinations from adjacent significant words
    for i in range(len(sig_words) - 1):
        phrase = f"{sig_words[i]} {sig_words[i+1]}"
        if len(phrase) > 7:  # skip trivially short
            phrases.append(phrase)

    return phrases


def _extract_keywords(rule: str) -> list[str]:
    """Extract significant single words from a rule for content matching."""
    stopwords = {
        "or", "and", "for", "the", "a", "an", "with", "without", "no", "not",
        "in", "on", "of", "to", "is", "are", "at", "by", "as", "from",
    }
    words = [w.strip(".,;:'\"()") for w in rule.split()]
    keywords = [w for w in words if w.lower() not in stopwords and len(w) > 3]
    return keywords[:6]
