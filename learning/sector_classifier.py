# learning/sector_classifier.py
"""Keyword-weighted sector classification for niche detection."""

SECTOR_KEYWORDS: dict[str, list[str]] = {
    "b2b-products": [
        "manufacturer", "manufacturing", "industrial", "equipment", "machinery",
        "factory", "supplier", "wholesale", "oem", "b2b", "насос", "pump",
        "станок", "завод", "поставщик", "производитель", "оборудование",
        "cnc", "логистика", "logistics", "consulting", "rfq",
    ],
    "b2c-products": [
        "shop", "store", "buy", "cart", "retail", "ecommerce", "product",
        "fashion", "electronics", "furniture", "bicycle", "велосипед",
        "магазин", "интернет-магазин", "купить", "электроника", "мебель",
    ],
    "services": [
        "booking", "appointment", "therapy", "coaching", "session", "tarot",
        "таролог", "тренер", "trainer", "клининг", "cleaning", "fitness",
        "legal", "юридический", "психолог", "service provider",
    ],
    "content-media": [
        "blog", "news", "magazine", "podcast", "media", "article",
        "новости", "блог", "журнал", "портал", "editorial", "publication",
    ],
    "education": [
        "course", "learn", "training", "academy", "school", "university",
        "certification", "курс", "обучение", "академия", "bootcamp",
        "curriculum", "lesson", "syllabus",
    ],
    "health": [
        "clinic", "hospital", "medical", "doctor", "dental", "wellness",
        "клиника", "стоматолог", "врач", "медицин", "therapy", "healthcare",
    ],
    "finance": [
        "bank", "invest", "insurance", "crypto", "payment", "fintech",
        "банк", "инвестиц", "страховая", "финансов", "кредит",
    ],
    "real-estate": [
        "property", "real estate", "apartment", "house", "mortgage",
        "недвижимость", "квартира", "аренда", "застройщик", "новостройка",
    ],
    "travel": [
        "hotel", "tour", "restaurant", "vacation", "booking", "trip",
        "отель", "ресторан", "туризм", "путешествие", "food delivery",
    ],
    "tech-saas": [
        "saas", "software", "platform", "api", "cloud", "developer",
        "разработчик", "платформа", "аналитика", "analytics", "startup",
    ],
    "non-profit": [
        "charity", "nonprofit", "ngo", "foundation", "donate", "volunteer",
        "благотворительн", "фонд", "НКО", "ecological", "environmental",
    ],
    "government": [
        "government", "municipal", "portal", "citizen", "public service",
        "госуслуг", "государственн", "муниципальн", "администрация",
    ],
    "entertainment": [
        "game", "gaming", "stream", "streaming", "event", "concert",
        "игра", "стриминг", "кино", "музыка", "casual", "aaa", "esports",
    ],
}

SUB_NICHE_KEYWORDS: dict[str, dict[str, list[str]]] = {
    "entertainment": {
        "casual-games": ["casual", "mobile game", "hyper-casual", "казуальн"],
        "aaa-games": ["aaa", "console", "fps", "rpg", "шутер", "open world"],
        "streaming": ["stream", "subscription", "series", "стриминг", "подписка"],
        "live-events": ["concert", "festival", "ticket", "концерт", "фестиваль"],
    }
}


def classify_sector(query: str) -> dict:
    """Classify a query string into a sector.

    Returns dict: {sector, confidence, sub_niche, alternatives}
    """
    q = query.lower()
    scores: dict[str, float] = {}

    for sector, keywords in SECTOR_KEYWORDS.items():
        score = sum(1.0 for kw in keywords if kw.lower() in q)
        if score > 0:
            scores[sector] = score

    if not scores:
        return {"sector": "unknown", "confidence": 0.0, "sub_niche": None, "alternatives": []}

    total = sum(scores.values())
    sorted_sectors = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_sector, top_score = sorted_sectors[0]

    confidence = round(top_score / max(total, top_score + 1), 2)
    if len(sorted_sectors) > 1 and top_score >= sorted_sectors[1][1] * 2:
        confidence = min(round(confidence * 1.2, 2), 1.0)

    sub_niche = None
    if top_sector in SUB_NICHE_KEYWORDS:
        for sn, sn_keywords in SUB_NICHE_KEYWORDS[top_sector].items():
            if any(kw.lower() in q for kw in sn_keywords):
                sub_niche = sn
                break

    alternatives = [
        {"sector": s, "score": sc}
        for s, sc in sorted_sectors[1:4]
    ]

    return {
        "sector": top_sector,
        "confidence": confidence,
        "sub_niche": sub_niche,
        "alternatives": alternatives,
    }
