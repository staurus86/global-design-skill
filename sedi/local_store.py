# sedi/local_store.py
import os
import stat
from pathlib import Path

STORE_ROOT = Path.home() / ".global-design-skill"

_SUBDIRS = ["knowledge", "weights", "feedback", "evolution_log", "metrics"]


def _get_store_root() -> Path:
    """Get the current STORE_ROOT, allowing for test patching."""
    import sedi.local_store as module
    return module.STORE_ROOT


def init_store() -> None:
    """Create local store directories with restricted permissions on first call."""
    root = _get_store_root()
    root.mkdir(parents=True, exist_ok=True)
    if os.name != "nt":
        os.chmod(root, stat.S_IRWXU)
    for subdir in _SUBDIRS:
        (root / subdir).mkdir(exist_ok=True)


def store_path(subdir: str, filename: str) -> Path:
    return _get_store_root() / subdir / filename
