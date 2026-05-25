# mcp-server/tools/design_audit.py
"""Quick diagnosis tool — maps 5 answers to a sector pattern."""
import json

DIAGNOSIS_MATRIX = {
    # (who_pays, decision_type, risk_level) -> sector
    ("business", "rational", "high"):    "b2b-products",
    ("business", "technical", "high"):   "b2b-products",
    ("business", "technical", "medium"): "tech-saas",
    ("consumer", "comparison", "medium"): "b2c-products",
    ("consumer", "impulse", "low"):      "b2c-products",
    ("consumer", "emotional", "medium"): "services",
    ("consumer", "trust", "medium"):     "services",
    ("consumer", "trust", "high"):       "health",
    ("consumer", "habitual", "low"):     "content-media",
    ("consumer", "investment", "high"):  "education",
    ("consumer", "cautious", "high"):    "finance",
    ("consumer", "rational", "high"):    "real-estate",
    ("consumer", "emotional", "medium", "travel"): "travel",
    ("donor", "values", "low"):          "non-profit",
    ("citizen", "task", "low"):          "government",
    ("citizen", "task", "high"):         "government",
    ("consumer", "impulse", "low", "fun"): "entertainment",
}

RATIONALE_MAP = {
    "b2b-products":  "Rational multi-stakeholder purchase with high financial risk — requires specs, certifications, and RFQ.",
    "b2c-products":  "Consumer product purchase driven by comparison and social validation.",
    "services":      "Trust-based personal service — story, testimonials, and booking are critical.",
    "content-media": "Attention-based with low barrier to entry — hierarchy and subscribe CTAs matter most.",
    "education":     "High-risk investment in skills — curriculum, outcomes, and instructor credentials drive conversion.",
    "health":        "Very high risk — trust and credentials must come first, booking second.",
    "finance":       "Very high risk with regulatory context — security and fee transparency are mandatory.",
    "real-estate":   "Largest purchase decision — gallery, location, and price transparency are essential.",
    "travel":        "Emotional desire + practical validation — visuals and real-time availability drive conversion.",
    "tech-saas":     "Technical validation cycle — demo, docs, and integration list required.",
    "non-profit":    "Mission alignment + financial transparency — impact metrics and trust signals first.",
    "government":    "Task completion, not persuasion — plain language, clear process, accessibility mandatory.",
    "entertainment": "Emotion + FOMO — immersive visuals and friction-free purchase flow.",
}


def get_quick_diagnosis(
    who_pays: str,
    decision_type: str,
    risk_level: str,
    choice_type: str,
    user_value: str,
) -> str:
    """Map 5 diagnostic answers to a recommended sector pattern.

    Args:
        who_pays:      "business" | "consumer" | "donor" | "citizen"
        decision_type: "rational" | "emotional" | "trust" | "impulse" |
                       "comparison" | "technical" | "investment" |
                       "cautious" | "habitual" | "values" | "task"
        risk_level:    "low" | "medium" | "high"
        choice_type:   context hint ("travel", "fun", etc.) or "general"
        user_value:    "save-money" | "save-time" | "reduce-risk" |
                       "gain-status" | "learn" | "enjoy" | "complete-task"

    Returns JSON string: {"sector": str, "pattern": str, "rationale": str}
    """
    # Try exact match with hint
    key = (who_pays.lower(), decision_type.lower(), risk_level.lower())
    key_with_hint = key + (choice_type.lower(),)

    sector = DIAGNOSIS_MATRIX.get(key_with_hint) or DIAGNOSIS_MATRIX.get(key)

    # Fallback heuristics
    if not sector:
        if who_pays == "citizen":
            sector = "government"
        elif who_pays == "donor":
            sector = "non-profit"
        elif risk_level == "high" and decision_type == "emotional":
            sector = "real-estate"
        elif user_value == "enjoy":
            sector = "entertainment"
        elif user_value == "learn":
            sector = "education"
        else:
            sector = "tech-saas"  # generic modern product default

    return json.dumps({
        "sector": sector,
        "pattern": f"industries/{sector}.md",
        "rationale": RATIONALE_MAP.get(sector, "Apply generic design rules."),
    })
