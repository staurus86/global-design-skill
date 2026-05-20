# Figma Handoff Checklist

> Component naming conventions and the handoff protocol that pairs with global-design-skill. A Figma file is handoff-ready only when its variables, components, and structure map cleanly onto tokens and code. Run this before marking any Figma file "ready for dev".

---

## How to Use

Mark each item **[P]** Pass, **[F]** Fail, **[N/A]** Not applicable. Any **[F]** in sections 1–4 blocks handoff.

---

## 1. Variables Map to Tokens

The Figma variable structure must mirror `tokens/design-tokens.json`.

- [ ] Two-layer structure: primitive variables + semantic variables (no raw values in semantic layer)
- [ ] Color variables use OKLCH-equivalent values matching `tokens/tokens.css`
- [ ] Semantic colors reference primitives — never hardcoded hex
- [ ] Spacing variables follow the 4px grid (`space/1` … `space/24`)
- [ ] Radius, typography, and shadow variables exist and match token names
- [ ] A `light` and `dark` mode exist on every semantic color collection
- [ ] No color, spacing, or radius is applied as a raw value anywhere — variables only

---

## 2. Naming Conventions

Names must translate 1:1 to code identifiers.

| Figma element | Convention | Example |
|---|---|---|
| Primitive variable | `category/scale` | `blue/500`, `space/4` |
| Semantic variable | `role/context` | `color/text-primary`, `color/surface` |
| Component | `PascalCase` | `Button`, `DataTable`, `EmptyState` |
| Component variant property | `lowercase` | `variant`, `size`, `state` |
| Variant value | `lowercase-kebab` | `primary`, `ghost`, `icon-only` |
| Layer (meaningful) | `kebab-case` describing role | `card-header`, `cta-label` |

- [ ] Component names match the component names used in `patterns/` and code
- [ ] Variant properties are `variant`, `size`, `state` — consistent across all components
- [ ] No default layer names left (`Frame 47`, `Group 12`, `Rectangle 3`)
- [ ] Icon components share one naming scheme and one icon set

---

## 3. Component Structure

- [ ] Every component uses Auto Layout — no absolute positioning for layout
- [ ] Padding and gaps use spacing variables, not typed-in numbers
- [ ] Components have proper constraints / resizing behavior set
- [ ] All interactive components include every state as a variant: idle, hover, focus, active, disabled, loading
- [ ] Components that hold data include empty and error variants
- [ ] Nested components are real instances, not detached copies
- [ ] Text layers use text styles / typography variables, not ad-hoc settings

---

## 4. Dev Mode Handoff

- [ ] File is organized into pages: Cover, Components, Screens, Archive
- [ ] Screens marked "Ready for dev" in Dev Mode — drafts are not
- [ ] Each screen is annotated for behavior: what is interactive, what animates
- [ ] Responsive intent shown: frames at 390px, 768px, 1280px (or annotated)
- [ ] Redlines for any spacing that cannot be inferred from Auto Layout
- [ ] Animation/transition intent documented (duration, easing token, trigger)
- [ ] Accessibility notes present: focus order, ARIA roles, contrast-checked pairs

---

## 5. Token Sync Pipeline

- [ ] Tokens Studio (or equivalent) connected and configured
- [ ] Variable export maps to `tokens/design-tokens.json` (W3C DTCG format)
- [ ] Style Dictionary transform produces `tokens.css` + `tokens-dark.css`
- [ ] Sync direction is documented (Figma → repo, or repo → Figma — pick one source of truth)
- [ ] A round-trip test confirms a Figma variable change reaches code unchanged

---

## 6. Pre-Delivery

- [ ] Unused components, styles, and variables removed or archived
- [ ] Cover page states: file purpose, owner, last-updated, status
- [ ] All "Ready for dev" screens pass the contrast check in Dev Mode
- [ ] Handoff paired with a written spec — see `templates/specs/frontend-tz.md`

---

## Final Gate

| Question | Answer |
|---|---|
| Can a developer pull every value from a variable, never a raw number? | Yes / No |
| Do Figma component names match the names in code and `patterns/`? | Yes / No |
| Does every interactive component show all its states as variants? | Yes / No |
| Is there one documented source of truth for tokens? | Yes / No |

---

*Checklist version: global-design-skill v1.0 — `integrations/figma/figma-handoff-checklist.md`*  
*Updated: 2026-05-20*  
*Related: `integrations/figma/variables-export-guide.md`, `integrations/figma/plugin-workflow.md`, `templates/specs/frontend-tz.md`, `checklists/frontend-handoff-review.md`*
