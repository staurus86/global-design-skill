# mcp-server/server.py
"""Global Design Skill MCP Server — entry point."""

import logging
import os
import sys
from pathlib import Path

logging.basicConfig(stream=sys.stderr, level=logging.WARNING)

_REPO_ROOT = Path(__file__).parent.parent
_SAFE_MODE = os.environ.get("GDS_MCP_SAFE_MODE", "").strip() not in ("", "0", "false", "no")

try:
    import fastmcp
    FASTMCP_AVAILABLE = True
except ImportError:
    FASTMCP_AVAILABLE = False

from tools.sector_context import classify_niche, get_sector_context, list_sectors
from tools.industry_rules import check_banned_patterns
from tools.design_audit import get_quick_diagnosis


def _read_repo_file(relative_path: str) -> str:
    p = _REPO_ROOT / relative_path
    if not p.exists():
        return f"# File not found\n\n`{relative_path}` does not exist in this installation."
    return p.read_text(encoding="utf-8").replace("\r\n", "\n")


def main():
    if not FASTMCP_AVAILABLE:
        logging.error(
            "fastmcp not installed. Run: pip install 'fastmcp>=0.1'\n"
            "Falling back to plain function mode — tools are importable directly."
        )
        return

    if _SAFE_MODE:
        logging.warning("GDS_MCP_SAFE_MODE=1 — learning and SEDI tools are disabled.")

    mcp = fastmcp.FastMCP("Global Design Skill")

    # ─── Tools: Static (always available) ────────────────────────────────────

    @mcp.tool()
    def classify_niche_tool(query: str) -> str:
        """Classify a user query into a design sector.
        Returns JSON: {"sector": str, "confidence": float, "alternatives": list}
        """
        return classify_niche(query)

    @mcp.tool()
    def list_sectors_tool() -> str:
        """List all 13 available sectors with descriptions.
        Returns JSON: list of {"sector": str, "description": str}
        """
        return list_sectors()

    @mcp.tool()
    def get_sector_context_tool(sector: str, niche: str | None = None) -> str:
        """Get full design context (required elements, banned patterns, trust signals)
        for a specific sector from industries/*.md.
        Returns JSON: {sector, frontmatter, sections}
        """
        return get_sector_context(sector, niche)

    @mcp.tool()
    def check_banned_patterns_tool(sector: str, content: str) -> str:
        """Check a plain-text design description for sector-specific banned patterns.
        content: plain text description (not HTML)
        Returns JSON: {"violations": list, "warnings": list}
        """
        return check_banned_patterns(sector, content)

    @mcp.tool()
    def get_quick_diagnosis_tool(
        who_pays: str,
        decision_type: str,
        risk_level: str,
        choice_type: str = "general",
        user_value: str = "general",
    ) -> str:
        """Map 5 diagnostic answers to a recommended design sector.
        who_pays: business | consumer | donor | citizen
        decision_type: rational | emotional | trust | impulse | technical
        risk_level: low | medium | high
        Returns JSON: {"sector": str, "pattern": str, "rationale": str}
        """
        return get_quick_diagnosis(who_pays, decision_type, risk_level, choice_type, user_value)

    # ─── Tools: Learning + SEDI ───────────────────────────────────────────────

    _safe_err = '{"error": "Learning tools are disabled (GDS_MCP_SAFE_MODE=1). Only static tools are available."}'

    if not _SAFE_MODE:
        from tools.learning_tools import (
            learn_from_reference as _learn,
            get_or_learn_sector as _get_or_learn,
            list_learned_niches as _list_niches,
            forget_niche as _forget,
            resolve_suspicion as _resolve,
            reset_weights_tool as _reset_weights,
        )

        @mcp.tool()
        def learn_from_reference_tool(url: str, sector: str | None = None, niche: str | None = None) -> str:
            """Scrape a reference URL, extract design patterns, save to local knowledge base."""
            return _learn(url, sector, niche)

        @mcp.tool()
        def get_or_learn_sector_tool(sector: str, niche: str) -> str:
            """Get sector context from static files + local knowledge base combined."""
            return _get_or_learn(sector, niche)

        @mcp.tool()
        def list_learned_niches_tool() -> str:
            """List all niches in the local knowledge base (~/.global-design-skill/knowledge/)."""
            return _list_niches()

        @mcp.tool()
        def forget_niche_tool(sector: str, niche: str) -> str:
            """Delete a learned niche from the local knowledge base."""
            return _forget(sector, niche)

        @mcp.tool()
        def resolve_suspicion_tool(sector: str, niche: str, resolution: str) -> str:
            """Clear suspicion flag on a knowledge entry.
            resolution: accept_learned | keep_static | merge"""
            return _resolve(sector, niche, resolution)

        @mcp.tool()
        def reset_weights_tool(sector: str | None = None) -> str:
            """Reset pattern weights to 1.0 for a sector, or globally if sector omitted."""
            return _reset_weights(sector)

    else:
        # Safe-mode stubs — discoverable but return a clear error

        @mcp.tool()
        def learn_from_reference_tool(url: str, sector: str | None = None, niche: str | None = None) -> str:
            """[SAFE MODE] Scrape a reference URL (disabled — set GDS_MCP_SAFE_MODE=0 to enable)."""
            return _safe_err

        @mcp.tool()
        def get_or_learn_sector_tool(sector: str, niche: str) -> str:
            """[SAFE MODE] Get learned sector context (disabled)."""
            return _safe_err

        @mcp.tool()
        def list_learned_niches_tool() -> str:
            """[SAFE MODE] List learned niches (disabled)."""
            return _safe_err

        @mcp.tool()
        def forget_niche_tool(sector: str, niche: str) -> str:
            """[SAFE MODE] Delete learned niche (disabled)."""
            return _safe_err

        @mcp.tool()
        def resolve_suspicion_tool(sector: str, niche: str, resolution: str) -> str:
            """[SAFE MODE] Resolve suspicion flag (disabled)."""
            return _safe_err

        @mcp.tool()
        def reset_weights_tool(sector: str | None = None) -> str:
            """[SAFE MODE] Reset pattern weights (disabled)."""
            return _safe_err

    # ─── Resources ────────────────────────────────────────────────────────────

    @mcp.resource("gds://rules/{name}", mime_type="text/markdown")
    def get_rule_resource(name: str) -> str:
        """A design rule file by short name (without .md).
        Available: 00-escalation-protocol | 01-visual-hierarchy | 02-layout-and-grid |
        03-typography | 04-color | 05-animation | 06-components | 07-accessibility |
        08-performance | 09-responsive | 10-forms | 11-data-tables | 12-admin-panels |
        13-saas-products | 14-landing-pages | 15-iconography | 16-design-for-seo |
        17-motion-react | 18-css-framework-selection | 19-contrast-standards"""
        return _read_repo_file(f"rules/{name}.md")

    @mcp.resource("gds://industries/{sector}", mime_type="text/markdown")
    def get_industry_resource(sector: str) -> str:
        """Sector-specific design rules. sector: b2b-products | b2c-products | services |
        content-media | education | health | finance | real-estate | travel |
        tech-saas | non-profit | government | entertainment | _index"""
        return _read_repo_file(f"industries/{sector}.md")

    @mcp.resource("gds://blueprints/{name}", mime_type="text/markdown")
    def get_blueprint_resource(name: str) -> str:
        """Build-from-scratch protocol. name: landing-page-from-scratch |
        interactive-landing-page | saas-app-from-scratch | admin-panel-from-scratch |
        website-from-scratch | redesign-existing-page | pricing-page-from-scratch |
        portfolio-from-scratch | onboarding-flow-from-scratch"""
        return _read_repo_file(f"blueprints/{name}.md")

    @mcp.resource("gds://patterns/{category}/{name}", mime_type="text/markdown")
    def get_pattern_resource(category: str, name: str) -> str:
        """UI pattern file. category: marketing-blocks | product-ui | navigation |
        admin-ui | effects | states"""
        if category == "states":
            return _read_repo_file(f"patterns/states/{name}.md")
        return _read_repo_file(f"patterns/{category}/{name}.md")

    @mcp.resource("gds://tokens/css", mime_type="text/css")
    def get_tokens_css() -> str:
        """Design tokens — CSS custom properties, light mode. Import in your project."""
        return _read_repo_file("tokens/tokens.css")

    @mcp.resource("gds://tokens/css-dark", mime_type="text/css")
    def get_tokens_css_dark() -> str:
        """Design tokens — CSS custom properties, dark mode overrides."""
        return _read_repo_file("tokens/tokens-dark.css")

    @mcp.resource("gds://templates/frontend-tz", mime_type="text/markdown")
    def get_template_frontend_tz() -> str:
        """Gate 8 developer handoff specification template."""
        return _read_repo_file("templates/specs/frontend-tz.md")

    @mcp.resource("gds://templates/component-spec", mime_type="text/markdown")
    def get_template_component_spec() -> str:
        """Component API + states + ARIA specification template."""
        return _read_repo_file("templates/specs/component-spec.md")

    @mcp.resource("gds://checklists/global-design-review", mime_type="text/markdown")
    def get_checklist_global() -> str:
        """100+ checks, 11 sections, banned patterns. Full design review checklist."""
        return _read_repo_file("checklists/global-design-review.md")

    @mcp.resource("gds://checklists/landing-conversion-review", mime_type="text/markdown")
    def get_checklist_landing() -> str:
        """AIDA, CTA, social proof, friction, SEO checklist for landing pages."""
        return _read_repo_file("checklists/landing-conversion-review.md")

    @mcp.resource("gds://skills/global-design", mime_type="text/markdown")
    def get_skill_entry_point() -> str:
        """Main skill entry point — task routing, quality gates, output formats."""
        return _read_repo_file("skills/global-design/SKILL.md")

    # ─── Prompts ──────────────────────────────────────────────────────────────

    @mcp.prompt
    def audit_landing_page(url: str = "", context: str = "") -> str:
        """Full landing page design audit — top 10 problems, gate failures, quick wins."""
        target = f": {url}" if url else ""
        ctx_line = f"\nContext: {context}" if context else ""
        return (
            f"Use global-design-skill to audit this landing page{target}.{ctx_line}\n\n"
            "Apply the full review protocol from gds://checklists/global-design-review.\n\n"
            "Return:\n"
            "1. Top 10 design problems — each with severity (critical/major/minor) "
            "and an implementation-ready fix\n"
            "2. Quality gate compliance — which of the 8 gates fail and exactly why\n"
            "3. Banned patterns found (cite the rule source for each)\n"
            "4. Quick wins — 3 changes with the highest impact-to-effort ratio"
        )

    @mcp.prompt
    def redesign_hero(current_design: str = "", sector: str = "", metric: str = "") -> str:
        """Hero section redesign — flags the generic centered default, proposes a concrete layout."""
        sector_line = f"\nBusiness sector: {sector}" if sector else ""
        metric_line = f"\nPrimary metric to optimize: {metric}" if metric else ""
        design_line = f"\nCurrent design: {current_design}" if current_design else ""
        return (
            f"Use global-design-skill to redesign this hero section."
            f"{design_line}{sector_line}{metric_line}\n\n"
            "Rules:\n"
            "- Read gds://rules/14-landing-pages for hero patterns\n"
            "- Read gds://checklists/global-design-review → Banned Patterns section\n"
            "- If the current design uses centered H1 + subtitle + two equal buttons, "
            "flag it as a banned pattern before proposing alternatives\n\n"
            "Return:\n"
            "1. What is wrong with the current hero (cite the banned pattern name)\n"
            "2. Recommended layout (editorial split / asymmetric / product-first / "
            "command-line) — explain why this fits the sector\n"
            "3. Complete layout spec: grid columns, type scale using clamp(), "
            "CTA label formula (Verb + Object + Context), responsive behavior at 390px\n"
            "4. Implementation notes: CSS grid, token references, motion entrance"
        )

    @mcp.prompt
    def create_frontend_handoff(component: str = "", context: str = "") -> str:
        """Gate 8 frontend handoff spec — developer-ready with all states, tokens, and ARIA."""
        comp_line = f": {component}" if component else ""
        ctx_line = f"\nContext: {context}" if context else ""
        return (
            f"Use global-design-skill to write a Gate 8 frontend handoff spec for "
            f"this component{comp_line}.{ctx_line}\n\n"
            "Template: gds://templates/frontend-tz\n"
            "Component spec format: gds://templates/component-spec\n\n"
            "The spec must pass all 8 quality gates. Key gates:\n"
            "- Gate 4: All states (idle/hover/active/focus/disabled/loading/empty/error/success)\n"
            "- Gate 6: Every ARIA attribute on every interactive element\n"
            "- Gate 7: All sizes and colors as token references — no raw hex, no raw px\n"
            "- Gate 8: A developer can implement without asking a single follow-up question\n\n"
            "Return the complete spec in template format."
        )

    @mcp.prompt
    def improve_admin_table(context: str = "") -> str:
        """Admin data table improvement — density, states, keyboard, bulk actions, filters."""
        ctx_line = f"\nContext: {context}" if context else ""
        return (
            f"Use global-design-skill to improve this admin data table.{ctx_line}\n\n"
            "Read gds://patterns/admin-ui/data-tables for patterns.\n"
            "Read gds://rules/11-data-tables for density and hierarchy rules.\n\n"
            "Audit against:\n"
            "1. Density: row height appropriate for data volume?\n"
            "2. States: loading skeleton, empty state, error state, bulk-selected — all designed?\n"
            "3. Keyboard: Tab stops, sort by keyboard, row selection, bulk action shortcuts\n"
            "4. Filters: chips visible, active filters removable, filter count shown?\n"
            "5. Bulk actions: confirmation for destructive actions, "
            "progressive disclosure of secondary actions\n\n"
            "Return improvements with priority (P0/P1/P2) and implementation spec for each."
        )

    @mcp.prompt
    def sector_design_brief(
        product_description: str,
        target_user: str = "",
        primary_metric: str = "",
    ) -> str:
        """Auto-detect sector, return sector-specific brief with rules, banned patterns, and required elements."""
        user_line = f"\nTarget user: {target_user}" if target_user else ""
        metric_line = f"\nPrimary metric: {primary_metric}" if primary_metric else ""
        return (
            f"Use global-design-skill to generate a sector-specific design brief.\n\n"
            f"Product: {product_description}{user_line}{metric_line}\n\n"
            "Steps:\n"
            "1. Call classify_niche_tool with the product description to detect the sector\n"
            "2. Call get_sector_context_tool with the detected sector\n"
            "3. Call check_banned_patterns_tool with any design decisions already mentioned\n\n"
            "Return:\n"
            "1. Detected sector + confidence\n"
            "2. Required elements for this sector\n"
            "3. Banned patterns to avoid\n"
            "4. Trust signals required\n"
            "5. Primary conversion path\n"
            "6. Mobile-first considerations\n"
            "7. Quick diagnosis checklist"
        )

    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
