# Reference — Aesthetic Archetypes in the Wild

> Real examples of each aesthetic archetype (A–H). Use when a client needs a direction, or when choosing which archetype to commit to. Each archetype includes 5–8 live sites, their defining visual signatures, and what makes them a strong reference for that archetype.

---

## Archetype A — Ethereal Black

> OLED dark background, electric accent, spring physics, blur reveals. Default for SaaS, AI tools, developer products.

**Signature visual traits:**
- Background: `oklch(8% 0.01 250)` — nearly OLED black with a blue hue tint
- One electric accent (electric blue, green, or neon) occupying ≤15% surface
- White hairlines (`oklch(100% 0 0 / 0.08)`) as borders
- Motion: spring-physics reveals, blur-in transitions
- Mono or semibold grotesque for UI; Display face only for hero

**Reference sites:**

| Site | URL | What makes it Ethereal Black |
|---|---|---|
| **Raycast** | raycast.com | The canonical example — OLED black, command palette UX, one purple accent, spring physics |
| **Linear** | linear.app | Dense OLED dark UI, tight type, keyboard-first, hairline grid lines |
| **Vercel** | vercel.com | Dark hero, electric accent strip, clean code-forward layout |
| **Resend** | resend.com | Minimal developer tool — black canvas, one color, code blocks |
| **Supabase** | supabase.com | Dark dashboard, green accent, developer aesthetic |
| **Liveblocks** | liveblocks.io | Collaborative realtime landing — dark, subtle gradient glows, no clutter |
| **Planetscale** | planetscale.com | Database product — dark, terminal aesthetic, schema diagrams |
| **Clerk** | clerk.com | Dark auth component library, system-level dark design |

**What to study specifically:**
- Raycast: how they use negative space on dark backgrounds; how the spotlight pattern creates depth without gradients
- Linear: information density in dark mode — how to keep tables readable without using borders everywhere
- Vercel: CLI-first product storytelling — code on the left, result on the right

---

## Archetype B — Editorial Luxury

> Warm cream or deep espresso surfaces, variable serif display fonts, slow parallax, mask reveals. For agencies, fashion, premium SaaS.

**Signature visual traits:**
- Background: `oklch(97% 0.008 80)` — warm cream, never pure white
- Display: Variable serif with optical size variation (Playfair, Editorial New, Cormorant)
- Gold or terracotta accent; deep espresso (#1C1008 equivalent) for text
- Motion: slow parallax (0.3–0.5 speed ratio), image mask reveals on scroll, curtain transitions
- Generous whitespace — 160–240px section padding

**Reference sites:**

| Site | URL | What makes it Editorial Luxury |
|---|---|---|
| **Craft** | craft.do | Warm cream, italic serif display, premium positioning |
| **Framer** | framer.com | Meta-editorial — design tool marketing itself with editorial elegance |
| **Basement Studio** | basement.studio | Agency portfolio — large serif, heavy whitespace, typographic identity |
| **Stripe** (marketing) | stripe.com | Not dark — clean, premium, editorial form hierarchy |
| **Arc Browser** | arc.net | Personality-driven, editorial typography, personality above features |
| **Pitch** | pitch.com | Presentation tool — editorial hierarchy, warm tones |
| **Loom** | loom.com | Consumer-friendly, editorial warmth, friendly but premium |
| **Cron** (now Notion Calendar) | cron.com (archived) | Calendar product — editorial, warm, precise typography |

**What to study specifically:**
- Craft.do: how they use a single serif typeface to carry the entire brand identity
- Basement Studio: the ratio between text size and whitespace — at what point does whitespace become the composition
- Arc Browser: how copy-driven design works when the typography IS the decoration

---

## Archetype C — Cyberbrutalism

> Raw black borders, no radius, high contrast, snap scroll, glitch effects. For portfolios, creative studios, experimental startups.

**Signature visual traits:**
- No border-radius (or extreme: 0px on containers, 999px on pills — nothing in between)
- Thick black borders (2–4px solid black)
- High-contrast color fills: neon yellow, hot pink, electric green — as backgrounds, not accents
- Motion: glitch/scramble text reveals, ASCII typeouts, snap scroll sections
- Font: Monument Extended, Neue Haas, or bold system fonts — heavy weight at large sizes

**Reference sites:**

| Site | URL | What makes it Cyberbrutalism |
|---|---|---|
| **Brutalist Websites** | brutalistwebsites.com | Gallery of the archetype itself — study the taxonomy |
| **Sheet2Site** | sheet2site.com | No-frills raw data product presentation |
| **Figma** (old identity) | — | Former brutalist elements before softening |
| **Cargo Collective** | cargo.site | Creative portfolio builder — raw, expressive typography |
| **mmm.page** | mmm.page | Brutalist creative tool for Gen Z |
| **Lunchbox** | lunchbox.io | Game development studio — raw, high contrast |
| **Read.cv** | read.cv | Stripped resume format — deliberate rawness as sophistication |
| **Poolside FM** | poolside.fm | Retro brutalism — synthwave meets 80s computing aesthetic |

**What to study specifically:**
- Brutalistwebsites.com: how brutalism ranges from functional minimalism to deliberate chaos
- Read.cv: how brutalist restraint reads as intellectual seriousness
- Poolside FM: how retro computing aesthetics translate to modern UI

---

## Archetype D — Organic Softness

> Off-white or sage, Fraunces variable serif, float animations, morphing blobs. For health, consumer apps, nature brands.

**Signature visual traits:**
- Background: warm off-white `oklch(97% 0.012 80)`, sage `oklch(72% 0.06 155)`, or terracotta
- Fraunces (variable) as display — optical size axis creates warmth at large sizes
- Rounded corners: `--radius-xl: 24px` to `--radius-full: 9999px`
- Motion: float animations (3–6s ease-in-out loop), soft morph transitions, no snappy springs
- No sharp edges anywhere — even data tables use subtle row backgrounds instead of borders

**Reference sites:**

| Site | URL | What makes it Organic Softness |
|---|---|---|
| **Superhuman** | superhuman.com | Product warmth + speed paradox — organic but performance-obsessed |
| **Calm** | calm.com | Canonical soft design — sage gradients, breathable layout |
| **Notion** | notion.so | Minimal organic — paper white, calm hierarchy, no decoration |
| **Monzo** | monzo.com | Consumer fintech — bright coral, rounded, friendly |
| **Headspace** | headspace.com | Illustration + type — round, playful, accessible |
| **Readymag** | readymag.com | Creative publishing — soft editorial, organic layout |
| **Maggie Appleton** | maggieappleton.com | Personal site — illustration + type, knowledge garden aesthetic |
| **Things 3** | culturedcode.com/things | Task app landing — paper white, warm, precision in simplicity |

**What to study specifically:**
- Calm.com: how to use soft gradients without making them look like the banned purple-indigo default
- Notion.so: how organic softness works at high information density — they never sacrifice clarity for warmth
- Maggie Appleton: how illustration integrates with typography instead of competing with it

---

## Archetype E — Volumetric Glass

> Midnight background, frosted glass layers, depth blur parallax. For premium SaaS, fintech, crypto, luxury tech.

**Signature visual traits:**
- Background: `oklch(12% 0.02 260)` — deep midnight blue-black
- Glass cards: `backdrop-filter: blur(24px) saturate(180%)` + `border: 1px solid oklch(100% 0 0 / 0.12)`
- Layered depth: 3+ z-levels visible simultaneously (background / glass midground / foreground elements)
- Motion: depth blur on entry, parallax scrolling between layers, 3D card tilt on hover
- Specular highlights: `inset 0 1px 0 oklch(100% 0 0 / 0.18)` on top edge of glass elements

**Reference sites:**

| Site | URL | What makes it Volumetric Glass |
|---|---|---|
| **Apple** | apple.com | Product pages — glass depth, photorealistic product renders, spatial hierarchy |
| **Stripe** (dashboard) | stripe.com/dashboard | Glass card system in dark mode, layered UI depth |
| **Coinbase** | coinbase.com | Crypto fintech — dark, glass panels, subtle gradient depth |
| **Gemini** | gemini.com | Crypto exchange — midnight dark, glass table rows |
| **Robinhood** | robinhood.com | Consumer fintech — dark, glass cards, premium positioning |
| **Linear** (pricing) | linear.app/pricing | Glass card isolation within dark context |
| **Liveblocks** | liveblocks.io | Collaboration SaaS — layered glass sections |
| **Mux** | mux.com | Video API — dark volumetric, glass dashboard previews |

**What to study specifically:**
- Apple product pages: how depth is created without actual 3D — through shadow size, blur intensity, and vertical offset
- Stripe dashboard: glass panel hierarchy — when to use glass vs. opaque cards for information grouping
- Coinbase: how glass handles interactive states (hover, active, selected) without losing the depth illusion

---

## Archetype F — Neo-Maximalism

> Full chromatic palette, kinetic marquees, grid chaos, drag pan. For art, music events, fashion.

**Signature visual traits:**
- Multiple saturated colors — no neutral base; color AS surface
- Typography: expressive display faces with extreme scale contrast (10px caption next to 200px display)
- Motion: velocity-linked marquees, infinite scroll columns, mouse-track parallax
- Grid: intentionally broken — elements overlap, extend past bounds, ignore the baseline
- Font: VTC or custom display, typically with multiple fonts in one screen

**Reference sites:**

| Site | URL | What makes it Neo-Maximalism |
|---|---|---|
| **Pentagram** | pentagram.com | Design firm — typographic chaos elevated to brand identity |
| **Wieden + Kennedy** | wk.com | Agency site — full bleed, grid breaking, expressive hierarchy |
| **SIX Agency** | six.agency | Interactive — color fields, bold typography, kinetic |
| **Cargo Collective** | cargo.site | Creative expression platform — maximalist templates |
| **Virgil Abloh** (archive) | virgilabloh.com | Fashion + art — maximalist typographic collage |
| **Dazed Digital** | dazeddigital.com | Fashion/art magazine — dense, kinetic, colorful |
| **I Love New York** (new identity) | — | Rebranded state identity — maximalist bold typography |
| **Figma Config** | config.figma.com | Conference site — festival-style, color, energy |

**What to study specifically:**
- Pentagram: how maximalist typographic design stays legible — the role of contrast in chaos
- Figma Config: how corporate brands temporarily enter maximalism for events — the line between brand and festival
- SIX Agency: interactive maximalism — how hover/scroll reveals work in grid-chaos layouts

---

## Archetype G — Post-Digital Terminal

> Phosphor green or amber on near-black, CRT scanlines, ASCII decode, terminal blink. For dev tools, hacker culture, indie products.

**Signature visual traits:**
- Background: `#0A0A0A` (near-black, not OLED black)
- Text: phosphor green `#4AF626` or amber `#FFB000` — never white as primary text
- Font: VT323, Courier Prime, or system mono — never a grotesque
- Motion: CRT scanline overlay, character-by-character typeout, blinking cursor, ASCII art reveals
- UI: no gradients, no shadows — flat, terminal-accurate

**Reference sites:**

| Site | URL | What makes it Post-Digital Terminal |
|---|---|---|
| **Poolside FM** | poolside.fm | Retro computing aesthetic — amber on dark, pixel UI |
| **Monkeytype** | monkeytype.com | Typing speed tool — terminal-first, single page, pure function |
| **Hackaday** | hackaday.com | Hardware hacking — raw terminal aesthetic, content-first |
| **RetroAchievements** | retroachievements.org | Gaming + retro computing aesthetic |
| **Zellij** | zellij.dev | Terminal multiplexer docs — lives in its own aesthetic |
| **Charm** | charm.sh | Developer CLI tools — terminal aesthetic on the web |
| **Helix** (editor) | helix-editor.com | Modal text editor — terminal-native design language |
| **Ghostty** | ghostty.org | Terminal emulator landing — lives in the terminal archetype |

**What to study specifically:**
- Charm.sh: how a terminal-aesthetic site stays usable for non-hackers — the accessibility of the archetype
- Monkeytype: function-first terminal design — zero decoration, pure information
- Poolside FM: how retro computing aesthetics work as personality, not just nostalgia

---

## Archetype H — Spatial Luxury

> Single neutral + deep photorealistic shadow depth, 3D orbit, HDRI lighting. For product, watches, automotive, premium hardware.

**Signature visual traits:**
- Single neutral base — warm cream or cool white, no color distractions
- Product renders/photos as primary visual — photorealistic, with real shadow depth
- Typography: Cinzel (classical), Cormorant Garamond (ultra-thin), or geometric precision sans
- Motion: 3D product orbit on scroll, camera dolly moves, depth-of-field blur transitions
- No icons, no decorative illustrations — the product IS the decoration

**Reference sites:**

| Site | URL | What makes it Spatial Luxury |
|---|---|---|
| **Apple** | apple.com/mac | Mac lineup pages — single product hero, depth-of-field, orbital 3D |
| **Porsche** | porsche.com | Automotive — single car on neutral, camera orbit, HDRI lighting |
| **Bang & Olufsen** | bang-olufsen.com | Audio hardware — minimal, spatial, product-centered |
| **AirPods Pro** | apple.com/airpods-pro | 3D product, scroll-driven explode animation, spatial depth |
| **Ferrari** | ferrari.com | Automotive luxury — spatial car photography, extreme depth |
| **Rolex** | rolex.com | Watch — extreme photo quality, single product on cream |
| **Teenage Engineering** | teenage.engineering | Hardware products — neutral canvas, product as art object |
| **Nothing** | nothing.tech | Consumer hardware — spatial product renders, clean neutral |

**What to study specifically:**
- Teenage Engineering: how to present hardware products on the web without 3D — photography quality and styling as the differentiator
- Nothing: the "product as primary decoration" principle — when you have a great-looking product, everything else moves to the background
- Apple AirPods Pro page: scroll-driven 3D — how to use CSS `perspective` + scroll position to create orbital motion

---

## Choosing Between Archetypes

Use this decision matrix as a starting point — always override with brand context:

| Product/Context | Default archetype | Why |
|---|---|---|
| AI/ML SaaS | A — Ethereal Black | OLED dark communicates technical depth and focus |
| Developer tools | A or G | Dark for productivity; terminal for CLI-first |
| Consumer finance | E — Volumetric Glass | Premium, trustworthy depth without feeling cold |
| Health/wellness app | D — Organic Softness | Warmth reduces anxiety; soft signals safety |
| Fashion/art | F — Neo-Maximalism | Expression IS the product |
| Premium hardware | H — Spatial Luxury | Product renders carry the story |
| Agency/portfolio | B or C | Editorial for classic sophistication; Cyberbrutalism for edgy |
| Marketing landing | B — Editorial Luxury | Converts better — premium without alienating |

---

## Anti-Pattern: Archetype Mixing

Do NOT mix archetypes unless you have a clear conceptual reason.

**Bad:** Ethereal Black hero + Organic Softness body sections. Looks inconsistent.
**Bad:** Volumetric Glass nav + Post-Digital Terminal content. Tonal mismatch.

**OK (with intent):**
- Spatial Luxury product visual inside an Ethereal Black dashboard (the product photo as the hero within the tool)
- Editorial Luxury landing page → Ethereal Black dashboard (marketing vs. product intentional contrast)

The rule: mixing is intentional contrast between modes (marketing vs. app), never accidental blending within a single view.

---

*Reference version: global-design-skill v1.0 — `references/aesthetic-archetypes.md`*  
*Updated: 2026-05-20*  
*Related: `agents/reference-hunter.md`, `references/inspiration-sites.md`, `skills/global-design/SKILL.md`*
