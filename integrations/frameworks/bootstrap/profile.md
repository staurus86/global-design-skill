# Bootstrap 5.3 — Framework Profile

> Bootstrap is the most widely deployed CSS framework. Best for enterprise dashboards, admin panels, and projects where teams need documented WCAG 2.2 compliance and 30+ pre-built components with zero custom design work.

**Auto-detected via:** `"bootstrap"` in package.json  
**Install:** `npm install bootstrap`  
**CDN (no build step):** `<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3/dist/css/bootstrap.min.css">`

---

## When to Use Bootstrap

- Enterprise or government projects requiring documented accessibility compliance
- Admin dashboards where dev speed > design uniqueness
- Teams already trained on Bootstrap — no ramp-up
- Rapid prototypes needing 30+ components out of the box
- Projects that must support wide browser compatibility (Bootstrap's grid is battle-tested)

**Do not choose Bootstrap when:** design differentiation matters, you want utility-first workflow, or you're building a consumer-facing product where "Bootstrap look" is a liability.

---

## OKLCH Adaptation

Override Bootstrap's CSS custom properties with OKLCH values in your `globals.css`:

```css
:root {
  /* Replace Bootstrap hex defaults with OKLCH tokens */
  --bs-primary:          oklch(57% 0.22 258);
  --bs-primary-rgb:      /* leave as-is for Bootstrap JS components */;
  --bs-body-bg:          oklch(100% 0.003 258);
  --bs-body-color:       oklch(18% 0.02 258);
  --bs-secondary-color:  oklch(45% 0.02 258);
  --bs-border-color:     oklch(88% 0.01 258);
  --bs-border-radius:    var(--radius-md, 12px);
  --bs-border-radius-lg: var(--radius-lg, 16px);
  --bs-border-radius-sm: var(--radius-sm, 8px);
}
```

**Never use Bootstrap's default color utilities directly:**
```html
<!-- BANNED — raw Bootstrap color -->
<button class="btn btn-primary" style="background:#0d6efd">CTA</button>

<!-- OK — after OKLCH override above, btn-primary uses your token -->
<button class="btn btn-primary">CTA</button>
```
The token override makes the class safe. Forbidden: adding explicit `style="background:#0d6efd"`.

---

## Typography

Bootstrap uses `rem` units. Apply `clamp()` only on hero headings — Bootstrap's scale is fine for body text:

```css
/* Override display headings with clamp() */
.display-1 { font-size: clamp(3rem,  7vw + 1rem, 5rem);   line-height: 1.1; }
.display-2 { font-size: clamp(2.5rem, 6vw + 1rem, 4.5rem); line-height: 1.1; }
.display-3 { font-size: clamp(2rem,   5vw + 1rem, 4rem);   line-height: 1.1; }

/* Ensure body text ≥ 16px (Bootstrap default is 1rem — OK) */
/* Ensure form inputs ≥ 16px to prevent iOS zoom */
.form-control { font-size: 1rem; }
```

Banned Bootstrap font utilities: `.display-*` with fixed `px` overrides — use `clamp()` above.

---

## Animation with motion/react

Bootstrap's JS components (modal, collapse, dropdown, toast) emit events. Wire `motion/react` to those events in React:

```tsx
import { motion, AnimatePresence } from 'motion/react'

// Animate Bootstrap modal content (not the backdrop)
function AnimatedModal({ show, children }: { show: boolean; children: React.ReactNode }) {
  return (
    <AnimatePresence>
      {show && (
        <motion.div
          initial={{ opacity: 0, scale: 0.96, y: 8 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.96, y: 8 }}
          transition={{ duration: 0.2, ease: 'easeOut' }}
        >
          {children}
        </motion.div>
      )}
    </AnimatePresence>
  )
}
```

For vanilla Bootstrap (no React): use Bootstrap's built-in CSS transitions — they are reduced-motion safe.

---

## Banned Patterns (Bootstrap-Specific)

| Banned | Problem | Replacement |
|---|---|---|
| `btn btn-primary` without OKLCH override | Default blue hex | Override `--bs-primary` first |
| `text-muted` | Often fails 4.5:1 contrast | Use explicit OKLCH value |
| `bg-gradient` utility | Decorative noise | Solid OKLCH background |
| `shadow-lg` default | Generic appearance | `box-shadow: 0 4px 24px oklch(0% 0 0 / 0.08)` |
| `col-*` with no responsive variant | Breaks on mobile | Always pair with `col-md-*` or `col-lg-*` |
| Bootstrap's `$primary` Sass variable | Overridden by CSS custom property | Set `--bs-primary` in `:root` |

---

## Checklist

- [ ] `--bs-primary` overridden with OKLCH token
- [ ] `--bs-body-bg` and `--bs-body-color` use OKLCH
- [ ] `display-*` headings use `clamp()`
- [ ] No `text-muted` — replaced with OKLCH value
- [ ] No `bg-gradient` utilities
- [ ] `motion/react` used for interactive animations, not Bootstrap JS transitions
- [ ] Lighthouse accessibility ≥ 90 (Bootstrap's defaults usually pass — verify overrides didn't break contrast)
