# Pattern — Visual Effects

> Ready-to-copy CSS and JS for atmospheric effects that make pages feel premium. These are the foundation of "wow" design — applied before any content is visible. Each effect has a performance note and a reduced-motion fallback.

---

## Effect 1 — Noise Grain Texture

The most impactful one-line upgrade. Adds organic texture to flat surfaces, making digital screens feel tactile.

```css
/* Apply once to body — fixed overlay that doesn't scroll */
body::after {
  content: '';
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 9999;
  opacity: 0.035;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-size: 256px 256px;
}
```

**Tuning:**
- `opacity: 0.025` — barely visible, clean pages
- `opacity: 0.035` — subtle (recommended)
- `opacity: 0.055` — visible on light backgrounds, film-grain feel
- `opacity: 0.08` — heavy grain, use only on dark or warm surfaces

**Dark surfaces:** increase opacity to 0.05–0.07 (dark absorbs the grain)  
**Light surfaces:** keep at 0.025–0.04  
**mix-blend-mode options:** `overlay` (default), `soft-light` (warmer), `screen` (brightens)

**Performance:** SVG data URI is ~350 bytes, zero network request, GPU-composited.

---

## Effect 2 — Mesh Gradient Background

Three overlapping radial gradients create organic color depth. The standard for SaaS dark heroes.

```css
.mesh-bg {
  background:
    radial-gradient(ellipse 60% 50% at 20% 60%,
      oklch(55% 0.22 280 / 0.35) 0%, transparent 70%),
    radial-gradient(ellipse 50% 40% at 80% 20%,
      oklch(65% 0.18 200 / 0.25) 0%, transparent 60%),
    radial-gradient(ellipse 40% 60% at 50% 90%,
      oklch(50% 0.15 320 / 0.2) 0%, transparent 60%),
    oklch(10% 0.01 260);
}
```

**Animated mesh (subtle float):**
```css
.mesh-bg {
  background:
    radial-gradient(ellipse 60% 50% at var(--pos-1-x, 20%) var(--pos-1-y, 60%),
      oklch(55% 0.22 280 / 0.35) 0%, transparent 70%),
    radial-gradient(ellipse 50% 40% at var(--pos-2-x, 80%) var(--pos-2-y, 20%),
      oklch(65% 0.18 200 / 0.25) 0%, transparent 60%),
    oklch(10% 0.01 260);
  animation: mesh-float 20s ease-in-out infinite;
}

@keyframes mesh-float {
  0%, 100% {
    --pos-1-x: 20%; --pos-1-y: 60%;
    --pos-2-x: 80%; --pos-2-y: 20%;
  }
  33% {
    --pos-1-x: 35%; --pos-1-y: 40%;
    --pos-2-x: 65%; --pos-2-y: 35%;
  }
  66% {
    --pos-1-x: 15%; --pos-1-y: 70%;
    --pos-2-x: 75%; --pos-2-y: 10%;
  }
}

/* Register properties for smooth animation */
@property --pos-1-x { syntax: '<percentage>'; inherits: false; initial-value: 20%; }
@property --pos-1-y { syntax: '<percentage>'; inherits: false; initial-value: 60%; }
@property --pos-2-x { syntax: '<percentage>'; inherits: false; initial-value: 80%; }
@property --pos-2-y { syntax: '<percentage>'; inherits: false; initial-value: 20%; }

@media (prefers-reduced-motion: reduce) {
  .mesh-bg { animation: none; }
}
```

**Color recipes for mesh:**

| Mood | Gradient 1 | Gradient 2 | Gradient 3 | Base |
|---|---|---|---|---|
| Electric blue (default) | `oklch(55% 0.22 280)` | `oklch(65% 0.18 200)` | `oklch(50% 0.15 320)` | `oklch(10% 0.01 260)` |
| Warm gold | `oklch(70% 0.15 80)` | `oklch(60% 0.12 50)` | `oklch(55% 0.18 30)` | `oklch(12% 0.02 60)` |
| Aurora green | `oklch(65% 0.20 165)` | `oklch(55% 0.18 220)` | `oklch(60% 0.15 140)` | `oklch(8% 0.01 160)` |
| Rose/pink | `oklch(65% 0.20 350)` | `oklch(60% 0.15 310)` | `oklch(55% 0.18 20)` | `oklch(10% 0.02 340)` |

---

## Effect 3 — Spotlight (Mouse-Tracking Light)

A radial gradient follows the cursor creating a spotlight on dark surfaces. Used by Raycast, Linear, and most premium dark SaaS.

```css
.spotlight {
  position: relative;
  overflow: hidden;
}

.spotlight::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(
    600px circle at var(--mouse-x, 50%) var(--mouse-y, 50%),
    oklch(65% 0.15 258 / 0.15),
    transparent 40%
  );
  opacity: 0;
  transition: opacity 500ms var(--ease-smooth);
  z-index: 1;
}

.spotlight:hover::before {
  opacity: 1;
}
```

```javascript
// Track mouse position — update CSS custom properties
document.querySelectorAll('.spotlight').forEach(el => {
  el.addEventListener('mousemove', (e) => {
    const rect = el.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * 100;
    const y = ((e.clientY - rect.top) / rect.height) * 100;
    el.style.setProperty('--mouse-x', `${x}%`);
    el.style.setProperty('--mouse-y', `${y}%`);
  });
});

// Page-level spotlight (full page tracking)
document.addEventListener('mousemove', (e) => {
  document.documentElement.style.setProperty('--cursor-x', `${e.clientX}px`);
  document.documentElement.style.setProperty('--cursor-y', `${e.clientY}px`);
});
```

**Full-page spotlight (dark hero):**
```css
.hero {
  background:
    radial-gradient(
      800px circle at var(--cursor-x, 50%) var(--cursor-y, 50%),
      oklch(55% 0.15 258 / 0.12),
      transparent 50%
    ),
    oklch(10% 0.015 258);
}
```

**Spotlight on card grid (each card reveals independently):**
```javascript
// Apply to each card separately for per-card spotlight
document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    card.style.setProperty('--mouse-x', `${e.clientX - rect.left}px`);
    card.style.setProperty('--mouse-y', `${e.clientY - rect.top}px`);
  });
});
```

```css
.card {
  background: radial-gradient(
    circle at var(--mouse-x, 50%) var(--mouse-y, 50%),
    oklch(100% 0 0 / 0.05),
    transparent 50%
  ), var(--color-surface-2);
}
```

---

## Effect 4 — Glow / Bloom

Layered box-shadows create a glow effect. Works on buttons, cards, images, and accents.

```css
/* Electric blue glow — for primary buttons or hero accents */
.glow-blue {
  box-shadow:
    0 0 0 1px oklch(65% 0.22 258 / 0.3),
    0 0 20px oklch(65% 0.22 258 / 0.15),
    0 0 60px oklch(65% 0.22 258 / 0.08),
    0 0 120px oklch(65% 0.22 258 / 0.04);
}

/* Warm gold glow */
.glow-gold {
  box-shadow:
    0 0 0 1px oklch(75% 0.18 85 / 0.4),
    0 0 20px oklch(75% 0.18 85 / 0.2),
    0 0 60px oklch(75% 0.18 85 / 0.1);
}

/* Pulse glow animation (use sparingly — one element max) */
.glow-pulse {
  animation: glow-pulse 3s ease-in-out infinite;
}

@keyframes glow-pulse {
  0%, 100% {
    box-shadow:
      0 0 20px oklch(65% 0.22 258 / 0.15),
      0 0 60px oklch(65% 0.22 258 / 0.05);
  }
  50% {
    box-shadow:
      0 0 30px oklch(65% 0.22 258 / 0.25),
      0 0 80px oklch(65% 0.22 258 / 0.12);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glow-pulse { animation: none; }
}

/* Text glow */
.text-glow {
  text-shadow:
    0 0 20px currentColor,
    0 0 40px currentColor;
  opacity: 0.9;
}
```

---

## Effect 5 — Glassmorphism (True Depth)

The common mistake: `backdrop-filter: blur()` alone = washed-out, flat glass. True glassmorphism has specular highlights and inner depth.

```css
.glass {
  /* Base glass surface */
  background: oklch(100% 0 0 / 0.05);
  backdrop-filter: blur(24px) saturate(180%);

  /* Depth: top-edge light + bottom-edge shadow */
  border: 1px solid oklch(100% 0 0 / 0.12);
  box-shadow:
    inset 0 1px 0 oklch(100% 0 0 / 0.18),   /* top edge highlight */
    inset 0 -1px 0 oklch(0% 0 0 / 0.05),    /* bottom edge shadow */
    0 8px 48px oklch(0% 0 0 / 0.35);        /* drop shadow */

  border-radius: var(--radius-xl);
}

/* Light glass (for light mode) */
.glass-light {
  background: oklch(100% 0 0 / 0.6);
  backdrop-filter: blur(16px) saturate(140%);
  border: 1px solid oklch(100% 0 0 / 0.8);
  box-shadow:
    inset 0 1px 0 oklch(100% 0 0 / 0.9),
    0 4px 24px oklch(0% 0 0 / 0.08);
}

/* Frosted dark glass (for nav, modals on dark) */
.glass-frosted {
  background: oklch(12% 0.02 260 / 0.7);
  backdrop-filter: blur(32px) saturate(200%);
  border: 1px solid oklch(100% 0 0 / 0.08);
  box-shadow:
    inset 0 1px 0 oklch(100% 0 0 / 0.12),
    0 16px 64px oklch(0% 0 0 / 0.5);
}
```

**Glass card with hover:**
```css
.glass-card {
  background: oklch(100% 0 0 / 0.04);
  backdrop-filter: blur(20px);
  border: 1px solid oklch(100% 0 0 / 0.1);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
  transition:
    background var(--duration-normal) var(--ease-smooth),
    border-color var(--duration-normal) var(--ease-smooth),
    box-shadow var(--duration-normal) var(--ease-smooth);
}

.glass-card:hover {
  background: oklch(100% 0 0 / 0.07);
  border-color: oklch(100% 0 0 / 0.18);
  box-shadow:
    inset 0 1px 0 oklch(100% 0 0 / 0.2),
    0 8px 48px oklch(0% 0 0 / 0.4);
}
```

---

## Effect 6 — Double Bezel (Container Depth)

Two nested containers with different border/background create an "inset screen" effect — used by premium hardware sites and SaaS product screenshots.

```css
.bezel-outer {
  padding: 0.375rem;        /* Gap between outer and inner */
  border-radius: 20px;
  background: linear-gradient(
    145deg,
    oklch(100% 0 0 / 0.12),
    oklch(100% 0 0 / 0.04)
  );
  border: 1px solid oklch(100% 0 0 / 0.15);
  box-shadow:
    inset 0 1px 0 oklch(100% 0 0 / 0.2),
    0 20px 80px oklch(0% 0 0 / 0.5);
}

.bezel-inner {
  border-radius: 16px;       /* Slightly smaller radius */
  overflow: hidden;
  background: var(--color-surface);
  border: 1px solid oklch(0% 0 0 / 0.3);
  box-shadow: inset 0 1px 0 oklch(0% 0 0 / 0.1);
}

.bezel-inner img,
.bezel-inner video {
  display: block;
  width: 100%;
  height: auto;
}
```

**Bezel + perspective tilt (hero screenshot effect):**
```css
.hero-screenshot {
  transform: perspective(1200px) rotateY(-6deg) rotateX(3deg) scale(0.98);
  transition: transform 600ms var(--ease-smooth);
}

.hero-screenshot:hover {
  transform: perspective(1200px) rotateY(-2deg) rotateX(1deg) scale(1);
}

@media (prefers-reduced-motion: reduce) {
  .hero-screenshot { transform: none; }
  .hero-screenshot:hover { transform: none; }
}
```

---

## Effect 7 — Background Patterns

Repeating patterns as alternatives to gradients. Zero performance cost.

```css
/* Dot grid */
.bg-dots {
  background-image: radial-gradient(
    circle,
    oklch(100% 0 0 / 0.08) 1px,
    transparent 1px
  );
  background-size: 24px 24px;
}

/* Line grid */
.bg-grid {
  background-image:
    linear-gradient(oklch(100% 0 0 / 0.04) 1px, transparent 1px),
    linear-gradient(90deg, oklch(100% 0 0 / 0.04) 1px, transparent 1px);
  background-size: 40px 40px;
}

/* Diagonal lines */
.bg-diagonal {
  background-image: repeating-linear-gradient(
    45deg,
    oklch(100% 0 0 / 0.03),
    oklch(100% 0 0 / 0.03) 1px,
    transparent 1px,
    transparent 20px
  );
}

/* Fade-out at edges (gradient mask over pattern) */
.bg-dots-fade {
  background-image: radial-gradient(
    circle,
    oklch(100% 0 0 / 0.08) 1px,
    transparent 1px
  );
  background-size: 24px 24px;
  mask-image: radial-gradient(ellipse 80% 80% at center, black 40%, transparent 100%);
}
```

---

## Effect 8 — Shadow Depth System

Professional shadows use multiple layers. Single `box-shadow` looks flat and amateurish.

```css
:root {
  /* Elevation scale — use these, never write box-shadow directly */

  --shadow-xs:
    0 1px 2px oklch(0% 0 0 / 0.06),
    0 0 0 1px oklch(0% 0 0 / 0.04);

  --shadow-sm:
    0 1px 3px oklch(0% 0 0 / 0.08),
    0 2px 8px oklch(0% 0 0 / 0.05),
    0 0 0 1px oklch(0% 0 0 / 0.04);

  --shadow-md:
    0 2px 4px oklch(0% 0 0 / 0.06),
    0 6px 20px oklch(0% 0 0 / 0.08),
    0 12px 40px oklch(0% 0 0 / 0.05),
    0 0 0 1px oklch(0% 0 0 / 0.04);

  --shadow-lg:
    0 4px 6px oklch(0% 0 0 / 0.05),
    0 10px 30px oklch(0% 0 0 / 0.1),
    0 24px 64px oklch(0% 0 0 / 0.08),
    0 0 0 1px oklch(0% 0 0 / 0.04);

  --shadow-xl:
    0 8px 12px oklch(0% 0 0 / 0.05),
    0 20px 50px oklch(0% 0 0 / 0.12),
    0 48px 120px oklch(0% 0 0 / 0.1),
    0 0 0 1px oklch(0% 0 0 / 0.04);

  /* Dark mode: borders replace shadows */
  /* On dark surfaces, shadows are invisible — use borders instead */
}

[data-theme="dark"] {
  --shadow-sm: 0 0 0 1px oklch(100% 0 0 / 0.08);
  --shadow-md: 0 0 0 1px oklch(100% 0 0 / 0.1), 0 8px 32px oklch(0% 0 0 / 0.4);
  --shadow-lg: 0 0 0 1px oklch(100% 0 0 / 0.1), 0 16px 64px oklch(0% 0 0 / 0.6);
  --shadow-xl: 0 0 0 1px oklch(100% 0 0 / 0.12), 0 32px 96px oklch(0% 0 0 / 0.7);
}
```

**Colored shadow (matches element color):**
```css
/* Button casts a colored shadow matching its background */
.btn--primary {
  background: var(--color-accent);
  box-shadow:
    0 4px 20px oklch(from var(--color-accent) l c h / 0.4),
    0 1px 3px oklch(from var(--color-accent) l c h / 0.2);
  transition: box-shadow var(--duration-fast) var(--ease-smooth);
}

.btn--primary:hover {
  box-shadow:
    0 8px 30px oklch(from var(--color-accent) l c h / 0.5),
    0 2px 6px oklch(from var(--color-accent) l c h / 0.3);
}
```

---

## Effect 9 — Aurora / Northern Lights

Full-screen animated color bloom — used by AI products (OpenAI, Perplexity, Claude).

```css
.aurora {
  position: absolute;
  inset: 0;
  overflow: hidden;
  pointer-events: none;
}

.aurora::before,
.aurora::after {
  content: '';
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.4;
  mix-blend-mode: screen;
  animation: aurora-float 12s ease-in-out infinite;
}

.aurora::before {
  width: 60%;
  height: 60%;
  top: -20%;
  left: -10%;
  background: oklch(60% 0.25 280);
  animation-delay: 0s;
}

.aurora::after {
  width: 50%;
  height: 50%;
  bottom: -20%;
  right: -10%;
  background: oklch(65% 0.2 200);
  animation-delay: -6s;
}

@keyframes aurora-float {
  0%, 100% { transform: translate(0, 0) scale(1); }
  33% { transform: translate(5%, 3%) scale(1.05); }
  66% { transform: translate(-3%, -5%) scale(0.95); }
}

@media (prefers-reduced-motion: reduce) {
  .aurora::before,
  .aurora::after { animation: none; }
}
```

**Third blob:**
```html
<div class="aurora">
  <div class="aurora__blob aurora__blob--3"></div>
</div>
```
```css
.aurora__blob--3 {
  position: absolute;
  width: 40%;
  height: 40%;
  top: 40%;
  left: 40%;
  background: oklch(55% 0.2 320);
  filter: blur(80px);
  opacity: 0.3;
  border-radius: 50%;
  mix-blend-mode: screen;
  animation: aurora-float 15s ease-in-out infinite;
  animation-delay: -3s;
}
```

---

## Combining Effects

**The dark SaaS hero stack (used by Raycast, Linear, Vercel):**

```html
<section class="hero">
  <!-- Layer 1: Base surface with mesh gradient -->
  <!-- Layer 2: Aurora blobs (optional, for extra depth) -->
  <!-- Layer 3: Background dot pattern -->
  <!-- Layer 4: Spotlight (mouse-tracked) -->
  <!-- Layer 5: Content -->
  <!-- Layer 6: Grain texture (body::after, fixed) -->
</section>
```

```css
.hero {
  position: relative;
  background:
    /* Mesh gradient layers */
    radial-gradient(ellipse 50% 60% at 20% 70%, oklch(55% 0.22 280 / 0.3) 0%, transparent 65%),
    radial-gradient(ellipse 40% 50% at 80% 20%, oklch(65% 0.18 200 / 0.2) 0%, transparent 55%),
    /* Dot pattern */
    radial-gradient(circle, oklch(100% 0 0 / 0.06) 1px, transparent 1px),
    /* Base color */
    oklch(8% 0.01 260);
  background-size: auto, auto, 24px 24px, auto;
}

/* Spotlight layer */
.hero::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(
    800px at var(--cursor-x, 50%) var(--cursor-y, 50%),
    oklch(55% 0.15 258 / 0.1),
    transparent 50%
  );
  pointer-events: none;
}
```

---

*Pattern version: global-design-skill v1.0 — `patterns/effects/visual-effects.md`*  
*Updated: 2026-05-20*  
*Related: `patterns/effects/parallax-system.md`, `patterns/effects/hover-effects.md`, `tokens/tokens.css`*
