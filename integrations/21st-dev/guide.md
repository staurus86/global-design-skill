# 21st.dev Integration Guide

> 21st.dev is a community-driven React component library with 284+ hero sections, navbar patterns, pricing layouts, cards, and footers — all production-ready, Tailwind + Next.js compatible. Use it to avoid building common UI from scratch and to get professional-grade component code in seconds.

---

## When to Use 21st.dev

Use before writing any common UI component from scratch:

| Component type | Use 21st.dev | Build from scratch |
|---|---|---|
| Hero sections | ✅ | Only if highly custom |
| Navbars / headers | ✅ | Only if highly custom |
| Pricing tables | ✅ | Only if highly custom |
| Feature grids | ✅ | |
| Testimonials / social proof | ✅ | |
| CTA sections | ✅ | |
| Footer layouts | ✅ | |
| Custom business logic UI | | ✅ |
| Dashboard charts | | ✅ |
| Form flows with validation | | ✅ |

---

## How to Search Components

### In Claude Code / Cursor — Magic Command

Describe the component you need. Use `/ui` or `/21` prefix:

```
/ui dark hero section with headline, subtext, and two CTA buttons
/ui pricing table with three tiers and highlighted middle plan
/ui navbar with logo, links, and mobile hamburger
/21 testimonials grid with avatars and star ratings
```

The MCP routes your description to 21st.dev's library and returns production-ready React + Tailwind code.

### Via 21st.dev website — Manual Search

Browse components by category: `https://21st.dev/community/components`

Category shortcuts:
- Hero: `https://21st.dev/community/components/s/hero`
- Navbar: `https://21st.dev/community/components/s/navbar-navigation`
- Pricing: search "pricing"
- Cards: search "card"

---

## MCP Setup (Claude Code)

Add to `.claude/mcp.json`:

```json
{
  "mcpServers": {
    "21st-dev": {
      "command": "npx",
      "args": ["-y", "@21st-dev/mcp@latest"],
      "env": {
        "API_KEY": "your-21st-dev-api-key"
      }
    }
  }
}
```

Get API key at: `https://21st.dev/account`

---

## Component Retrieval Workflow

When asked to build a page or section, follow this order:

```
1. Identify all "standard" sections (hero, nav, pricing, footer, testimonials)
2. For each standard section: search 21st.dev first
3. Select the closest match — then adapt to the project's design tokens
4. For custom/unique sections: build from scratch using global-design-skill rules
```

Example prompt that leverages this fully:
> "Build a SaaS landing page for a project management tool. Use 21st.dev for the hero, navbar, and pricing section. Apply our OKLCH tokens and sector rules for B2B SaaS."

---

## Adapting 21st.dev Components to Global Design Skill Rules

21st.dev components use Tailwind defaults. After importing, apply these transformations:

### 1. Replace hex/raw colors with OKLCH tokens

```tsx
// Before (21st.dev default)
<div className="bg-indigo-600 text-white">

// After (global-design-skill)
<div style={{ background: 'var(--color-accent)' }} className="text-white">
```

### 2. Replace generic font sizes with clamp()

```tsx
// Before
<h1 className="text-5xl font-bold">

// After
<h1 className="text-hero font-bold">  {/* uses clamp() from tokens.css */}
```

### 3. Replace border-radius defaults with tokens

```tsx
// Before
<button className="rounded-lg">

// After
<button className="rounded-[var(--radius-md)]">
```

### 4. Add motion/react entry animation

```tsx
import { motion } from 'motion/react'

// Wrap the imported component
<motion.section
  initial={{ opacity: 0, y: 24 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true }}
  transition={{ duration: 0.5, ease: 'easeOut' }}
>
  <HeroFromTwentyFirst />
</motion.section>
```

### 5. Remove banned patterns from component code

Check imported code for:
- `shadow-indigo-500/20` → remove shadow or use `shadow-black/10`
- `bg-gradient-to-br from-violet-600` → replace with solid color
- `transition: all` / `transition-all` → replace with specific property
- `framer-motion` imports → replace with `motion/react`

---

## Prompt Templates for Common Page Types

### Landing page from scratch
```
Build a [INDUSTRY] landing page for [PRODUCT]. 

Use 21st.dev components for: hero, navbar, and footer.
Build from scratch: [custom sections based on product].

Design constraints:
- OKLCH color tokens, no raw hex
- B2B SaaS sector rules from global-design-skill
- motion/react for entry animations (whileInView, once: true)
- 390/768/1280px breakpoints
- No framer-motion imports
```

### Redesign existing page
```
Redesign the [SECTION] of this page using 21st.dev as a source for the base component structure.

Current problems: [list from audit]

Apply:
- global-design-skill Level [N] escalation
- [SECTOR] industry rules
- Adapt to existing token system
```

---

## Sector-Specific Component Guidance

| Sector | Key 21st.dev components to use | Avoid |
|---|---|---|
| B2B SaaS | Feature grid, comparison table, integration logos | Generic hero with gradient |
| E-commerce | Product card, pricing, trust badges | Feature-list heavy sections |
| Health / Medical | Clean card layouts, FAQ | Dark hero, heavy animation |
| Finance / Fintech | Stats bar, compliance badges | Playful illustrations |
| Agency / Portfolio | Image-led hero, case study cards | Icon-heavy feature grids |

---

## Component Quality Checklist

Before using a 21st.dev component in production, verify:

- [ ] Removed all Tailwind default colors (indigo-*, violet-*, gray-*)
- [ ] Replaced rounded-* with token equivalents
- [ ] No `framer-motion` import in component source
- [ ] Added `useReducedMotion` if component has animation
- [ ] Checked mobile layout at 390px
- [ ] Text contrast ≥ 4.5:1 (run Lighthouse accessibility)
- [ ] Replaced placeholder copy with real content
