# Reference — Authoritative Sources

> The primary sources behind this skill's standards. When a rule states a threshold (contrast ratio, Core Web Vital, touch target) or a technique, the authority for it lives here. Cite these — not blog summaries — when a claim needs backing. Links verified current as of **May 2026**; specs and framework docs evolve, so re-check the dated facts before quoting them as today's state.

---

## Accessibility & Contrast

- **WCAG 2.2** — https://www.w3.org/TR/WCAG22/ — the contrast floors (4.5:1 body, 3:1 large/UI), focus-visible (§2.4.11), target size (§2.5.8). W3C Recommendation 5 Oct 2023 (updated Dec 2024); also ISO/IEC 40500:2025.
- **What's New in WCAG 2.2** — https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/ — the 9 success criteria added since 2.1.
- **WAI-ARIA Authoring Practices Guide (APG)** — https://www.w3.org/WAI/ARIA/apg/ — keyboard interaction + ARIA patterns for every widget (combobox, dialog, tabs, listbox).
- **MDN — ARIA** — https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA — roles, states, properties reference.
- **APCA (Advanced Perceptual Contrast Algorithm)** — https://www.myndex.com/APCA/ — the WCAG 3.0-track Lc contrast model used in `rules/19-contrast-standards.md` R11.

## Color — OKLCH

- **MDN — `oklch()`** — https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklch — syntax and browser support (Baseline since 2023).
- **Evil Martians — "OKLCH in CSS: why we moved from RGB and HSL"** — https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl — the rationale for perceptual uniformity behind `rules/04-color.md`.
- **OKLCH Color Picker & Converter** — https://oklch.com — interactive picker (Evil Martians) for building the OKLCH scales in this skill.

## Typography

- **MDN — `clamp()`** — https://developer.mozilla.org/en-US/docs/Web/CSS/clamp — the fluid type scale mechanism in `rules/03-typography.md` R1.
- **Butterick's Practical Typography** — https://practicaltypography.com — line length, line-height, and body-text legibility principles.
- **Adham Dannaway — "16 UI Design Tips"** — https://www.uxplanet.org/16-ui-design-tips-ba2e7524d203 — source of the x-height, left-align, and contrast guidance harvested into `rules/03-typography.md` R11–R12. Book: https://www.practical-ui.com.

## Motion & Animation

- **Motion (formerly Framer Motion)** — https://motion.dev/docs/react — the `motion/react` API in `rules/17-motion-react.md`. Renamed from `framer-motion` in 2025; import path is `motion/react`.
- **GSAP Docs + ScrollTrigger** — https://gsap.com/docs/v3/ · https://gsap.com/docs/v3/Plugins/ScrollTrigger/ — scroll choreography and `useGSAP`.
- **MDN — CSS scroll-driven animations** — https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll-driven_animations — `animation-timeline: view()/scroll()` (Baseline 2024).
- **MDN — `prefers-reduced-motion`** — https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion — the mandatory motion-preference gate.

## Performance & Core Web Vitals

- **web.dev — Web Vitals** — https://web.dev/articles/vitals — the three Core Web Vitals and their "good" thresholds: **LCP < 2.5s, INP < 200ms, CLS < 0.1** (75th percentile). INP replaced FID as a Core Web Vital in March 2024.
- **web.dev — LCP / INP / CLS** — https://web.dev/articles/lcp · https://web.dev/articles/inp · https://web.dev/articles/cls — per-metric optimization behind `rules/08-performance.md`.

## CSS Platform & Baseline

- **Baseline (web.dev)** — https://web.dev/baseline — feature support status used throughout "Technology Standards"; "Widely available" = 30 months across core browsers. Defined by the WebDX Community Group.
- **MDN — Baseline** — https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility · **Can I use** — https://caniuse.com — per-feature support checks.
- **MDN — `@starting-style`** https://developer.mozilla.org/en-US/docs/Web/CSS/@starting-style · **`@property`** https://developer.mozilla.org/en-US/docs/Web/CSS/@property · **Popover API** https://developer.mozilla.org/en-US/docs/Web/API/Popover_API · **Container queries** https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries · **Anchor positioning** https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_anchor_positioning — the CSS 2026 techniques cited inline in the rules.

## Frameworks (stack standards)

- **React 19** — https://react.dev/blog/2024/12/05/react-19 — `ref` as prop, `useActionState`, `useOptimistic`, `useFormStatus`.
- **Next.js 15** — https://nextjs.org/docs — async `cookies`/`headers`/`params`/`searchParams`, `"use cache"`, explicit `revalidate`.
- **Tailwind CSS v4** — https://tailwindcss.com/docs — CSS-first `@theme`, `@custom-variant dark` (no `tailwind.config.js`).

## UX Laws & Cognitive Design

- **Laws of UX — Jon Yablonski** — https://lawsofux.com — Hick's, Fitts's, Miller's, Doherty, Jakob's, plus Gestalt and cognitive biases. Book: *Laws of UX* (O'Reilly, 2020/2024).
- **Nielsen Norman Group** — https://www.nngroup.com — usability heuristics, evidence-based UX research.
- **Don Norman — *The Design of Everyday Things*** (Basic Books, revised ed. 2013) — affordances, mapping, the gulf of evaluation behind feedback rules.
- **Baymard Institute** — https://baymard.com — large-sample form, checkout, and e-commerce UX research.

## Design Systems (reference implementations)

- **Material Design 3** — https://m3.material.io — color roles, state layers, elevation, type scale (note: `m3`, not legacy `m2`).
- **Apple Human Interface Guidelines** — https://developer.apple.com/design/human-interface-guidelines — 44pt touch-target baseline, platform conventions.
- **Ant Design** — https://ant.design — dense enterprise/admin component conventions and feedback patterns.
- **GOV.UK Design System** — https://design-system.service.gov.uk — accessibility-first, research-backed form and component patterns. Code MIT; content under Open Government Licence.
- **USWDS (U.S. Web Design System)** — https://designsystem.digital.gov — government-grade UX: forms, alerts, accordions, search, banners, service patterns.
- **Microsoft Fluent UI** — https://developer.microsoft.com/fluentui — Microsoft 365 patterns for enterprise, dashboards, productivity apps. Fluent UI React is MIT; fonts/icons have separate asset terms.
- **IBM Carbon Design System** — https://carbondesignsystem.com — B2B, industrial, data-heavy enterprise SaaS.
- **Shopify Polaris** — https://polaris.shopify.com — ecommerce, seller dashboards, product-admin UI.
- **Atlassian Design System** — https://atlassian.design — B2B SaaS, project/task managers, statuses, tables, docs.

---

*Reference version: global-design-skill v1.9.3 — `references/sources.md`*
*Related: every `rules/*.md` (claims) · `references/tech-standards.md` (stack snippets) · `rules/19-contrast-standards.md` (WCAG/APCA) · `rules/04-color.md` (OKLCH)*
