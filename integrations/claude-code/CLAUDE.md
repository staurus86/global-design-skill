# Design System — Claude Code Integration

Paste this block into your project's `CLAUDE.md` to load the global-design-skill rules into every Claude Code session.

---

## Instructions for Claude

You are working on a project that follows the **global-design-skill** design system. The rules below are non-negotiable quality gates — apply them to every UI decision, code suggestion, and review.

---

## Design Standards

### Colors
- All color values use **OKLCH** — no hex, no `rgb()` in component CSS
- Neutrals carry hue tint toward accent (chroma 0.005–0.018)
- One accent hue — state variations use L/C changes, not H changes
- Accent area ≤ 15% of visible screen
- Text contrast ≥ 4.5:1 body, ≥ 3:1 large text/UI components
- Alpha variants: `oklch(from var(--token) l c h / α)` pattern — never hardcoded opacity
- Dark mode uses separate token values (`[data-theme="dark"]`) — not color inversion

### Typography
- All display headings use `clamp()` fluid scale — no fixed px
- Body text minimum 16px on all viewports (inputs too — prevents iOS zoom)
- Hero H1 ≤ 3 lines on 390px viewport
- Line heights: 1.1 headlines / 1.65 body
- Eyebrow tag present on hero H1 and major section H2s
- No gradient text (`background-clip: text` banned)
- Banned primary display fonts: Inter, Roboto, Arial, Helvetica, Poppins, Space Grotesk

### Animation & Effects
- Every element must enter — nothing appears statically
- No `ease-in-out`, no `ease` — all `cubic-bezier()` via `var(--ease-*)` tokens
- No `transition: all` — explicit property list only
- `@starting-style` for elements transitioning from `display: none`
- `prefers-reduced-motion` override on EVERY animation and transition
- `IntersectionObserver` for scroll triggers — never `window.addEventListener('scroll')`
- `will-change: transform` set only during active animation, removed after
- No multiple simultaneous `animate-pulse` — use shimmer pattern
- Sequential elements stagger 60–120ms
- Import from `motion/react` — never `framer-motion`
- Canvas `devicePixelRatio` capped at 2 — `Math.min(window.devicePixelRatio, 2)`
- Three.js / R3F canvas pauses when off-screen via `IntersectionObserver`
- Cursor / tilt effects disabled on `pointer: coarse` (touch devices)
- `min-height: 100dvh` on full-screen sections — never `100vh` (iOS Safari bug)

### Accessibility (WCAG 2.2 AA minimum)
- All interactive elements reachable and operable by keyboard
- `:focus-visible` ring always present — never `outline: none` globally
- Every form input has a visible, persistent `<label>` with `for`/`id` wiring
- All images: descriptive `alt` or `alt=""` for decorative
- Custom components: correct ARIA role + state attributes
- Modals: focus trap + Escape closes + focus returns to trigger
- Dynamic content (errors, toasts, counts): `aria-live` regions wired
- All touch targets ≥ 44×44px
- Semantic HTML first — ARIA supplements, never replaces

### Performance (Core Web Vitals)
- LCP element identified: `fetchpriority="high"` + `loading="eager"` + `<link rel="preload">`
- All images have explicit `width` + `height` attributes (prevents CLS)
- All images: WebP or AVIF — never JPEG/PNG for photographs
- Above-fold images `loading="eager"`; below-fold `loading="lazy"`
- Critical fonts: `<link rel="preload">` + `font-display: swap`
- Third-party scripts: `async` or `defer` — never blocking in `<head>`
- Skeleton heights match loaded component heights (no CLS on data load)
- Lists > 200 rows: virtualized (TanStack Virtual)
- All interactions respond within 400ms (Doherty Threshold)

---

## Token Usage

Import order:
```html
<link rel="stylesheet" href="/tokens/tokens.css" />
<link rel="stylesheet" href="/tokens/tokens-dark.css" />
```

Anti-flash script (before `<body>`):
```html
<script>
  const t = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')
  document.documentElement.setAttribute('data-theme', t)
</script>
```

Use token variables — never raw values:
```css
/* Correct */
color: var(--color-text-primary);
padding: var(--space-4);
border-radius: var(--radius-md);
transition: opacity var(--duration-fast) var(--ease-smooth);

/* Wrong */
color: #1a1a2e;
padding: 16px;
border-radius: 6px;
transition: opacity 150ms ease-in-out;
```

---

## Banned Patterns (Instant Rejection)

```
Layout:    Centered hero + H1 + subtext + 2 buttons (default SaaS cliché)
           Full-width sticky nav touching top edge
           Section padding < 80px
           3-equal-column icon feature grid (only exception: ≤3 features)

Color:     Purple-to-indigo gradient on white
           Neon glow shadows
           Pure #000000 or #ffffff without hue tint
           Gradient text (background-clip: text)
           rgba(purple, 0.2) blobs as only decoration

Typography: Inter/Roboto/Arial as primary display font
            Font size < 16px for body text
            Line-height < 1.4 for body text

Components: Side-stripe borders (border-left/right > 1px as accent)
            Multiple primary CTAs per section
            Nested cards
            Identical card grids (same size, icon + heading + text, repeated)

Motion:    transition: all
           ease-in-out on any transition
           Multiple simultaneous animate-pulse
           Importing from framer-motion
           window.addEventListener('scroll') for animation calculations
           will-change: transform left on permanently
           h-screen / 100vh on full-height sections (use 100dvh)
           Cursor/tilt effects on touch devices (pointer: coarse)

Copy:      "Seamless", "Elevate", "Unleash", "Next-Gen", "Empower", "Revolutionize"
           Placeholder data: "John Doe", "Acme Corp", generic numbers
           "Get Started" / "Learn More" with no specificity
           Em dashes (—) — use commas, colons, or parentheses instead
```

---

## Quality Gates

Before marking any UI task complete:

```
[ ] Tokens used everywhere — no raw hex, px, or unitless values for colors/spacing/radius
[ ] All interactive elements keyboard accessible
[ ] Focus-visible ring present and visible in both themes
[ ] Images have width + height + appropriate loading strategy
[ ] Animations respect prefers-reduced-motion
[ ] Color contrast verified (4.5:1 text, 3:1 components)
[ ] Touch targets ≥ 44×44px
[ ] No banned patterns present
[ ] Effects: will-change removed after animation completes
[ ] Effects: cursor/tilt disabled on pointer: coarse
[ ] Effects: min-height: 100dvh used (not 100vh)
```

For pages with motion/effects, also run `checklists/wow-effects-checklist.md` (score ≥ 80% required).

---

## Reference Files

Full rule documentation in the `rules/` directory:

| Rule | File |
|---|---|
| Visual Hierarchy | `rules/01-visual-hierarchy.md` |
| Layout and Grid | `rules/02-layout-and-grid.md` |
| Typography | `rules/03-typography.md` |
| Color (OKLCH) | `rules/04-color.md` |
| Animation and Motion | `rules/05-animation.md` |
| Components | `rules/06-components.md` |
| Accessibility (WCAG 2.2) | `rules/07-accessibility.md` |
| Performance (CWV) | `rules/08-performance.md` |
| Responsive Design | `rules/09-responsive.md` |
| Forms | `rules/10-forms.md` |
| Data Tables | `rules/11-data-tables.md` |
| Landing Pages | `rules/14-landing-pages.md` |
| Iconography | `rules/15-iconography.md` |

**Effects patterns** (animations, parallax, 3D, motion): `patterns/effects/`

| Effect | Pattern |
|---|---|
| Grain, mesh, spotlight, glow | `patterns/effects/visual-effects.md` |
| Parallax (CSS / JS / GSAP) | `patterns/effects/parallax-system.md` |
| Text reveals, scramble, marquee | `patterns/effects/text-animations.md` |
| Pinned scroll, horizontal gallery | `patterns/effects/scroll-experiences.md` |
| Hover tilt, magnetic button | `patterns/effects/hover-effects.md` |
| Custom cursor | `patterns/effects/cursor-effects.md` |
| CSS 3D, Three.js, Spline | `patterns/effects/3d-effects.md` |

**Blueprints**: `blueprints/` — complete page scaffolds  
**Wow blueprint**: `blueprints/interactive-landing-page.md` — full effects stack  
**Recipes**: `recipes/` — targeted improvements  
**Tokens**: `tokens/tokens.css` + `tokens/tokens-dark.css`  
**Real-world references**: `references/` — curated production examples

---

*Source: github.com/staurus86/global-design-skill — add to CLAUDE.md in any project*

## Industry Context (new in v1.5.0)

When the user request mentions a business, product, or service:
1. Open `industries/_index.md` to identify the correct sector
2. Load the matching `industries/<sector>.md` file
3. Apply sector-specific Required Elements, Banned Patterns, Trust Signals,
   and Conversion Path rules before generating any design output

If no sector matches, proceed with generic rules from `rules/` and `blueprints/`.

## Extended States (new in v1.5.0)

The 9-state system is extended to 14 states. Read `patterns/states/_decision-matrix.md`
when designing loading, error, or access-control interactions.
