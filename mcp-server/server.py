# mcp-server/server.py
"""Global Design Skill MCP Server — entry point."""

try:
    import fastmcp
    FASTMCP_AVAILABLE = True
except ImportError:
    FASTMCP_AVAILABLE = False

from tools.sector_context import classify_niche, get_sector_context, list_sectors
from tools.industry_rules import check_banned_patterns
from tools.design_audit import get_quick_diagnosis


def main():
    if not FASTMCP_AVAILABLE:
        print(
            "WARNING: fastmcp not installed. "
            "Run: pip install 'fastmcp>=0.1'\n"
            "Falling back to plain function mode — tools are importable directly."
        )
        return

    mcp = fastmcp.FastMCP("Global Design Skill")

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
    def get_sector_context_tool(sector: str, niche: str = None) -> str:
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
        decision_type: rational | emotional | trust | impulse | technical | ...
        risk_level: low | medium | high
        Returns JSON: {"sector": str, "pattern": str, "rationale": str}
        """
        return get_quick_diagnosis(who_pays, decision_type, risk_level, choice_type, user_value)

    mcp.run()


if __name__ == "__main__":
    main()
