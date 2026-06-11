# Reference — Authoritative Sources

> The primary sources behind this skill's standards. When a rule states a threshold (contrast ratio, Core Web Vital, touch target) or a technique, the authority for it lives here. Cite these — not blog summaries — when a claim needs backing. Links verified current as of **May 2026**; specs and framework docs evolve, so re-check the dated facts before quoting them as today's state.
>
> **The anti-slop floor.** Generic AI sites fail *below* the visual layer first: non-semantic `<div>` soup, ad-hoc CSS with random magic numbers, inaccessible custom controls, features used "because trendy" without a Baseline check, unvalidated markup. A site is not "not slop" because it looks nice — it earns that only on a foundation of correct semantics, a systematic CSS architecture (cascade layers + tokens), keyboard/AT access, verified browser support, and clean validation. The specs and tools below are that floor; the *ceiling* — the visual and interaction tells with concrete fixes — lives in `references/anti-slop-system.md`.

---

## Web Platform Specifications

The source of truth for HTML semantics and JS — get the structure right before any visual layer.

- **W3C Web Standards (catalog)** — https://www.w3.org/standards/ — top-level index of HTML/CSS/a11y/i18n/API standards; use as the upper catalog, not a tutorial.
- **WHATWG HTML Living Standard** — https://html.spec.whatwg.org/multipage/ — the authority for semantic elements, document structure, forms, interactivity. Correct HTML (`header`/`main`/`nav`/`section`/`article`/`button`/`label`) is the anti-slop foundation.
- **WHATWG DOM Standard** — https://dom.spec.whatwg.org/ — the document tree, events, `EventTarget`, mutations — how JS actually operates on HTML.
- **WHATWG Fetch Standard** — https://fetch.spec.whatwg.org/ — `fetch`, CORS, request/response, resource loading (frontend, performance, security).
- **WHATWG URL Standard** — https://url.spec.whatwg.org/ — URL/domain/query/`form-urlencoded` parsing (routing, canonical, filters, params).
- **WHATWG Encoding Standard** — https://encoding.spec.whatwg.org/ — UTF-8, legacy encodings, `TextEncoder`/`TextDecoder` (mandatory for multilingual sites).
- **ECMA-262 / ECMAScript** — https://ecma-international.org/publications-and-standards/standards/ecma-262/ — the JS language itself (types, syntax, runtime model) — not a React guide.
- **Web IDL Standard** — https://webidl.spec.whatwg.org/ — how specs describe browser interfaces and bind them to JavaScript.

## CSS Specifications

The authority behind systematic CSS — cascade layers, tokens, values, color. Random `margin: 37px` and specificity wars are slop; these define the system that prevents them.

- **CSS Snapshot** — https://www.w3.org/TR/css-2024/ — which CSS modules define the current state of CSS (status map, not a tutorial).
- **CSS Cascading and Inheritance Level 5** — https://www.w3.org/TR/css-cascade-5/ — the cascade, inheritance, specificity, and `@layer` cascade layers behind a maintainable architecture.
- **CSS Values and Units Level 4** — https://www.w3.org/TR/css-values-4/ — value types, functions, units behind fluid typography, `clamp()`, responsive spacing, viewport units.
- **CSS Color Module Level 4** — https://www.w3.org/TR/css-color-4/ — modern color: `oklch()`, `color-mix()`, new color spaces, opacity (the spec under `rules/04-color.md`).

## Accessibility & Contrast

- **WCAG 2.2** — https://www.w3.org/TR/WCAG22/ — the contrast floors (4.5:1 body, 3:1 large/UI), focus-visible (§2.4.11), target size (§2.5.8). W3C Recommendation 5 Oct 2023 (updated Dec 2024); also ISO/IEC 40500:2025.
- **WCAG Quick Reference (How to Meet WCAG)** — https://www.w3.org/WAI/WCAG22/quickref/ — filterable criteria by A/AA/AAA + techniques; the official source to turn into an agent/dev checklist.
- **What's New in WCAG 2.2** — https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/ — the 9 success criteria added since 2.1.
- **WAI-ARIA 1.2 (spec)** — https://www.w3.org/TR/wai-aria-1.2/ — roles, states, properties for complex widgets. Use sparingly: native HTML first, ARIA only where HTML cannot express the semantics.
- **WAI-ARIA Authoring Practices Guide (APG)** — https://www.w3.org/WAI/ARIA/apg/ — keyboard interaction + ARIA patterns for every widget (combobox, dialog, tabs, listbox). Keeps "unique" custom blocks from being pretty-but-broken.
- **MDN — ARIA** — https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA — roles, states, properties reference.
- **APCA (Advanced Perceptual Contrast Algorithm)** — https://www.myndex.com/APCA/ — the WCAG 3.0-track Lc contrast model used in `rules/19-contrast-standards.md` R11.

## Internationalization & Text

- **W3C Internationalization (i18n)** — https://www.w3.org/International/ — languages, scripts, text direction, locales; the authority for RTL UI, `hreflang`, and multilingual layout (RU/EN/AR).
- **Unicode Standard** — https://www.unicode.org/standard/standard.html — characters, scripts, emoji, normalization — correct text in search, forms, and multilingual content.

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
- **Google — Core Web Vitals & Search** — https://developers.google.com/search/docs/appearance/core-web-vitals — how CWV feed Google's page-experience signal.
- **W3C — Navigation Timing Level 2** — https://www.w3.org/TR/navigation-timing-2/ — the spec for measuring navigation/document-load timing (real-user metrics).
- **W3C — Resource Hints** — https://www.w3.org/TR/resource-hints/ — `dns-prefetch`, `preconnect`, `prefetch`, `prerender` to warm up critical resources early.
- **MDN — Lazy loading** — https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Lazy_loading — defer non-critical media (`loading="lazy"`), never the LCP image.

**Performance is a design constraint, not a post-ship fix.** Every block has a budget: hero weight, font count, JS bundle, the LCP image, animation cost. Design that breaks the budget is not done.

## HTTP & Networking

How the site is actually delivered — beautiful markup over a chaos of statuses, redirects, and cache headers is still a broken product.

- **RFC 9110 — HTTP Semantics** — https://www.rfc-editor.org/rfc/rfc9110.html — methods, status codes, headers, URI semantics; the authority for 200/301/302/404/410, canonical logic, forms, and error responses.
- **RFC 9111 — HTTP Caching** — https://www.rfc-editor.org/rfc/rfc9111.html — `Cache-Control`, `Age`, cacheable responses (SEO, speed, CDN).
- **RFC 9112 / 9113 / 9114 — HTTP/1.1 · HTTP/2 · HTTP/3** — https://www.rfc-editor.org/rfc/rfc9112.html · …/rfc9113.html · …/rfc9114.html — which protocol the project runs on and how it affects speed (technical audit).

## Security (headers & frontend)

Every template needs a security pass: HTTPS, CSP, HSTS, safe external scripts, no inline chaos, safe forms, XSS protection.

- **Content-Security-Policy (CSP)** — https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP — control which resources a page may load; primary XSS/injection defense.
- **Strict-Transport-Security (HSTS)** — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security — force HTTPS on future visits.
- **Permissions-Policy** — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy — allow/deny camera, mic, geolocation, fullscreen, etc.
- **Referrer-Policy** — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy — how much referrer info leaks on navigation.
- **COOP / CORP / CORS** — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Opener-Policy — cross-origin isolation and resource-loading rules.
- **OWASP Cheat Sheet Series** — https://cheatsheetseries.owasp.org/ — practical guides: auth, input validation, XSS, CSRF, file upload, API security.

## SEO & Machine-Readability

Every page is designed for the crawler/AI reader too: title, description, canonical, `hreflang`, schema, breadcrumbs, sitemap, robots, clean semantics. See `rules/16-design-for-seo.md`.

- **Google Search Essentials** — https://developers.google.com/search/docs/essentials — baseline requirements to appear and work in Google Search.
- **RFC 9309 — Robots Exclusion Protocol** — https://www.rfc-editor.org/rfc/rfc9309.html — the `robots.txt` standard (note: not an access-authorization mechanism).
- **Sitemaps Protocol** — https://www.sitemaps.org/protocol.html — XML sitemap format, UTF-8, entity escaping, sitemap index.
- **Robots meta / X-Robots-Tag** — https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag — `noindex`, `nofollow`, `nosnippet`, snippet limits.
- **Schema.org** — https://schema.org/ — structured-data vocabulary for pages, products, organizations, articles, FAQ, events.

## Social Preview

A page can look great and share terribly. Every important page needs a share card: OG image 1200×630, real title + description, messenger fallback.

- **Open Graph Protocol** — https://ogp.me/ — `og:title`, `og:description`, `og:image`, `og:url`, `og:type` to become a rich object in social graphs.

## PWA & Offline

For SaaS / dashboards / tools / web apps — check manifest, icons, offline fallback, install + update behavior.

- **W3C — Web App Manifest** — https://www.w3.org/TR/appmanifest/ — app metadata: name, icons, `start_url`, launch behavior.
- **W3C — Service Workers** — https://www.w3.org/TR/service-workers/ — background scripts for offline, caching, push.

## Service Files (`.well-known` & site metadata)

For modern SEO/GEO/AI-visibility projects, verify `/robots.txt`, `/sitemap.xml`, `/.well-known/security.txt`, `/humans.txt`, `/llms.txt`.

- **RFC 8615 — Well-Known URIs** — https://datatracker.ietf.org/doc/html/rfc8615 — the standard `/.well-known/` path.
- **RFC 9116 — security.txt** — https://datatracker.ietf.org/doc/rfc9116/ — machine-readable vulnerability-disclosure contact.
- **humans.txt** — https://humanstxt.org/ — initiative (not a formal standard) crediting the people/tech behind a site.
- **llms.txt** — https://llmstxt.org/ — *proposal* (not a mature standard) giving LLMs a curated context file. GEO/AI-visibility work is owned by the separate `geo` skill — cross-reference, don't duplicate it here.

## CSS Platform & Baseline

- **Baseline (web.dev)** — https://web.dev/baseline — feature support status used throughout "Technology Standards"; "Widely available" = 30 months across core browsers. Defined by the WebDX Community Group.
- **MDN — Baseline** — https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility · **Can I use** — https://caniuse.com — per-feature support checks.
- **MDN Browser Compatibility Data (BCD)** — https://github.com/mdn/browser-compat-data — machine-readable support data powering MDN/IDEs; the programmatic source for "is this feature safe?".
- **Chrome Platform Status** — https://chromestatus.com — feature status, origin trials, shipping status in Chrome/Chromium.
- **MDN — `@starting-style`** https://developer.mozilla.org/en-US/docs/Web/CSS/@starting-style · **`@property`** https://developer.mozilla.org/en-US/docs/Web/CSS/@property · **Popover API** https://developer.mozilla.org/en-US/docs/Web/API/Popover_API · **Container queries** https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries · **Anchor positioning** https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_anchor_positioning — the CSS 2026 techniques cited inline in the rules.

**Feature-use rule:** before using a CSS/JS feature, confirm it on Baseline (or BCD/Can I use) — "trendy" is not a support guarantee. If it's not Widely Available, gate it behind `@supports` or provide a fallback.

## Design Tokens & Component Standards

- **Design Tokens Community Group (DTCG)** — https://www.designtokens.org/ — the W3C Community Group format for color/type/spacing/radius/shadow/theme tokens. This skill's `tokens/design-tokens.json` already uses the DTCG `$value`/`$type` schema; this is its spec.
- **Open UI** — https://open-ui.org/ — W3C Community Group standardizing native UI controls (`select`, checkbox, radio, date/color pickers). Build custom components against the platform direction — unique without being broken.

## Validation, Linting & Quality Tools

The verifiable floor. These don't make a design beautiful; they remove the technical slop underneath it. Wire them into the workflow (see `validators/` for CI recipes).

- **W3C Markup Validation Service** — https://validator.w3.org/ · **Nu Html Checker** — https://validator.w3.org/nu — validate HTML on templates, articles, cards, landings (Nu is the modern HTML5 checker, CI-friendly).
- **W3C CSS Validation Service** — https://jigsaw.w3.org/css-validator/ — CSS syntax errors (not design quality).
- **W3C Link Checker** — https://validator.w3.org/checklink — broken links, redirects, fragment problems on large sites/docs.
- **Lighthouse** — https://developer.chrome.com/docs/lighthouse/overview — automated performance / a11y / SEO / best-practices audit; catches baseline technical slop (does not replace manual review). Targets in `rules/08-performance.md`.
- **Stylelint** — https://stylelint.io/ · **ESLint** — https://eslint.org/docs/latest/ · **Prettier** — https://prettier.io/docs — CSS/JS linting + formatting; enforce conventions, end manual style debates.
- **Google HTML/CSS Style Guide** — https://google.github.io/styleguide/htmlcssguide.html — practical (non-W3C) code-style reference for consistency.

## Frameworks (stack standards)

- **React 19** — https://react.dev/blog/2024/12/05/react-19 — `ref` as prop, `useActionState`, `useOptimistic`, `useFormStatus`.
- **Next.js 16** — https://nextjs.org/docs — async `cookies`/`headers`/`params`/`searchParams`, `"use cache"`, explicit `revalidate`.
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
- **getdesign.md** — https://getdesign.md — curated library of production-grade DESIGN.md analyses (Stripe, Figma, Tesla, Coinbase…): extracted color systems, type rules, and UI conventions in the same `design-system-master` shape this skill produces. A cross-brand reference layer, not a spec — verify any extracted value against the primary source before quoting.

---

*Reference version: global-design-skill v1.9.7 — `references/sources.md`*
*Related: every `rules/*.md` (claims) · `references/tech-standards.md` (stack snippets) · `tokens/design-tokens.json` (DTCG format) · `validators/` (CI recipes) · `rules/16-design-for-seo.md` (SEO) · `rules/19-contrast-standards.md` (WCAG/APCA) · `rules/04-color.md` (OKLCH)*
