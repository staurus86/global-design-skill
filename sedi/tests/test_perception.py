# sedi/tests/test_perception.py
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from sedi.perception import analyse_request, RequestAnalysis

def test_create_intent_detected():
    result = analyse_request("design a landing page for an industrial pump manufacturer")
    assert isinstance(result, RequestAnalysis)
    assert result.intent == "create"
    assert result.sector == "b2b-products"

def test_audit_intent_detected():
    result = analyse_request("audit this SaaS hero section")
    assert result.intent == "audit"
    assert result.sector == "tech-saas"

def test_low_confidence_returns_unknown():
    result = analyse_request("do the thing")
    assert result.sector == "unknown"

def test_sub_niche_populated_for_entertainment():
    result = analyse_request("redesign a casual mobile game landing page")
    assert result.sector == "entertainment"
    assert result.sub_niche == "casual-games"

def test_constraints_extracted():
    result = analyse_request("create a landing page, budget is tight, we use React")
    assert isinstance(result.constraints, dict)
