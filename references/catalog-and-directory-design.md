# Reference — Catalog & Directory Design (anti-slop)

> A catalog is the hardest page to make memorable: hundreds of similar items pull every design toward "a list of links". Removing AI-slop tells (default fonts, purple gradients, identical cards) makes a catalog *cleaner* — but clean is not the same as **having a design DNA**. A good directory is a *curated product with a point of view*, not an agregator. This reference covers the generative half of anti-slop for catalogs: a visual metaphor, selection scenarios, differentiated cards, distributed author curation, and a memorable hook.

**The shift this encodes:** defensive anti-slop removes what makes a page generic; **generative anti-slop adds what makes it *this* product.** A catalog that passes the AI Slop Test on tells can still be forgettable. Run the 10-second recall test (bottom) — if a visitor can't say what made *this* directory different, it isn't done.

**Load alongside:** `rules/00-escalation-protocol.md` (Macrostructure-First, Memorability Gate), `rules/13-saas-products.md`, `rules/11-data-tables.md`, `references/inspiration-sites.md`.

---

## 1. Pick a visual metaphor before layout

A directory needs an organising *idea*, not just a grid. The metaphor drives navigation, card shape, motion, and copy — and it is what a visitor remembers. Choose one and commit (don't blend).

| Metaphor | Reads as | Best when |
|---|---|---|
| **Cockpit / control panel** | A specialist's working dashboard — search, filters, status, quick access | Tools used daily by pros |
| **Market map** | Categories as zones/clusters of a territory you navigate | Many categories, exploration |
| **Tool radar** | Items placed by task / level / price / maturity on a 2-axis field | Helping users *choose*, not just browse |
| **Arsenal / stack** | A curated set of working modules, not a list | Strong author point of view |
| **Command center** | One surface: search + filters + saved + recent | Power users, return visits |

**Anti-slop test for the metaphor:** could a competitor's directory in the same niche have used it by default? If yes, push further. The metaphor should make *this* catalog recognisable.

---

## 2. Catalog macrostructures — don't default to the standard skeleton

The slop skeleton is `hero → stats → search → filters → categories → long catalog → author`. It works, but it doesn't break the template. Offer 2–3 alternatives and pick by audience (see `rules/00` Macrostructure-First):

- **Scenario-first** — "What do you need right now?" → 6–8 job buttons → results. The catalog is the *answer*, not the front door.
- **Map-first** — an interactive category map / radar above the fold; the long list is the drill-down.
- **Top-picks-first** — curated "best of" shelves (Top-10 for X) before the full base; the firehose is below for those who want it.
- **Mode-switch** — Beginner mode (guided, fewer items, annotated) vs Pro mode (dense, all items, keyboard-first).

A catalog should feel **designed as a tool for choosing**, not as a feed of links.

---

## 3. Design selection scenarios (JTBD), not just tag filters

Tag filters (`Free`, `RU`, `AI`, `Аналитика`) answer "what *kind* is it". Users arrive with a **job**: "what do I do next?". Design the jobs as first-class entry points, mapped to filter combinations underneath.

```
Tag filters (have):        Free · RU · AI · Beginners · Tech SEO · Analytics
Job scenarios (add):       "Quickly check a site"      → audit + free + fast
                           "Build a keyword set"        → semantics + RU
                           "Find indexing problems"     → tech SEO + crawl
                           "Pick a paid all-in-one"     → suite + paid
                           "Free tools for a beginner"  → free + beginner
                           "AI / GEO / AEO tooling"     → ai + geo
                           "Russian alternatives to X"  → ru + alternative-to
```

Each job is a labelled shortcut (a chip, a card, a row) that pre-applies the right filters. Jobs convert a browser into a chooser.

---

## 4. Card differentiation matrix — kill the visual monotony of N identical cards

Identical icon+title+description cards repeated 393× are visual noise (Banned Pattern). Differentiate cards with *useful* signals, not decoration. Not every card needs every field — tier them.

| Signal | Example | Why it helps choosing |
|---|---|---|
| **Commercial status** | Free / Freemium / Paid / Enterprise | The first filter in a buyer's head |
| **Region** | RU / EN / Global | Critical for localised work |
| **Authority** | Official / Community | Trust |
| **Level** | Beginner / Specialist / Enterprise | Sets expectation of effort |
| **Best for** | "large sites", "quick checks" | The job it wins at |
| **Alternative to** | "RU alternative to Ahrefs" | Anchors the unknown to the known |
| **Mini-ratings** | speed · price · complexity · usefulness | Scannable comparison |
| **Freshness** | updated / verified date | Proves the catalog is alive |
| **Author note** | see §5 | Turns aggregation into curation |

Keep colour for **one** decisive signal (commercial status); render the rest quiet (`rules/04` R7). Use tiers — featured/recommended cards carry more signals; the long tail stays minimal.

---

## 5. Author curation layer — distribute the expertise into the catalog

An "About the author" block at the bottom proves *who*. But the thing that makes a directory a *curated tool* (not an aggregator) is the author's opinion **next to the items themselves**:

```
"I use this daily"        "Best for large sites"     "Careful — expensive"
"Great for beginners"     "Strong RU alternative"    "I run this in audits"
"Beats its peers at X"    "Overkill for small sites"
```

A short, honest author note on the *important* cards (not all) is the single highest-leverage anti-slop move for a catalog: no AI-generated aggregator has a real person's working opinion. Pair with a small author chip near the top (§7) so trust is established before the scroll, with the full bio at the bottom.

---

## 6. Show the selection methodology

"All links checked and regularly updated" is a claim. A short, explicit method turns it into trust and removes the "just a list" feeling:

> **How tools get into this catalog:** live-site checked · free/paid verified · RU/EN tagged · sorted by job · dead services removed · base dated on update · only what a working SEO/marketer would actually use.

One compact block. It signals editorial standards and a human behind the curation.

---

## 7. Entry points for a large base

A 300+ item base needs fast on-ramps so a normal visitor isn't forced to scroll a firehose:

- **Top-N shelves** at the top: Top-10 for SEO · Top free · Top for tech audit · Top for beginners · Top AI · Top RU · "bookmark these first".
- **Author chip** near the hero: *"Curated by [Name], Technical SEO / AI — tools I use or vet in real work."* (full bio stays at the bottom).
- **Sticky finder** — search + active filters persist on scroll for a tall page.

---

## 8. Save / share / export — turn a catalog into a product

A reference people *return to and send* needs lightweight portability. These also create the memorability and shareability the page otherwise lacks:

- Copy link to a **category** or a **filtered view** (URL carries the state).
- Copy / share a **curated set** ("my stack").
- Export the visible list to **CSV / Markdown**.
- "Open all tools in this category."
- "Suggest a tool" (keeps the base growing, invites the audience in).

---

## 9. The 10-second recall test (memorability gate)

After the build, the gate every catalog must pass:

> Show the page for 10 seconds, then hide it. Can the viewer say **what made *this* directory different** from any other list of tools — in one sentence?

If the answer is only "a catalog of SEO tools", it failed memorability. A pass sounds like: "the one with the *tool radar* / the *author's real notes* / the *job-first finder* / *beginner-vs-pro modes*." Pick the hook in §1 and make it unmistakable.

**Catalog-specific scorecard (rate each /10):** usefulness · IA · anti-slop tells removed · **selection scenarios** · **card differentiation** · **author curation in-catalog** · **memorability / design DNA** · save-share. A catalog can score high on the first three and still be forgettable — the last four are where generative anti-slop lives.

---

*Reference version: global-design-skill v1.9.9 — `references/catalog-and-directory-design.md`*
*Related: `rules/00-escalation-protocol.md` (Macrostructure-First + Memorability Gate), `rules/11-data-tables.md`, `rules/13-saas-products.md`, `checklists/global-design-review.md` (AI Slop Test), `references/behavioral-design.md`*
