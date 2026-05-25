# sedi/tests/test_sedi_integration.py
"""
Integration test: full pipeline from request text -> design output.
Does not require network access or MCP server.
"""
import tempfile
from pathlib import Path
from unittest.mock import patch


def test_full_pipeline_b2b():
    with tempfile.TemporaryDirectory() as tmp:
        store = Path(tmp) / ".global-design-skill"
        with patch("sedi.local_store.STORE_ROOT", store):
            from sedi.local_store import init_store
            from sedi.perception import analyse_request
            from sedi.cognition import select_blueprint, resolve_knowledge
            from sedi.execution import generate_output
            from sedi.feedback_engine import record_feedback, get_success_rate
            from sedi.evolution import capture_baseline, update_current_accuracy

            init_store()

            # Perception
            analysis = analyse_request(
                "create a landing page for an industrial pump manufacturer with rfq form"
            )
            assert analysis.sector == "b2b-products"
            assert analysis.intent == "create"

            # Cognition
            blueprint = select_blueprint(analysis)
            assert "landing-page" in blueprint or "from-scratch" in blueprint

            knowledge = resolve_knowledge(
                analysis,
                static_rules={
                    "required_elements": ["rfq-form", "certifications"],
                    "banned_patterns": ["generic-centered-hero"],
                    "trust_signals": ["iso-certification", "client-logos"],
                    "conversion_elements": ["rfq-form"],
                },
                learned_rules=None,
            )
            assert knowledge["priority"].value == 3  # STATIC

            # Execution
            output = generate_output(analysis, blueprint, knowledge)
            assert output.sector == "b2b-products"
            assert len(output.citations) > 0

            # Feedback loop
            for _ in range(5):
                record_feedback("b2b-products", "industrial-pumps", revision_count=1)
            rate = get_success_rate("b2b-products", "industrial-pumps")
            assert rate > 0  # should be 4/5 = 0.8

            # Evolution baseline
            capture_baseline(sample_accuracy=0.85)
            update_current_accuracy(0.88)

            imp_path = store / "metrics" / "improvement_rate.json"
            assert imp_path.exists()


def test_full_pipeline_unknown_sector():
    with tempfile.TemporaryDirectory() as tmp:
        store = Path(tmp) / ".global-design-skill"
        with patch("sedi.local_store.STORE_ROOT", store):
            from sedi.local_store import init_store
            from sedi.perception import analyse_request
            init_store()
            analysis = analyse_request("do the thing")
            assert analysis.sector == "unknown"
