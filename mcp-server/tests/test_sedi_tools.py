# mcp-server/tests/test_sedi_tools.py
import json
import sys
import os
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pathlib import Path
from unittest.mock import patch


def test_resolve_suspicion_accept_learned():
    with tempfile.TemporaryDirectory() as tmp:
        store = Path(tmp) / ".global-design-skill"
        with patch("sedi.local_store.STORE_ROOT", store):
            from sedi.local_store import init_store
            init_store()
            kb_path = store / "knowledge" / "b2b-products" / "industrial-pumps.json"
            kb_path.parent.mkdir(parents=True, exist_ok=True)
            kb_path.write_text(json.dumps({
                "sector": "b2b-products", "niche": "industrial-pumps",
                "suspicion_flag": True, "source": "learned",
                "suspicion_resolved_at": None
            }))
            from tools.learning_tools import resolve_suspicion
            result = json.loads(resolve_suspicion("b2b-products", "industrial-pumps", "accept_learned"))
            assert result["status"] == "ok"
            assert result["suspicion_flag"] is False


def test_resolve_suspicion_keep_static():
    with tempfile.TemporaryDirectory() as tmp:
        store = Path(tmp) / ".global-design-skill"
        with patch("sedi.local_store.STORE_ROOT", store):
            from sedi.local_store import init_store
            init_store()
            kb_path = store / "knowledge" / "finance" / "crypto.json"
            kb_path.parent.mkdir(parents=True, exist_ok=True)
            kb_path.write_text(json.dumps({
                "sector": "finance", "niche": "crypto",
                "suspicion_flag": True, "source": "learned",
                "suspicion_resolved_at": None
            }))
            from tools.learning_tools import resolve_suspicion
            result = json.loads(resolve_suspicion("finance", "crypto", "keep_static"))
            assert result["status"] == "ok"
            assert result["source"] == "static"


def test_reset_weights_calls_feedback_engine():
    with tempfile.TemporaryDirectory() as tmp:
        store = Path(tmp) / ".global-design-skill"
        with patch("sedi.local_store.STORE_ROOT", store):
            from sedi.local_store import init_store
            init_store()
            from tools.learning_tools import reset_weights_tool
            result = json.loads(reset_weights_tool(sector="finance"))
            assert result["reset"] == "finance"
