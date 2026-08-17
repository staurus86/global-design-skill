# Recipe — Extract a Design System from a Reference

> "Make it look like this" is a reference, not a spec. Before building, turn the reference — a screenshot, a live site, or a Figma frame — into something a developer can build *from*: a filled `MASTER` (tokens, type, spacing, components) plus DTCG tokens and an honest list of what you could and couldn't infer. Extraction first, build second; then verify the build against the reference (`rules/20` R6).

---

## When to use

- The brief is a reference, not a spec ("make it like Linear", a competitor screenshot, a Figma file)
- You're starting a multi-page build and want to lock one source of truth before any page (pairs with `templates/specs/design-system-master.md`)
- You need to reconstruct or re-theme an existing site/app you don't have the tokens for
- You want a token export (DTCG) from a design you can only see, not access

**Not for:** auditing your own already-built UI (use `checklists/global-design-review.md`), or finding *new* references (use `agents/reference-hunter.md`).

---

## Step 1 — Identify source and intent

| Source | How to capture | Intent |
|---|---|---|
| **Image / screenshot** | Vision analysis; pull dominant colors pixel-precise (sample the image, don't eyeball hex) | Reconstruct — infer the system from pixels |
| **Live site / URL** | Extract declared CSS custom properties (`--*`) from stylesheets first — those are *given*, not inferred; Playwright screenshots at 390/768/1280 | Replicate — prefer extracted tokens over inferred |
| **Figma file** | Figma MCP: pull variable definitions (explicit tokens) + a frame screenshot; cross-check declared vs used | Replicate — variables are the source of truth |

**Rule:** prefer *extracted* values (CSS `--*`, Figma variables) over *inferred* ones (eyeballed from a picture). Mark which is which in Step 4.

---

## Step 2 — Layered analysis, general to specific

Work top-down so the identity drives the details, not the reverse:

```
1. IDENTITY    → mood, aesthetic direction, the one memorable thing, macrostructure
2. SYSTEM      → color (OKLCH), type scale, spacing rhythm, radii, shadow, borders
3. COMPONENTS  → inventory: each component + its variants/states + visual props
4. LAYOUT      → grid, composition, section rhythm, responsive behavior across viewports
5. EFFECTS     → what the reference does that plain CSS can't (Step 2b)
6. RECONSTRUCT → notes a developer needs to rebuild it; what's load-bearing vs incidental
```

Convert every color to **OKLCH** (never store the raw hex you sampled — translate it). Snap spacing to the nearest 4px-grid step and say so.

---

## Step 2b — The effects layer

Tokens describe surfaces. They say nothing about the WebGL scene behind the hero, the particle field, the shader distortion on hover, or the scroll choreography — and those are usually *why* the user picked the reference. "There are some floating dots" is not buildable. Capture effects as parameters, the same way you capture color.

**Detect from a live site (✅ extracted, not guessed).** Grep the served HTML/JS before you interpret pixels:

| Signal | Means |
|---|---|
| `<canvas>` element | Canvas 2D or WebGL surface — check `getContext` argument |
| `three`, `@react-three/fiber`, `pixi.js`, `ogl` imports | 3D / WebGL scene |
| `.glsl`, `vertexShader`, `fragmentShader`, `uniform ` strings | custom shaders |
| `gsap`, `ScrollTrigger`, `lenis`, `locomotive-scroll` | JS-driven scroll choreography |
| `IntersectionObserver` + class toggles | reveal-on-scroll (cheap tier) |
| `lottie`, `.lottie`, `.json` animation payloads | Lottie |
| SVG `<animate>` / `stroke-dasharray` transitions | SVG path animation |
| `backdrop-filter`, `mix-blend-mode`, `feTurbulence` | glass, blend, grain — pure CSS/SVG tier |
| `cursor: none` + a following element | custom cursor |

**Detect from a screenshot (❓ by definition).** A static frame cannot show motion. Describe what is visibly beyond flat CSS — glow, depth, noise, distortion, glass — and mark it ❓. Do not name a technology you did not observe.

**Record each effect found as a row, not a sentence:**

| Field | Example |
|---|---|
| Where | hero background |
| What | connected-node particle field, mouse-repel |
| Tier | `css` / `canvas2d` / `gsap` / `webgl` (see below) |
| Params | ~120 nodes, 1–3px, link radius ~140px, accent hue at 30% opacity |
| Confidence | ✅ / ⚠️ / ❓ |

**Tier decides cost, so name it explicitly:**

| Tier | Tech | Budget reality |
|---|---|---|
| `css` | CSS animation, SVG, `backdrop-filter`, gradients | free — always prefer |
| `canvas2d` | Canvas 2D, one rAF loop | cheap, main-thread |
| `gsap` | GSAP / ScrollTrigger / Lottie | pulls a library — justify it |
| `webgl` | Three.js, R3F, custom GLSL | heaviest — needs a real reason and a fallback |

**Two things the reference will not tell you — decide and record them anyway:**

- **Fallback** — what renders when the effect is off: static poster frame, CSS-only reduction, or nothing. Every effect above `css` tier needs one.
- **Reduced motion** — `prefers-reduced-motion` gating is not optional and is not inherited from the reference. The reference is probably wrong about this; we are not.

**Do not force-fill.** An effect category the reference does not use is absent, not an empty row. A single screenshot yields a short effects table and a long Open Questions list — that is the honest output, not a failure.

Implementation lives in `patterns/effects/` (noise, mesh gradients, cursor, parallax, scroll, text, 3D) and `references/3d-animations.md`. This step decides *what* to build; those decide *how*.

---

## Step 3 — Emit the artifacts

Produce four outputs, not a prose summary:

1. **Filled `MASTER`** — fill `templates/specs/design-system-master.md` from the analysis: identity + Design Dials (inferred from the reference's variance/motion/density), OKLCH tokens, type, spacing/radii/shadow, component conventions, voice. This is the build's source of truth.
2. **DTCG tokens** — `design-tokens.json` in W3C DTCG format (`$value` / `$type`), matching `tokens/design-tokens.json`'s shape so it feeds Style Dictionary / Figma Variables / Tokens Studio directly.
3. **Component inventory** — table: component · observed variants/states · key visual props · usage context.
4. **Effects inventory** — the Step 2b table: where · what · tier · params · confidence, plus the fallback decided for each row above `css` tier. Omit if the reference has no effects; do not emit a table of "none".

---

## Step 4 — Mark confidence; list open questions

Every inferred value is a claim. Tag each with calibrated confidence so the developer knows what to trust vs confirm:

| Marker | Meaning | Example |
|---|---|---|
| ✅ | Extracted, not guessed | CSS `--accent` read from the stylesheet; a Figma variable |
| ⚠️ | Inferred but consistent | spacing snapped to 4px grid from measured gaps; type scale fitted to observed sizes |
| ❓ | Genuinely uncertain | exact font when only a screenshot exists; hover/focus states not visible in a static image |

End with **Open Questions** — the things a static reference can't tell you: interaction states, dark mode, edge-case content, motion. Do not invent them; ask or flag. (Calibrated certainty over confident guessing — same standard as the rest of the skill.)

---

## Step 5 — Build, then verify fidelity against the reference

Extraction is the input to the build, not the end. After building from the MASTER:

- Diff the rendered build against the reference across layout / type / color / spacing / radii / shadow / assets — `rules/20` **R6**. 1px borders and shadow spread: confirm by computed value, not by eye.
- Run the token-drift audit (`rules/20` **R7**, snippet K) so the tokens you extracted are the tokens that actually render.

---

## Source-specific notes

- **Image-only references are lossy.** You cannot extract real fonts, interaction states, dark mode, or motion from one static frame — these are ❓ by definition. Say so; don't fabricate.
- **Video / screen recording** is the only source that shows motion and effects honestly. If the user has one, ask for it before guessing at Step 2b.
- **Live sites:** read `--*` custom properties before inferring anything — a site that ships tokens hands you the system for free. Dismiss cookie banners before screenshotting.
- **Figma:** variables are ground truth (✅); but cross-check declared variables against actual usage on the frame — declared ≠ applied (the same drift `rules/20` R7 guards against).

---

*Recipe version: global-design-skill v2.7.0 — `recipes/extract-design-from-reference.md`*
*Related: `templates/specs/design-system-master.md` (the artifact this fills), `tokens/design-tokens.json` (DTCG shape), `rules/20-rendered-verification.md` (R6 fidelity, R7 token drift), `agents/reference-hunter.md` (finding references), `references/color-alchemy.md` (hex → OKLCH translation), `rules/00-escalation-protocol.md` (Design Dials, macrostructure), `patterns/effects/` + `references/3d-animations.md` (building what Step 2b captured)*
