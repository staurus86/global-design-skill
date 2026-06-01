# Reference — Anti-Slop System (the Visual Ceiling)

> **Floor vs ceiling.** `references/sources.md` defines the *anti-slop floor* — correct semantics, systematic CSS, accessibility, validation. This file is the *ceiling*: the visual and interaction layer.
>
> **Read the type tags — not every row is an "AI tell."** This catalog mixes three things, and conflating them is itself a slop habit. Each row is tagged:
>
> - **[AI]** — a *diagnostic* tell: its presence specifically marks output as AI/template-generated. A pro avoids it; the default produces it. Sourced from catalogs that explicitly study AI output.
> - **[craft]** — timeless good design the generated default skips. True and useful, but **not** a diagnostic of AI — a human amateur skips it too. It belongs here as a *fix that pre-empts slop*, not as evidence of AI.
> - **[trend]** — time-bound taste/forecast. Weakly verifiable; treat as opinion, re-check before quoting as fact.
>
> **Why slop happens.** An image model and a coding model both regress to the statistical mean of their training data. "Slop" is that mean rendered confidently. The [AI] rows name the mean directly; the [craft] rows are the deviations that read as *chosen, not defaulted*.
>
> **How to use.** Deep catalog behind the short ban list in `skills/global-design/SKILL.md` → Banned Patterns and the `AI Slop Test` in `checklists/global-design-review.md`. When *diagnosing* "did AI make this?", weigh the [AI] rows. When *improving* any design (AI or human), apply [craft]. Values are defaults to deviate *from* with intent, not new dogma to default *to*.

---

## 1. Color

| # | Type | Pattern | Premium fix | Source |
|---|---|---|---|---|
| C1 | [AI] | Purple→indigo/violet gradient (`linear-gradient(135deg, #6366f1, #8b5cf6)`) as hero/CTA/background — the single most-recognized AI fingerprint. Cyan-on-dark is the runner-up. | One confident accent from a defined OKLCH ramp, occupying 10–20% of the surface. If the product needs no accent (Vercel), go monochrome + a single brand hue. Never the Tailwind purple defaults. | impeccable.style/slop · prg.sh · pixeldarts |
| C2 | [AI] | Gradient text (`background-clip: text`) on H1/H2 or metric numbers. | Solid color for text. Carry emphasis with weight or size, never a decorative gradient that marks the heading as generated. | impeccable.style/slop |
| C3 | [craft] | Raw hex/HSL tokens; 5+ hues; gray text (`#6b7280`) on colored surfaces → washed out, fails contrast. *(general color hygiene, not AI-specific)* | OKLCH throughout — perceptual lightness holds across hues and prevents muddy ramps. On a colored surface use a darker tint *of that surface's hue* or near-white; never generic gray on hue. Step `L` only for ramps: `oklch(0.97 0.01 h)` → `oklch(0.25 0.02 h)`. Relative syntax: `oklch(from var(--accent) calc(l - 0.1) c h)`. | evilmartians · refactoringui |
| C4 | [AI] | Colored `box-shadow` "glow" on dark UI used as a "cool" effect. | Replace with subtle layered lighting (see D1) or remove. Glow is decoration with no depth information. | impeccable.style/slop |

≤3 colors total; accent ≤ 15–20% of perceived surface. Cross-ref `rules/04-color.md`, `rules/19-contrast-standards.md`.

## 2. Typography

| # | Type | Pattern | Premium fix | Source |
|---|---|---|---|---|
| T1 | [AI] | Inter / Geist / Roboto / Space Grotesk as the only face — the "shadcn default" monoculture (~95% of generated sites). | Pair a distinctive display face with a refined body face, or one variable font with real character. Antidote galleries: Typewolf, Fonts In Use. Borrow Linear's trick — load a better `&` glyph if nothing else. | 925studios · prg.sh · paco-coursey |
| T2 | [craft] | Flat type scale — adjacent levels differ < 1.25× (e.g. 16/18/20px). No clear "where to look." | Modular scale ≥ 1.25 between steps; 3–4 visibly distinct levels. Swiss discipline: a 4-size scale only (e.g. 12 / 16 / 28 / 56). | impeccable.style/slop · swissthemes |
| T3 | [craft] | `line-height < 1.3` on body; `letter-spacing` widened on body text. | Body `line-height: 1.5–1.7`; widen tracking only on short uppercase labels (`0.08–0.12em`). Headings tighten: `-0.02em` to `-0.04em`. Min body 16px. | impeccable.style/slop |
| T4 | [craft] | Same stroke weight at 14px body and 72px hero — thin and generic at large sizes. | `font-optical-sizing: auto` + `font-feature-settings: "liga" 1, "kern" 1`. Variable fonts make this free. | fonts.google.com/knowledge |
| T5 | [craft] | **Discrete** `font-weight` swap on hover/selected → text reflows and jumps width (switching between separate font files). | Don't swap discrete weights on hover; shift color, opacity, or `text-decoration`. Note: animating the `wght` axis of a *variable* font (`font-variation-settings: 'wght' …`) does **not** reflow — it interpolates one font — so kinetic weight on scroll/hover is fine (see `rules/03-typography.md` R10). | interfaces.rauno.me · uraldes (ES) |
| T6 | [craft] | Body set full-viewport-width (>80 chars/line). | `max-width: 65ch–75ch` on text containers; ≥16px horizontal padding from the edge. | impeccable.style/slop · butterick |

Cross-ref `rules/03-typography.md`.

## 3. Layout & Structure

| # | Type | Pattern | Premium fix | Source |
|---|---|---|---|---|
| L1 | [AI] | Icon-tile + heading + 3 equal columns — the universal AI feature-card scaffold. | Vary card sizes; drop the rounded-square icon container (let icons sit in flow); alternate layout direction; one feature full-width, others half. | impeccable.style/slop · 925studios |
| L2 | [AI] | Nested cards (cards inside cards). | Flat hierarchy via spacing, type, and dividers. Each level of nesting must earn itself. | impeccable.style/slop |
| L3 | [AI] | Eyebrow pill + oversized full-sentence headline as the default SaaS hero. | Drop the eyebrow or fold it into the headline. A large headline is 1–3 words, not a sentence. Roman over italic for hero display. | impeccable.style/slop |
| L4 | [craft] | Uniform spacing — one value at every level; "mathematically perfect, emotionally cold." | Keep the 8px grid but vary multipliers by relationship: tight (`4–8px`) within a group, generous (`48–96px`, sections `96–128px`) between groups. Heuristic: take what feels enough, then double the section gap. | pixeldarts · refactoringui |
| L5 | [trend] | Bento grid + global glassmorphism as the homepage default ("reads as 2026 template" — a taste forecast, not a hard tell). | One signature moment per page beats 20 scattered effects. Apply blur only where layering is the actual problem. | metabole.studio · utsubo |
| L6 | [craft] | Inner pages drift from the homepage (different shadows on /blog vs /product). | A single propagated token set: `--shadow-color`, `--radius-{sm,md,lg}`, `--space-unit`. Coherence across routes is the premium signal (Awwwards judges flag drift). | utsubo |
| L7 | [AI] | The card grid as the *only* structural idea — every section is boxes. The generated default reaches for cards because they're safe. | Match structure to content. Menu of alternatives: editorial/asymmetric layout, comparison table, timeline, dense list, annotated diagram, process/flow map, split feature, bento *with intent*. Cards are one option, not the default. | impeccable.style/slop · 925studios |

Cross-ref `rules/02-layout-and-grid.md`, `rules/00-escalation-protocol.md` (Macrostructure-First).

## 4. Depth — Shadows, Borders, Radius

| # | Type | Pattern | Premium fix | Source |
|---|---|---|---|---|
| D1 | [craft] | One flat `box-shadow: 0 4px 20px rgba(0,0,0,.15)` on every card. | Light comes from above: x-offset 0, y-offset grows with elevation, **blur ≈ 2× the y-distance** (Hobday). Stack several layers at one low alpha (Comeau's verified pattern below); hue-tint, don't use pure black. Every shadow on the page shares the same ratio. <br>`box-shadow: 0 1px 1px oklch(0% 0 0/.075), 0 2px 2px oklch(0% 0 0/.075), 0 4px 4px oklch(0% 0 0/.075), 0 8px 8px oklch(0% 0 0/.075), 0 16px 16px oklch(0% 0 0/.075);` | joshwcomeau (verified) · anthonyhobday |
| D2 | [AI] | Hairline border **and** wide soft shadow on the same surface — the "safe depth" double-signal (verified wording: "a recurring generated-UI signature"). | Pick one: defined edge *or* soft elevation. Two depth cues on one card cancel. | impeccable.style/slop (verified) |
| D3 | [AI] | Thick accent border on a card that clashes with its rounded corners (the verified phrasing) — side-stripe `border-left` is the common form. | Remove it (already a Banned Pattern). If accent is needed, use a background tint or inset top shadow, not a stripe that fights the radius. | impeccable.style/slop (verified) |
| D4 | [AI] | One uniform radius on everything, and radius pushed so high (`44px+`) the card "rounds into a blob" (verified threshold — *not* 16–24px). | Radius hierarchy: cards 12–16px, inputs 6–8px, full-pill (`9999px`) only for tags/badges, large sections 0–minimal. Nested radius: **inner = outer − gap** (Hobday). | impeccable.style/slop (verified) · anthonyhobday |
| D5 | [craft] | Borders on every element (cards, inputs, rows, sections, dividers) → noise at every level. | Remove half. Separate sections with spacing + a background-color change, not lines. Needed borders go near-invisible: light `oklch(0% 0 0/.06)`, dark `oklch(100% 0 0/.08)`. | pixeldarts · refactoringui |
| D6 | [craft] | Garish high-saturation "neutral" grays; containers indistinguishable from the background. | Neutrals < 5% saturation (HSB). A container differs from its background by ≤ 7% brightness on light UI, ≤ 12% on dark — present but not loud (Hobday). Button horizontal padding ≈ 2× vertical. | anthonyhobday · learnui.design |

## 5. Texture & Surface

| # | Type | Pattern | Premium fix | Source |
|---|---|---|---|---|
| X1 | [craft] | Flat solid/two-stop gradient backgrounds — "void-like" in dark mode. | SVG grain overlay: `feTurbulence baseFrequency≈0.65 numOctaves=3` as a pseudo-element, `mix-blend-mode: soft-light`, opacity ≈ 0.5. Cheap vs a raster image, kills the flatness. | bstefanski |
| X2 | [AI] | `repeating-linear-gradient` stripes used as decorative "texture." | Plain surface, or a deliberate texture with a reason. Stripes-as-filler is a generated-UI signature. | impeccable.style/slop |

Cross-ref `references/visual-effects.md`, `references/aesthetic-recipes.md` (Glassmorphism guardrails).

## 6. Motion

| # | Type | Pattern | Premium fix | Source |
|---|---|---|---|---|
| M1 | [craft] | `transition: all 0.3s ease-in-out` on everything (also a common generated-code default). | A custom easing token (`cubic-bezier(0.25, 0.46, 0.45, 0.94)` standard; `cubic-bezier(0.16, 1, 0.3, 1)` for enters). Durations: hover ~150ms, state ~200–250ms, layout < 350ms. Interactions feel immediate under ~200ms. | interfaces.rauno.me · techbytes |
| M2 | [craft] | Bounce/elastic easing on UI; scale/rotate on hover for images. | Spring physics only for elements with real mass (drag, sheets). Modals scale `0.95 → 1` from opacity 0, not `0 → 1`. Make image hover transforms subtle or drop them. | impeccable.style/slop · interfaces.rauno.me |
| M3 | [craft] | Animating layout props (`height`, `padding`, `top/left`) → reflow and jank. | Animate `transform`/`opacity` only. Height reveal via `grid-template-rows: 0fr → 1fr`; press via `transform: scale(0.96)`. *(general perf practice; not verbatim from Rauno)* | MDN · web.dev |
| M4 | [craft] | Generic everywhere-animation (AOS on every div, entrance on body copy). | One intentional motion per scroll section, serving narrative pacing. Stagger 0.1/0.2/0.3s. Always gate behind `prefers-reduced-motion`. | utsubo · coosy |

Cross-ref `rules/05-animation.md`, `rules/17-motion-react.md` (`motion/react`, not `framer-motion`).

## 7. Imagery & Copy

| # | Type | Pattern | Premium fix | Source |
|---|---|---|---|---|
| I1 | [AI] | Stock hero, Midjourney grid-fill, placeholder avatars (literally AI/template imagery). | Original photography or hand illustration. As AI imagery floods the web, real/handcrafted reads as expensive — the German "echte Bilder" credibility argument and the French 2026 analog counter-signal both point here. | leineglueck (DE) · metabole (FR) |
| I2 | [AI] | Generic SaaS copy: "Build the future", "all-in-one platform", "streamline / empower / supercharge"; hedging ("may help", "can potentially"). | Concrete verb + noun (Stripe: "Financial infrastructure for the internet"; Linear: "Plan and build products"). Test: would a founder say it aloud? See `checklists/global-design-review.md` §10 and the `writing-rule` skill. | 925studios · prg.sh |
| I3 | [AI] | Emoji used as primary UI icons or section markers (🚀 ✨ 🔒 in headings, buttons, feature rows) — a strong LLM-output tell; renders inconsistently across platforms and breaks a11y naming. | One consistent SVG icon system (Lucide, Phosphor, a custom set) at a single stroke weight and grid. Emoji only where the content is literally about that emoji (e.g. a reactions picker). | impeccable.style/slop · 925studios |
| I4 | [AI] | Decorative charts: sparklines, gauges, and dashboards with no labels, units, axes, or real data — "data slop" used as visual filler. | Every chart tells one true story with labels + units + source. No fake metrics, no chart that survives deleting its data. If it's decoration, it's not a chart — remove it. | impeccable.style/slop · `patterns/admin-ui/charts.md` |

## 8. Premium Craft Signals — [craft], NOT AI-specific tells

> Everything in this section is **[craft]** unless tagged otherwise: timeless, locale, and tradition-specific design hygiene. It is here because the generated default skips it — so applying it pre-empts slop — **but its absence is not evidence of AI**. Two items carry the conceptual anti-AI argument and are tagged **[AI]**; a few are time-bound and tagged **[trend]**.

- **Japanese — 余白 (yohaku / "extra white").** [craft] Whitespace signals a brand that can afford restraint, not absence. Content at ~1/4–1/5 of "feels complete" density; whitespace ≥ 30–40% of the visual field; one fade-in per product shot. *(nextage-tech, coosy)*
- **Japanese — intentionality.** [AI] Before building, answer 「なぜ、このデザインであるべきなのか」 — *why this design specifically?* The same CSS values read cheap or premium by whether they were chosen or defaulted. This is the conceptual core of slop — AI optimizes pattern-match, not meaning. *(goodpatch)*
- **Swiss — the grid is the design.** [craft] 8pt grid, 12 columns, 24px gutters (16px mobile); every dimension a multiple of 8; type on a 4-size scale. Mathematical alignment alone reads premium. *(swissthemes)*
- **French — typography as graphic element.** [trend] Break the grid with one oversized display heading (`clamp(3rem, 10vw, 9rem)`) surrounded by negative space, functioning as image. Anti-bento, anti-template. *(metabole, elias.studio)*
- **German — authenticity over polish.** [AI] As AI output floods the web, real images and concrete proof raise credibility more than effects; handcraft becomes the anti-AI signal. *(leineglueck)*
- **Russian (Бюро Горбунова / Бирман) — the density rule.** [craft] Inner padding ≤ outer padding: tighter groups read as more related. Plus rhythm, modularity, strict text hierarchy. *(awdee.ru, bureau.ru)*
- **Chinese — 留白 / 计白当黑 (whitespace as the subject).** [craft] Inherited from ink-painting composition: empty space signals a brand that can afford restraint. Section breaks 48–96px. *(woshipm, wellworks)*
- **Chinese — CJK typography is not Latin typography.** [craft] *Locale typography hygiene, unrelated to AI — applies to any CJK site.* CJK glyphs are denser, so body needs **more** leading: `line-height 1.6–1.75` for prose (not the 1.5 default), and a shorter measure — **35–42 CJK chars/line** desktop, 20–25 mobile. Build text-color hierarchy by stacking opacity (`oklch(0% 0 0/.85 / .55 / .25)`), not hand-picked grays. Watch the **思源黑体 / Source Han Sans baseline-drift bug** at ≥64px (text sits low in centered buttons); use PingFang SC on iOS or the 梦源黑体 fork. Add a thin space (`letter-spacing: .05em` or U+2009) between CJK and Latin; never mix full-width and half-width punctuation in one block. *(uisdc, zcool, meia)*
- **Korean — type as image, tight headings.** [craft] *Locale typography, not AI.* Tighten headings ≥32px to `letter-spacing: -0.02em` to `-0.03em` with `line-height 1.1–1.2`; mobile body 17px / 155% / single weight. Treat at least one typographic element per zone as a graphic object — 폰트를 이미지로. *(brunch.co.kr)*
- **Latin (ES / PT / IT).** [trend] Fluid section padding `clamp(4rem, 10vw, 8rem)` instead of breakpoint jumps [craft]; unconventional high-contrast color pairings over the muted-sage template [trend]; deliberate analog imperfection (grain, brush, hand-drawn layer) as the luxury / anti-AI signal [trend]; every animation must answer "what happened?" or "what can I do?" — else cut it [craft]. *(pabloalcalde, designtec, grafigata, a126)*
- **Universal — widow control.** [craft] `h1,h2,h3 { text-wrap: balance }` and `p { text-wrap: pretty }` kill orphaned last-line words across every script — see `rules/03-typography.md` R14.

## 9. The Meta Principle [AI]

Slop is the confident average. Every fix above is one act of *deviation with a reason*. The fastest tell that something is generated is that it looks correct yet explains nothing about the brand — it could belong to any company. The fastest tell that something is *made* is that each spatial, type, and motion decision traces back to user, brand, or content. Pass this through tokens, not one-off prompts: a propagated design-token set carries taste across every route; a clever prompt carries it across one screen.

**Consistent, not uniform.** The system logic repeats (tokens, type ramp, spacing scale, icon language); the *composition* varies — rhythm, density, layout direction, and visual storytelling change section to section. Uniformity is the slop reflex (every section identical); consistency is the craft (the same grammar, different sentences). And ship one **signature move** — an unusual grid, a distinctive type pairing, a branded illustration or icon language, a tactile texture, a strong editorial rhythm, or one memorable interaction — so the result is a product with a point of view, not a cleaner template. See `rules/00-escalation-protocol.md` Memorability Gate.

---

## Provenance & confidence

- **Independently fetched and quoted (2026-05-31):** impeccable.style/slop, joshwcomeau (shadows), interfaces.rauno.me, evilmartians (OKLCH), bstefanski (grain), anthonyhobday, learnui.design — the [AI] color/depth tells and the [craft] shadow/radius values rest on verified quotes.
- **Agent-summarized, not verifier-fetched:** the CN / KR / JP / FR / ES / PT / IT sources in §8. Their AI-irrelevance is a conceptual judgment (locale/craft ≠ AI diagnostic), independent of source-quote accuracy; treat specific numbers (e.g. 思源黑体 bug, 17px/155%) as second-hand until checked against the primary page.
- **Corrections already applied from the verification pass:** over-rounding threshold **44px+** (not 16–24px); shadow **blur ≈ 2× y-distance**, x-offset 0 (not "vertical = 2× horizontal"); T5 reflow applies to **discrete** weight swaps, not variable-axis animation.
- **Honesty note:** of ~40 rows, ~40% are diagnostic **[AI]** tells; ~45% are **[craft]** the default skips; ~15% are **[trend]**. Use the tags — do not cite a [craft] or [trend] row as proof that "AI made this."

## Curated Sources (the strongest, deduped)

> Core CSS values independently verified against the primary pages on 2026-05-31. Dead/blocked at check time: several Smashing Magazine and nngroup deep links, bradfrost.com state-of-design-systems — cite the live equivalents below.

**Catalogs of AI tells (the [AI] rows)**
- **impeccable.style/slop** — https://impeccable.style/slop/ — the most concrete checklist of AI UI tells by category, with CSS values and fixes. Primary reference.
- **925Studios — AI Slop Web Design Guide** — https://www.925studios.co/blog/ai-slop-web-design-guide — typography/color/spacing/motion/copy with real brand examples.
- **prg.sh — Why Your AI Keeps Building the Same Purple Gradient Website** — https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website — root cause + concrete bans.
- **Hallmark (Nutlope)** — https://github.com/Nutlope/hallmark — competitive anti-slop *skill*: build/audit/redesign modes, macrostructure variance.
- **Goodpatch (JP)** — https://goodpatch.com/blog/2025-12-tochio — intentionality vs pattern-match (the conceptual [AI] argument).

**Craft fundamentals (the [craft] rows — good design, not AI-diagnostic)**
- **Josh Comeau — Designing Beautiful Shadows** — https://www.joshwcomeau.com/css/designing-shadows/ — layered shadow physics with exact CSS.
- **Rauno Freiberg — Web Interface Guidelines** — https://interfaces.rauno.me/ — numbered interaction/motion/timing rules.
- **Refactoring UI — 7 Practical Tips** — https://medium.com/refactoring-ui/7-practical-tips-for-cheating-at-design-40c736799886 — Wathan/Schoger micro-fixes.
- **Evil Martians — OKLCH in CSS** — https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl — the perceptual-color case with code.
- **bstefanski — Noisy/grainy backgrounds in CSS** — https://www.bstefanski.com/blog/noisygrainy-backgrounds-and-gradients-in-css — SVG grain recipe.
- **pixeldarts — Behind Stripe, Linear & Vercel** — https://www.pixeldarts.com/en/post/four-design-principles-behind-stripe-linear-and-vercel — what the benchmarks actually share.
- **Anthony Hobday — Visual design rules** — https://anthonyhobday.com/sideprojects/saferules/ — measurable verbatim rules: nested radius (inner = outer − gap), shadow blur = 2× distance, neutrals < 5% saturation, container brightness ≤ 7%/12%, body ≥ 16px, line length ~70, button h-padding 2× v-padding.
- **Erik Kennedy — 7 Rules for Gorgeous UI** — https://www.learnui.design/blog/7-rules-for-creating-gorgeous-ui-part-1.html — light-from-above shading, "double your whitespace."
- **Nielsen Norman Group** — https://www.nngroup.com — response-time thresholds (0.1s / 1s / 10s) behind the < 200ms interaction target; F-pattern.

**International craft & trend (the §8 [craft]/[trend] rows)**
- **nextage-tech (JP)** — https://nextage-tech.com/blog/2025/08/26/post-2198/ — yohaku whitespace ratios, premium genre archetypes.
- **metabole.studio (FR)** — https://metabole.studio/fr/blog/tendances-web-design-2026 — editorial layout, anti-bento, analog counter-signal *(trend forecast)*.
- **utsubo — Award-Winning Design Guide** — https://www.utsubo.com/blog/award-winning-website-design-guide — decoded Awwwards criteria + perf benchmarks (LCP < 1.5s, CLS < 0.05).
- **swissthemes — Swiss design for web** — https://swissthemes.design/insights/swiss-design-for-web-designers — 8pt grid tradition.
- **awdee.ru — Советы Бюро Горбунова** — https://awdee.ru/sovety-dizajn-byuro-gorbunova/ · **bureau.ru/soviet/ilyabirman** — density rule, rhythm, hierarchy.
- **UISDC 优设网 (CN)** — https://www.uisdc.com/ — CJK typography (line-height, measure, 思源黑体 baseline bug, 梦源黑体 fix), opacity-stacked text color.
- **人人都是产品经理 woshipm (CN)** — https://www.woshipm.com/pd/4325052.html — premium detail rules: color hierarchy, shadow types, border removal, 留白.
- **brunch.co.kr (KR)** — https://brunch.co.kr/@chulhochoiucj0/34 · https://brunch.co.kr/@sarayun/31 — Korean mobile typography, tight headings, type-as-image.
- **pabloalcalde.dev (ES)** — https://pabloalcalde.dev/blog/diseno-web-profesional-2025/ · **uraldes.com** — clamp() section padding, two-level shadow, variable-font hover.
- **designtec.com.br (PT-BR)** — https://designtec.com.br/ · **grafigata.com (IT)** · **a126.it (IT)** — unconventional color pairings, analog imperfection *(trend)*, motion-with-purpose.

---

*Reference version: global-design-skill v2.1.3 — `references/anti-slop-system.md`*
*Related: `references/sources.md` (the floor) · `skills/global-design/SKILL.md` → Banned Patterns · `checklists/global-design-review.md` → AI Slop Test · `references/inspiration-sites.md` → Category 12 · `references/aesthetic-recipes.md` (slop vs premium per trend) · `rules/00-escalation-protocol.md` (Macrostructure-First)*
