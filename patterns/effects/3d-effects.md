# Pattern — 3D Effects

> CSS 3D perspective, card flips, product showcases, Three.js basics, and Spline embeds. Every technique includes reduced-motion fallback and mobile performance guidance.

---

## CSS 3D Fundamentals

### The Perspective Model

```css
/* Parent establishes the 3D space */
.scene {
  perspective: 1000px;          /* Distance from viewer to z=0 plane */
  perspective-origin: 50% 50%;  /* Vanishing point — change for dramatic angles */
}

/* Child transforms in 3D space */
.card {
  transform-style: preserve-3d; /* Children also exist in 3D */
  transform: rotateY(15deg) rotateX(5deg);
  transition: transform 400ms var(--ease-spring);
}

/* Individual child on z-axis */
.card-face {
  backface-visibility: hidden; /* Hide reverse side during flip */
}
```

**Perspective values and their feel:**

| Value | Effect | Best for |
|---|---|---|
| `200px–500px` | Extreme fish-eye, dramatic | Hero statements, stylized |
| `600px–900px` | Moderate depth, visible | Product showcases |
| `1000px–1500px` | Subtle depth, realistic | Cards, feature sections |
| `2000px+` | Near-isometric | Data dashboards |

---

## 3D Card Flip

```html
<div class="flip-scene">
  <div class="flip-card" id="flip-card">
    <div class="flip-face flip-front">
      <!-- Front content -->
      <h3>Feature Title</h3>
      <p>Short description</p>
    </div>
    <div class="flip-face flip-back">
      <!-- Back content -->
      <h3>How It Works</h3>
      <p>Technical detail or expanded content</p>
    </div>
  </div>
</div>
```

```css
.flip-scene {
  perspective: 900px;
  width: 320px;
  height: 200px;
}

.flip-card {
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 600ms var(--ease-spring);
  cursor: pointer;
}

.flip-card.flipped {
  transform: rotateY(180deg);
}

.flip-face {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  border: 1px solid oklch(100% 0 0 / 0.12);
  background: oklch(16% 0.012 258);
}

.flip-back {
  transform: rotateY(180deg);
  background: oklch(20% 0.02 258);
}

/* No animation — just show back */
@media (prefers-reduced-motion: reduce) {
  .flip-card { transition: none; }
  .flip-front { opacity: 1; }
  .flip-card.flipped .flip-front { opacity: 0; }
  .flip-card.flipped .flip-back { opacity: 1; }
  .flip-back { transform: none; opacity: 0; }
}
```

```javascript
document.querySelectorAll('.flip-card').forEach(card => {
  card.addEventListener('click', () => card.classList.toggle('flipped'));
});
```

---

## Product Tilt Showcase

Mouse-tracked 3D tilt with layered depth — the signature SaaS hero effect.

```html
<div class="tilt-container" data-tilt>
  <div class="tilt-inner">
    <!-- Layer 0: background / glow -->
    <div class="tilt-layer" data-depth="0.1">
      <div class="product-glow"></div>
    </div>
    <!-- Layer 1: main product image -->
    <div class="tilt-layer" data-depth="0.3">
      <img class="product-screenshot" src="/app-screenshot.png" alt="Product UI" fetchpriority="high">
    </div>
    <!-- Layer 2: floating badge -->
    <div class="tilt-layer tilt-float" data-depth="0.6">
      <div class="floating-badge">
        <span>↑ 42%</span>
        <span>Conversion rate</span>
      </div>
    </div>
  </div>
</div>
```

```css
.tilt-container {
  perspective: 1200px;
  width: min(560px, 100%);
}

.tilt-inner {
  position: relative;
  transform-style: preserve-3d;
  transition: transform 100ms linear;
  will-change: transform;
}

.tilt-layer {
  position: relative;
  transform-style: preserve-3d;
  transition: transform 100ms linear;
}

.product-screenshot {
  width: 100%;
  border-radius: var(--radius-lg);
  border: 1px solid oklch(100% 0 0 / 0.1);
  box-shadow:
    0 0 0 1px oklch(100% 0 0 / 0.05),
    0 24px 80px oklch(0% 0 0 / 0.5),
    0 8px 24px oklch(0% 0 0 / 0.3);
}

.product-glow {
  position: absolute;
  inset: -20%;
  background: radial-gradient(ellipse 60% 50% at 50% 50%, oklch(55% 0.22 258 / 0.2), transparent 70%);
  filter: blur(40px);
}

.floating-badge {
  display: flex;
  flex-direction: column;
  gap: 2px;
  padding: var(--space-3) var(--space-4);
  background: oklch(100% 0 0 / 0.08);
  backdrop-filter: blur(16px);
  border: 1px solid oklch(100% 0 0 / 0.15);
  border-radius: var(--radius-md);
  font-size: 0.75rem;
  position: absolute;
  bottom: 10%;
  right: -5%;
}

@media (prefers-reduced-motion: reduce) {
  .tilt-inner,
  .tilt-layer {
    transition: none;
    transform: none !important;
  }
}

@media (pointer: coarse) {
  /* Mobile: static, no tilt */
  .tilt-inner { transform: none !important; }
}
```

```javascript
class ProductTilt {
  constructor(el) {
    this.el = el;
    this.inner = el.querySelector('.tilt-inner');
    this.layers = el.querySelectorAll('[data-depth]');
    this.bounds = null;
    this.raf = null;
    this.targetX = 0;
    this.targetY = 0;
    this.currentX = 0;
    this.currentY = 0;

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    if (window.matchMedia('(pointer: coarse)').matches) return;

    this.el.addEventListener('mouseenter', () => {
      this.bounds = this.el.getBoundingClientRect();
      this.inner.style.willChange = 'transform';
    });

    this.el.addEventListener('mousemove', (e) => {
      const x = (e.clientX - this.bounds.left) / this.bounds.width - 0.5;
      const y = (e.clientY - this.bounds.top) / this.bounds.height - 0.5;
      this.targetX = x * 16; // max ±8deg
      this.targetY = -y * 12;
      this.tick();
    });

    this.el.addEventListener('mouseleave', () => {
      this.targetX = 0;
      this.targetY = 0;
      this.inner.style.willChange = 'auto';
    });
  }

  tick() {
    cancelAnimationFrame(this.raf);
    this.raf = requestAnimationFrame(() => {
      this.currentX += (this.targetX - this.currentX) * 0.12;
      this.currentY += (this.targetY - this.currentY) * 0.12;

      this.inner.style.transform =
        `rotateY(${this.currentX}deg) rotateX(${this.currentY}deg)`;

      // Parallax per layer depth
      this.layers.forEach(layer => {
        const depth = parseFloat(layer.dataset.depth);
        layer.style.transform =
          `translateZ(${depth * 40}px) translateX(${this.currentX * depth * -0.5}px) translateY(${this.currentY * depth * -0.5}px)`;
      });

      if (Math.abs(this.targetX - this.currentX) > 0.01 || Math.abs(this.targetY - this.currentY) > 0.01) {
        this.tick();
      }
    });
  }
}

document.querySelectorAll('[data-tilt]').forEach(el => new ProductTilt(el));
```

---

## CSS 3D Rotating Cube / Prism

Brand logo or feature icon rotating in 3D. Low cost, high visual interest.

```html
<div class="prism-scene">
  <div class="prism">
    <div class="prism-face prism-front">
      <svg><!-- icon --></svg>
    </div>
    <div class="prism-face prism-right">
      <svg><!-- icon --></svg>
    </div>
    <div class="prism-face prism-back">
      <svg><!-- icon --></svg>
    </div>
    <div class="prism-face prism-left">
      <svg><!-- icon --></svg>
    </div>
    <div class="prism-face prism-top">
      <svg><!-- icon --></svg>
    </div>
    <div class="prism-face prism-bottom">
      <svg><!-- icon --></svg>
    </div>
  </div>
</div>
```

```css
.prism-scene {
  perspective: 600px;
  width: 80px;
  height: 80px;
}

.prism {
  width: 80px;
  height: 80px;
  transform-style: preserve-3d;
  animation: prism-rotate 8s linear infinite;
}

.prism-face {
  position: absolute;
  width: 80px;
  height: 80px;
  border: 1px solid oklch(100% 0 0 / 0.15);
  background: oklch(16% 0.015 258 / 0.8);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
}

.prism-front  { transform: rotateY(0deg)   translateZ(40px); }
.prism-right  { transform: rotateY(90deg)  translateZ(40px); }
.prism-back   { transform: rotateY(180deg) translateZ(40px); }
.prism-left   { transform: rotateY(270deg) translateZ(40px); }
.prism-top    { transform: rotateX(90deg)  translateZ(40px); }
.prism-bottom { transform: rotateX(-90deg) translateZ(40px); }

@keyframes prism-rotate {
  from { transform: rotateX(10deg) rotateY(0deg); }
  to   { transform: rotateX(10deg) rotateY(360deg); }
}

@media (prefers-reduced-motion: reduce) {
  .prism { animation: none; transform: rotateX(10deg) rotateY(20deg); }
}
```

---

## Isometric Layout

Grid-based isometric projection — powerful for dashboards and feature sections.

```css
.iso-grid {
  display: grid;
  grid-template-columns: repeat(3, 200px);
  gap: 0;
  transform: rotateX(45deg) rotateZ(-45deg);
  transform-style: preserve-3d;
}

.iso-card {
  width: 200px;
  height: 120px;
  background: oklch(18% 0.015 258);
  border: 1px solid oklch(100% 0 0 / 0.1);
  padding: var(--space-4);
  transform-style: preserve-3d;
  position: relative;
}

/* Right face */
.iso-card::before {
  content: '';
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  height: 20px;
  background: oklch(12% 0.01 258);
  transform: rotateX(-90deg);
  transform-origin: top;
}

/* Left face */
.iso-card::after {
  content: '';
  position: absolute;
  top: 0;
  left: 100%;
  width: 20px;
  height: 100%;
  background: oklch(14% 0.01 258);
  transform: rotateY(90deg);
  transform-origin: left;
}
```

---

## Three.js — Minimal Setup

When CSS 3D isn't enough. Minimal Three.js for a hero visual.

```html
<canvas id="hero-canvas" aria-hidden="true"></canvas>
```

```javascript
import * as THREE from 'three';

// Skip if reduced motion
if (window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
  initHeroCanvas();
}

function initHeroCanvas() {
  const canvas = document.getElementById('hero-canvas');
  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2)); // Cap at 2x

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(45, canvas.offsetWidth / canvas.offsetHeight, 0.1, 100);
  camera.position.z = 5;

  // Geometry — torus knot as example
  const geometry = new THREE.TorusKnotGeometry(1.2, 0.35, 128, 32);
  const material = new THREE.MeshStandardMaterial({
    color: new THREE.Color('oklch(65% 0.22 258)'),
    roughness: 0.2,
    metalness: 0.8,
    wireframe: false,
  });
  const mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);

  // Lighting
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.4);
  scene.add(ambientLight);

  const pointLight = new THREE.PointLight(0x6699ff, 2, 10);
  pointLight.position.set(3, 3, 3);
  scene.add(pointLight);

  const pointLight2 = new THREE.PointLight(0xff66aa, 1, 8);
  pointLight2.position.set(-3, -1, 2);
  scene.add(pointLight2);

  // Resize
  const ro = new ResizeObserver(() => {
    const w = canvas.offsetWidth;
    const h = canvas.offsetHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  });
  ro.observe(canvas);

  // Mouse tracking
  let mouseX = 0, mouseY = 0;
  document.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
    mouseY = -(e.clientY / window.innerHeight - 0.5) * 2;
  });

  // Animation loop
  let raf;
  function animate() {
    raf = requestAnimationFrame(animate);
    mesh.rotation.y += 0.005;
    mesh.rotation.x += 0.002;
    // Subtle mouse follow
    mesh.rotation.y += (mouseX * 0.3 - mesh.rotation.y) * 0.02;
    mesh.rotation.x += (mouseY * 0.2 - mesh.rotation.x) * 0.02;
    renderer.render(scene, camera);
  }
  animate();

  // Pause when not visible
  const observer = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) {
      animate();
    } else {
      cancelAnimationFrame(raf);
    }
  });
  observer.observe(canvas);
}
```

**CSS to size the canvas:**
```css
#hero-canvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}
```

---

## react-three-fiber (R3F) — Minimal Hero

For React/Next.js projects.

```tsx
'use client';

import { useRef, useFrame } from '@react-three/fiber';
import { Canvas, useThree } from '@react-three/fiber';
import { MeshDistortMaterial, Float } from '@react-three/drei';
import { useReducedMotion } from 'motion/react';

function HeroSphere() {
  const meshRef = useRef<THREE.Mesh>(null);
  const prefersReducedMotion = useReducedMotion();

  useFrame((state) => {
    if (!meshRef.current || prefersReducedMotion) return;
    meshRef.current.rotation.y = state.clock.elapsedTime * 0.3;
    meshRef.current.rotation.x = Math.sin(state.clock.elapsedTime * 0.2) * 0.15;
  });

  return (
    <Float speed={2} rotationIntensity={0.2} floatIntensity={0.5}>
      <mesh ref={meshRef}>
        <sphereGeometry args={[1.5, 64, 64]} />
        <MeshDistortMaterial
          color="oklch(65% 0.22 258)"
          attach="material"
          distort={0.4}
          speed={2}
          roughness={0.2}
          metalness={0.6}
        />
      </mesh>
    </Float>
  );
}

export function HeroCanvas() {
  return (
    <Canvas
      camera={{ position: [0, 0, 5], fov: 45 }}
      style={{ position: 'absolute', inset: 0, pointerEvents: 'none' }}
      gl={{ alpha: true, antialias: true }}
      dpr={[1, 2]}
      aria-hidden="true"
    >
      <ambientLight intensity={0.4} />
      <pointLight position={[3, 3, 3]} intensity={2} color="#6699ff" />
      <pointLight position={[-3, -1, 2]} intensity={1} color="#ff66aa" />
      <HeroSphere />
    </Canvas>
  );
}
```

---

## Spline 3D Embed

Zero Three.js knowledge required. Use when you need polished 3D visuals fast.

```html
<!-- Option 1: Runtime embed (lazy load) -->
<script type="module" src="https://unpkg.com/@splinetool/viewer@latest/build/spline-viewer.js"></script>

<spline-viewer
  url="https://prod.spline.design/YOUR-SCENE-ID/scene.splinecode"
  loading-anim
  aria-hidden="true"
></spline-viewer>
```

```css
spline-viewer {
  width: 100%;
  height: 600px;
  pointer-events: none; /* Allow page scroll through the canvas */
}

/* Re-enable pointer events for interactive scenes */
spline-viewer.interactive {
  pointer-events: auto;
}
```

```tsx
// Option 2: React with @splinetool/react-spline
import Spline from '@splinetool/react-spline';
import { useReducedMotion } from 'motion/react';

export function SplineHero() {
  const prefersReducedMotion = useReducedMotion();

  if (prefersReducedMotion) {
    return <img src="/hero-static-fallback.jpg" alt="Product preview" />;
  }

  return (
    <Spline
      scene="https://prod.spline.design/YOUR-SCENE-ID/scene.splinecode"
      style={{ width: '100%', height: '600px', pointerEvents: 'none' }}
    />
  );
}
```

**Spline optimization rules:**
- Export compressed: `.splinecode` not `.spline`
- Disable "Retina" resolution in export if targeting <2x devices
- Set a static `<img>` fallback for reduced-motion preference
- `pointer-events: none` unless scene is interactive

---

## 3D Text with CSS

Extruded text effect — pure CSS, no JS.

```css
.text-3d {
  font-size: clamp(4rem, 10vw, 10rem);
  font-weight: 900;
  color: oklch(85% 0.01 258);
  text-shadow:
    1px 1px 0 oklch(55% 0.02 258),
    2px 2px 0 oklch(50% 0.02 258),
    3px 3px 0 oklch(45% 0.02 258),
    4px 4px 0 oklch(40% 0.02 258),
    5px 5px 0 oklch(35% 0.02 258),
    6px 6px 0 oklch(30% 0.02 258),
    7px 7px 0 oklch(25% 0.02 258),
    8px 8px 12px oklch(0% 0 0 / 0.5);
  transform: perspective(500px) rotateX(10deg);
  display: inline-block;
}
```

---

## Performance Rules for 3D

| Rule | Why |
|---|---|
| Use `will-change: transform` only during active animation, remove after | Avoids promoting every element to its own GPU layer |
| Cap `devicePixelRatio` at 2 for `<canvas>` | Prevents 3x/4x render on mobile (4× the pixels) |
| Pause `requestAnimationFrame` when off-screen | Use `IntersectionObserver` to cancel/resume the loop |
| `ResizeObserver` for canvas sizing | Never listen to `window.resize` directly |
| Static image fallback for `prefers-reduced-motion` | Never remove the section — just swap the element |
| Prefer CSS 3D over Three.js for < 5 objects | Zero bundle, GPU compositing, works everywhere |

---

## When to Use What

| Complexity | Solution | Bundle cost |
|---|---|---|
| Card hover depth, product tilt | CSS 3D + `perspective` | 0kb |
| Card flip, prism rotation | CSS 3D + `transform-style: preserve-3d` | 0kb |
| Animated blob / distortion | Three.js or R3F (minimal) | ~150kb |
| Full 3D scene, orbit controls | Three.js or R3F + Drei | ~200kb |
| Polished 3D hero visual, fast | Spline embed | ~120kb runtime |
| Interactive 3D product viewer | Three.js + GLTF loader | ~200kb + model |

---

*Pattern version: global-design-skill v1.0 — `patterns/effects/3d-effects.md`*  
*Updated: 2026-05-20*  
*Related: `patterns/effects/hover-effects.md`, `patterns/effects/parallax-system.md`, `rules/05-animation.md`*
