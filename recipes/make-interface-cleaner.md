# Recipe — Make an Interface Cleaner

> Clutter is not an abundance of elements — it is an absence of hierarchy. Clean interfaces have the same amount of information, presented with intentional contrast, grouping, and restraint. Remove nothing until you've tried making it quieter first.

---

## When to use

- Interface feels "busy" or "overwhelming"
- Everything has the same visual weight
- Users can't find the primary action
- UI looks like every element is fighting for attention
- Design uses too many colors, borders, shadows, or icons simultaneously

---

## Diagnosis: Clutter Sources

Identify what's causing noise before removing anything.

```
[ ] Too many colors (> 2 accent colors in the UI)
[ ] Border on every card (use background difference instead)
[ ] Icon on every list item, heading, and label
[ ] Every button is filled / primary weight
[ ] Long paragraph copy in the UI (not documentation — UI copy)
[ ] Multiple font sizes that differ by < 2px
[ ] Shadow on every card regardless of elevation
[ ] Dividers between every row (only needed for adjacent same-type items)
[ ] Form labels AND placeholder text doing the same job
[ ] Toast + banner + badge + inline message all active at once
[ ] Padding inconsistent across cards (some tight, some loose, randomly)
[ ] Section backgrounds all different colors (surface, surface-2, accent-tint, etc.)
```

---

## Step 1 — Reduce to One Accent Color

Every additional color competes with the one that matters.

**Before:**
```css
.btn-primary   { background: #6366f1; }  /* purple */
.badge-success { background: #22c55e; }  /* green */
.badge-warning { background: #f59e0b; }  /* yellow */
.badge-error   { background: #ef4444; }  /* red */
.link          { color: #0ea5e9; }       /* blue */
.tag-feature   { background: #8b5cf6; }  /* another purple */
```

**After — one accent, semantic variants only:**
```css
:root {
  --color-accent:  oklch(65% 0.22 258);  /* one accent */
  --color-success: oklch(55% 0.18 145);  /* semantic only */
  --color-warning: oklch(65% 0.18 75);   /* semantic only */
  --color-error:   oklch(52% 0.22 25);   /* semantic only */
}

/* Semantic colors appear only in status badges — not in decorative elements */
.btn-primary { background: var(--color-accent); }
.link        { color: var(--color-accent); }

/* Badges use semantic colors with reduced saturation */
.badge-success { background: oklch(from var(--color-success) l c h / 0.12); color: var(--color-success); }
```

---

## Step 2 — Remove Borders, Use Background Depth Instead

Borders create visual noise. Background contrast creates separation without lines.

**Before:**
```css
.card {
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 24px;
}
```

**After — three options ordered by visual weight:**

```css
/* Option A: Background only (lightest) — for items on a colored page */
.card {
  background: var(--color-surface);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
}

/* Option B: Background + subtle shadow (medium) — for floating elements */
.card {
  background: var(--color-surface);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
  box-shadow: 0 1px 2px oklch(0% 0 0 / 0.04),
              0 4px 8px oklch(0% 0 0 / 0.04);
}

/* Option C: Hairline border only when surface = background (needed for definition) */
.card {
  background: var(--color-surface);
  border: 1px solid oklch(0% 0 0 / 0.06);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
}
```

**Rule:** If the card background is different from its parent background, you don't need a border.

---

## Step 3 — Establish a 3-Level Type Hierarchy (and stop there)

More than 3 visual levels in a section creates chaos.

```css
/* Level 1: Primary — must be the most important thing */
.text-primary {
  font-size: var(--text-h3);    /* clamp(1.25rem, 2vw + 0.25rem, 2rem) */
  font-weight: 600;
  color: var(--color-text-primary);
  line-height: 1.3;
}

/* Level 2: Secondary — supporting information */
.text-secondary {
  font-size: var(--text-body);  /* clamp(1rem, 1.2vw + 0.4rem, 1.2rem) */
  font-weight: 400;
  color: var(--color-text-primary);
  line-height: 1.65;
}

/* Level 3: Muted — labels, captions, timestamps */
.text-muted {
  font-size: 0.875rem;
  font-weight: 400;
  color: var(--color-text-muted);  /* ~50% lightness contrast */
  line-height: 1.5;
}

/* Everything else is forbidden */
/* No .text-tiny, .text-micro, .text-label-secondary — use muted */
```

---

## Step 4 — Remove Icons from Non-Actions

Icons earn their place only when they add meaning that text cannot convey alone.

**Remove icons from:**
- Section headings ("Our Features ✨")
- Nav items that already have text labels
- Card headings when they're already titled
- List items that are just bullets
- Any decorative context

**Keep icons in:**
- Action buttons (edit, delete, copy, download)
- Status indicators (success ✓, error ✗, warning ⚠)
- Navigation (icon + label for recognition speed)
- Data types (calendar icon on dates, user icon on names)

```html
<!-- Before: icons everywhere -->
<h2>📊 Analytics</h2>
<li>🔒 Secure</li>
<li>⚡ Fast</li>
<li>🤝 Collaborative</li>

<!-- After: icons only where they convey type or status -->
<h2>Analytics</h2>
<li>Secure</li>
<li>Fast</li>
<li>Collaborative</li>
```

---

## Step 5 — Reduce Dividers

Dividers between every row create a grid that competes with the content.

**Before:**
```css
.list-item {
  padding: var(--space-3) var(--space-4);
  border-bottom: 1px solid var(--color-border); /* every row divided */
}
```

**After:**
```css
/* Option A: Space instead of lines */
.list {
  display: flex;
  flex-direction: column;
  gap: var(--space-1); /* whitespace creates separation */
}
.list-item {
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-md);
}
.list-item:hover { background: var(--color-surface-2); }

/* Option B: Dividers only between sections, not rows */
.section + .section {
  border-top: 1px solid var(--color-border);
  padding-top: var(--space-6);
}
```

---

## Step 6 — Normalize Button Hierarchy

Every filled button creates noise. Establish an absolute hierarchy.

```css
/* Rule: ONE primary action per section */

/* Primary — one per section, maximum */
.btn-primary {
  background: var(--color-accent);
  color: oklch(10% 0.01 258);
  font-weight: 600;
}

/* Ghost — secondary actions, can appear multiple times */
.btn-ghost {
  background: transparent;
  border: 1px solid var(--color-border);
  color: var(--color-text-secondary);
}

/* Text / Link — tertiary, lowest weight */
.btn-text {
  background: transparent;
  border: none;
  color: var(--color-accent);
  text-decoration: underline;
  text-underline-offset: 2px;
}

/* NEVER: Two filled buttons side by side */
```

---

## Step 7 — Consolidate Spacing to the Grid

Random padding values are a major clutter source.

**Audit the current spacing:**
```bash
# Find all hardcoded pixel values for padding/margin
grep -r "padding:\|margin:" src/ | grep -v "var(--" | grep "[0-9]px"
```

**Replace everything with the 4px grid:**
```css
:root {
  --space-1:  4px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;
  --space-5:  20px;
  --space-6:  24px;
  --space-8:  32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
}

/* Common patterns */
.card            { padding: var(--space-6); }
.card--compact   { padding: var(--space-4); }
.card--spacious  { padding: var(--space-8) var(--space-10); }
```

---

## Step 8 — Tighten Copy

Verbose UI copy is visual clutter. Every word must earn its place.

| Before | After |
|---|---|
| "Click here to submit your form" | "Submit" |
| "Please enter your email address below" | `placeholder="you@example.com"` |
| "Your changes have been saved successfully" | "Saved" |
| "Are you sure you want to delete this item?" | "Delete this item?" |
| "No results were found for your search" | "No results for "[query]"" |

**UI copy rules:**
- Remove "Please" — it adds length without warmth
- Remove "Click here to" — the affordance is already clear
- Replace "Your [noun]" with just the noun: "Your account" → "Account"
- Dates: show the date, not the explanation ("May 20, 2026" not "Last updated on May 20, 2026")

---

## Step 9 — Align on the Z-Axis

Inconsistent elevation is invisible clutter — it makes elements feel unrelated.

```
Level 0 — Page background:     oklch(8% 0.015 258)
Level 1 — Default surface:      oklch(13% 0.012 258)   cards, panels
Level 2 — Raised surface:       oklch(17% 0.010 258)   hover states, input bg
Level 3 — Floating:             shadow-md, slightly lighter
Level 4 — Overlay:              shadow-lg, backdrop blur, modal/drawer
Level 5 — Toast / critical:     above everything, shadow-lg + border
```

**Assign every element to exactly one level. Elements on the same level look the same.**

---

## Before / After Comparison

**Before (cluttered):**
- 5 accent colors in use
- Border on every card
- Icon on every list item
- 3 filled buttons visible at once
- Every row separated by divider
- 7 different font sizes on one page

**After (clean):**
- 1 accent color + 3 semantic-only colors
- Cards separated by background contrast
- Icons only on actions and status
- 1 primary button per section
- Rows separated by gap + hover state
- 3 hierarchical text levels

---

*Recipe version: global-design-skill v1.0 — `recipes/make-interface-cleaner.md`*
*Related: `rules/01-visual-hierarchy.md`, `rules/06-components.md`, `recipes/make-page-more-premium.md`*
