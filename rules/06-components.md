# Rule 06 — Components

> Components are units of behavior, not units of style. Every component has a contract: inputs, states, outputs. Style follows contract.

---

## The Component Contract

Before building any component, define:

```
Name:       [exact component name]
Purpose:    [one sentence — what user problem it solves]
Props:      [inputs: variant, size, disabled, loading, etc.]
States:     [idle | hover | active | focus | disabled | loading | error | success]
Outputs:    [events: onClick, onChange, onSubmit, etc.]
Do not:     [explicit prohibitions]
```

A component without a defined contract becomes a style decision. Style decisions drift. Contracts don't.

---

## Rules

### R1 — Components communicate function through shape, not decoration

Shape is function:
- Button: pill or rectangle → clickable
- Input: rectangular with border → editable
- Badge: small pill → informational label
- Tag: small, closeable pill → selectable / removable
- Card: contained rectangle with elevation → clickable container or grouping

**Banned:** Giving a `<div>` button-like styling without making it a `<button>`. Giving a non-interactive element the visual appearance of an interactive element.

---

### R2 — All states are required before implementation

A component is not complete until all its states are designed. No state is optional.

**Universal states (every interactive component):**

| State | Trigger | Visual change |
|---|---|---|
| **Idle** | Default | Base appearance |
| **Hover** | `@media (hover: hover)` + cursor enters | Subtle bg shift, cursor: pointer |
| **Active** | Mouse/touch down | Scale 0.98 or tint shift |
| **Focus-visible** | Keyboard focus | Visible ring — not `outline: none` |
| **Disabled** | `disabled` attr or `aria-disabled` | 40% opacity, cursor: not-allowed |
| **Loading** | Async operation pending | Spinner or skeleton + disabled |
| **Error** | Failed operation | Error color, error message |
| **Success** | Completed operation | Success color or checkmark |

---

### R3 — Button hierarchy is absolute

One visual system per page. No exceptions.

```
Primary:      Filled, highest contrast background, strongest color
Secondary:    Ghost (border-only) or outline, same height as primary
Tertiary:     Text-only, no border, no background
Destructive:  Same visual weight as Secondary — never Primary
              Exception: confirmation modal "Delete" button can be Destructive Primary
              but only inside the confirmation context
```

**Sizes:**
```css
.btn-sm { height: 32px; padding-inline: var(--space-3); font-size: 0.875rem; }
.btn-md { height: 40px; padding-inline: var(--space-4); font-size: 1rem; }
.btn-lg { height: 48px; padding-inline: var(--space-6); font-size: 1rem; }
```

**Touch target:** visual size can be smaller than 44px; padding extends the hit area.
```css
.btn-sm { min-height: 32px; position: relative; }
.btn-sm::after {
  content: '';
  position: absolute;
  inset: -6px; /* extends touch target to 44px */
}
```

---

### R4 — Form input anatomy

Every input follows the same structure. Consistency is correctness.

```html
<div class="field">
  <label for="email" class="label">
    Email <span aria-hidden="true">*</span>
  </label>
  <input
    id="email"
    type="email"
    name="email"
    placeholder="name@company.com"
    aria-describedby="email-hint email-error"
    aria-required="true"
    aria-invalid="false"
  />
  <span id="email-hint" class="field-hint">We'll send a confirmation link.</span>
  <span id="email-error" class="field-error" role="alert" aria-live="polite"></span>
</div>
```

**Rules:**
- Label always visible above the field — never placeholder-only
- `for` attribute on label, `id` on input — always linked
- Error message appears below the field, not above
- Hint text appears below the label or below the field (pick one, stay consistent)
- Required: mark in label with `*` + footnote `* Required fields`
- Validation: on blur (not on every keystroke, not only on submit)

---

### R5 — Card rules

Cards are used when items are:
- Individually clickable/selectable
- Have their own independent context
- Need visual separation from adjacent items

**Banned uses:**
- Wrapping every section in a card because it "looks cleaner"
- Nesting cards inside cards
- Using cards as a grid filler for content that has no interactive or grouping purpose

**Card anatomy:**
```css
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  /* Optional: subtle shadow for elevated cards */
  box-shadow: 0 1px 3px oklch(0% 0 0 / 0.08);
}

.card[role="button"],
a.card {
  cursor: pointer;
  transition: background 120ms, box-shadow 120ms;
}

.card[role="button"]:hover,
a.card:hover {
  background: var(--color-surface-2);
  box-shadow: 0 4px 16px oklch(0% 0 0 / 0.12);
}
```

---

### R6 — Modal rules

Modals are for: confirmations, forms that need full focus, complex selections.

Modals are not for: first-time experiences, walkthroughs, expanding card content (use a detail panel instead).

**Before using a modal, exhaust alternatives:**
1. Inline expand (accordion, collapsible)
2. Detail panel (slides in from right, content stays in context)
3. New page / route (for complex forms)

**Modal requirements:**
```tsx
// Focus trap: focus goes to modal on open, returns to trigger on close
// Keyboard: Escape closes, Tab cycles within modal
// Backdrop: click closes (unless destructive confirmation)
// ARIA: role="dialog", aria-modal="true", aria-labelledby=[title-id]
// Animation: @starting-style for enter, transition for exit

dialog {
  &:modal {
    background: var(--color-surface);
    border-radius: var(--radius-xl);
    padding: var(--space-8);
    max-width: min(90vw, 560px);
    border: 1px solid var(--color-border);
    box-shadow: 0 16px 64px oklch(0% 0 0 / 0.4);

    /* Animate open */
    opacity: 1;
    transform: scale(1);
    transition: opacity 200ms, transform 200ms, display 200ms allow-discrete;

    @starting-style {
      opacity: 0;
      transform: scale(0.96);
    }

    /* Animate close */
    &:not(:open) {
      opacity: 0;
      transform: scale(0.96);
    }
  }
}
```

---

### R7 — Toast / notification rules

**One toast type per trigger:**
- Success: green badge, 4s auto-dismiss
- Error: red badge, persist until dismissed
- Info: neutral, 4s auto-dismiss
- Warning: amber badge, persist until acknowledged

**One toast at a time.** Queue, don't stack.

```tsx
// Container: fixed, top-right on desktop; bottom on mobile
// aria-live="polite" for success/info
// aria-live="assertive" for errors
// Keyboard: Escape dismisses; Tab moves focus to dismiss button
```

---

### R8 — Badge / status rules

Badges communicate state. State requires both color AND label — never color alone.

```css
/* Pattern: color is semantic, label is explicit */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  padding: 0.125rem 0.5rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
}

.badge::before {
  content: '';
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
}
```

**Semantic colors:**
```css
.badge-active   { color: oklch(38% 0.16 145); background: oklch(94% 0.08 145); }
.badge-pending  { color: oklch(42% 0.16 65);  background: oklch(95% 0.08 65); }
.badge-error    { color: oklch(38% 0.18 25);  background: oklch(94% 0.08 25); }
.badge-inactive { color: oklch(45% 0 0);      background: oklch(93% 0 0); }
```

---

### R9 — Tooltip rules

Tooltips are for supplementary information only. Never hide required information in a tooltip.

**Required:**
- `role="tooltip"` + `id` linked to trigger via `aria-describedby`
- Appears on hover (desktop) + focus (keyboard)
- Never on click (that's a popover)
- Maximum 80 characters — longer needs a popover or inline explanation

**CSS Anchor Positioning (CSS 2026 — no JavaScript needed):**
```css
.tooltip-trigger { anchor-name: --tt; }

.tooltip {
  position: absolute;
  position-anchor: --tt;
  bottom: calc(anchor(top) - 8px);
  left: anchor(center);
  translate: -50% -100%;
  /* ... */
}
```

---

### R10 — Select / dropdown rules

Native `<select>` for simple single-value selection (≤ 8 options, mobile-critical path).
Custom dropdown for: multi-select, search-within, grouped options, custom rendering.

**Custom dropdown requirements:**
- `role="combobox"` (single) or `role="listbox"` (multi)
- `aria-expanded` on trigger
- `aria-activedescendant` pointing to highlighted option
- Arrow keys navigate options; Enter selects; Escape closes
- Search: `role="searchbox"` within `role="combobox"`
- Minimum option height: 36px (32px dense)

---

## Component Audit Checklist

```
[ ] All states designed before any state is implemented
[ ] Button hierarchy: primary / secondary / tertiary / destructive defined
[ ] Every input: label visible, linked by for/id, error below field
[ ] No nested cards
[ ] Modals: focus trapped, Escape closes, backdrop click closes
[ ] Badges: color + label (never color alone)
[ ] Tooltips: ≤ 80 chars, aria-describedby linked
[ ] Touch targets ≥ 44×44px on all interactive elements
[ ] Focus-visible ring on every interactive element (not outline: none)
[ ] prefers-reduced-motion: all transitions collapse or reduce
```

## Related Files

- `skills/global-design/quality-gates.md` — Gate 4 (all states required)
- `rules/07-accessibility.md` — ARIA patterns per component type
- `rules/10-forms.md` — full form rules
- `references/accessibility.md` — ARIA recipes and keyboard nav patterns
- `references/forms.md` — input anatomy, validation patterns
