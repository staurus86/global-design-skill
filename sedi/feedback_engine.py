# sedi/feedback_engine.py
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
import sedi.local_store as _local_store

_WEIGHT_MIN = 0.1
_WEIGHT_MAX = 2.0
_MIN_INTERACTIONS = 5

_IMPLICIT_SCORES: dict[int, float] = {
    0: 5.0,
    1: 4.0,
    2: 3.0,
}


def _feedback_path(sector: str, niche: str) -> Path:
    _local_store.init_store()
    return _local_store.STORE_ROOT / "feedback" / f"{sector}__{niche}.json"


def _weights_path(sector: str) -> Path:
    _local_store.init_store()
    return _local_store.STORE_ROOT / "weights" / f"{sector}.json"


def _load_feedback(sector: str, niche: str) -> dict:
    path = _feedback_path(sector, niche)
    if path.exists():
        return json.loads(path.read_text())
    return {"interactions": [], "total": 0}


def _save_feedback(sector: str, niche: str, data: dict) -> None:
    _feedback_path(sector, niche).write_text(json.dumps(data, indent=2))


def record_feedback(
    sector: str,
    niche: str,
    explicit_rating: int | None = None,
    revision_count: int | None = None,
    abandoned: bool = False,
) -> None:
    if explicit_rating is not None:
        score = float(explicit_rating)
    elif abandoned:
        score = 1.0
    elif revision_count is not None:
        score = _IMPLICIT_SCORES.get(revision_count, 2.0 if revision_count >= 3 else 3.0)
    else:
        score = 5.0

    data = _load_feedback(sector, niche)
    data["interactions"].append({
        "score": score,
        "recorded_at": datetime.now(timezone.utc).isoformat(),
    })
    data["total"] = len(data["interactions"])
    _save_feedback(sector, niche, data)


def get_success_rate(sector: str, niche: str) -> float:
    data = _load_feedback(sector, niche)
    interactions = data.get("interactions", [])
    if len(interactions) < _MIN_INTERACTIONS:
        return 0.0
    return sum(i["score"] for i in interactions) / (len(interactions) * 5.0)


def _load_weights(sector: str) -> dict:
    path = _weights_path(sector)
    if path.exists():
        return json.loads(path.read_text())
    return {}


def _save_weights(sector: str, data: dict) -> None:
    _weights_path(sector).write_text(json.dumps(data, indent=2))


def update_pattern_weight(sector: str, pattern: str, delta: float) -> None:
    weights = _load_weights(sector)
    current = weights.get(pattern, 1.0)
    updated = max(_WEIGHT_MIN, min(_WEIGHT_MAX, current + delta))
    weights[pattern] = updated
    _save_weights(sector, weights)


def get_pattern_weight(sector: str, pattern: str) -> float:
    weights = _load_weights(sector)
    return weights.get(pattern, 1.0)


def reset_weights(sector: str | None = None) -> str:
    if sector:
        path = _weights_path(sector)
        if path.exists():
            path.unlink()
        return json.dumps({"reset": sector, "status": "ok"})
    weights_dir = _local_store.STORE_ROOT / "weights"
    deleted = []
    for f in weights_dir.glob("*.json"):
        f.unlink()
        deleted.append(f.stem)
    return json.dumps({"reset": "all", "deleted": deleted})
