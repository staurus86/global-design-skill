# mcp-server/tools/sector_context.py
"""Tools for sector classification and context retrieval."""
import json
import re
from pathlib import Path

INDUSTRIES_DIR = Path(__file__).parent.parent.parent / "industries"

SECTOR_KEYWORDS: dict[str, list[str]] = {
    "b2b-products": [
        "manufacturer", "manufacturing", "industrial", "equipment", "machinery",
        "factory", "supplier", "wholesale", "oem", "b2b", "насос", "pump",
        "станок", "завод", "поставщик", "производитель", "оборудование",
        "cnc", "чпу", "логистика", "logistics", "consulting", "консалтинг",
    ],
    "b2c-products": [
        "shop", "store", "buy", "cart", "product", "retail", "ecommerce",
        "fashion", "electronics", "furniture", "bicycle", "велосипед",
        "магазин", "интернет-магазин", "купить", "электроника", "мебель",
    ],
    "services": [
        "booking", "appointment",
        "therapy", "coaching", "treatment", "session", "таролог", "tarot",
        "тренер", "trainer", "клининг", "cleaning", "фитнес", "fitness",
        "юридический", "legal", "психолог", "therapist",
    ],
    "content-media": [
        "blog", "news", "magazine", "podcast", "media", "article", "story",
        "journal", "publication", "новости", "блог", "журнал", "портал",
        "редакция", "editorial",
    ],
    "education": [
        "course", "learn", "training", "academy", "school", "university",
        "education", "certification", "degree", "курс", "обучение",
        "академия", "университет", "bootcamp", "дистанционное",
    ],
    "health": [
        "clinic", "hospital", "medical", "health", "wellness", "doctor",
        "care", "клиника", "больница", "медицин",
        "стоматолог", "dental", "врач", "здоровье",
    ],
    "finance": [
        "bank", "invest", "finance", "insurance", "crypto", "payment",
        "fintech", "trading", "wealth", "банк", "инвестиц", "страховая",
        "финансов", "платеж", "кредит", "осаго", "policy",
        "страховани", "comparison",
    ],
    "real-estate": [
        "property", "real estate", "rent", "apartment", "house", "mortgage",
        "realty", "недвижимость", "квартира",
        "аренда", "застройщик", "новостройка", "агентство недвижимости",
        "продажа квартир", "квартир",
    ],
    "travel": [
        "hotel", "tour", "travel", "flight", "vacation", "restaurant",
        "destination", "trip", "отель", "ресторан", "туризм",
        "путешествие", "доставка еды", "food delivery",
        "boutique hotel", "resort",
    ],
    "tech-saas": [
        "saas", "software", "platform", "ai", "startup", "tech",
        "api", "cloud", "разработчик", "приложение",
        "платформа", "аналитика", "analytics", "инструмент",
    ],
    "non-profit": [
        "charity", "nonprofit", "ngo", "foundation", "donate", "volunteer",
        "cause", "mission", "благотворительн", "фонд", "нко",
        "экологическ", "environmental",
    ],
    "government": [
        "government", "civic", "municipal", "portal", "citizen", "public",
        "госуслуг", "государственн", "муниципальн", "администрация",
        "министерство",
    ],
    "entertainment": [
        "game", "gaming", "music", "movie", "stream", "streaming", "event",
        "ticket", "concert", "festival", "show", "игра", "стриминг",
        "кино", "музыка", "казуальн", "casual", "aaa", "shooter",
        "видеоигр",
    ],
}

# Pairs (query_substr, required_sector) — if query matches, force the sector
# regardless of keyword scores. Listed from most specific to least.
_FORCED_RULES: list[tuple[str, str]] = [
    ("агентство недвижимости", "real-estate"),
    ("продажа квартир", "real-estate"),
    ("new apartment sales", "real-estate"),
    ("благотворительный фонд", "non-profit"),
    ("children's charity", "non-profit"),
    ("government citizen", "government"),
    ("государственный портал госуслуг", "government"),
    ("municipal government", "government"),
    ("муниципальный сайт", "government"),
    ("стриминговый сервис", "entertainment"),
    ("streaming video service", "entertainment"),
    ("мобильная игра", "entertainment"),
    ("casual mobile game", "entertainment"),
    ("aaa видеоигра", "entertainment"),
    ("aaa game", "entertainment"),
    ("инвестиционная платформа", "finance"),
    ("investment platform", "finance"),
    ("car insurance", "finance"),
    ("страховая компания", "finance"),
    ("analytics saas", "tech-saas"),
    ("saas", "tech-saas"),
    ("api инструмент", "tech-saas"),
    ("developer api", "tech-saas"),
]


def classify_niche(query: str) -> str:
    """Classify a user query into a sector.

    Returns JSON string: {"sector": str, "confidence": float, "alternatives": list}
    """
    q = query.lower()

    # Check forced rules first (most specific patterns win)
    for pattern, forced_sector in _FORCED_RULES:
        if pattern.lower() in q:
            return json.dumps({
                "sector": forced_sector,
                "confidence": 0.9,
                "alternatives": [],
            })

    scores: dict[str, float] = {}

    for sector, keywords in SECTOR_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw.lower() in q)
        if score > 0:
            scores[sector] = score

    if not scores:
        return json.dumps({"sector": "unknown", "confidence": 0.0, "alternatives": []})

    total = sum(scores.values())
    sorted_sectors = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    top_sector, top_score = sorted_sectors[0]
    # Base confidence: share of total hits
    confidence = top_score / max(total, 1)
    # Boost if top sector has a clear lead over second
    if len(sorted_sectors) > 1:
        second_score = sorted_sectors[1][1]
        if top_score >= second_score * 2:
            confidence = min(confidence * 1.4, 1.0)
    else:
        confidence = min(confidence * 1.4, 1.0)

    confidence = round(confidence, 2)

    alternatives = [
        {"sector": s, "score": sc}
        for s, sc in sorted_sectors[1:4]
    ]

    return json.dumps({
        "sector": top_sector,
        "confidence": confidence,
        "alternatives": alternatives,
    })


def list_sectors() -> str:
    """Return all available sectors with descriptions.

    Returns JSON string: list of {"sector": str, "description": str, "examples": list}
    """
    index_file = INDUSTRIES_DIR / "_index.md"
    if not index_file.exists():
        return json.dumps({"error": "industries/_index.md not found"})

    sectors = []
    for path in sorted(INDUSTRIES_DIR.glob("*.md")):
        if path.name == "_index.md":
            continue
        sector_id = path.stem
        text = path.read_text(encoding="utf-8").replace('\r\n', '\n')

        # Extract description from Sector Profile section
        profile_match = re.search(
            r"## Sector Profile\n(.*?)(?=\n##|\Z)", text, re.DOTALL
        )
        description = ""
        if profile_match:
            first_line = profile_match.group(1).strip().split("\n")[0]
            description = re.sub(r"^\s*-\s*\*\*.*?\*\*:\s*", "", first_line).strip()

        sectors.append({
            "sector": sector_id,
            "file": path.name,
            "description": description,
            "examples": [],
        })

    return json.dumps(sectors)


def get_sector_context(sector: str, niche: str | None = None) -> str:
    """Return full design context for a sector.

    Returns JSON string with all sections from the industries/*.md file.
    """
    sector_file = INDUSTRIES_DIR / f"{sector}.md"
    if not sector_file.exists():
        available = [p.stem for p in INDUSTRIES_DIR.glob("*.md") if p.stem != "_index"]
        return json.dumps({
            "error": f"Sector '{sector}' not found",
            "available_sectors": available,
        })

    text = sector_file.read_text(encoding="utf-8").replace('\r\n', '\n')

    # Parse frontmatter
    fm_match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    frontmatter = {}
    if fm_match:
        import datetime
        import yaml
        raw_fm = yaml.safe_load(fm_match.group(1)) or {}
        # Convert non-JSON-serializable types (e.g. date) to strings
        frontmatter = {
            k: v.isoformat() if isinstance(v, (datetime.date, datetime.datetime)) else v
            for k, v in raw_fm.items()
        }

    # Extract each section
    sections: dict[str, str] = {}
    section_pattern = re.compile(r"^## (.+?)$", re.MULTILINE)
    matches = list(section_pattern.finditer(text))

    for i, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        content = text[start:end].strip()
        sections[title] = content

    return json.dumps({
        "sector": sector,
        "niche": niche,
        "frontmatter": frontmatter,
        "sections": sections,
    })
