# Pattern — Hover Effects

> Micro-interactions on hover separate functional interfaces from delightful ones. These are the details users don't consciously notice but immediately feel. All effects respect `prefers-reduced-motion`.

---

## Effect 1 — 3D Card Tilt (Mouse Tracking)

Card tilts toward the cursor in 3D space. Used by Raycast, Linear, Vercel for product screenshots and feature cards.

```html
<div class="tilt-card" data-tilt>
  <div class="tilt-card__inner">
    <!-- Content -->
  </div>
</div>
```

```css
.tilt-card {
  perspective: 1000px;
  cursor: pointer;
}

.tilt-card__inner {
  transform: rotateX(var(--tilt-x, 0deg)) rotateY(var(--tilt-y, 0deg));
  transform-style: preserve-3d;
  transition: transform 150ms linear;
  border-radius: var(--radius-xl);
  background: var(--color-surface-2);
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-lg);
}

/* Shine effect on tilt */
.tilt-card__inner::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: radial-gradient(
    circle at var(--shine-x, 50%) var(--shine-y, 50%),
    oklch(100% 0 0 / 0.12) 0%,
    transparent 60%
  );
  pointer-events: none;
  opacity: 0;
  transition: opacity 200ms var(--ease-smooth);
}

.tilt-card:hover .tilt-card__inner::after {
  opacity: 1;
}

.tilt-card:not(:hover) .tilt-card__inner {
  transition: transform 500ms var(--ease-spring); /* Spring return */
}

@media (prefers-reduced-motion: reduce) {
  .tilt-card__inner { transform: none !important; transition: none; }
  .tilt-card__inner::after { display: none; }
}
```

```javascript
class TiltCard {
  constructor(el) {
    this.el = el;
    this.inner = el.querySelector('.tilt-card__inner');
    this.maxTilt = parseFloat(el.dataset.maxTilt) || 12; // degrees

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    el.addEventListener('mousemove', (e) => this.onMove(e));
    el.addEventListener('mouseleave', () => this.reset());
  }

  onMove(e) {
    const rect = this.el.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width;  // 0–1
    const y = (e.clientY - rect.top) / rect.height;   // 0–1

    const tiltX = (0.5 - y) * this.maxTilt * 2;  // +max to -max
    const tiltY = (x - 0.5) * this.maxTilt * 2;

    this.inner.style.setProperty('--tilt-x', `${tiltX}deg`);
    this.inner.style.setProperty('--tilt-y', `${tiltY}deg`);
    this.inner.style.setProperty('--shine-x', `${x * 100}%`);
    this.inner.style.setProperty('--shine-y', `${y * 100}%`);
  }

  reset() {
    this.inner.style.setProperty('--tilt-x', '0deg');
    this.inner.style.setProperty('--tilt-y', '0deg');
  }
}

document.querySelectorAll('[data-tilt]').forEach(el => new TiltCard(el));
```

---

## Effect 2 — Magnetic Button

Button is attracted toward the cursor when hovering nearby — premium physicality.

```html
<a href="/signup" class="btn btn--primary" data-magnetic>
  Start deploying free
</a>
```

```css
.btn[data-magnetic] {
  display: inline-block;
  transform: translate(var(--mag-x, 0), var(--mag-y, 0));
  transition: transform 300ms var(--ease-smooth);
}

/* Expand the magnetic hit zone via padding */
.btn[data-magnetic]::before {
  content: '';
  position: absolute;
  inset: -24px;  /* Magnetic zone extends 24px beyond button */
}

@media (prefers-reduced-motion: reduce) {
  .btn[data-magnetic] { transform: none !important; }
}
```

```javascript
class MagneticButton {
  constructor(el) {
    this.el = el;
    this.strength = parseFloat(el.dataset.magneticStrength) || 0.4;

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    // Larger zone for detection
    const zone = 80; // px around button that activates magnet

    document.addEventListener('mousemove', (e) => {
      const rect = el.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;

      const dx = e.clientX - centerX;
      const dy = e.clientY - centerY;
      const distance = Math.sqrt(dx * dx + dy * dy);

      if (distance < rect.width / 2 + zone) {
        const moveX = dx * this.strength;
        const moveY = dy * this.strength;
        el.style.setProperty('--mag-x', `${moveX}px`);
        el.style.setProperty('--mag-y', `${moveY}px`);
      } else {
        el.style.setProperty('--mag-x', '0px');
        el.style.setProperty('--mag-y', '0px');
      }
    });
  }
}

document.querySelectorAll('[data-magnetic]').forEach(el => new MagneticButton(el));
```

---

## Effect 3 — Button Hover Fill (Slide / Wipe)

Button background slides in from left/bottom on hover — more dynamic than a simple color change.

```css
/* Slide fill from left */
.btn-fill {
  position: relative;
  overflow: hidden;
  background: transparent;
  border: 1px solid var(--color-accent);
  color: var(--color-accent);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: color 300ms var(--ease-smooth);
}

.btn-fill::after {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--color-accent);
  transform: translateX(-101%);
  transition: transform 350ms var(--ease-spring);
  z-index: -1;
}

.btn-fill:hover {
  color: oklch(97% 0.005 258);
}

.btn-fill:hover::after {
  transform: translateX(0);
}

@media (prefers-reduced-motion: reduce) {
  .btn-fill::after { transition: none; }
  .btn-fill:hover::after { transform: none; }
  .btn-fill:hover { background: var(--color-accent); color: oklch(97% 0.005 258); }
}
```

**Radial fill (from click point outward):**
```css
.btn-radial {
  position: relative;
  overflow: hidden;
  background: var(--color-accent);
  isolation: isolate;
}

.btn-radial::after {
  content: '';
  position: absolute;
  width: 200%;
  aspect-ratio: 1;
  top: 50%;
  left: 50%;
  background: oklch(from var(--color-accent) calc(l + 0.1) c h);
  transform: translate(-50%, -50%) scale(0);
  border-radius: 50%;
  transition: transform 500ms var(--ease-smooth);
  z-index: -1;
}

.btn-radial:hover::after {
  transform: translate(-50%, -50%) scale(1);
}
```

---

## Effect 4 — Image Hover Effects

Images transform on hover to reveal additional information or add dynamism.

```css
/* Zoom on hover */
.img-zoom {
  overflow: hidden;
  border-radius: var(--radius-lg);
}

.img-zoom img {
  transform: scale(1);
  transition: transform 500ms var(--ease-smooth);
  display: block;
  width: 100%;
}

.img-zoom:hover img {
  transform: scale(1.05);
}

/* Clip-path reveal (image un-crops on hover) */
.img-reveal {
  clip-path: inset(5% round var(--radius-lg));
  transition: clip-path 500ms var(--ease-spring);
}

.img-reveal:hover {
  clip-path: inset(0% round var(--radius-lg));
}

/* Color overlay reveal */
.img-overlay {
  position: relative;
  overflow: hidden;
  border-radius: var(--radius-lg);
}

.img-overlay::after {
  content: '';
  position: absolute;
  inset: 0;
  background: oklch(from var(--color-accent) l c h / 0.6);
  opacity: 0;
  transition: opacity 300ms var(--ease-smooth);
}

.img-overlay:hover::after {
  opacity: 1;
}

/* Caption reveal on hover */
.img-caption {
  position: relative;
  overflow: hidden;
  border-radius: var(--radius-lg);
}

.img-caption__text {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: flex-end;
  padding: var(--space-4);
  background: linear-gradient(to top, oklch(0% 0 0 / 0.8) 0%, transparent 60%);
  transform: translateY(100%);
  transition: transform 350ms var(--ease-spring);
  color: white;
}

.img-caption:hover .img-caption__text {
  transform: translateY(0);
}

@media (prefers-reduced-motion: reduce) {
  .img-zoom img,
  .img-reveal,
  .img-overlay::after,
  .img-caption__text {
    transition: none;
    transform: none;
    clip-path: none;
  }
}
```

---

## Effect 5 — Link Underline Draw

Underline draws in from left on hover instead of appearing instantly.

```css
/* Draw underline from left */
.link-draw {
  position: relative;
  text-decoration: none;
  color: inherit;
}

.link-draw::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 100%;
  height: 1px;
  background: currentColor;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 300ms var(--ease-smooth);
}

.link-draw:hover::after,
.link-draw:focus-visible::after {
  transform: scaleX(1);
}

/* Draw from center */
.link-draw-center::after {
  transform-origin: center;
}

/* Retract on mouse-out (exit from right) */
.link-draw-dir::after {
  transform-origin: left;
}

.link-draw-dir:hover::after {
  transform-origin: left;
  transform: scaleX(1);
}

.link-draw-dir:not(:hover)::after {
  transform-origin: right;
  transform: scaleX(0);
  transition: transform 250ms var(--ease-exit);
}

/* Two-color underline (original + hover color) */
.link-draw-two::before,
.link-draw-two::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 100%;
  height: 1px;
}

.link-draw-two::before {
  background: var(--color-border);
}

.link-draw-two::after {
  background: var(--color-accent);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 300ms var(--ease-smooth);
}

.link-draw-two:hover::after {
  transform: scaleX(1);
}

@media (prefers-reduced-motion: reduce) {
  .link-draw::after,
  .link-draw-dir::after,
  .link-draw-two::after {
    transition: none;
    transform: scaleX(1);
  }
}
```

---

## Effect 6 — Card Lift

Cards rise with increased shadow on hover — physical lift metaphor.

```css
.card-lift {
  background: var(--color-surface-2);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
  transform: translateY(0);
  box-shadow: var(--shadow-sm);
  transition:
    transform 250ms var(--ease-spring),
    box-shadow 250ms var(--ease-smooth),
    border-color 250ms var(--ease-smooth);
}

.card-lift:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-color: oklch(from var(--color-border) l c h / 1.5);
}

/* Active: press down */
.card-lift:active {
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
  transition-duration: 100ms;
}

@media (prefers-reduced-motion: reduce) {
  .card-lift {
    transform: none;
    transition: box-shadow 200ms var(--ease-smooth);
  }
  .card-lift:hover { transform: none; }
}
```

---

## Effect 7 — Navigation Item Hover (Sliding Pill)

Active/hover state is a background pill that slides between items.

```html
<nav class="pill-nav" data-pill-nav>
  <a href="#" class="pill-nav__item" data-active>Features</a>
  <a href="#" class="pill-nav__item">Pricing</a>
  <a href="#" class="pill-nav__item">Docs</a>
  <div class="pill-nav__pill" aria-hidden="true"></div>
</nav>
```

```css
.pill-nav {
  position: relative;
  display: inline-flex;
  gap: var(--space-1);
  background: var(--color-surface-2);
  border-radius: var(--radius-full);
  padding: var(--space-1);
}

.pill-nav__item {
  position: relative;
  z-index: 1;
  padding: var(--space-2) var(--space-4);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  text-decoration: none;
  border-radius: var(--radius-full);
  transition: color 200ms var(--ease-smooth);
  white-space: nowrap;
}

.pill-nav__item[data-active] {
  color: var(--color-text-primary);
}

.pill-nav__pill {
  position: absolute;
  top: var(--space-1);
  left: 0;
  height: calc(100% - var(--space-2));
  background: var(--color-surface);
  border-radius: var(--radius-full);
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-sm);
  transition:
    left 300ms var(--ease-spring),
    width 300ms var(--ease-spring);
  pointer-events: none;
}
```

```javascript
class PillNav {
  constructor(el) {
    this.el = el;
    this.pill = el.querySelector('.pill-nav__pill');
    this.items = [...el.querySelectorAll('.pill-nav__item')];

    this.updatePill(el.querySelector('[data-active]'));
    this.listen();
  }

  updatePill(target) {
    if (!target) return;
    const navRect = this.el.getBoundingClientRect();
    const itemRect = target.getBoundingClientRect();

    this.pill.style.left = `${itemRect.left - navRect.left}px`;
    this.pill.style.width = `${itemRect.width}px`;
  }

  listen() {
    this.items.forEach(item => {
      item.addEventListener('mouseenter', () => this.updatePill(item));
      item.addEventListener('focus', () => this.updatePill(item));
    });

    this.el.addEventListener('mouseleave', () => {
      this.updatePill(this.el.querySelector('[data-active]'));
    });
  }
}

document.querySelectorAll('[data-pill-nav]').forEach(el => new PillNav(el));
```

---

## Effect 8 — Button-in-Button (nested trailing icon)

A trailing arrow never sits naked next to the label. It lives in its own circular wrapper, flush with the pill's right inner padding, and translates *independently* of the button on hover — giving mechanical depth instead of a flat color swap.

```html
<button class="bib group">
  <span>Start free trial</span>
  <span class="bib__icon" aria-hidden="true">↗</span>
</button>
```

```css
.bib {
  display: inline-flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-2) var(--space-2) var(--space-2) var(--space-5); /* tighter right — icon fills it */
  border-radius: var(--radius-full);
  background: var(--color-accent);
  color: var(--color-neutral-0);
  transition:
    transform var(--duration-fast) var(--ease-snappy),
    background-color var(--duration-fast) var(--ease-smooth);
}

.bib__icon {
  display: grid;
  place-items: center;
  width: 2rem;
  height: 2rem;
  border-radius: var(--radius-full);
  background: oklch(from var(--color-neutral-0) l c h / 0.15);  /* nested circle */
  transition: transform var(--duration-normal) var(--ease-spring);
}

/* Button presses; inner icon advances diagonally — independent motion = depth */
.bib:active { transform: scale(0.98); }
@media (hover: hover) {
  .bib:hover .bib__icon { transform: translate(2px, -1px) scale(1.05); }
}

@media (prefers-reduced-motion: reduce) {
  .bib, .bib__icon { transition: background-color var(--duration-fast) var(--ease-smooth); }
  .bib:hover .bib__icon { transform: none; }
}
```

**When to use:** primary CTAs with a directional verb (launch, open, continue, external link). The independent icon motion signals "this goes somewhere." Pair the icon glyph with the action's direction — `↗` external, `→` forward, `↓` download. Keep the icon `aria-hidden`; the label carries meaning.

---

## Hover Effect Selection Guide

| Element | Best hover effect | Duration |
|---|---|---|
| Primary CTA button | Magnetic + colored shadow | 300ms spring |
| Directional CTA (launch, external) | Button-in-Button trailing icon | 300ms spring |
| Ghost/outline button | Slide fill from left | 350ms spring |
| Feature card | 3D tilt + shine | 150ms linear |
| Portfolio card | Lift + scale image 1.04 | 250ms spring |
| Navigation link | Underline draw from left | 300ms smooth |
| Pill/tab navigation | Sliding pill | 300ms spring |
| Blog post card | Lift + caption reveal | 250ms smooth |
| Image grid | Zoom + color overlay | 400ms smooth |
| Project thumbnail | Clip-path expand | 400ms spring |

---

*Pattern version: global-design-skill v1.9.4 — `patterns/effects/hover-effects.md`*  
*Updated: 2026-05-30*  
*Related: `patterns/effects/cursor-effects.md`, `patterns/effects/visual-effects.md`, `rules/05-animation.md`*
