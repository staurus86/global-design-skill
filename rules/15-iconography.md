# Rule — Iconography

> Icons are a communication system, not decoration. An icon without a label is a test of whether the user shares your mental model. An icon with a label is just visual noise if the label already says everything. These rules encode when icons add meaning and when they subtract it.

---

## R1 — Icon without label requires 100% recognition confidence.

Show an icon alone only when you are certain every user will instantly know what it means. This is a much smaller set than you think.

```
Icons that can stand alone (universal):
  ✓ Search (magnifying glass) — near-universal
  ✓ Close (×) — in a dialog or tag
  ✓ Back (←) — in a navigation context
  ✓ Print, Share, Download — familiar from OS conventions

Icons that require a label:
  ✗ Any application-specific action
  ✗ Star (favorite? bookmark? rate? premium?)
  ✗ Bell (notifications? alerts? preferences?)
  ✗ Sparkle (AI? new? featured?)
  ✗ Three dots / hamburger — many users still don't recognize these
```

**Rule:** When in doubt, show the label. The label costs 30px. An unusable icon costs conversion.

---

## R2 — Icon + label: icon is decorative, label carries the meaning.

When both icon and label are present, the icon is `aria-hidden="true"` — the label does the semantic work.

```html
<!-- Correct: icon + label, icon decorative -->
<button type="button">
  <svg aria-hidden="true" focusable="false" width="16" height="16" ...>
    <!-- download icon paths -->
  </svg>
  Download report
</button>

<!-- Correct: icon-only button MUST have aria-label -->
<button type="button" aria-label="Download report">
  <svg aria-hidden="true" focusable="false" width="16" height="16" ...>
    <!-- download icon paths -->
  </svg>
</button>

<!-- Wrong: icon + label, neither has aria treatment -->
<button>
  <svg><!-- icon --></svg>
  Download report
</button>

<!-- Wrong: icon-only, no accessible name -->
<button>
  <svg><!-- icon --></svg>
</button>
```

---

## R3 — Consistent stroke weight. 1.5px or 1.25px. Never default Lucide 2px.

Thick icon strokes compete with body text. The default Lucide stroke-width (2px at 24px size) is correct for isolated display but too heavy at 16px in dense UI. Reduce to 1.5px for 20–24px icons, 1.25px for 16px icons.

```html
<!-- Lucide React: always override stroke-width -->
import { Download, Settings, Bell } from 'lucide-react'

/* Wrong — default 2px stroke */
<Download size={16} />

/* Correct — reduced stroke for small size */
<Download size={16} strokeWidth={1.25} />
<Settings size={20} strokeWidth={1.5}  />
<Bell     size={24} strokeWidth={1.5}  />
```

```css
/* CSS override for all SVG icons in the UI */
.icon {
  stroke-width: 1.5;
  flex-shrink: 0;       /* icons don't compress in flex layouts */
}

.icon--sm { stroke-width: 1.25; }   /* 12–16px icons */
.icon--md { stroke-width: 1.5;  }   /* 18–24px icons */
.icon--lg { stroke-width: 1.25; }   /* 28–32px icons — thick looks wrong at large size too */
```

---

## R4 — Icon size must be a token value. Never arbitrary px.

```css
/* Icon size tokens */
--icon-xs:  12px;
--icon-sm:  16px;
--icon-md:  20px;
--icon-lg:  24px;
--icon-xl:  32px;
--icon-2xl: 48px;

/* Usage */
.icon { width: var(--icon-md); height: var(--icon-md); }

/* Context: inline with text — match cap height */
.btn-sm svg  { width: var(--icon-sm); height: var(--icon-sm); }
.btn-md svg  { width: var(--icon-md); height: var(--icon-md); }
.btn-lg svg  { width: var(--icon-lg); height: var(--icon-lg); }

/* Context: hero or feature icons — larger */
.feature-icon svg { width: var(--icon-xl); height: var(--icon-xl); }
```

---

## R5 — Use one icon set. Never mix Lucide + Heroicons + FontAwesome.

Mixed icon sets create visual inconsistency — different line weights, corner radii, and design philosophies on the same page. Choose one and use it exclusively.

```
Recommended sets (in priority order):
  1. Lucide — Baseline 2024, tree-shakeable, consistent geometry
  2. Heroicons — Tailwind's set, two sizes (16 + 24)
  3. Phosphor — Rich weight variants (thin/regular/bold)
  4. Radix Icons — If using Radix UI components

Never mix sets in the same product.
Exception: one-off custom SVGs for brand-specific concepts (verified by designer).
```

**Free, commercial-safe icon sources (verify the set's license once, then commit to it):**

| Set | License | Notes |
|---|---|---|
| **Lucide** (lucide.dev) | ISC | Default recommendation — consistent geometry, tree-shakeable |
| **Heroicons** (heroicons.com) | MIT | Tailwind Labs, 16 + 24 sizes |
| **Tabler Icons** (tabler.io/icons) | MIT | 6,100+ icons, personal + commercial |
| **Phosphor** (phosphoricons.com) | MIT | Weight variants (thin → bold) |
| **SVG Repo** (svgrepo.com) | Mixed — **verify per icon** | 500k+ vectors; license varies by icon, do not assume |

Pick one set as the product's system; SVG Repo is a fallback for a missing concept — check that icon's specific license before shipping.

---

## R6 — Icon-only navigation items always have visible labels.

Navigation icons without labels force users to guess. Tab bars, sidebars, and toolbars always show labels next to or below icons.

```html
<!-- Correct: icon + label in nav -->
<nav aria-label="Main navigation">
  <a href="/dashboard" aria-current="page" class="nav-item">
    <svg aria-hidden="true" class="nav-icon" ...></svg>
    <span class="nav-label">Dashboard</span>
  </a>
  <a href="/deployments" class="nav-item">
    <svg aria-hidden="true" class="nav-icon" ...></svg>
    <span class="nav-label">Deployments</span>
  </a>
</nav>

<!-- Wrong: icon-only sidebar — collapsed mode must still have tooltip -->
<!-- If you collapse to icon-only, add tooltip via title or aria-label -->
<a href="/dashboard" aria-label="Dashboard" title="Dashboard">
  <svg aria-hidden="true" ...></svg>
</a>
```

---

## R7 — `currentColor` for icon color. Never hardcode fill or stroke.

Icons should inherit color from their parent context — button states, active states, and theme changes propagate automatically without touching the SVG.

```css
/* Correct: SVG inherits from parent */
.icon {
  color: currentColor;    /* stroke: currentColor; fill: none; for line icons */
  stroke: currentColor;
  fill: none;
}

/* Color controlled via the parent */
.btn:hover .icon       { color: var(--color-text-primary); }
.nav-item--active .icon { color: var(--color-accent); }
```

```tsx
/* React: Lucide already uses currentColor — just control via className */
<button className="btn text-muted hover:text-primary">
  <Download className="icon" />
  Download
</button>
```

---

## R8 — Status and feedback icons: always pair with color AND text.

Status icons (success checkmark, error X, warning triangle) must not rely on color alone. The icon shape provides one signal; the label provides a second.

```html
<!-- Correct: icon shape + color + text -->
<div class="status status--success" role="status">
  <svg class="status__icon" aria-hidden="true"><!-- check icon --></svg>
  <span>Deployment successful</span>
</div>

<div class="status status--error" role="alert">
  <svg class="status__icon" aria-hidden="true"><!-- x-circle icon --></svg>
  <span>Build failed — 3 tests failed in auth.test.ts</span>
</div>

<!-- Wrong: icon + color, no text -->
<div class="status">
  <svg class="status__icon status--success" aria-hidden="true"><!-- check --></svg>
  <!-- No text — color-blind users see only the shape, no explanation -->
</div>
```

---

## R9 — Animated icons: one icon, one moment. Never animate ambient icons.

An icon animation draws the eye. Use it to communicate a state change, not as decoration. An icon that pulses continuously, spins forever, or bounces on hover is distracting visual noise.

```tsx
/* Correct: spinner while loading, static when done */
{isLoading
  ? <Loader2 className="animate-spin" aria-label="Loading..." />
  : <Check  aria-hidden="true" />
}

/* Correct: one-time success animation */
.icon-check {
  stroke-dasharray: 100;
  stroke-dashoffset: 100;
  transition: stroke-dashoffset 400ms var(--ease-spring);
}
.icon-check.complete { stroke-dashoffset: 0; }

/* Wrong: ambient hover animation on an informational icon */
.info-icon:hover { animation: spin 1s linear infinite; }

/* Wrong: pulsing icon in the sidebar */
.notification-icon { animation: pulse 2s ease-in-out infinite; }
```

```css
/* prefers-reduced-motion: disable icon animations */
@media (prefers-reduced-motion: reduce) {
  .animate-spin    { animation: none; }
  .icon-check      { transition: none; stroke-dashoffset: 0; }
}
```

---

## R10 — Emoji are never UI icons.

Emoji have inconsistent rendering across platforms, operating systems, and screen readers. An emoji that looks like a warning on macOS looks different on Android and gets announced differently by VoiceOver vs. NVDA. Use SVG icons.

```html
<!-- Wrong: emoji as UI icon -->
<button>⚠️ Delete account</button>
<span>✅ Verified</span>
<li>🚀 Performance</li>

<!-- Correct: SVG icon + text -->
<button>
  <svg aria-hidden="true" class="icon icon--warning" ...></svg>
  Delete account
</button>
<span>
  <svg aria-hidden="true" class="icon icon--success" ...></svg>
  Verified
</span>

<!-- Exception: emoji in user-generated content (chat, comments) — appropriate context -->
```

---

## R11 — A domain-specific icon set can *be* the system (extends R5).

R5 says "one icon set, exception: one-off custom SVGs." On a content, portfolio, catalog, or personal-brand site that exception scales up: a **purpose-built branded icon set** (one visual language — same stroke, same accent, transparent background) beats a generic Lucide row, because each icon maps 1:1 to the *topic* of the thing it labels instead of being a decorative stand-in.

```
When a branded set beats the generic set:
  ✓ Blog / article cards   → icon = the article's subject (entity-seo, robots-rules, core-web-vitals)
  ✓ Service / tool cards    → icon = what the service/tool does
  ✓ Catalog / directory     → icon = the item's category
A generic Lucide "document/gear/rocket" placeholder communicates nothing the title doesn't.
```

**Rules for a branded set:**

1. **One topic → one icon, no repeats on a single plane.** If 30 cards share a page, use 30 distinct icons. A repeated icon reads as "these two are the same thing." (Cross-page reuse is fine.)
2. **Self-styled SVGs sit bare — drop the colored box.** A branded icon carries its own accent/gradient; nesting it in the generic `--accent-green-glow` chip double-decorates. Use a transparent ~56px container.
3. **The set is still *one* system.** Same stroke weight, same accent, same canvas. Mixing a branded set with leftover Lucide on the same surface is the R5 violation in a new costume — convert the whole plane or none of it.
4. **Decorative role stays (R2).** Branded topic icons are `alt=""` / `aria-hidden`; the card title is the accessible name.
5. **Below-the-fold icons are `loading="lazy"`** — and verify they actually decode on scroll (`naturalWidth > 0`), not just that the file 200s.

```html
<div class="card__icon card__icon--brand">
  <img src="/img/icons/robots-rules.svg" width="56" height="56" alt="" loading="lazy">
</div>
<h3 class="card__title">Robots.txt</h3>   <!-- carries the accessible meaning -->
```

```css
.card__icon--brand { width: 56px; height: 56px; background: none; border-radius: 0; }
.card__icon--brand img { width: 56px; height: 56px; display: block; }
```

**Trade-off:** a branded set is real design + maintenance cost. Worth it when icons *recur as a system* across many topic-labeled cards; overkill for a handful of generic actions — there, stay on Lucide (R5).

*Field-tested: sk-seo.ru 2026-05-31 — 60-icon branded set on blog (15) + services (6) + tools (30), see `examples/before-after/sk-seo-2026-05-31/`.*

---

## Iconography Acceptance Criteria

```
[ ] Icon-only interactive elements have aria-label
[ ] Icon + label: icon is aria-hidden="true"
[ ] Stroke weight overridden: 1.5px for 20-24px, 1.25px for 16px and 32px+
[ ] One icon set used throughout — no mixing
[ ] Navigation items show visible labels (not icon-only)
[ ] Icon color via currentColor — no hardcoded fill/stroke in SVG
[ ] Status icons paired with text (not icon + color alone)
[ ] Animated icons: state-change only, not ambient decoration
[ ] prefers-reduced-motion override on icon animations
[ ] No emoji as UI icons
[ ] Icon sizes from token scale (--icon-sm through --icon-2xl)
[ ] Branded set (if used): one topic → one icon, no repeats on a plane, bare (no colored box), still one visual system
```

---

*Rule version: global-design-skill v1.9.11 — `rules/15-iconography.md`*
*Related: `rules/07-accessibility.md` R4, `rules/04-color.md` R7, `rules/05-animation.md` R8, `rules/06-components.md`*
