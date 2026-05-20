# global-design-skill

A design operating system for AI-assisted development. Not a style guide — a production toolkit for building interfaces from zero to frontend handoff.

Works with Claude Code, Cursor, ChatGPT Custom GPTs, and any AI coding assistant.

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](CHANGELOG.md)
[![Standards](https://img.shields.io/badge/CSS-2026%20Baseline-green)](rules/)
[![React](https://img.shields.io/badge/React-19-blue)](rules/)
[![Next.js](https://img.shields.io/badge/Next.js-15-black)](rules/)
[![Tailwind](https://img.shields.io/badge/Tailwind-v4-cyan)](tokens/)

---

## What this is

```
Global Design Skill =
  Design Principles          (rules/)
+ UX Frameworks              (blueprints/)
+ UI Patterns                (patterns/)
+ Design Tokens              (tokens/)
+ Specialized Agents         (agents/)
+ Output Templates           (templates/)
+ Review Checklists          (checklists/)
+ Improvement Recipes        (recipes/)
```

**Not:** "make it look nice."
**Yes:** what to build, for whom, why, which grid, which states, how to hand it off, how to verify the result.

---

## Quick Start

### Claude Code

```bash
# 1. Clone
git clone https://github.com/yourusername/global-design-skill.git

# 2. Add to your project's CLAUDE.md
echo "\n# Design System\nSee global-design-skill/skills/global-design/SKILL.md" >> your-project/CLAUDE.md
```

### Cursor

```bash
cp skills/global-design/SKILL.md your-project/.cursorrules
```

### Any AI assistant

Start your prompt with:
```
Use the design system defined in [path to SKILL.md].
```

---

## Capabilities

| Task | How to invoke |
|---|---|
| Build a landing page from scratch | "Use global-design-skill and create a landing page for [product]" |
| Build a SaaS app | "Use global-design-skill and scaffold a SaaS app shell for [product]" |
| Build an admin panel | "Use global-design-skill and architect an admin panel for [product]" |
| Design a dashboard | "Use global-design-skill and build a dashboard for [app]" |
| Run a design audit | "Use global-design-skill and audit this page: [HTML/screenshot/URL]" |
| Write a frontend spec | "Use global-design-skill and write a frontend ТЗ for [component]" |
| Improve a hero section | "Use global-design-skill and improve this hero section" |
| Add dark mode | "Use global-design-skill and add dark mode to this project" |
| Review before shipping | "Use global-design-skill and run a UI review checklist" |

---

## Repository Structure

```
global-design-skill/
│
├── skills/global-design/           ← Core skill — start here
│   ├── SKILL.md                    ← Main AI entry point
│   ├── task-routing.md             ← "If task is X, use files Y"
│   ├── operating-principles.md     ← Design decision framework
│   ├── output-formats.md           ← Output format per audience
│   └── quality-gates.md            ← 8 acceptance gates
│
├── agents/                         ← Specialized review agents
│   ├── design-director.md          ← Visual maturity, brand alignment
│   ├── ux-architect.md             ← User flows, IA, edge cases
│   ├── conversion-designer.md      ← CTAs, pricing, friction
│   ├── design-critic.md            ← Adversarial — finds banned patterns
│   └── frontend-handoff-reviewer.md ← Gate 8: implementation-ready?
│
├── blueprints/                     ← Build-from-scratch protocols
│   ├── landing-page-from-scratch.md ← 9-section AIDA landing page
│   ├── saas-app-from-scratch.md    ← 3 shell options, 6 core screens
│   ├── admin-panel-from-scratch.md ← Density-first, 6 screens
│   ├── website-from-scratch.md     ← Multi-page IA, nav, schema
│   └── redesign-existing-page.md   ← 6-phase redesign protocol
│
├── rules/                          ← Design rules by domain
│   ├── 01-visual-hierarchy.md      ← 10 hierarchy rules
│   ├── 02-layout-and-grid.md       ← 12 layout rules, breakpoints
│   ├── 06-components.md            ← Component contracts, 10 rules
│   ├── 12-admin-panels.md          ← Density-first, 11 rules
│   ├── 13-saas-products.md         ← Day 1 vs Day 365, 10 rules
│   ├── 14-landing-pages.md         ← Single metric, 11 rules
│   └── 16-design-for-seo.md        ← CWV, schema, semantic HTML
│
├── patterns/
│   ├── marketing-blocks/           ← Landing page sections
│   │   ├── hero-sections.md        ← 4 patterns: split, centered, video, bento
│   │   ├── pricing-sections.md     ← 3 patterns + psychology principles
│   │   ├── social-proof.md         ← 5 patterns: logos, metrics, testimonials
│   │   ├── cta-sections.md         ← 4 patterns + button system
│   │   └── faq-sections.md         ← 3 patterns + FAQPage schema
│   │
│   ├── product-ui/                 ← SaaS / app UI
│   │   ├── onboarding.md           ← Linear wizard, checklist, product tour
│   │   ├── empty-states.md         ← 5 types with copy formulas
│   │   ├── error-states.md         ← 9-type taxonomy, 5 patterns
│   │   ├── loading-states.md       ← Decision matrix + 6 patterns
│   │   └── settings-pages.md       ← IA, forms, toggles, danger zone
│   │
│   ├── navigation/                 ← Navigation systems
│   │   ├── header-patterns.md      ← Marketing + app headers
│   │   ├── sidebar-patterns.md     ← Full + collapsed + workspace switcher
│   │   └── mobile-navigation.md    ← Bottom tab bar + hamburger drawer
│   │
│   └── admin-ui/                   ← Admin / data-heavy interfaces
│       ├── data-tables.md          ← Full anatomy: sort, select, pagination
│       ├── filters.md              ← Filter bar, chips, dropdown, URL state
│       └── dashboard-layouts.md    ← KPI cards, charts, real-time pattern
│
├── tokens/                         ← Design token system
│   ├── design-tokens.json          ← W3C DTCG format (Style Dictionary ready)
│   ├── tokens.css                  ← CSS custom properties — light mode
│   ├── tokens-dark.css             ← Dark mode overrides
│   └── README.md                   ← Usage guide + tooling integration
│
├── templates/
│   ├── specs/
│   │   ├── frontend-tz.md          ← Gate 8 developer handoff template
│   │   └── component-spec.md       ← Component API + states + ARIA template
│   └── briefs/
│       └── project-brief.md        ← Problem → goal → scope → sign-off
│
├── checklists/
│   ├── global-design-review.md     ← 100+ checks, 11 sections, banned patterns
│   ├── landing-conversion-review.md ← AIDA, CTA, social proof, friction, SEO
│   └── ui-review.md                ← Forms, tables, modals, loading, errors, a11y
│
├── recipes/                        ← "How to improve X" step-by-step guides
│   ├── make-page-more-premium.md   ← 9 steps: font → texture → asymmetry
│   ├── make-interface-cleaner.md   ← 9 steps: 1 accent → borders → hierarchy
│   ├── improve-hero-section.md     ← 7 steps: layout → headline → visual → CTA
│   ├── improve-pricing-page.md     ← 8 steps: annual → recommended → anchoring
│   ├── improve-forms.md            ← 7 steps: fields → labels → errors → loading
│   ├── add-dark-mode.md            ← 7 steps: tokens → toggle → flash prevention
│   ├── improve-mobile-version.md   ← 10 steps: dvh → targets → safe areas
│   └── improve-empty-states.md     ← 5 types with copy formulas and animations
│
├── README.md                       ← This file
├── CONTRIBUTING.md                 ← Contribution standards
├── CHANGELOG.md                    ← Version history
└── install.md                      ← Setup per tool
```

---

## Technology Standards (2026 Baseline)

| Area | Standard |
|---|---|
| **CSS** | Nesting, `:has()`, `@property`, `@starting-style`, Popover API, Anchor Positioning, Scroll-driven Animations, View Transitions Level 2 |
| **Colors** | OKLCH throughout — `oklch(65% 0.22 258)` not hex |
| **Tailwind** | v4 — `@theme {}` in CSS, no `tailwind.config.js` |
| **React** | 19 — `useActionState`, `useOptimistic`, `useFormStatus`, ref as prop |
| **Next.js** | 15 — `await cookies()`, `"use cache"`, Turbopack |
| **Motion** | `motion/react` — `useAnimate`, `useInView`, `animateView()` |
| **GSAP** | `useGSAP` from `@gsap/react`, `contextSafe()` |
| **TypeScript** | 5.x — `satisfies`, `const` type params, template literal types |
| **Accessibility** | WCAG 2.2 AA — 4.5:1 contrast, 44px touch targets, focus-visible |

---

## Design System

All colors use **OKLCH** for perceptual uniformity. All spacing on a **4px grid**. All type sizes use **`clamp()`** for fluid scaling.

```css
/* tokens/tokens.css — import in your project */
--color-accent:  oklch(57% 0.22 258);          /* electric blue */
--color-surface: oklch(100% 0.003 258);        /* card background */
--text-hero:     clamp(3.5rem, 8vw + 1rem, 12rem);
--space-6:       24px;                          /* 4px × 6 */
--radius-xl:     16px;
--ease-spring:   cubic-bezier(0.16, 1, 0.3, 1);
```

Dark mode: import `tokens-dark.css` and add `data-theme="dark"` to `<html>`. See `recipes/add-dark-mode.md`.

---

## Agents

Five agents run in sequence. Each has a distinct role:

| Agent | Runs when | Verdict format |
|---|---|---|
| `ux-architect` | Problem definition phase | Gates checklist |
| `design-director` | After concept is presented | Table: area / problem / severity |
| `conversion-designer` | Landing pages, pricing, onboarding | Friction inventory |
| `design-critic` | After design-director | REJECTED / CONDITIONAL / APPROVED |
| `frontend-handoff-reviewer` | Before dev handoff | Pass/fail per Gate 8 criterion |

---

## Key Patterns at a Glance

**Landing page structure:** `blueprints/landing-page-from-scratch.md`
→ Hero → Social proof bar → Problem → How it works → Features → Deep proof → Pricing → FAQ → Final CTA

**Admin panel core screens:** `blueprints/admin-panel-from-scratch.md`
→ Data table → Detail/Edit → Create/Form → User management → Audit log → Settings

**SaaS empty state formula:** `patterns/product-ui/empty-states.md`
→ Preview image → "[Feature] will appear here" → Why valuable → "Create your first [noun]"

**Error message formula:** `patterns/product-ui/error-states.md`
→ `[What failed] — [Why] — [How to fix]`

**CTA label formula:** `rules/14-landing-pages.md`
→ `Verb + Object + Context` — "Start Pro free for 14 days"

---

## Quality Gates

A design passes handoff when it clears all 8 gates:

```
Gate 1 — Problem defined (specific, data-backed)
Gate 2 — User identified (concrete person with context)
Gate 3 — Metric set (one primary metric with target)
Gate 4 — All states designed (idle/hover/active/focus/disabled/loading/empty/error/success)
Gate 5 — Responsive behavior specified (390px / 768px / 1280px)
Gate 6 — ARIA specified (every attribute on every interactive element)
Gate 7 — Tokens used (no raw hex, no raw px in components)
Gate 8 — Developer can implement without asking a question
```

Full gate specifications: `skills/global-design/quality-gates.md`
Developer handoff template: `templates/specs/frontend-tz.md`

---

## Banned Patterns

These patterns cause immediate design failure. Full list in `checklists/global-design-review.md`.

- Centered hero: H1 + subtext + 2 equal buttons (the default)
- Side-stripe accent borders (border-left/right > 1px colored)
- Gradient text (`background-clip: text`)
- Pure `#000000` / `#ffffff` without hue tint
- `transition: all` or `ease-in-out`
- `100vh` instead of `100dvh`
- `framer-motion` import instead of `motion/react`
- Placeholder text as form label
- Error messages: "Invalid", "Required", "Error" — no context

---

## Philosophy

**Removes uncertainty, doesn't generate beauty.**

Every output answers:
- What are we building?
- For whom?
- What business goal does this serve?
- Which grid, which blocks, which states?
- How does this adapt to mobile?
- How is this handed off to a developer?
- How do we know the result is good?

---

## Installation

See [install.md](install.md) for detailed setup per tool.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

MIT — use freely, attribution appreciated.
