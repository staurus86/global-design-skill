# Design Tokens — Usage Guide

> The token system is the single source of truth for all visual values. A component that uses a raw hex, pixel value, or hardcoded opacity is a bug. Every visual decision is a token.

---

## Quick Start

```css
/* In your main CSS entry point */
@import './tokens/tokens.css';
@import './tokens/tokens-dark.css';  /* if dark mode is needed */
```

```html
<!-- In <head>, before CSS — prevents dark mode flash -->
<script>
  const stored = localStorage.getItem('theme')
  const system = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  document.documentElement.setAttribute('data-theme', stored ?? system)
</script>
```

---

## Token Categories

| File | Contents |
|---|---|
| `tokens.css` | All tokens: colors, spacing, typography, radius, shadow, animation, z-index, layout, component aliases |
| `tokens-dark.css` | Dark mode semantic overrides, component tweaks, theme-transition class |
| `design-tokens.json` | W3C DTCG format — source of truth for tooling (Style Dictionary, Tokens Studio) |

---

## Color Tokens

### Two-layer system

**Primitive tokens** — raw OKLCH values. Never use in components.
```css
--color-accent-500:  oklch(65% 0.22 258);
--color-neutral-100: oklch(97% 0.007 258);
```

**Semantic tokens** — contextual meaning. Use ONLY these in components.
```css
--color-base        /* page background */
--color-surface     /* card, panel, dialog */
--color-surface-2   /* input bg, hover bg, nested surface */
--color-border      /* dividers, card borders, input borders */

--color-text-primary    /* headlines, body */
--color-text-secondary  /* supporting text */
--color-text-muted      /* labels, captions, timestamps */

--color-accent      /* links, CTAs, focus rings, active states */
--color-accent-bg   /* accent-tinted backgrounds */

--color-success / --color-success-bg
--color-warning / --color-warning-bg
--color-error   / --color-error-bg
--color-info    / --color-info-bg     /* cyan — informational, distinct from accent */
```

### Usage examples
```css
/* Correct */
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  color: var(--color-text-primary);
}

/* Wrong — hardcoded hex */
.card {
  background: #ffffff;
  border: 1px solid #e5e7eb;
}

/* Wrong — using primitive token in component */
.card {
  background: var(--color-neutral-0);  /* use --color-surface instead */
}
```

### Color-mix for alpha variants
```css
/* Tint a semantic color */
background: oklch(from var(--color-accent) l c h / 0.1);   /* 10% opacity */
background: oklch(from var(--color-error)  l c h / 0.08);  /* 8% opacity */

/* Lighten/darken relative to current theme */
background: color-mix(in oklch, var(--color-surface) 80%, var(--color-accent));
```

---

## Spacing Tokens

All spacing is the 4px base grid. Token name = multiplier of 4.

```
--space-1  =  4px    --space-10 = 40px
--space-2  =  8px    --space-11 = 44px  (touch target minimum)
--space-3  = 12px    --space-12 = 48px
--space-4  = 16px    --space-14 = 56px  (bottom nav height)
--space-5  = 20px    --space-16 = 64px
--space-6  = 24px    --space-20 = 80px
--space-7  = 28px    --space-24 = 96px
--space-8  = 32px    --space-32 = 128px
--space-9  = 36px
```

**Usage:**
```css
.card  { padding: var(--space-6); }         /* 24px */
.input { height: var(--space-11); }         /* 44px — touch target */
.gap   { gap: var(--space-4); }             /* 16px */
.icon  { width: var(--space-5); height: var(--space-5); }  /* 20px */
```

---

## Typography Tokens

### Fluid scale — display sizes
```css
font-size: var(--text-hero);    /* clamp(3.5rem, 8vw + 1rem, 12rem) — landing H1 */
font-size: var(--text-display); /* clamp(2.5rem, 5vw + 0.5rem, 7rem) — section hero */
font-size: var(--text-h1);      /* clamp(2rem, 4vw + 0.25rem, 4.5rem) */
font-size: var(--text-h2);      /* clamp(1.75rem, 3vw + 0.5rem, 4rem) */
font-size: var(--text-h3);      /* clamp(1.25rem, 2vw + 0.25rem, 2rem) */
font-size: var(--text-body);    /* clamp(1rem, 1.2vw + 0.4rem, 1.2rem) */
font-size: var(--text-sm);      /* 0.9375rem — 15px */
font-size: var(--text-xs);      /* 0.875rem — 14px */
font-size: var(--text-2xs);     /* 0.8125rem — 13px */
font-size: var(--text-3xs);     /* 0.75rem — 12px */
```

### Letter spacing guide
```css
/* Large display (> 48px) */
letter-spacing: var(--tracking-tighter);  /* -0.04em */

/* Medium display (32–48px) */
letter-spacing: var(--tracking-tight);    /* -0.03em */

/* Headings (24–32px) */
letter-spacing: var(--tracking-snug);     /* -0.02em */

/* Body text */
letter-spacing: var(--tracking-normal);   /* 0 */

/* Uppercase labels, table headers */
letter-spacing: var(--tracking-wider);    /* 0.06em */

/* Eyebrow tags (uppercase, tiny) */
letter-spacing: var(--tracking-widest);   /* 0.12em */
```

---

## Border Radius Tokens

```
--radius-none  = 0       —  no rounding
--radius-sm    = 4px     —  checkboxes, small indicators
--radius-md    = 8px     —  buttons, inputs, dropdowns, small cards
--radius-lg    = 12px    —  standard cards, panels
--radius-xl    = 16px    —  large cards, modals, drawers
--radius-2xl   = 24px    —  hero containers, featured sections
--radius-3xl   = 32px    —  large marketing cards
--radius-full  = 9999px  —  pills, tags, badge chips
```

---

## Shadow Tokens

Light mode: multi-layer box-shadow with OKLCH black.
Dark mode: automatically switches to `border + depth` via `tokens-dark.css`.

```css
box-shadow: var(--shadow-xs);   /* form inputs, subtle lift */
box-shadow: var(--shadow-sm);   /* default card */
box-shadow: var(--shadow-md);   /* hover card, dropdown */
box-shadow: var(--shadow-lg);   /* modal, popover */
box-shadow: var(--shadow-xl);   /* command palette, large overlay */
box-shadow: var(--shadow-accent); /* primary button accent glow */
box-shadow: var(--shadow-inner);  /* glass inner highlight */
```

---

## Animation Tokens

### Duration
```css
transition: background var(--duration-micro)  var(--ease-smooth);  /* hover */
transition: opacity    var(--duration-normal) var(--ease-spring);  /* enter */
transition: transform  var(--duration-slow)   var(--ease-spring);  /* modal */
```

### Easing — never use `ease-in-out`
```css
var(--ease-spring)   /* default — spring into place */
var(--ease-smooth)   /* color/background transitions */
var(--ease-enter)    /* entering elements */
var(--ease-exit)     /* exiting elements */
var(--ease-snappy)   /* micro-interactions, clicks */
var(--ease-linear)   /* spinners only */
```

---

## Z-Index Tokens

```css
z-index: var(--z-base);     /* 0 — normal flow */
z-index: var(--z-raised);   /* 10 — sticky headers, raised cards */
z-index: var(--z-sticky);   /* 100 — fixed nav, bottom bar */
z-index: var(--z-overlay);  /* 200 — tooltips */
z-index: var(--z-dropdown); /* 300 — dropdown menus */
z-index: var(--z-drawer);   /* 400 — navigation drawers */
z-index: var(--z-modal);    /* 500 — dialogs */
z-index: var(--z-toast);    /* 600 — notifications */
z-index: var(--z-max);      /* 9999 — emergencies only */
```

---

## Component Alias Tokens

Pre-configured values for the most common components:

```css
/* Form inputs */
height: var(--input-height);        /* 44px */
height: var(--input-height-sm);     /* 36px — desktop compact */
padding-inline: var(--input-padding-x);
border: var(--input-border);
border-radius: var(--input-radius);
background: var(--input-bg);

/* Buttons */
height: var(--btn-height-md);       /* 44px */
padding-inline: var(--btn-padding-x-md);
border-radius: var(--btn-radius);
font-weight: var(--btn-font-weight);

/* Cards */
padding: var(--card-padding);       /* 24px */
border-radius: var(--card-radius);  /* 16px */
border: var(--card-border);
background: var(--card-bg);

/* Focus ring */
outline: var(--focus-ring);         /* 2px solid var(--color-accent) */
outline-offset: var(--focus-ring-offset);
```

---

## Tailwind v4 Integration

```css
/* globals.css */
@import "tailwindcss";
@import "./tokens/tokens.css";
@import "./tokens/tokens-dark.css";

@theme {
  /* Map token values into Tailwind's theme */
  --color-accent:   var(--color-accent);
  --color-surface:  var(--color-surface);
  --color-border:   var(--color-border);

  --spacing-1:  var(--space-1);
  --spacing-2:  var(--space-2);
  /* ... */

  --radius-sm:  var(--radius-sm);
  --radius-md:  var(--radius-md);
  --radius-xl:  var(--radius-xl);

  --shadow-sm:  var(--shadow-sm);
  --shadow-md:  var(--shadow-md);
  --shadow-lg:  var(--shadow-lg);
}
```

---

## Tooling (Design Tokens Pipeline)

**Style Dictionary** — transforms `design-tokens.json` to platform-specific output:
```json
{
  "source": ["tokens/design-tokens.json"],
  "platforms": {
    "css": {
      "transformGroup": "css",
      "buildPath": "tokens/",
      "files": [{ "destination": "tokens.generated.css", "format": "css/variables" }]
    },
    "ios": {
      "transformGroup": "ios-swift",
      "buildPath": "ios/Tokens/",
      "files": [{ "destination": "StyleTokens.swift", "format": "ios-swift/class.swift" }]
    },
    "android": {
      "transformGroup": "android",
      "buildPath": "android/res/values/",
      "files": [{ "destination": "style_tokens.xml", "format": "android/resources" }]
    }
  }
}
```

**Tokens Studio for Figma** — sync `design-tokens.json` bidirectionally with Figma variables.

---

## Lint Rule — No Raw Values

Add this CSS lint rule to catch token violations:

```js
// stylelint.config.js
module.exports = {
  rules: {
    'color-no-hex': true,  // no #hex in any .css file
    'color-named': 'never',
    'declaration-property-value-disallowed-list': {
      'font-size': ['/^[0-9]+(px|rem)$/'],  // must use var()
    }
  }
}
```

---

*Token version: global-design-skill v1.0*
*Source: `tokens/design-tokens.json` (W3C DTCG format)*
*Related: `references/color-alchemy.md`, `rules/02-layout-and-grid.md`, `recipes/add-dark-mode.md`*
