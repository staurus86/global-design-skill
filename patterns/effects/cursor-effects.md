# Pattern — Cursor Effects

> Custom cursors transform a mouse pointer into a design element. Use sparingly — one well-executed cursor effect beats 10 mediocre ones. All effects include reduced-motion and touch-device detection.

---

## Rule: When to Use Custom Cursors

**Use when:**
- Portfolio sites with strong creative identity
- Agency/studio sites where interaction design IS the product
- Dark, premium SaaS landing pages (subtle cursor glow)
- Full-screen interactive experiences

**Never use when:**
- Productivity apps (Linear, Notion — users need the native cursor)
- E-commerce (removes trust signals)
- Data-heavy dashboards
- Any app where cursor precision matters (forms, tables, selects)

**Always provide:**
- `cursor: none` only when custom cursor is visible
- Restore native cursor when custom cursor fails to load
- Touch device detection (no custom cursor on touch)
- `prefers-reduced-motion` fallback

---

## Effect 1 — Glow Cursor

Subtle radial gradient follows the cursor. Barely visible — just adds atmospheric depth. Used by Raycast, Linear, and most premium dark SaaS.

```javascript
// This is the spotlight effect from visual-effects.md — the cursor IS the spotlight
// See patterns/effects/visual-effects.md Effect 3 for implementation

// Minimal version for just a cursor glow:
document.addEventListener('mousemove', (e) => {
  document.documentElement.style.setProperty('--cursor-x', `${e.clientX}px`);
  document.documentElement.style.setProperty('--cursor-y', `${e.clientY}px`);
});
```

```css
.hero::after {
  content: '';
  position: fixed;   /* fixed = follows viewport, not scroll */
  inset: 0;
  background: radial-gradient(
    300px circle at var(--cursor-x, -999px) var(--cursor-y, -999px),
    oklch(65% 0.15 258 / 0.08),
    transparent 50%
  );
  pointer-events: none;
  z-index: 1;
}
```

Note: Starting at `-999px` ensures glow is off-screen until first mousemove.

---

## Effect 2 — Custom Dot Cursor

Replaces the native cursor with a small colored dot that follows with spring physics.

```html
<!-- Add to body, before closing </body> -->
<div class="cursor" aria-hidden="true"></div>
```

```css
/* Hide native cursor on elements that have custom cursor */
body:has(.cursor) {
  cursor: none;
}

/* Restore native cursor on interactive elements where precision matters */
input, textarea, select, [contenteditable] {
  cursor: text !important;
}

.cursor {
  position: fixed;
  top: 0;
  left: 0;
  width: 12px;
  height: 12px;
  background: var(--color-accent);
  border-radius: 50%;
  pointer-events: none;
  z-index: 99999;
  transform: translate(var(--cursor-x, -100px), var(--cursor-y, -100px)) translate(-50%, -50%);
  transition: transform 60ms linear, width 250ms var(--ease-spring), height 250ms var(--ease-spring), background 250ms var(--ease-smooth);
  mix-blend-mode: normal;
}

/* Expand on hover over clickable elements */
body:has(a:hover, button:hover) .cursor,
.cursor.hovering {
  width: 40px;
  height: 40px;
  background: oklch(from var(--color-accent) l c h / 0.2);
  border: 1px solid var(--color-accent);
}

/* Compress on click */
body:has(.cursor-clicking) .cursor,
.cursor.clicking {
  width: 8px;
  height: 8px;
  transition-duration: 80ms;
}

@media (pointer: coarse) {
  /* Touch device — never show custom cursor */
  .cursor { display: none; }
  body { cursor: auto !important; }
}

@media (prefers-reduced-motion: reduce) {
  .cursor { transition: none; }
}
```

```javascript
class CustomCursor {
  constructor() {
    // Skip on touch devices
    if (!window.matchMedia('(pointer: fine)').matches) return;

    this.cursor = document.querySelector('.cursor');
    if (!this.cursor) return;

    this.pos = { x: -100, y: -100 };
    this.current = { x: -100, y: -100 };

    this.init();
  }

  init() {
    document.addEventListener('mousemove', (e) => {
      this.pos.x = e.clientX;
      this.pos.y = e.clientY;
    });

    document.addEventListener('mousedown', () => this.cursor.classList.add('clicking'));
    document.addEventListener('mouseup', () => this.cursor.classList.remove('clicking'));

    // Track hover on interactive elements
    document.addEventListener('mouseover', (e) => {
      if (e.target.closest('a, button, [role="button"], label')) {
        this.cursor.classList.add('hovering');
      }
    });
    document.addEventListener('mouseout', (e) => {
      if (e.target.closest('a, button, [role="button"], label')) {
        this.cursor.classList.remove('hovering');
      }
    });

    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      this.lerp(); // Smooth follow
    } else {
      // Direct follow (no lerp) for reduced-motion
      document.addEventListener('mousemove', (e) => {
        this.cursor.style.setProperty('--cursor-x', `${e.clientX}px`);
        this.cursor.style.setProperty('--cursor-y', `${e.clientY}px`);
      });
    }
  }

  lerp() {
    // Lerp towards mouse position for smooth follow
    this.current.x += (this.pos.x - this.current.x) * 0.15;
    this.current.y += (this.pos.y - this.current.y) * 0.15;

    this.cursor.style.setProperty('--cursor-x', `${this.current.x}px`);
    this.cursor.style.setProperty('--cursor-y', `${this.current.y}px`);

    requestAnimationFrame(() => this.lerp());
  }
}

new CustomCursor();
```

---

## Effect 3 — Mix-Blend-Mode Cursor (Color Inversion)

Cursor inverts colors of everything beneath it. Works especially well on black/white or high-contrast designs.

```html
<div class="cursor-invert" aria-hidden="true"></div>
```

```css
.cursor-invert {
  position: fixed;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: white;
  mix-blend-mode: difference;
  pointer-events: none;
  z-index: 99999;
  transform: translate(var(--cursor-x, -100px), var(--cursor-y, -100px)) translate(-50%, -50%);
  transition: transform 80ms linear;
}

/* Expand when hovering clickable elements */
.cursor-invert.hovering {
  width: 60px;
  height: 60px;
  transition: transform 80ms linear, width 300ms var(--ease-spring), height 300ms var(--ease-spring);
}

@media (pointer: coarse) { .cursor-invert { display: none; } }
@media (prefers-reduced-motion: reduce) { .cursor-invert { transition: none; } }
```

Note: `mix-blend-mode: difference` with a white circle inverts whatever is beneath it. White text becomes black, black backgrounds become white. The cursor is invisible on mid-gray surfaces.

**Best on:** Black/white designs (brutalism, minimalism, editorial).  
**Avoid on:** Colorful surfaces — the inversion looks random, not intentional.

---

## Effect 4 — Text-Reveal Cursor

When hovering over specific elements, cursor transforms into text ("View", "Open", "Play").

```html
<div class="cursor-text" aria-hidden="true">
  <span class="cursor-text__label"></span>
</div>
```

```css
.cursor-text {
  position: fixed;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: var(--color-accent);
  color: white;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
  z-index: 99999;
  transform: translate(var(--cursor-x, -200px), var(--cursor-y, -200px)) translate(-50%, -50%) scale(0);
  transition:
    transform 300ms var(--ease-spring),
    opacity 200ms var(--ease-smooth);
  opacity: 0;
}

.cursor-text.active {
  transform: translate(var(--cursor-x, -200px), var(--cursor-y, -200px)) translate(-50%, -50%) scale(1);
  opacity: 1;
}

/* Restore native cursor on the triggering element */
[data-cursor-text] {
  cursor: none;
}

@media (pointer: coarse) { .cursor-text { display: none; } }
@media (prefers-reduced-motion: reduce) {
  .cursor-text { transition: none; transform: none; display: none; }
}
```

```javascript
const textCursor = document.querySelector('.cursor-text');
const label = textCursor?.querySelector('.cursor-text__label');

if (textCursor && window.matchMedia('(pointer: fine)').matches) {
  document.addEventListener('mousemove', (e) => {
    textCursor.style.setProperty('--cursor-x', `${e.clientX}px`);
    textCursor.style.setProperty('--cursor-y', `${e.clientY}px`);
  });

  document.querySelectorAll('[data-cursor-text]').forEach(el => {
    const text = el.dataset.cursorText;

    el.addEventListener('mouseenter', () => {
      label.textContent = text;
      textCursor.classList.add('active');
    });

    el.addEventListener('mouseleave', () => {
      textCursor.classList.remove('active');
    });
  });
}
```

```html
<!-- Triggers text cursor -->
<a href="/case-study" data-cursor-text="View">
  <img src="/project.jpg" alt="Project case study">
</a>

<button type="button" data-cursor-text="Play">
  <div class="video-thumbnail">...</div>
</button>

<a href="/project" data-cursor-text="Open →">
  <div class="portfolio-card">...</div>
</a>
```

---

## Effect 5 — Cursor Trail

A series of dots that follow the cursor with increasing delay. Creates a ribbon/comet effect.

```javascript
class CursorTrail {
  constructor(count = 12) {
    if (!window.matchMedia('(pointer: fine)').matches) return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    this.count = count;
    this.dots = [];
    this.positions = Array(count).fill({ x: -100, y: -100 });
    this.mousePos = { x: -100, y: -100 };

    this.createDots();
    this.track();
    this.animate();
  }

  createDots() {
    for (let i = 0; i < this.count; i++) {
      const dot = document.createElement('div');
      dot.className = 'cursor-trail-dot';
      dot.style.cssText = `
        position: fixed;
        pointer-events: none;
        z-index: 99998;
        width: ${Math.max(4, 12 - i)}px;
        height: ${Math.max(4, 12 - i)}px;
        border-radius: 50%;
        background: var(--color-accent);
        opacity: ${(1 - i / this.count) * 0.6};
        transform: translate(-50%, -50%);
        transition: width 200ms, height 200ms;
      `;
      document.body.appendChild(dot);
      this.dots.push(dot);
    }
  }

  track() {
    document.addEventListener('mousemove', (e) => {
      this.mousePos = { x: e.clientX, y: e.clientY };
    });
  }

  animate() {
    // Each dot follows the one ahead of it
    this.positions[0] = { ...this.mousePos };

    for (let i = 1; i < this.count; i++) {
      const prev = this.positions[i - 1];
      const curr = this.positions[i];
      this.positions[i] = {
        x: curr.x + (prev.x - curr.x) * 0.35,
        y: curr.y + (prev.y - curr.y) * 0.35
      };
    }

    this.dots.forEach((dot, i) => {
      dot.style.left = `${this.positions[i].x}px`;
      dot.style.top = `${this.positions[i].y}px`;
    });

    requestAnimationFrame(() => this.animate());
  }
}

new CursorTrail(10);
```

---

## Cursor Effect Selection Guide

| Context | Best cursor effect | Reason |
|---|---|---|
| Dark SaaS landing page | Glow/spotlight | Atmospheric, invisible to most users — just adds depth |
| Portfolio site | Custom dot or invert | Shows interaction design skill |
| Creative agency | Text-reveal cursor | High impact, branded |
| Editorial/magazine | Mix-blend inversion | Works perfectly on b/w designs |
| Interactive art project | Trail | Full creative expression |
| App / dashboard | None | Never use custom cursors in functional apps |
| E-commerce | None | Trust signals require native cursor |

---

*Pattern version: global-design-skill v1.0 — `patterns/effects/cursor-effects.md`*  
*Updated: 2026-05-20*  
*Related: `patterns/effects/hover-effects.md`, `patterns/effects/visual-effects.md`, `rules/05-animation.md`*
