# Example — SaaS Hero Redesign (Landing Page)

> **Before:** Centered hero with H1 + subtitle + two equal blue buttons. The banned default layout.  
> **After:** Left-aligned editorial hero with eyebrow, expressive typeface, single primary CTA, and a product screenshot on the right.

---

## Before

```html
<!-- The banned default — centered, generic, interchangeable -->
<section style="text-align: center; padding: 100px 20px; background: linear-gradient(135deg, #6366f1, #8b5cf6);">
  <h1 style="font-size: 48px; color: white; font-family: Inter, sans-serif; font-weight: 700;">
    Ship faster with our platform
  </h1>
  <p style="font-size: 18px; color: rgba(255,255,255,0.8); margin: 20px auto; max-width: 600px;">
    The all-in-one deployment platform that helps teams build, deploy, and scale.
    Seamless integration. No hassle.
  </p>
  <div style="display: flex; gap: 12px; justify-content: center; margin-top: 32px;">
    <button style="background: white; color: #6366f1; padding: 12px 24px; border-radius: 8px; font-weight: 600; border: none;">
      Get Started
    </button>
    <button style="background: transparent; color: white; padding: 12px 24px; border-radius: 8px; font-weight: 600; border: 2px solid rgba(255,255,255,0.4);">
      Learn More
    </button>
  </div>
</section>
```

**Problems:**
- Purple-to-indigo gradient — banned pattern
- Inter as the only font — no display/body separation
- Centered hero — banned SaaS cliché
- Two equal-weight CTAs — no priority hierarchy
- "Seamless" and "Get Started" — banned copy patterns
- Fixed 48px heading — not fluid
- Inline styles — no token system

---

## After

```html
<!-- Tokens first — in <head> -->
<link rel="preload" as="font"
  href="https://fonts.gstatic.com/s/fraunces/v31/6NUh8FyLNQOQZAnv9bYEvDiIdE9Eqcbf.woff2"
  type="font/woff2" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Instrument+Sans:wght@400;500;600&display=swap"
  rel="stylesheet" />

<section class="hero">
  <div class="container hero__container">

    <!-- Left column: text -->
    <div class="hero__text">
      <span class="eyebrow">Now in public beta</span>

      <h1 class="hero__heading">
        Deploy in 23&nbsp;seconds,<br>
        roll back in&nbsp;<em>10.</em>
      </h1>

      <p class="hero__sub">
        Push to GitHub and your changes are live — globally, on the edge,
        with zero config. Your team ships. Infrastructure waits.
      </p>

      <div class="hero__actions">
        <a href="/signup" class="btn btn--primary btn--lg">
          Start deploying free
        </a>
        <a href="/demo" class="hero__demo-link">
          Watch 2-min demo
          <svg aria-hidden="true" width="16" height="16" viewBox="0 0 16 16" fill="none"
            stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
            <path d="M3 8h10M8 3l5 5-5 5"/>
          </svg>
        </a>
      </div>

      <p class="hero__trust">
        Trusted by 18,000 teams. No credit card required.
      </p>
    </div>

    <!-- Right column: product screenshot -->
    <div class="hero__media">
      <div class="hero__screenshot-wrap">
        <img
          class="hero__screenshot"
          src="/hero-dashboard.png"
          alt="Acme dashboard showing a successful deployment with 23-second build time"
          width="1200" height="800"
          loading="eager"
          fetchpriority="high"
        />
      </div>
    </div>

  </div>
</section>
```

```css
/* tokens — in tokens.css, just showing the relevant ones here */
:root {
  --font-display: 'Fraunces', Georgia, serif;
  --font-body:    'Instrument Sans', system-ui, sans-serif;
  --text-h1:      clamp(2rem, 4vw + 0.25rem, 4.5rem);
  --text-body:    clamp(1rem, 1.2vw + 0.4rem, 1.2rem);
}

.hero {
  padding-block: clamp(var(--space-16), 12vh, var(--space-24));
  background: var(--color-surface);
  overflow: hidden;
}

.hero__container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-16);
  align-items: center;
}

.hero__text {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}

.hero__heading {
  font-size: var(--text-h1);
  font-family: var(--font-display);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.1;
  color: var(--color-text-primary);
}

.hero__heading em {
  font-style: italic;
  color: var(--color-accent);
}

.hero__sub {
  font-size: var(--text-body);
  color: var(--color-text-secondary);
  line-height: 1.65;
  max-width: 46ch;
}

.hero__actions {
  display: flex;
  align-items: center;
  gap: var(--space-5);
  flex-wrap: wrap;
}

.hero__demo-link {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: color var(--duration-fast) var(--ease-smooth);
}

.hero__demo-link:hover { color: var(--color-text-primary); }

.hero__trust {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
}

/* Screenshot panel */
.hero__media {
  position: relative;
}

.hero__screenshot-wrap {
  position: relative;
  border-radius: var(--radius-xl);
  overflow: hidden;
  box-shadow: var(--shadow-lg), 0 0 0 1px var(--color-border);
  transform: perspective(1200px) rotateY(-4deg) rotateX(2deg);
  transition: transform 500ms var(--ease-smooth);
}

.hero__screenshot-wrap:hover {
  transform: perspective(1200px) rotateY(-1deg) rotateX(0deg);
}

.hero__screenshot {
  display: block;
  width: 100%;
  height: auto;
}

@media (max-width: 900px) {
  .hero__container {
    grid-template-columns: 1fr;
    gap: var(--space-10);
  }
  .hero__screenshot-wrap { transform: none; }
  .hero__screenshot-wrap:hover { transform: none; }
}
```

---

## Before/After Comparison

| Element | Before | After |
|---|---|---|
| Background | Purple-to-indigo gradient | Surface color (no gradient) |
| Layout | Centered single column | Left text + right screenshot |
| Font | Inter everywhere | Fraunces (display) + Instrument Sans (body) |
| H1 size | Fixed `48px` | `clamp(2rem, 4vw + 0.25rem, 4.5rem)` |
| CTAs | Two equal blue buttons | 1 primary + 1 text link |
| Copy | "Ship faster, seamless" | Specific claim: "23 seconds, roll back in 10" |
| Colors | Hardcoded hex | Semantic tokens |
| Product media | None | Screenshot with perspective tilt |
| Trust signal | None | "18,000 teams, no credit card" |

---

*Example version: global-design-skill v1.0 — `examples/landing-pages/01-saas-hero-redesign.md`*  
*Related: `recipes/improve-typography.md`, `rules/03-typography.md`, `rules/04-color.md`*
