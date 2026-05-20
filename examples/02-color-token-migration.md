# Example 02 — Color Token Migration

> **Rules applied:** color R1–R9 · animation R3 · tokens/tokens.css

**Scenario:** A component library built without a token system. Colors are hardcoded hex values scattered across 40+ component files. A designer changes the brand color and it takes 3 days to propagate everywhere — with misses. The fix: migrate to OKLCH tokens in one pass.

---

## Before — Raw Values Everywhere

```css
/* components/button.css */
.btn-primary {
  background: #6366f1;
  color: #ffffff;
  border: none;
  border-radius: 6px;
  padding: 10px 20px;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background: #4f46e5;
}

.btn-primary:disabled {
  background: #a5b4fc;
  color: rgba(255, 255, 255, 0.5);
  cursor: not-allowed;
}

/* components/card.css */
.card {
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06);
}

.card__heading {
  color: #111827;
  font-size: 18px;
  font-weight: 600;
}

.card__body {
  color: #6b7280;
  font-size: 14px;
}

/* components/badge.css */
.badge--success  { background: #d1fae5; color: #065f46; }
.badge--warning  { background: #fef3c7; color: #92400e; }
.badge--error    { background: #fee2e2; color: #991b1b; }
.badge--info     { background: #dbeafe; color: #1e40af; }

/* components/input.css */
.input {
  border: 1px solid #d1d5db;
  border-radius: 6px;
  background: #f9fafb;
  color: #111827;
  font-size: 14px;
  padding: 8px 12px;
}

.input:focus {
  outline: 2px solid #6366f1;
  outline-offset: 0;
  border-color: #6366f1;
}

.input--error {
  border-color: #ef4444;
  background: #fef2f2;
}

/* _dark.css — attempted dark mode, mostly broken */
@media (prefers-color-scheme: dark) {
  .card    { background: #1f2937; border-color: #374151; }
  .input   { background: #374151; color: #f9fafb; border-color: #4b5563; }
  /* btn-primary not updated — still shows light mode colors in dark */
  /* badge colors not updated — too many to handle */
}
```

---

## Diagnosis

| # | Violation | Rule |
|---|---|---|
| 1 | All colors are hex — no OKLCH anywhere | color R1 |
| 2 | Neutrals are pure gray — no hue tint | color R2 |
| 3 | Accent has 3 separate hardcoded values (#6366f1 / #4f46e5 / #a5b4fc) — not a system | color R3 |
| 4 | Disabled state uses hardcoded lighter accent instead of token | color R3 |
| 5 | `rgba(0,0,0,0.1)` shadow — hardcoded alpha | color R9 |
| 6 | Badge status colors are hardcoded hex pairs, not semantic tokens | color R7 |
| 7 | `transition: all 0.3s ease` — two violations | animation R2, R3 |
| 8 | Font-size 14px on body-level copy | typography R2 |
| 9 | Dark mode overrides are incomplete — accent, badges untouched | color R8 |

**Root cause:** No single source of truth for color. Every hardcoded value is a liability — when the brand changes, every file breaks individually.

---

## Migration Strategy

**Phase 1:** Add tokens file (30 min)
**Phase 2:** Replace values with tokens across all components (automated with grep + sed)
**Phase 3:** Delete `_dark.css` and replace with `tokens-dark.css` overrides
**Phase 4:** Verify dark mode works across all components automatically

---

## After — Token System

### Step 1 — Define tokens

```css
/* tokens/tokens.css */
:root {
  /* ── Accent (brand blue) ── */
  --color-accent-100: oklch(93% 0.06 258);
  --color-accent-200: oklch(85% 0.10 258);
  --color-accent-300: oklch(75% 0.16 258);
  --color-accent-400: oklch(68% 0.20 258);
  --color-accent-500: oklch(60% 0.22 258);   /* base — was #6366f1 */
  --color-accent-600: oklch(52% 0.22 258);   /* hover — was #4f46e5 */
  --color-accent-700: oklch(44% 0.20 258);

  /* ── Semantic accent ── */
  --color-accent:       var(--color-accent-500);
  --color-accent-dark:  var(--color-accent-600);
  --color-accent-light: var(--color-accent-300);
  --color-accent-bg:    oklch(from var(--color-accent) l c h / 0.08);
  --color-accent-border: var(--color-accent-200);

  /* ── Neutrals — hue-tinted toward accent (H 258) ── */
  --color-neutral-0:    oklch(99%  0.004 258);   /* near-white */
  --color-neutral-50:   oklch(97%  0.006 258);   /* surface */
  --color-neutral-100:  oklch(94%  0.008 258);   /* border light */
  --color-neutral-200:  oklch(88%  0.009 258);   /* border */
  --color-neutral-400:  oklch(66%  0.009 258);   /* muted text */
  --color-neutral-600:  oklch(45%  0.010 258);   /* secondary text */
  --color-neutral-800:  oklch(28%  0.012 258);   /* primary text */
  --color-neutral-900:  oklch(18%  0.014 258);   /* strong text */
  --color-neutral-950:  oklch(10%  0.015 258);   /* base surface */
  --color-neutral-1000: oklch(5%   0.014 258);   /* darkest */

  /* ── Semantic surface tokens ── */
  --color-base:          var(--color-neutral-0);
  --color-surface:       var(--color-neutral-50);
  --color-surface-2:     var(--color-neutral-100);
  --color-border:        var(--color-neutral-200);
  --color-text-primary:  var(--color-neutral-900);
  --color-text-secondary:var(--color-neutral-600);
  --color-text-muted:    var(--color-neutral-400);

  /* ── Status ── */
  --color-success-bg:    oklch(93% 0.06 150);
  --color-success-text:  oklch(32% 0.12 150);
  --color-warning-bg:    oklch(93% 0.08 85);
  --color-warning-text:  oklch(38% 0.14 65);
  --color-error-bg:      oklch(93% 0.05 22);
  --color-error-text:    oklch(38% 0.16 22);
  --color-info-bg:       oklch(92% 0.06 258);
  --color-info-text:     oklch(38% 0.14 258);

  /* ── Focus ring ── */
  --focus-ring: 2px solid var(--color-accent);
  --focus-ring-offset: 2px;
}
```

```css
/* tokens/tokens-dark.css */
[data-theme="dark"],
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --color-base:           var(--color-neutral-950);
  --color-surface:        oklch(14% 0.012 258);
  --color-surface-2:      oklch(19% 0.010 258);
  --color-border:         oklch(from var(--color-neutral-200) l c h / 0.15);
  --color-text-primary:   var(--color-neutral-0);
  --color-text-secondary: oklch(68% 0.008 258);
  --color-text-muted:     oklch(50% 0.008 258);

  /* Accent: lighter in dark mode (same hue, higher L) */
  --color-accent:         var(--color-accent-300);
  --color-accent-dark:    var(--color-accent-400);
  --color-accent-bg:      oklch(from var(--color-accent-500) l c h / 0.12);

  /* Status backgrounds in dark need less lightness */
  --color-success-bg:     oklch(22% 0.06 150);
  --color-success-text:   oklch(75% 0.12 150);
  --color-warning-bg:     oklch(22% 0.07 85);
  --color-warning-text:   oklch(78% 0.12 65);
  --color-error-bg:       oklch(20% 0.06 22);
  --color-error-text:     oklch(78% 0.14 22);
  --color-info-bg:        oklch(20% 0.07 258);
  --color-info-text:      oklch(78% 0.12 258);
}}
```

### Step 2 — Rewrite components with tokens

```css
/* components/button.css */
.btn-primary {
  background: var(--color-accent);
  color: oklch(98% 0.005 258);
  border: none;
  border-radius: var(--radius-md);
  padding-inline: var(--space-5);
  height: var(--btn-height-md);         /* 44px — touch target */
  font-weight: var(--font-weight-semibold);
  font-size: var(--text-sm);
  cursor: pointer;
  transition:
    background  var(--duration-fast) var(--ease-smooth),
    box-shadow  var(--duration-fast) var(--ease-smooth),
    transform   var(--duration-fast) var(--ease-snappy);
}

.btn-primary:hover {
  background: var(--color-accent-dark);
  box-shadow: var(--shadow-sm);
  transform: translateY(-1px);
}

.btn-primary:disabled {
  background: var(--color-accent-bg);
  color: var(--color-accent);
  cursor: not-allowed;
  opacity: 0.5;
  transform: none;
  box-shadow: none;
}

/* components/card.css */
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
}

.card__heading {
  color: var(--color-text-primary);
  font-size: var(--text-lg);
  font-weight: var(--font-weight-semibold);
}

.card__body {
  color: var(--color-text-secondary);
  font-size: var(--text-body);          /* 1rem minimum */
}

/* components/badge.css */
.badge--success  { background: var(--color-success-bg);  color: var(--color-success-text); }
.badge--warning  { background: var(--color-warning-bg);  color: var(--color-warning-text); }
.badge--error    { background: var(--color-error-bg);    color: var(--color-error-text);   }
.badge--info     { background: var(--color-info-bg);     color: var(--color-info-text);    }

/* components/input.css */
.input {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-surface);
  color: var(--color-text-primary);
  font-size: var(--text-body);          /* 1rem — prevents iOS zoom */
  padding-inline: var(--space-4);
  height: var(--input-height);          /* 44px */
  transition: border-color var(--duration-fast) var(--ease-smooth);
}

.input:focus-visible {
  outline: var(--focus-ring);
  outline-offset: var(--focus-ring-offset);
  border-color: var(--color-accent);
}

.input--error {
  border-color: var(--color-error-text);
  background: var(--color-error-bg);
}
```

---

## Result

**Dark mode:** Works automatically — `tokens-dark.css` overrides the semantic tokens. No component CSS changes needed.

**Brand change:** Update 7 OKLCH values in `tokens/tokens.css`. Every component updates in one edit.

**Audit command** — find remaining hardcoded colors:
```bash
grep -rn ":\s*#\|:\s*rgb\|:\s*hsl\|rgba(" src/ --include="*.css" --include="*.tsx"
```

Expected output after migration: zero matches.

---

## OKLCH vs Hex Equivalents

For reference — the approximate hex values the original code was using:

| Token | OKLCH | Old hex |
|---|---|---|
| `--color-accent-500` | `oklch(60% 0.22 258)` | `#6366f1` |
| `--color-accent-600` | `oklch(52% 0.22 258)` | `#4f46e5` |
| `--color-text-primary` | `oklch(18% 0.014 258)` | `#111827` |
| `--color-text-secondary` | `oklch(45% 0.010 258)` | `#6b7280` |
| `--color-border` | `oklch(88% 0.009 258)` | `#e5e7eb` |
| `--color-surface` | `oklch(97% 0.006 258)` | `#f9fafb` |

OKLCH equivalents are not exact matches — they are perceptually uniform replacements with a slight blue tint that creates system cohesion. The hex values had no consistent hue relationship.

---

*Example 02 — `examples/02-color-token-migration.md`*
*Related: `rules/04-color.md`, `tokens/tokens.css`, `tokens/tokens-dark.css`, `recipes/add-dark-mode.md`*
