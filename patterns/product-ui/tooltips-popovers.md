# Pattern — Tooltips and Popovers

> Tooltips reveal a label for icon-only controls. Popovers reveal richer content on click. The key distinction: tooltips are for labeling, popovers are for contextual information. Never reverse the two.

---

## Decision Tree

```
Does the trigger have visible text?
  └─ Yes → No tooltip needed
  └─ No (icon-only button) → Tooltip required for accessibility

Does the trigger reveal interactive content (links, buttons, forms)?
  └─ Yes → Popover (click-triggered, dismissable)
  └─ No → Tooltip (hover-triggered, auto-dismiss on blur)

Does content persist when user moves cursor away?
  └─ Yes → Popover
  └─ No → Tooltip
```

---

## Pattern 1 — Tooltip

Simple text label for icon buttons, badges, or truncated text.

```html
<!-- Icon button with tooltip -->
<button
  class="icon-btn"
  type="button"
  aria-label="Copy to clipboard"
  data-tooltip="Copy to clipboard"
>
  <svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24"
    fill="none" stroke="currentColor" stroke-width="1.5"
    stroke-linecap="round" stroke-linejoin="round">
    <rect width="14" height="14" x="8" y="8" rx="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/>
  </svg>
</button>
```

```css
/* CSS-only tooltip — no JS required */
[data-tooltip] {
  position: relative;
}

[data-tooltip]::before {
  content: attr(data-tooltip);
  position: absolute;
  bottom: calc(100% + var(--space-2));
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  padding: var(--space-1) var(--space-2);
  border-radius: var(--radius-sm);
  background: var(--color-text-primary);
  color: var(--color-surface);
  font-size: 12px;
  font-family: var(--font-body);
  font-weight: var(--font-weight-medium);
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  transition:
    opacity   var(--duration-fast) var(--ease-smooth),
    transform var(--duration-fast) var(--ease-smooth);
  z-index: var(--z-tooltip);
}

[data-tooltip]::after {
  content: '';
  position: absolute;
  bottom: calc(100% + var(--space-1));
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  border: 5px solid transparent;
  border-top-color: var(--color-text-primary);
  pointer-events: none;
  opacity: 0;
  transition:
    opacity   var(--duration-fast) var(--ease-smooth),
    transform var(--duration-fast) var(--ease-smooth);
  z-index: var(--z-tooltip);
}

[data-tooltip]:hover::before,
[data-tooltip]:hover::after,
[data-tooltip]:focus-visible::before,
[data-tooltip]:focus-visible::after {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}

/* Tooltip below trigger */
[data-tooltip-pos="bottom"]::before {
  top: calc(100% + var(--space-2));
  bottom: auto;
  transform: translateX(-50%) translateY(-4px);
}
[data-tooltip-pos="bottom"]::after {
  top: calc(100% + var(--space-1));
  bottom: auto;
  border-top-color: transparent;
  border-bottom-color: var(--color-text-primary);
  transform: translateX(-50%) translateY(-4px);
}
[data-tooltip-pos="bottom"]:hover::before,
[data-tooltip-pos="bottom"]:hover::after,
[data-tooltip-pos="bottom"]:focus-visible::before,
[data-tooltip-pos="bottom"]:focus-visible::after {
  transform: translateX(-50%) translateY(0);
}

/* Tooltip right */
[data-tooltip-pos="right"]::before {
  top: 50%;
  bottom: auto;
  left: calc(100% + var(--space-2));
  transform: translateY(-50%) translateX(-4px);
}
[data-tooltip-pos="right"]::after {
  top: 50%;
  bottom: auto;
  left: calc(100% + var(--space-1));
  border-top-color: transparent;
  border-right-color: var(--color-text-primary);
  transform: translateY(-50%) translateX(-4px);
}
[data-tooltip-pos="right"]:hover::before,
[data-tooltip-pos="right"]:hover::after {
  transform: translateY(-50%) translateX(0);
}

@media (prefers-reduced-motion: reduce) {
  [data-tooltip]::before,
  [data-tooltip]::after {
    transition: none;
    transform: translateX(-50%) !important;
  }
}
```

---

## Pattern 2 — Popover (Click-triggered)

Richer content: description, metadata, links, or a short form.

```html
<div class="popover-wrapper">
  <button
    class="btn btn--ghost"
    type="button"
    aria-expanded="false"
    aria-controls="popover-member"
    aria-haspopup="true"
    id="trigger-member"
  >
    <img src="/avatar.jpg" alt="" class="avatar" aria-hidden="true" />
    Alexis Martin
  </button>

  <div
    class="popover"
    id="popover-member"
    role="dialog"
    aria-labelledby="trigger-member"
    aria-modal="false"
    hidden
  >
    <div class="popover__header">
      <img src="/avatar.jpg" alt="Alexis Martin" class="popover__avatar" />
      <div>
        <p class="popover__name">Alexis Martin</p>
        <p class="popover__role">Senior Engineer</p>
      </div>
    </div>
    <div class="popover__body">
      <p class="popover__meta">Member since January 2024</p>
      <p class="popover__meta">5 open pull requests</p>
    </div>
    <div class="popover__footer">
      <a href="/team/alexis" class="popover__link">View profile</a>
      <a href="mailto:alexis@example.com" class="popover__link">Send email</a>
    </div>
  </div>
</div>
```

```css
.popover-wrapper { position: relative; display: inline-flex; }

.popover {
  position: absolute;
  top: calc(100% + var(--space-2));
  left: 0;
  min-width: 240px;
  max-width: 320px;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  z-index: var(--z-dropdown);
  overflow: hidden;

  @starting-style {
    opacity: 0;
    transform: translateY(-6px);
  }
  opacity: 1;
  transform: translateY(0);
  transition:
    opacity   var(--duration-fast) var(--ease-spring),
    transform var(--duration-fast) var(--ease-spring);
}

.popover[hidden] { display: none; }

.popover__header {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-4);
  border-bottom: 1px solid var(--color-border);
}

.popover__avatar {
  width: 40px; height: 40px;
  border-radius: var(--radius-full);
  object-fit: cover;
  flex-shrink: 0;
}

.popover__name {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-primary);
}

.popover__role {
  font-size: 12px;
  color: var(--color-text-secondary);
}

.popover__body {
  padding: var(--space-3) var(--space-4);
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.popover__meta {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
}

.popover__footer {
  display: flex;
  gap: var(--space-3);
  padding: var(--space-3) var(--space-4);
  border-top: 1px solid var(--color-border);
}

.popover__link {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-accent);
  text-decoration: none;
}

.popover__link:hover { text-decoration: underline; }

@media (prefers-reduced-motion: reduce) {
  .popover {
    transition: none;
  }
  @starting-style { .popover { opacity: 0; transform: none; } }
}
```

```js
class Popover {
  constructor (wrapper) {
    this.trigger = wrapper.querySelector('[aria-expanded]')
    this.panel   = wrapper.querySelector('[role="dialog"]')
    this.focusable = null

    this.trigger.addEventListener('click', () => this.toggle())

    document.addEventListener('click', e => {
      if (!wrapper.contains(e.target)) this.close()
    })

    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') this.close()
    })
  }

  toggle () {
    const open = this.trigger.getAttribute('aria-expanded') === 'true'
    open ? this.close() : this.open()
  }

  open () {
    this.panel.hidden = false
    this.trigger.setAttribute('aria-expanded', 'true')
    // Focus first focusable element in popover
    const first = this.panel.querySelector('a, button, input, [tabindex]:not([tabindex="-1"])')
    if (first) first.focus()
  }

  close () {
    this.panel.hidden = true
    this.trigger.setAttribute('aria-expanded', 'false')
    this.trigger.focus()
  }
}

document.querySelectorAll('.popover-wrapper').forEach(el => new Popover(el))
```

---

## Pattern 3 — Info Tooltip (Non-interactive)

For form fields, labels, and data values needing a clarifying explanation.

```html
<label class="field-label" for="api-key">
  API Key
  <button class="info-btn" type="button" aria-label="About API keys"
    data-tooltip="Your secret API key. Never share it publicly.">
    <svg aria-hidden="true" width="14" height="14" viewBox="0 0 24 24" fill="none"
      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>
    </svg>
  </button>
</label>
<input id="api-key" class="field-input" type="password" autocomplete="current-password" />
```

```css
.info-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 16px; height: 16px;
  padding: 0;
  border: none;
  background: transparent;
  color: var(--color-text-muted);
  cursor: help;
  vertical-align: middle;
}

.info-btn:hover { color: var(--color-text-secondary); }
.info-btn:focus-visible {
  outline: 2px solid var(--color-border-focus);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}
```

---

## Positioning Rules

```
Default position: above trigger (tooltip) / below trigger (popover)

Flip to opposite when:
  - Not enough space above (tooltip): show below
  - Not enough space below (popover): show above
  - Trigger is near left edge: align popover to right
  - Trigger is near right edge: align popover to left

For complex positioning needs, use Floating UI:
  import { computePosition, flip, shift, offset } from '@floating-ui/dom'
```

---

## Anti-Patterns

```
× Tooltip with interactive content (links, buttons) — use popover
× Tooltip revealed only on focus but not on hover — must do both
× Tooltip on disabled elements — users can't focus disabled elements
× Tooltip with more than 60 characters — consider popover instead
× Popover without close on Escape — required for keyboard users
× Popover without focus management — focus must move into popover on open
× Nested popovers — maximum 1 popover layer
× Tooltip delay > 500ms — annoying for users who hover over many elements
× Tooltip on touch devices without fallback — hover events unreliable on mobile
```

---

*Pattern version: global-design-skill v1.0 — `patterns/product-ui/tooltips-popovers.md`*  
*Related: `patterns/product-ui/modals.md`, `patterns/product-ui/command-palette.md`, `rules/07-accessibility.md`*
