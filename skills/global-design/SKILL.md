---
name: global-design-skill
version: 1.7.0
version_schema: semver
license: MIT
author: global-design-skill
tags: [design, ui-ux, react, nextjs, tailwind, accessibility, frontend, design-system]
created: 2024-09-01
updated: 2026-05-26
package: https://github.com/staurus86/global-design-skill
requires:
  - blueprints/
  - patterns/
  - references/
  - checklists/
  - rules/
  - templates/
  - agents/
standalone: "partial — inline sections cover most common tasks; full package adds blueprints, patterns, references"
description: >
  Design operating system for any UI/UX task: websites, landing pages, SaaS apps,
  admin panels, dashboards, forms, design systems, frontend handoff specs.
  Self-contained: inline tokens, quality gates, banned patterns, and technology standards
  cover most common tasks without external files. Requires full package for deep domain references (blueprints,
  patterns, checklists). React 19, Next.js 15, Tailwind v4, Motion, GSAP.
  Standards: CSS 2026 Baseline, WCAG 2.2 AA.
---

# Global Design Skill

> **Package skill:** Part of [global-design-skill](https://github.com/staurus86/global-design-skill). The inline Decision Pipeline, Design Tokens, Quality Gates, Banned Patterns, and Technology Standards in this file are self-sufficient for most common design tasks. The full package adds deep reference catalogs, build blueprints, pattern libraries, and agent workflows.
>
> **Inline (works standalone):** Decision Pipeline · Design Tokens · Quality Gates · Banned Patterns · Technology Standards · Output Formats
>
> **Requires full package:** `blueprints/` build protocols · `patterns/` component library · `references/` domain catalogs · `rules/` detailed rules · `checklists/` full review checklists

You are a senior design system architect, UX strategist, and product design reviewer.

**Not:** "generate something beautiful."
**Yes:** define what to build, for whom, why, and exactly how — down to states, tokens, and developer spec.

---

## Core Mandate

For every task, resolve these before any code or visuals:

1. **What type of interface?** (landing / SaaS app / admin / dashboard / form / component)
2. **Who is the user?** (role, context, device, ambient light, emotional state)
3. **What is the business goal?** (conversion / retention / efficiency / trust)
4. **What does "done" look like?** (concrete acceptance criteria — see Quality Gates section in this file)

If any of these is unclear — ask. One targeted question beats an hour of wrong work.

**When context cannot be obtained:** If the user cannot provide type/user/goal after one targeted question, proceed with explicit stated assumptions: "Assuming [X] based on [signal in the request] — flag for review." Generate the design against those assumptions; do not invent unstated requirements silently. Offer to revise once real context arrives.

---

## Task Routing

Quick routing table — apply the Decision Pipeline for any task type. Full package adds step-by-step build protocols for each type.

| Task type | Inline approach | Full-package protocol |
|---|---|---|
| Landing page / marketing site | Decision Pipeline → Lead gen conversion focus | `blueprints/landing-page-from-scratch.md` |
| Interactive landing page (wow/effects) | Effects Decision Block + Motion standards | `blueprints/interactive-landing-page.md` |
| SaaS product / app | Decision Pipeline → Retention + task efficiency | `blueprints/saas-app-from-scratch.md` |
| Admin panel / back-office | Decision Pipeline → Density + keyboard nav | `blueprints/admin-panel-from-scratch.md` |
| Pricing page | Decision Pipeline → Trust + clarity focus | `blueprints/pricing-page-from-scratch.md` |
| Onboarding flow | Decision Pipeline → Activation + aha moment | `blueprints/onboarding-flow-from-scratch.md` |
| Portfolio site | Decision Pipeline → Credibility + work showcase | `blueprints/portfolio-from-scratch.md` |
| Redesign / improvement | Banned Patterns audit → targeted fixes | `blueprints/redesign-existing-page.md` |
| Website from scratch | Decision Pipeline → full IA → blueprints | `blueprints/website-from-scratch.md` |
| Animations / motion | Effects Decision Block (in this file) | `patterns/effects/` directory |
| UI block / component | Quality Gates → States → Tokens | `patterns/` directory |
| UI review / audit | Banned Patterns + Quality Gates (in this file) | `checklists/ui-review.md` |
| Frontend spec / handoff | Output Formats → developer template (in this file) | `templates/specs/frontend-tz.md` |

> **Standalone mode:** Inline sections listed above are sufficient for correct, handoff-ready output. Blueprint and pattern files (full package) provide step-by-step protocols for complex builds.

---

## Decision Pipeline

For any design task, follow this order. Do not skip steps.

```
1. TYPE      → What are we building? Which blueprint applies?
2. USER      → Who uses this? Where? In what state of mind?
3. GOAL      → What business outcome does this serve?
4. IA        → What pages/screens/blocks are required?
5. GRID      → Which layout system? (12-col / bento / sidebar / fluid)
6. TOKENS    → Colors (OKLCH), type scale (clamp), spacing (4px grid)
7. BLOCKS    → Which patterns from patterns/?
8. STATES    → Loading / empty / error for every interactive component
9. RESPONSIVE → Mobile-first. Test at 390px, 768px, 1280px
10. A11Y     → Contrast, keyboard, ARIA, focus management
11. HANDOFF  → Can a developer implement this without guessing?
12. VERIFY   → Does output pass all Quality Gates? (see Quality Gates section in this file)
```

---

## Effects Decision Block

For any task involving motion, animation, or visual atmosphere, answer these before selecting patterns.

**Step 1 — Does this need effects at all?**

| Signal | Answer |
|---|---|
| User explicitly requests "wow", animations, parallax, 3D | Yes — use Effect Type table below |
| Interactive landing page, portfolio, agency | Yes — use Effect Type table below |
| Standard B2B SaaS form-first page | No — skip effects, apply Decision Pipeline for conversion focus |
| Admin panel, data table, dashboard | No — performance matters more than wow |

**Step 2 — Select effect type and implementation approach**

| Goal | Implementation | Full-package pattern |
|---|---|---|
| Atmosphere (grain, mesh, spotlight, glow) | CSS `backdrop-filter`, `radial-gradient`, SVG `feTurbulence` | `patterns/effects/visual-effects.md` |
| Depth / multi-layer scroll | GSAP ScrollTrigger with `parallax` or CSS `animation-timeline: scroll()` | `patterns/effects/parallax-system.md` |
| Text reveals, scramble, typewriter, marquee | GSAP SplitText or CSS `@keyframes` with `clip-path` | `patterns/effects/text-animations.md` |
| Pinned scroll, horizontal gallery, progress bar | GSAP ScrollTrigger `pin: true` or CSS scroll-driven | `patterns/effects/scroll-experiences.md` |
| Hover tilt, magnetic button, link underline | CSS `transform` on `:hover` or Motion `useMotionValue` | `patterns/effects/hover-effects.md` |
| Custom cursor, blend mode, trail | CSS `mix-blend-mode`, JS `mousemove` + RAF | `patterns/effects/cursor-effects.md` |
| CSS 3D, card flip, product tilt, Three.js, Spline | CSS `perspective`/`rotateX` or `@react-three/fiber` | `patterns/effects/3d-effects.md` |

**Step 3 — Set motion budget before writing code**

| Budget | When | Libraries |
|---|---|---|
| CSS-only | Simple reveals, hover states | 0kb |
| CSS + IntersectionObserver | Scroll reveals, entrance sequences | ~0.5kb |
| CSS + GSAP ScrollTrigger | Pinned scroll, complex timelines | ~40kb |
| Three.js or R3F | 3D scene with lighting, orbit | ~150–200kb |

**Step 4 — Always check before shipping**

| Check | Pass | Fail → Action |
|---|---|---|
| `prefers-reduced-motion` | All animations disabled | Wrap every animation in `@media (prefers-reduced-motion: no-preference)` |
| Layout shift (CLS) | No shift from late effects | Animate only `transform`/`opacity`; add `will-change: transform` |
| GPU compositing | No `top`/`left` animation | Replace with `translateX`/`translateY` |
| Mobile overflow | No horizontal scroll at 390px | Constrain effect container with `overflow: hidden` |
| Performance | Lighthouse ≥ 88 mobile | Defer heavy scripts; reduce Three.js bundle |
| Interactive feedback | Response ≤ 400ms | Separate hover/click animations from scroll-driven ones |

---

## Technology Standards (2025–2026)

Use these — not legacy alternatives.

### CSS

```css
/* File: app/globals.css (or styles/tokens.css) */

/* OKLCH for all colors */
--color-accent: oklch(65% 0.22 258);
--color-base:   oklch(9%  0.012 258);

/* Animate custom properties via @property */
@property --gradient-angle {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

/* Native nesting */
.card {
  background: var(--color-surface);
  &:hover { background: var(--color-surface-2); }
  @media (min-width: 768px) { display: flex; }
}

/* Popover API — no JS needed for basic dropdowns */
[popover] {
  opacity: 0; transform: scale(0.95);
  transition: opacity 0.2s, transform 0.2s,
              display 0.2s allow-discrete,
              overlay 0.2s allow-discrete;
}
[popover]:popover-open { opacity: 1; transform: scale(1); }
@starting-style { [popover]:popover-open { opacity: 0; transform: scale(0.95); } }

/* Scroll-driven animations — no JS for simple reveals */
@keyframes reveal {
  from { opacity: 0; transform: translateY(1.5rem); }
  to   { opacity: 1; transform: none; }
}
.card {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 40%;
}

/* Dialog native transition */
dialog:open { opacity: 1; transform: scaleY(1); }
dialog {
  opacity: 0; transform: scaleY(0);
  transition: opacity 0.2s, transform 0.2s,
              overlay 0.2s allow-discrete, display 0.2s allow-discrete;
}
@starting-style { dialog:open { opacity: 0; transform: scaleY(0); } }
```

### Tailwind v4

```css
/* File: app/globals.css */

/* No tailwind.config.js — everything in CSS */
@import "tailwindcss";

@theme {
  --color-brand:    oklch(65% 0.22 258);
  --font-display:   "Syne", "sans-serif";
  --breakpoint-3xl: 1920px;
}

/* Dark mode */
@custom-variant dark (&:is(.dark *));

/* shadcn/Radix theming layer */
@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
}
```

### React 19

```tsx
/* File: components/Input.tsx (any component file) */

/* ref as regular prop — no forwardRef needed */
function Input({ ref, ...props }: Props & { ref?: Ref<HTMLInputElement> }) {
  return <input ref={ref} {...props} />
}

/* Form state management */
const [state, action, isPending] = useActionState(serverAction, null)

/* Optimistic UI */
const [optimisticItems, addOptimistic] = useOptimistic(items)

/* Form status */
function Submit() {
  const { pending } = useFormStatus()
  return <button disabled={pending}>{pending ? 'Saving...' : 'Save'}</button>
}

/* Async form actions */
<form action={async (formData) => {
  addOptimistic(newItem)
  await createItem(formData)
}}>
```

### Next.js 15

```tsx
/* File: app/[id]/page.tsx (Server Component) */

/* Async APIs — must await (breaking change from v14) */
const cookieStore = await cookies()
const headersList = await headers()
const { id } = await params
const { q } = await searchParams

/* fetch: no-store by default (breaking — v14 was force-cache) */
fetch(url, { next: { revalidate: 3600 } })  /* explicit cache */

/* New "use cache" directive */
async function getData() {
  "use cache"
  cacheLife('minutes')
  return db.query(...)
}
```

### Motion (`motion/react`)

```tsx
/* File: components/Section.tsx */

import { motion, AnimatePresence, useScroll, useAnimate, useInView } from 'motion/react'
import { animate, spring } from 'motion'

/* Scroll-triggered with useInView */
function Section() {
  const [scope, animate] = useAnimate()
  const isInView = useInView(scope, { once: true })

  useEffect(() => {
    if (isInView) animate('li', { opacity: 1, y: 0 }, { delay: stagger(0.08) })
  }, [isInView])

  return <ul ref={scope}><li /><li /></ul>
}

/* View Transitions */
import { animateView } from 'motion'
```

### GSAP

```tsx
/* File: components/Hero.tsx */

import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { useGSAP } from '@gsap/react'

gsap.registerPlugin(ScrollTrigger, useGSAP)

function Hero() {
  const container = useRef(null)

  const { contextSafe } = useGSAP(() => {
    gsap.from('.title', { y: 50, autoAlpha: 0, duration: 0.8, ease: 'power3.out' })
    gsap.to('.bg', {
      xPercent: -10,
      scrollTrigger: { trigger: container.current, start: 'top top', end: 'bottom top', scrub: 1 }
    })
  }, { scope: container })

  const handleClick = contextSafe(() => gsap.to('.cta', { scale: 1.05, yoyo: true, repeat: 1 }))

  return <section ref={container}>...</section>
}
```

### TypeScript 5

```typescript
/* File: lib/tokens.ts (or any .ts / .tsx file) */

/* satisfies — validate without widening */
const tokens = {
  accent: 'oklch(65% 0.22 258)',
  muted:  'oklch(55% 0.01 258)',
} satisfies Record<string, string>

/* const type params — literal inference */
function variants<const T extends string[]>(v: T): T { return v }
const v = variants(['primary', 'ghost'])  /* → readonly ["primary", "ghost"] */

/* Template literal types for tokens */
type SpaceToken  = `--space-${1|2|3|4|5|6|8|10|12|16|20|24|32}`
type ColorToken  = `--color-${string}`
```

---

## Design Tokens (Core)

Use these when no project token system exists, or as the reference palette. Full token file: `tokens/tokens.css` (full package).

### Color — OKLCH Primitive Palette

```css
:root {
  /* Accent (hue 258 = electric blue) */
  --color-accent-50:  oklch(97% 0.04 258);
  --color-accent-100: oklch(93% 0.07 258);
  --color-accent-300: oklch(80% 0.15 258);
  --color-accent-500: oklch(65% 0.22 258);  /* primary accent */
  --color-accent-700: oklch(48% 0.20 258);
  --color-accent-900: oklch(28% 0.12 258);

  /* Neutral (hue-tinted toward accent) */
  --color-neutral-0:    oklch(100% 0.002 258);  /* white */
  --color-neutral-100:  oklch(97%  0.007 258);
  --color-neutral-400:  oklch(72%  0.010 258);
  --color-neutral-700:  oklch(32%  0.012 258);
  --color-neutral-900:  oklch(15%  0.013 258);
  --color-neutral-1000: oklch(8%   0.015 258);  /* near-black */

  /* Status */
  --color-success: oklch(55% 0.18 145);
  --color-warning: oklch(65% 0.18 75);
  --color-error:   oklch(52% 0.22 25);

  /* Semantic — map to primitives in your theme */
  --color-bg:           var(--color-neutral-0);
  --color-surface:      var(--color-neutral-100);
  --color-text:         var(--color-neutral-1000);
  --color-text-muted:   var(--color-neutral-700);
  --color-border:       var(--color-neutral-200);
  --color-accent:       var(--color-accent-500);
}
```

### Typography — Fluid Type Scale

```css
:root {
  --text-xs:   clamp(0.69rem,  0.66rem + 0.14vw, 0.75rem);
  --text-sm:   clamp(0.83rem,  0.78rem + 0.24vw, 0.94rem);
  --text-base: clamp(1rem,     0.93rem + 0.34vw, 1.19rem);
  --text-lg:   clamp(1.2rem,   1.11rem + 0.47vw, 1.5rem);
  --text-xl:   clamp(1.44rem,  1.31rem + 0.65vw, 1.88rem);
  --text-2xl:  clamp(1.73rem,  1.54rem + 0.92vw, 2.34rem);
  --text-3xl:  clamp(2.07rem,  1.82rem + 1.28vw, 2.93rem);
  --text-4xl:  clamp(2.49rem,  2.14rem + 1.76vw, 3.66rem);
  --text-5xl:  clamp(2.99rem,  2.52rem + 2.37vw, 4.58rem);

  --font-sans:    system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-display: var(--font-sans);  /* override with brand font */
  --font-mono:    "Cascadia Code", "Fira Code", ui-monospace, monospace;

  --leading-tight:  1.15;
  --leading-normal: 1.5;
  --leading-loose:  1.75;
}
```

### Spacing — 4px Grid

```css
:root {
  --space-1:  0.25rem;  /*  4px */
  --space-2:  0.5rem;   /*  8px */
  --space-3:  0.75rem;  /* 12px */
  --space-4:  1rem;     /* 16px */
  --space-6:  1.5rem;   /* 24px */
  --space-8:  2rem;     /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
  --space-20: 5rem;     /* 80px */
  --space-24: 6rem;     /* 96px */
  --space-32: 8rem;     /* 128px */

  /* Semantic */
  --space-section: var(--space-24);  /* between page sections */
  --space-group:   var(--space-16);  /* between related blocks */
  --space-element: var(--space-6);   /* between elements in a block */
}
```

### Border Radius & Shadows

```css
:root {
  --radius-sm: 0.25rem;   /*  4px */
  --radius-md: 0.5rem;    /*  8px */
  --radius-lg: 0.75rem;   /* 12px */
  --radius-xl: 1rem;      /* 16px */
  --radius-full: 9999px;

  --shadow-sm: 0 1px 2px oklch(0% 0 0 / 0.06), 0 1px 3px oklch(0% 0 0 / 0.10);
  --shadow-md: 0 4px 6px oklch(0% 0 0 / 0.07), 0 2px 4px oklch(0% 0 0 / 0.06);
  --shadow-lg: 0 10px 15px oklch(0% 0 0 / 0.10), 0 4px 6px oklch(0% 0 0 / 0.05);
}
```

---

## Quality Gates

A design is "done" only when it passes all gates for its type.

| Gate | Landing | SaaS | Admin | Component |
|---|---|---|---|---|
| 1 Problem Definition | Required | Required | Required | Required |
| 2 Information Architecture | Required | Required | Required | — |
| 3 Design System | Required | Required | Required | Required |
| 4 States | Required | Required | Required | Required |
| 5 Responsive | Required | Required | Required | Required |
| 6 Accessibility | Required | Required | Required | Required |
| 7 Performance | Required | Recommended | Recommended | — |
| 8 Frontend Readiness | Required | Required | Required | Required |

**Gate 1 — Problem Definition:** User defined (role, device, context). Business goal stated as measurable outcome. Success metric exists. Scope is clear. *Blocked: no design work proceeds without this.*

**Gate 3 — Design System:** Colors in OKLCH. Type scale with `clamp()`. Spacing on 4px grid. All values as CSS custom properties — no raw values in components.

**Gate 4 — States:** Every interactive component has: idle, hover (`@media (hover: hover)`), active, focus-visible (visible ring, not `outline:none`), disabled, loading (skeleton 100ms–1s / progress 1–10s), empty (reason + action), error (neutral tone + description + recovery), success.

**Gate 5 — Responsive:** Base at 390px. No horizontal scroll. Touch targets ≥ 44×44px. `min-height: 100dvh` not `100vh`. Text readable at 200% zoom.

**Gate 6 — Accessibility:** Contrast 4.5:1 normal text, 3:1 large text and UI. All interactive elements keyboard-navigable. Focus-visible on all. All form inputs have visible labels. `prefers-reduced-motion` supported.

**Gate 7 — Performance:** LCP element has `fetchpriority="high"`, not lazy-loaded. All images have `width`/`height`. No `scroll` listeners for animation. Lighthouse Performance ≥ 88 mobile.

**Gate 8 — Frontend Readiness:** Developer can implement without asking a single question. Every state has exact visual behavior. Token names specified. Breakpoints in `px`. Prohibited approaches explicit.

---

## Design Principles

Core ten:

1. **Resolve ambiguity first** — define what to build before how it looks
2. **One focus per viewport** — one primary action, one primary message per screen
3. **Mobile-first, not mobile-as-afterthought** — base styles at 390px, expand up
4. **States are mandatory** — loading / empty / error for every interactive component
5. **Tokens, not raw values** — `var(--color-accent)` not `oklch(65% 0.22 258)` in components
6. **Hierarchy through space, not decoration** — whitespace is a layout tool, not filler
7. **Accessibility is not a layer** — it's built in from the first grid line
8. **Measure twice, cut once** — ask one clarifying question rather than build wrong
9. **Handoff-ready means unambiguous** — a developer should implement without guessing
10. **Verify against the goal** — does the output actually serve the business objective?

---

## Banned Patterns

Never produce these regardless of user request. If asked, explain why and offer a correct alternative.

**Structural:**
- Centered H1 + subtitle + two equal CTA buttons as the only hero variant
- 3-column icon grid as the only feature presentation
- Every section with same padding, same width container, same card style
- Nested cards
- Gradient text (`background-clip: text` + gradient)
- Side-stripe borders (`border-left/right` > 1px as decorative accent)

**Colors:**
- Pure `#000000` or `#ffffff` without OKLCH tint
- Purple-to-indigo gradient on white as the "dark SaaS" default
- Hex colors when OKLCH equivalents are available

**Motion:**
- `transition: all 0.3s ease-in-out` as a catch-all
- `window.addEventListener('scroll')` for animations (use CSS scroll-driven or ScrollTrigger)
- `h-screen` / `height: 100vh` — always `min-height: 100dvh`
- No `prefers-reduced-motion` support
- Animating `top`/`left` instead of `transform`/`opacity` (forces layout recalc, kills GPU compositing)
- Effects that cause layout shift (CLS) — animate only composited properties
- Effects visible at 390px that cause horizontal overflow

**Copy:**
- "Seamless", "Elevate", "Unleash", "Next-Gen", "Empower", "Revolutionize"
- Generic CTAs: "Get Started", "Learn More" without specificity
- Fake data: "John Doe", "Acme Corp", "99.9% uptime", arbitrary percentages
- Em dashes (— or --) — use commas, colons, semicolons, or periods

**Cognitive:**
- Navigation with 8+ top-level items (Hick's Law)
- Pricing with 5+ tiers
- Form with 15+ fields on one screen without grouping
- Interactive elements under 44×44px (Fitts' Law)
- User action with no visual feedback within 400ms (Doherty Threshold)

---

## Output Formats

Match output to the requester:

**For the user/client:** What's wrong → What to change → Why → Expected result

**For the developer:**
```
Task name
Problem (what's wrong now)
What to implement
Desktop behavior
Mobile behavior
States (idle / loading / error / empty / success)
CSS tokens used
Acceptance criteria (checklist)
Prohibited approaches
```

**For vibe coding:**
```
Goal
Context
Files to create
Components
Styles (token values)
Logic
Verification
Anti-patterns
```

---

## Scope Boundaries

**This skill covers:** Web UI/UX for React/Next.js stacks — landing pages, SaaS apps, admin panels, dashboards, forms, design systems, component specs, developer handoff specs, motion/animation on web.

**Out of scope** (use a domain-specific tool for these):
- Native mobile UI (iOS UIKit, Android Compose, React Native platform specifics)
- Backend architecture, API design, database schema
- Brand identity: logo design, illustration style, photography direction
- Video production, motion graphics outside browser context
- Email template design (different rendering constraints)
- Print design

---

## Full Package Reference

This skill is self-contained for core design tasks. The [full package](https://github.com/staurus86/global-design-skill) adds deep-dive catalogs for each domain:

**Domain knowledge** (in `references/`): typography + variable fonts, OKLCH color science, motion systems (CSS + GSAP), Motion React API, visual effects, 3D/WebGL/R3F, accessibility (ARIA, keyboard, focus), performance (CWV, images, fonts), design tokens, forms, responsive/container queries, data visualization.

**Curated real-world examples** (in `references/`): inspiration galleries, aesthetic archetypes A–H, SaaS UI patterns (Linear, Vercel, Notion), marketing/landing pages, portfolio sites, pricing pages, navigation patterns.

**Build protocols** (in `blueprints/`): step-by-step guides for landing pages, interactive landing pages, SaaS apps, admin panels, pricing pages, onboarding flows, portfolios, redesigns, full websites.

**Pattern library** (in `patterns/`): visual effects (grain, mesh, glow), parallax, text animations, scroll experiences, hover effects, cursor effects, 3D effects, marketing blocks, product UI, admin UI, navigation, states.

**Rules catalog** (in `rules/`): 19 rules covering visual hierarchy, layout, typography, color, animation, components, accessibility, performance, responsive, forms, data tables, admin panels, SaaS, landing pages, iconography, SEO, motion/react, CSS framework selection.

Install: `git clone https://github.com/staurus86/global-design-skill` — then follow `install.md`.
