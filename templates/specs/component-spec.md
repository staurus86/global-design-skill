# Component Spec — Template

> Use for individual UI components (buttons, inputs, modals, cards, dropdowns, etc.). Fill all sections. A spec with "TBD" does not pass review.

**Usage:** Copy this template for every new component added to the design system.

---

## Component: [Name]

**Category:** `[ ] Primitive` `[ ] Composite` `[ ] Pattern`

> Primitive = single element (button, input, badge). Composite = multiple primitives (card, form-field, modal). Pattern = full interaction flow (search-with-dropdown, date-picker).

**Ticket / link:** [Linear / Jira / GitHub URL]

**Design source:** [Figma frame URL or local path]

**Status:** `[ ] Proposal` `[ ] Approved` `[ ] In development` `[ ] Shipped`

---

## Purpose

[One sentence: what problem this component solves. What it is NOT for.]

**Do not use for:**
- [List specific misuse cases]

---

## Anatomy

[Label every part of the component. Use diagram or list.]

```
[ComponentName]
├── [Part 1] — purpose
├── [Part 2] — purpose
│   ├── [Sub-part A] — purpose
│   └── [Sub-part B] — purpose (optional)
└── [Part 3] — purpose
```

---

## Props / API

```ts
interface [ComponentName]Props {
  // Required
  [propName]: [type];          // [description]

  // Optional
  [propName]?: [type];         // [description] — default: [value]
  [propName]?: [type];         // [description] — default: [value]

  // Event handlers
  on[Event]?: (value: [type]) => void;  // [when it fires]

  // Accessibility
  'aria-label'?: string;       // required when no visible label
}
```

---

## Variants

[Every variant must be listed. No "etc."]

| Variant | Token / prop value | When to use |
|---|---|---|
| Default | `variant="default"` | [description] |
| [Variant 2] | `variant="[value]"` | [description] |
| [Variant 3] | `variant="[value]"` | [description] |

**Sizes** (if applicable):

| Size | Height | Font | Padding-inline | Touch target |
|---|---|---|---|---|
| `sm` | [px] | [token] | [token] | [px]×[px] |
| `md` | [px] | [token] | [token] | [px]×[px] |
| `lg` | [px] | [token] | [token] | [px]×[px] |

---

## States

### Idle (default)

```css
background:    var(--[token]);
color:         var(--[token]);
border:        [px] solid var(--[token]);
border-radius: var(--[token]);
shadow:        [value or "none"];
```

### Hover `@media (hover: hover)`

```css
/* Changes from idle: */
background:   var(--[token]);
border-color: var(--[token]);
/* Transition: */
transition: background [ms] [cubic-bezier(...)], border-color [ms] [...];
```

### Active / Pressed

```css
transform:  scale([value]);
transition: transform [ms] [cubic-bezier(...)];
```

### Focus-Visible (keyboard)

```css
outline:        2px solid var(--color-accent);
outline-offset: [px];
border-radius:  [same as component or override];
```

### Disabled

```css
opacity:        0.4;
cursor:         not-allowed;
pointer-events: none;
/* aria-disabled="true" on element */
```

### Loading (if applicable)

```css
/* Button: label changes to "[Verb]ing…", spinner appears */
/* Disabled during loading */
/* aria-busy="true" */
```

```
Trigger:    [what action triggers loading]
Indicator:  [spinner / skeleton / pulse]
Duration:   [< 100ms: none | 100ms–1s: spinner | 1–10s: progress]
```

### Error (if applicable)

```css
border-color: var(--color-error);
/* Additional: */
```

```
Display:   [inline message / tooltip / border highlight]
Copy:      "[What failed] — [Why] — [How to fix]"
aria-live: "polite" (non-blocking) | "assertive" (blocking)
```

### Success (if applicable)

```
Display:   [inline / toast / icon swap]
Copy:      "[Exact success message]"
Duration:  [auto-dismiss Ns / persist]
```

---

## Tokens

[Complete token list for this component. No raw values.]

```css
/* [ComponentName] tokens */
--[component]-background:      var(--color-surface);
--[component]-border:          var(--color-border);
--[component]-text:            var(--color-text-primary);
--[component]-radius:          var(--radius-md);
--[component]-padding-block:   var(--space-[n]);
--[component]-padding-inline:  var(--space-[n]);
--[component]-height:          [px];

/* Variant: [name] */
--[component]-[variant]-background: var(--color-[token]);
--[component]-[variant]-text:       var(--color-[token]);
```

---

## Typography

```css
font-size:   var(--text-[scale]);
font-weight: [400 / 500 / 600];
line-height: [1.2 / 1.4 / 1.65];
letter-spacing: [value or "normal"];
```

---

## Animation

```css
/* Entry (if applicable) */
@starting-style {
  opacity: 0;
  transform: translateY([px]) scale([value]);
}

transition:
  opacity    [ms] cubic-bezier([...]),
  transform  [ms] cubic-bezier([...]);
```

**Trigger:** `[on mount / on open / on hover / on scroll entry]`

**prefers-reduced-motion:** `[opacity-only / no animation]`

---

## ARIA

```html
<[element]
  role="[role]"
  aria-label="[exact string — not 'label here']"
  aria-expanded="[true|false — if applicable]"
  aria-controls="[id — if applicable]"
  aria-haspopup="[listbox|dialog|menu — if applicable]"
  aria-describedby="[id — if applicable]"
  aria-disabled="[true|false — if applicable]"
  aria-invalid="[true|false — if applicable]"
  aria-busy="[true|false — if applicable]"
>
```

**Keyboard behavior:**

| Key | Action |
|---|---|
| `Tab` | [focus behavior] |
| `Enter` | [action] |
| `Space` | [action] |
| `Escape` | [action — e.g., closes, cancels] |
| `Arrow ↑↓` | [if applicable] |
| `Arrow ←→` | [if applicable] |

**Focus management:**

- On open: focus moves to `[element]`
- On close: focus returns to `[trigger]`
- Focus trap: `[yes — inside dialog/modal | no]`

---

## Responsive behavior

| Breakpoint | Changes |
|---|---|
| `≥ 1280px` | [desktop — baseline behavior] |
| `768px – 1279px` | [tablet — what changes, or "no changes"] |
| `≤ 767px` | [mobile — exact changes, touch targets] |

**Touch targets (mobile):** minimum 44×44px — all interactive elements.

---

## Composition rules

[Where this component can and cannot be used. What it can contain.]

**Can contain:**
- [Allowed child types]

**Cannot contain:**
- [Explicitly forbidden nesting]

**Composable with:**
- `[OtherComponent]` — [how and why]

**Never inside:**
- `[Component]` — [reason]

---

## Implementation notes

[Framework-specific implementation details. Dependencies. Known quirks.]

**React:**
```tsx
// Minimal example
<[ComponentName]
  [prop]={[value]}
  on[Event]={() => {}}
>
  [children or content]
</[ComponentName]>
```

**Dependencies:**
- `[package@version]` — [why needed]

**Known issues / quirks:**
- [Browser-specific behavior if any]
- [Edge case to handle]

---

## Do not

- Do not use raw pixel values — use tokens
- Do not add `margin` to the component itself — use layout context
- Do not override internal styles via class selectors — use CSS custom properties
- Do not use this component for [specific misuse]
- [Add component-specific prohibitions]

---

## Acceptance criteria

```
[ ] Renders correctly in all [N] variants × [M] sizes
[ ] All states present: idle, hover, active, focus-visible, disabled [+ applicable]
[ ] Keyboard navigable: Tab reaches, Enter/Space activates
[ ] Focus-visible ring: 2px solid var(--color-accent), correct offset
[ ] Touch target ≥ 44×44px on mobile
[ ] Screen reader announces: role + name + state
[ ] Animation respects prefers-reduced-motion
[ ] No raw hex / pixel values — all tokens
[ ] Tokens override works: custom --[component]-* vars apply correctly
[ ] Composites: all child components meet their own criteria
[ ] [Component-specific criterion]
```

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | [YYYY-MM-DD] | Initial spec |

---

*Template version: global-design-skill v1.0 — `templates/specs/component-spec.md`*
