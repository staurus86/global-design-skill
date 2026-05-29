# HyperFrames Integration Guide

> HyperFrames converts HTML + CSS + animations into deterministic MP4 video. Compositions are plain HTML files with `data-*` timing attributes — no React, no build step. Renders via Puppeteer + FFmpeg.
>
> **Source:** github.com/heygen-com/hyperframes — Apache 2.0, used in production at HeyGen, tldraw, TanStack.

---

## When to use HyperFrames

| Task | Use HyperFrames | Build as UI |
|---|---|---|
| Product demo / feature announcement video | ✅ | |
| Social media content (1080×1920, 1080×1080) | ✅ | |
| Changelog or PR walkthrough animation | ✅ | |
| Data viz export to video | ✅ | |
| Animated hero for a landing page | | ✅ |
| Interactive component | | ✅ |

---

## Setup

Requirements: Node.js ≥ 22, FFmpeg.

```bash
npx hyperframes init my-video
cd my-video
npx hyperframes preview    # live preview at localhost:3002
npx hyperframes render     # → output.mp4
npx hyperframes doctor     # verify environment
```

**Agent-first workflow** (Claude Code):
```bash
npx skills add heygen-com/hyperframes
# then describe the video to Claude Code
```

---

## Composition HTML structure

```html
<div id="stage"
  data-composition-id="product-launch"
  data-start="0"
  data-width="1920"
  data-height="1080">

  <!-- Background layer -->
  <div data-start="0" data-duration="8" class="bg"></div>

  <!-- Video clip -->
  <video data-start="0" data-duration="6"
         data-track-index="0" src="screen.mp4"></video>

  <!-- Title — enters at 1s, stays 5s -->
  <h1 data-start="1" data-duration="5">Ship it.</h1>

  <!-- Ambient music -->
  <audio data-start="0" data-duration="8"
         data-volume="0.4" src="music.wav"></audio>
</div>
```

**Key attributes:**

| Attribute | Type | Meaning |
|---|---|---|
| `data-start` | seconds | When element becomes visible |
| `data-duration` | seconds | How long it stays |
| `data-track-index` | integer | Audio track lane (for mixing) |
| `data-volume` | 0–1 | Volume for audio elements |

Common dimensions: `1920×1080` (16:9), `1080×1920` (9:16 / Reels), `1080×1080` (square).

---

## Using global-design-skill tokens in compositions

CSS variables from `tokens/tokens.css` work **natively** — HyperFrames renders in a real browser.

```html
<head>
  <link rel="stylesheet" href="../../tokens/tokens.css">
  <style>
    #stage {
      background: var(--color-bg);
      font-family: var(--font-sans);
    }
    h1 {
      color: var(--color-text-primary);
      font-size: clamp(2.5rem, 5vw, 5rem);
      font-weight: var(--font-weight-bold);
    }
  </style>
</head>
```

OKLCH colors animate natively between keyframes:
```css
@keyframes color-shift {
  from { color: oklch(65% 0.18 250); }
  to   { color: oklch(75% 0.22 200); }
}
```

---

## Animation compatibility

| Approach | Works in HyperFrames | Notes |
|---|---|---|
| CSS animations + `@keyframes` | ✅ | Preferred for simple motion |
| GSAP | ✅ | Via `createGSAPFrameAdapter` — must be seekable |
| CSS scroll-driven animations | ❌ | No scroll context in video |
| `motion/react` | ❌ | Requires React runtime |
| Lottie | ✅ | Via Lottie frame adapter |
| Three.js | ✅ | Via custom adapter |
| `IntersectionObserver` triggers | ❌ | No viewport events in renderer |

**Critical rule for video:** Animations must be **seekable by frame index**, not wall-clock dependent. GSAP timelines work; `setTimeout`-based animations don't.

**`prefers-reduced-motion` is irrelevant in video** — use full animations without the media query guard.

---

## CSS animation pattern for video

Use `@keyframes` directly on `data-start`/`data-duration` elements:

```css
.title-enter {
  animation: slide-up 0.6s cubic-bezier(0.16, 1, 0.3, 1) both;
  animation-delay: 0.2s;
}

@keyframes slide-up {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

Stagger children via `animation-delay` (same rule from `rules/05-animation.md` applies):
```css
.feature:nth-child(1) { animation-delay: 0.1s; }
.feature:nth-child(2) { animation-delay: 0.2s; }
.feature:nth-child(3) { animation-delay: 0.3s; }
```

---

## Checklist

```
[ ] `data-composition-id` set on #stage
[ ] `data-width` / `data-height` match target aspect ratio
[ ] All elements have `data-start` + `data-duration`
[ ] OKLCH color tokens imported from tokens/tokens.css
[ ] No motion/react or framer-motion imports
[ ] No scroll-driven animations or IntersectionObserver
[ ] GSAP timelines use frame adapter (not gsap.play())
[ ] `npx hyperframes lint` passes with 0 errors
[ ] `npx hyperframes preview` — visual review before render
[ ] Output MP4 reviewed for timing and color accuracy
```

---

*Related: `rules/05-animation.md` (CSS animation rules), `tokens/tokens.css`, `blueprints/landing-page-from-scratch.md`*
