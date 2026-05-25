# mcp-server/tests/test_sector_context.py
import json
import sys
from pathlib import Path

import pytest

# Add mcp-server directory to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.industry_rules import check_banned_patterns
from tools.sector_context import get_sector_context, list_sectors


def test_check_banned_patterns_finds_violation():
    result = json.loads(check_banned_patterns(
        sector="b2b-products",
        content="We have a Buy Now button and show RFQ form. Pricing is hidden."
    ))
    assert "violations" in result
    # "Buy Now" and hidden pricing are banned in b2b-products
    violation_texts = " ".join(result["violations"]).lower()
    assert any(kw in violation_texts for kw in ["buy now", "hidden", "pricing"])


def test_check_banned_patterns_no_violation():
    result = json.loads(check_banned_patterns(
        sector="b2b-products",
        content="We show technical specs, ISO certifications, and a Request Quote form."
    ))
    assert "violations" in result
    assert len(result["violations"]) == 0


def test_get_sector_context_returns_sections():
    result = json.loads(get_sector_context("b2b-products"))
    assert "sections" in result
    assert "Required Elements" in result["sections"]
    assert "Banned Patterns" in result["sections"]
    assert "frontmatter" in result
    assert result["frontmatter"].get("version") == "1.0.0"


def test_get_sector_context_unknown_sector():
    result = json.loads(get_sector_context("nonexistent-sector"))
    assert "error" in result
    assert "available_sectors" in result


def test_list_sectors_returns_all_13():
    result = json.loads(list_sectors())
    assert isinstance(result, list)
    sector_ids = [s["sector"] for s in result]
    for expected in [
        "b2b-products", "b2c-products", "services", "content-media",
        "education", "health", "finance", "real-estate", "travel",
        "tech-saas", "non-profit", "government", "entertainment",
    ]:
        assert expected in sector_ids, f"Sector {expected} missing from list_sectors()"


def test_list_sectors_each_has_required_fields():
    result = json.loads(list_sectors())
    for item in result:
        assert "sector" in item
        assert "file" in item
