# Example 06 — Dark Mode Implementation

> **Before:** Site uses hardcoded hex/rgb colors, no dark mode. Adding `prefers-color-scheme` styles at the end of each CSS file as a patch.  
> **After:** Full semantic token layer, class-based toggle with `localStorage` persistence, zero hardcoded colors in components.

---

## The Problem

```css
/* Before — scattered through 12 component files */
.card {
  background: #ffffff;
  color: #111827;
  border: 1px solid #e5e7eb;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.btn-primary {
  background: #6366f1;
  color: #ffffff;
}

/* Attempted dark mode patch at bottom of file */
@media (prefers-color-scheme: dark) {
  .card {
    background: #1f2937;
    color: #f9fafb;
    border-color: #374151;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
  }
  .btn-primary {
    background: #818cf8; /* adjusted manually — will drift */
  }
}
```

**Problems:**
- Every component has its own dark variant — 12 files to maintain
- Colors drift as devs adjust hex values independently
- No user preference toggle — only follows OS setting
- `prefers-color-scheme` patch cannot be disabled per-session
- Contrast ratios never verified in dark variants

---

## Step 1 — Build the Token Architecture

Two layers: **primitive** (raw OKLCH values) + **semantic** (meaning-based aliases). Components only touch semantic tokens.

### `tokens/tokens.css` — Primitive layer

```css
/* ============================================================
   PRIMITIVE TOKENS — Raw values, never used directly in components
   ============================================================ */
:root {
  /* Neutral scale — hue-tinted toward accent */
  --primitive-neutral-0:   oklch(99%  0.003 258);
  --primitive-neutral-50:  oklch(97%  0.005 258);
  --primitive-neutral-100: oklch(94%  0.006 258);
  --primitive-neutral-200: oklch(88%  0.008 258);
  --primitive-neutral-300: oklch(78%  0.009 258);
  --primitive-neutral-400: oklch(65%  0.010 258);
  --primitive-neutral-500: oklch(52%  0.010 258);
  --primitive-neutral-600: oklch(42%  0.010 258);
  --primitive-neutral-700: oklch(32%  0.010 258);
  --primitive-neutral-800: oklch(22%  0.010 258);
  --primitive-neutral-850: oklch(17%  0.010 258);
  --primitive-neutral-900: oklch(13%  0.010 258);
  --primitive-neutral-950: oklch(10%  0.008 258);

  /* Accent — indigo */
  --primitive-accent-300: oklch(75%  0.18  258);
  --primitive-accent-400: oklch(68%  0.20  258);
  --primitive-accent-500: oklch(60%  0.22  258);
  --primitive-accent-600: oklch(53%  0.22  258);
  --primitive-accent-700: oklch(45%  0.20  258);

  /* Semantic status */
  --primitive-green-400:  oklch(72%  0.17  145);
  --primitive-green-500:  oklch(62%  0.19  145);
  --primitive-yellow-400: oklch(80%  0.16  85);
  --primitive-yellow-500: oklch(72%  0.18  85);
  --primitive-red-400:    oklch(65%  0.20  22);
  --primitive-red-500:    oklch(56%  0.22  22);
  --primitive-blue-400:   oklch(68%  0.18  235);
  --primitive-blue-500:   oklch(59%  0.20  235);
}
```

### `tokens/tokens-light.css` — Light semantic layer

```css
/* ============================================================
   LIGHT THEME SEMANTIC TOKENS
   Applied to :root (default) and [data-theme="light"]
   ============================================================ */
:root,
[data-theme="light"] {

  /* Surface */
  --color-surface:   var(--primitive-neutral-0);
  --color-surface-2: var(--primitive-neutral-50);
  --color-surface-3: var(--primitive-neutral-100);

  /* Text */
  --color-text-primary:   var(--primitive-neutral-900);
  --color-text-secondary: var(--primitive-neutral-600);
  --color-text-muted:     var(--primitive-neutral-400);
  --color-text-disabled:  var(--primitive-neutral-300);
  --color-text-inverse:   var(--primitive-neutral-0);

  /* Border */
  --color-border:        var(--primitive-neutral-200);
  --color-border-strong: var(--primitive-neutral-300);
  --color-border-focus:  var(--primitive-accent-500);

  /* Accent */
  --color-accent:          var(--primitive-accent-500);
  --color-accent-hover:    var(--primitive-accent-600);
  --color-accent-subtle:   oklch(from var(--primitive-accent-500) l c h / 0.08);
  --color-accent-text:     var(--primitive-accent-700);

  /* Status */
  --color-success:         var(--primitive-green-500);
  --color-success-subtle:  oklch(from var(--primitive-green-500) l c h / 0.10);
  --color-warning:         var(--primitive-yellow-500);
  --color-warning-subtle:  oklch(from var(--primitive-yellow-500) l c h / 0.10);
  --color-danger:          var(--primitive-red-500);
  --color-danger-subtle:   oklch(from var(--primitive-red-500) l c h / 0.10);
  --color-info:            var(--primitive-blue-500);
  --color-info-subtle:     oklch(from var(--primitive-blue-500) l c h / 0.10);

  /* Elevation */
  --shadow-sm: 0 1px 2px oklch(0% 0 0 / 0.06);
  --shadow-md: 0 4px 12px oklch(0% 0 0 / 0.08), 0 1px 3px oklch(0% 0 0 / 0.04);
  --shadow-lg: 0 8px 32px oklch(0% 0 0 / 0.10), 0 2px 8px oklch(0% 0 0 / 0.06);
}
```

### `tokens/tokens-dark.css` — Dark semantic layer

```css
/* ============================================================
   DARK THEME SEMANTIC TOKENS
   Applied to [data-theme="dark"] or prefers-color-scheme fallback
   ============================================================ */
[data-theme="dark"] {

  /* Surface */
  --color-surface:   var(--primitive-neutral-950);
  --color-surface-2: var(--primitive-neutral-900);
  --color-surface-3: var(--primitive-neutral-850);

  /* Text */
  --color-text-primary:   var(--primitive-neutral-50);
  --color-text-secondary: var(--primitive-neutral-400);
  --color-text-muted:     var(--primitive-neutral-600);
  --color-text-disabled:  var(--primitive-neutral-700);
  --color-text-inverse:   var(--primitive-neutral-900);

  /* Border */
  --color-border:        var(--primitive-neutral-800);
  --color-border-strong: var(--primitive-neutral-700);
  --color-border-focus:  var(--primitive-accent-400);

  /* Accent — lighter variant for dark backgrounds */
  --color-accent:          var(--primitive-accent-400);
  --color-accent-hover:    var(--primitive-accent-300);
  --color-accent-subtle:   oklch(from var(--primitive-accent-400) l c h / 0.12);
  --color-accent-text:     var(--primitive-accent-300);

  /* Status — brighter for dark bg */
  --color-success:         var(--primitive-green-400);
  --color-success-subtle:  oklch(from var(--primitive-green-400) l c h / 0.12);
  --color-warning:         var(--primitive-yellow-400);
  --color-warning-subtle:  oklch(from var(--primitive-yellow-400) l c h / 0.12);
  --color-danger:          var(--primitive-red-400);
  --color-danger-subtle:   oklch(from var(--primitive-red-400) l c h / 0.12);
  --color-info:            var(--primitive-blue-400);
  --color-info-subtle:     oklch(from var(--primitive-blue-400) l c h / 0.12);

  /* Elevation — shadows barely visible on dark, replace with borders */
  --shadow-sm: 0 1px 0 var(--color-border);
  --shadow-md: 0 1px 0 var(--color-border), 0 4px 12px oklch(0% 0 0 / 0.4);
  --shadow-lg: 0 1px 0 var(--color-border), 0 8px 32px oklch(0% 0 0 / 0.6);
}

/* OS-level dark when no JS toggle has been set */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme]) {
    --color-surface:         var(--primitive-neutral-950);
    --color-surface-2:       var(--primitive-neutral-900);
    --color-surface-3:       var(--primitive-neutral-850);
    --color-text-primary:    var(--primitive-neutral-50);
    --color-text-secondary:  var(--primitive-neutral-400);
    --color-text-muted:      var(--primitive-neutral-600);
    --color-text-disabled:   var(--primitive-neutral-700);
    --color-text-inverse:    var(--primitive-neutral-900);
    --color-border:          var(--primitive-neutral-800);
    --color-border-strong:   var(--primitive-neutral-700);
    --color-border-focus:    var(--primitive-accent-400);
    --color-accent:          var(--primitive-accent-400);
    --color-accent-hover:    var(--primitive-accent-300);
    --color-accent-subtle:   oklch(from var(--primitive-accent-400) l c h / 0.12);
    --color-accent-text:     var(--primitive-accent-300);
    --color-success:         var(--primitive-green-400);
    --color-success-subtle:  oklch(from var(--primitive-green-400) l c h / 0.12);
    --color-warning:         var(--primitive-yellow-400);
    --color-warning-subtle:  oklch(from var(--primitive-yellow-400) l c h / 0.12);
    --color-danger:          var(--primitive-red-400);
    --color-danger-subtle:   oklch(from var(--primitive-red-400) l c h / 0.12);
    --color-info:            var(--primitive-blue-400);
    --color-info-subtle:     oklch(from var(--primitive-blue-400) l c h / 0.12);
    --shadow-sm:             0 1px 0 var(--color-border);
    --shadow-md:             0 1px 0 var(--color-border), 0 4px 12px oklch(0% 0 0 / 0.4);
    --shadow-lg:             0 1px 0 var(--color-border), 0 8px 32px oklch(0% 0 0 / 0.6);
  }
}
```

---

## Step 2 — Migrate Components to Semantic Tokens

```css
/* After — component uses only semantic tokens */
.card {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-md);
}

.btn-primary {
  background: var(--color-accent);
  color: var(--color-text-inverse);
}

.btn-primary:hover {
  background: var(--color-accent-hover);
}

/* No dark media query needed — tokens swap automatically */
```

**The result:** Toggle `data-theme="dark"` on `<html>` and every component adapts — no extra CSS.

---

## Step 3 — Theme Toggle UI

### HTML

```html
<button
  class="theme-toggle"
  type="button"
  aria-label="Switch to dark mode"
  title="Toggle color theme"
>
  <!-- Sun icon — shown in dark mode -->
  <svg class="theme-toggle__icon theme-toggle__icon--sun" aria-hidden="true"
    width="20" height="20" viewBox="0 0 24 24" fill="none"
    stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="4"/>
    <path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41
             M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/>
  </svg>
  <!-- Moon icon — shown in light mode -->
  <svg class="theme-toggle__icon theme-toggle__icon--moon" aria-hidden="true"
    width="20" height="20" viewBox="0 0 24 24" fill="none"
    stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
  </svg>
</button>
```

### CSS

```css
.theme-toggle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: var(--radius-md);
  background: transparent;
  border: 1px solid var(--color-border);
  color: var(--color-text-secondary);
  cursor: pointer;
  transition:
    background  var(--duration-fast) var(--ease-smooth),
    color       var(--duration-fast) var(--ease-smooth),
    border-color var(--duration-fast) var(--ease-smooth);
}

.theme-toggle:hover {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
}

/* Show sun in dark mode, moon in light mode */
[data-theme="dark"] .theme-toggle__icon--moon,
.theme-toggle__icon--sun { display: none; }

[data-theme="dark"] .theme-toggle__icon--sun,
.theme-toggle__icon--moon { display: block; }
```

### JavaScript

```js
// theme-toggle.js — runs before first paint to avoid flash
(function () {
  const STORAGE_KEY = 'color-theme'
  const root = document.documentElement

  function getPreferred () {
    const stored = localStorage.getItem(STORAGE_KEY)
    if (stored === 'dark' || stored === 'light') return stored
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  }

  function apply (theme) {
    root.setAttribute('data-theme', theme)
    localStorage.setItem(STORAGE_KEY, theme)
  }

  // Apply immediately — prevents flash on page load
  apply(getPreferred())

  // Wire toggle buttons
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.theme-toggle').forEach(btn => {
      btn.addEventListener('click', () => {
        const current = root.getAttribute('data-theme')
        const next    = current === 'dark' ? 'light' : 'dark'
        apply(next)
        btn.setAttribute('aria-label', `Switch to ${current} mode`)
      })
    })
  })
})()
```

**Load the script in `<head>` before any styles to prevent flash:**

```html
<head>
  <script src="/theme-toggle.js"></script>  <!-- before stylesheet -->
  <link rel="stylesheet" href="/tokens/tokens.css" />
  <link rel="stylesheet" href="/tokens/tokens-light.css" />
  <link rel="stylesheet" href="/tokens/tokens-dark.css" />
  <link rel="stylesheet" href="/styles.css" />
</head>
```

---

## Step 4 — Smooth Theme Transition

Prevent jarring hard-cuts when toggling — but disable for `prefers-reduced-motion`.

```css
/* Add to tokens.css or styles.css */
html {
  color-scheme: light dark;
}

/* Smooth token transitions on toggle — opt-in, not default */
html.theme-transitioning,
html.theme-transitioning * {
  transition:
    background-color 200ms var(--ease-smooth),
    color            150ms var(--ease-smooth),
    border-color     150ms var(--ease-smooth) !important;
}

@media (prefers-reduced-motion: reduce) {
  html.theme-transitioning,
  html.theme-transitioning * {
    transition: none !important;
  }
}
```

```js
// Add to theme toggle handler — briefly apply class
function apply (theme) {
  document.documentElement.classList.add('theme-transitioning')
  document.documentElement.setAttribute('data-theme', theme)
  localStorage.setItem(STORAGE_KEY, theme)
  setTimeout(() => document.documentElement.classList.remove('theme-transitioning'), 250)
}
```

---

## Step 5 — Next.js / React Implementation

### `app/layout.tsx`

```tsx
// Inline script prevents flash — runs synchronously before hydration
const themeScript = `
  (function () {
    var stored = localStorage.getItem('color-theme')
    var preferred = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    document.documentElement.setAttribute('data-theme', stored || preferred)
  })()
`

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: themeScript }} />
      </head>
      <body>{children}</body>
    </html>
  )
}
```

### `useTheme` hook

```tsx
'use client'
import { useEffect, useState } from 'react'

type Theme = 'light' | 'dark'

export function useTheme () {
  const [theme, setTheme] = useState<Theme>('light')

  useEffect(() => {
    const stored = localStorage.getItem('color-theme') as Theme | null
    const preferred = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    setTheme(stored ?? preferred)
  }, [])

  function toggle () {
    const next: Theme = theme === 'dark' ? 'light' : 'dark'
    setTheme(next)
    document.documentElement.setAttribute('data-theme', next)
    localStorage.setItem('color-theme', next)
  }

  return { theme, toggle, isDark: theme === 'dark' }
}
```

```tsx
'use client'
import { useTheme } from '@/hooks/useTheme'

export function ThemeToggle () {
  const { isDark, toggle } = useTheme()
  return (
    <button
      className="theme-toggle"
      onClick={toggle}
      aria-label={`Switch to ${isDark ? 'light' : 'dark'} mode`}
    >
      {isDark ? <SunIcon /> : <MoonIcon />}
    </button>
  )
}
```

---

## Before/After Summary

| Problem | Fix |
|---|---|
| 12 files with hardcoded hex colors | Primitive tokens → semantic tokens → components |
| Dark patches added as `@media` blocks | `[data-theme="dark"]` overrides semantic layer only |
| OS dark mode can't be overridden | `localStorage` preference + class-based toggle |
| Flash of light theme on load | Inline `<script>` in `<head>` before stylesheets |
| All shadows invisible in dark mode | Dark shadows replaced with border-based elevation |
| Status colors same lightness in both modes | Lighter (400-level) palette for dark backgrounds |
| No contrast verification | Status tokens shift from 500-level (light) to 400-level (dark) for WCAG AA |

---

## Verification

```
[ ] Toggle [data-theme="dark"] on <html> — every component adapts, no white flashes
[ ] No hex/rgb values in component CSS files — only var(--color-*)
[ ] Preference persists across page reload (localStorage)
[ ] OS preference respected on first visit (no stored pref)
[ ] No flash on page load (inline script before stylesheet)
[ ] Smooth transition on toggle (theme-transitioning class)
[ ] prefers-reduced-motion disables transition
[ ] Text contrast ≥ 4.5:1 in both themes (check DevTools → Accessibility)
[ ] Status badges (success/warning/danger) legible in both themes
[ ] Shadows visible in light, borders carry elevation cues in dark
```

---

*Example version: global-design-skill v1.0 — `examples/06-dark-mode-implementation.md`*  
*Related: `tokens/tokens.css`, `tokens/tokens-dark.css`, `rules/04-color.md`, `agents/design-systems-auditor.md`*
