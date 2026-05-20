# GitHub Copilot Instructions — global-design-skill

> Paste this content into `.github/copilot-instructions.md` at the project root. GitHub Copilot Chat reads this file automatically for workspace context in VS Code and JetBrains.

---

```markdown
# Design System Instructions for GitHub Copilot

This project uses global-design-skill — a complete design operating system.
Follow all rules below when generating or suggesting code.

## Colors

Use semantic CSS custom properties. Never suggest hex, rgb(), or hsl() directly in components.

Correct:
  color: var(--color-text-primary);
  background: var(--color-surface-2);
  border: 1px solid var(--color-border);
  accent: var(--color-accent);

Wrong (never suggest):
  color: #111827;
  background: rgba(255, 255, 255, 0.9);
  color: oklch(13% 0.01 258);  ← primitive, not semantic

Dark mode: use [data-theme="dark"] attribute on <html>, never patch with @media prefers-color-scheme inline on components.

## Typography

All heading font-size values must use clamp(). Never suggest fixed px.

CSS custom property scale:
  --text-hero:    clamp(3.5rem, 8vw + 1rem, 12rem)
  --text-display: clamp(2.5rem, 5vw + 0.5rem, 7rem)
  --text-h1:      clamp(2rem, 4vw + 0.25rem, 4.5rem)
  --text-h2:      clamp(1.75rem, 3vw + 0.5rem, 4rem)
  --text-h3:      clamp(1.25rem, 2vw + 0.25rem, 2rem)
  --text-body:    clamp(1rem, 1.2vw + 0.4rem, 1.2rem)

Line-height:
  h1, h2: 1.1 (tight — headline density)
  h3, h4: 1.3 (snug)
  p, li:  1.65 (comfortable reading)

Letter-spacing:
  Hero/display: -0.04em to -0.03em
  h1, h2: -0.02em
  Uppercase labels: +0.08em to +0.12em

Font families — only through variables:
  var(--font-display)  → expressive typeface (Fraunces, Syne, etc.)
  var(--font-body)     → functional (Instrument Sans, DM Sans)
  var(--font-mono)     → monospace (JetBrains Mono)

Never suggest Inter, Roboto, Arial, Helvetica, or Poppins as the display/hero font.

## Spacing

Use the 4px grid token scale:
  --space-1: 4px   --space-4: 16px  --space-8: 32px   --space-16: 64px
  --space-2: 8px   --space-5: 20px  --space-10: 40px  --space-20: 80px
  --space-3: 12px  --space-6: 24px  --space-12: 48px  --space-24: 96px

Never suggest: 5px, 7px, 10px (use 8 or 12), 14px, 18px, 22px, 25px, 30px

## Animations and Transitions

Never suggest:
  transition: all            ← too broad, causes performance issues
  ease-in-out                ← generic, signals no thought given to timing
  framer-motion import       ← use motion/react instead
  window.addEventListener('scroll') ← causes reflows, use IntersectionObserver
  Multiple pulse animations  ← use single shimmer on skeleton container

Correct easing by context:
  Entering elements:   cubic-bezier(0.16, 1, 0.3, 1)    [spring]
  Hover changes:       cubic-bezier(0.25, 0.46, 0.45, 0.94) [smooth]
  Menu/modal closing:  cubic-bezier(0.4, 0, 1, 1)        [exit]
  Button click:        cubic-bezier(0.4, 0, 0, 1)        [snappy]

Duration guide:
  Hover/icon: 80–150ms
  Enter/exit: 150–300ms
  Modal/drawer: 300–500ms
  Hero entrance: 500–800ms

Always include prefers-reduced-motion override for any animation.

Scroll animations — correct pattern:
  new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('visible'); observer.unobserve(e.target) }
    })
  }, { threshold: 0.1 }).observe(el)

## Accessibility

- All touch targets: minimum 44×44px (width and height)
- Text contrast: ≥ 4.5:1 | UI components: ≥ 3:1
- Never suggest outline: none without a visible focus replacement
- Form inputs: always paired with <label>, never placeholder-only
- Images: meaningful alt text, or alt="" for purely decorative images
- Use aria-current="page" on active navigation links
- All interactive elements keyboard accessible

## Components

### Buttons
Must handle all states: default / hover / active / focus-visible / disabled / loading
Loading state: spinner inside, min-width set to prevent layout shift

### Forms
- Validate on blur, not keypress
- Error messages: [input label]: [what went wrong]. [how to fix].
- aria-describedby links input to its error message
- Never reset form on submission failure
- Input font-size minimum 1rem (prevents iOS auto-zoom)

### Navigation
- Primary nav: ≤ 7 items
- Active nav link: aria-current="page" + background + color + font-weight change
- Mobile nav: aria-expanded on toggle button, aria-controls pointing to menu

## Layout Rules

Never suggest:
  h-screen or height: 100vh   ← iOS Safari bug, use min-h-[100dvh]
  Centered hero with H1 + subtext + 2 equal buttons ← banned cliché
  3 equal columns with icon + heading + text ← banned grid pattern
  border-left > 1px as colored accent on cards ← side-stripe pattern, banned
  background-clip: text with gradient ← gradient text, banned

Section padding minimum: padding-block: 96px (var(--space-24))

## Performance

- LCP image: fetchpriority="high" loading="eager" with explicit width/height
- All other images: loading="lazy" with explicit width/height
- Display font: preload before LCP paint
- Avoid @import in CSS — use <link> tags

## Module and Import Patterns

Correct:
  import { motion, AnimatePresence } from 'motion/react'

Wrong:
  import { motion } from 'framer-motion'

## Banned Copy Patterns

Never suggest these words in UI copy:
  Seamless, Elevate, Unleash, Next-Gen, Empower, Revolutionize
  "Get Started" without specificity
  "Learn More" without context
  Em dashes (—) — use commas, colons, or parentheses instead
  Placeholder stats: "50% faster", "99.9% uptime" without source
```

---

## Setup

1. Create the directory: `mkdir -p .github`
2. Create the file: `.github/copilot-instructions.md`
3. Paste the content above (between the triple backtick fences, without the fences)
4. Commit the file — Copilot reads it from the repository

### Verification

In VS Code, open Copilot Chat and ask: `@workspace What design constraints should I follow when writing CSS?`

Copilot should respond with rules from this file: token-based colors, clamp() type scale, banned easing values, and accessibility requirements.

### Scope Notes

- Instructions apply to all Copilot Chat responses in the workspace
- Copilot inline suggestions (tab completion) are not directly controlled by this file — they are influenced by surrounding code patterns
- For inline suggestion consistency, ensure existing files already use the token system (Copilot learns from local patterns)

---

*Integration version: global-design-skill v1.0 — `integrations/github-copilot/copilot-instructions.md`*  
*Related: `integrations/cursor/cursor-rules.md`, `integrations/windsurf/rules.md`, `integrations/claude-code/CLAUDE.md`*
