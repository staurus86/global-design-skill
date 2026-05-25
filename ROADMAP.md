# Roadmap

## Released

### v1.0.0 — Foundation (2026-05-20)
154 files (~59,000 lines). Core design rules, blueprints, patterns, tokens, 11 agents, templates, checklists, recipes, examples, integrations for 6 AI tools.

### v1.5.0 — Industry-Aware Design Intelligence / SEDI (2026-05-25)
+69 files (~18,000 lines). 13 industry sector files, MCP server with 11 tools, learning engine, full SEDI 6-layer architecture (Perception → Cognition → Execution → Feedback → Evolution → Local Store).

---

## Planned

### v1.6 — Infrastructure
- CI pipeline (line endings, syntax, test suite)
- Eval suite (trigger + output evals, golden outputs)
- `GDS_MCP_SAFE_MODE` flag for static-only operation
- MCP resources and prompts (in addition to tools)
- `gds doctor` — verifies install health

### v1.7 — Discovery & Onboarding
- Visual demo gallery (`docs/gallery/`) — before/after screenshots per task type
- One-step installer (`scripts/install.sh` + `gds` CLI)
- Compatibility matrix (expanded — per-feature per-tool)
- Figma token import/export pipeline

### v2.0 — Design Intelligence Platform
- Design benchmark viewer — compare outputs with/without skill
- Reference pattern scoring — rank learned niches by accuracy
- MCP registry packaging — installable via `mcp install global-design-skill`
- Multi-agent design pipeline — perception → cognition → execution as separate agents
- Industry sector auto-update — detect stale niches from reference drift

---

## Contributing to the roadmap

Open a GitHub issue with the label `roadmap` to suggest a feature or vote on priorities.
