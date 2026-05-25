# sedi/tests/test_feedback_engine.py
import json, tempfile
from pathlib import Path
from unittest.mock import patch

def test_explicit_rating_updates_success_rate():
    with tempfile.TemporaryDirectory() as tmp:
        store = Path(tmp) / ".global-design-skill"
        with patch("sedi.local_store.STORE_ROOT", store):
            from sedi.local_store import init_store
            from sedi.feedback_engine import record_feedback, get_success_rate
            init_store()
            for _ in range(5):
                record_feedback("b2b-products", "industrial-pumps", explicit_rating=5)
            rate = get_success_rate("b2b-products", "industrial-pumps")
            assert rate == 1.0

def test_implicit_score_from_revision_count():
    with tempfile.TemporaryDirectory() as tmp:
        store = Path(tmp) / ".global-design-skill"
        with patch("sedi.local_store.STORE_ROOT", store):
            from sedi.local_store import init_store
            from sedi.feedback_engine import record_feedback, get_success_rate
            init_store()
            for _ in range(5):
                record_feedback("b2b-products", "pumps2", revision_count=0)
            rate = get_success_rate("b2b-products", "pumps2")
            assert rate == 1.0  # implicit 5.0/5 = 1.0

def test_weight_update_within_bounds():
    with tempfile.TemporaryDirectory() as tmp:
        store = Path(tmp) / ".global-design-skill"
        with patch("sedi.local_store.STORE_ROOT", store):
            from sedi.local_store import init_store
            from sedi.feedback_engine import update_pattern_weight, get_pattern_weight
            init_store()
            update_pattern_weight("b2b-products", "rfq-form", delta=+0.1)
            w = get_pattern_weight("b2b-products", "rfq-form")
            assert 0.1 <= w <= 2.0

def test_weight_capped_at_max():
    with tempfile.TemporaryDirectory() as tmp:
        store = Path(tmp) / ".global-design-skill"
        with patch("sedi.local_store.STORE_ROOT", store):
            from sedi.local_store import init_store
            from sedi.feedback_engine import update_pattern_weight, get_pattern_weight
            init_store()
            for _ in range(30):
                update_pattern_weight("b2b-products", "rfq-form2", delta=+0.1)
            w = get_pattern_weight("b2b-products", "rfq-form2")
            assert w <= 2.0
