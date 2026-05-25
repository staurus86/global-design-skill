# sedi/tests/test_evolution.py
import json, tempfile
from pathlib import Path
from unittest.mock import patch

def test_capture_baseline_creates_file():
    with tempfile.TemporaryDirectory() as tmp:
        store = Path(tmp) / ".global-design-skill"
        with patch("sedi.local_store.STORE_ROOT", store):
            from sedi.local_store import init_store
            from sedi.evolution import capture_baseline
            init_store()
            capture_baseline(sample_accuracy=0.87)
            baseline_path = store / "metrics" / "baseline_accuracy.json"
            assert baseline_path.exists()
            data = json.loads(baseline_path.read_text())
            assert data["accuracy"] == 0.87

def test_update_current_accuracy():
    with tempfile.TemporaryDirectory() as tmp:
        store = Path(tmp) / ".global-design-skill"
        with patch("sedi.local_store.STORE_ROOT", store):
            from sedi.local_store import init_store
            from sedi.evolution import capture_baseline, update_current_accuracy
            init_store()
            capture_baseline(sample_accuracy=0.80)
            update_current_accuracy(new_accuracy=0.85)
            current_path = store / "metrics" / "current_accuracy.json"
            imp_path = store / "metrics" / "improvement_rate.json"
            assert current_path.exists()
            assert imp_path.exists()
            imp = json.loads(imp_path.read_text())
            assert abs(imp["delta"] - 0.05) < 0.001

def test_log_evolution_event():
    with tempfile.TemporaryDirectory() as tmp:
        store = Path(tmp) / ".global-design-skill"
        with patch("sedi.local_store.STORE_ROOT", store):
            from sedi.local_store import init_store
            from sedi.evolution import log_evolution_event
            init_store()
            log_evolution_event("retrain", {"sector": "finance", "reason": "stale"})
            logs = list((store / "evolution_log").glob("*.json"))
            assert len(logs) == 1

def test_check_stale_returns_list():
    with tempfile.TemporaryDirectory() as tmp:
        store = Path(tmp) / ".global-design-skill"
        with patch("sedi.local_store.STORE_ROOT", store):
            from sedi.local_store import init_store
            from sedi.evolution import check_stale_niches
            init_store()
            result = check_stale_niches()
            assert isinstance(result, list)
