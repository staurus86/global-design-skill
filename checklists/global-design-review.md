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

---

*Checklist version: global-design-skill v1.6 — `checklists/global-design-review.md`*
*Related: `agents/design-critic.md`, `agents/frontend-handoff-reviewer.md`, `rules/00-escalation-protocol.md`*
