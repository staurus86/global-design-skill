# Operating Principles

> How to think about design decisions. Not rules about what things should look like — rules about how to reach correct decisions.

---

## 1. Resolve ambiguity first

Design is mostly a question-answering activity. The first job is to surface and resolve unknowns, not to produce visuals.

Before producing anything: what type of interface, who uses it, what business goal it serves, what "done" looks like. One wrong assumption at the start costs hours at the end.

**Apply when:** any new task begins. Ask the minimum necessary questions — one targeted question beats guessing.

---

## 2. One focus per viewport

Every screen section has one primary job. One headline. One primary action. One data point that matters most.

Multiple competing focal points = no focal point. If two elements are equally prominent, neither is the focal point and the user has no direction.

**Apply when:** designing any screen or section. Ask: what is the one thing this section must communicate?

---

## 3. Mobile-first, not mobile-as-afterthought

Base styles for 390px viewport. Expand with `min-width` queries. Test at 390px → 768px → 1280px.

`min-height: 100dvh` everywhere. Never `100vh` (iOS Safari bug). `env(safe-area-inset-*)` for fixed elements.

**Apply when:** every layout and component, from the first line of CSS.

---

## 4. All states are required

Loading, empty, and error are not edge cases — they are the default states for first-time users and network failures.

A design with only the "happy path" is an incomplete design. Never ship a component that hasn't had its loading, empty, and error states designed.

**Decision matrix:**
- Under 100ms: no loading indicator
- 100ms–1s: skeleton or subtle opacity shift
- 1–10s: explicit progress
- Over 10s: progress + "continue in background"

**Apply when:** every interactive component, form, data-fetching screen.

---

## 5. Tokens, not values

Never use raw color values or spacing values in components. Always use CSS custom properties.

```css
/* Never */
.card { background: oklch(14% 0.010 258); padding: 1.5rem; }

/* Always */
.card { background: var(--color-surface); padding: var(--space-6); }
```

Tokens make theming, dark mode, and design system changes possible without touching components.

**Apply when:** writing any CSS or Tailwind classes that reference design decisions.

---

## 6. Hierarchy through space, not decoration

Visual hierarchy is created by: size difference, weight difference, spatial separation, contrast, and position. Not by borders, shadows, background colors, or icons on every heading.

Decoration added to compensate for weak hierarchy is noise. Fix the hierarchy instead.

**Test:** cover the decorative elements. Does the hierarchy still read? If not, fix it at the structural level.

**Apply when:** any layout that feels flat, cluttered, or visually undifferentiated.

---

## 7. Accessibility is structural

WCAG 2.2 AA is a floor, not a ceiling. Accessibility decisions are architectural — they cannot be added as a layer after design is complete.

Minimum requirements built in from the start:
- 4.5:1 contrast for normal text, 3:1 for large text and UI components
- 44×44px touch targets (visual can be smaller, padding extends the target)
- Focus-visible styles that match the visual design
- ARIA roles and labels on all interactive components
- All animations respect `prefers-reduced-motion`

**Apply when:** every component, from the first instance.

---

## 8. Measure twice, cut once

One clarifying question before starting beats rebuilding after. If something is ambiguous, ask. If the answer reveals the task was different than assumed, the question paid for itself many times over.

Do not guess at: brand preferences, primary user persona, primary device, business goal, or success metrics.

**Apply when:** whenever an assumption would significantly affect the design direction.

---

## 9. Handoff-ready means unambiguous

A frontend spec passes when a developer can implement it without a single question. Ambiguity in specs becomes bugs in production.

A spec is unambiguous when it includes: exact states, exact token names, exact breakpoints, exact animation easing and duration, exact ARIA attributes, and explicit "do not do" list.

**Apply when:** preparing any `templates/specs/frontend-tz.md` output.

---

## 10. Verify against the goal

The final check is not "does it look good?" but "does this accomplish the stated business goal?"

A beautiful landing page that doesn't explain what the product is has failed. An elegant dashboard that buries the critical metric has failed.

Verify against the acceptance criteria from `quality-gates.md`, not against aesthetic preference.

**Apply when:** before declaring any design complete.

---

## Cognitive laws (always active)

These are not rules to check — they are forces that operate whether you account for them or not.

| Law | Effect | Design implication |
|---|---|---|
| **Hick's Law** | Decision time scales with number of choices | Nav ≤ 7 items; pricing ≤ 3 tiers; one primary CTA per section |
| **Fitts' Law** | Acquisition time scales with distance and inverse of size | Primary actions are large and central; destructive actions are spatially separated |
| **Miller's Law** | Working memory holds 7±2 items | Group beyond 7 rather than cutting; categorize before listing |
| **Doherty Threshold** | Control perception breaks after 400ms silence | Every action gets visual feedback within 400ms |
| **Jakob's Law** | Users spend most time on other sites | Follow established conventions for navigation, forms, and controls |
| **Law of Proximity** | Elements close together are perceived as related | Related items cluster; unrelated items separate |
| **Law of Similarity** | Same visual treatment = same function | Consistent component variants; no visual noise from decorative variation |
