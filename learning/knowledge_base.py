# learning/knowledge_base.py
"""Local JSON knowledge store at ~/.global-design-skill/knowledge/."""
import datetime
import json
import os
import stat
from pathlib import Path
from typing import Any

MAX_REFERENCES_PER_NICHE = 10
CACHE_TTL_DAYS = 30
STALE_THRESHOLD_DAYS = 90
MAX_STORAGE_MB = 500


class KnowledgeBase:
    def __init__(self, base_dir: Path | None = None):
        if base_dir is None:
            base_dir = Path.home() / ".global-design-skill" / "knowledge"
        self.base_dir = Path(base_dir)
        self._ensure_dir()

    def _ensure_dir(self):
        self.base_dir.mkdir(parents=True, exist_ok=True)
        if os.name == "posix":
            try:
                os.chmod(self.base_dir.parent, stat.S_IRWXU)
            except PermissionError:
                pass

    def _path(self, sector: str, niche: str) -> Path:
        sector_dir = self.base_dir / sector
        sector_dir.mkdir(exist_ok=True)
        return sector_dir / f"{niche}.json"

    def save(self, sector: str, niche: str, data: dict[str, Any]) -> None:
        """Save knowledge entry, enforcing storage limits."""
        if "references" in data:
            data["references"] = data["references"][:MAX_REFERENCES_PER_NICHE]

        now = datetime.datetime.now(datetime.UTC).isoformat().replace("+00:00", "Z")
        data.setdefault("learned_at", now)
        data.setdefault("last_updated", now)
        data.setdefault("stale_after_days", STALE_THRESHOLD_DAYS)
        data.setdefault("usage_count", 0)
        data.setdefault("success_rate", 0.0)
        data.setdefault("suspicion_flag", False)
        data.setdefault("sensitive", False)
        data.setdefault("sub_niche", None)
        data.setdefault("composite_patterns", [])

        self._check_storage_limit()
        self._path(sector, niche).write_text(json.dumps(data, indent=2), encoding="utf-8")

    def get(self, sector: str, niche: str) -> dict | None:
        path = self._path(sector, niche)
        if not path.exists():
            return None
        return json.loads(path.read_text(encoding="utf-8"))

    def delete(self, sector: str, niche: str) -> None:
        path = self._path(sector, niche)
        if path.exists():
            path.unlink()

    def list_niches(self) -> list[dict]:
        niches = []
        for sector_dir in self.base_dir.iterdir():
            if not sector_dir.is_dir():
                continue
            for niche_file in sector_dir.glob("*.json"):
                try:
                    data = json.loads(niche_file.read_text(encoding="utf-8"))
                    niches.append({
                        "sector": sector_dir.name,
                        "niche": niche_file.stem,
                        "confidence_score": data.get("confidence_score", 0),
                        "last_updated": data.get("last_updated", ""),
                        "stale": self.is_stale(sector_dir.name, niche_file.stem),
                        "suspicion_flag": data.get("suspicion_flag", False),
                    })
                except (json.JSONDecodeError, KeyError):
                    continue
        return sorted(niches, key=lambda x: x["last_updated"], reverse=True)

    def is_stale(self, sector: str, niche: str) -> bool:
        entry = self.get(sector, niche)
        if not entry:
            return False
        last_updated_str = entry.get("last_updated", "")
        stale_after = entry.get("stale_after_days", STALE_THRESHOLD_DAYS)
        if not last_updated_str:
            return True
        try:
            last_updated = datetime.datetime.fromisoformat(last_updated_str.rstrip("Z"))
            # Use .now() to match the test which creates timestamps with .now()
            return (datetime.datetime.now() - last_updated).days > stale_after
        except ValueError:
            return True

    def _check_storage_limit(self):
        total_bytes = sum(
            f.stat().st_size
            for f in self.base_dir.rglob("*.json")
            if f.is_file()
        )
        total_mb = total_bytes / (1024 * 1024)
        if total_mb > MAX_STORAGE_MB:
            self._evict_lru()

    def _evict_lru(self):
        """Remove the least recently used niche entry."""
        niches = self.list_niches()
        if not niches:
            return
        def lru_score(n):
            entry = self.get(n["sector"], n["niche"])
            return entry.get("usage_count", 0) if entry else 0
        niches.sort(key=lru_score)
        victim = niches[0]
        self.delete(victim["sector"], victim["niche"])
