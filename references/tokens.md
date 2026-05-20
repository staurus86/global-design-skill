# Reference — Design Tokens

> The complete token system: spacing scale, shadow system, radius scale, z-index layers, breakpoints, and how to compose them. Source of truth is `tokens/design-tokens.json`. This file explains the reasoning behind the values.

---

## Spacing — 4px Grid

All spacing uses multiples of 4px. Never raw pixel values in components.

```css
:root {
  --space-1:  4px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;
  --space-5:  20px;
  --space-6:  24px;
  --space-7:  28px;
  --space-8:  32px;
  --space-9:  36px;
  --space-10: 40px;
  --space-11: 44px;   /* min touch target size */
  --space-12: 48px;
  --space-14: 56px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;   /* min section padding */
  --space-32: 128px;
  --space-40: 160px;
  --space-48: 192px;
  --space-64: 256px;
}
```

### Spacing by context

| Context | Token(s) |
|---|---|
| Button padding | `--space-3` (vertical) `--space-5` (horizontal) |
| Card padding (default) | `--space-6` to `--space-8` |
| Card padding (compact) | `--space-4` |
| Form field gap | `--space-4` |
| Section padding (mobile) | `--space-12` to `--space-16` |
| Section padding (desktop) | `--space-24` to `--space-32` |
| Hero section padding | `clamp(6rem, 14vw, 16rem)` |
| Min touch target | `--space-11` (44px) |
| Icon size (default) | `--space-5` (20px) |
| Icon size (large) | `--space-6` (24px) |

---

## Shadow Scale

Layered shadows using OKLCH. Dark mode: use surface + border instead of shadows.

```css
:root {
  /* Subtle lift — inputs, focused elements */
  --shadow-xs: 0 1px 2px oklch(0% 0 0 / 0.04);

  /* Default card at rest */
  --shadow-sm:
    0 1px 2px oklch(0% 0 0 / 0.04),
    0 2px 4px oklch(0% 0 0 / 0.04);

  /* Hover card, dropdowns */
  --shadow-md:
    0 4px 8px  oklch(0% 0 0 / 0.06),
    0 12px 24px oklch(0% 0 0 / 0.08);

  /* Modals, sheets, popovers */
  --shadow-lg:
    0 8px 16px  oklch(0% 0 0 / 0.08),
    0 24px 48px oklch(0% 0 0 / 0.14);

  /* Large overlays, command palette */
  --shadow-xl:
    0 16px 32px oklch(0% 0 0 / 0.10),
    0 48px 96px oklch(0% 0 0 / 0.18);

  /* Accent shadow on primary buttons */
  --shadow-accent: 0 8px 32px oklch(from var(--color-accent) l c h / 0.25);

  /* Inner specular highlight */
  --shadow-inner:
    inset 0 1px 0 oklch(100% 0 0 / 0.12),
    inset 0 -1px 0 oklch(0% 0 0 / 0.06);
}
```

### Shadow usage guide

| Context | Shadow |
|---|---|
| Card at rest | `--shadow-sm` |
| Card on hover | `--shadow-md` |
| Dropdown / tooltip | `--shadow-md` |
| Modal / dialog | `--shadow-lg` |
| Command palette | `--shadow-xl` |
| Primary button | `--shadow-accent` |
| Input, form field | `--shadow-xs` |
| Glass surface | `--shadow-lg` + `--shadow-inner` |

**Dark mode rule:** In dark mode, elevate surfaces by increasing background lightness rather than adding shadows. Shadows disappear on dark backgrounds.

```css
/* Dark mode elevation — by background not shadow */
.dark .card       { background: var(--color-surface); }    /* L=15% */
.dark .card-raised { background: var(--color-surface-2); } /* L=22% */
.dark .card-float  { background: oklch(28% 0.012 258); }  /* L=28% — elevated */
```

---

## Border Radius Scale

```css
:root {
  --radius-none: 0;
  --radius-sm:   4px;    /* checkboxes, small badges */
  --radius-md:   8px;    /* buttons, inputs, dropdowns, small cards */
  --radius-lg:   12px;   /* cards, panels */
  --radius-xl:   16px;   /* large cards, modals, drawers */
  --radius-2xl:  24px;   /* hero containers, featured sections */
  --radius-3xl:  32px;   /* large marketing cards */
  --radius-full: 9999px; /* pills, badge chips, toggles */
}
```

### Radius consistency rules

**Match radius to architectural level:**
- Page-level containers → `--radius-2xl` or `--radius-3xl`
- Component-level cards → `--radius-xl` or `--radius-lg`
- UI elements (buttons, inputs) → `--radius-md`
- Small details (checkboxes, tags) → `--radius-sm` or `--radius-md`

**The inner radius rule:** When a child element is inset within a rounded parent, use `inner-radius = outer-radius - padding`.

```css
.bezel-outer { border-radius: var(--radius-2xl); padding: 0.375rem; }
.bezel-inner { border-radius: calc(var(--radius-2xl) - 0.375rem); }
```

**Cyberbrutalism exception:** No radius on containers (0px), but full `--radius-full` on pill chips. Nothing between.

---

## Z-Index Layers

Never use arbitrary z-index values. Use these named layers.

```css
:root {
  --z-base:     0;
  --z-raised:   10;    /* slightly raised cards, sticky table headers */
  --z-sticky:   100;   /* sticky nav, bottom tab bar */
  --z-overlay:  200;   /* tooltips, hover cards */
  --z-dropdown: 300;   /* dropdown menus, date pickers */
  --z-drawer:   400;   /* sidebars, navigation drawers */
  --z-modal:    500;   /* dialogs, modals */
  --z-toast:    600;   /* notifications (above modals) */
  --z-max:      9999;  /* emergency override — avoid */
}
```

**Rule:** If you need a z-index between existing layers, your component hierarchy is wrong. Fix the stacking context rather than add an intermediate value.

---

## Duration and Easing Tokens

```css
:root {
  /* Durations */
  --duration-instant:   80ms;
  --duration-micro:    120ms;
  --duration-fast:     150ms;
  --duration-normal:   200ms;
  --duration-moderate: 300ms;
  --duration-slow:     400ms;
  --duration-entrance: 600ms;
  --duration-relaxed:  800ms;

  /* Easings — never use named easings (ease, ease-in-out, etc.) */
  --ease-spring:  cubic-bezier(0.16, 1, 0.3, 1);
  --ease-smooth:  cubic-bezier(0.25, 0.46, 0.45, 0.94);
  --ease-enter:   cubic-bezier(0, 0, 0.2, 1);
  --ease-exit:    cubic-bezier(0.4, 0, 1, 1);
  --ease-snappy:  cubic-bezier(0.4, 0, 0, 1);
  --ease-linear:  cubic-bezier(0, 0, 1, 1);
}
```

---

## Breakpoints

Mobile-first. Always `min-width`. Never `max-width`.

```css
:root {
  --bp-sm:  640px;   /* large phones, small landscape */
  --bp-md:  768px;   /* tablet portrait */
  --bp-lg:  1024px;  /* tablet landscape, small laptop */
  --bp-xl:  1280px;  /* desktop */
  --bp-2xl: 1440px;  /* wide desktop */
  --bp-3xl: 1920px;  /* ultra-wide */
}

/* Usage — always min-width */
@media (min-width: 768px)  { /* tablet+  */ }
@media (min-width: 1024px) { /* desktop+ */ }
@media (min-width: 1280px) { /* wide+    */ }
```

**Test viewports:** 390px (iPhone 15), 768px (iPad), 1280px (standard desktop), 1440px (wide). If it works at these four, it works everywhere.

---

## Container Query Tokens

For components that adapt based on container size, not viewport.

```css
/* Define a containment context on the parent */
.card-wrapper {
  container-type: inline-size;
  container-name: card;
}

/* Query the card's own width */
@container card (min-width: 400px) {
  .card-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--space-6);
  }
}

@container card (min-width: 600px) {
  .card-heading { font-size: var(--text-h2); }
}
```

---

## Token Composition Rules

**Rule 1 — Never raw values in components:**
```css
/* Wrong */
.btn { padding: 12px 20px; background: oklch(65% 0.22 258); }

/* Correct */
.btn { padding: var(--space-3) var(--space-5); background: var(--color-accent); }
```

**Rule 2 — Semantic tokens in components, primitives only in token definitions:**
```css
/* Wrong — primitive in component */
.card { background: var(--neutral-950); }

/* Correct — semantic in component */
.card { background: var(--color-surface); }
```

**Rule 3 — Relative color syntax for opacity variants:**
```css
/* Don't create separate tokens for every opacity level */
/* Use relative color syntax instead */
.overlay { background: oklch(from var(--color-accent) l c h / 0.08); }
.border-subtle { border-color: oklch(from var(--color-border) l c h / 0.5); }
```

---

*Reference version: global-design-skill v1.0 — `references/tokens.md`*
*Related: `tokens/design-tokens.json`, `tokens/tokens.css`, `rules/02-layout-and-grid.md`*
