# Frontend ТЗ — Template

> The canonical spec template for developer handoff. A spec passes Gate 8 when a developer can implement it without asking a single question. Fill every section. Leave nothing as "TBD".

**Usage:** Copy this template, fill all sections, delete any sections marked "(if applicable)" that don't apply to this component/feature.

---

## Task: [Component or page name]

**Type:** `[ ] New component` `[ ] New page` `[ ] Modification` `[ ] Redesign`

**Ticket / link:** [Linear / Jira / GitHub issue URL]

**Design source:** [Figma frame URL or screenshot path]

**Target branch:** [branch name]

---

## Problem

[What exists now and why it's wrong. Be specific — not "the current design is outdated" but "the button label 'Submit' gives the user no information about what will happen. After clicking, 32% of users immediately click Back (source: Hotjar)."]

---

## What to implement

[Exact description of the desired end state. A developer reading this should be able to close the design file and build from this description alone.]

---

## Scope

**In scope:**
- [Explicit list of what must be built]

**Out of scope:**
- [Explicit list of what is NOT included in this task — prevents scope creep]

---

## Desktop behavior (≥ 1280px)

[Exact layout, dimensions, alignment, content. No vague language.]

**Layout:**
- [Describe the grid / flexbox structure]
- Container: [max-width value]px, centered / full-width
- Padding: [exact token value]

**Content:**
- [Every text string — exact copy, not "add a title here"]
- [Every image — dimensions, alt text]

**Interactions:**
- [What happens on hover, click, drag]
- [Transition: duration, easing, property]

---

## Tablet behavior (768px – 1279px)

[How it changes from desktop. Not "make it responsive" — exact behavior.]

[If no changes: "Identical to desktop, no layout changes required at this breakpoint."]

---

## Mobile behavior (≤ 767px)

[How it changes from desktop. Every change is explicit.]

**Layout changes:**
- [Column → stack / sidebar → drawer / grid → carousel]

**Touch targets:**
- All interactive elements: minimum 44×44px

**Specific changes:**
- [List every visual or behavioral change]

---

## States

### Idle
[Exact visual description. Default appearance with no interaction.]

```
Background:   [token name — e.g., var(--color-surface)]
Border:       [token name or "none"]
Text color:   [token name]
Border radius: [token name or exact value]
Shadow:       [token name or "none"]
```

### Hover (desktop only — wrap in `@media (hover: hover)`)
[Exact change from idle. What changes, what stays the same.]

```
Transition: [property] [duration]ms [easing cubic-bezier or named]
Change:     [background / border / shadow / transform / color]
```

### Active / pressed
```
Transform:   scale([value]) — e.g., scale(0.97)
Duration:    [ms]
```

### Focus-visible (keyboard navigation)
```
Outline:        2px solid var(--color-accent)
Outline-offset: [px]
Border-radius:  [same as element or explicitly override]
```

### Disabled (if applicable)
```
Opacity:         0.4
Cursor:          not-allowed
Pointer-events:  none
aria-disabled:   "true"
```

### Loading (if applicable)
```
Trigger:    [what action triggers loading state]
Indicator:  [spinner / skeleton / progress bar]
Duration:   [< 100ms: no indicator | 100ms-1s: skeleton | 1-10s: progress]
Button:     disabled during loading, label changes to "[Verb]ing…"
```

### Empty (if applicable)
```
Visual:  [specific illustration or icon — not "empty state icon"]
Title:   "[Exact copy]"
Body:    "[Exact copy]"
CTA:     "[Exact label]" → [exact destination]
```

### Error (if applicable)
```
Trigger:    [what causes the error state]
Display:    [toast / inline / banner / full-page]
Copy:       "[What failed] — [Why] — [How to fix]"
aria-live:  "polite" (non-blocking) or "assertive" (blocking)
Recovery:   [exact action label and behavior]
```

### Success (if applicable)
```
Display:    [toast / inline badge / redirect]
Copy:       "[Exact success message]"
Duration:   [auto-dismiss: Ns | persist until dismissed]
```

---

## Tokens

[Every design value expressed as a CSS custom property. Never raw hex or pixel values.]

```css
/* Background */
background: var(--color-surface);

/* Text */
color: var(--color-text-primary);

/* Border */
border: 1px solid var(--color-border);

/* Spacing */
padding: var(--space-4) var(--space-6);
gap: var(--space-3);

/* Border radius */
border-radius: var(--radius-lg);

/* Shadow */
box-shadow: [exact value or "none"];
```

---

## Typography

```css
/* Heading (if any) */
font-size:   var(--text-h3);        /* clamp(1.25rem, 2vw + 0.25rem, 2rem) */
font-weight: [600 / 700];
line-height: [1.2 / 1.4];

/* Body text */
font-size:   var(--text-body);      /* clamp(1rem, 1.2vw + 0.4rem, 1.2rem) */
font-weight: 400;
line-height: 1.65;

/* Label / caption */
font-size:   0.875rem;
font-weight: 500;
color:       var(--color-text-muted);
```

---

## Animation

[Every animated property. No "smooth transition" — give exact values.]

```css
/* Entry animation (if applicable) */
@starting-style {
  opacity: 0;
  transform: translateY([px]);
}

transition:
  opacity [duration]ms [cubic-bezier(...)],
  transform [duration]ms [cubic-bezier(...)];

/* Or GSAP / Motion */
animate(element, {
  opacity: [0, 1],
  y: [24, 0]
}, {
  duration: [s],
  easing: [easing string]
})
```

**Trigger:** `[on mount / on hover / on scroll entry / on user action]`

**prefers-reduced-motion:** `[animation collapses to opacity-only / no animation]`

---

## ARIA

[Every ARIA attribute for every interactive element. No "add appropriate ARIA".]

```html
<!-- Primary interactive element -->
<[element]
  role="[role — e.g., button / dialog / listbox / combobox]"
  aria-label="[exact string — not 'descriptive label']"
  aria-expanded="[true | false — if applicable]"
  aria-controls="[id of controlled element — if applicable]"
  aria-describedby="[id of description element — if applicable]"
  aria-disabled="[true | false — if applicable]"
  aria-live="[polite | assertive — if applicable]"
>
```

**Keyboard behavior:**
- `Tab`: [what gets focused next]
- `Enter` / `Space`: [what happens]
- `Escape`: [what happens — e.g., closes modal, clears selection]
- `Arrow keys`: [if applicable — navigation within component]

**Focus management:**
- On open (dialog/drawer): focus moves to [first focusable element / heading / close button]
- On close: focus returns to [the trigger element]
- Focus trap: [yes — inside modal/dialog | no]

---

## Responsive images (if applicable)

```html
<img
  src="[path]"
  alt="[exact alt text — describes content, not decorative]"
  width="[exact px]"
  height="[exact px]"
  loading="[lazy | eager]"
  fetchpriority="[high — if LCP element | auto]"
/>
```

---

## Data / API (if applicable)

**Endpoint:** `[METHOD /api/path]`

**Request shape:**
```json
{
  "field": "type and description"
}
```

**Success response:**
```json
{
  "field": "type and description"
}
```

**Error codes and handling:**
```
400: [what to show the user]
401: [redirect to login]
404: [show not-found state]
500: [show server error state with retry]
```

**Loading threshold:** [< 100ms: no indicator | 100ms–1s: skeleton | 1–10s: progress]

---

## Do not

[Explicit list of prohibited approaches. Every "do not" prevents a specific misinterpretation.]

- Do not use `framer-motion` — use `motion/react`
- Do not use `100vh` — use `100dvh`
- Do not use raw hex values — use CSS custom properties
- Do not use `ease-in-out` — use the specified `cubic-bezier()`
- Do not add features not listed in scope
- Do not show hover states on touch devices — wrap in `@media (hover: hover)`
- [Add component-specific prohibitions]

---

## Acceptance criteria

[Every criterion is pass/fail. No subjective criteria. A QA engineer can verify each one without seeing the design.]

```
[ ] Component renders correctly at 390px, 768px, 1280px viewports
[ ] All states present: idle, hover, active, focus-visible, [+ applicable states]
[ ] Keyboard navigable: Tab reaches the element, Enter/Space activates it
[ ] Focus-visible ring visible on keyboard navigation (2px solid, correct color)
[ ] Touch target ≥ 44×44px on mobile
[ ] Reads correctly at 200% browser zoom (no overflow, no cut-off text)
[ ] Screen reader announces element correctly (role + label + state)
[ ] Animation respects prefers-reduced-motion (collapses or removes)
[ ] No raw color values or pixel values — all tokens used
[ ] Error state shows message in format: [What failed] — [How to fix]
[ ] Loading state disables the trigger button during operation
[ ] [Add component-specific criteria]
```

---

## Notes

[Anything that doesn't fit above — edge cases, browser quirks, dependencies, known issues.]

---

*Template version: global-design-skill v1.0 — `templates/specs/frontend-tz.md`*
*Gate 8 checklist: `skills/global-design/quality-gates.md`*
