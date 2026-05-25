# AGENTS.md — Global Design Skill

Guidelines for AI agents (Codex, Copilot, Claude, Cursor, Gemini) contributing to this repository.

## What this repository is

A self-learning design system for AI-assisted frontend work. It contains:
- Design rules (`rules/`, `checklists/`, `quality-gates.md`)
- Build protocols (`blueprints/`)
- UI patterns (`patterns/`)
- Industry sector rules (`industries/`) — 13 sectors, niche auto-detected
- Python MCP server (`mcp-server/`) — 11 tools for sector context, pattern learning, SEDI
- Learning engine (`learning/`) — scrapes reference sites, builds local KB
- SEDI architecture (`sedi/`) — self-evolving design intelligence (6 layers)

## Development rules

**Never:**
- Delete files without explicit instruction
- Write to stdout in `mcp-server/` (use `sys.stderr` or `logging` — stdout breaks STDIO MCP transport)
- Use `from sedi.local_store import STORE_ROOT` — always `import sedi.local_store as _local_store` to keep mock patching working
- Add `@mcp.tool()` without a corresponding test in `mcp-server/tests/`
- Introduce CRLF line endings — all files must use LF

**Always:**
- Run `pytest` after any Python change
- Run `python scripts/validate-industries.py` after any `industries/*.md` change
- Keep `CHANGELOG.md` up to date
- Use `utcnow()` (not timezone-aware `datetime.now(UTC)`) in SEDI/learning modules — both sides of comparisons must match

## Industry files (`industries/*.md`)

Each file requires this frontmatter:
```yaml
---
version: 1.0.0
last_updated: YYYY-MM-DD
source: manual
stale_after_days: 90
---
```

Required sections (9): Sector Profile, Mobile Rules, Required Elements, Banned Patterns, Trust Signals, Conversion Path, Page Structure, Quick Diagnosis, Disambiguation.

## MCP server (`mcp-server/`)

- Entry point: `server.py` → `main()` → `mcp.run(transport="stdio")`
- Add tools inside the `if FASTMCP_AVAILABLE:` block only
- Tool naming convention: `<action>_tool` (e.g. `classify_niche_tool`)
- All tools return `str` (JSON serialized)
- Log with `logging.error()` / `logging.warning()` to stderr, never `print()`

## SEDI modules (`sedi/`)

- `STORE_ROOT` lives in `sedi/local_store.py` — import the module, not the constant
- `ConflictPriority` order: `USER_OVERRIDE=1 > LEARNED=2 > STATIC=3 > GENERIC=4`
- Learned rules are only trusted when `success_rate > 0.6 AND suspicion_flag == False`
- Pattern weights are bounded `[0.1, 2.0]`, updated ±10% per interaction

## Tests

| Scope | Command |
|---|---|
| MCP server | `cd mcp-server && python -m pytest tests/ -q` |
| Learning modules | `python -m pytest tests/learning/ -q` |
| SEDI | `python -m pytest sedi/tests/ -q` |
| All | `python -m pytest mcp-server/tests/ sedi/tests/ tests/learning/ -q` |

105 tests must pass before any commit to `master`.
