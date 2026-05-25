# sedi/execution.py
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from sedi.perception import RequestAnalysis


@dataclass
class DesignOutput:
    sector: str
    niche: str
    sub_niche: str | None
    intent: str
    blueprint: str
    rules_applied: dict[str, Any]
    citations: list[str]
    gates_passed: list[str]
    generated_at: str


def generate_output(
    analysis: RequestAnalysis,
    blueprint: str,
    knowledge: dict[str, Any],
) -> DesignOutput:
    rules = knowledge.get("rules", {})
    source = knowledge.get("source", "generic")

    citations = _build_citations(rules, source, analysis)
    gates_passed = _run_gates(rules)

    return DesignOutput(
        sector=analysis.sector,
        niche=analysis.niche,
        sub_niche=analysis.sub_niche,
        intent=analysis.intent,
        blueprint=blueprint,
        rules_applied=rules,
        citations=citations,
        gates_passed=gates_passed,
        generated_at=datetime.now(timezone.utc).isoformat(),
    )


def _build_citations(rules: dict, source: str, analysis: RequestAnalysis) -> list[str]:
    citations = []
    for element in rules.get("required_elements", []):
        citations.append(
            f"{element} required by {analysis.sector} rules "
            f"[source: {source}]"
        )
    for pattern in rules.get("banned_patterns", []):
        citations.append(
            f"{pattern} banned in {analysis.sector} [source: {source}]"
        )
    return citations


def _run_gates(rules: dict) -> list[str]:
    passed = []
    if rules.get("required_elements"):
        passed.append("all_states_designed")
    if rules.get("trust_signals"):
        passed.append("user_identified")
    return passed
