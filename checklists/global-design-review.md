# Global Design Review Checklist

> Run this checklist on every design before handoff. A design that fails any CRITICAL item must be revised before development starts. IMPORTANT items should be fixed before handoff. NICE items are improvements for the next iteration.

**Legend:** ✅ Pass · ❌ Fail (blocks handoff) · ⚠️ Needs review · N/A Not applicable

---

## 1. Visual Hierarchy

| # | Check | Priority | Status |
|---|---|---|---|
| 1.1 | One clear primary focal point per screen section | CRITICAL | |
| 1.2 | Font size difference between adjacent hierarchy levels ≥ 1.25× | CRITICAL | |
| 1.3 | Only ONE primary CTA per section (max two CTAs total: primary + ghost) | CRITICAL | |
| 1.4 | The most important element is the most visually dominant | CRITICAL | |
| 1.5 | Elements with the same visual weight serve the same function | IMPORTANT | |
| 1.6 | Whitespace is used to group/separate — not filled with decoration | IMPORTANT | |
| 1.7 | Reading direction flows naturally (Z or F pattern for web) | IMPORTANT | |
| 1.8 | No more than 3 distinct font weights used in one section | NICE | |

---

## 2. Color & Contrast

| # | Check | Priority | Status |
|---|---|---|---|
| 2.1 | All colors use CSS custom properties — no raw hex values | CRITICAL | |
| 2.2 | All colors defined in OKLCH | CRITICAL | |
| 2.3 | Text contrast ≥ 4.5:1 for normal text (< 24px regular, < 18.7px bold) — WCAG AA | CRITICAL | |
| 2.4 | Text contrast ≥ 3:1 for large text (≥ 24px regular or ≥ 18.7px bold) | CRITICAL | |
| 2.5 | Color is not the only differentiator (add label/icon/pattern) | CRITICAL | |
| 2.6 | Contrast measured against the immediate block background, not page background | CRITICAL | |
| 2.7 | Placeholder text contrast ≥ 4.5:1 (not exempt like disabled states) | CRITICAL | |
| 2.8 | Focus ring contrast ≥ 3:1 against both the background and the focused element | CRITICAL | |
| 2.9 | Dark mode body text contrast ≤ 15:1 — no pure white text on dark surfaces | IMPORTANT | |
| 2.10 | Gradient backgrounds: contrast verified at the worst-contrast sampling point | IMPORTANT | |
| 2.11 | Adjacent sections: ΔL ≥ 4 OR a visible 1px border at 3:1 on both sides | IMPORTANT | |
| 2.12 | Card/block on page background: ≥ 1.5:1 contrast OR border defines the boundary | IMPORTANT | |
| 2.13 | Accent color occupies ≤ 15% of visible surface area | IMPORTANT | |
| 2.14 | All neutrals are tinted toward the accent hue — no pure gray | IMPORTANT | |
| 2.15 | Dark/light mode: all colors switch correctly via CSS variables | IMPORTANT | |
| 2.16 | Tested in grayscale — hierarchy still clear without color | NICE | |

> Full contrast standards and fix workflow: `rules/19-contrast-standards.md`

**BANNED colors (immediate fail):**
- [ ] No purple-to-indigo gradient on white background
- [ ] No neon outer glow shadows
- [ ] No pure `#000000` or `#ffffff` without hue tint
- [ ] No violet hero gradients
- [ ] No `rgba(purple, 0.2)` blobs as only decoration

---

## 3. Typography

| # | Check | Priority | Status |
|---|---|---|---|
| 3.1 | Display type uses `clamp()` fluid scale — no fixed px | CRITICAL | |
| 3.2 | Body text ≥ 16px (1rem) on all viewports | CRITICAL | |
| 3.3 | Line height ≥ 1.5 for body text | CRITICAL | |
| 3.4 | Paragraph width ≤ 75 characters (≤ 680px at 16px) | IMPORTANT | |
| 3.5 | No banned fonts: Inter as default, Roboto, Arial, Open Sans, Helvetica, Poppins | CRITICAL | |
| 3.6 | Hero H1 ≤ 3 lines on smallest target viewport | CRITICAL | |
| 3.7 | Every H1/H2 has an eyebrow tag | IMPORTANT | |
| 3.8 | Font pairing: expressive display + functional body | IMPORTANT | |
| 3.9 | No gradient text (`background-clip: text`) | CRITICAL | |
| 3.10 | Copy contains no banned words: Seamless, Elevate, Unleash, Next-Gen, Empower | IMPORTANT | |

---

## 4. Layout & Spacing

| # | Check | Priority | Status |
|---|---|---|---|
| 4.1 | All spacing uses 4px base grid tokens (--space-*) | CRITICAL | |
| 4.2 | No raw pixel values for spacing — all tokens | CRITICAL | |
| 4.3 | Section padding ≥ 6rem (96px) | CRITICAL | |
| 4.4 | At least one section breaks the grid (asymmetry) | IMPORTANT | |
| 4.5 | No nested cards | CRITICAL | |
| 4.6 | Container max-width defined (not full-bleed at all widths) | IMPORTANT | |
| 4.7 | No `100vh` — use `100dvh` | CRITICAL | |
| 4.8 | Images have explicit width + height (CLS prevention) | CRITICAL | |
| 4.9 | Content doesn't overflow at 320px viewport width | IMPORTANT | |
| 4.10 | Bento grid: column spans verified to sum correctly | IMPORTANT | |

---

## 5. Responsive Design

| # | Check | Priority | Status |
|---|---|---|---|
| 5.1 | Mobile-first CSS: `min-width` breakpoints only (no `max-width`) | CRITICAL | |
| 5.2 | All touch targets ≥ 44×44px on mobile | CRITICAL | |
| 5.3 | Tested at: 390px, 768px, 1280px, 1440px | CRITICAL | |
| 5.4 | No hover-only interactions on mobile (wrap in `@media (hover: hover)`) | CRITICAL | |
| 5.5 | iOS safe areas: `env(safe-area-inset-*)` applied where needed | IMPORTANT | |
| 5.6 | Bottom tab bar: `padding-bottom: env(safe-area-inset-bottom)` | IMPORTANT | |
| 5.7 | Horizontal scroll only in scroll-wrapper, not on page body | CRITICAL | |
| 5.8 | Text readable at 200% browser zoom (no overflow, no cut-off) | IMPORTANT | |

---

## 6. Components & States

| # | Check | Priority | Status |
|---|---|---|---|
| 6.1 | Every interactive component has all required states designed | CRITICAL | |
| 6.2 | Required states present: idle, hover, active, focus-visible, disabled | CRITICAL | |
| 6.3 | Loading state designed for all async operations | CRITICAL | |
| 6.4 | Empty state designed for all list/data views | CRITICAL | |
| 6.5 | Error state designed for all form submissions and data fetches | CRITICAL | |
| 6.6 | Success state designed for all user-completing actions | IMPORTANT | |
| 6.7 | Button hierarchy absolute: one primary, ghost/text for secondary | CRITICAL | |
| 6.8 | Form fields: label + input + helper + error anatomy complete | CRITICAL | |
| 6.9 | Modals use native `<dialog>` element | IMPORTANT | |
| 6.10 | No decorative side-stripe borders (`border-left` > 1px as accent) | CRITICAL | |

---

## 7. Accessibility

| # | Check | Priority | Status |
|---|---|---|---|
| 7.1 | Focus-visible ring on all interactive elements (2px solid, correct color) | CRITICAL | |
| 7.2 | Skip navigation link at page top | CRITICAL | |
| 7.3 | Every form input has a visible `<label>` or `aria-label` | CRITICAL | |
| 7.4 | Images have alt text (descriptive for content, `alt=""` for decorative) | CRITICAL | |
| 7.5 | Error messages have `aria-live` region | CRITICAL | |
| 7.6 | Modal/dialog: focus trap + `aria-modal` + focus returns on close | CRITICAL | |
| 7.7 | ARIA roles specified for custom interactive elements | IMPORTANT | |
| 7.8 | `aria-expanded`, `aria-controls` on all accordion/dropdown triggers | IMPORTANT | |
| 7.9 | Charts have accessible data table alternative | IMPORTANT | |
| 7.10 | Logical tab order matches visual reading order | CRITICAL | |

---

## 8. Animation

| # | Check | Priority | Status |
|---|---|---|---|
| 8.1 | `prefers-reduced-motion` respected: animation collapses to opacity-only or off | CRITICAL | |
| 8.2 | No `ease-in-out` — use specific `cubic-bezier()` values | IMPORTANT | |
| 8.3 | No `transition: all` | IMPORTANT | |
| 8.4 | Entry animations use `@starting-style` (not JS class toggle) | IMPORTANT | |
| 8.5 | No `window.addEventListener('scroll')` for animations (use IntersectionObserver) | CRITICAL | |
| 8.6 | Animation duration: micro < 150ms, standard 200-400ms, layout < 500ms | IMPORTANT | |
| 8.7 | `import from 'motion/react'` not `framer-motion` | CRITICAL | |
| 8.8 | No `animate-pulse` on multiple elements simultaneously | IMPORTANT | |

---

## 9. Performance

| # | Check | Priority | Status |
|---|---|---|---|
| 9.1 | LCP ≤ 2.5s (LCP element identified, `fetchpriority="high"` set) | CRITICAL | |
| 9.2 | CLS ≤ 0.1 (all images/embeds have explicit dimensions) | CRITICAL | |
| 9.3 | INP ≤ 200ms (interactions respond within Doherty Threshold) | CRITICAL | |
| 9.4 | Images use `loading="lazy"` except LCP and above-fold images | IMPORTANT | |
| 9.5 | Images in modern format: WebP or AVIF | IMPORTANT | |
| 9.6 | No unused Google Fonts (load only weights/styles in use) | IMPORTANT | |
| 9.7 | Third-party scripts load async/defer | IMPORTANT | |

---

## 10. Copy & Content

| # | Check | Priority | Status |
|---|---|---|---|
| 10.1 | No placeholder data: "John Doe", "Acme Corp", "99.9% uptime", ".99", "50%" | CRITICAL | |
| 10.2 | No generic CTAs: "Get Started", "Learn More" without specificity | CRITICAL | |
| 10.3 | No em dashes (— or --) — use commas, colons, or parentheses | IMPORTANT | |
| 10.4 | CTA labels follow formula: Verb + Object + Context | IMPORTANT | |
| 10.5 | Headline formula: [Outcome] for [Audience] without [Pain] | IMPORTANT | |
| 10.6 | No "SECTION 01", "ABOUT US" eyebrow labels (state what's there, not meta-labels) | IMPORTANT | |
| 10.7 | No "Scroll to explore" or bouncing chevrons | IMPORTANT | |
| 10.8 | Testimonials have: full name, title, company, photo, specific claim | IMPORTANT | |

---

## 11. Banned Patterns (immediate failure)

Check these explicitly — any `✓` is an automatic fail:

- [ ] Centered hero: H1 + subtext + 2 equal buttons (the default layout)
- [ ] 3-equal-column icon feature grid
- [ ] Full-width sticky nav touching top edge (needs top margin/padding)
- [ ] Hero metric template: big number + small label + gradient accent (SaaS cliché)
- [ ] Identical card grid: same-sized cards with icon + heading + text, repeated 3–6×
- [ ] Glassmorphism as default polish (only if it carries spatial meaning)
- [ ] Modal as first design thought (exhaust inline/progressive alternatives first)
- [ ] Gradient text (`background-clip: text`)
- [ ] Side-stripe accent borders (border-left/right > 1px colored)
- [ ] SVG-drawn faces, people, or objects (always looks wrong)
- [ ] Data slop: meaningless fake statistics ("50% faster", "99.9% uptime")
- [ ] Icon on every heading, bullet, and card label
- [ ] Gradient backgrounds on every section

---

## Review Summary

**Date:** [YYYY-MM-DD]

**Reviewer:** [Name]

**Project:** [Name]

**Total checks:** [N]

**Critical fails:** [N] — *must be 0 before handoff*

**Important fails:** [N] — *should be 0 before handoff*

**Verdict:**

```
[ ] APPROVED — all critical pass, important issues logged
[ ] CONDITIONAL — specific items to fix before handoff: [list]
[ ] REJECTED — critical failures: [list failures]
```

**Notes:**
[Anything else the designer should address]

---

---

## Pre-Delivery Sanity Tests

Run these three tests after completing any design work. They catch problems that checklists miss.

### Squint Test
Squint your eyes until the page is blurry. Can you still identify:
- The primary headline?
- The main CTA?
- The section boundaries?

If not — the visual hierarchy is broken. Something has equal weight that shouldn't.

### Remove-One-Element Test
For every section, mentally remove one element. Does the section still work?
- If yes → that element was probably unnecessary. Remove it.
- If no → the element is load-bearing. Keep it.

Apply this to: decorative icons, subheadings, background textures, secondary CTAs, badge labels, illustration details.

### 3-Second Mobile Test
Load the page on a 390px viewport. In 3 seconds, can a visitor answer:
- What is this?
- What am I supposed to do?
- Do I trust this?

If any answer is unclear in 3 seconds — the above-the-fold is not doing its job.

### AI Slop Test

Run before declaring any design done. Three altitudes — each catches what the previous misses.

**First-order reflex — category → look.** Could someone guess the theme + palette from the category alone? "Observability → dark blue", "healthcare → white + teal", "finance → navy + gold", "crypto → neon on black". If yes, rework the scene sentence and color strategy until the answer is *not* obvious from the domain.

**Second-order reflex — category + avoided-cliché → look.** Could someone guess the aesthetic family once the obvious cliché is avoided? "AI tool that's not SaaS-cream → editorial-typographic", "fintech that's not navy-and-gold → terminal-native dark". This is the trap one tier deeper: the first reflex was dodged, the second wasn't. Rework until *both* altitude checks fail to predict the result.

**Third-order — composition audit (independent of aesthetic).** Does the layout hold up spatially regardless of style?
- **Balance:** clear visual centre of gravity? Heavy elements offset by lighter ones across the axis?
- **Whitespace:** does negative space guide the eye, or fragment the layout into disconnected islands?
- **Rhythm:** are spacing intervals derived from a scale, creating legible cadence — not arbitrary padding?
- **Gestalt:** proximity (related close, unrelated separated), similarity (same function = same treatment), figure/ground (content unmistakably distinct from background)?

If any composition dimension fails, the design has a structural problem that style cannot fix. **If someone could look at the interface and say "AI made that" without doubt, it has failed.**

### Standards Floor

Anti-slop has a technical floor beneath the visual ceiling. A nice-looking page still fails if the foundation is slop. Verify:

- [ ] **Semantic HTML** — `header`/`main`/`nav`/`section`/`article`/`button`/`form`/`label` used for meaning, not `<div>` soup (WHATWG HTML — `references/sources.md`)
- [ ] **Systematic CSS** — cascade layers + tokens + scales; no random magic numbers (`margin: 37px`), no specificity wars
- [ ] **Accessible interactivity** — every interactive block is keyboard-operable with visible focus and idle/disabled/loading/error/success states (WCAG, ARIA APG)
- [ ] **Verified features** — any modern CSS/JS feature checked on Baseline / Can I use before use; non-Baseline behind `@supports` or with a fallback
- [ ] **Clean validation** — markup passes Nu HTML Checker; CSS/JS pass Stylelint/ESLint/Prettier; Lighthouse a11y ≥ 95, performance ≥ 88

Full source list and tools: `references/sources.md`.

### Ship-Readiness Product Gates

A site is a product in a real network, not just a visual. Before shipping a real page (not a mockup), clear the product gates that apply. Standards for each live in `references/sources.md`.

**Security** (apply to every shipped template)
- [ ] HTTPS + HSTS; a Content-Security-Policy is set (no unrestricted inline scripts)
- [ ] `Referrer-Policy` + `Permissions-Policy` set; cross-origin (CORS/COOP/CORP) deliberate
- [ ] External scripts are trusted + minimal; forms protected against XSS/CSRF (OWASP)

**SEO & machine-readability** (`rules/16-design-for-seo.md`)
- [ ] Unique `title` + meta description; one `<h1>`; `canonical` set; `hreflang` if multilingual
- [ ] `robots.txt` + XML sitemap valid; `noindex` only where intended
- [ ] Schema.org JSON-LD for the page type (Article / Product / Organization / FAQ / Breadcrumb)
- [ ] HTTP status hygiene: 200 for live pages, 301 for moves, 404/410 for gone (RFC 9110)

**Social preview**
- [ ] Open Graph set: `og:title`, `og:description`, `og:image` (1200×630), `og:url`, `og:type`
- [ ] Card previews correctly in a messenger/X/LinkedIn before launch

**PWA / app** (only if SaaS / dashboard / tool / installable)
- [ ] Web App Manifest + icons; offline fallback; sensible update behavior

**Privacy & consent** (commercial / EU / regulated)
- [ ] Cookie/consent banner is honest — not a dark pattern; privacy policy linked in footer
- [ ] Analytics/pixels disclosed; third-party scripts minimized; forms collect only needed data

**QA matrix** (design is not done until edge states are checked)
- [ ] Chrome / Safari / Firefox / Edge · desktop / tablet / mobile · light / dark
- [ ] Long strings + RU/EN · empty state · data-heavy state · load-error · slow network
- [ ] Keyboard-only pass · hoverless (touch) devices · visual-regression check before release

### Live Redesign Verification (exercise the UI — don't trust the default screenshot)

A redesign is **not** verified by a screenshot of the homepage hero. Bugs hide in states and modes that the default view never shows. Run `references/live-audit-snippets.md` against the rendered DOM, then exercise the full matrix.

- [ ] **Both themes audited** — run the contrast + invisible-text scans in light AND dark (a heading can be visible in light, invisible in dark — `-webkit-text-fill-color`, see `rules/19` R14)
- [ ] **Every view mode toggled** — grid ↔ list (and any other layout switch); confirm the grid actually reflows, cards don't cram, badges don't stretch
- [ ] **Empty / no-results state** — type a query that matches nothing; confirm the empty state shows (reason + recovery)
- [ ] **Every filter exercised** — each quick-filter/category; counts update; combined filters don't break layout
- [ ] **Keyboard pass** — Tab through; every interactive element shows a visible focus ring
- [ ] **Combinatorial edge matrix** — the bug is at the intersection, not the homepage:

```
themes × view-modes × states × card-tiers × viewports
  light/dark  ·  grid/list  ·  default/filtered/empty/error
  ·  normal/featured/paid/FEATURED+PAID  ·  390/768/1280
```

- [ ] **Fix at the system level** — if a defect appears on one instance of a repeated component (one card, one badge), it is in the shared definition → fix the rule, not the instance. "If it's a bug, it's everywhere." Re-scan to confirm the fix is global.

> Lesson encoded here: every item above maps to a real miss — invisible dark headings, a broken list view, a hidden paid badge, a per-instance patch that left the bug elsewhere. Verify the rendered result, in every mode.

---

*Checklist version: global-design-skill v1.9.8 — `checklists/global-design-review.md`*
*Related: `agents/design-critic.md`, `agents/frontend-handoff-reviewer.md`, `rules/00-escalation-protocol.md`*
