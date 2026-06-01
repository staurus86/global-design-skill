# CLAUDE.md — Global Design Skill

Instructions for Claude Code when working in this repository.

## What to use this skill for

Use `global-design-skill` when the task involves:
- designing, redesigning, improving, or auditing UI/UX
- frontend handoff specs, component specs, landing pages, SaaS UI, dashboards, admin panels
- design quality review, visual hierarchy, typography, color, motion, accessibility, conversion, responsive behavior
- generating sector-specific design rules (use MCP `get_sector_context`)

Do **not** use for pure backend, SQL, server config, data analysis — unless UI/UX output is requested.

## Task routing

| Task | Resource |
|---|---|
| CSS framework detection (run first) | `rules/18-css-framework-selection.md` |
| Interpret user request depth first | `rules/00-escalation-protocol.md` |
| Landing page from scratch | `blueprints/landing-page-from-scratch.md` |
| Existing page redesign | `blueprints/redesign-existing-page.md` |
| Full UI audit | `checklists/global-design-review.md` |
| Developer handoff | `templates/specs/frontend-tz.md` |
| Accessibility review | `agents/accessibility-auditor.md` + `rules/07-accessibility.md` |
| Contrast audit / fix (text, blocks, sections, dark mode) | `rules/19-contrast-standards.md` |
| Anti-slop audit / "looks AI-generated" | `references/anti-slop-system.md` |
| Animation (scroll, transitions, stagger) | `rules/17-motion-react.md` |
| Ready-made React components | `integrations/21st-dev/guide.md` |
| HTML design → MP4 video (product demo, social, changelog) | `integrations/hyperframes/guide.md` |
| Industry-specific rules | `GlobalDesignSkill:get_sector_context` (MCP tool) |
| Unknown niche | `GlobalDesignSkill:learn_from_reference` (MCP tool) |

## Key constraints

- Always clear all 8 quality gates before declaring handoff-ready (`skills/global-design/quality-gates.md`)
- Use OKLCH for all colors — never raw hex or `rgb()`
- Banned patterns list: `checklists/global-design-review.md` → "Banned Patterns"
- Design for 390px / 768px / 1280px breakpoints minimum

## Development rules (when editing this repo)

- **Never** write to stdout in `mcp-server/` — use `logging` to stderr
- **Always** `import sedi.local_store as _local_store` (not `from sedi.local_store import STORE_ROOT`)
- Run `python scripts/validate-industries.py` after editing `industries/*.md`
- Run tests: `cd mcp-server && python -m pytest tests/ -q`
- All files must use LF line endings

## MCP server setup

```bash
cd mcp-server
pip install -e ".[test]"
python server.py
```

Add to `.mcp.json` at the project root (Claude Code does not read `.claude/mcp.json`):
```json
{
  "mcpServers": {
    "GlobalDesignSkill": {
      "command": "python",
      "args": ["/path/to/global-design-skill/mcp-server/server.py"]
    }
  }
}
```
