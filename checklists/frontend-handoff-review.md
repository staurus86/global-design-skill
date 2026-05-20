# Checklist — Frontend Handoff Review

> The extended handoff checklist. A design passes handoff only when a developer can implement it without asking a single question. This is the operational expansion of Gate 8. Run it before any spec leaves the design phase.

---

## How to Use

Run every item against the spec or design file. Mark **[P]** Pass, **[F]** Fail, **[N/A]** Not applicable.

- **Any [F] in section 1–6** → handoff is blocked. Fix before sending to developers.
- **[F] only in section 7** → conditional pass, note the gap explicitly in the spec.

The test for every item: *would a developer have to guess, assume, or ask?* If yes, it fails.

---

## 1. Problem & Intent

- [ ] The spec states what problem this UI solves (not just what it looks like)
- [ ] The target user and their context are named (role, device, ambient conditions)
- [ ] The primary success metric is stated with a target number
- [ ] The scope boundary is explicit — what is and is not part of this handoff

---

## 2. Visual Specification

- [ ] Every color is a token reference (`var(--color-*)`) — no raw hex, no raw `oklch()` in the spec
- [ ] Every spacing value is a token (`var(--space-*)`) — no raw px
- [ ] Every radius, shadow, and duration is a token
- [ ] Typography per element: font family, size token, weight, line-height, letter-spacing
- [ ] Exact dimensions or constraints given for every container (max-width, min-height, aspect-ratio)
- [ ] Z-index values come from the documented z-index scale — no arbitrary numbers

---

## 3. All States Designed

For every interactive element, the spec shows or describes:

- [ ] Idle / default
- [ ] Hover (and a note that hover is gated behind `@media (hover: hover)`)
- [ ] Focus-visible (ring style specified)
- [ ] Active / pressed
- [ ] Disabled (including why it would be disabled)
- [ ] Loading (skeleton or spinner, with exact placement)
- [ ] Empty (for any container that can have zero items)
- [ ] Error (with the error message copy or copy formula)
- [ ] Success (if the action has a completion state)

---

## 4. Responsive Behavior

- [ ] Behavior specified at 390px (mobile), 768px (tablet), 1280px (desktop)
- [ ] What reflows, stacks, hides, or collapses at each breakpoint is explicit
- [ ] Touch targets are ≥ 44×44px on mobile
- [ ] No fixed heights that break with longer content or larger text
- [ ] `100dvh` used for full-height sections, not `100vh`
- [ ] Container queries vs. media queries decision is stated where it matters

---

## 5. Accessibility Specification

- [ ] Semantic HTML element named for every region (`<nav>`, `<main>`, `<button>`, etc.)
- [ ] Every interactive element has its ARIA role and state attributes listed
- [ ] Every form input has an associated `<label>` with `for`/`id` wiring
- [ ] Focus order is specified and matches visual reading order
- [ ] `aria-live` regions identified for dynamic content (errors, toasts, counts)
- [ ] Modals/dialogs: focus trap, Escape behavior, focus-return target all specified
- [ ] Color contrast verified: ≥ 4.5:1 body text, ≥ 3:1 large text and UI components
- [ ] `prefers-reduced-motion` fallback specified for every animation

---

## 6. Assets & Content

- [ ] All images provided at correct resolution, with format (WebP/AVIF) specified
- [ ] Every image has `width` + `height` and a loading strategy (`eager`/`lazy`)
- [ ] The LCP element is identified and marked `fetchpriority="high"`
- [ ] Icons: source set named (single set), stroke width and sizing specified
- [ ] Real copy provided — no "Lorem ipsum", no "John Doe", no placeholder numbers
- [ ] Fonts: files or source named, `font-display` strategy specified
- [ ] Empty/error/loading copy provided (not left to the developer to invent)

---

## 7. Implementation Notes

- [ ] Framework-specific notes given (React 19 / Next.js 15 / Tailwind v4 conventions)
- [ ] Animation library decision stated (`motion/react`, GSAP, or CSS-only) with budget
- [ ] Third-party dependencies named and justified
- [ ] Edge cases noted: long text, zero data, max data, slow network, offline
- [ ] Prohibited approaches listed (banned patterns relevant to this component)
- [ ] Acceptance criteria written as a verifiable checklist

---

## Final Gate

Answer all four. Any "no" blocks handoff.

| Question | Answer |
|---|---|
| Could a developer build this without opening a chat to ask a question? | Yes / No |
| Is every state, token, and ARIA attribute on the page specified? | Yes / No |
| Is the responsive behavior unambiguous at all three breakpoints? | Yes / No |
| Is the copy final and real, not placeholder? | Yes / No |

---

*Checklist version: global-design-skill v1.0 — `checklists/frontend-handoff-review.md`*  
*Updated: 2026-05-20*  
*Related: `templates/specs/frontend-tz.md`, `skills/global-design/quality-gates.md` (Gate 8), `agents/frontend-handoff-reviewer.md`*
