# Pattern — Text Animations

> Kinetic typography techniques with copy-paste code. Text is the primary content of most web pages — animating it well is the fastest path to premium feel. All patterns include `prefers-reduced-motion` fallback.

---

## Effect 1 — Split Text Reveal (Character / Word / Line)

The most common premium animation pattern. Text is split into units that reveal with stagger.

**CSS-only word reveal (Baseline 2024):**
```html
<h1 class="split-reveal">
  <span class="word">Deploy</span>
  <span class="word">in</span>
  <span class="word">23</span>
  <span class="word">seconds</span>
</h1>
```

```css
@keyframes word-reveal {
  from {
    opacity: 0;
    transform: translateY(60%) rotate(3deg);
    filter: blur(4px);
  }
  to {
    opacity: 1;
    transform: translateY(0) rotate(0deg);
    filter: blur(0);
  }
}

.split-reveal {
  overflow: hidden;
}

.split-reveal .word {
  display: inline-block;
  animation: word-reveal 600ms var(--ease-spring) both;
  animation-timeline: view();
  animation-range: entry 0% entry 40%;
}

/* Stagger via :nth-child */
.split-reveal .word:nth-child(1) { animation-delay: 0ms; }
.split-reveal .word:nth-child(2) { animation-delay: 60ms; }
.split-reveal .word:nth-child(3) { animation-delay: 120ms; }
.split-reveal .word:nth-child(4) { animation-delay: 180ms; }
.split-reveal .word:nth-child(5) { animation-delay: 240ms; }
.split-reveal .word:nth-child(6) { animation-delay: 300ms; }

@media (prefers-reduced-motion: reduce) {
  .split-reveal .word {
    animation: none;
    opacity: 1;
    transform: none;
    filter: none;
  }
}
```

**GSAP SplitText (handles arbitrary text automatically):**
```javascript
import gsap from 'gsap';
import { SplitText } from 'gsap/SplitText';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(SplitText, ScrollTrigger);

const mm = gsap.matchMedia();

mm.add('(prefers-reduced-motion: no-preference)', () => {

  document.querySelectorAll('.gsap-split-reveal').forEach(el => {
    const split = new SplitText(el, { type: 'words,chars' });

    gsap.from(split.chars, {
      opacity: 0,
      y: '100%',
      rotationZ: 5,
      stagger: 0.02,
      duration: 0.6,
      ease: 'power2.out',
      scrollTrigger: {
        trigger: el,
        start: 'top 85%',
        toggleActions: 'play none none reverse'
      }
    });
  });

});
```

---

## Effect 2 — Blur-In Reveal

Text appears from a blurred state — feels like coming into focus. Used by Arc Browser, Framer.

```css
@keyframes blur-in {
  from {
    opacity: 0;
    filter: blur(12px);
    transform: translateY(8px);
  }
  to {
    opacity: 1;
    filter: blur(0);
    transform: translateY(0);
  }
}

.blur-in {
  animation: blur-in 800ms var(--ease-smooth) both;
}

/* Stagger for multiple elements */
.blur-in:nth-child(1) { animation-delay: 0ms; }
.blur-in:nth-child(2) { animation-delay: 150ms; }
.blur-in:nth-child(3) { animation-delay: 300ms; }
.blur-in:nth-child(4) { animation-delay: 450ms; }

/* Scroll-triggered variant */
.blur-in-scroll {
  animation: blur-in 800ms var(--ease-smooth) both;
  animation-timeline: view();
  animation-range: entry 0% entry 35%;
}

@media (prefers-reduced-motion: reduce) {
  .blur-in,
  .blur-in-scroll { animation: none; opacity: 1; filter: none; transform: none; }
}
```

**Hero entrance sequence (eyebrow → H1 → subtitle → CTA):**
```css
.hero-eyebrow  { animation: blur-in 600ms var(--ease-smooth) 0ms   both; }
.hero-heading  { animation: blur-in 800ms var(--ease-spring)  150ms both; }
.hero-subtitle { animation: blur-in 600ms var(--ease-smooth)  400ms both; }
.hero-cta      { animation: blur-in 500ms var(--ease-smooth)  600ms both; }
.hero-trust    { animation: blur-in 400ms var(--ease-smooth)  800ms both; }

@media (prefers-reduced-motion: reduce) {
  .hero-eyebrow, .hero-heading, .hero-subtitle, .hero-cta, .hero-trust {
    animation: none;
    opacity: 1;
  }
}
```

---

## Effect 3 — Character Scramble (Hover)

Characters cycle through random characters before revealing the correct letter. Used on hover for developer tools.

```javascript
class TextScramble {
  constructor(el) {
    this.el = el;
    this.chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*';
    this.originalText = el.textContent;
    this.frameRequest = null;

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    el.addEventListener('mouseenter', () => this.scramble());
    el.addEventListener('mouseleave', () => this.restore());
  }

  scramble() {
    cancelAnimationFrame(this.frameRequest);
    const text = this.originalText;
    let frame = 0;
    const totalFrames = text.length * 3;

    const update = () => {
      let output = '';
      for (let i = 0; i < text.length; i++) {
        if (text[i] === ' ') {
          output += ' ';
        } else if (i < Math.floor(frame / 3)) {
          output += text[i]; // Reveal correct char
        } else {
          output += this.chars[Math.floor(Math.random() * this.chars.length)];
        }
      }
      this.el.textContent = output;
      frame++;

      if (frame <= totalFrames) {
        this.frameRequest = requestAnimationFrame(update);
      }
    };

    update();
  }

  restore() {
    cancelAnimationFrame(this.frameRequest);
    let frame = 0;
    const text = this.originalText;
    const totalFrames = text.length * 2;

    const update = () => {
      let output = '';
      for (let i = 0; i < text.length; i++) {
        if (text[i] === ' ') {
          output += ' ';
        } else if (i < text.length - Math.floor(frame / 2)) {
          output += this.chars[Math.floor(Math.random() * this.chars.length)];
        } else {
          output += text[i];
        }
      }
      this.el.textContent = output;
      frame++;

      if (frame <= totalFrames) {
        this.frameRequest = requestAnimationFrame(update);
      } else {
        this.el.textContent = this.originalText;
      }
    };

    update();
  }
}

document.querySelectorAll('[data-scramble]').forEach(el => new TextScramble(el));
```

```html
<h2 data-scramble>Deploy in 23 seconds</h2>
<a href="#" class="nav-link" data-scramble>Documentation</a>
```

---

## Effect 4 — Typewriter Effect

Text types out character by character. Best for code examples, terminal aesthetics, or loading sequences.

```javascript
class Typewriter {
  constructor(el, options = {}) {
    this.el = el;
    this.text = el.dataset.typewriter || el.textContent;
    this.speed = options.speed || 35;        // ms per character
    this.delay = options.delay || 0;          // ms before starting
    this.cursor = options.cursor !== false;

    el.textContent = '';

    if (this.cursor) {
      this.cursorEl = document.createElement('span');
      this.cursorEl.className = 'typewriter-cursor';
      this.cursorEl.setAttribute('aria-hidden', 'true');
      el.appendChild(this.cursorEl);
    }

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      // Immediately show full text
      el.textContent = this.text;
      return;
    }

    setTimeout(() => this.type(), this.delay);
  }

  type() {
    const text = this.text;
    let i = 0;

    const tick = () => {
      if (i < text.length) {
        const textNode = document.createTextNode(text[i]);
        if (this.cursorEl) {
          this.el.insertBefore(textNode, this.cursorEl);
        } else {
          this.el.appendChild(textNode);
        }
        i++;
        setTimeout(tick, this.speed + Math.random() * 20); // Slight randomness = human feel
      } else if (this.cursorEl) {
        // Blink cursor after done
        this.cursorEl.classList.add('done');
      }
    };

    tick();
  }
}
```

```css
.typewriter-cursor {
  display: inline-block;
  width: 2px;
  height: 1em;
  background: currentColor;
  margin-left: 2px;
  vertical-align: text-top;
  animation: cursor-blink 1s step-end infinite;
}

.typewriter-cursor.done {
  animation-duration: 0.8s;
}

@keyframes cursor-blink {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0; }
}
```

```html
<p data-typewriter="const deploy = () => ship({ fast: true, global: true });" class="code-demo"></p>
<script>
  new Typewriter(document.querySelector('.code-demo'), { speed: 30, delay: 500 });
</script>
```

---

## Effect 5 — Variable Font Weight Animation on Scroll

Animate `font-weight` from thin to bold as a heading enters the viewport. Creates a "materializing" effect.

```css
/* Requires a variable font with weight axis */
/* Good options: Fraunces, Outfit, Syne, Inter (has wght axis) */

@keyframes weight-in {
  from {
    font-variation-settings: 'wght' 200;
    opacity: 0.4;
    letter-spacing: 0.1em;
  }
  to {
    font-variation-settings: 'wght' 700;
    opacity: 1;
    letter-spacing: -0.02em;
  }
}

.weight-reveal {
  font-family: 'Fraunces', serif;
  animation: weight-in 1000ms var(--ease-smooth) both;
  animation-timeline: view();
  animation-range: entry 0% entry 50%;
}

/* Register for smooth interpolation */
@property --font-wght {
  syntax: '<number>';
  inherits: false;
  initial-value: 200;
}

@media (prefers-reduced-motion: reduce) {
  .weight-reveal {
    animation: none;
    font-variation-settings: 'wght' 700;
    opacity: 1;
    letter-spacing: -0.02em;
  }
}
```

**Scroll-linked weight (weight follows scroll position in real time):**
```javascript
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const heading = document.querySelector('.dynamic-weight-heading');

  const observer = new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) {
      window.addEventListener('scroll', updateWeight, { passive: true });
    } else {
      window.removeEventListener('scroll', updateWeight);
    }
  });
  observer.observe(heading);

  function updateWeight() {
    const rect = heading.getBoundingClientRect();
    const progress = 1 - (rect.top / window.innerHeight);
    const weight = Math.round(200 + (progress * 500)); // 200 → 700
    heading.style.fontVariationSettings = `'wght' ${Math.min(700, Math.max(200, weight))}`;
  }
}
```

---

## Effect 6 — Gradient Text Reveal (Clip-Path)

Text reveals with a moving gradient clip — creates a "light sweeping across" feel. Different from banned static gradient text (this is animated).

```css
@keyframes text-sweep {
  from {
    background-position: -200% center;
  }
  to {
    background-position: 200% center;
  }
}

.text-sweep {
  background: linear-gradient(
    90deg,
    var(--color-text-primary) 0%,
    var(--color-text-primary) 35%,
    var(--color-accent) 50%,
    var(--color-text-primary) 65%,
    var(--color-text-primary) 100%
  );
  background-size: 200% auto;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: text-sweep 3s linear infinite;
}

@media (prefers-reduced-motion: reduce) {
  .text-sweep {
    background: none;
    color: var(--color-text-primary);
    animation: none;
  }
}
```

**One-time reveal (not looping — used on page load):**
```css
@keyframes text-reveal-once {
  from {
    background-position: 100% center;
    opacity: 0.3;
  }
  to {
    background-position: 0% center;
    opacity: 1;
  }
}

.text-reveal-once {
  background: linear-gradient(
    90deg,
    var(--color-text-primary) 50%,
    oklch(75% 0.08 258) 75%,
    var(--color-text-primary) 100%
  );
  background-size: 200% auto;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: text-reveal-once 1200ms var(--ease-smooth) 300ms both;
}
```

---

## Effect 7 — Kinetic Text Marquee (Scroll-Velocity Linked)

Infinite-loop text marquee that speeds up when scrolling fast, slows when still.

```html
<div class="marquee" aria-hidden="true">
  <div class="marquee__track">
    <div class="marquee__content">
      <span>Used by 18,000 teams</span>
      <span class="marquee__dot">·</span>
      <span>Trusted worldwide</span>
      <span class="marquee__dot">·</span>
      <span>Zero config deploys</span>
      <span class="marquee__dot">·</span>
      <!-- Duplicate for seamless loop -->
      <span>Used by 18,000 teams</span>
      <span class="marquee__dot">·</span>
      <span>Trusted worldwide</span>
      <span class="marquee__dot">·</span>
      <span>Zero config deploys</span>
      <span class="marquee__dot">·</span>
    </div>
  </div>
</div>
```

```css
.marquee {
  overflow: hidden;
  border-top: 1px solid var(--color-border);
  border-bottom: 1px solid var(--color-border);
  padding-block: var(--space-4);
}

.marquee__track {
  display: flex;
}

.marquee__content {
  display: flex;
  align-items: center;
  gap: var(--space-8);
  white-space: nowrap;
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  animation: marquee-scroll 20s linear infinite;
  padding-right: var(--space-8);
}

.marquee__dot {
  color: var(--color-accent);
  font-size: 1.2em;
}

@keyframes marquee-scroll {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); } /* -50% because content is duplicated */
}

/* Pause on hover */
.marquee:hover .marquee__content {
  animation-play-state: paused;
}

@media (prefers-reduced-motion: reduce) {
  .marquee__content { animation: none; }
  .marquee { overflow: auto; }
}
```

**Velocity-linked speed (faster scroll = faster marquee):**
```javascript
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const marqueeContent = document.querySelector('.marquee__content');
  let lastScrollY = 0;
  let velocity = 0;
  let speed = 20; // base duration in seconds

  window.addEventListener('scroll', () => {
    velocity = Math.abs(window.scrollY - lastScrollY);
    lastScrollY = window.scrollY;

    // Faster scroll = lower duration = faster animation
    const targetSpeed = Math.max(5, 20 - velocity * 0.5);
    marqueeContent.style.animationDuration = `${targetSpeed}s`;
  }, { passive: true });
}
```

---

## Effect 8 — Counting Number Animation

Numbers count up when they enter the viewport.

```javascript
class CountUp {
  constructor(el) {
    this.el = el;
    this.target = parseFloat(el.dataset.target) || 0;
    this.duration = parseInt(el.dataset.duration) || 2000;
    this.prefix = el.dataset.prefix || '';
    this.suffix = el.dataset.suffix || '';
    this.decimals = parseInt(el.dataset.decimals) || 0;

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      el.textContent = this.prefix + this.target.toFixed(this.decimals) + this.suffix;
      return;
    }

    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        this.animate();
        observer.disconnect();
      }
    }, { threshold: 0.5 });
    observer.observe(el);
  }

  animate() {
    const start = Date.now();
    const from = 0;

    const tick = () => {
      const elapsed = Date.now() - start;
      const progress = Math.min(elapsed / this.duration, 1);

      // Ease out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = from + (this.target - from) * eased;

      this.el.textContent = this.prefix + current.toFixed(this.decimals) + this.suffix;

      if (progress < 1) requestAnimationFrame(tick);
    };

    requestAnimationFrame(tick);
  }
}

document.querySelectorAll('[data-count-up]').forEach(el => new CountUp(el));
```

```html
<span data-count-up data-target="18000" data-suffix="+" data-duration="2500">18000+</span>
<span data-count-up data-target="99.9" data-suffix="% uptime" data-decimals="1" data-duration="2000">99.9% uptime</span>
<span data-count-up data-target="23" data-suffix="s avg deploy" data-duration="1500">23s avg deploy</span>
```

---

## Text Animation by Context

| Heading type | Best animation | Duration |
|---|---|---|
| Page H1 (hero) | Blur-in with stagger per word | 600–800ms, 60ms stagger |
| Section H2 | Word reveal from bottom | 500ms, scroll-triggered |
| Feature heading | Variable weight morph | 800ms, scroll-triggered |
| Stats/numbers | Count-up | 1500–2500ms, ease-out cubic |
| Code examples | Typewriter | 25–40ms/char |
| Navigation items | Scramble on hover | Frame-based |
| Social proof marquee | Marquee continuous | 20s/loop |

---

*Pattern version: global-design-skill v1.0 — `patterns/effects/text-animations.md`*  
*Updated: 2026-05-20*  
*Related: `patterns/effects/scroll-experiences.md`, `patterns/effects/hover-effects.md`, `rules/05-animation.md`, `rules/03-typography.md`*
