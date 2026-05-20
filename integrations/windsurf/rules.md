# Windsurf Rules — global-design-skill

> Paste this content into your `.windsurfrules` file at the project root. Windsurf reads this file automatically for every session in the workspace.

---

```
# ============================================================
# DESIGN SYSTEM RULES — global-design-skill
# Windsurf (.windsurfrules)
# ============================================================

## Core Principle

Every design decision must earn its place. One visual choice per question.
When in doubt, simplify.

## Color — OKLCH Only

- NEVER use hex (#rrggbb), rgb(), or hsl() values in components
- ALL colors through semantic CSS custom properties:
  var(--color-surface), var(--color-text-primary), var(--color-accent)
- Dark mode via [data-theme="dark"] attribute on <html> — NOT @media prefers-color-scheme patches
- Semantic token layer: --color-text-primary (not --primitive-neutral-900)
- Status colors: --color-success, --color-warning, --color-danger, --color-info

## Typography — Fluid Scale

- NEVER fixed px on heading font sizes — always clamp()
- Scale: --text-hero / --text-display / --text-h1 / --text-h2 / --text-h3 / --text-body / --text-sm
- Display font: --font-display (Fraunces, Syne, Playfair, or similar expressive typeface)
- Body font: --font-body (Instrument Sans, DM Sans, Outfit — functional, high legibility)
- Mono font: --font-mono (JetBrains Mono, Berkeley Mono)
- BANNED as primary display: Inter, Roboto, Arial, Helvetica, Open Sans, Poppins
- Line-height: 1.1 on h1/h2 | 1.3 on h3/h4 | 1.65 on p/li | 1.5 on labels
- Letter-spacing: -0.04em on hero | -0.02em on h1/h2 | +0.12em on uppercase labels
- Eyebrow tag before every hero H1 and major section H2
- Hero H1 must fit ≤ 3 lines at 390px viewport

## Spacing — 4px Grid

- ALL spacing from token scale: --space-1 (4px) through --space-24 (96px)
- Off-grid values FORBIDDEN: 5px, 7px, 10px, 14px, 18px, 22px, 25px, 30px
- Section padding: minimum padding-block: var(--space-24) — never less than 96px
- Use 8 or 12 instead of 10, use 8 instead of 7

## Layout

- NEVER centered hero (H1 + subtext + 2 buttons) — banned SaaS cliché
- NEVER 3-equal-column icon grid
- NEVER full-width sticky nav touching top edge
- At least 1 section per page must break the grid
- Sections: minimum padding-block 96px (--space-24), preferred 160px
- Max-width prose: 65ch for articles, 42ch for card descriptions, 48ch for hero sub
- min-h-[100dvh] NOT h-screen (iOS Safari bug with address bar)
- Bento grid: 12-column base, hero cell span 8, stat cells span 4

## Animation

- NEVER: transition: all | ease-in-out | ease (generic) | ease-in (except exits)
- NEVER: window.addEventListener('scroll') for animations — use IntersectionObserver
- NEVER: framer-motion import — use motion/react instead
- NEVER: multiple pulse animations — use single shimmer on skeleton container
- Easing tokens:
  Entering: --ease-spring (0.16, 1, 0.3, 1)
  Hover: --ease-smooth (0.25, 0.46, 0.45, 0.94)
  Closing: --ease-exit (0.4, 0, 1, 1)
  Click: --ease-snappy (0.4, 0, 0, 1)
- Duration: hover 80-150ms | enter/exit 150-300ms | modal 300-500ms | hero 500-800ms
- prefers-reduced-motion MUST be implemented on EVERY animation

## Accessibility

- Touch targets: minimum 44×44px for all interactive elements
- Color contrast: ≥ 4.5:1 for text | ≥ 3:1 for UI components and focus indicators
- Focus indicators: always visible, never outline: none without custom replacement
- aria-current="page" on active nav items
- All images: meaningful alt text or alt="" for decorative
- Form inputs: always paired with <label> — no placeholder-only labeling
- Keyboard: all interactions reachable via Tab + Enter/Space
- Skip navigation link at top of every page

## Performance

- LCP image: fetchpriority="high" + loading="eager" + explicit width/height
- All other images: loading="lazy" + explicit width/height (prevents CLS)
- Fonts: rel="preload" as="font" for display font before LCP
- Core Web Vitals targets: LCP ≤ 2.5s | CLS ≤ 0.1 | INP ≤ 200ms
- No layout shift: set explicit dimensions on images, embeds, ads
- Avoid @import in CSS — use <link> tags

## Banned Patterns — Instant Fail

- Gradient text (background-clip: text with gradient)
- Purple-to-indigo gradient on white background
- Side-stripe borders (border-left or border-right > 1px as decorative accent)
- Multiple animate-pulse elements — use single shimmer
- Glassmorphism used decoratively (only for genuine spatial layering)
- Em dashes (— or --) in copy — use commas, colons, semicolons, periods, or parentheses
- "Seamless", "Elevate", "Unleash", "Next-Gen", "Empower", "Revolutionize" in copy
- Placeholder data: "John Doe", "Acme Corp", fake stats without source
- Generic CTAs: "Get Started", "Learn More" without specificity

## Components

### Buttons
Required states: default / hover / active / focus-visible / disabled / loading
Loading state: spinner replaces label, button width locked via min-width

### Forms
- Validate on blur, never on keypress
- Error message: what happened + how to fix (aria-describedby on input)
- No form reset on submission failure — preserve user input
- Input font-size: var(--text-body) minimum — prevents iOS zoom

### Navigation
- Primary nav: ≤ 7 items (Hick's Law)
- Items named for user goals, not feature/section names
- Active state: background + color + font-weight change (not color-only)
- Mobile: hamburger animates to X via CSS transform

## CSS Architecture

Load order:
1. tokens.css (primitives)
2. tokens-light.css (semantic aliases)
3. tokens-dark.css ([data-theme="dark"] overrides)
4. base.css (reset, root styles)
5. components/*.css
6. pages/*.css

Never:
- Use !important except in reset and utility overrides
- Nest more than 3 levels deep
- Use @import in non-entry CSS files
```

---

## Configuring Windsurf

1. Create `.windsurfrules` at the root of your project
2. Paste the content above (between the triple backtick fences, without the fences themselves)
3. Windsurf will read this file and apply it to every Cascade session in the workspace

### Verification

Windsurf displays active rules in the context panel. After adding the file, start a new Cascade session and ask: "What design rules are you following?" — it should summarize the token, typography, and animation constraints.

---

*Integration version: global-design-skill v1.0 — `integrations/windsurf/rules.md`*  
*Related: `integrations/cursor/cursor-rules.md`, `integrations/claude-code/CLAUDE.md`, `tokens/tokens.css`*
