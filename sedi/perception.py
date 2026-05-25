# sedi/perception.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
import re

Intent = Literal["create", "improve", "audit", "learn", "compare"]

_INTENT_KEYWORDS: dict[str, list[str]] = {
    "create":  ["design", "create", "build", "make", "scaffold", "write"],
    "improve": ["improve", "redesign", "fix", "enhance", "update", "refactor"],
    "audit":   ["audit", "review", "check", "analyse", "analyze", "critique"],
    "learn":   ["learn", "train", "add reference", "scrape"],
    "compare": ["compare", "vs", "versus", "benchmark"],
}

_SECTOR_KEYWORDS: dict[str, list[str]] = {
    "b2b-products":  ["industrial", "b2b", "manufacturer", "procurement", "rfq", "logistics",
                      "equipment", "machinery", "wholesale", "supplier"],
    "b2c-products":  ["shop", "store", "ecommerce", "product", "bicycle", "furniture",
                      "electronics", "consumer", "retail", "buy"],
    "services":      ["service", "agency", "cleaning", "tarot", "fitness", "consulting",
                      "freelance", "booking", "appointment"],
    "content-media": ["blog", "podcast", "news", "magazine", "media", "content", "editorial",
                      "newsletter", "publication"],
    "education":     ["course", "academy", "training", "learning", "education", "school",
                      "university", "lms", "bootcamp"],
    "health":        ["clinic", "medical", "health", "doctor", "telemedicine", "wellness",
                      "hospital", "pharmacy", "mental health"],
    "finance":       ["bank", "finance", "fintech", "insurance", "crypto", "investment",
                      "payment", "wallet", "trading"],
    "real-estate":   ["real estate", "property", "apartment", "housing", "rental", "mortgage",
                      "realty", "agent"],
    "travel":        ["hotel", "travel", "tour", "restaurant", "hospitality", "booking",
                      "flight", "airbnb", "vacation"],
    "tech-saas":     ["saas", "startup", "developer", "software", "api", "dashboard",
                      "platform", "tool", "app", "b2b software"],
    "non-profit":    ["nonprofit", "non-profit", "ngo", "charity", "foundation", "donation",
                      "volunteer"],
    "government":    ["government", "civic", "portal", "e-gov", "public service", "municipality",
                      "citizen", "ministry"],
    "entertainment": ["game", "gaming", "streaming", "concert", "event", "sports", "music",
                      "entertainment", "festival", "esports"],
}

_SUB_NICHE_KEYWORDS: dict[str, list[str]] = {
    "casual-games": ["casual", "mobile game", "hyper-casual", "puzzle", "idle"],
    "aaa-games":    ["aaa", "triple-a", "console", "shooter", "rpg", "mmorpg"],
    "streaming":    ["streaming", "subscription video", "vod", "watch", "series", "film"],
    "live-events":  ["concert", "festival", "live event", "ticket", "venue", "sports event"],
}

_EMOTION_KEYWORDS = {
    "urgent":     ["urgent", "asap", "deadline", "quickly", "fast", "immediately"],
    "frustrated": ["broken", "terrible", "bad", "wrong", "frustrating", "ugly"],
    "confused":   ["not sure", "don't know", "unclear", "confused", "maybe", "?"],
}

_CONSTRAINT_KEYWORDS = {
    "budget":    ["budget", "cheap", "affordable", "low cost", "expensive"],
    "timeline":  ["deadline", "by", "launch", "sprint", "week"],
    "tech_stack": ["react", "vue", "angular", "next.js", "nuxt", "tailwind", "wordpress",
                   "webflow", "framer"],
}


@dataclass
class RequestAnalysis:
    intent: str
    sector: str
    niche: str
    sub_niche: str | None
    context: dict = field(default_factory=dict)
    emotions: dict = field(default_factory=dict)
    constraints: dict = field(default_factory=dict)


def _detect_intent(text: str) -> str:
    lower = text.lower()
    scores: dict[str, int] = {k: 0 for k in _INTENT_KEYWORDS}
    for intent, keywords in _INTENT_KEYWORDS.items():
        for kw in keywords:
            if kw in lower:
                scores[intent] += 1
    best = max(scores, key=lambda k: scores[k])
    return best if scores[best] > 0 else "create"


def _detect_sector(text: str) -> tuple[str, float]:
    lower = text.lower()
    scores: dict[str, int] = {s: 0 for s in _SECTOR_KEYWORDS}
    for sector, keywords in _SECTOR_KEYWORDS.items():
        for kw in keywords:
            if kw in lower:
                scores[sector] += 1
    best = max(scores, key=lambda k: scores[k])
    total_hits = sum(scores.values())
    if scores[best] == 0:
        return "unknown", 0.0
    confidence = min(scores[best] / max(total_hits, 1) + 0.3, 1.0)
    return best, confidence


def _detect_sub_niche(text: str, sector: str) -> str | None:
    if sector != "entertainment":
        return None
    lower = text.lower()
    for sub, keywords in _SUB_NICHE_KEYWORDS.items():
        for kw in keywords:
            if kw in lower:
                return sub
    return None


def _detect_emotions(text: str) -> dict:
    lower = text.lower()
    return {k: any(kw in lower for kw in words)
            for k, words in _EMOTION_KEYWORDS.items()}


def _detect_constraints(text: str) -> dict:
    lower = text.lower()
    result = {}
    for key, keywords in _CONSTRAINT_KEYWORDS.items():
        for kw in keywords:
            if kw in lower:
                result[key] = kw
                break
    return result


def analyse_request(text: str) -> RequestAnalysis:
    intent = _detect_intent(text)
    sector, confidence = _detect_sector(text)
    if confidence < 0.5:
        sector = "unknown"
    sub_niche = _detect_sub_niche(text, sector)
    niche = sector
    return RequestAnalysis(
        intent=intent,
        sector=sector,
        niche=niche,
        sub_niche=sub_niche,
        context={"confidence": confidence},
        emotions=_detect_emotions(text),
        constraints=_detect_constraints(text),
    )
