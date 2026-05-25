# Golden output — o01: SaaS hero redesign

**Prompt:** "Use global-design-skill and redesign this SaaS hero. The current version has a centered H1, subtitle, and two equal CTA buttons."

---

## What a correct response must include

### 1. Banned pattern identification

Must explicitly flag the current design as a banned pattern:
> "The centered H1 + subtitle + two equal buttons layout is the default AI hero pattern. It is banned. See `checklists/global-design-review.md` → Banned Patterns."

### 2. Replacement layout

Must propose a specific alternative — not "improve it" but a concrete layout choice:
- Editorial split (headline left, visual right)
- Asymmetric hero with dominant visual anchor
- Product-first hero with inline demo/screenshot
- Command-line / code hero for developer tools

Example of correct specificity:
> "Use an asymmetric split: 60% left column with headline + CTA, 40% right with product screenshot. Grid: 12-col, hero spans cols 1–7 on desktop, full-width on mobile."

### 3. CTA specification

Must give a specific primary CTA label using `Verb + Object + Context` formula:
> Primary: "Start free — no card required" | Secondary: "See how it works (2 min)"

Must NOT propose two equal-weight CTAs.

### 4. Typography

Must specify font size using `clamp()`:
> `--text-hero: clamp(2.5rem, 5vw + 1rem, 5rem);`

### 5. Mobile behavior

Must address 390px breakpoint explicitly.

### 6. Gate compliance

Must address Gate 2 (user identified) and Gate 3 (metric set) before proposing layout.

---

## What a correct response must NOT include

- `background-clip: text` (gradient text — banned)
- `transition: all` (banned)
- `100vh` without `dvh` fallback (banned)
- `framer-motion` import (banned — use `motion/react`)
- Two equal-prominence CTAs
- Centered layout without explicit justification
