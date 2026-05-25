# Global Design Skill — MCP Server

Gives AI assistants structured access to sector-specific design rules from
Global Design Skill. Classify a niche, get required elements, check for
banned patterns, run a quick diagnosis.

## Install

```bash
cd mcp-server
pip install -e .
```

## Tools

| Tool | Description |
|------|-------------|
| `classify_niche(query)` | Detect sector from free-text query. Returns JSON with sector + confidence. |
| `list_sectors()` | List all 13 sectors. |
| `get_sector_context(sector)` | Full context: required elements, banned patterns, trust signals. |
| `check_banned_patterns(sector, content)` | Check design description for violations. |
| `get_quick_diagnosis(who_pays, decision_type, risk_level, ...)` | 5-question sector diagnosis. |

## Setup in Claude Code

Add to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "global-design-skill": {
      "command": "python",
      "args": ["/absolute/path/to/global-design-skill/mcp-server/server.py"],
      "env": {}
    }
  }
}
```

## Setup in Cursor

Add to `.cursor/mcp.json` in your project root:

```json
{
  "mcpServers": {
    "global-design-skill": {
      "command": "python",
      "args": ["/absolute/path/to/global-design-skill/mcp-server/server.py"]
    }
  }
}
```

## Setup in Windsurf

Add to `.windsurf/mcp.json`:

```json
{
  "mcpServers": {
    "global-design-skill": {
      "command": "python",
      "args": ["/absolute/path/to/global-design-skill/mcp-server/server.py"]
    }
  }
}
```

## Privacy Note

This server reads local files only. No data is sent to external services.
The learning tools (Phase 3) make outgoing HTTP requests to reference sites —
those servers will see your requests in their access logs.
