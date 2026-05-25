## Global Design Skill v1.5.0 — Industry-Aware Design Intelligence

This release evolves the skill from a universal design system into a self-learning, niche-aware design intelligence system (SEDI). The 4-phase architecture is now fully implemented.

### What's new

**13 industry sector files** — the skill now knows what it's designing *for*. Each `industries/*.md` file contains sector-specific required elements, banned patterns, trust signals, conversion paths, mobile rules, and a 5-question quick diagnosis. Sectors: B2B Products, B2C Products, Services, Content & Media, Education, Health, Finance, Real Estate, Travel, Tech/SaaS, Non-Profit, Government, Entertainment (with sub-niche routing for games/streaming/events).

**MCP Server (12 tools)** — a Python server you can connect to Claude Code, Cursor, or Windsurf. Classifies your niche automatically, returns sector-specific rules, checks banned patterns, learns from reference sites you provide, and resolves conflicts between static and learned knowledge.

**Learning Engine** — when a niche isn't in the static files, the engine scrapes reference sites (ethically, with robots.txt compliance and 10 req/min rate limiting), extracts layout/component/trust patterns, and saves them locally. Knowledge is stored at `~/.global-design-skill/` — no data leaves your machine.

**SEDI Full Architecture** — 6-layer orchestration:
- **Perception** — detects intent (create/improve/audit), sector, sub-niche, constraints, and emotional signals from your request
- **Cognition** — applies a 4-level conflict resolver (user override → validated learned → static rules → generic) and selects the right blueprint
- **Execution** — generates design output with cited sources per rule applied
- **Feedback Engine** — tracks explicit ratings (1–5) and implicit signals (revision count); updates pattern weights ±10%, bounded [0.1, 2.0]
- **Evolution** — weekly cycle captures baseline accuracy, detects stale niches, logs all changes to `evolution_log/`

**Extended State System** — 14 UI states (up from 9). New: skeleton, partial-error, offline, permission, rate-limit. Includes a `_decision-matrix.md` with a loading/skeleton mutual exclusion rule.

**Validators + Feedback tracking** — Lighthouse CI budgets (LCP < 2.5s, CLS < 0.1), axe-core a11y setup, bundle size limits, Gate 8 tracker, and iteration log templates.

### Privacy

All learning and personalization data stays on your machine at `~/.global-design-skill/`. No telemetry. No remote logging. The ethical scraper discloses itself via User-Agent and respects robots.txt.

### Breaking changes

None. All new directories are additive. Existing skill files are unchanged. The MCP server is optional.

### Upgrade

```bash
git pull origin master
# If using MCP server:
cd mcp-server && pip install -e ".[test]"
```

### File count

v1.0.0: 154 files (~59,000 lines)
v1.5.0: +69 files (~18,000 lines) = **223 files (~77,000 lines)**
