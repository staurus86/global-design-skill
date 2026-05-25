import json, tempfile, os
from pathlib import Path
from unittest.mock import patch

def test_init_creates_directories():
    with tempfile.TemporaryDirectory() as tmp:
        test_root = Path(tmp) / ".global-design-skill"
        with patch("sedi.local_store.STORE_ROOT", test_root):
            from sedi.local_store import init_store
            init_store()
            for subdir in ["knowledge", "weights", "feedback", "evolution_log", "metrics"]:
                assert (test_root / subdir).is_dir(), f"Missing directory: {test_root / subdir}"

def test_init_is_idempotent():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / ".global-design-skill"
        with patch("sedi.local_store.STORE_ROOT", root):
            from sedi.local_store import init_store
            init_store()
            init_store()  # second call must not raise
            assert (root / "knowledge").is_dir(), f"Missing directory: {root / 'knowledge'}"
