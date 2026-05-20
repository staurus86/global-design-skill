# Changelog

All notable changes to global-design-skill are documented here.

Format: [version] — date — description

---

## [1.0.0] — 2026-05-20

### Added — Sprint 0: Foundation

**Repository structure**
- Full directory tree: skills/, agents/, rules/, patterns/, tokens/, templates/, checklists/, recipes/, examples/, integrations/, docs/, scripts/
- `README.md` — public-facing with quick start, capabilities, technology standards
- `install.md` — setup for Claude Code, Cursor, ChatGPT, Figma
- `CONTRIBUTING.md` — contribution standards, file formats, philosophy
- `manifest.yaml` — skill metadata, standards, agent list, token sets
- `CHANGELOG.md` (this file)

**Core skill (skills/global-design/)**
- `SKILL.md` — main entry point: decision pipeline, technology standards (CSS 2026, React 19, Next.js 15, Tailwind v4, Motion, GSAP, TypeScript 5), banned patterns, output formats
- `task-routing.md` — full routing table: build / review / improve / output tasks mapped to files
- `operating-principles.md` — 10 design decision principles + cognitive laws
- `quality-gates.md` — 8 acceptance gates (problem definition through frontend readiness)
- `output-formats.md` — output templates for client / developer / vibe coding / designer / audit

### Technology baseline established

- CSS 2026: `@starting-style`, Popover API, `dialog:open`, View Transitions Level 2, Scroll-driven animations, CSS Anchor Positioning, `@property`, `color-mix()`, native nesting
- React 19: `useActionState`, `useOptimistic`, `useFormStatus`, ref-as-prop, async form actions, React Compiler
- Next.js 15: async `cookies()`/`headers()`/`params`, `"use cache"` directive, `cacheLife()`, Turbopack stable, fetch default `no-store`
- Tailwind v4: `@theme {}` CSS-native config, OKLCH default colors, 3D transforms, `@custom-variant dark`
- Motion: `motion/react` package, `useAnimate`, `useInView`, `animateView()`
- GSAP: `useGSAP` hook, `contextSafe()`, auto-cleanup pattern
- TypeScript 5: `satisfies`, `const` type params, template literal types
- shadcn/ui + Tailwind v4: `@theme inline` theming pattern, OKLCH tokens

---

## Upcoming

### Sprint 1: Task Routing & Core Skill — planned

### Sprint 2: Agents — planned
- design-director, ux-architect, conversion-designer, design-critic, frontend-handoff-reviewer

### Sprint 3: Blueprints — planned
- landing-page, saas-app, admin-panel, website, redesign

### Sprint 4: Rules — planned
- visual-hierarchy, layout-and-grid, components, admin-panels, saas-products, landing-pages, design-for-seo

### Sprint 5–7: Patterns — planned
- Marketing blocks, Product UI, Navigation, Admin UI

### Sprint 8–9: Templates & Checklists — planned

### Sprint 10–11: Recipes & Tokens — planned

### Sprint 12–14: Examples, Integrations, Docs — planned
