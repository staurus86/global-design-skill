# Demo Gallery — Design Spec
**Date:** 2026-05-25  
**Project:** global-design-skill  
**Repo:** https://github.com/staurus86/global-design-skill  

---

## 1. Problem Definition

**What:** A Demo Gallery showcasing real-world UI redesigns produced using the global-design-skill system.

**Who:** Developers and teams evaluating whether to adopt the skill. They need to see concrete output quality — not abstract principles.

**Business goal:** Every visitor should leave with "this skill actually works on real interfaces I recognise." The gallery is the primary proof of capability.

**Success metric:** A first-time visitor can open any demo, see the before/after in under 5 seconds, and immediately understand what changed and why.

**Scope:**
- 8 demo files (3 waves) + 1 gallery index page
- Wave 1 (this spec): Hacker News story item, Stack Overflow question card, GitHub PR/Issue card
- Wave 2: npm package card, MDN API block, Product Hunt listing
- Wave 3: Can I Use table, Dev.to article card
- All output: self-contained HTML files, no build step, GitHub Pages ready

---

## 2. File Structure

```
global-design-skill/
  demo/
    index.html          ← Gallery page (GitHub Pages entry point)
    hacker-news.html    ← Wave 1
    stack-overflow.html ← Wave 1
    github-pr.html      ← Wave 1
    npm-package.html    ← Wave 2
    mdn-api.html        ← Wave 2
    product-hunt.html   ← Wave 2
    caniuse-table.html  ← Wave 3
    devto-card.html     ← Wave 3
```

No build tooling. Each file is self-contained HTML+CSS+JS. No external dependencies beyond system fonts.

---

## 3. Demo File Format (applies to all 8 files)

### Structure (top to bottom)

```
[Header]          site name · component type · link back to gallery
[Toggle bar]      ← Before  |  After →   (default: After)
[Component]       live, interactive, fully styled
[Skeleton state]  shimmer skeleton matching component layout
[Change log]      before/after table with principle references
[Token legend]    CSS custom properties used in this demo
```

### Toggle behaviour

- Default state: **After** (shows the redesign — visitor sees the best version first, Before is the contrast, not the hero)
- Clicking "Before" renders the original component recreation (faithful to the original, not a screenshot)
- Both states are rendered live HTML — no images
- Toggle is keyboard accessible: `Tab` to focus, `Space`/`Enter` to switch
- `aria-live="polite"` region wraps the component for screen reader announcements
- Transition: `opacity` + `transform` crossfade, 200ms `cubic-bezier(0.16, 1, 0.3, 1)`
- `prefers-reduced-motion`: transition disabled, instant swap

### Skeleton state

- Matches the **After** (redesigned) component layout exactly
- CSS shimmer animation: `background-position` sweep, 1.5s, `linear` — shimmer is functional, not decorative; `ease-in-out` is banned per §8
- `prefers-reduced-motion`: static flat colour, no animation
- Labelled with `aria-busy="true"` and `aria-label="Loading [component name]"`

### Change log format

```markdown
| Change | Before | After | Principle |
|--------|--------|-------|-----------|
| Image position | Inside body block | Fixed 16:9 at top | Hierarchy §2, CLS Gate 7 |
| CTA | Plain text link | Pill button, accent fill | Gate 4 — all states |
...
```

### Token legend

Table of every CSS custom property used, with its computed OKLCH value and semantic purpose. Light and dark mode columns.

---

## 4. Design Tokens (shared across all demos)

All demos embed the same token block inline (no external CSS, no build step). This means tokens are duplicated across 8 files — an explicit trade-off for self-containment.

**Token update protocol:** `demo/tokens.css` is the single source of truth (not loaded by browsers — exists only as a reference). To update a token across all files, run:
```bash
# Example: update --color-accent in all demo files
grep -rl "\-\-color-accent:" demo/ | xargs sed -i 's/--color-accent: oklch(52% 0.20 258)/--color-accent: oklch(NEW)/g'
```
Document this in `demo/README.md`. Never edit token values in individual demo files directly.

### Colour — OKLCH

```css
/* Light */
--color-bg:             oklch(96% 0.004 258)
--color-surface:        oklch(100% 0 0)
--color-border:         oklch(90% 0.006 258)
--color-text:           oklch(17% 0.012 258)
--color-text-secondary: oklch(42% 0.012 258)
--color-text-muted:     oklch(60% 0.008 258)
--color-accent:         oklch(52% 0.20 258)   /* committed single hue */
--color-accent-hover:   oklch(45% 0.21 258)

/* Dark — via @media (prefers-color-scheme: dark) */
--color-bg:             oklch(13% 0.010 258)
--color-surface:        oklch(17% 0.010 258)
--color-text:           oklch(94% 0.004 258)
--color-accent:         oklch(65% 0.20 258)
```

### Spacing — 4px grid

`--space-1: 4px` through `--space-10: 40px`

### Typography — fixed sizes (no `clamp()`)

1px fluid ranges are indistinguishable from fixed values. Use fixed sizes; reserve `clamp()` for display headings with genuine viewport dependence.

```css
--text-xs:   11px
--text-sm:   13px
--text-base: 15px
--text-md:   17px
--text-lg:   19px
--text-xl:   clamp(20px, 2.3vw + 0.5rem, 26px)   /* display size — real range */
--text-2xl:  clamp(26px, 3.5vw + 0.5rem, 36px)
```

### Motion

```css
--ease-out:    cubic-bezier(0.16, 1, 0.3, 1)
--ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1)
--t-fast: 140ms
--t-base: 210ms
--t-slow: 320ms
```

---

## 5. Gallery Page (index.html)

### Layout

```
[Nav]     logo "global-design-skill" · wave filter tabs
[Hero]    dark bg · "Demo Gallery" · tagline
[Grid]    3-column card grid (1-col on mobile)
[Footer]  link to repo · MIT licence
```

### Demo card (within grid)

```
[Thumbnail]   split 50/50 — left: Before (red tint), right: After (green tint)
              Centre of each half: site emoji (32px) + component name (11px, bold)
              Without this, all 8 cards are visually identical colour blocks
[Info]        site emoji + name · component type · difficulty badge
[CTA]         "View demo →" link
```

### Filter tabs

"All" | "Wave 1" | "Wave 2" | "Wave 3"  
Client-side JS filter — no page reload. Cards not matching the active filter get `opacity: 0; transform: scale(0.96); pointer-events: none` with `transition: opacity 150ms, transform 150ms` — not `display: none` (would block transition).

### Difficulty badges

- `WOW` — amber · Hacker News, Stack Overflow
- `High` — green · GitHub, npm, Product Hunt
- `Deep` — indigo · MDN, Can I Use, Dev.to

### Responsive

- 390px: 1-column grid, hero text clamps down
- 768px: 2-column grid
- 1280px: 3-column grid
- `gap` scales with viewport via `clamp()`

---

## 6. Quality Gates per Demo File

Every demo file must pass before it ships:

| Gate | Requirement |
|------|-------------|
| **Toggle** | Before and After both render correctly. Toggle is keyboard accessible. `aria-live` present. |
| **Skeleton** | Matches After layout. Shimmer disabled with `prefers-reduced-motion`. |
| **Dark mode** | Both Before and After render in dark mode without broken contrast. |
| **Responsive** | No horizontal overflow at 390px, 768px, 1280px. |
| **Accessibility** | All interactive elements have `aria-label`. Focus ring visible. Touch targets ≥ 44×44px. |
| **Performance** | No layout shift during Before/After toggle. `aspect-ratio` locked on component container so height doesn't jump between states. |
| **Change log** | Every visible change is documented with the principle or gate it addresses. |

---

## 7. Implementation Order

### Step 1 — Shared token block
Extract the common CSS custom properties into a `<style>` comment block used as a copy-paste template for all 8 files.

### Step 2 — Wave 1 demos (3 files)

**2a. hacker-news.html**
- Before: faithful recreation of HN story item as of **2026-05-25** snapshot (black text, Times New Roman, orange link, grey meta)
- After: modern redesign — card surface, vote widget, domain pill, time, comment count, share
- Key challenge: maximum contrast with minimum components

**2b. stack-overflow.html**
- Before: faithful recreation of SO question card (vote widget, tags, user card, answer count badge)
- After: redesigned with improved information hierarchy — vote widget → title → tags → meta row → answer badge
- Key challenge: dense data without visual noise

**2c. github-pr.html**
- Before: faithful recreation of GitHub PR list item (status badge, title, meta, label chips, assignee avatars)
- After: redesigned with clearer status visibility, label hierarchy, and action affordance
- Key challenge: status communication

### Step 3 — Gallery page (index.html)
Built after Wave 1 is complete. Thumbnails are colour-block splits (50/50, red-tint Before / green-tint After) with site emoji + component name centred in each half — no screenshots or iframes required.

### Step 4 — Enable GitHub Pages
In repo Settings → Pages → Source: deploy from branch `master`, folder `/demo`. Verify `demo/index.html` is reachable at the published URL before marking Wave 1 done. Add the Pages URL to `README.md`.

### Step 5 — Wave 2 and Wave 3
Follow same format. Each gets its own spec addendum if the component type requires it.

---

## 8. Do Not

- Use external CSS frameworks (Tailwind, Bootstrap) — tokens only
- Use images for Before/After — both states must be live HTML
- Use `ease-in-out` on transitions — use named bezier curves
- Use `100vh` — use `100dvh`
- Use raw hex/rgb colour values — OKLCH tokens only
- Use `gradient text` (background-clip: text) — banned pattern
- Ship a demo without a change log
- Ship a demo without testing dark mode and 390px viewport

---

## 9. Success Criteria

- [ ] All 8 demo files open without errors in Chrome, Firefox, Safari
- [ ] Toggle works keyboard-only on all demos
- [ ] Dark mode renders correctly on all demos
- [ ] No horizontal scroll at 390px on any demo or gallery page
- [ ] Gallery page filter works without JS errors
- [ ] Every change log entry references a specific principle or quality gate
- [ ] GitHub Pages configured (Settings → Pages → branch `master`, folder `/demo`)
- [ ] README links to the live GitHub Pages URL
- [ ] `demo/tokens.css` exists as the token source of truth
- [ ] `demo/README.md` documents the token update protocol
