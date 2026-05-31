# Rule 01 — Visual Hierarchy

> Hierarchy is created by structure and contrast, not by decoration. Every element has a rank. The rank must be visible.

---

## The Hierarchy Stack

Elements have exactly one rank. Rank determines size, weight, contrast, and spatial position. Elements of the same rank look the same. Elements of different ranks look different.

```
Rank 1 — Primary:    The one thing this screen communicates
Rank 2 — Secondary:  Context that supports Rank 1
Rank 3 — Supporting: Labels, metadata, timestamps
Rank 4 — Muted:      Borders, dividers, placeholder text
```

If you cannot assign a rank to every element on the screen, the hierarchy is undefined.

---

## Rules

### R1 — One primary focal point per section

Every screen section has exactly one element at Rank 1. If two elements compete for Rank 1, neither is the focal point.

**Test:** Cover one element. Does the section still have a clear primary? If yes, the covered element is not Rank 1. If no, both elements were fighting for it — fix the hierarchy.

**Fix:** Reduce the secondary element's size, weight, or contrast until the primary is unambiguously dominant.

---

### R2 — Size delta must be meaningful

The size difference between adjacent hierarchy levels must be perceptually significant — not 2px different.

**Minimum ratios:**
- Rank 1 → Rank 2: 1.33× size difference (e.g., 48px → 36px)
- Rank 2 → Rank 3: 1.25× size difference (e.g., 36px → 28px or 24px → 18px)
- Body → Label: 1.14× difference (e.g., 16px → 14px)

**Banned:** Two heading levels that are the same size but different weights. Pick size OR weight, not weight as the only differentiator between levels.

---

### R3 — Weight amplifies hierarchy, size establishes it

`font-weight` is not a substitute for `font-size`. Size creates rank. Weight reinforces it.

| Level | Size | Weight |
|---|---|---|
| Hero / H1 | `var(--text-display)` | 700-800 |
| H2 | `var(--text-h2)` | 600-700 |
| H3 | `var(--text-h3)` | 600 |
| Body | `var(--text-body)` | 400 |
| Label / Caption | `0.875rem` | 500 |
| Muted | `0.875rem` | 400 |

---

### R4 — Contrast communicates rank

High contrast = high importance. Low contrast = low importance. Never reverse this.

```css
/* Correct: rank maps to contrast */
--color-text-primary: oklch(96% 0.005 258);   /* Rank 1-2 */
--color-text-secondary: oklch(70% 0.01 258);  /* Rank 3 */
--color-text-muted: oklch(50% 0.008 258);     /* Rank 4 */

/* Banned: high-contrast label under low-contrast heading */
.card-label { color: var(--color-text-primary); }  /* Don't if heading is muted */
```

---

### R5 — Spatial separation creates grouping

Elements close together are perceived as related. Elements far apart are perceived as separate.

**Rules:**
- Gap between groups: 2× the gap within groups
- Related elements cluster; unrelated elements separate
- A heading's visual group is what comes immediately after it — nothing else

**Test:** Remove all borders and backgrounds. Does the grouping still read? If not, the hierarchy depends on decoration, not structure.

---

### R6 — Decoration does not create hierarchy

Borders, shadows, background colors, icons on headings, and underlines do not establish rank — they decorate existing rank.

**Banned:**
- Adding a border to a section to make it "feel more important"
- Using an icon on every heading (all icons = no icons in terms of hierarchy)
- Colored backgrounds as the primary differentiator between sections

**Fix:** If you're adding decoration to compensate for weak hierarchy, fix the hierarchy. Increase size delta or weight. Remove the decoration.

---

### R7 — CTA must be the most visually dominant interactive element

The primary action on any screen section must have higher visual weight than all other interactive elements.

**Rules:**
- Primary CTA: filled, highest contrast, 44-52px height
- Secondary CTA: ghost or outline, same height as primary
- Tertiary action: text-only link, no border, no background
- Destructive action: same visual weight as secondary — never primary

**Test:** Screenshot the screen. Blur it slightly. What draws the eye? If it's not the primary CTA, fix the CTA first.

---

### R8 — The visual temperature rule

Elements with the same visual treatment must have the same function. Different functions need different treatments.

| Element | Treatment |
|---|---|
| All primary CTAs | Same color, same size, same style |
| All secondary actions | Same ghost/outline style |
| All status badges | Same badge component, color only varies |
| All data labels | Same size, same color token |
| All navigation items | Same style, active state varies by background |

**Banned:** Two different visual styles for the same type of element on the same page.

---

### R9 — Whitespace is not decoration

Whitespace is a hierarchy tool. It separates ranks, creates breathing room for focal points, and makes primary elements more visible by increasing their surrounding negative space.

**Rules:**
- The most important element on the screen gets the most whitespace around it
- Cramping a hero headline to fit more content above the fold is the wrong tradeoff
- Adding content to fill whitespace is the wrong solution — the whitespace was intentional
- **Workflow:** start with more whitespace than feels comfortable, then reduce. Tightening a spacious layout is easier and safer than finding room in a cramped one.

**Minimum section padding:** `6rem` block (96px). Preferred: `10rem-16rem`.

---

### R10 — Reading direction defines hierarchy order

Users read in F or Z patterns depending on layout. Place Rank 1 elements where the eye naturally lands first.

**F-pattern (content-heavy, left-aligned):** Top-left is Rank 1. Scanline priority decreases as users scan down.

**Z-pattern (sparse, landing pages):** Top-left → top-right → bottom-left → bottom-right. Place CTA at bottom-right of the Z.

**Center composition:** Only for hero sections with centered layout. The focal point is in the vertical and horizontal center. CTAs go below the headline.

---

## Hierarchy Audit Checklist

```
[ ] Every section has exactly one Rank 1 element
[ ] Size delta between levels is ≥ 1.25×
[ ] No two elements of different rank are the same size
[ ] CTA is the most visually dominant interactive element
[ ] Removing decoration leaves the hierarchy intact
[ ] Same visual treatment = same function throughout
[ ] Whitespace is largest around the most important element
```

## Related Files

- `operating-principles.md` — Principle 2 (one focus), Principle 6 (hierarchy through space)
- `rules/03-typography.md` — type scale and weight system
- `rules/04-color.md` — contrast and color hierarchy
- `rules/02-layout-and-grid.md` — spatial grouping
- `checklists/ui-review.md` — visual review checklist
