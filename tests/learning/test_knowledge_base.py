import json
import pytest
from pathlib import Path
from learning.knowledge_base import KnowledgeBase

@pytest.fixture
def kb(tmp_path):
    return KnowledgeBase(base_dir=tmp_path / "knowledge")

def test_save_and_get(kb):
    data = {
        "sector": "b2b-products",
        "niche": "industrial-pumps",
        "sub_niche": None,
        "confidence_score": 0.85,
        "patterns": {"components": ["rfq-form"]},
        "rules": {"required_elements": ["Technical specs"]},
        "references": [],
    }
    kb.save("b2b-products", "industrial-pumps", data)
    result = kb.get("b2b-products", "industrial-pumps")
    assert result is not None
    assert result["niche"] == "industrial-pumps"
    assert result["confidence_score"] == 0.85

def test_get_missing_returns_none(kb):
    assert kb.get("b2b-products", "nonexistent") is None

def test_storage_limits_enforced(kb):
    data = {"sector": "b2b-products", "niche": "test", "references": [{"url": f"http://example{i}.com"} for i in range(15)]}
    kb.save("b2b-products", "test", data)
    result = kb.get("b2b-products", "test")
    assert len(result["references"]) <= 10

def test_list_niches(kb):
    kb.save("b2b-products", "pumps", {"sector": "b2b-products", "niche": "pumps"})
    kb.save("services", "tarot", {"sector": "services", "niche": "tarot"})
    niches = kb.list_niches()
    assert any(n["niche"] == "pumps" for n in niches)
    assert any(n["niche"] == "tarot" for n in niches)

def test_delete_niche(kb):
    kb.save("b2b-products", "pumps", {"sector": "b2b-products", "niche": "pumps"})
    kb.delete("b2b-products", "pumps")
    assert kb.get("b2b-products", "pumps") is None

def test_is_stale_returns_true_for_old_entry(kb):
    import datetime
    old_date = (datetime.datetime.now() - datetime.timedelta(days=100)).isoformat() + "Z"
    kb.save("b2b-products", "pumps", {
        "sector": "b2b-products", "niche": "pumps",
        "last_updated": old_date, "stale_after_days": 90,
    })
    assert kb.is_stale("b2b-products", "pumps") is True
