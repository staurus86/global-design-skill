# sedi/cognition.py
from __future__ import annotations
from enum import Enum
from typing import Any
from sedi.perception import RequestAnalysis

BLUEPRINT_MAP = {
    "create":  "blueprints/landing-page-from-scratch.md",
    "improve": "blueprints/redesign-existing-page.md",
    "audit":   "checklists/global-design-review.md",
    "learn":   "learning/knowledge_base.py",
    "compare": "checklists/global-design-review.md",
}

SECTOR_BLUEPRINT_OVERRIDE = {
    ("create", "tech-saas"):    "blueprints/saas-app-from-scratch.md",
    ("create", "government"):   "blueprints/website-from-scratch.md",
    ("create", "non-profit"):   "blueprints/website-from-scratch.md",
    ("audit",  "tech-saas"):    "checklists/ui-review.md",
}


class ConflictPriority(Enum):
    USER_OVERRIDE = 1
    LEARNED       = 2
    STATIC        = 3
    GENERIC       = 4


def select_blueprint(analysis: RequestAnalysis) -> str:
    override_key = (analysis.intent, analysis.sector)
    if override_key in SECTOR_BLUEPRINT_OVERRIDE:
        return SECTOR_BLUEPRINT_OVERRIDE[override_key]
    return BLUEPRINT_MAP.get(analysis.intent, BLUEPRINT_MAP["create"])


def resolve_knowledge(
    analysis: RequestAnalysis,
    static_rules: dict[str, Any] | None,
    learned_rules: dict[str, Any] | None,
    user_override: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Conflict Resolver — returns rules with their source priority.
    Priority: user_override > learned (validated) > static > generic fallback.
    """
    if user_override:
        return {
            "rules": user_override,
            "source": "user_override",
            "priority": ConflictPriority.USER_OVERRIDE,
        }

    if (learned_rules
            and learned_rules.get("success_rate", 0) > 0.6
            and not learned_rules.get("suspicion_flag", False)):
        return {
            "rules": learned_rules,
            "source": "learned",
            "priority": ConflictPriority.LEARNED,
        }

    if static_rules:
        return {
            "rules": static_rules,
            "source": "static",
            "priority": ConflictPriority.STATIC,
        }

    return {
        "rules": {},
        "source": "generic",
        "priority": ConflictPriority.GENERIC,
    }
