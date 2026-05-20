# Changelog

All notable changes to global-design-skill are documented here.

Format: [version] — date — description

---

## [1.0.0] — 2026-05-20

### Sprint 0 — Foundation

- `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `install.md`, `manifest.yaml`
- Full directory scaffold: skills/, agents/, rules/, patterns/, tokens/, templates/, checklists/, recipes/, examples/, integrations/
- `skills/global-design/SKILL.md` — main entry point: decision pipeline, 8 aesthetic archetypes, banned patterns list, technology standards
- `skills/global-design/task-routing.md` — routing table: build / review / improve / output tasks
- `skills/global-design/operating-principles.md` — 10 principles, cognitive laws (Hick, Fitts, Miller, Doherty)
- `skills/global-design/quality-gates.md` — 8 acceptance gates from problem definition to frontend readiness
- `skills/global-design/output-formats.md` — output templates per audience

### Sprint 1 — Agents (5 files)

- `agents/design-director.md` — visual maturity, brand alignment, aesthetic archetype check
- `agents/ux-architect.md` — problem definition, IA, user flows, edge cases
- `agents/conversion-designer.md` — CTAs, offer structure, friction inventory, pricing psychology
- `agents/design-critic.md` — adversarial review, banned pattern audit, REJECTED/CONDITIONAL/APPROVED verdicts
- `agents/frontend-handoff-reviewer.md` — Gate 8 validation: every state, token, ARIA attribute specified

### Sprint 2 — Blueprints (5 files)

- `blueprints/landing-page-from-scratch.md` — 9-section AIDA structure, hero to final CTA
- `blueprints/saas-app-from-scratch.md` — 3 shell options, 6 core screens, React 19 + Next.js 15 code
- `blueprints/admin-panel-from-scratch.md` — density-first, 6 screens, keyboard shortcuts
- `blueprints/website-from-scratch.md` — multi-page IA, CSS Anchor Positioning nav, schema markup
- `blueprints/redesign-existing-page.md` — 6-phase protocol: audit → classify → preserve/replace → redesign → regression

### Sprint 3 — Rules (7 files)

- `rules/01-visual-hierarchy.md` — 10 rules: focal point, size delta, contrast mapping, CTA dominance
- `rules/02-layout-and-grid.md` — 12 rules: mobile-first, grid break, safe areas, z-index system
- `rules/06-components.md` — 10 rules: component contracts, all states required, native dialog
- `rules/12-admin-panels.md` — 11 rules: density-first, label everything, destructive friction levels
- `rules/13-saas-products.md` — 10 rules: Day 1 vs Day 365, aha moment, useOptimistic
- `rules/14-landing-pages.md` — 11 rules: one CTA per section, headline formula, AIDA structure
- `rules/16-design-for-seo.md` — 10 rules: Core Web Vitals, schema markup, semantic HTML

### Sprint 4 — Marketing Patterns (5 files)

- `patterns/marketing-blocks/hero-sections.md` — 4 patterns: split, centered, full-bleed, asymmetric bento
- `patterns/marketing-blocks/pricing-sections.md` — 3 patterns + anchoring, decoy effect, annual default
- `patterns/marketing-blocks/social-proof.md` — 5 patterns: logos, metrics, testimonials, featured quote
- `patterns/marketing-blocks/cta-sections.md` — 4 patterns + full button CSS system
- `patterns/marketing-blocks/faq-sections.md` — 3 patterns + FAQPage schema JSON-LD

### Sprint 5 — Product UI Patterns (5 files)

- `patterns/product-ui/onboarding.md` — linear wizard, in-app checklist, product tour
- `patterns/product-ui/empty-states.md` — 5 types, copy formula, float animation
- `patterns/product-ui/error-states.md` — 9-type taxonomy, 5 patterns, copy formula
- `patterns/product-ui/loading-states.md` — decision matrix (<100ms / 100ms–1s / 1–10s / >10s), 6 patterns
- `patterns/product-ui/settings-pages.md` — IA, save-on-change vs submit, toggle, danger zone, API keys

### Sprint 6 — Navigation + Admin Patterns (6 files)

- `patterns/navigation/header-patterns.md` — marketing header (transparent→solid), app header, skip nav
- `patterns/navigation/sidebar-patterns.md` — full + collapsed, workspace switcher, expandable groups
- `patterns/navigation/mobile-navigation.md` — bottom tab bar, hamburger drawer with @starting-style
- `patterns/admin-ui/data-tables.md` — toolbar, bulk bar, sort, sticky headers, skeleton, pagination
- `patterns/admin-ui/filters.md` — filter bar, active chips, dropdown panel, date range, URL state
- `patterns/admin-ui/dashboard-layouts.md` — KPI cards, sparklines, 12-col grid, real-time pattern, accessible charts

### Sprint 7 — Templates + Checklists (6 files)

- `templates/specs/frontend-tz.md` — Gate 8 developer handoff: all states with exact values, tokens, ARIA, acceptance criteria
- `templates/specs/component-spec.md` — component API, anatomy, variants, states, ARIA, changelog
- `templates/briefs/project-brief.md` — problem, north star metric, scope, constraints, sign-off table
- `checklists/global-design-review.md` — 100+ checks across 11 sections, banned pattern audit
- `checklists/landing-conversion-review.md` — AIDA, CTA quality, social proof, friction, pricing, SEO
- `checklists/ui-review.md` — forms, tables, filters, modals, loading, errors, admin-specific, a11y

### Sprint 8 — Recipes (8 files)

- `recipes/make-page-more-premium.md` — 9 steps: typeface, OKLCH tint, grain texture, grid break, split hero, shadow system, bezel, spacing rhythm, signature detail
- `recipes/make-interface-cleaner.md` — 9 steps: 1 accent color, background depth, 3-level hierarchy, icon removal, dividers, button hierarchy, spacing grid, copy, z-axis
- `recipes/improve-hero-section.md` — 7 steps: layout choice, headline formula, eyebrow tag, product visual with perspective, CTA discipline, entry animation, LCP
- `recipes/improve-pricing-page.md` — 8 steps: annual default, recommended plan, price anchoring, feature table, social proof, CTA copy, enterprise, FAQ
- `recipes/improve-forms.md` — 7 steps: field audit, labels, error formula (validate on blur), loading/success, password reqs, never reset fields, keyboard nav
- `recipes/add-dark-mode.md` — 7 steps: OKLCH token architecture, shadow system, toggle without flash, localStorage, image/logo handling, component audit, transition
- `recipes/improve-mobile-version.md` — 10 steps: 100dvh, 44px targets, iOS zoom prevention, mobile nav, safe area insets, horizontal scroll, typography, hover-only, CTA above fold, performance
- `recipes/improve-empty-states.md` — 5 types (first-time/no-results/cleared/permission/error), copy tone rules, float animation, acceptance criteria

### Sprint 9 — Design Tokens (4 files)

- `tokens/design-tokens.json` — W3C DTCG format: OKLCH primitive palettes (10-step), semantic light/dark tokens, 20-value spacing grid, fluid type scale, tracking, line-height, radius, shadow, duration, cubic-bezier easings, z-index, breakpoints
- `tokens/tokens.css` — complete CSS custom properties: all token categories + component aliases (input/button/card/focus-ring) + global resets
- `tokens/tokens-dark.css` — dark mode via `[data-theme="dark"]` + `@media prefers-color-scheme`, shadow→border conversion, `.theme-transition` class
- `tokens/README.md` — two-layer color system, usage examples, Style Dictionary config, Tailwind v4 integration, stylelint rule

### Sprint 10 — Repository Finalization

- `README.md` — updated: complete file map (57 files), quick start, capabilities table, quality gates summary, banned patterns quick reference
- `CHANGELOG.md` — updated: complete sprint history

---

## Total: 57 files, ~18,000 lines

| Category | Files | Description |
|---|---|---|
| Core skill | 5 | Entry point, routing, principles, gates, formats |
| Agents | 5 | 5 specialized review roles |
| Blueprints | 5 | Build-from-scratch protocols |
| Rules | 7 | Domain rules with rationale and code |
| Patterns | 16 | Marketing, product UI, navigation, admin |
| Tokens | 4 | JSON + CSS light + CSS dark + guide |
| Templates | 3 | Specs and briefs |
| Checklists | 3 | Design review, conversion, UI ship |
| Recipes | 8 | Step-by-step improvement guides |
| Docs | 4 | README, CONTRIBUTING, CHANGELOG, install |

---

## Upcoming

- `examples/` — worked examples with before/after rationale
- `integrations/` — Claude Code CLAUDE.md, Cursor .cursorrules, ChatGPT system prompt
- Rules gaps: `03-typography.md`, `04-color.md`, `05-animation.md`, `07-accessibility.md`, `08-performance.md`
- Patterns gaps: form patterns, modal patterns, notification system
