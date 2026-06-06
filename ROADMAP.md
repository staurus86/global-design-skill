# Roadmap

## Released

### v1.0.0 — Foundation (2026-05-20)
154 files (~59,000 lines). Core design rules, blueprints, patterns, tokens, 11 agents, templates, checklists, recipes, examples, integrations for 6 AI tools.

### v1.5.0 — Industry-Aware Design Intelligence / SEDI (2026-05-25)
+69 files (~18,000 lines). 13 industry sector files, MCP server with 11 tools, learning engine, full SEDI 6-layer architecture (Perception → Cognition → Execution → Feedback → Evolution → Local Store).

### v2.0.0 — Stable milestone (2026-05-31)
236 files. Consolidation of the full 1.x line into a hardened design operating system. Folds in everything shipped through v1.6 (CI, eval suite, `GDS_MCP_SAFE_MODE`, MCP resources + prompts) and v1.7 (demo gallery, one-step installer + `gds` CLI, Figma token pipeline), plus the 1.8–1.9 design-system depth: 20 rules (contrast standards, motion/react, CSS framework selection, typographic punctuation), 44 patterns (incl. microinteractions), 26 references (incl. aesthetic recipes), behavioral-design biases, and real before/after case studies (bestseotools, sk-seo.ru, chexter.ru). Standards floor: CSS 2026 Baseline · React 19 · Next.js 15 · Tailwind v4 · WCAG 2.2 AA · OKLCH-only.

### v2.3.0 — Install hardening + verification depth (2026-06-06)
244 files. Post-2.0 maintenance and a GitHub-audit-driven depth pass. **Install reliability (2.1.1–2.1.4):** the installer now bundles the resource folders beside `SKILL.md` (the v2.1.0 flatten bug), writes MCP config to `.mcp.json` (not the unread `.claude/mcp.json`), bundles `validators/`, and resolves the core-file path references in the flattened layout. **Design depth (2.2.0–2.3.0):** `rules/20-rendered-verification.md` (21 rules total) makes Decision Pipeline step 12 a mandatory render → audit → fix loop; `templates/specs/design-system-master.md` adds a multi-page source-of-truth + page-overrides convention (the UI/UX Pro Max MASTER mechanism); a third before/after case (GEO course landing — answer-graph metaphor, dark pattern removed). Now 45 patterns, 27 references, 11 agents, 13 industry sectors.

---

## Planned

> v1.6 (CI, evals, `GDS_MCP_SAFE_MODE`, MCP resources + prompts) and v1.7 (demo gallery, installer + `gds` CLI, Figma pipeline) shipped and are folded into the v2.0.0 milestone above. The "Design Intelligence Platform" items below are still open — the v2.1–v2.3 releases shipped install hardening and design depth instead.

### Next — Design Intelligence Platform
- Design benchmark viewer — compare outputs with/without skill
- Reference pattern scoring — rank learned niches by accuracy
- MCP registry packaging — installable via `mcp install global-design-skill`
- Multi-agent design pipeline — perception → cognition → execution as separate agents
- Industry sector auto-update — detect stale niches from reference drift

---

## Contributing to the roadmap

Open a GitHub issue with the label `roadmap` to suggest a feature or vote on priorities.
