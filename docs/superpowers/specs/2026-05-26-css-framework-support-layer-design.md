# CSS Framework Support Layer — Design Spec

**Date:** 2026-05-26  
**Status:** Approved  
**Scope:** Add 5 CSS framework profiles + selection router to global-design-skill

---

## Problem

The skill currently assumes Tailwind CSS on every project. When an agent encounters Bootstrap, Bulma, UnoCSS, Panda CSS, or Open Props it has no framework-specific rules to apply and may generate incorrect or mismatched code (wrong class names, missing token patterns, wrong import paths).

---

## Solution

A **CSS Framework Support Layer** consisting of:

1. A **selection router** (`rules/18-css-framework-selection.md`) — auto-detects framework from `package.json`, recommends based on project type, and asks when uncertain
2. **Five framework profiles** (`integrations/frameworks/<name>/profile.md`) — each containing when to use, installation, OKLCH adaptation, typography, animation, banned patterns, and code examples
3. **Minor updates** to `CLAUDE.md`, `blueprints/website-from-scratch.md`, and `blueprints/landing-page-from-scratch.md` to include framework selection in the project start flow

---

## Architecture

```
integrations/
  frameworks/
    bootstrap/profile.md
    bulma/profile.md
    open-props/profile.md
    unocss/profile.md
    panda-css/profile.md

rules/
  18-css-framework-selection.md   ← router (read first on every project)
```

---

## File Specifications

### rules/18-css-framework-selection.md

**Purpose:** Router that determines which framework profile to load.

**Sections:**

#### 1. Auto-Detection (read package.json)

| Dependency | Framework |
|---|---|
| `tailwindcss` | Tailwind (current default) |
| `bootstrap` | Bootstrap |
| `bulma` | Bulma |
| `unocss` | UnoCSS |
| `@pandacss/dev` | Panda CSS |
| `open-props` | Open Props |
| none found | Ask user (see below) |

Detection order: check `dependencies` and `devDependencies`. First match wins.

#### 2. Ask-When-Uncertain Protocol

When no framework is detected (new project or missing package.json), agent asks exactly one question:

> "Which CSS framework are we using? Options: Tailwind (default) / Bootstrap / Bulma / UnoCSS / Panda CSS / Open Props / Other"

If user says "Other" or names an unsupported framework: fall back to generic global-design-skill rules and note the limitation.

#### 3. Recommendation Matrix

| Project type | Auto-recommend |
|---|---|
| React + Next.js, new project, no preference | Tailwind v4 |
| React + Next.js, design system, TypeScript-first | Panda CSS |
| Vanilla HTML, rapid prototype | Bootstrap 5 |
| Vanilla HTML, CSS-only, no JS | Bulma |
| Any stack, custom token system | Open Props |
| Enterprise admin panel, Bootstrap already in org | Bootstrap 5 |
| Migrating from Tailwind to atomic CSS | UnoCSS |

#### 4. Routing Table

After detection, load the corresponding profile:

```
Tailwind   → (default rules apply, no additional profile needed)
Bootstrap  → integrations/frameworks/bootstrap/profile.md
Bulma      → integrations/frameworks/bulma/profile.md
Open Props → integrations/frameworks/open-props/profile.md
UnoCSS     → integrations/frameworks/unocss/profile.md
Panda CSS  → integrations/frameworks/panda-css/profile.md
```

---

### integrations/frameworks/bootstrap/profile.md

**Framework:** Bootstrap 5.3  
**Stack:** Universal (HTML, React, Next.js, Vue)  
**Install:** `npm install bootstrap`

**When to use:**
- Rapid enterprise or admin dashboards
- Teams requiring documented WCAG 2.2 compliance out-of-the-box
- Projects where devs know Bootstrap and onboarding speed matters
- Vanilla HTML without a build step (CDN)

**OKLCH Adaptation:**
Override Bootstrap's CSS custom properties with OKLCH values:
```css
:root {
  --bs-primary: oklch(57% 0.22 258);
  --bs-body-bg: oklch(100% 0.003 258);
  --bs-body-color: oklch(18% 0.02 258);
  --bs-border-radius: var(--radius-md);
}
```
Never use Bootstrap's default `--bs-blue`, `--bs-red` hex values directly.

**Typography:** Bootstrap uses `rem` units natively. Apply `clamp()` on hero headings only:
```css
.display-1 { font-size: clamp(2.5rem, 6vw + 1rem, 5rem); }
```

**Animation:** motion/react compatible — Bootstrap's JS components (modal, dropdown) emit events. Wrap transitions with `AnimatePresence` for React.

**Banned patterns specific to Bootstrap:**
- `btn-primary` with default blue — override with OKLCH primary token
- `text-muted` — contrast often fails WCAG; use explicit OKLCH value
- Bootstrap's gradient utilities (`bg-gradient`) — replace with solid OKLCH tokens
- `shadow-lg` default — replace with OKLCH-based shadow tokens

---

### integrations/frameworks/bulma/profile.md

**Framework:** Bulma 1.0 (released March 2025)  
**Stack:** Universal, CSS-only (zero JavaScript)  
**Install:** `npm install bulma`

**When to use:**
- Projects where zero JavaScript dependency is required
- Clean, readable class names preferred over utility classes
- CSS-only landing pages and marketing sites
- Teams coming from Bootstrap but wanting a lighter footprint

**OKLCH Adaptation:**
Bulma 1.0 uses CSS variables throughout. Override in `:root`:
```css
:root {
  --bulma-primary: oklch(57% 0.22 258);
  --bulma-background: oklch(100% 0.003 258);
  --bulma-text: oklch(18% 0.02 258);
  --bulma-radius: var(--radius-md);
  --bulma-radius-large: var(--radius-lg);
}
```

**Typography:** Bulma uses `em` units. Apply clamp on hero `.title.is-1`:
```css
.hero .title.is-1 {
  font-size: clamp(2.5rem, 6vw + 1rem, 5rem);
}
```

**Animation:** Pure CSS transitions only (Bulma has no JS). Use motion/react for interactive states.

**Banned patterns specific to Bulma:**
- Default `.hero.is-primary` — override with OKLCH primary
- `.has-background-light` — replace with OKLCH token
- Bulma's `$family-sans-serif: BlinkMacSystemFont` — set custom font stack

---

### integrations/frameworks/open-props/profile.md

**Framework:** Open Props (by Adam Argyle, Google Chrome DevRel)  
**Stack:** Universal — pure CSS custom properties, works anywhere  
**Install:** `npm install open-props`

**When to use:**
- Projects building a custom design system from tokens up
- Teams who want OKLCH-native design tokens without a component library
- Augmenting any other framework with a consistent token layer
- Projects where Tailwind/Bootstrap feel like too much opinion

**OKLCH Adaptation:**
Open Props already ships OKLCH-based color tokens. Layer our tokens on top:
```css
@import "open-props/style";
@import "open-props/colors"; /* includes oklch() colors */

:root {
  /* Override with project-specific tokens */
  --accent: oklch(57% 0.22 258);
  --surface-1: oklch(100% 0.003 258);
  --text-1: oklch(18% 0.02 258);
}
```

**Typography:** Use Open Props' `--font-size-*` scale with our `clamp()` override for display sizes:
```css
h1 {
  font-size: var(--font-size-fluid-3); /* already uses clamp() */
}
```

**Easing tokens:** Open Props ships `--ease-spring-*`, `--ease-*` — map to our animation tokens:
```css
--ease-smooth: var(--ease-3);
--ease-spring: var(--ease-spring-3);
```

**Banned patterns:** Open Props has no banned patterns by default — it's a token layer. Apply all standard global-design-skill rules as-is.

---

### integrations/frameworks/unocss/profile.md

**Framework:** UnoCSS  
**Stack:** React, Next.js, Vue, Nuxt, Vite  
**Install:** `npm install -D unocss`

**When to use:**
- Migrating a Tailwind project to a faster, more configurable atomic CSS engine
- Projects needing custom shortcut systems or icon presets
- Monorepos where startup/rebuild speed is critical
- Teams wanting Tailwind compatibility with more flexibility

**OKLCH Adaptation:**
UnoCSS supports OKLCH natively in `uno.config.ts`:
```typescript
import { defineConfig, presetUno } from 'unocss'

export default defineConfig({
  presets: [presetUno()],
  theme: {
    colors: {
      accent: 'oklch(57% 0.22 258)',
      surface: 'oklch(100% 0.003 258)',
      text: 'oklch(18% 0.02 258)',
    },
  },
})
```

**Tailwind compatibility:** Use `presetUno()` for Tailwind-compatible class names. All global-design-skill Tailwind class references work unchanged.

**Typography:** Same clamp() rules apply. UnoCSS supports arbitrary values: `text-[clamp(2rem,5vw,5rem)]`.

**Animation:** motion/react compatible. UnoCSS animation utilities follow same patterns.

**Banned patterns specific to UnoCSS:**
- Dynamic class construction: `"text-" + color` — UnoCSS cannot detect dynamic strings; use full class names
- Avoid mixing UnoCSS and Tailwind in the same project

---

### integrations/frameworks/panda-css/profile.md

**Framework:** Panda CSS (by Chakra UI team)  
**Stack:** React, Next.js (TypeScript-first, zero-runtime CSS-in-JS)  
**Install:** `npm install -D @pandacss/dev && npx panda init`

**When to use:**
- TypeScript-first React/Next.js projects requiring type-safe styles
- Design systems where token contracts must be enforced at compile time
- Teams who want CSS-in-JS DX without runtime overhead
- Projects that want co-located styles with full TypeScript autocomplete

**OKLCH Adaptation:**
Define tokens in `panda.config.ts`:
```typescript
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  theme: {
    tokens: {
      colors: {
        accent: { value: 'oklch(57% 0.22 258)' },
        surface: { value: 'oklch(100% 0.003 258)' },
        textPrimary: { value: 'oklch(18% 0.02 258)' },
      },
      fontSizes: {
        hero: { value: 'clamp(3.5rem, 8vw + 1rem, 12rem)' },
      },
      radii: {
        md: { value: '12px' },
        lg: { value: '16px' },
      },
    },
  },
})
```

Usage with type safety:
```tsx
import { css } from '../styled-system/css'

const heroStyle = css({
  fontSize: 'hero',          // type-checked
  color: 'textPrimary',      // type-checked
  borderRadius: 'md',        // type-checked
})
```

**Banned patterns specific to Panda CSS:**
- Inline style props without token references: `css({ color: '#3b82f6' })` — use token
- Generating classes at runtime with template literals — use static recipes instead
- Mixing Panda CSS with Tailwind in the same component

---

## Updates to Existing Files

### CLAUDE.md — routing table addition

Add row:
```
| CSS framework detection | `rules/18-css-framework-selection.md` |
```

Position: above "Interpret user request depth first" — framework selection happens before design rules.

### blueprints/website-from-scratch.md — Before You Start block

Add to "Resolve These First":
```
CSS framework: [Tailwind / Bootstrap / Bulma / UnoCSS / Panda CSS / Open Props]
```

### blueprints/landing-page-from-scratch.md — Before You Start block

Same addition as above.

---

## Agent Behaviour Contract

**On every new design/build task:**

1. Check `package.json` for framework signals
2. If found → load profile silently, state "Using [framework]" once
3. If not found → ask one question
4. Apply framework profile alongside all global-design-skill rules
5. If framework is unknown → use generic rules, note limitation

**Framework rules do NOT override global-design-skill rules.** They are additive — OKLCH tokens, banned patterns, motion/react, and escalation protocol all still apply.

---

## Out of Scope

- CSS Modules (methodology, not a framework — no profile needed)
- Styled Components / Emotion (runtime CSS-in-JS, no planned support)
- Material UI / Ant Design (component libraries, not CSS frameworks)
- shadcn/ui (built on Tailwind, covered by Tailwind rules)
- Generating setup boilerplate / scaffolding projects (agent installs nothing)

---

## File Count

| Type | Count |
|---|---|
| New profile files | 5 |
| New rules file | 1 |
| Updated files | 3 (CLAUDE.md, 2 blueprints) |
| **Total changes** | **9 files** |

---

## Success Criteria

- Agent correctly identifies framework from `package.json` in ≥95% of cases
- Agent asks exactly one question when framework is unknown
- Each profile provides enough context to generate correct framework-specific code without additional prompting
- All OKLCH token patterns work in each framework
- No global-design-skill rules are broken or overridden by framework profiles
