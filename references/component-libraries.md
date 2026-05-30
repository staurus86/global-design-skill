# Reference — Component Libraries, Templates & Assets

> Where to get **usable code and assets** — not inspiration to study, but components, blocks, and files you can drop into a build. The line that matters: **copy code only where the license permits it**. Everything below is free; the License column tells you what you can actually ship. When in doubt, open the repo's `LICENSE` and verify before committing client work.

---

## Licensing — read this first

| You want to… | Rule |
|---|---|
| Copy a component's code | OK **only** if the source is MIT/ISC/Apache or explicitly "open code / copy-paste". Verify per-component on "free + Pro" sites. |
| Copy a brand's UI 1:1 from a gallery | **No.** Galleries (`references/inspiration-sites.md`) are for *techniques* — grid, spacing, type, motion — never their logo, copy, photos, or identity. |
| Use an icon / font / illustration | Check its specific license (MIT, ISC, OFL, CC0). CC0 and MIT = commercial-safe, no attribution. |
| Ship a "Pro/Premium" block on a free tier | **No** unless you bought it. Many libraries gate templates/blocks behind Pro while the core components stay MIT. |

**Anti-slop note:** these libraries are a *starting skeleton*, not the final design. Shipping shadcn/ui or daisyUI with default tokens is exactly the generic AI look this skill exists to prevent. Re-token (OKLCH per `rules/04-color.md`), re-type (`rules/03-typography.md`), and break the default layout before delivery.

---

## Component libraries (copyable code)

### Tailwind + React — copy-paste / open code

| Library | License | Best for |
|---|---|---|
| **shadcn/ui** (ui.shadcn.com) | MIT (open code) | The default base: buttons, forms, cards, tables, dashboard UI. Owns the code — re-token freely. Best AI/vibe-coding starting point. |
| **Magic UI** (magicui.design) | MIT | Animated hero, marquee, Bento, motion sections (React + Tailwind + Motion). Pairs with shadcn. |
| **Aceternity UI** (ui.aceternity.com) | Free copy-paste; **verify per-component / Pro for commercial** | Wow-effects, animated cards, backgrounds, SaaS hero. |
| **Origin UI** (originui.com) | Open source copy-paste | Large set of app-UI components for fast interfaces. |
| **HyperUI** (hyperui.dev) | MIT | Landing, ecommerce, admin, forms, cards, pricing, nav blocks. |
| **Meraki UI** (merakiui.com) | MIT | Tailwind blocks with RTL, dark mode, responsive grids. |

### Tailwind — class-based / block libraries

| Library | License | Best for |
|---|---|---|
| **daisyUI** (daisyui.com) | MIT | Fast Tailwind styling via ready classes: button, card, modal, navbar. Commercial-safe. |
| **Preline UI** (preline.co) | Open source | Large Tailwind library: blocks, plugins, Figma design system. |
| **Flowbite** (flowbite.com) | MIT (code); **some templates are Pro** | Tailwind components, interactive elements, dark mode, Figma kit. |

### React component systems (full frameworks)

| Library | License | Best for |
|---|---|---|
| **Radix Themes / Primitives** (radix-ui.com) | MIT | Accessible, headless primitives + themed system. The a11y backbone under shadcn. |
| **Mantine** (mantine.dev) | MIT | 120+ components — admin, SaaS, forms, tables, dashboards, complex apps. |
| **MUI / Material UI** (mui.com) | MIT | Material interfaces, enterprise UI, forms, tables, panels. |
| **Chakra UI** (chakra-ui.com) | MIT | Clean accessible React UI, fast design systems. |
| **Ant Design** (ant.design) | MIT | Enterprise admin, CRM, dense tables, filters, complex forms. |

---

## Free templates & cloneables

Structure and composition you can take apart — study the layout, motion, and type, then rebuild on your own tokens.

| Source | What you get |
|---|---|
| **Figma Community Templates** (figma.com/templates) | 300+ free design/whiteboard templates — wireframes, UX maps, presentations. |
| **Framer Free Templates** (framer.com/marketplace/templates) | Free responsive site templates — dissect composition, motion, typography. |
| **Webflow Cloneables** (webflow.com/made-in-webflow/template-cloneable) | Community cloneable sites — clone and customize in Webflow. |
| **Untitled UI Free Figma Kit** (untitledui.com/free-figma-ui-kit) | Neutral UI kit: components, forms, layout systems. Good baseline to re-skin. |

---

## Free illustrations & generated SVG assets

| Source | License | Use |
|---|---|---|
| **unDraw** (undraw.co) | Free, no attribution, commercial | Recolorable SVG illustrations (set accent to match your palette). |
| **Open Doodles** (opendoodles.com) | CC0 / public domain | Loose hand-drawn illustrations, no credit required. |
| **Open Peeps** (openpeeps.com) | CC0 | Mix-and-match hand-drawn people; commercial-safe. |
| **Haikei** (haikei.app) | Free, no signup | Generate SVG backgrounds, waves, blobs, mesh gradients (export and tokenize). |

**Caution:** generic stock-style illustrations (especially the over-used flat "corporate Memphis" sets) are themselves an AI-slop tell. Prefer recolored line illustrations that match the brand, or none at all — see `checklists/global-design-review.md` → Banned Patterns.

---

*Reference version: global-design-skill v1.9.5 — `references/component-libraries.md`*
*Related: `references/inspiration-sites.md` (study, don't copy) · `references/sources.md` (design systems) · `rules/18-css-framework-selection.md` · `integrations/21st-dev/guide.md`*
