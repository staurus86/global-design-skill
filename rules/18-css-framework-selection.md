# Rule 18 — CSS Framework Selection

> Every project uses a CSS framework. This rule runs first on any design or build task. It detects which framework is in use, routes to the correct profile, and asks when detection fails.

---

## Step 1 — Auto-Detect from package.json

Read `package.json` (both `dependencies` and `devDependencies`). First match wins:

| Detected dependency | Framework |
|---|---|
| `tailwindcss` | Tailwind — no additional profile needed, all global-design-skill rules apply as-is |
| `bootstrap` | Bootstrap → load `integrations/frameworks/bootstrap/profile.md` |
| `bulma` | Bulma → load `integrations/frameworks/bulma/profile.md` |
| `unocss` | UnoCSS → load `integrations/frameworks/unocss/profile.md` |
| `@pandacss/dev` | Panda CSS → load `integrations/frameworks/panda-css/profile.md` |
| `open-props` | Open Props → load `integrations/frameworks/open-props/profile.md` |
| _(none found)_ | → go to Step 2 |

If `package.json` does not exist (new project, repo root, vanilla HTML): → go to Step 2.

---

## Step 2 — Ask When Uncertain

If no framework was detected, ask exactly one question before any design work:

> "Which CSS framework are we using?
> - **Tailwind** (default for React/Next.js)
> - **Bootstrap** (components, enterprise, vanilla)
> - **Bulma** (CSS-only, no JS)
> - **UnoCSS** (Tailwind alternative, faster builds)
> - **Panda CSS** (type-safe, React/Next.js)
> - **Open Props** (token layer, any stack)
> - **Other / none** (vanilla CSS)"

If user answers "Other" or names an unsupported framework: apply all standard global-design-skill rules and note: _"No specific profile for [framework] — applying universal design rules."_

---

## Step 3 — Recommendation Matrix

When starting a brand-new project with no framework installed, recommend based on project type:

| Project type | Recommend |
|---|---|
| React + Next.js, new project | **Tailwind v4** (ecosystem default) |
| React + Next.js, design system, TypeScript | **Panda CSS** (type-safe tokens) |
| Migrating from Tailwind, need more flexibility | **UnoCSS** |
| Vanilla HTML, needs components fast | **Bootstrap 5** |
| Vanilla HTML, CSS-only, no JS budget | **Bulma** |
| Any stack, building custom token system | **Open Props** |
| Enterprise org already using Bootstrap | **Bootstrap 5** |

State your recommendation with one sentence of reasoning. Wait for confirmation before proceeding.

---

## Step 4 — Load Profile

After detection or confirmation, load the profile:

| Framework | Profile path |
|---|---|
| Bootstrap | `integrations/frameworks/bootstrap/profile.md` |
| Bulma | `integrations/frameworks/bulma/profile.md` |
| Open Props | `integrations/frameworks/open-props/profile.md` |
| UnoCSS | `integrations/frameworks/unocss/profile.md` |
| Panda CSS | `integrations/frameworks/panda-css/profile.md` |
| Tailwind | _(no profile — default rules apply)_ |

State once: _"Using [Framework]. Applying framework profile alongside global-design-skill rules."_

---

## Important: Framework Rules Are Additive

Framework profiles do **not** override global-design-skill rules. All of the following always apply regardless of framework:

- OKLCH colors — never raw hex
- `clamp()` for all display type
- `motion/react` for animations — never `framer-motion`
- Escalation protocol (`rules/00-escalation-protocol.md`)
- Accessibility: WCAG 2.2 AA, 44px touch targets, focus-visible
- Banned patterns from `checklists/global-design-review.md`
- Breakpoints: 390px / 768px / 1280px minimum
