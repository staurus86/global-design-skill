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

### Sprint 11 — Missing Rules (5 files)

- `rules/03-typography.md` — R1 fluid clamp scale, R2 16px minimum, R3 letter-spacing tracks size, R4 line-height by context, R5 75ch max line length, R6 font pairing (banned fonts list), R7 eyebrow tag CSS, R8 H1 ≤3 lines on mobile, R9 no gradient text, R10 variable font weight animation
- `rules/04-color.md` — R1 OKLCH mandatory (anatomy), R2 tinted neutrals, R3 one accent hue, R4 accent ≤15% surface area, R5 chroma at extremes, R6 WCAG contrast table, R7 color not only differentiator, R8 dark mode as separate system, R9 color-mix() for alpha, R10 color strategy selection
- `rules/05-animation.md` — R1 everything must enter, R2 no ease-in-out (easing guide), R3 no transition:all, R4 duration scale table, R5 @starting-style, R6 prefers-reduced-motion, R7 IntersectionObserver, R8 no multiple pulse (shimmer), R9 stagger, R10 motion/react not framer-motion
- `rules/07-accessibility.md` — R1 keyboard-operable, R2 focus-visible ring, R3 persistent labels, R4 alt text, R5 ARIA custom components, R6 aria-live dynamic content, R7 modal focus trap, R8 44px touch targets, R9 skip navigation, R10 semantic HTML first. Keyboard reference table.
- `rules/08-performance.md` — Core Web Vitals targets table, R1 LCP fetchpriority, R2 image dimensions (CLS), R3 WebP/AVIF (compression targets), R4 lazy/eager loading, R5 font-display:swap, R6 async/defer scripts, R7 no CLS from dynamic content, R8 Doherty Threshold 400ms, R9 virtualize >200 rows, R10 Next.js "use cache"

### Sprint 12 — Integrations (3 files)

- `integrations/claude-code/CLAUDE.md` — ready-to-paste CLAUDE.md snippet: all 8 rule categories, token usage guide, quality gates checklist, banned patterns quick reference, reference file table
- `integrations/cursor/cursor-rules.md` — .cursorrules content for Cursor IDE: complete rule set in cursor-native format, 3 setup options (file/settings/docs)
- `integrations/chatgpt/custom-gpt-instructions.md` — full system prompt for Custom GPT or OpenAI API: role definition, all rule categories, banned patterns, color strategy guide, tech stack defaults, response format instructions, Python API usage example

### Sprint 13 — Worked Examples (5 files)

- `examples/01-hero-redesign.md` — centered to editorial split: font, gradient, CTA hierarchy fixes
- `examples/02-color-token-migration.md` — 12 files of hardcoded hex → OKLCH semantic token layer
- `examples/03-form-accessibility.md` — 8 a11y fixes: labels, error formula, touch targets, autocomplete
- `examples/04-card-grid-cleanup.md` — 3-equal-column grid → asymmetric bento with hierarchy
- `examples/05-performance-lcp.md` — fetchpriority, preload, image sizing, defer: LCP 4.2s → 1.8s

### Sprint 14 — Missing Rules (4 files)

- `rules/09-responsive.md` — 5 breakpoints, mobile-first, 100dvh, safe area insets, srcset/sizes, hover-only gating
- `rules/10-forms.md` — minimum fields, blur validation, error formula, no reset, autocomplete/inputmode, disabled states
- `rules/11-data-tables.md` — column alignment, density modes, aria-sort, row selection, sticky header, pagination vs infinite
- `rules/15-iconography.md` — stroke 1.5px, currentColor, single icon set, no emoji as icons, semantic labels

### Sprint 15 — Missing Patterns (4 files)

- `patterns/product-ui/forms.md` — sign-in, settings, multi-step, shared elements
- `patterns/product-ui/modals.md` — confirmation dialog, form modal, drawer, @starting-style entry, focus trap
- `patterns/product-ui/notifications.md` — 4-type decision tree, toast manager, banner, inline alert, aria-live
- `patterns/marketing-blocks/feature-sections.md` — alternating split, asymmetric bento grid, how-it-works steps

### Sprint 16 — New Agents (5 files)

- `agents/accessibility-auditor.md` — 4-phase WCAG audit (visual, keyboard, ARIA, content), severity matrix, WCAG 2.2 table
- `agents/performance-auditor.md` — CWV investigation, LCP/CLS/INP identification, budget table, regression detection
- `agents/copy-editor.md` — headline test, CTA formula, error formula, 20+ banned words, tone calibration table
- `agents/motion-designer.md` — easing audit by context, duration scale, prefers-reduced-motion, motion budget by page type
- `agents/design-systems-auditor.md` — token coverage grep commands, component state matrix, debt scoring 0–100, migration path

### Sprint 17 — Marketing Patterns + Recipes (3 files)

- `patterns/marketing-blocks/feature-sections.md` — alternating split, asymmetric bento, how-it-works with connectors
- `recipes/improve-navigation.md` — 6 steps: Hick's Law audit, rename to user goals, active state, mobile nav, breadcrumbs
- `recipes/improve-typography.md` — 7 steps: font replacement, fluid scale, line-height, letter-spacing, eyebrow, 65ch prose, gradient text

### Sprint 18 — Example + New Integrations (3 files)

- `examples/06-dark-mode-implementation.md` — primitive→semantic token layer, class-based toggle, localStorage, no-flash inline script, Next.js implementation
- `integrations/windsurf/rules.md` — .windsurfrules content: all 8 rule categories in Windsurf-native format
- `integrations/github-copilot/copilot-instructions.md` — .github/copilot-instructions.md: full design system rules for Copilot Chat

### Sprint 19 — Figma Integration (2 files)

- `integrations/figma/variables-export-guide.md` — variable architecture (primitives + semantic), Tokens Studio export, Style Dictionary transform, GitHub Actions auto-sync
- `integrations/figma/plugin-workflow.md` — plugin stack, Tokens Studio setup + GitHub sync, contrast checking workflow, handoff annotation, Gate checklist

### Sprint 20 — Navigation Patterns (3 files)

- `patterns/navigation/tabs-patterns.md` — horizontal tabs, pill tabs, vertical tabs, keyboard handler, ARIA roles
- `patterns/navigation/breadcrumbs.md` — standard, collapsed (ellipsis), dropdown variant, JSON-LD structured data
- `patterns/navigation/pagination.md` — standard, compact, rows-per-page, ellipsis algorithm, rel=prev/next SEO

### Sprint 21 — Product UI Patterns (3 files)

- `patterns/product-ui/search.md` — inline filter, live search with combobox ARIA + keyboard, empty state
- `patterns/product-ui/tooltips-popovers.md` — CSS-only tooltip, click popover, info tooltip, positioning rules
- `patterns/product-ui/command-palette.md` — full ⌘K palette: combobox, grouping, keyboard nav, search, command data schema

### Sprint 22 — Marketing + Admin Patterns (4 files)

- `patterns/marketing-blocks/comparison-sections.md` — pricing card grid, feature comparison table with highlighted column
- `patterns/marketing-blocks/stats-sections.md` — horizontal stats bar, stats with context + source, animated counter
- `patterns/admin-ui/charts.md` — chart type selection, Recharts line/bar/donut, sparklines, accessibility requirements
- `patterns/admin-ui/bulk-actions.md` — inline toolbar (slides in on selection), sticky bottom bar (mobile), confirmation modal

### Sprint 23 — Recipes (3 files)

- `recipes/add-animations.md` — 8 steps: motion budget, easing tokens, hover transitions, IntersectionObserver, hero entrance, skeleton shimmer, motion/react migration, @starting-style modals
- `recipes/improve-loading-states.md` — 5 patterns: skeleton loading, button spinner, optimistic UI, blur-up images, empty state
- `recipes/improve-onboarding.md` — 3 principles, multi-step wizard component, empty dashboard checklist, activation metrics

### Sprint 24 — Blueprints (3 files)

- `blueprints/pricing-page-from-scratch.md` — hero + annual toggle, 3-tier cards, comparison table, FAQ accordion, trust strip, final CTA, pricing psychology checklist
- `blueprints/portfolio-from-scratch.md` — hero with availability status, work grid (featured + 2-col), short about, contact CTA, portfolio anti-patterns
- `blueprints/onboarding-flow-from-scratch.md` — signup form (OAuth first), 3-step wizard, aha moment animation, getting-started checklist, activation metrics

### Sprint 25 — Example Directories (2 files)

- `examples/landing-pages/01-saas-hero-redesign.md` — banned centered hero → editorial left-aligned split with Fraunces + product screenshot
- `examples/apps/01-settings-page.md` — flat single-column form → vertical tab navigation with two-column rows + isolated danger zone

### Sprint 26 — References System + Reference Hunter Agent (13 files)

- `references/inspiration-sites.md` — 8-category curated gallery: general galleries, SaaS/product, marketing, portfolios, pricing, navigation, forms, dashboards
- `references/aesthetic-archetypes.md` — real production sites per archetype A–H, each with 8 examples + signature techniques + what to study
- `references/saas-ui-examples.md` — annotated SaaS UI: command palette, empty states, settings pages, onboarding, loading states, errors, modals, notifications, tables
- `references/marketing-sites.md` — hero sections, social proof, feature sections, pricing, CTAs, nav, animation — all annotated with "what to steal"
- `references/portfolios.md` — 8 top portfolio sites (paco.me, rauno.me, leerob.io, antfu.me, joshwcomeau.com, maggieappleton.com, brianlovin.it, tobiasahlin.com) with thesis analysis
- `references/pricing-pages.md` — Linear, Vercel, Stripe, Notion, GitHub, Intercom pricing analyzed — psychology, patterns, anti-patterns
- `references/navigation-examples.md` — sidebar (Linear, Vercel, Stripe, Notion), top nav (Webflow, Stripe, Arc), mobile (bottom tabs, hamburger), breadcrumbs
- `agents/reference-hunter.md` — 4 capabilities: (1) search by block category, (2) search by style/aesthetic, (3) competitive analysis, (4) URL audit with scoring rubric
- `templates/specs/design-review-report.md` — structured review output: gates, dimension scores, banned patterns, critical/major/minor issues, sign-off table
- `templates/briefs/redesign-brief.md` — redesign scope brief: what exists, what fails, constraints, acceptance criteria, sign-off
- `examples/audits/01-landing-page-audit.md` — full audit of generic B2B SaaS landing: 34/100 → all 8 gates, banned patterns found, prioritized fixes
- `examples/websites/01-multi-page-site.md` — multi-page site IA decisions, docs nav system, CSS Anchor Positioning, View Transitions, schema markup per page type

---

## Total: 121 files, ~44,000 lines

| Category | Files | Description |
|---|---|---|
| Core skill | 5 | Entry point, routing, principles, gates, formats |
| Agents | 11 | 11 specialized review roles (+ reference-hunter) |
| Blueprints | 8 | Build-from-scratch protocols |
| Rules | 16 | Domain rules with rationale and code |
| Patterns | 27 | Marketing, product UI, navigation, admin |
| References | 7 | Curated real-world examples per category and archetype |
| Tokens | 4 | JSON + CSS light + CSS dark + guide |
| Templates | 5 | Specs, briefs, review report, redesign brief |
| Checklists | 3 | Design review, conversion, UI ship |
| Recipes | 13 | Step-by-step improvement guides (+wow hero, +page transitions) |
| Integrations | 7 | Claude Code, Cursor, ChatGPT, Windsurf, Copilot, Figma (×2) |
| Examples | 10 | Before/after worked examples + audits + websites |
| Docs | 4 | README, CONTRIBUTING, CHANGELOG, install |

### Sprint 27 — Effects System + Wow Recipes (8 files)

**patterns/effects/ (new directory):**
- `patterns/effects/visual-effects.md` — grain texture, mesh gradient, spotlight cursor, glow/bloom, glassmorphism depth, double bezel, background patterns (dot/grid/diagonal), shadow depth system, aurora
- `patterns/effects/parallax-system.md` — 6 levels: CSS perspective (zero JS), JS scroll+RAF, multi-layer depth, mouse-tracking (lerp), GSAP ScrollTrigger scrub+pin, CSS scroll-driven `@scroll-timeline`
- `patterns/effects/text-animations.md` — split reveal (CSS + GSAP SplitText), blur-in sequence, character scramble hover, typewriter with cursor, variable font weight on scroll, gradient sweep, velocity marquee, count-up with IntersectionObserver
- `patterns/effects/scroll-experiences.md` — Lenis smooth scroll + GSAP integration, pinned stacking cards, horizontal scroll gallery, reading progress bar, section reveal system (IntersectionObserver), scroll-linked opacity fade, scroll snap
- `patterns/effects/hover-effects.md` — 3D card tilt + shine (mouse tracking), magnetic button, button fill slide/radial, image zoom/clip-path/overlay/caption, link underline draw, card lift, pill nav sliding indicator
- `patterns/effects/cursor-effects.md` — cursor glow tracking, custom dot cursor with lerp + hover/click states, mix-blend-mode invert, text-reveal cursor, cursor trail (`pointer: coarse` detection throughout)

**recipes/ (2 files):**
- `recipes/create-wow-hero.md` — 9-step wow hero: headline formula, 3 layout options, background atmosphere per archetype, display font setup, product visual with bezel+perspective, CTA hierarchy with magnetic, trust signal, entrance sequence, LCP optimization checklist
- `recipes/add-page-transitions.md` — first-load entrance (`[data-enter]` stagger system), View Transitions API (Baseline 2024), shared element transitions for portfolios, Next.js App Router integration, navigation progress bar

### Sprint 28 — Effects Completion + Wow Blueprint (4 new files + 3 updates)

**New files:**
- `patterns/effects/3d-effects.md` — CSS 3D fundamentals (perspective model), card flip, product tilt showcase with layered parallax, isometric layout, prism rotation, Three.js minimal setup, react-three-fiber integration, Spline embed, 3D text. Performance rules + when-to-use matrix
- `blueprints/interactive-landing-page.md` — full wow-stack blueprint: token foundation, global atmosphere (grain + spotlight), hero with entrance sequence, scroll reveals, GSAP pinned stack, marquee, CTA glow, View Transitions. 25-item assembly checklist, 4 archetype starter configs
- `checklists/wow-effects-checklist.md` — 9-category effects quality gate (65 items): reduced motion, GPU/compositing, bundle/load, mobile degradation, visual quality, entrance sequence, banned patterns, scroll integrity, accessibility. Scoring: ≥90% ship, 70–89% beta, <70% block
- `examples/websites/02-agency-portfolio.md` — full Cyberbrutalism (archetype C) studio site: brutal nav with offset-shadow buttons, kinetic marquee, Monument hero, asymmetric work grid, manifesto, case study layout, character scramble effect, view-transition title morph

**Updates:**
- `skills/global-design/task-routing.md` — rewritten: fixed broken paths, added Visual Effects Tasks section (all 7 effects files), references routing, reference-hunter agent
- `skills/global-design/SKILL.md` — added Effects Decision Block (4-step flow), fixed routing table, restored knowledge references + added example references
- `integrations/claude-code/CLAUDE.md` — added effects rules (will-change, devicePixelRatio, pointer:coarse, 100dvh), corrected rule file paths, added effects patterns table

**Also committed:** 12 knowledge references (`references/typography.md`, `color-alchemy.md`, `motion-systems.md`, `motion-dev.md`, `visual-effects.md`, `3d-animations.md`, `accessibility.md`, `performance.md`, `tokens.md`, `forms.md`, `responsive.md`, `data-viz.md`) and `patterns/marketing-blocks/bento-grid.md` — content that existed on disk but was never tracked (~5,700 lines).

---

## Total: 149 files, ~58,000 lines

| Category | Files | Description |
|---|---|---|
| Core skill | 5 | Entry point, routing, principles, gates, formats |
| Agents | 11 | Specialized review roles incl. reference-hunter |
| Blueprints | 9 | Build-from-scratch protocols incl. interactive landing |
| Rules | 16 | Domain rules with rationale and code |
| Patterns | 38 | Marketing, product UI, navigation, admin, effects |
| References | 19 | 12 knowledge references + 7 curated example galleries |
| Tokens | 4 | JSON + CSS light + CSS dark + guide |
| Templates | 5 | Specs, briefs, review report, redesign brief |
| Checklists | 4 | Design review, conversion, UI ship, wow effects |
| Recipes | 15 | Step-by-step improvement guides incl. wow recipes |
| Integrations | 7 | Claude Code, Cursor, ChatGPT, Windsurf, Copilot, Figma (×2) |
| Examples | 11 | Before/after worked examples + audits + websites |
| Docs | 5 | README, CONTRIBUTING, CHANGELOG, install, manifest |
