import pytest
from learning.sector_classifier import classify_sector

def test_classifies_b2b():
    result = classify_sector("industrial pump manufacturer B2B equipment")
    assert result["sector"] == "b2b-products"
    assert result["confidence"] >= 0.6

def test_classifies_services():
    result = classify_sector("tarot reader booking website")
    assert result["sector"] == "services"
    assert result["confidence"] >= 0.6

def test_unknown_returns_low_confidence():
    result = classify_sector("xyzzy frobble nonce")
    assert result["confidence"] < 0.5
    assert result["sector"] == "unknown"

def test_returns_required_keys():
    result = classify_sector("online shop")
    assert "sector" in result
    assert "confidence" in result
    assert "sub_niche" in result
    assert "alternatives" in result
