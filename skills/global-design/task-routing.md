# Task Routing

> Match the incoming task to the right set of files. Load only what's relevant — not the entire system. All paths are relative to the repository root.

---

## How to Route

1. Read the user's request
2. Find the matching row below
3. Load the listed files before responding
4. Blueprint first, then patterns, then rules
5. When in doubt: load the blueprint + the most specific rules file

---

## Build From Scratch

| Task | Blueprint | Key rules | Patterns | Checklist |
|---|---|---|---|---|
| Landing page (standard) | `blueprints/landing-page-from-scratch.md` | `rules/14-landing-pages.md` | `patterns/marketing-blocks/` | `checklists/landing-conversion-review.md` |
| Landing page (wow/interactive) | `blueprints/interactive-landing-page.md` | `rules/14-landing-pages.md` `rules/05-animation.md` | `patterns/marketing-blocks/` `patterns/effects/` | `checklists/landing-conversion-review.md` `checklists/wow-effects-checklist.md` |
| SaaS app / product | `blueprints/saas-app-from-scratch.md` | `rules/13-saas-products.md` | `patterns/product-ui/` | `checklists/ui-review.md` |
| Admin panel | `blueprints/admin-panel-from-scratch.md` | `rules/12-admin-panels.md` | `patterns/admin-ui/` | `checklists/ui-review.md` |
| Multi-page website | `blueprints/website-from-scratch.md` (Step 0: lock the MASTER → `templates/specs/design-system-master.md`) | `rules/14-landing-pages.md` `rules/02-layout-and-grid.md` | `patterns/marketing-blocks/` `patterns/navigation/` | `checklists/global-design-review.md` |
| Pricing page | `blueprints/pricing-page-from-scratch.md` | `rules/14-landing-pages.md` | `patterns/marketing-blocks/pricing-sections.md` `patterns/marketing-blocks/comparison-sections.md` | `checklists/landing-conversion-review.md` |
| Portfolio site | `blueprints/portfolio-from-scratch.md` | `rules/01-visual-hierarchy.md` `rules/03-typography.md` | `patterns/effects/` `references/portfolios.md` | `checklists/global-design-review.md` |
| Onboarding flow | `blueprints/onboarding-flow-from-scratch.md` | `rules/13-saas-products.md` | `patterns/product-ui/onboarding.md` `patterns/product-ui/forms.md` | `checklists/ui-review.md` |
| Redesign existing page | `blueprints/redesign-existing-page.md` | relevant domain rule | — | `checklists/global-design-review.md` |
| Site in one prompt (autonomous, no dialogue) | `rules/21-one-shot-build.md` → blueprint for the site type | `rules/00-escalation-protocol.md` `rules/20-rendered-verification.md` | per blueprint | `checklists/global-design-review.md` |

---

## Visual Effects Tasks

> For any task involving animations, motion, atmosphere, or "wow" factor.

| Task | Primary file | Supporting files |
|---|---|---|
| Add grain/mesh/spotlight/glow | `patterns/effects/visual-effects.md` | `tokens/tokens.css` |
| Add parallax (any type) | `patterns/effects/parallax-system.md` | `rules/05-animation.md` |
| Add text animations | `patterns/effects/text-animations.md` | `rules/03-typography.md` |
| Add scroll experiences | `patterns/effects/scroll-experiences.md` | `rules/05-animation.md` |
| Add hover effects | `patterns/effects/hover-effects.md` | `rules/06-components.md` |
| Add cursor effects | `patterns/effects/cursor-effects.md` | — |
| Add 3D effects | `patterns/effects/3d-effects.md` | `rules/05-animation.md` |
| Add page transitions | `recipes/add-page-transitions.md` | `patterns/effects/scroll-experiences.md` |
| Make hero wow | `recipes/create-wow-hero.md` | `patterns/effects/visual-effects.md` `patterns/effects/hover-effects.md` |
| Make page more premium | `recipes/make-page-more-premium.md` | `patterns/effects/visual-effects.md` |
| Add animations (general) | `recipes/add-animations.md` | `patterns/effects/text-animations.md` `patterns/effects/scroll-experiences.md` |
| Full wow landing page | `blueprints/interactive-landing-page.md` | `patterns/effects/` (all) |
| Review effects quality | `checklists/wow-effects-checklist.md` | `rules/05-animation.md` |

---

## Specific UI Component Tasks

| Task | Files |
|---|---|
| Hero section | `patterns/marketing-blocks/hero-sections.md` + `recipes/improve-hero-section.md` |
| Pricing section | `patterns/marketing-blocks/pricing-sections.md` + `references/pricing-pages.md` |
| Feature section | `patterns/marketing-blocks/feature-sections.md` |
| Social proof / testimonials | `patterns/marketing-blocks/social-proof.md` |
| Stats section | `patterns/marketing-blocks/stats-sections.md` |
| CTA section | `patterns/marketing-blocks/cta-sections.md` |
| FAQ section | `patterns/marketing-blocks/faq-sections.md` |
| Comparison table | `patterns/marketing-blocks/comparison-sections.md` |
| Top navigation / header | `patterns/navigation/header-patterns.md` + `references/navigation-examples.md` |
| Sidebar navigation | `patterns/navigation/sidebar-patterns.md` + `references/navigation-examples.md` |
| Mobile navigation | `patterns/navigation/mobile-navigation.md` |
| Tabs | `patterns/navigation/tabs-patterns.md` |
| Breadcrumbs | `patterns/navigation/breadcrumbs.md` |
| Pagination | `patterns/navigation/pagination.md` |
| Data table | `patterns/admin-ui/data-tables.md` + `rules/11-data-tables.md` |
| Charts / dashboard | `patterns/admin-ui/charts.md` + `patterns/admin-ui/dashboard-layouts.md` |
| Filters | `patterns/admin-ui/filters.md` |
| Bulk actions | `patterns/admin-ui/bulk-actions.md` |
| Form / inputs | `patterns/product-ui/forms.md` + `rules/10-forms.md` |
| Onboarding wizard | `patterns/product-ui/onboarding.md` |
| Empty states | `patterns/product-ui/empty-states.md` |
| Error states | `patterns/product-ui/error-states.md` |
| Loading states | `patterns/product-ui/loading-states.md` + `recipes/improve-loading-states.md` |
| Settings page | `patterns/product-ui/settings-pages.md` |
| Modal / dialog | `patterns/product-ui/modals.md` + `rules/07-accessibility.md` |
| Notifications / toast | `patterns/product-ui/notifications.md` |
| Search | `patterns/product-ui/search.md` |
| Tooltips / popovers | `patterns/product-ui/tooltips-popovers.md` |
| Command palette | `patterns/product-ui/command-palette.md` |
| Icons | `rules/15-iconography.md` |

---

## Review and Audit Tasks

| Task | Agent | Files |
|---|---|---|
| Full design audit | `agents/design-director.md` + `agents/design-critic.md` | `checklists/global-design-review.md` |
| UX / user flow audit | `agents/ux-architect.md` | `checklists/ui-review.md` |
| Landing page conversion audit | `agents/conversion-designer.md` | `checklists/landing-conversion-review.md` |
| Accessibility audit | `agents/accessibility-auditor.md` | `rules/07-accessibility.md` |
| Performance audit | `agents/performance-auditor.md` | `rules/08-performance.md` |
| Copy / headline audit | `agents/copy-editor.md` | `rules/14-landing-pages.md` |
| Motion / animation audit | `agents/motion-designer.md` | `rules/05-animation.md` `checklists/wow-effects-checklist.md` |
| Design system / token audit | `agents/design-systems-auditor.md` | `tokens/tokens.css` `tokens/tokens-dark.css` |
| Frontend handoff review | `agents/frontend-handoff-reviewer.md` | `templates/specs/frontend-tz.md` |
| Banned patterns scan | `agents/design-critic.md` | `checklists/global-design-review.md` |
| UI component review | — | `checklists/ui-review.md` |
| Verify rendered result / "looks right in source but breaks live" | — | `rules/20-rendered-verification.md` + `references/live-audit-snippets.md` |
| Find real design references | `agents/reference-hunter.md` | `references/inspiration-sites.md` `references/aesthetic-archetypes.md` |
| Audit a live URL | `agents/reference-hunter.md` (Capability 4) | `quality-gates.md` |
| Competitive analysis | `agents/reference-hunter.md` (Capability 3) | `references/saas-ui-examples.md` |

---

## Improvement Recipes

| Task | Recipe |
|---|---|
| Make design more premium | `recipes/make-page-more-premium.md` |
| Clean up cluttered interface | `recipes/make-interface-cleaner.md` |
| Improve hero section | `recipes/improve-hero-section.md` |
| Create wow hero from scratch | `recipes/create-wow-hero.md` |
| Improve pricing page | `recipes/improve-pricing-page.md` |
| Improve forms | `recipes/improve-forms.md` |
| Add dark mode | `recipes/add-dark-mode.md` |
| Improve mobile version | `recipes/improve-mobile-version.md` |
| Fix empty states | `recipes/improve-empty-states.md` |
| Improve navigation | `recipes/improve-navigation.md` |
| Improve typography | `recipes/improve-typography.md` |
| Add animations | `recipes/add-animations.md` |
| Improve loading states | `recipes/improve-loading-states.md` |
| Improve onboarding | `recipes/improve-onboarding.md` |
| Add page transitions | `recipes/add-page-transitions.md` |
| Extract a design system from a reference (image / site / Figma) | `recipes/extract-design-from-reference.md` + `templates/specs/design-system-master.md` |

---

## Output Templates

| Output needed | Template |
|---|---|
| Developer handoff spec | `templates/specs/frontend-tz.md` |
| Component specification | `templates/specs/component-spec.md` |
| Design review report | `templates/specs/design-review-report.md` |
| Design-system source of truth (multi-page consistency) | `templates/specs/design-system-master.md` |
| New project brief | `templates/briefs/project-brief.md` |
| Redesign brief | `templates/briefs/redesign-brief.md` |

---

## Rules by Domain

Load the relevant rule alongside any blueprint or pattern.

| Domain | Rule file |
|---|---|
| Visual hierarchy | `rules/01-visual-hierarchy.md` |
| Layout and grid | `rules/02-layout-and-grid.md` |
| Typography | `rules/03-typography.md` |
| Color (OKLCH) | `rules/04-color.md` |
| Animation and motion | `rules/05-animation.md` + `patterns/effects/` |
| Components | `rules/06-components.md` |
| Accessibility (WCAG 2.2) | `rules/07-accessibility.md` |
| Performance (CWV) | `rules/08-performance.md` |
| Responsive design | `rules/09-responsive.md` |
| Forms | `rules/10-forms.md` |
| Data tables | `rules/11-data-tables.md` |
| Admin panels | `rules/12-admin-panels.md` |
| SaaS products | `rules/13-saas-products.md` |
| Landing pages | `rules/14-landing-pages.md` |
| Iconography | `rules/15-iconography.md` |
| Design for SEO | `rules/16-design-for-seo.md` |
| Motion / React | `rules/17-motion-react.md` |
| CSS framework selection | `rules/18-css-framework-selection.md` |
| Contrast standards (WCAG/APCA) | `rules/19-contrast-standards.md` |
| Rendered verification (render → audit → fix) | `rules/20-rendered-verification.md` + `references/live-audit-snippets.md` |
| Escalation protocol (request depth) | `rules/00-escalation-protocol.md` |
| One-shot autonomous build (single prompt) | `rules/21-one-shot-build.md` |

---

## Reference Files (Curated Examples)

Load when the task involves finding, studying, or referencing real-world examples.

| Need | Reference file |
|---|---|
| Site galleries / inspiration sources | `references/inspiration-sites.md` |
| Archetype A–H real examples | `references/aesthetic-archetypes.md` |
| SaaS UI patterns in production | `references/saas-ui-examples.md` |
| Best marketing/landing pages | `references/marketing-sites.md` |
| Best portfolio sites | `references/portfolios.md` |
| Best pricing pages | `references/pricing-pages.md` |
| Navigation in real products | `references/navigation-examples.md` |

---

## Decision Tree for Ambiguous Requests

```
"Help me with the design" / "Make something"
  └── Ask: landing page / app / portfolio / component?

"Make it look better" / "Improve this"
  └── Run: agents/design-director.md first
      Then: relevant recipe from recipes/

"Make it wow" / "Add effects" / "Make it impressive"
  └── Load: recipes/create-wow-hero.md (if hero)
      Or: patterns/effects/ (specific effect type)
      Or: blueprints/interactive-landing-page.md (full page)

"Build X from scratch"
  └── Load: blueprints/[type]-from-scratch.md
      Then: relevant rules/ + patterns/

"Add parallax / animations / transitions"
  └── Load: patterns/effects/[matching file]
      Check: rules/05-animation.md (easing, reduced-motion)

"Find examples" / "Show references"
  └── Load: agents/reference-hunter.md
      Then: references/[matching category]

"Audit this" / "Review this"
  └── Load: agents/design-critic.md (banned patterns first)
      Then: checklists/global-design-review.md

"Write a spec" / "Handoff"
  └── Load: templates/specs/frontend-tz.md
      Gate check: quality-gates.md
```

---

*Routing version: global-design-skill v2.5.0 — `task-routing.md`*  
*Updated: 2026-06-11*
