# Reference — 3D Animations

> CSS perspective transforms, Three.js / React Three Fiber (R3F), Spline integration, and scroll-driven 3D. Covers both lightweight CSS 3D (no library) and full WebGL (R3F). Match the approach to the complexity.

---

## Decision Tree — Which 3D approach?

```
Is the 3D element a product screenshot or card?
  → CSS perspective transform (no library)

Is it a simple 3D shape or floating object?
  → CSS 3D transforms or Spline embed

Is it an interactive 3D scene with lighting?
  → React Three Fiber (R3F) + @react-three/drei

Is it a scroll-driven 3D product explode (like Apple)?
  → R3F + Lenis smooth scroll + ScrollTrigger

Is it a pre-built interactive scene from a designer?
  → Spline embed (fastest, no code)

Is performance critical (mobile, CWV)?
  → CSS-only or Spline. Avoid R3F on mobile unless essential.
```

---

## CSS 3D — Card Perspective

For product screenshots, pricing cards, and feature visuals. No library required.

### Static perspective hero visual

```css
.product-visual {
  transform: perspective(1200px) rotateY(-8deg) rotateX(2deg);
  transform-style: preserve-3d;
  will-change: transform;
  transition: transform 600ms cubic-bezier(0.16, 1, 0.3, 1);
}

.product-visual:hover {
  transform: perspective(1200px) rotateY(-4deg) rotateX(1deg) scale(1.02);
}

@media (prefers-reduced-motion: reduce) {
  .product-visual {
    transform: none;
    transition: none;
  }
  .product-visual:hover {
    transform: scale(1.01);
  }
}
```

### Scroll-driven perspective (CSS native, no JS)

```css
@keyframes orbit-product {
  from { transform: perspective(1000px) rotateY(10deg) rotateX(3deg); }
  to   { transform: perspective(1000px) rotateY(-5deg) rotateX(1deg); }
}

.product-orbital {
  animation: orbit-product linear both;
  animation-timeline: scroll(root block);
  animation-range: 0% 50%;
}

@media (prefers-reduced-motion: reduce) {
  .product-orbital { animation: none; }
}
```

### Pointer-driven tilt (interactive)

```ts
function initTilt(selector = '.tilt-card') {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  if (reduced) return

  document.querySelectorAll<HTMLElement>(selector).forEach(card => {
    let rafId: number

    card.addEventListener('mousemove', (e: MouseEvent) => {
      cancelAnimationFrame(rafId)
      rafId = requestAnimationFrame(() => {
        const rect = card.getBoundingClientRect()
        const dx = ((e.clientX - rect.left) / rect.width  - 0.5) * 2   // -1 to 1
        const dy = ((e.clientY - rect.top)  / rect.height - 0.5) * 2   // -1 to 1
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

initTilt()
```

---

## CSS 3D Scene (Layered Depth)

Create apparent 3D depth using multiple layers at different Z positions.

```css
.scene {
  perspective: 800px;
  transform-style: preserve-3d;
}

.layer-back {
  transform: translateZ(-60px) scale(1.08);
  opacity: 0.6;
  filter: blur(2px);
}

.layer-mid {
  transform: translateZ(0);
}

.layer-front {
  transform: translateZ(40px);
  filter: drop-shadow(0 20px 40px oklch(0% 0 0 / 0.3));
}

/* Scroll-driven parallax between layers */
@keyframes parallax-back  { to { transform: translateZ(-60px) scale(1.08) translateY(-5%); } }
@keyframes parallax-front { to { transform: translateZ(40px) translateY(-12%); } }

.layer-back  {
  animation: parallax-back  linear both;
  animation-timeline: scroll(root);
  animation-range: 0% 100%;
}

.layer-front {
  animation: parallax-front linear both;
  animation-timeline: scroll(root);
  animation-range: 0% 100%;
}
```

---

## Spline — Pre-built 3D Scenes

**When to use:** Designer-created 3D objects, interactive 3D product showcases, animated 3D illustrations. No Three.js knowledge needed.

**Performance warning:** Spline scenes include the full Spline runtime (~1.5MB). Use only for above-the-fold hero visuals where the visual impact justifies the cost. Lazy-load below fold.

### Embed (iframe — simplest)

```html
<iframe
  src="https://my.spline.design/[scene-id]/"
  width="100%"
  height="600px"
  loading="lazy"
  style="border: none; border-radius: var(--radius-xl);"
  title="3D product visualization"
/>
```

### React component with lazy load

```tsx
import { Suspense, lazy } from 'react'

const Spline = lazy(() => import('@splinetool/react-spline'))

function Hero3D() {
  return (
    <div className="hero-3d" style={{ height: '600px' }}>
      <Suspense fallback={<div className="skeleton-container" style={{ height: '100%' }} />}>
        <Spline scene="https://prod.spline.design/[scene-id]/scene.splinecode" />
      </Suspense>
    </div>
  )
}
```

---

## React Three Fiber (R3F)

For custom 3D scenes with lighting, physics, and full control.

### Setup

```bash
npm install three @react-three/fiber @react-three/drei
npm install -D @types/three
```

### Basic scene with lighting

```tsx
import { Canvas, useFrame } from '@react-three/fiber'
import { OrbitControls, Environment, Float } from '@react-three/drei'
import { useRef } from 'react'
import type { Mesh } from 'three'

function FloatingMesh() {
  const meshRef = useRef<Mesh>(null)

  useFrame((state) => {
    if (!meshRef.current) return
    meshRef.current.rotation.y = state.clock.elapsedTime * 0.3
  })

  return (
    <Float speed={1.5} rotationIntensity={0.5} floatIntensity={0.5}>
      <mesh ref={meshRef}>
        <torusKnotGeometry args={[1, 0.35, 128, 32]} />
        <meshStandardMaterial
          color="#4d9fff"    /* use a color close to your OKLCH accent */
          metalness={0.8}
          roughness={0.2}
        />
      </mesh>
    </Float>
  )
}

export function Scene3D() {
  return (
    <Canvas
      camera={{ position: [0, 0, 4], fov: 50 }}
      style={{ background: 'transparent' }}
      dpr={[1, 2]}       /* retina support with performance cap */
      gl={{ antialias: true, alpha: true }}
    >
      <ambientLight intensity={0.5} />
      <directionalLight position={[5, 5, 5]} intensity={1.5} castShadow />
      <Environment preset="city" />
      <FloatingMesh />
      <OrbitControls enableZoom={false} enablePan={false} />
    </Canvas>
  )
}
```

### Scroll-driven 3D (Apple-style product orbit)

```tsx
import { Canvas, useFrame, useThree } from '@react-three/fiber'
import { useScroll } from '@react-three/drei'
import { useRef } from 'react'
import type { Group } from 'three'

function ProductModel() {
  const groupRef = useRef<Group>(null)
  const scroll = useScroll()

  useFrame(() => {
    if (!groupRef.current) return
    const progress = scroll.offset   // 0 to 1 based on scroll position

    groupRef.current.rotation.y = progress * Math.PI * 2   // full rotation on scroll
    groupRef.current.position.y = Math.sin(progress * Math.PI) * 0.5
  })

  return (
    <group ref={groupRef}>
      {/* your model here */}
    </group>
  )
}

export function ScrollScene() {
  return (
    <Canvas style={{ height: '300vh' }}>
      {/* ScrollControls wraps the scene and provides scroll context */}
      {/* import { ScrollControls } from '@react-three/drei' */}
      {/* <ScrollControls pages={3}> */}
        <ProductModel />
      {/* </ScrollControls> */}
    </Canvas>
  )
}
```

### GLTF model loading

```tsx
import { useGLTF, Stage } from '@react-three/drei'
import { Canvas } from '@react-three/fiber'
import { Suspense } from 'react'

function Model({ url }: { url: string }) {
  const { scene } = useGLTF(url)
  return <primitive object={scene} />
}

/* Preload for faster LCP */
useGLTF.preload('/models/product.glb')

export function ProductViewer() {
  return (
    <Canvas camera={{ fov: 45 }}>
      <Suspense fallback={null}>
        <Stage environment="city" intensity={0.5}>
          <Model url="/models/product.glb" />
        </Stage>
      </Suspense>
    </Canvas>
  )
}
```

---

## Performance Rules for 3D

| Rule | Why |
|---|---|
| `dpr={[1, 2]}` on Canvas | Cap at 2× — 3× is imperceptibly better, 50% more GPU load |
| `lazy()` wrap for R3F components | Don't block first paint for below-fold 3D |
| `useGLTF.preload()` for models | Start loading during idle time |
| Compress `.glb` with `gltfpack` | Reduces model size 60–80% |
| `shadows={false}` unless essential | Real-time shadows are expensive |
| `performance.min` throttle | R3F can auto-drop quality on slow devices |
| Never use R3F inside a list | One Canvas per page, isolate |

### Throttle on low-end devices

```tsx
import { Canvas, useThree } from '@react-three/fiber'
import { PerformanceMonitor } from '@react-three/drei'
import { useState } from 'react'

function AdaptiveScene() {
  const [dpr, setDpr] = useState(1.5)

  return (
    <Canvas dpr={dpr}>
      <PerformanceMonitor
        onIncline={() => setDpr(2)}    /* fast device — increase quality */
        onDecline={() => setDpr(1)}    /* slow device — drop quality */
      >
        {/* scene */}
      </PerformanceMonitor>
    </Canvas>
  )
}
```

---

## Reduced Motion for 3D

```tsx
import { useReducedMotion } from 'motion/react'
import { useFrame } from '@react-three/fiber'
import { useRef } from 'react'

function AnimatedMesh() {
  const ref = useRef<THREE.Mesh>(null)
  const reduced = useReducedMotion()

  useFrame((state) => {
    if (!ref.current || reduced) return
    ref.current.rotation.y = state.clock.elapsedTime * 0.5
  })

  return <mesh ref={ref}>{/* ... */}</mesh>
}
```

---

## Archetype-Specific 3D Usage

| Archetype | 3D technique | Example |
|---|---|---|
| A — Ethereal Black | CSS perspective + bezel, CSS scroll-driven | Raycast command palette |
| E — Volumetric Glass | R3F glass sphere, layered CSS depth | Liveblocks hero |
| H — Spatial Luxury | R3F GLTF product orbit | Apple AirPods Pro |
| F — Neo-Maximalism | CSS 3D text extrusion | Figma Config |
| G — Terminal | None — 2D only | Terminal aesthetic |
| D — Organic Softness | CSS floating blobs (not 3D) | Calm.com |

---

*Reference version: global-design-skill v1.0 — `references/3d-animations.md`*
*Related: `references/visual-effects.md`, `references/motion-systems.md`, `references/motion-dev.md`*
