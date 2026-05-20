# Reference — Visual Effects Catalog

> Production-ready visual effect techniques. Each effect includes when to use it, when to avoid it, and exact implementation. Effects are organized by category: background, surface, text, interaction, and ambient.

---

## Index

| Category | Effect | Archetypes |
|---|---|---|
| Background | Aurora / Gradient Mesh | A, E |
| Background | Dot Grid | A, G |
| Background | Animated Noise Grain | A, B, E |
| Background | Conic Gradient Sweep | All |
| Surface | Glassmorphism (correct) | E |
| Surface | Bezel Frame | A, B, E, H |
| Surface | Gradient Border (animated) | A, E |
| Surface | Inner Highlight (specular) | E, H |
| Text | Hue-Shift Headline | A, F |
| Text | Clip-Path Reveal | B, E |
| Text | Text Scramble | G |
| Interaction | Spotlight / Cursor Glow | A, E |
| Interaction | 3D Card Tilt | E, H |
| Interaction | Magnetic Button | F |
| Ambient | Floating Blobs | D |
| Ambient | CRT Scanlines | G |
| Ambient | Shimmer Sweep | A, E |

---

## Background Effects

### Aurora / Gradient Mesh

**When to use:** Dark hero backgrounds, section accents in Ethereal Black (A) and Volumetric Glass (E) archetypes.

**When NOT to use:** Light-mode pages (use 3–5% opacity max), sections with dense text content (competes with readability).

**Banned version:** Purple → indigo gradient on white. This is listed in `checklists/global-design-review.md` as an automatic fail.

```css
/* Multi-source radial aurora — different hues, all low opacity */
.aurora-bg {
  background:
    radial-gradient(
      ellipse 80% 50% at 20% -10%,
      oklch(65% 0.22 258 / 0.15),
      transparent 60%
    ),
    radial-gradient(
      ellipse 60% 70% at 80% 110%,
      oklch(65% 0.18 295 / 0.12),
      transparent 60%
    ),
    radial-gradient(
      ellipse 40% 40% at 60% 30%,
      oklch(75% 0.15 200 / 0.06),
      transparent 60%
    ),
    var(--color-base);
}

/* Animated aurora — slow hue rotation via @property */
@property --aurora-hue-1 { syntax: "<number>"; inherits: false; initial-value: 258; }
@property --aurora-hue-2 { syntax: "<number>"; inherits: false; initial-value: 295; }

.aurora-animated {
  background:
    radial-gradient(
      ellipse 80% 50% at 20% 0%,
      oklch(65% 0.20 var(--aurora-hue-1) / 0.12), transparent 60%
    ),
    radial-gradient(
      ellipse 60% 60% at 80% 100%,
      oklch(65% 0.18 var(--aurora-hue-2) / 0.10), transparent 60%
    ),
    var(--color-base);
  animation: aurora-shift 20s linear infinite;
}

@keyframes aurora-shift {
  0%   { --aurora-hue-1: 258; --aurora-hue-2: 295; }
  50%  { --aurora-hue-1: 220; --aurora-hue-2: 330; }
  100% { --aurora-hue-1: 258; --aurora-hue-2: 295; }
}

@media (prefers-reduced-motion: reduce) {
  .aurora-animated { animation: none; }
}
```

**Key constraints:**
- Total opacity of all gradient layers combined ≤ 20% on dark, ≤ 6% on light
- Hue spread between gradients: ±30–60° for harmony, not ±120° (too jarring)
- Always set `var(--color-base)` as the terminal color, not `#000` or `#fff`

---

### Dot Grid Background

**When to use:** Behind hero sections, feature sections, and dashboard panels in Ethereal Black (A) and Post-Digital Terminal (G) archetypes.

```css
/* Radial-gradient dot grid */
.dot-grid {
  background-image: radial-gradient(
    circle,
    oklch(from var(--color-accent) l c h / 0.25) 1px,
    transparent 1px
  );
  background-size: 24px 24px;
  background-position: 0 0;
}

/* Faded edges — dot grid that disappears toward borders */
.dot-grid-faded {
  background-image: radial-gradient(
    circle,
    oklch(from var(--color-accent) l c h / 0.25) 1px,
    transparent 1px
  );
  background-size: 24px 24px;
  -webkit-mask-image: radial-gradient(
    ellipse 80% 80% at 50% 50%,
    black 40%,
    transparent 100%
  );
  mask-image: radial-gradient(
    ellipse 80% 80% at 50% 50%,
    black 40%,
    transparent 100%
  );
}

/* Line grid (for dashboards) */
.line-grid {
  background-image:
    linear-gradient(oklch(from var(--color-border) l c h / 0.6) 1px, transparent 1px),
    linear-gradient(90deg, oklch(from var(--color-border) l c h / 0.6) 1px, transparent 1px);
  background-size: 40px 40px;
}
```

---

### Noise Grain Texture

**When to use:** Any surface that feels "flat matte" — especially dark-mode hero sections and premium card surfaces. The fastest single signal for "premium" in modern web design.

**Implementation note:** Animated grain (step-based) adds life; static grain adds texture without distraction. Choose based on section importance.

```css
/* Static grain — for general surface texture */
.grain {
  position: relative;
}

.grain::after {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 10;
  opacity: 0.04;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E");
  background-size: 200px;
  border-radius: inherit;
}

/* Animated grain — for hero sections, adds kinetic life */
.grain-animated::after {
  animation: grain-flicker 0.5s steps(2) infinite;
}

@keyframes grain-flicker {
  0%   { transform: translate(0, 0); }
  25%  { transform: translate(-1%, -1%); }
  50%  { transform: translate(1.5%, 0.5%); }
  75%  { transform: translate(-0.5%, 1%); }
  100% { transform: translate(1%, -1%); }
}

@media (prefers-reduced-motion: reduce) {
  .grain-animated::after { animation: none; }
}
```

**Opacity guide:**

| Surface | Opacity | Blend mode |
|---|---|---|
| Dark hero (near-black) | 0.04–0.06 | `overlay` |
| Dark card surface | 0.03–0.04 | `overlay` |
| Light surface (cream) | 0.03–0.04 | `multiply` |
| Image overlay | 0.05–0.08 | `overlay` |

---

### Conic Gradient Sweep

**When to use:** Accent decorations, loading indicators, circular progress. NOT as a primary background.

```css
/* Conic gradient as section accent */
.conic-accent {
  background: conic-gradient(
    from 0deg at 50% 50%,
    oklch(65% 0.22 258),
    oklch(65% 0.18 295),
    oklch(65% 0.22 258)
  );
  border-radius: 50%;
  filter: blur(60px);
  opacity: 0.15;
}

/* Animated — spinning accent blob */
.conic-spinning {
  animation: conic-rotate 8s linear infinite;
}

@keyframes conic-rotate {
  to { transform: rotate(360deg); }
}

@media (prefers-reduced-motion: reduce) {
  .conic-spinning { animation: none; }
}
```

---

## Surface Effects

### Glassmorphism (correct implementation)

**When to use:** ONLY in Volumetric Glass archetype (E). Only when there is a visible background layer behind the glass — glassmorphism on a flat background is meaningless.

**Required conditions:**
1. Layered background visible through the glass
2. `backdrop-filter` support (Chrome 76+, Firefox 103+, Safari 9+)
3. Specular highlight on top edge (inner shadow)
4. Border at 10–15% opacity

**Banned use:** As "polish" added to any UI that isn't actually layered. Glassmorphism as decoration on a flat background is the most common misuse.

```css
.glass-card {
  background: oklch(from var(--color-surface) l c h / 0.08);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid oklch(100% 0 0 / 0.12);
  border-radius: var(--radius-xl);
  box-shadow:
    0 8px 32px oklch(0% 0 0 / 0.20),
    inset 0 1px 0 oklch(100% 0 0 / 0.18),   /* specular top edge */
    inset 0 -1px 0 oklch(0% 0 0 / 0.08);    /* shadow bottom edge */
}

/* Dark mode glass (more opacity needed for legibility) */
.dark .glass-card {
  background: oklch(from var(--color-surface) l c h / 0.12);
  border-color: oklch(100% 0 0 / 0.08);
}

/* Fallback for browsers without backdrop-filter */
@supports not (backdrop-filter: blur(1px)) {
  .glass-card {
    background: oklch(from var(--color-surface) l c h / 0.85);
  }
}
```

**Performance note:** `backdrop-filter` forces GPU compositing. Limit to 3–5 visible glass elements per viewport. More causes frame drops on mobile.

---

### Bezel Frame

**When to use:** Product screenshots, dashboard previews, app mockups. Creates depth that makes product visuals feel premium.

```css
.bezel {
  padding: 0.375rem;
  background: oklch(from var(--color-accent) l c h / 0.06);
  border: 1px solid oklch(from var(--color-accent) l c h / 0.18);
  border-radius: var(--radius-2xl);
  box-shadow:
    0 24px 64px oklch(0% 0 0 / 0.20),
    0 4px 16px oklch(0% 0 0 / 0.12);
}

.bezel-inner {
  border-radius: calc(var(--radius-2xl) - 0.375rem);
  overflow: hidden;
  background: var(--color-surface);
  box-shadow:
    inset 0 1px 0 oklch(100% 0 0 / 0.12),
    inset 0 -1px 0 oklch(0% 0 0 / 0.06);
}

/* Perspective transform for hero product visuals */
.bezel-perspective {
  transform: perspective(1200px) rotateY(-8deg) rotateX(2deg);
  transition: transform 600ms cubic-bezier(0.16, 1, 0.3, 1);
}

.bezel-perspective:hover {
  transform: perspective(1200px) rotateY(-4deg) rotateX(1deg) scale(1.01);
}
```

---

### Animated Gradient Border

**When to use:** Primary CTA cards, featured pricing tier, highlighted feature. One instance per page — overuse destroys the effect.

```css
@property --border-angle {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.gradient-border {
  position: relative;
  border-radius: var(--radius-xl);
  padding: 1px; /* border thickness */
  background: conic-gradient(
    from var(--border-angle),
    oklch(65% 0.22 258),
    oklch(65% 0.18 310),
    oklch(75% 0.15 200),
    oklch(65% 0.22 258)
  );
  animation: border-spin 4s linear infinite;
}

.gradient-border-inner {
  background: var(--color-surface);
  border-radius: calc(var(--radius-xl) - 1px);
  padding: var(--space-6);
}

@keyframes border-spin {
  to { --border-angle: 360deg; }
}

@media (prefers-reduced-motion: reduce) {
  .gradient-border {
    animation: none;
    background: linear-gradient(
      135deg,
      oklch(65% 0.22 258),
      oklch(65% 0.18 310)
    );
  }
}
```

---

### Inner Highlight (Specular)

**When to use:** Any surface that should feel physically raised — buttons, cards, bezel frames, glass panels. The specular highlight simulates light catching the top edge.

```css
/* Button specular */
.btn-primary {
  box-shadow:
    0 1px 0 oklch(100% 0 0 / 0.15) inset,   /* top specular */
    0 -1px 0 oklch(0% 0 0 / 0.10) inset,    /* bottom shadow */
    var(--shadow-accent);                    /* outer glow */
}

/* Card inner highlight */
.card-raised {
  box-shadow:
    inset 0 1px 0 oklch(100% 0 0 / 0.10),
    var(--shadow-md);
}

/* Glass specular (stronger) */
.glass-surface {
  box-shadow:
    inset 0 1px 0 oklch(100% 0 0 / 0.20),
    inset 0 -1px 0 oklch(0% 0 0 / 0.08),
    var(--shadow-lg);
}
```

---

## Text Effects

### Hue-Shift Headline

**When to use:** Hero display headlines in Ethereal Black (A) or Neo-Maximalism (F) archetypes. Alternative to banned gradient text (`background-clip: text`).

**Why this instead of gradient text:** Gradient text breaks on dark backgrounds, has poor accessibility, and is listed as a banned pattern. Hue-shift uses `color` which is accessible, readable, and animatable.

```css
@property --headline-hue {
  syntax: "<number>";
  inherits: false;
  initial-value: 258;
}

.hue-headline {
  color: oklch(72% 0.20 var(--headline-hue));
  animation: hue-drift 12s linear infinite;
}

@keyframes hue-drift {
  0%   { --headline-hue: 258; }
  33%  { --headline-hue: 210; }
  66%  { --headline-hue: 290; }
  100% { --headline-hue: 258; }
}

/* Accent word only — rest stays neutral */
.headline-accent-word {
  color: var(--color-accent);
}

@media (prefers-reduced-motion: reduce) {
  .hue-headline {
    animation: none;
    color: var(--color-accent);
  }
}
```

---

### Clip-Path Text Reveal

**When to use:** Cinematic entrances for hero headlines in Editorial Luxury (B) and Volumetric Glass (E) archetypes.

```css
/* Wrapper clips the reveal area */
.reveal-line {
  overflow: hidden;
  display: block;
}

.reveal-line-inner {
  display: block;
  transform: translateY(110%);
  animation: line-reveal 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
}

.reveal-line:nth-child(1) .reveal-line-inner { animation-delay: 0ms; }
.reveal-line:nth-child(2) .reveal-line-inner { animation-delay: 80ms; }
.reveal-line:nth-child(3) .reveal-line-inner { animation-delay: 160ms; }

@keyframes line-reveal {
  to { transform: translateY(0); }
}

@media (prefers-reduced-motion: reduce) {
  .reveal-line-inner {
    animation: fade-in 200ms both;
    transform: none;
  }
  @keyframes fade-in { from { opacity: 0; } to { opacity: 1; } }
}
```

**HTML structure:**
```html
<h1 aria-label="Ship faster without the chaos">
  <span class="reveal-line">
    <span class="reveal-line-inner">Ship faster</span>
  </span>
  <span class="reveal-line">
    <span class="reveal-line-inner">without the chaos</span>
  </span>
</h1>
```

---

### Text Scramble

**When to use:** Post-Digital Terminal archetype (G), command palette headings, data readouts. Creates a character-decoding effect.

```ts
class TextScramble {
  private readonly chars = '!<>-_\\/[]{}—=+*^?#@$%'
  private frame = 0
  private rafId: number | null = null

  constructor(private el: HTMLElement) {}

  setText(newText: string): Promise<void> {
    const length = Math.max(this.el.innerText.length, newText.length)

    interface QueueItem {
      from: string
      to: string
      start: number
      end: number
      char: string
    }

    const queue: QueueItem[] = Array.from({ length }, (_, i) => ({
      from: this.el.innerText[i] ?? '',
      to: newText[i] ?? '',
      start: Math.floor(Math.random() * 10),
      end: Math.floor(Math.random() * 20) + 10,
      char: '',
    }))

    this.frame = 0
    if (this.rafId) cancelAnimationFrame(this.rafId)

    return new Promise(resolve => {
      const update = () => {
        let output = ''
        let complete = 0

        for (const item of queue) {
          if (this.frame >= item.end) {
            complete++
            output += item.to
          } else if (this.frame >= item.start) {
            item.char = this.chars[Math.floor(Math.random() * this.chars.length)]
            output += `<span aria-hidden="true" style="opacity:0.4">${item.char}</span>`
          } else {
            output += item.from
          }
        }

        this.el.innerHTML = output

        if (complete < queue.length) {
          this.frame++
          this.rafId = requestAnimationFrame(update)
        } else {
          resolve()
        }
      }

      update()
    })
  }

  destroy() {
    if (this.rafId) cancelAnimationFrame(this.rafId)
  }
}

// Usage
const heading = document.querySelector('[data-scramble]') as HTMLElement
const fx = new TextScramble(heading)
const phrases = ['Initialize', 'Load config', 'Ready']
let i = 0
const cycle = async () => {
  await fx.setText(phrases[i % phrases.length])
  await new Promise(r => setTimeout(r, 2000))
  i++
  cycle()
}
cycle()
```

---

## Interaction Effects

### Spotlight / Cursor Glow

**When to use:** Cards, feature panels, and hero sections in Ethereal Black (A) and Volumetric Glass (E) archetypes. Creates a sense of "the card watches the cursor."

```css
.spotlight-card {
  background:
    radial-gradient(
      circle 300px at var(--spotlight-x, -100%) var(--spotlight-y, -100%),
      oklch(from var(--color-accent) l c h / 0.08),
      transparent 60%
    ),
    var(--color-surface);
  transition: background 0.05s;
}

/* Border glow follows cursor */
.spotlight-card-border {
  position: relative;
  border-radius: var(--radius-xl);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
}

.spotlight-card-border::before {
  content: '';
  position: absolute;
  inset: -1px;
  border-radius: inherit;
  background: radial-gradient(
    circle 200px at var(--spotlight-x, -100%) var(--spotlight-y, -100%),
    oklch(from var(--color-accent) l c h / 0.5),
    transparent 70%
  );
  z-index: -1;
  opacity: 0;
  transition: opacity 300ms;
}

.spotlight-card-border:hover::before {
  opacity: 1;
}
```

```ts
// Applies to all .spotlight-card elements — single event listener on parent
function initSpotlight(container: HTMLElement) {
  container.addEventListener('mousemove', (e: MouseEvent) => {
    const cards = container.querySelectorAll<HTMLElement>('.spotlight-card, .spotlight-card-border')
    cards.forEach(card => {
      const rect = card.getBoundingClientRect()
      card.style.setProperty('--spotlight-x', `${e.clientX - rect.left}px`)
      card.style.setProperty('--spotlight-y', `${e.clientY - rect.top}px`)
    })
  })
}

initSpotlight(document.body)
```

---

### 3D Card Tilt

**When to use:** Product screenshots, pricing cards, and feature hero images in Volumetric Glass (E) and Spatial Luxury (H) archetypes.

**Constraint:** Maximum rotation ±8° on Y axis, ±6° on X axis. More feels broken, not premium.

```ts
function initTiltCards(selector = '.tilt-card') {
  const cards = document.querySelectorAll<HTMLElement>(selector)
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches

  if (reduced) return

  cards.forEach(card => {
    let rafId: number

    card.addEventListener('mousemove', (e: MouseEvent) => {
      cancelAnimationFrame(rafId)
      rafId = requestAnimationFrame(() => {
        const rect = card.getBoundingClientRect()
        const cx = rect.left + rect.width / 2
        const cy = rect.top + rect.height / 2
        const dx = (e.clientX - cx) / (rect.width / 2)   // -1 to 1
        const dy = (e.clientY - cy) / (rect.height / 2)  // -1 to 1
        card.style.transform =
          `perspective(900px) rotateY(${dx * 7}deg) rotateX(${-dy * 5}deg) scale(1.02)`
      })
    })

    card.addEventListener('mouseleave', () => {
      cancelAnimationFrame(rafId)
      card.style.transform = ''
    })
  })
}
```

```css
.tilt-card {
  transition: transform 500ms cubic-bezier(0.16, 1, 0.3, 1);
  transform-style: preserve-3d;
  will-change: transform;
}
```

---

### Magnetic Button

**When to use:** Primary CTA buttons in Neo-Maximalism (F) and Cyberbrutalism (C) archetypes. The button is attracted toward the cursor.

```ts
function initMagneticButtons(selector = '.btn-magnetic') {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  if (reduced) return

  document.querySelectorAll<HTMLElement>(selector).forEach(btn => {
    btn.addEventListener('mousemove', (e: MouseEvent) => {
      const rect = btn.getBoundingClientRect()
      const dx = e.clientX - (rect.left + rect.width / 2)
      const dy = e.clientY - (rect.top + rect.height / 2)
      btn.style.transform = `translate(${dx * 0.3}px, ${dy * 0.3}px)`
    })

    btn.addEventListener('mouseleave', () => {
      btn.style.transform = ''
    })
  })
}
```

```css
.btn-magnetic {
  transition: transform 400ms cubic-bezier(0.16, 1, 0.3, 1);
}
```

---

## Ambient Effects

### Floating Blobs

**When to use:** Organic Softness archetype (D) — health, wellness, consumer apps. Soft morphing shapes create an "alive" background.

**Constraint:** Max 2 blobs per section. Slow animation (6–12s). Never on dark backgrounds.

```css
.blob-container {
  position: absolute;
  inset: 0;
  overflow: hidden;
  pointer-events: none;
  z-index: 0;
}

.blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  animation: blob-float 10s ease-in-out infinite;
}

.blob-1 {
  width: 400px;
  height: 400px;
  background: oklch(80% 0.12 155 / 0.25); /* soft sage */
  top: -10%;
  left: -5%;
  animation-delay: 0s;
}

.blob-2 {
  width: 300px;
  height: 300px;
  background: oklch(85% 0.10 80 / 0.20); /* warm amber */
  bottom: -5%;
  right: -8%;
  animation-delay: -4s;
}

@keyframes blob-float {
  0%, 100% { transform: translate(0, 0) scale(1); }
  33%       { transform: translate(20px, -15px) scale(1.05); }
  66%       { transform: translate(-10px, 20px) scale(0.95); }
}

@media (prefers-reduced-motion: reduce) {
  .blob { animation: none; }
}
```

---

### CRT Scanlines

**When to use:** Post-Digital Terminal archetype (G) only. Creates vintage monitor aesthetic.

```css
.crt-overlay {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 9998;
  background: repeating-linear-gradient(
    0deg,
    oklch(0% 0 0 / 0.03) 0px,
    oklch(0% 0 0 / 0.03) 1px,
    transparent 1px,
    transparent 4px
  );
}

/* Vignette edge darkening */
.crt-vignette {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 9997;
  background: radial-gradient(
    ellipse 80% 80% at 50% 50%,
    transparent 50%,
    oklch(0% 0 0 / 0.4) 100%
  );
}

/* Phosphor flicker — very subtle */
@keyframes phosphor-flicker {
  0%, 100% { opacity: 1; }
  92%       { opacity: 0.97; }
  94%       { opacity: 1; }
}

.crt-screen {
  animation: phosphor-flicker 8s linear infinite;
}

@media (prefers-reduced-motion: reduce) {
  .crt-screen { animation: none; }
}
```

---

### Shimmer Sweep

**When to use:** Loading states (skeleton screens), and as a subtle ambient effect on premium card surfaces.

**Rule:** One shimmer sweep across the entire skeleton container — not individual pulses on each element. See `rules/05-animation.md` R8.

```css
@keyframes shimmer {
  from { background-position: 200% 0; }
  to   { background-position: -200% 0; }
}

/* Skeleton loading */
.skeleton-container {
  position: relative;
  overflow: hidden;
}

.skeleton-container::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    transparent 0%,
    oklch(from var(--color-surface) calc(l + 0.05) c h / 0.08) 50%,
    transparent 100%
  );
  background-size: 200% 100%;
  animation: shimmer 1.8s linear infinite;
  pointer-events: none;
}

/* Premium card ambient shimmer — very subtle, on hover only */
.card-shimmer:hover::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(
    105deg,
    transparent 40%,
    oklch(100% 0 0 / 0.04) 50%,
    transparent 60%
  );
  background-size: 200% 100%;
  animation: shimmer 1.2s linear;
  pointer-events: none;
}

@media (prefers-reduced-motion: reduce) {
  .skeleton-container::after,
  .card-shimmer:hover::after {
    animation: none;
  }
}
```

---

## Effect Decision Matrix

| Effect | Dark mode | Light mode | Mobile safe | Performance | Archetype |
|---|---|---|---|---|---|
| Aurora gradient mesh | ✅ | ⚠️ (≤5% opacity) | ✅ | ✅ | A, E |
| Dot grid | ✅ | ✅ | ✅ | ✅ | A, G |
| Noise grain | ✅ | ✅ | ✅ | ✅ | All |
| Glassmorphism | ✅ | ⚠️ (needs layers) | ⚠️ (3 max) | ⚠️ (GPU) | E |
| Gradient border | ✅ | ✅ | ✅ | ✅ | A, E |
| Spotlight cursor | ✅ | ✅ | ❌ (hover only) | ✅ | A, E |
| 3D card tilt | ✅ | ✅ | ❌ (hover only) | ✅ | E, H |
| Magnetic button | ✅ | ✅ | ❌ (hover only) | ✅ | C, F |
| Floating blobs | ❌ | ✅ | ✅ | ✅ | D |
| CRT scanlines | ✅ | ❌ | ✅ | ✅ | G |
| Text scramble | ✅ | ⚠️ | ✅ | ✅ | G |
| Bezel frame | ✅ | ✅ | ✅ | ✅ | A, E, H |

---

## Combining Effects

**Allowed combinations:**
- Noise grain + Aurora mesh (complementary — texture over gradient)
- Bezel frame + 3D card tilt (both serve depth in archetype E)
- Dot grid + Spotlight cursor (cursor reveals the grid)
- Glassmorphism + Specular inner highlight (both serve depth)

**Banned combinations:**
- Multiple animated effects simultaneously per section (competing motion)
- Glassmorphism + Aurora gradient mesh (both rely on blur — compete, look muddy)
- CRT scanlines on any non-terminal archetype
- Magnetic buttons + 3D tilt on the same element (conflicting transforms)

---

*Reference version: global-design-skill v1.0 — `references/visual-effects.md`*
*Related: `rules/05-animation.md`, `references/3d-animations.md`, `references/aesthetic-archetypes.md`, `skills/hyperdesign/SKILL.md`*
