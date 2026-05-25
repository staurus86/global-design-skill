---
applyTo: "mcp-server/**/*.py"
---

# MCP Server Rules

- Never write to stdout — use `logging.error()` / `logging.warning()` with `stream=sys.stderr`
- All `@mcp.tool()` functions must be inside `main()` after `FASTMCP_AVAILABLE` check
- Tool naming: `<action>_tool` suffix, returns `str` (JSON)
- After adding a tool, add a test in `mcp-server/tests/`
- `mcp.run(transport="stdio")` — always specify transport explicitly
- Import learning/SEDI functions inline inside `main()` to avoid circular import issues
