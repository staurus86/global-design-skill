# Task Routing

> Match the incoming task to the right set of files. Load only what's relevant — not the entire system.

---

## How to route

1. Read the user's request
2. Find the matching row below
3. Load the listed files before responding
4. If multiple task types apply, start with the blueprint, then load patterns

---

## Routing Table

### Build from scratch

| Task | Blueprint | Rules | Patterns | Checklist |
|---|---|---|---|---|
| Landing page | `blueprints/landing-page-from-scratch.md` | `rules/14-landing-pages.md` | `patterns/marketing-blocks/` | `checklists/landing-conversion-review.md` |
| SaaS product / app | `blueprints/saas-app-from-scratch.md` | `rules/13-saas-products.md` | `patterns/product-ui/` | `checklists/ui-review.md` |
| Admin panel | `blueprints/admin-panel-from-scratch.md` | `rules/12-admin-panels.md` | `patterns/admin-ui/` | `checklists/admin-panel-review.md` |
| Dashboard / analytics | `blueprints/dashboard-from-scratch.md` | `rules/11-tables-and-data-ui.md` | `patterns/admin-ui/dashboard-layouts.md` | `checklists/dashboard-review.md` |
| Marketing website | `blueprints/website-from-scratch.md` | `rules/14-landing-pages.md` `rules/02-layout-and-grid.md` | `patterns/marketing-blocks/` `patterns/navigation/` | `checklists/global-design-review.md` |
| Redesign | `blueprints/redesign-existing-page.md` | relevant domain rule | — | `checklists/global-design-review.md` |

---

### Specific UI tasks

| Task | Files |
|---|---|
| Hero section | `patterns/marketing-blocks/hero-sections.md` |
| Pricing page | `patterns/marketing-blocks/pricing-sections.md` + `rules/14-landing-pages.md` |
| Navigation / header | `patterns/navigation/header-patterns.md` |
| Sidebar | `patterns/navigation/sidebar-patterns.md` |
| Data table | `patterns/admin-ui/data-tables.md` + `references/data-viz.md` |
| Charts / KPI | `references/data-viz.md` |
| Form / inputs | `references/forms.md` + `rules/10-forms-and-inputs.md` |
| Onboarding flow | `patterns/product-ui/onboarding.md` |
| Empty states | `patterns/product-ui/empty-states.md` |
| Error states | `patterns/product-ui/error-states.md` |
| Loading states | `patterns/product-ui/loading-states.md` |
| Settings page | `patterns/product-ui/settings-pages.md` |
| Modal / dialog | `references/accessibility.md` (focus trap) + CSS `dialog:open` pattern |
| Testimonials / social proof | `patterns/marketing-blocks/social-proof.md` |
| FAQ | `patterns/marketing-blocks/faq-sections.md` |
| CTA section | `patterns/marketing-blocks/cta-sections.md` |
| Filters | `patterns/admin-ui/filters.md` |
| Mobile navigation | `patterns/navigation/mobile-navigation.md` |

---

### Review and audit tasks

| Task | Files |
|---|---|
| Full UX audit | `checklists/ux-review.md` + `templates/outputs/ux-audit-report.md` |
| Full UI audit | `checklists/ui-review.md` + `checklists/global-design-review.md` |
| Mobile review | `checklists/mobile-review.md` + `references/responsive.md` |
| Accessibility audit | `checklists/accessibility-review.md` + `references/accessibility.md` |
| Landing conversion audit | `checklists/landing-conversion-review.md` |
| Form review | `checklists/forms-review.md` + `references/forms.md` |
| Frontend handoff review | `checklists/frontend-handoff-review.md` |

---

### Output tasks

| Task | Files |
|---|---|
| Write frontend ТЗ | `templates/specs/frontend-tz.md` |
| Write design spec | `templates/specs/design-spec.md` |
| Write component spec | `templates/specs/component-spec.md` |
| Create project brief | `templates/briefs/project-brief.md` |
| Create landing brief | `templates/briefs/landing-brief.md` |
| Generate vibe coding prompt | `templates/prompts/generate-landing.md` or `generate-admin.md` |
| Write UX audit report | `templates/outputs/ux-audit-report.md` |

---

### Improvement recipes

| Task | File |
|---|---|
| Make design more premium | `recipes/make-page-more-premium.md` |
| Clean up a cluttered interface | `recipes/make-interface-cleaner.md` |
| Improve hero section | `recipes/improve-hero-section.md` |
| Improve pricing page | `recipes/improve-pricing-page.md` |
| Improve forms | `recipes/improve-forms.md` |
| Add dark mode | `recipes/add-dark-mode.md` |
| Improve mobile version | `recipes/improve-mobile-version.md` |
| Fix empty states | `recipes/improve-empty-states.md` |

---

### Rules by domain

Always load the relevant domain rule alongside the blueprint.

| Domain | Rule file |
|---|---|
| Visual hierarchy | `rules/01-visual-hierarchy.md` |
| Layout and grid | `rules/02-layout-and-grid.md` |
| Typography | `rules/03-typography.md` → `references/typography.md` |
| Color systems | `rules/04-color-systems.md` → `references/color-alchemy.md` |
| Spacing and density | `rules/05-spacing-and-density.md` → `references/tokens.md` |
| Components | `rules/06-components.md` |
| Responsive design | `rules/07-responsive-design.md` → `references/responsive.md` |
| Accessibility | `rules/08-accessibility.md` → `references/accessibility.md` |
| Motion and effects | `rules/09-motion-and-effects.md` → `references/motion-systems.md` |
| Forms and inputs | `rules/10-forms-and-inputs.md` → `references/forms.md` |
| Tables and data UI | `rules/11-tables-and-data-ui.md` → `references/data-viz.md` |
| Admin panels | `rules/12-admin-panels.md` |
| SaaS products | `rules/13-saas-products.md` |
| Landing pages | `rules/14-landing-pages.md` |
| Design for SEO | `rules/16-design-for-seo.md` |

---

## Decision tree for ambiguous requests

```
"Help me with the design"
  └── Ask: What type? (landing / app / admin / component / audit)

"Make it look better"
  └── Run: checklists/global-design-review.md first
      Then: relevant recipe from recipes/

"Build X from scratch"
  └── Load: blueprints/[type]-from-scratch.md
      Then: relevant rules + patterns

"Write a spec"
  └── Ask: For whom? (developer → frontend-tz.md / designer → design-spec.md)

"Audit this"
  └── Ask: UX or UI? Specific domain?
      UX → checklists/ux-review.md
      UI → checklists/ui-review.md
      Conversion → checklists/landing-conversion-review.md
```
