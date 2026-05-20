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
+ Worked Examples            (examples/)
+ Tool Integrations          (integrations/)
```

**Not:** "make it look nice."
**Yes:** what to build, for whom, why, which grid, which states, how to hand it off, how to verify the result.

---

## Capabilities

| Task | Command |
|---|---|
| Build a landing page from scratch | "Use global-design-skill and create a landing page structure for [product]" |
| Design a SaaS dashboard | "Use global-design-skill and build a dashboard blueprint for [app]" |
| Audit existing UI | "Use global-design-skill and run a UX/UI audit of this page: [URL/HTML/screenshot]" |
| Create a design system | "Use global-design-skill and generate a design system: grid, typography, tokens, components" |
| Prepare frontend spec | "Use global-design-skill and write a frontend ТЗ for this design decision" |
| Redesign a page | "Use global-design-skill and create a redesign plan for [page], prioritized by impact" |
| Build admin panel | "Use global-design-skill and architect an admin panel for [product]" |

---

## Quick Start

### Claude Code

```bash
# 1. Clone
git clone https://github.com/yourusername/global-design-skill.git

# 2. Copy skill to your project
bash scripts/copy-skill-to-project.sh

# 3. Add to your project's CLAUDE.md
cat integrations/claude-code/CLAUDE.md >> your-project/CLAUDE.md
```

### Cursor

```bash
cp integrations/cursor/cursor-rules.md your-project/.cursorrules
```

### ChatGPT

Copy `integrations/chatgpt/custom-gpt-instructions.md` into your Custom GPT system prompt.

---

## Repository Structure

```
global-design-skill/
│
├── skills/global-design/        ← Core skill: routing, principles, quality gates
│   ├── SKILL.md                 ← Main entry point for AI agents
│   ├── task-routing.md          ← "If task is X, use files Y"
│   ├── operating-principles.md  ← How to think about design decisions
│   ├── output-formats.md        ← Output format per audience
│   └── quality-gates.md        ← Acceptance criteria
│
├── agents/                      ← Specialized agent roles
├── rules/                       ← Design rules by domain
├── blueprints/                  ← Build-from-scratch scenarios
├── patterns/                    ← UI block patterns with variants
├── tokens/                      ← Design tokens (CSS + JSON)
├── templates/                   ← Briefs, specs, prompts, outputs
├── checklists/                  ← Review checklists by task type
├── recipes/                     ← "How to improve X" guides
├── examples/                    ← Worked examples
└── integrations/                ← Claude Code, Cursor, ChatGPT, Figma
```

---

## Technology Standards (2025–2026)

This skill is built on current baseline — no legacy patterns:

| Area | Standard |
|---|---|
| CSS | Nesting, `:has()`, `@property`, `@starting-style`, Popover API, Anchor Positioning, Scroll-driven Animations, View Transitions Level 2 |
| Colors | OKLCH throughout — `oklch(65% 0.22 258)` not hex |
| Tailwind | v4 — `@theme {}` in CSS, no `tailwind.config.js` |
| React | 19 — `useActionState`, `useOptimistic`, `useFormStatus`, ref as prop |
| Next.js | 15 — async APIs (`await cookies()`), `"use cache"`, Turbopack |
| Motion | `motion/react` package — `useAnimate`, `useInView`, `animateView()` |
| GSAP | `useGSAP` hook from `@gsap/react`, `contextSafe()`, auto-cleanup |
| TypeScript | 5.x — `satisfies`, `const` type params, template literal types |
| Accessibility | WCAG 2.2 AA — 4.5:1 contrast, 44px touch targets, focus-visible |

---

## Design System

All color values use OKLCH for perceptual uniformity. All spacing on a 4px grid. All type sizes use `clamp()` for fluid scaling.

```css
/* Core token example */
--color-accent:  oklch(65% 0.22 258);   /* electric blue */
--color-base:    oklch(9%  0.012 258);  /* dark surface */
--text-hero:     clamp(3.5rem, 8vw + 1rem, 12rem);
--space-6:       1.5rem;               /* 24px */
```

See `tokens/` for full token sets per design style (SaaS dark, SaaS light, Editorial, Enterprise Admin).

---

## Agents

| Agent | Responsibility |
|---|---|
| `design-director` | Overall concept, visual maturity, brand alignment |
| `ux-architect` | User journeys, information architecture, flows |
| `conversion-designer` | CTAs, offer structure, pricing psychology |
| `design-critic` | Adversarial review — finds weak points, not solutions |
| `frontend-handoff-reviewer` | Verifies implementation-readiness |

---

## Philosophy

**Снимает неопределённость, не генерирует красоту.**

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
