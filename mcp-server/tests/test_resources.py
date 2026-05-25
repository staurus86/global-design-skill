# mcp-server/tests/test_resources.py
"""Tests for _read_repo_file helper and GDS_MCP_SAFE_MODE flag."""

import importlib
import os
import sys
from pathlib import Path
from unittest import mock

import pytest

# Ensure mcp-server/ is on path
sys.path.insert(0, str(Path(__file__).parent.parent))


def _get_read_repo_file():
    """Import _read_repo_file from server (re-import each time to pick up env changes)."""
    if "server" in sys.modules:
        del sys.modules["server"]
    import server
    return server._read_repo_file


class TestReadRepoFile:
    def test_reads_existing_file(self):
        fn = _get_read_repo_file()
        result = fn("industries/b2b-products.md")
        assert len(result) > 100
        assert "---" in result  # has frontmatter

    def test_returns_error_string_for_missing_file(self):
        fn = _get_read_repo_file()
        result = fn("industries/does-not-exist.md")
        assert "not found" in result.lower()
        assert "does-not-exist" in result

    def test_normalizes_crlf(self, tmp_path):
        fn = _get_read_repo_file()
        # The function reads from _REPO_ROOT; we test normalization indirectly
        # by checking that none of the actual files return \r\n after reading
        result = fn("industries/b2b-products.md")
        assert "\r\n" not in result
        assert "\r" not in result

    def test_tokens_css_readable(self):
        fn = _get_read_repo_file()
        result = fn("tokens/tokens.css")
        assert "--color-accent" in result or "color" in result.lower()

    def test_rule_file_readable(self):
        fn = _get_read_repo_file()
        result = fn("rules/07-accessibility.md")
        assert len(result) > 200


class TestSafeMode:
    def test_safe_mode_env_false_by_default(self):
        env = {k: v for k, v in os.environ.items() if k != "GDS_MCP_SAFE_MODE"}
        with mock.patch.dict(os.environ, env, clear=True):
            if "server" in sys.modules:
                del sys.modules["server"]
            import server
            assert server._SAFE_MODE is False

    def test_safe_mode_env_set_to_1(self):
        with mock.patch.dict(os.environ, {"GDS_MCP_SAFE_MODE": "1"}):
            if "server" in sys.modules:
                del sys.modules["server"]
            import server
            assert server._SAFE_MODE is True

    def test_safe_mode_env_set_to_true(self):
        with mock.patch.dict(os.environ, {"GDS_MCP_SAFE_MODE": "true"}):
            if "server" in sys.modules:
                del sys.modules["server"]
            import server
            assert server._SAFE_MODE is True

    def test_safe_mode_env_set_to_0_is_false(self):
        with mock.patch.dict(os.environ, {"GDS_MCP_SAFE_MODE": "0"}):
            if "server" in sys.modules:
                del sys.modules["server"]
            import server
            assert server._SAFE_MODE is False

    def test_safe_mode_env_set_to_false_string_is_false(self):
        with mock.patch.dict(os.environ, {"GDS_MCP_SAFE_MODE": "false"}):
            if "server" in sys.modules:
                del sys.modules["server"]
            import server
            assert server._SAFE_MODE is False
