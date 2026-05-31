# Reference — Named Aesthetic Recipes (Composition Layer)

> Trendy aesthetics are *compositions* of techniques, not new techniques. This file maps a named look to the existing technique recipes that build it, plus the accessibility guardrails that keep it shippable and when to **not** use it. The CSS lives in `references/visual-effects.md`; this file is the assembly + judgment layer.
>
> **Excluded by design:** neumorphism and claymorphism. Both depend on low-contrast tonal shadows that routinely fail WCAG 1.4.3 (text) and 1.4.11 (UI contrast) and read as 2020-era slop. If a client insists, treat it as a Level-1 accent on a single non-critical surface — never the system. See Banned Patterns in `skills/global-design/SKILL.md`.

---

## How to use this file

1. Pick the named look (or let the brief imply one).
2. Build it from the linked technique sections — don't reinvent the CSS.
3. Clear the **guardrails** before shipping. They are not optional; they are what separates a premium execution from the slop version of the same trend.
4. Read **Skip when** — most failures are using the look in the wrong context, not getting the CSS wrong.

---

## Glassmorphism

**Essence:** Frosted, translucent surfaces floating over a colored/imagery background; depth through blur, not shadow.

**Compose from:**
- `references/visual-effects.md` → **Glassmorphism (correct implementation)** — `backdrop-filter: blur()` + saturate + 1px inner highlight
- A non-flat background to refract — pair with **Aurora / Gradient Mesh** or an image
- `references/visual-effects.md` → **Inner Highlight (Specular)** for the glass edge

**Guardrails:**
- Text on glass must hit 4.5:1 against the *blurred-through* worst-case pixel, not the card fill — sample it (`rules/19-contrast-standards.md`). Add a semi-opaque solid layer under text if it fails.
- Provide a `@supports not (backdrop-filter: blur(1px))` fallback to a solid surface.
- `backdrop-filter` is GPU-expensive — cap the number of simultaneous glass layers (≤ 3 in viewport); never animate the blur radius.

**Skip when:** dense dashboards, data tables, long-form reading (legibility cost), or any low-end-device target.

---

## Aurora / Gradient Mesh

**Essence:** Slow, breathing color fields — soft blobs of accent hue drifting behind content. Atmosphere without imagery.

**Compose from:**
- `references/visual-effects.md` → **Aurora / Gradient Mesh** + **Floating Blobs**
- Keep it behind a contrast-safe content layer (often a glass or solid panel)

**Guardrails:**
- Motion must respect `prefers-reduced-motion` — freeze the blobs to a static gradient (`rules/05-animation.md`).
- Content sits on its own layer with verified contrast; never put body text directly on the moving mesh.
- Animate `transform`/`opacity` only — never `background-position` on large areas (paint cost, jank).
- Accent occupies ≤ 15% perceived surface; mesh is ambient, not the subject (`rules/04-color.md`).

**Skip when:** trust-critical/enterprise (reads as consumer/playful), or when the mesh competes with a hero product shot.

---

## OLED-Luxury (Dark + Metallic Accent)

**Essence:** Near-black canvas, a single warm-metal accent (gold/champagne/bronze), spotlight depth, generous space. The premium end of dark mode.

**Compose from:**
- `references/aesthetic-archetypes.md` → **Archetype A (Ethereal Black)** is the foundation; OLED-luxury is its warm-accent variant
- `references/visual-effects.md` → **Spotlight / Cursor Glow** for depth without gradients
- Editorial type from `rules/03-typography.md` (variable serif display)

**Guardrails:**
- Background is tinted near-black (`oklch(8% 0.01 h)`), never pure `#000` (`rules/04`).
- Body text contrast ≤ ~15:1 — no pure white on black (halation/eye strain, `rules/19` R-dark).
- The metal accent is a *highlight*, ≤ 10% surface; gold on black still needs 4.5:1 for any text use.
- One accent only. Gold **and** neon **and** gradient = costume jewelry, not luxury.

**Skip when:** high-density data UI (dark luxury wastes the space it needs), or budget/value positioning (the look signals expensive).

---

## Brutalism (Structured)

**Essence:** Raw, high-contrast, grid-breaking — thick borders, hard shadows, system/mono type, unapologetic blocks. Personality over polish.

**Compose from:**
- Thick borders (3–4px), hard offset shadows (`box-shadow: 6px 6px 0` solid, no blur)
- Mono or grotesque type at extreme scale contrast (`rules/03-typography.md`)
- Deliberate asymmetry / broken grid (`rules/02-layout-and-grid.md`)

**Guardrails:**
- Brutalism is not an excuse to fail a11y: contrast, focus-visible, touch targets, and reading order all still apply (`rules/07-accessibility.md`). Raw ≠ inaccessible.
- "Grid-breaking" must still reflow without horizontal overflow at 390px (`rules/09-responsive.md`).
- Keep the system coherent — one border weight, one shadow offset, one type pair. Random ≠ brutalist; *rigorously raw* is the look.

**Skip when:** conversion-critical funnels, trust-sensitive (finance/health), or audiences that read "broken" as "broken."

---

## Related Files

- `references/visual-effects.md` — the technique CSS these looks are built from
- `references/aesthetic-archetypes.md` — curated archetypes A–H with reference sites
- `rules/00-escalation-protocol.md` — `DESIGN_VARIANCE` dial + Design Direction Fallback
- `rules/19-contrast-standards.md` — the contrast gate every look above must pass
- `rules/04-color.md` — accent ≤ 15%, tinted neutrals, no pure black/white
