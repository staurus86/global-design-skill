# CSS Framework Support Layer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 5 CSS framework profiles + a selection router so agents auto-detect or ask which framework a project uses, then apply framework-specific OKLCH/token/animation adaptations alongside all existing global-design-skill rules.

**Architecture:** One router file (`rules/18-css-framework-selection.md`) reads `package.json` signals and routes to one of 5 framework profiles in `integrations/frameworks/<name>/profile.md`. Framework rules are additive — they never override global-design-skill rules. Three existing files get a one-line framework field added to their "Before You Start" blocks.

**Tech Stack:** Markdown only. No code changes to MCP server or Python scripts. Validation via `grep` and internal link checker.

---

## File Map

| Action | Path | Responsibility |
|---|---|---|
| Create | `rules/18-css-framework-selection.md` | Router: auto-detection, ask protocol, recommendation matrix, routing table |
| Create | `integrations/frameworks/bootstrap/profile.md` | Bootstrap 5.3 profile |
| Create | `integrations/frameworks/bulma/profile.md` | Bulma 1.0 profile |
| Create | `integrations/frameworks/open-props/profile.md` | Open Props profile |
| Create | `integrations/frameworks/unocss/profile.md` | UnoCSS profile |
| Create | `integrations/frameworks/panda-css/profile.md` | Panda CSS profile |
| Modify | `CLAUDE.md` | Add CSS framework detection row to routing table |
| Modify | `blueprints/website-from-scratch.md` | Add `CSS framework:` field to Before You Start block |
| Modify | `blueprints/landing-page-from-scratch.md` | Add `CSS framework:` field to Before You Start block |

---

## Task 1: Router — rules/18-css-framework-selection.md

**Files:**
- Create: `rules/18-css-framework-selection.md`

- [ ] **Step 1: Create the router file**

```markdown
# Rule 18 — CSS Framework Selection

> Every project uses a CSS framework. This rule runs first on any design or build task. It detects which framework is in use, routes to the correct profile, and asks when detection fails.

---

## Step 1 — Auto-Detect from package.json

Read `package.json` (both `dependencies` and `devDependencies`). First match wins:

| Detected dependency | Framework |
|---|---|
| `tailwindcss` | Tailwind — no additional profile needed, all global-design-skill rules apply as-is |
| `bootstrap` | Bootstrap → load `integrations/frameworks/bootstrap/profile.md` |
| `bulma` | Bulma → load `integrations/frameworks/bulma/profile.md` |
| `unocss` | UnoCSS → load `integrations/frameworks/unocss/profile.md` |
| `@pandacss/dev` | Panda CSS → load `integrations/frameworks/panda-css/profile.md` |
| `open-props` | Open Props → load `integrations/frameworks/open-props/profile.md` |
| _(none found)_ | → go to Step 2 |

If `package.json` does not exist (new project, repo root, vanilla HTML): → go to Step 2.

---

## Step 2 — Ask When Uncertain

If no framework was detected, ask exactly one question before any design work:

> "Which CSS framework are we using?
> - **Tailwind** (default for React/Next.js)
> - **Bootstrap** (components, enterprise, vanilla)
> - **Bulma** (CSS-only, no JS)
> - **UnoCSS** (Tailwind alternative, faster builds)
> - **Panda CSS** (type-safe, React/Next.js)
> - **Open Props** (token layer, any stack)
> - **Other / none** (vanilla CSS)"

If user answers "Other" or names an unsupported framework: apply all standard global-design-skill rules and note: _"No specific profile for [framework] — applying universal design rules."_

---

## Step 3 — Recommendation Matrix

When starting a brand-new project with no framework installed, recommend based on project type:

| Project type | Recommend |
|---|---|
| React + Next.js, new project | **Tailwind v4** (ecosystem default) |
| React + Next.js, design system, TypeScript | **Panda CSS** (type-safe tokens) |
| Migrating from Tailwind, need more flexibility | **UnoCSS** |
| Vanilla HTML, needs components fast | **Bootstrap 5** |
| Vanilla HTML, CSS-only, no JS budget | **Bulma** |
| Any stack, building custom token system | **Open Props** |
| Enterprise org already using Bootstrap | **Bootstrap 5** |

State your recommendation with one sentence of reasoning. Wait for confirmation before proceeding.

---

## Step 4 — Load Profile

After detection or confirmation, load the profile:

| Framework | Profile path |
|---|---|
| Bootstrap | `integrations/frameworks/bootstrap/profile.md` |
| Bulma | `integrations/frameworks/bulma/profile.md` |
| Open Props | `integrations/frameworks/open-props/profile.md` |
| UnoCSS | `integrations/frameworks/unocss/profile.md` |
| Panda CSS | `integrations/frameworks/panda-css/profile.md` |
| Tailwind | _(no profile — default rules apply)_ |

State once: _"Using [Framework]. Applying framework profile alongside global-design-skill rules."_

---

## Important: Framework Rules Are Additive

Framework profiles do **not** override global-design-skill rules. All of the following always apply regardless of framework:

- OKLCH colors — never raw hex
- `clamp()` for all display type
- `motion/react` for animations — never `framer-motion`
- Escalation protocol (`rules/00-escalation-protocol.md`)
- Accessibility: WCAG 2.2 AA, 44px touch targets, focus-visible
- Banned patterns from `checklists/global-design-review.md`
- Breakpoints: 390px / 768px / 1280px minimum
```

- [ ] **Step 2: Verify file was created with required sections**

```bash
cd "C:\Users\Staurus\Desktop\global-design-skill"
python -c "
content = open('rules/18-css-framework-selection.md').read()
checks = ['Auto-Detect', 'package.json', 'bootstrap', 'bulma', 'unocss', '@pandacss', 'open-props', 'Ask When Uncertain', 'Recommendation Matrix', 'Load Profile', 'Additive']
missing = [c for c in checks if c not in content]
print('MISSING:', missing if missing else 'none')
print('OK' if not missing else 'FAIL')
"
```
Expected: `MISSING: none` and `OK`

- [ ] **Step 3: Commit**

```bash
git add rules/18-css-framework-selection.md
git commit -m "feat: add CSS framework selection router (rule 18)"
```

---

## Task 2: Bootstrap Profile

**Files:**
- Create: `integrations/frameworks/bootstrap/profile.md`

- [ ] **Step 1: Create Bootstrap profile**

```markdown
# Bootstrap 5.3 — Framework Profile

> Bootstrap is the most widely deployed CSS framework. Best for enterprise dashboards, admin panels, and projects where teams need documented WCAG 2.2 compliance and 30+ pre-built components with zero custom design work.

**Auto-detected via:** `"bootstrap"` in package.json  
**Install:** `npm install bootstrap`  
**CDN (no build step):** `<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3/dist/css/bootstrap.min.css">`

---

## When to Use Bootstrap

- Enterprise or government projects requiring documented accessibility compliance
- Admin dashboards where dev speed > design uniqueness
- Teams already trained on Bootstrap — no ramp-up
- Rapid prototypes needing 30+ components out of the box
- Projects that must support IE-era browsers (Bootstrap's grid is widest-compatibility)

**Do not choose Bootstrap when:** design differentiation matters, you want utility-first workflow, or you're building a consumer-facing product where "Bootstrap look" is a liability.

---

## OKLCH Adaptation

Override Bootstrap's CSS custom properties with OKLCH values in your `globals.css`:

```css
:root {
  /* Replace Bootstrap hex defaults with OKLCH tokens */
  --bs-primary:          oklch(57% 0.22 258);
  --bs-primary-rgb:      /* leave as-is for Bootstrap JS components */;
  --bs-body-bg:          oklch(100% 0.003 258);
  --bs-body-color:       oklch(18% 0.02 258);
  --bs-secondary-color:  oklch(45% 0.02 258);
  --bs-border-color:     oklch(88% 0.01 258);
  --bs-border-radius:    var(--radius-md, 12px);
  --bs-border-radius-lg: var(--radius-lg, 16px);
  --bs-border-radius-sm: var(--radius-sm, 8px);
}
```

**Never use Bootstrap's default color utilities directly:**
```html
<!-- BANNED — raw Bootstrap color -->
<button class="btn btn-primary">CTA</button>

<!-- OK — after OKLCH override above, btn-primary uses your token -->
<button class="btn btn-primary">CTA</button>
```
The token override makes the class safe. Forbidden: adding explicit `style="background:#0d6efd"`.

---

## Typography

Bootstrap uses `rem` units. Apply `clamp()` only on hero headings — Bootstrap's scale is fine for body text:

```css
/* Override display headings with clamp() */
.display-1 { font-size: clamp(3rem,  7vw + 1rem, 5rem);   line-height: 1.1; }
.display-2 { font-size: clamp(2.5rem, 6vw + 1rem, 4.5rem); line-height: 1.1; }
.display-3 { font-size: clamp(2rem,   5vw + 1rem, 4rem);   line-height: 1.1; }

/* Ensure body text ≥ 16px (Bootstrap default is 1rem — OK) */
/* Ensure form inputs ≥ 16px to prevent iOS zoom */
.form-control { font-size: 1rem; }
```

Banned Bootstrap font utilities: `.display-*` with fixed `px` overrides — use `clamp()` above.

---

## Animation with motion/react

Bootstrap's JS components (modal, collapse, dropdown, toast) emit events. Wire `motion/react` to those events in React:

```tsx
import { motion, AnimatePresence } from 'motion/react'

// Animate Bootstrap modal content (not the backdrop)
function AnimatedModal({ show, children }: { show: boolean; children: React.ReactNode }) {
  return (
    <AnimatePresence>
      {show && (
        <motion.div
          initial={{ opacity: 0, scale: 0.96, y: 8 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.96, y: 8 }}
          transition={{ duration: 0.2, ease: 'easeOut' }}
        >
          {children}
        </motion.div>
      )}
    </AnimatePresence>
  )
}
```

For vanilla Bootstrap (no React): use Bootstrap's built-in CSS transitions — they are reduced-motion safe.

---

## Banned Patterns (Bootstrap-Specific)

| Banned | Problem | Replacement |
|---|---|---|
| `btn btn-primary` without OKLCH override | Default blue hex | Override `--bs-primary` first |
| `text-muted` | Often fails 4.5:1 contrast | Use explicit OKLCH value |
| `bg-gradient` utility | Decorative noise | Solid OKLCH background |
| `shadow-lg` default | Generic appearance | `box-shadow: 0 4px 24px oklch(0% 0 0 / 0.08)` |
| `col-*` with no responsive variant | Breaks on mobile | Always pair with `col-md-*` or `col-lg-*` |
| Bootstrap's `$primary` Sass variable | Overridden by CSS custom property — use CSS layer | Set `--bs-primary` in `:root` |

---

## Checklist

- [ ] `--bs-primary` overridden with OKLCH token
- [ ] `--bs-body-bg` and `--bs-body-color` use OKLCH
- [ ] `display-*` headings use `clamp()`
- [ ] No `text-muted` — replaced with OKLCH value
- [ ] No `bg-gradient` utilities
- [ ] `motion/react` used for interactive animations, not Bootstrap JS transitions
- [ ] Lighthouse accessibility ≥ 90 (Bootstrap's defaults usually pass — verify overrides didn't break contrast)
```

- [ ] **Step 2: Verify**

```bash
cd "C:\Users\Staurus\Desktop\global-design-skill"
python -c "
content = open('integrations/frameworks/bootstrap/profile.md').read()
checks = ['OKLCH', 'clamp()', 'motion/react', 'Banned Patterns', 'Checklist', '--bs-primary']
missing = [c for c in checks if c not in content]
print('MISSING:', missing if missing else 'none — OK')
"
```

- [ ] **Step 3: Commit**

```bash
git add integrations/frameworks/bootstrap/profile.md
git commit -m "feat: add Bootstrap 5.3 framework profile"
```

---

## Task 3: Bulma Profile

**Files:**
- Create: `integrations/frameworks/bulma/profile.md`

- [ ] **Step 1: Create Bulma profile**

```markdown
# Bulma 1.0 — Framework Profile

> Bulma is a modern CSS-only framework — zero JavaScript. Version 1.0 (released March 2025) rewrote the entire variable system to CSS custom properties. Best for vanilla HTML projects, static sites, and projects where JS bundle size is constrained.

**Auto-detected via:** `"bulma"` in package.json  
**Install:** `npm install bulma`  
**CDN:** `<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@1.0/css/bulma.min.css">`

---

## When to Use Bulma

- Vanilla HTML/CSS projects with no framework or build step
- Static site generators (Hugo, Jekyll, Eleventy)
- Developers who want readable, English-like class names over utility classes
- Projects where zero JavaScript dependency is a hard requirement
- Landing pages and marketing sites that don't need React

**Do not choose Bulma when:** you need interactive JS components (modals, dropdowns), you're in a React/Next.js project, or you need a large component library.

---

## OKLCH Adaptation

Bulma 1.0 uses CSS custom properties throughout. Override in `:root`:

```css
@import 'bulma/css/bulma.css';

:root {
  --bulma-primary:        oklch(57% 0.22 258);
  --bulma-primary-light:  oklch(92% 0.06 258);
  --bulma-primary-dark:   oklch(38% 0.20 258);
  --bulma-background:     oklch(100% 0.003 258);
  --bulma-text:           oklch(18% 0.02 258);
  --bulma-text-light:     oklch(45% 0.02 258);
  --bulma-border:         oklch(88% 0.01 258);
  --bulma-radius:         var(--radius-md, 12px);
  --bulma-radius-large:   var(--radius-lg, 16px);
  --bulma-radius-small:   var(--radius-sm, 8px);
}
```

---

## Typography

Bulma uses `em` units. Override hero `.title` sizes with `clamp()`:

```css
.hero .title.is-1 {
  font-size: clamp(2.5rem, 6vw + 1rem, 5rem);
  line-height: 1.1;
}
.hero .title.is-2 {
  font-size: clamp(2rem, 4vw + 1rem, 4rem);
  line-height: 1.15;
}
/* Body text — Bulma default is 1em = 16px — acceptable */
/* Ensure inputs don't trigger iOS zoom */
.input, .textarea, .select select {
  font-size: 1rem;
}
```

---

## Animation

Bulma has zero built-in JavaScript animations. Use `motion/react` for interactive states, or CSS `@starting-style` for pure CSS entry animations:

```css
/* Pure CSS entry — no JS needed */
.card {
  transition: opacity 0.3s ease, transform 0.3s ease;

  @starting-style {
    opacity: 0;
    transform: translateY(12px);
  }
}
```

For interactive React components using Bulma classes with motion/react:
```tsx
import { motion } from 'motion/react'

<motion.div
  className="card"
  initial={{ opacity: 0, y: 16 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true }}
  transition={{ duration: 0.4, ease: 'easeOut' }}
>
```

---

## Banned Patterns (Bulma-Specific)

| Banned | Problem | Replacement |
|---|---|---|
| `.is-primary` without OKLCH override | Default blue | Set `--bulma-primary` first |
| `.has-text-grey-light` | Often fails contrast | Explicit OKLCH value |
| `.has-background-light` | Hex default | Override `--bulma-background` |
| Bulma's default font stack (BlinkMacSystemFont) | Generic | Set `--bulma-family-primary` to your font |
| Nested `.columns` more than 2 levels | Layout confusion | Flatten structure |

---

## Checklist

- [ ] `--bulma-primary` overridden with OKLCH token
- [ ] `--bulma-background` and `--bulma-text` use OKLCH
- [ ] `.title.is-1` / `.is-2` use `clamp()`
- [ ] No `.has-text-grey-light` — replaced with OKLCH value
- [ ] Inputs have `font-size: 1rem` (iOS zoom prevention)
- [ ] CSS `@starting-style` used for entry animations (no JS needed)
- [ ] motion/react used only when React is in the stack
```

- [ ] **Step 2: Verify**

```bash
cd "C:\Users\Staurus\Desktop\global-design-skill"
python -c "
content = open('integrations/frameworks/bulma/profile.md').read()
checks = ['OKLCH', 'clamp()', '@starting-style', 'Banned Patterns', 'Checklist', '--bulma-primary']
missing = [c for c in checks if c not in content]
print('MISSING:', missing if missing else 'none — OK')
"
```

- [ ] **Step 3: Commit**

```bash
git add integrations/frameworks/bulma/profile.md
git commit -m "feat: add Bulma 1.0 framework profile"
```

---

## Task 4: Open Props Profile

**Files:**
- Create: `integrations/frameworks/open-props/profile.md`

- [ ] **Step 1: Create Open Props profile**

```markdown
# Open Props — Framework Profile

> Open Props (by Adam Argyle, Google Chrome DevRel) is a CSS custom properties token library — not a component framework. It ships 300+ design tokens including OKLCH-native color palettes, fluid typography, easing functions, and animation keyframes. Works with any stack as a token foundation layer.

**Auto-detected via:** `"open-props"` in package.json  
**Install:** `npm install open-props`  
**CDN:** `@import "https://unpkg.com/open-props"`

---

## When to Use Open Props

- Building a custom design system from tokens up (no component opinions)
- Augmenting any other framework with a consistent token layer
- Projects where Tailwind/Bootstrap feel like too much framework opinion
- Designers who want OKLCH colors, fluid type, and spring easings ready-made
- Vanilla CSS projects that want a professional token system without a build step

**Do not choose Open Props as your only tool when:** you need pre-built interactive components — pair it with a component library or build your own.

---

## OKLCH Adaptation

Open Props already ships OKLCH color tokens (`--pink-5`, `--blue-7`, etc.). Layer your project tokens on top:

```css
@import "open-props/style";      /* core tokens */
@import "open-props/colors";     /* oklch() color palette */
@import "open-props/sizes";      /* spacing scale */
@import "open-props/fonts";      /* fluid font sizes */
@import "open-props/easings";    /* spring and easing functions */

:root {
  /* Override or extend with project-specific tokens */
  --color-accent:   oklch(57% 0.22 258);
  --color-surface:  oklch(100% 0.003 258);
  --color-text:     oklch(18% 0.02 258);

  /* Map Open Props easings to global-design-skill tokens */
  --ease-smooth:  var(--ease-3);
  --ease-spring:  var(--ease-spring-3);
  --ease-bounce:  var(--ease-elastic-3);
}
```

**Never use Open Props color tokens directly in components** — always map through your project tokens first. This ensures your OKLCH values stay consistent even if Open Props changes.

---

## Typography

Open Props ships fluid font sizes that already use `clamp()`:

```css
/* Open Props fluid scale — already clamp() */
--font-size-0:  clamp(.75rem, 2vw, 1rem);
--font-size-1:  clamp(1rem,   2vw, 1.1rem);
--font-size-6:  clamp(2.5rem, 6vw, 4rem);
--font-size-7:  clamp(3rem,   7vw, 5rem);
--font-size-8:  clamp(3.75rem, 8vw, 6.5rem);
```

Map to global-design-skill typography tokens:
```css
:root {
  --text-hero:    var(--font-size-8);   /* clamp(3.75rem, 8vw, 6.5rem) */
  --text-section: var(--font-size-6);   /* clamp(2.5rem, 6vw, 4rem) */
  --text-body:    var(--font-size-1);   /* 1rem min */
}
```

---

## Animation

Open Props ships animation keyframes and easing tokens — combine with `motion/react`:

```css
/* Use Open Props keyframes in CSS */
.card {
  animation: var(--animation-fade-in);
  animation-duration: 0.4s;
  animation-timing-function: var(--ease-3);
}
```

```tsx
// Use Open Props easing in motion/react
import { motion } from 'motion/react'

<motion.div
  initial={{ opacity: 0, y: 16 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{
    duration: 0.4,
    ease: [0.25, 0.1, 0.25, 1] // var(--ease-3) value
  }}
/>
```

---

## Banned Patterns (Open Props-Specific)

| Banned | Problem | Replacement |
|---|---|---|
| Using `--pink-5` directly in components | Breaks token abstraction | Map to `--color-accent` first |
| Importing all of Open Props | Unused tokens add weight | Import only needed modules |
| Mixing Open Props font scale with Tailwind font scale | Conflicting values | Use one scale only |

---

## Checklist

- [ ] Open Props imported modularly (only needed files)
- [ ] Project tokens defined that map from Open Props tokens
- [ ] `--ease-smooth` and `--ease-spring` mapped to Open Props equivalents
- [ ] Fluid font sizes mapped to global-design-skill typography tokens
- [ ] No Open Props color tokens used directly in components (mapped through project tokens)
```

- [ ] **Step 2: Verify**

```bash
cd "C:\Users\Staurus\Desktop\global-design-skill"
python -c "
content = open('integrations/frameworks/open-props/profile.md').read()
checks = ['OKLCH', 'clamp()', 'motion/react', 'Banned Patterns', 'Checklist', '--ease-spring']
missing = [c for c in checks if c not in content]
print('MISSING:', missing if missing else 'none — OK')
"
```

- [ ] **Step 3: Commit**

```bash
git add integrations/frameworks/open-props/profile.md
git commit -m "feat: add Open Props framework profile"
```

---

## Task 5: UnoCSS Profile

**Files:**
- Create: `integrations/frameworks/unocss/profile.md`

- [ ] **Step 1: Create UnoCSS profile**

```markdown
# UnoCSS — Framework Profile

> UnoCSS is an atomic CSS engine — the architecture behind Tailwind but faster, more configurable, and with a richer preset ecosystem. With `presetUno()`, all Tailwind class names work unchanged. Best for teams migrating from Tailwind or building monorepos where build speed matters.

**Auto-detected via:** `"unocss"` in package.json  
**Install:** `npm install -D unocss`

---

## When to Use UnoCSS

- Migrating a Tailwind project to a faster build engine (Tailwind class names work as-is)
- Monorepos where Tailwind's full rebuild is slow
- Projects needing custom atomic class generators (shortcuts, rules)
- Vue/Nuxt projects where UnoCSS has first-class integration
- Teams who want icon sets as CSS classes (`@unocss/preset-icons`)

**Do not choose UnoCSS when:** your team knows only Tailwind and the project is small — Tailwind v4 is fast enough and has wider community resources.

---

## Setup

```typescript
// uno.config.ts
import { defineConfig, presetUno } from 'unocss'

export default defineConfig({
  presets: [
    presetUno(), // Tailwind-compatible class names
  ],
  theme: {
    colors: {
      accent:  'oklch(57% 0.22 258)',
      surface: 'oklch(100% 0.003 258)',
      text:    'oklch(18% 0.02 258)',
      border:  'oklch(88% 0.01 258)',
    },
    borderRadius: {
      sm: '8px',
      md: '12px',
      lg: '16px',
    },
  },
})
```

```typescript
// vite.config.ts / next.config.ts
import UnoCSS from 'unocss/vite'
export default { plugins: [UnoCSS()] }
```

---

## OKLCH Adaptation

UnoCSS resolves colors through its theme config. All OKLCH values defined in `theme.colors` are available as utility classes:

```html
<!-- Uses oklch(57% 0.22 258) defined in theme -->
<div class="bg-accent text-surface">
<button class="bg-accent hover:bg-accent/90 text-surface rounded-md">
```

Arbitrary OKLCH values:
```html
<div class="bg-[oklch(57%_0.22_258)]">
```

**CSS custom properties in UnoCSS:**
```typescript
// uno.config.ts — output CSS variables
shortcuts: {
  'btn-primary': 'bg-accent text-surface rounded-md px-6 py-3 hover:bg-accent/90',
}
```

---

## Typography

UnoCSS supports arbitrary `clamp()` values natively:

```html
<h1 class="text-[clamp(3.5rem,8vw+1rem,12rem)] leading-[1.1]">
```

Or define in theme:
```typescript
theme: {
  fontSize: {
    hero:    ['clamp(3.5rem, 8vw + 1rem, 12rem)',    { lineHeight: '1.1' }],
    section: ['clamp(2rem,   4vw + 1rem, 3.5rem)',   { lineHeight: '1.2' }],
    body:    ['1rem',                                 { lineHeight: '1.65' }],
  },
}
```

Usage: `<h1 class="text-hero">`

---

## Banned Patterns (UnoCSS-Specific)

| Banned | Problem | Replacement |
|---|---|---|
| Dynamic class construction: `"text-" + color` | UnoCSS can't detect at build time | Use full class name `text-accent` |
| Mixing UnoCSS and Tailwind in same project | Class conflicts | Choose one |
| `presetWind()` + `presetUno()` together | Duplicate rules | Use `presetUno()` only for Tailwind compat |
| Inline arbitrary values for every property | Defeats the purpose of a theme | Define tokens in `uno.config.ts` |

---

## Checklist

- [ ] `uno.config.ts` has OKLCH color tokens in `theme.colors`
- [ ] `presetUno()` included for Tailwind class compatibility
- [ ] Hero font sizes defined in `theme.fontSize` with `clamp()`
- [ ] No dynamic class string construction
- [ ] `motion/react` used for animations — not UnoCSS animation utilities for complex interactions
- [ ] No Tailwind installed alongside UnoCSS
```

- [ ] **Step 2: Verify**

```bash
cd "C:\Users\Staurus\Desktop\global-design-skill"
python -c "
content = open('integrations/frameworks/unocss/profile.md').read()
checks = ['OKLCH', 'clamp()', 'presetUno', 'Banned Patterns', 'Checklist', 'uno.config.ts']
missing = [c for c in checks if c not in content]
print('MISSING:', missing if missing else 'none — OK')
"
```

- [ ] **Step 3: Commit**

```bash
git add integrations/frameworks/unocss/profile.md
git commit -m "feat: add UnoCSS framework profile"
```

---

## Task 6: Panda CSS Profile

**Files:**
- Create: `integrations/frameworks/panda-css/profile.md`

- [ ] **Step 1: Create Panda CSS profile**

```markdown
# Panda CSS — Framework Profile

> Panda CSS (by the Chakra UI team) is a type-safe, zero-runtime CSS-in-JS framework for React and Next.js. Styles are co-located with components, tokens are fully typed with TypeScript autocomplete, and the output is static CSS — no runtime overhead. Best for teams building design systems where token contracts must be enforced at compile time.

**Auto-detected via:** `"@pandacss/dev"` in package.json  
**Install:** `npm install -D @pandacss/dev && npx panda init --postcss`

---

## When to Use Panda CSS

- TypeScript-first React/Next.js projects requiring type-safe design tokens
- Teams building a component library where token misuse should be a compile error
- Projects moving away from runtime CSS-in-JS (Styled Components, Emotion) for performance
- Design systems where token contracts between design and dev must be machine-enforced

**Do not choose Panda CSS when:** the team is not using TypeScript, the project is vanilla HTML, or fast setup is more important than type safety.

---

## Setup

```typescript
// panda.config.ts
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  preflight: true,
  include: ['./src/**/*.{ts,tsx}'],
  exclude: [],
  outdir: 'styled-system',
  theme: {
    tokens: {
      colors: {
        accent:      { value: 'oklch(57% 0.22 258)' },
        surface:     { value: 'oklch(100% 0.003 258)' },
        textPrimary: { value: 'oklch(18% 0.02 258)' },
        textMuted:   { value: 'oklch(45% 0.02 258)' },
        border:      { value: 'oklch(88% 0.01 258)' },
      },
      fontSizes: {
        hero:    { value: 'clamp(3.5rem, 8vw + 1rem, 12rem)' },
        section: { value: 'clamp(2rem, 4vw + 1rem, 3.5rem)' },
        body:    { value: '1rem' },
      },
      radii: {
        sm: { value: '8px' },
        md: { value: '12px' },
        lg: { value: '16px' },
      },
      easings: {
        smooth: { value: 'cubic-bezier(0.25, 0.1, 0.25, 1)' },
        spring: { value: 'cubic-bezier(0.16, 1, 0.3, 1)' },
      },
    },
  },
})
```

```json
// package.json — add prepare script
{
  "scripts": {
    "prepare": "panda codegen"
  }
}
```

---

## OKLCH Adaptation

All OKLCH values are defined once in `panda.config.ts`. Components reference tokens by name — no raw values in component code:

```tsx
import { css } from '../styled-system/css'

// Type-safe — 'accent' autocompletes from your token definition
const heroStyle = css({
  fontSize: 'hero',
  color: 'textPrimary',
  background: 'surface',
  borderRadius: 'md',
})

// Semantic recipes for repeated patterns
import { cva } from '../styled-system/css'

const button = cva({
  base: {
    borderRadius: 'md',
    fontSize: 'body',
    cursor: 'pointer',
  },
  variants: {
    intent: {
      primary:   { background: 'accent', color: 'surface' },
      secondary: { border: '2px solid token(colors.accent)', color: 'accent' },
    },
  },
})
```

---

## Typography

Font sizes are type-checked through the token system. `clamp()` is defined once in the config, used everywhere via token name:

```tsx
// hero, section, body are token names — TypeScript autocompletes them
<h1 className={css({ fontSize: 'hero', lineHeight: '1.1' })}>
<h2 className={css({ fontSize: 'section', lineHeight: '1.2' })}>
<p  className={css({ fontSize: 'body', lineHeight: '1.65' })}>
```

---

## Animation with motion/react

Panda CSS handles static styles. Use `motion/react` for all animations — the two systems are fully compatible:

```tsx
import { motion } from 'motion/react'
import { css } from '../styled-system/css'

const cardStyle = css({
  borderRadius: 'lg',
  background: 'surface',
  border: '1px solid token(colors.border)',
})

<motion.div
  className={cardStyle}
  initial={{ opacity: 0, y: 16 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true }}
  transition={{ duration: 0.4, ease: 'easeOut' }}
>
```

---

## Banned Patterns (Panda CSS-Specific)

| Banned | Problem | Replacement |
|---|---|---|
| Raw OKLCH in `css()` calls: `{ color: 'oklch(57% 0.22 258)' }` | Bypasses token system | Use `{ color: 'accent' }` |
| Dynamic template literal class generation | Panda can't statically analyze | Use `cva` recipes with explicit variants |
| Mixing Panda CSS with Tailwind | Class conflicts, bloated output | Choose one |
| Skipping `panda codegen` after token changes | Type definitions go stale | Run `panda codegen` in `prepare` script |

---

## Checklist

- [ ] `panda.config.ts` has all OKLCH colors as named tokens
- [ ] `clamp()` font sizes defined as tokens, not inline values
- [ ] `prepare` script runs `panda codegen`
- [ ] No raw OKLCH values in component `css()` calls — all through token names
- [ ] `motion/react` used for animations
- [ ] No Tailwind installed alongside Panda CSS
- [ ] TypeScript autocomplete working for token names in `css()` calls
```

- [ ] **Step 2: Verify**

```bash
cd "C:\Users\Staurus\Desktop\global-design-skill"
python -c "
content = open('integrations/frameworks/panda-css/profile.md').read()
checks = ['OKLCH', 'clamp()', 'motion/react', 'Banned Patterns', 'Checklist', 'panda.config.ts', 'cva']
missing = [c for c in checks if c not in content]
print('MISSING:', missing if missing else 'none — OK')
"
```

- [ ] **Step 3: Commit**

```bash
git add integrations/frameworks/panda-css/profile.md
git commit -m "feat: add Panda CSS framework profile"
```

---

## Task 7: Update CLAUDE.md

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Add CSS framework detection as first routing row**

In `CLAUDE.md`, replace:

```markdown
| Task | Resource |
|---|---|
| Interpret user request depth first | `rules/00-escalation-protocol.md` |
```

With:

```markdown
| Task | Resource |
|---|---|
| CSS framework detection (run first) | `rules/18-css-framework-selection.md` |
| Interpret user request depth first | `rules/00-escalation-protocol.md` |
```

- [ ] **Step 2: Verify**

```bash
cd "C:\Users\Staurus\Desktop\global-design-skill"
python -c "
content = open('CLAUDE.md').read()
assert 'rules/18-css-framework-selection.md' in content, 'MISSING: framework selection row'
lines = content.split('\n')
fw_line = next(i for i,l in enumerate(lines) if '18-css-framework' in l)
esc_line = next(i for i,l in enumerate(lines) if '00-escalation' in l)
assert fw_line < esc_line, f'Framework row ({fw_line}) must come before escalation row ({esc_line})'
print('OK — framework row is first in routing table')
"
```

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: add CSS framework detection as first routing step in CLAUDE.md"
```

---

## Task 8: Update Blueprints

**Files:**
- Modify: `blueprints/website-from-scratch.md`
- Modify: `blueprints/landing-page-from-scratch.md`

- [ ] **Step 1: Add framework field to website-from-scratch.md**

In `blueprints/website-from-scratch.md`, find the "Before You Start" code block:

```
Business type: [SaaS / Agency / Product / Service / Content]
Primary visitor intent: [learn / evaluate / contact / buy / read]
Primary conversion goal: [trial / contact / purchase / newsletter / download]
Content volume: [landing-only / 5-10 pages / 20+ pages with blog]
SEO priority: [low / medium / high — determines content architecture]
Brand maturity: [new brand / established brand with guidelines]
```

Add one line at the end of that block:

```
CSS framework:  [Tailwind / Bootstrap / Bulma / UnoCSS / Panda CSS / Open Props]
```

- [ ] **Step 2: Add framework field to landing-page-from-scratch.md**

In `blueprints/landing-page-from-scratch.md`, find the "Before You Start" block:

```
User: [role] using [device] at [moment in their day]
Goal: [one measurable outcome — signups, trials, purchases]
Primary CTA: [exact label + destination]
Offer: [what the user gets + at what cost/commitment]
Differentiator: [one thing this does that alternatives don't]
```

Add one line at the end:

```
CSS framework:  [Tailwind / Bootstrap / Bulma / UnoCSS / Panda CSS / Open Props]
```

- [ ] **Step 3: Verify both files**

```bash
cd "C:\Users\Staurus\Desktop\global-design-skill"
python -c "
for f in ['blueprints/website-from-scratch.md', 'blueprints/landing-page-from-scratch.md']:
    content = open(f).read()
    if 'CSS framework' in content:
        print(f'OK  {f}')
    else:
        print(f'MISSING  {f}')
"
```

- [ ] **Step 4: Commit**

```bash
git add blueprints/website-from-scratch.md blueprints/landing-page-from-scratch.md
git commit -m "docs: add CSS framework field to website and landing page blueprints"
```

---

## Task 9: Update README + Push

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Add frameworks to integrations tree in README**

Find in `README.md`:

```
├── integrations/                   ← 9 AI tool configuration files
```

Replace with:

```
├── integrations/                   ← 10 AI tool + framework configuration files
│   ├── frameworks/                 ← CSS framework profiles (5 frameworks)
│   │   ├── bootstrap/profile.md   ← Bootstrap 5.3 OKLCH adaptation
│   │   ├── bulma/profile.md       ← Bulma 1.0 CSS-only
│   │   ├── open-props/profile.md  ← Token layer, any stack
│   │   ├── unocss/profile.md      ← Tailwind-compatible atomic CSS
│   │   └── panda-css/profile.md   ← Type-safe React/Next.js
```

- [ ] **Step 2: Add rules/18 to rules tree in README**

Find in `README.md`:

```
├── rules/                          ← 18 domain rules files
```

Replace with:

```
├── rules/                          ← 19 domain rules files
```

- [ ] **Step 3: Final link validation**

```bash
cd "C:\Users\Staurus\Desktop\global-design-skill"
python -c "
import os
files = [
    'rules/18-css-framework-selection.md',
    'integrations/frameworks/bootstrap/profile.md',
    'integrations/frameworks/bulma/profile.md',
    'integrations/frameworks/open-props/profile.md',
    'integrations/frameworks/unocss/profile.md',
    'integrations/frameworks/panda-css/profile.md',
]
for f in files:
    print(f'  {\"OK\" if os.path.exists(f) else \"MISSING\"} {f}')
"
```

Expected: all `OK`

- [ ] **Step 4: Commit + push**

```bash
git add README.md
git commit -m "docs: update README with CSS framework profiles in integrations tree"
git push origin master
```
