# Packs — Global Design Skill

Global Design Skill is modular. You can install everything or only the parts you need.

---

## Start here

| Goal | Install |
|---|---|
| Better landing pages | Core + Landing Pack |
| SaaS app screens | Core + SaaS Pack |
| Admin panels | Core + Admin Pack |
| Design audits | Core + Audit Pack |
| Sector-aware design | Core + MCP Intelligence |
| Everything | `gds install --tool=all` |

---

## Core Skill

The foundation. Required by all other packs.

| File | Purpose |
|---|---|
| `skills/global-design/SKILL.md` | Main entry point — task routing |
| `skills/global-design/operating-principles.md` | Design decision framework |
| `skills/global-design/output-formats.md` | Output format per audience |
| `skills/global-design/quality-gates.md` | 8 acceptance gates |
| `skills/global-design/task-routing.md` | "If task is X, use files Y" |
| `rules/` (16 files) | Domain rules: layout, color, type, a11y, perf… |
| `tokens/` | OKLCH design tokens (CSS + JSON) |
| `checklists/global-design-review.md` | 100+ checks, banned patterns |
| `templates/specs/frontend-tz.md` | Gate 8 developer handoff template |

**Install:**
```bash
gds install --tool=claude-code [path]
```

---

## UI Packs

Build-from-scratch protocols for specific page types.

### Landing Pack

| File | Purpose |
|---|---|
| `blueprints/landing-page-from-scratch.md` | 9-section AIDA protocol |
| `blueprints/interactive-landing-page.md` | Grain + mesh + effects stack |
| `blueprints/pricing-page-from-scratch.md` | Hero + toggle, 3 tiers, FAQ, trust |
| `patterns/marketing-blocks/` | 9 section files (hero, features, social proof…) |
| `rules/14-landing-pages.md` | Landing page rules + banned patterns |
| `checklists/landing-conversion-review.md` | AIDA, CTA, friction checklist |

**Invoke:** `"Use global-design-skill and create a landing page for [product]"`

### SaaS Pack

| File | Purpose |
|---|---|
| `blueprints/saas-app-from-scratch.md` | 3 shell options, 6 core screens |
| `blueprints/onboarding-flow-from-scratch.md` | Signup → aha moment → checklist |
| `patterns/product-ui/` | 10 files: empty states, loading, modals, forms… |
| `rules/13-saas-products.md` | SaaS-specific rules |

**Invoke:** `"Use global-design-skill and scaffold a SaaS app for [product]"`

### Admin Pack

| File | Purpose |
|---|---|
| `blueprints/admin-panel-from-scratch.md` | Density-first, 6 screens |
| `patterns/admin-ui/` | 5 files: tables, charts, filters, bulk actions |
| `rules/12-admin-panels.md` | Admin density + destructive action rules |
| `checklists/admin-panel-review.md` | Admin-specific review checklist |

**Invoke:** `"Use global-design-skill and architect an admin panel for [product]"`

### Portfolio / Website Pack

| File | Purpose |
|---|---|
| `blueprints/portfolio-from-scratch.md` | Work grid, about, contact, anti-patterns |
| `blueprints/website-from-scratch.md` | Multi-page IA, nav, schema |
| `blueprints/redesign-existing-page.md` | 6-phase redesign protocol |

### Effects Pack

| File | Purpose |
|---|---|
| `blueprints/interactive-landing-page.md` | Full wow stack |
| `patterns/effects/` | 7 files: grain, parallax, text animations, 3D… |
| `references/motion-systems.md` | CSS + GSAP motion patterns |
| `checklists/wow-effects-checklist.md` | 65 checks: reduced-motion, GPU, mobile |
| `recipes/create-wow-hero.md` | Step-by-step wow hero recipe |

**Invoke:** `"Use global-design-skill and add a wow hero with grain, mesh gradient, and scroll animations"`

---

## Audit Packs

Review agents and checklists for specific audit types.

### Accessibility Audit Pack

| File | Purpose |
|---|---|
| `agents/accessibility-auditor.md` | 4-phase WCAG 2.2 audit |
| `rules/07-accessibility.md` | ARIA, focus, keyboard rules |
| `references/accessibility.md` | ARIA reference |
| `validators/axe-core.md` | axe-core + Jest/Playwright setup |

**Invoke:** `"Use global-design-skill accessibility-auditor on this component"`

### Performance Audit Pack

| File | Purpose |
|---|---|
| `agents/performance-auditor.md` | CWV investigation, LCP/CLS/INP |
| `rules/08-performance.md` | Performance rules |
| `validators/lighthouse-ci.md` | LCP < 2.5s, CLS < 0.1 budgets |
| `validators/bundle-analyzer.md` | Size limits, tree-shaking checklist |

**Invoke:** `"Use global-design-skill performance-auditor on this page"`

### Design System Audit Pack

| File | Purpose |
|---|---|
| `agents/design-systems-auditor.md` | Token coverage, debt scoring 0–100 |
| `agents/design-critic.md` | Adversarial pattern checker |
| `checklists/global-design-review.md` | Full 100+ checks |
| `feedback/gate-8-tracker.md` | Post-handoff question log |
| `feedback/iteration-log.md` | Revision count tracker |

**Invoke:** `"Use global-design-skill design-systems-auditor on this codebase"`

### Conversion Audit Pack

| File | Purpose |
|---|---|
| `agents/conversion-designer.md` | CTA, pricing, friction analysis |
| `agents/copy-editor.md` | Headline test, banned words |
| `checklists/landing-conversion-review.md` | AIDA + social proof checklist |

---

## MCP Intelligence

Self-learning design intelligence layer. Requires Python 3.11+.

| Capability | Tools |
|---|---|
| Auto-detect business sector | `classify_niche` |
| Get sector-specific rules | `get_sector_context` |
| Check design against sector rules | `check_banned_patterns` |
| Learn from reference sites | `learn_from_reference` |
| Manage local knowledge base | `list_learned_niches`, `forget_niche` |
| Resolve static/learned conflicts | `resolve_suspicion` |
| Reset pattern weights | `reset_weights` |

**Install:**
```bash
gds install --tool=mcp [path]
```

**Invoke:** `"Use global-design-skill and design for [context]"` — niche auto-detected.

See `mcp-server/README.md` for full setup and `PRIVACY.md` for data handling.

---

## All packs reference

| Pack | Files | Invoke prefix |
|---|---|---|
| Core | rules/, tokens/, skills/, templates/ | `"Use global-design-skill"` |
| Landing | blueprints/landing*, patterns/marketing-blocks/ | `"create a landing page"` |
| SaaS | blueprints/saas*, patterns/product-ui/ | `"scaffold a SaaS app"` |
| Admin | blueprints/admin*, patterns/admin-ui/ | `"architect an admin panel"` |
| Effects | patterns/effects/, blueprints/interactive* | `"add wow effects"` |
| Accessibility | agents/accessibility-auditor.md | `"accessibility-auditor"` |
| Performance | agents/performance-auditor.md | `"performance-auditor"` |
| Design System | agents/design-systems-auditor.md | `"design-systems-auditor"` |
| MCP Intelligence | mcp-server/, industries/, learning/, sedi/ | auto-detected |
