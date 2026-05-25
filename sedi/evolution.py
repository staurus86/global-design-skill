# sedi/evolution.py
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
import sedi.local_store as _local_store


def _metrics_path(filename: str) -> Path:
    _local_store.init_store()
    return _local_store.STORE_ROOT / "metrics" / filename


def capture_baseline(sample_accuracy: float) -> None:
    data = {
        "accuracy": sample_accuracy,
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "sample_count": 20,
    }
    _metrics_path("baseline_accuracy.json").write_text(json.dumps(data, indent=2))


def update_current_accuracy(new_accuracy: float) -> None:
    baseline_path = _metrics_path("baseline_accuracy.json")
    baseline = 0.0
    if baseline_path.exists():
        baseline = json.loads(baseline_path.read_text()).get("accuracy", 0.0)

    current = {
        "accuracy": new_accuracy,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    _metrics_path("current_accuracy.json").write_text(json.dumps(current, indent=2))

    improvement = {
        "baseline": baseline,
        "current": new_accuracy,
        "delta": round(new_accuracy - baseline, 4),
        "updated_at": current["updated_at"],
    }
    _metrics_path("improvement_rate.json").write_text(json.dumps(improvement, indent=2))


def log_evolution_event(event_type: str, payload: dict) -> None:
    _local_store.init_store()
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    filename = f"{ts}_{event_type}.json"
    entry = {
        "event": event_type,
        "payload": payload,
        "logged_at": datetime.now(timezone.utc).isoformat(),
    }
    (_local_store.STORE_ROOT / "evolution_log" / filename).write_text(json.dumps(entry, indent=2))


def check_stale_niches() -> list[dict]:
    """Return list of niche entries where last_updated exceeds stale_after_days."""
    knowledge_dir = _local_store.STORE_ROOT / "knowledge"
    if not knowledge_dir.exists():
        return []
    stale = []
    now = datetime.now(timezone.utc)
    for f in knowledge_dir.glob("*.json"):
        try:
            data = json.loads(f.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        last_updated_str = data.get("last_updated")
        stale_after = data.get("stale_after_days", 90)
        if not last_updated_str:
            continue
        last_updated = datetime.fromisoformat(last_updated_str.replace("Z", "+00:00"))
        days_old = (now - last_updated).days
        if days_old > stale_after:
            stale.append({
                "sector": data.get("sector"),
                "niche": data.get("niche"),
                "days_old": days_old,
                "stale_after_days": stale_after,
            })
    return stale


def run_weekly_cycle() -> str:
    """Run one evolution cycle: check stale, log."""
    stale = check_stale_niches()
    log_evolution_event("weekly_cycle", {
        "stale_niches_found": len(stale),
        "stale_niches": stale,
    })
    return json.dumps({"status": "ok", "stale_niches": len(stale)})
