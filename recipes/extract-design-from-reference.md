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
5. RECONSTRUCT → notes a developer needs to rebuild it; what's load-bearing vs incidental
```

Convert every color to **OKLCH** (never store the raw hex you sampled — translate it). Snap spacing to the nearest 4px-grid step and say so.

---

## Step 3 — Emit the artifacts

Produce three outputs, not a prose summary:

1. **Filled `MASTER`** — fill `templates/specs/design-system-master.md` from the analysis: identity + Design Dials (inferred from the reference's variance/motion/density), OKLCH tokens, type, spacing/radii/shadow, component conventions, voice. This is the build's source of truth.
2. **DTCG tokens** — `design-tokens.json` in W3C DTCG format (`$value` / `$type`), matching `tokens/design-tokens.json`'s shape so it feeds Style Dictionary / Figma Variables / Tokens Studio directly.
3. **Component inventory** — table: component · observed variants/states · key visual props · usage context.

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
- **Live sites:** read `--*` custom properties before inferring anything — a site that ships tokens hands you the system for free. Dismiss cookie banners before screenshotting.
- **Figma:** variables are ground truth (✅); but cross-check declared variables against actual usage on the frame — declared ≠ applied (the same drift `rules/20` R7 guards against).

---

*Recipe version: global-design-skill v2.4.0 — `recipes/extract-design-from-reference.md`*
*Related: `templates/specs/design-system-master.md` (the artifact this fills), `tokens/design-tokens.json` (DTCG shape), `rules/20-rendered-verification.md` (R6 fidelity, R7 token drift), `agents/reference-hunter.md` (finding references), `references/color-alchemy.md` (hex → OKLCH translation), `rules/00-escalation-protocol.md` (Design Dials, macrostructure)*
