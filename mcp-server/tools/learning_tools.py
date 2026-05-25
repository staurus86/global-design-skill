# mcp-server/tools/learning_tools.py
"""MCP tools for learning from references and retrieving/learning sector context."""
import datetime
import json
import sys
from pathlib import Path

# Allow importing from learning/ directory (project root)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from learning.sector_classifier import classify_sector
from learning.knowledge_base import KnowledgeBase
from learning.ethical_scraper import EthicalScraper
from learning.pattern_extractor import extract_patterns
from learning.gap_detector import detect_gaps
from tools.sector_context import get_sector_context

_kb = KnowledgeBase()
_scraper = EthicalScraper()


def learn_from_reference(url: str, sector: str = None, niche: str = None) -> str:
    """Scrape a reference site, extract patterns, save to knowledge base.

    Returns JSON: {sector, niche, patterns, gaps, suspicion_flag, references_count}
    """
    fetch_result = _scraper.fetch(url)
    if "error" in fetch_result:
        return json.dumps({"error": fetch_result["error"]})

    html = fetch_result["html"]

    if not sector:
        classification = classify_sector(html[:2000])
        sector = classification["sector"]
        if not niche:
            niche = classification.get("sub_niche") or "general"

    niche = niche or "general"

    patterns = extract_patterns(html)
    if "error" in patterns:
        return json.dumps({"error": patterns["error"]})

    gaps = detect_gaps(sector, patterns)

    existing = _kb.get(sector, niche) or {}
    existing_refs = existing.get("references", [])
    existing_refs.append({"url": url, "quality_score": 0.7, "scraped_at": _now()})

    knowledge = {
        "sector": sector,
        "niche": niche,
        "sub_niche": None,
        "source": "learned",
        "confidence_score": round(min(0.5 + len(existing_refs) * 0.05, 0.95), 2),
        "patterns": patterns,
        "rules": {
            "required_elements": [],
            "banned_patterns": [],
            "trust_signals": patterns.get("trust_signals", []),
            "conversion_elements": patterns.get("conversion_elements", []),
        },
        "references": existing_refs,
        "suspicion_flag": gaps.get("suspicion_flag", False),
    }

    _kb.save(sector, niche, knowledge)

    return json.dumps({
        "sector": sector,
        "niche": niche,
        "patterns_found": {k: len(v) if isinstance(v, list) else v for k, v in patterns.items()},
        "gaps": gaps,
        "suspicion_flag": gaps.get("suspicion_flag", False),
        "references_count": len(existing_refs),
        "saved": True,
    })


def get_or_learn_sector(sector: str, niche: str) -> str:
    """Get sector context from static files or knowledge base.

    Priority: industries/*.md -> knowledge_base -> "not found, run learn_from_reference"
    Returns JSON: {source, sector, niche, context}
    """
    static = json.loads(get_sector_context(sector))
    if "error" not in static:
        return json.dumps({
            "source": "static",
            "sector": sector,
            "niche": niche,
            "context": static,
        })

    learned = _kb.get(sector, niche)
    if learned:
        stale = _kb.is_stale(sector, niche)
        return json.dumps({
            "source": "learned" + ("_stale" if stale else ""),
            "sector": sector,
            "niche": niche,
            "stale": stale,
            "context": learned,
        })

    return json.dumps({
        "source": "not_found",
        "sector": sector,
        "niche": niche,
        "action": f"Call learn_from_reference(url=<reference_url>, sector='{sector}', niche='{niche}') to learn this niche.",
    })


def list_learned_niches() -> str:
    """List all niches in the knowledge base with metadata."""
    return json.dumps(_kb.list_niches())


def forget_niche(sector: str, niche: str) -> str:
    """Delete a learned niche from the knowledge base."""
    existing = _kb.get(sector, niche)
    if not existing:
        return json.dumps({"error": f"Niche '{sector}/{niche}' not found in knowledge base"})
    _kb.delete(sector, niche)
    return json.dumps({"deleted": True, "sector": sector, "niche": niche})


def reset_weights(sector: str = None) -> str:
    """Reset pattern weights to neutral (Phase 4 feature stub)."""
    return json.dumps({
        "status": "weights_reset_pending",
        "note": "Weight reset is implemented in Phase 4 (sedi/feedback_engine.py). "
                "Complete Phase 4 to use this tool.",
        "sector": sector,
    })


def resolve_suspicion(sector: str, niche: str, resolution: str) -> str:
    """
    Clear suspicion_flag on a knowledge entry.
    resolution: "accept_learned" | "keep_static" | "merge"
    """
    valid = {"accept_learned", "keep_static", "merge"}
    if resolution not in valid:
        return json.dumps({"error": f"resolution must be one of {sorted(valid)}"})

    try:
        import sedi.local_store as _local_store
        _local_store.init_store()
        kb_path = _local_store.STORE_ROOT / "knowledge" / f"{sector}__{niche}.json"
        if not kb_path.exists():
            return json.dumps({"error": "niche not found in knowledge base"})

        data = json.loads(kb_path.read_text())
        data["suspicion_flag"] = False
        data["suspicion_resolved_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()

        if resolution == "accept_learned":
            data["source"] = "learned+validated"
        elif resolution == "keep_static":
            data["source"] = "static"

        kb_path.write_text(json.dumps(data, indent=2))

        try:
            from sedi.evolution import log_evolution_event
            log_evolution_event("suspicion_resolved", {
                "sector": sector, "niche": niche, "resolution": resolution
            })
        except Exception:
            pass

        return json.dumps({
            "status": "ok",
            "sector": sector,
            "niche": niche,
            "resolution": resolution,
            "suspicion_flag": False,
            "source": data["source"],
        })
    except Exception as exc:
        return json.dumps({"error": str(exc)})


def reset_weights_tool(sector: str = None) -> str:
    """Reset pattern weights to 1.0 for a sector or globally."""
    try:
        from sedi.feedback_engine import reset_weights as _fw_reset
        return _fw_reset(sector=sector)
    except Exception as exc:
        return json.dumps({"error": str(exc)})


def _now() -> str:
    return datetime.datetime.utcnow().isoformat() + "Z"
