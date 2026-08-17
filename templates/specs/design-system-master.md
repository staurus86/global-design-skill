# Design System MASTER — Template

> The single source of truth for one project's design system. Two pages with the same palette but different decisions look like two different products; two pages that both inherit from one MASTER look like one product. This file freezes the project-wide decisions once; every page inherits them by default and declares only its justified deviations. Without it, a multi-page build re-decides tokens, spacing, and voice on every page and drifts into "the same brand, recolored."

**Usage:** Fill this once, before designing any page. Copy it into the project as `design-system/MASTER.md`. Each page gets a `design-system/pages/[name].md` that lists *only* its overrides (see the convention at the bottom). The MASTER operationalizes `rules/00-escalation-protocol.md` (Design Dials, Macrostructure, the Memorability Gate) for a whole site — lock those decisions here so they stop being re-litigated per page.

**Do not** restate the full token system from scratch — start from `skills/global-design/SKILL.md` Design Tokens (Core) or `tokens/tokens.css` and record the project's *deltas* and *choices*.

---

## Project: [Name]

**Date:** [YYYY-MM-DD] · **Design lead:** [Name] · **Brief:** [link to project-brief.md]

**Stack:** [React 19 / Next.js 16 / Tailwind v4 / other] · **CSS framework:** [Tailwind / Bootstrap / Bulma / UnoCSS / Panda CSS / Open Props]

---

## 1. Identity — locked before tokens

These three come from `rules/00-escalation-protocol.md`. They are the project's DNA; every page serves them.

```
The One Memorable Thing: [the single element a visitor recalls in 3 days — name it]
Visual metaphor:         [the organizing idea — "control cockpit", "the author's arsenal" — not "a grid"]
Default macrostructure:  [editorial / dashboard-first / product-led / manifesto / split-screen /
                          narrative-scroll / comparison-first / proof-first / scenario-first / map-first / top-picks-first]
Aesthetic archetype:     [Ethereal Black / Editorial Luxury / Cyberbrutalism / Organic Softness /
                          Volumetric Glass / Neo-Maximalism / Post-Digital Terminal / Spatial Luxury]
```

### Design Dials (project default)

State the project baseline; individual pages may push a dial in their override file with a reason.

```
DESIGN_VARIANCE:  [1–10]   (safe/conventional ←→ pioneering/unexpected)
MOTION_INTENSITY: [1–10]   (static ←→ full theatrical)
VISUAL_DENSITY:   [1–10]   (sparse/editorial ←→ data-dense)
```

---

## 2. Color — OKLCH tokens

Record the project palette as resolved OKLCH values. No raw hex in components — semantic tokens only.

```css
:root {
  /* Accent ramp (hue [H]) */
  --color-accent-500: oklch([L]% [C] [H]);   /* primary accent */
  /* ...record the full ramp the project actually uses */

  /* Neutral ramp (hue-tinted toward accent) */
  --color-neutral-0:    oklch([L]% [C] [H]);
  --color-neutral-1000: oklch([L]% [C] [H]);

  /* Status */
  --color-success: oklch([L]% [C] [H]);
  --color-warning: oklch([L]% [C] [H]);
  --color-error:   oklch([L]% [C] [H]);

  /* Semantic — what components reference */
  --color-bg:      var(--color-neutral-0);
  --color-surface: var(--color-neutral-100);
  --color-text:    var(--color-neutral-1000);
  --color-accent:  var(--color-accent-500);
}
```

**Dark mode:** [ ] supported — record the dark token overrides in `tokens-dark.css` style. Body text L ≤ 92% (no pure white; `rules/19` ceiling).

---

## 3. Typography

```
Display / headings font: [name + source + license]   (banned: Inter, Roboto, Arial, Open Sans, Poppins)
Body / UI font:          [name + source]
Mono (if used):          [name]
Type scale:              [inherit SKILL.md fluid clamp() scale / project override — record deltas]
Heading line-height:     [value]   Body line-height: [≥ 1.5]   Max measure: [≤ 75ch]
```

---

## 4. Spacing, radius, shadow

```
Spacing grid:     [4px base — inherit SKILL.md scale / record overrides]
Section rhythm:   [--space-section value]   (between page sections)
Radius hierarchy: cards ≤ [12px] · inputs [6–8px] · pill only for [tags]   (no over-rounded everything)
Shadow system:    [layered, hue-tinted, one light source — record the 2–3 tokens used]
```

---

## 5. Component conventions

Lock the rules every component on every page follows, so a button on /pricing matches a button on /blog.

| Element | Convention |
|---|---|
| Primary button | [size, radius, weight, hover/active/focus-visible behavior] |
| Secondary button | [how it differs from primary] |
| Card | [radius, border vs shadow — pick one, not both; padding] |
| Input | [radius, border, focus ring ≥ 3:1] |
| Link | [color, underline behavior — no font-weight change on hover] |
| Icon set | [one consistent SVG set — name it; no emoji as UI icons] |
| Focus ring | [visible, ≥ 3:1, never `outline:none` with no replacement] |

---

## 6. Motion budget (project default)

```
Budget tier:        [CSS-only / CSS+IntersectionObserver / CSS+GSAP ScrollTrigger / R3F]
Signature moment:   [the ONE place motion earns its weight — not blur/animation everywhere]
prefers-reduced-motion: every animation gated — [confirmed]
Effect fallback:    [what renders when the effect is off — static poster / CSS-only reduction / nothing]
Fallback triggers:  [prefers-reduced-motion · save-data · no WebGL context · low hardwareConcurrency]
```

A tier above `CSS-only` without a named fallback is an unfinished decision, not a budget. The fallback is a design state someone sees — specify it here, don't leave it to the implementer.

---

## 7. Voice & copy

```
Tone:        [3–5 adjectives]
Reading on:  [writing-rule applied — no AI-slop signature words, no em dashes]
CTA style:   [specific verbs, not "Get Started"/"Learn More"]
```

---

## Page-Overrides Convention

The MASTER above is the default for **every** page. Each page file declares only what it changes — and *why*. A deviation without a justification is an inconsistency to fix, not a feature.

**Per-page file** (`design-system/pages/[name].md`):

```
# Page: /[route]

Inherits: MASTER (everything not listed below)
Macrostructure: [MASTER default, OR a different one + one-line reason]

Overrides:
| What | MASTER value | This page | Why (required) |
|---|---|---|---|
| [e.g. VISUAL_DENSITY] | [4] | [8] | [this is the data dashboard — density serves the task] |
| [e.g. background rhythm] | [single surface] | [alternating sections] | [homepage needs section separation] |

No other deviations. Tokens, fonts, spacing, components, voice = MASTER.
```

**Rules:**
- Default is inheritance. Listing a value unchanged is noise — only record deltas.
- Every override row needs a *why* tied to that page's job, not taste.
- If three pages all override the same MASTER value the same way, the MASTER is wrong — fix the MASTER, delete the three overrides.
- Run the 10-second recall test (`rules/00` Memorability Gate) on the homepage against the MASTER identity before replicating patterns across pages.

---

*Template version: global-design-skill v2.7.0 — `templates/specs/design-system-master.md`*
*Related: `rules/00-escalation-protocol.md` (Dials, Macrostructure, Memorability Gate), `skills/global-design/SKILL.md` (Design Tokens Core), `tokens/tokens.css`, `templates/briefs/project-brief.md` (the what/why this freezes the how for), `blueprints/website-from-scratch.md` (Step 0)*
