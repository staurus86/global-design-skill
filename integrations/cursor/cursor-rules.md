# Cursor Rules — global-design-skill

Copy the block below into `.cursorrules` at your project root (or into Cursor's "Rules for AI" setting).

---

```
You are working on a project that follows the global-design-skill design system. Apply these rules to every UI suggestion, code generation, and review.

## COLORS
- Use OKLCH for all color values. Never hex or rgb() in component CSS.
- Tint all neutrals toward the accent hue (chroma 0.005–0.018).
- One accent hue only. State variations change L and C, never H.
- Accent color occupies ≤ 15% of visible surface area.
- Text contrast ≥ 4.5:1 body, ≥ 3:1 large text and UI components.
- Alpha variants: oklch(from var(--token) l c h / α) — never hardcoded rgba.
- Dark mode: separate [data-theme="dark"] overrides — never color inversion.
- BANNED colors: purple-to-indigo gradient on white, neon glow shadows, pure #000/#fff without hue tint, gradient text (background-clip: text), rgba(purple, 0.2) blobs.

## TYPOGRAPHY
- All display/heading sizes use clamp() — never fixed px.
- Body text minimum 1rem (16px) everywhere, including form inputs.
- Hero H1 must be ≤ 3 lines on 390px viewport. Shorten the headline, never shrink the font.
- Line heights: 1.1 for headlines, 1.65 for body text.
- Letter spacing: tighten on large display type, widen on uppercase labels.
- Eyebrow tag (small caps pill) before every hero H1 and major section H2.
- No gradient text (background-clip: text with gradient background).
- BANNED fonts as primary display: Inter, Roboto, Arial, Open Sans, Helvetica, Poppins, Space Grotesk.

## ANIMATION
- Every element must enter the page — nothing appears at full opacity statically.
- No ease-in-out. No ease. Use cubic-bezier() via var(--ease-*) tokens.
- No transition: all. List specific properties.
- Use @starting-style for elements transitioning from display: none.
- Every animation must have a @media (prefers-reduced-motion: reduce) override.
- Use IntersectionObserver for scroll animations — never window.addEventListener('scroll').
- No multiple simultaneous animate-pulse elements. Use single shimmer sweep instead.
- Stagger sequential elements 60–120ms.
- Import from 'motion/react' — NEVER from 'framer-motion' (deprecated package name).

## ACCESSIBILITY
- All interactive elements keyboard-operable via Tab and Enter/Space.
- Never remove :focus-visible outline globally. Never use *:focus { outline: none }.
- Every form input needs a visible <label> with for/id — placeholder is not a label.
- Images: descriptive alt text or alt="" + aria-hidden="true" for decorative.
- Custom components (dropdowns, accordions, tabs, modals): add correct ARIA role, aria-expanded, aria-selected, aria-controls, aria-labelledby as appropriate.
- Dynamic content changes (errors, toasts, live counts): wire aria-live regions.
- Modal dialogs: focus trap within dialog + Escape closes + focus returns to trigger.
- Touch targets ≥ 44×44px for all interactive elements.
- Use semantic HTML (<button>, <nav>, <main>, <article>) over div soup + ARIA.

## PERFORMANCE
- Identify LCP element. Give it fetchpriority="high" loading="eager" and a <link rel="preload">.
- All <img> elements need explicit width and height attributes (prevents CLS).
- Use WebP or AVIF — never JPEG or PNG for photographic content.
- Above-fold images: loading="eager". Below-fold: loading="lazy".
- Web fonts: font-display: swap + <link rel="preload"> for critical fonts.
- Third-party scripts: async or defer — never synchronous in <head>.
- Reserve space for dynamic content before it loads (skeleton heights match real content).
- Lists > 200 rows: use virtual scrolling (TanStack Virtual).
- All interactions must respond within 400ms (Doherty Threshold).
- Next.js 15: use "use cache" + cacheLife() on slow data fetches.

## LAYOUT
- Minimum section padding: 80px (6rem). Preferred 96–128px.
- Spacing from 4px grid: var(--space-1) through var(--space-64).
- At least one section per page must break the grid — no full symmetry.
- Use min-h-[100dvh] for full-height sections — never h-screen (iOS Safari bug).

## BANNED PATTERNS
Layout: centered hero + H1 + subtext + 2 buttons | 3-equal-column icon grid | sticky nav touching top edge | section padding < 80px
Components: nested cards | side-stripe borders (border-left > 1px as accent) | multiple primary CTAs per section | identical card grids
Motion: transition: all | ease-in-out | multiple animate-pulse | framer-motion import
Copy: "Seamless" "Elevate" "Unleash" "Next-Gen" "Empower" "Revolutionize" | placeholder data | "Get Started"/"Learn More" | em dashes (—)

## TOKENS
Use CSS custom properties from tokens.css:
- Colors: var(--color-text-primary), var(--color-accent), var(--color-border)
- Spacing: var(--space-4) not 16px
- Radius: var(--radius-md) not 6px
- Shadows: var(--shadow-md) not box-shadow: 0 4px 8px ...
- Duration: var(--duration-fast) not 150ms
- Easing: var(--ease-smooth) not ease-in-out
```

---

## Usage Notes

**Option A — `.cursorrules` file** (project-level):
1. Create `.cursorrules` in your project root
2. Copy the content between the triple-backtick block above
3. Cursor automatically loads it for every chat in that project

**Option B — Cursor Settings** (global):
1. Open Cursor → Settings → Features → Rules for AI
2. Paste the block there to apply to all projects

**Option C — `@docs` reference**:
If you've indexed the global-design-skill repository in Cursor:
- Use `@global-design-skill` in chat to pull specific rules
- Reference specific files: `@rules/04-color.md` for color questions

---

*Source: global-design-skill — `integrations/cursor/cursor-rules.md`*
