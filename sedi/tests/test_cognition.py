# sedi/tests/test_cognition.py
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from sedi.cognition import select_blueprint, resolve_knowledge, ConflictPriority
from sedi.perception import RequestAnalysis

def _make_analysis(intent="create", sector="b2b-products", sub_niche=None):
    return RequestAnalysis(
        intent=intent, sector=sector, niche=sector,
        sub_niche=sub_niche,
        context={"confidence": 0.9},
        emotions={}, constraints={}
    )

def test_create_selects_landing_blueprint():
    analysis = _make_analysis(intent="create")
    bp = select_blueprint(analysis)
    assert "landing-page" in bp or "from-scratch" in bp

def test_improve_selects_redesign_blueprint():
    analysis = _make_analysis(intent="improve")
    bp = select_blueprint(analysis)
    assert "redesign" in bp

def test_audit_selects_checklist():
    analysis = _make_analysis(intent="audit")
    bp = select_blueprint(analysis)
    assert "checklist" in bp or "review" in bp

def test_resolve_knowledge_returns_dict():
    analysis = _make_analysis()
    result = resolve_knowledge(analysis, static_rules={}, learned_rules=None)
    assert isinstance(result, dict)
    assert "source" in result
    assert "priority" in result

def test_user_override_has_highest_priority():
    analysis = _make_analysis()
    result = resolve_knowledge(
        analysis,
        static_rules={"required_elements": ["rfq-form"]},
        learned_rules={"required_elements": ["contact-form"]},
        user_override={"required_elements": ["custom-form"]}
    )
    assert result["priority"] == ConflictPriority.USER_OVERRIDE
    assert result["rules"]["required_elements"] == ["custom-form"]
