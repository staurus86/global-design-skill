# sedi/tests/test_execution.py
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from sedi.execution import generate_output, DesignOutput
from sedi.perception import RequestAnalysis
from sedi.cognition import ConflictPriority

def _make_analysis(sector="b2b-products", intent="create"):
    return RequestAnalysis(
        intent=intent, sector=sector, niche=sector,
        sub_niche=None,
        context={"confidence": 0.9},
        emotions={}, constraints={}
    )

def _make_knowledge(source="static"):
    return {
        "rules": {
            "required_elements": ["rfq-form", "trust-signals"],
            "banned_patterns": ["generic-hero"],
        },
        "source": source,
        "priority": ConflictPriority.STATIC,
    }

def test_output_is_design_output():
    result = generate_output(
        analysis=_make_analysis(),
        blueprint="blueprints/landing-page-from-scratch.md",
        knowledge=_make_knowledge()
    )
    assert isinstance(result, DesignOutput)

def test_output_contains_sector():
    result = generate_output(
        analysis=_make_analysis(sector="finance"),
        blueprint="blueprints/landing-page-from-scratch.md",
        knowledge=_make_knowledge()
    )
    assert result.sector == "finance"

def test_output_cites_sources():
    result = generate_output(
        analysis=_make_analysis(),
        blueprint="blueprints/landing-page-from-scratch.md",
        knowledge=_make_knowledge(source="learned")
    )
    assert len(result.citations) > 0

def test_gates_validation_present():
    result = generate_output(
        analysis=_make_analysis(),
        blueprint="blueprints/landing-page-from-scratch.md",
        knowledge=_make_knowledge()
    )
    assert isinstance(result.gates_passed, list)
