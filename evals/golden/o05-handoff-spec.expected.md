# Golden output — o05: frontend handoff spec for a pricing toggle

**Prompt:** "Use global-design-skill and write a frontend handoff spec for a pricing toggle component (monthly/annual)."

---

## What a correct response must include

Must follow the developer handoff format (`templates/specs/frontend-tz.md`) so a developer implements without a single follow-up question (Gate 8).

### 1. All component states

Must enumerate `states` for the toggle:
- **Idle** (monthly selected vs annual selected)
- **Hover** (desktop, inside `@media (hover: hover)`)
- **Active/pressed**
- **Focus-visible** (visible ring)
- **Disabled** (if a plan lacks annual pricing)
- Transition behavior between monthly ↔ annual (including the price update)

### 2. ARIA and semantics

Must specify `aria`:
- Implemented as a `role="switch"` (or grouped radios) with `aria-checked`
- `aria-label` describing the billing period
- `aria-live` announcement when the displayed prices change

### 3. Keyboard

Must specify `keyboard` operation: focusable, toggled with `Space`/`Enter`, arrow keys if radios; visible focus throughout.

### 4. Tokens

Must reference design `token` names, not raw values:
- Track/thumb colors via `var(--color-*)`, spacing via `var(--space-*)`, radius via `var(--radius-full)`

### 5. Acceptance criteria

Must give a testable `acceptance criteria` checklist (pass/fail), e.g.:
- [ ] Toggling updates all plan prices and the annual savings badge
- [ ] Keyboard operable (Tab + Space/Enter)
- [ ] Touch target ≥ 44×44px
- [ ] `prefers-reduced-motion` collapses the slide animation
- [ ] State announced to assistive tech

### 6. Gate compliance

Must satisfy Gates 4, 6, 7, 8.

---

## What a correct response must NOT include

- "`ask developer`" / deferring decisions back to the implementer
- "`TBD`" placeholders for any state or value
- "`figure out`" the animation/behavior — every value must be exact
- Raw hex/px values instead of tokens
