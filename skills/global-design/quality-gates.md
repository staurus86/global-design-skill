# Quality Gates

> Formal acceptance criteria. A design is "done" only when it passes all gates relevant to its type.

---

## Gate 1: Problem Definition

- [ ] User is defined: role, context, device, ambient conditions
- [ ] Business goal is stated (not "look nice" — a measurable outcome)
- [ ] Success metric exists (conversion rate, task completion time, error rate, etc.)
- [ ] Scope is clear: what is and is not included

**Blocked by:** Gate 1 failure means no design work proceeds.

---

## Gate 2: Information Architecture

- [ ] All required pages/screens are listed
- [ ] Navigation structure is defined and within Hick's Law limits (≤ 7 top-level)
- [ ] User flow is mapped: entry → task → outcome
- [ ] Edge cases are covered: first-time user, empty state, error state

---

## Gate 3: Design System

- [ ] Color tokens defined in OKLCH
- [ ] Type scale defined with `clamp()` for all display sizes
- [ ] Spacing on 4px grid (`--space-1` through `--space-64`)
- [ ] Border radius scale defined
- [ ] Shadow scale defined
- [ ] Z-index named layers defined (no arbitrary values)
- [ ] All values as CSS custom properties — no raw values in components

---

## Gate 4: States

Every interactive component must have:
- [ ] **Idle** state (default appearance)
- [ ] **Hover** state (desktop only, inside `@media (hover: hover)`)
- [ ] **Active/pressed** state
- [ ] **Focus-visible** state (visible ring, not `outline: none`)
- [ ] **Disabled** state (if applicable)
- [ ] **Loading** state: skeleton for 100ms–1s, progress for 1–10s
- [ ] **Empty** state: reason + action to fill
- [ ] **Error** state: neutral tone + specific description + one recovery action
- [ ] **Success** state (if applicable)

---

## Gate 5: Responsive

- [ ] Base styles at 390px (mobile-first)
- [ ] No horizontal scroll at any viewport
- [ ] Touch targets ≥ 44×44px on mobile
- [ ] `min-height: 100dvh` — never `100vh`
- [ ] Safe area insets on fixed/sticky elements
- [ ] Navigation collapses gracefully at ≤ 768px
- [ ] Images have `width` + `height` attributes set (prevents CLS)
- [ ] Text remains readable at 200% zoom

---

## Gate 6: Accessibility

- [ ] Color contrast: 4.5:1 for normal text, 3:1 for large text and UI components
- [ ] All interactive elements keyboard-navigable (Tab, Enter, Escape, Arrow keys)
- [ ] Focus-visible on all interactive elements (custom ring matching visual design)
- [ ] Skip navigation link present on pages with navigation
- [ ] All images have meaningful `alt` text (decorative = `alt=""`)
- [ ] All form inputs have visible labels linked with `for`/`id`
- [ ] All ARIA roles, states, and properties are correct
- [ ] `aria-live` regions for dynamic content (toasts, errors, counters)
- [ ] Modal focus is trapped while open; focus returns on close
- [ ] Color is not the sole differentiator (always add text/shape/pattern)
- [ ] `prefers-reduced-motion` supported — all animations conditional

---

## Gate 7: Performance

- [ ] LCP element identified, `fetchpriority="high"`, not lazy-loaded
- [ ] All images have explicit `width`/`height` (CLS = 0)
- [ ] `aspect-ratio` on media containers
- [ ] Heavy components use `dynamic(() => import(...), { ssr: false })`
- [ ] No `window.addEventListener('scroll')` for animations
- [ ] Tailwind: no accidental full-library imports
- [ ] Font: `font-display: optional` or `swap` (no invisible text)
- [ ] Lighthouse Performance ≥ 88 on mobile throttled

---

## Gate 8: Frontend Readiness

The spec passes when a developer can implement without asking a single question:

- [ ] Every state is described with exact visual behavior
- [ ] Token names are specified (not hex values or descriptive colors)
- [ ] Breakpoints are listed with exact `px` values
- [ ] Animation easing and duration specified per component
- [ ] ARIA attributes listed for all interactive components
- [ ] Prohibited approaches are explicit (what NOT to do)
- [ ] Acceptance criteria are testable (pass/fail, not subjective)

---

## Gate Summary by Project Type

| Gate | Landing | SaaS App | Admin | Component |
|---|---|---|---|---|
| 1 Problem Definition | Required | Required | Required | Required |
| 2 Information Architecture | Required | Required | Required | — |
| 3 Design System | Required | Required | Required | Required |
| 4 States | Required | Required | Required | Required |
| 5 Responsive | Required | Required | Required | Required |
| 6 Accessibility | Required | Required | Required | Required |
| 7 Performance | Required | Recommended | Recommended | — |
| 8 Frontend Readiness | Required | Required | Required | Required |

---

## Failure modes

**Gate 1 failure:** No design work. Resolve problem definition first.

**Gate 3 failure:** Inconsistency will compound. Fix token system before adding components.

**Gate 4 failure:** Ship with explicit "states TBD" — never pretend happy path is complete.

**Gate 6 failure:** This is a legal requirement in many jurisdictions. Do not ship inaccessible interfaces.

**Gate 8 failure:** Return to design. A spec that requires interpretation is not a spec.
