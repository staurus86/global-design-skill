# Example 01 — Hero Section Redesign

> **Rules applied:** typography R1, R3, R7, R8 · color R1, R2 · animation R1, R2, R3, R6, R9 · layout (SKILL.md §7) · performance R1

**Scenario:** A SaaS landing page hero. The original was written by a developer following "good enough" conventions. It renders, it works. It also violates 14 rules.

---

## Before — The Original

```html
<!-- index.html -->
<head>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet" />
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Inter', sans-serif; background: #ffffff; color: #333333; }

    .hero {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      padding: 60px 24px;
      background: linear-gradient(135deg, #6366f1, #8b5cf6);
    }

    .hero h1 {
      font-size: 48px;
      font-weight: 700;
      color: white;
      line-height: 1.5;
      margin-bottom: 16px;
    }

    .hero p {
      font-size: 18px;
      color: rgba(255, 255, 255, 0.8);
      max-width: 600px;
      margin-bottom: 32px;
    }

    .btn-primary {
      background: #ffffff;
      color: #6366f1;
      padding: 12px 24px;
      border-radius: 6px;
      font-size: 16px;
      font-weight: 600;
      cursor: pointer;
      border: none;
      transition: all 0.3s ease-in-out;
    }

    .btn-primary:hover { opacity: 0.9; transform: scale(1.02); }

    .btn-secondary {
      background: transparent;
      color: white;
      padding: 12px 24px;
      border: 2px solid rgba(255,255,255,0.5);
      border-radius: 6px;
      font-size: 16px;
      cursor: pointer;
      transition: all 0.3s ease-in-out;
    }
  </style>
</head>
<body>
  <section class="hero">
    <h1>The Next-Generation Platform That Empowers Teams to Seamlessly Collaborate</h1>
    <p>Elevate your workflow and unleash the full potential of your team with our revolutionary suite of tools designed to transform how you work together.</p>
    <div style="display:flex; gap:12px;">
      <button class="btn-primary">Get Started</button>
      <button class="btn-secondary">Learn More</button>
    </div>
  </section>
</body>
```

---

## Diagnosis — 14 Violations

| # | Violation | Rule |
|---|---|---|
| 1 | Font: Inter as primary display font | typography R6 |
| 2 | `font-size: 48px` — fixed px, breaks on mobile | typography R1 |
| 3 | `line-height: 1.5` on a headline | typography R4 |
| 4 | No eyebrow tag before H1 | typography R7 |
| 5 | Headline copy: "Next-Generation", "Empowers", "Seamlessly" (banned words) | SKILL.md §2 |
| 6 | Hero CTA copy: "Get Started", "Learn More" (generic) | SKILL.md §2 |
| 7 | Purple-to-indigo gradient background (banned) | color R1, SKILL.md §2 |
| 8 | `background: #ffffff` — raw hex, no token | color R1 |
| 9 | `rgba(255,255,255,0.8)` — hardcoded alpha, not relative OKLCH | color R9 |
| 10 | `transition: all 0.3s ease-in-out` — two violations in one | animation R2, R3 |
| 11 | No entry animation — elements appear statically | animation R1 |
| 12 | No `prefers-reduced-motion` override | animation R6 |
| 13 | Hero image missing — LCP element unidentified | performance R1 |
| 14 | Section `padding: 60px` — below 80px minimum | SKILL.md §7 |

---

## After — Corrected

```html
<!-- index.html -->
<head>
  <!-- Preload critical font (used in hero = LCP) -->
  <link rel="preload" as="font"
    href="https://fonts.gstatic.com/s/fraunces/v31/6NUh8FyLNQOQZAnv9bYEvDiIdE9Eqcbf.woff2"
    type="font/woff2" crossorigin />

  <!-- Preload LCP image -->
  <link rel="preload" as="image" href="/product-dashboard.webp" fetchpriority="high" />

  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300..900&family=Instrument+Sans:wght@400;500;600&display=swap"
        rel="stylesheet" />

  <link rel="stylesheet" href="/tokens/tokens.css" />
  <link rel="stylesheet" href="/tokens/tokens-dark.css" />

  <style>
    body {
      font-family: var(--font-body);
      background: var(--color-base);
      color: var(--color-text-primary);
    }

    /* ── Hero ── */
    .hero {
      display: grid;
      grid-template-columns: 1fr 1fr;
      align-items: center;
      gap: var(--space-16);
      padding-block: var(--space-24);   /* 96px — above 80px minimum */
      padding-inline: var(--space-10);
      max-width: var(--container-xl);
      margin-inline: auto;
    }

    @media (max-width: 768px) {
      .hero { grid-template-columns: 1fr; padding-block: var(--space-16); }
      .hero__visual { display: none; }
    }

    /* ── Typography ── */
    .hero__eyebrow {
      display: inline-flex;
      align-items: center;
      gap: var(--space-2);
      padding: 0.25rem 0.875rem;
      border: 1px solid oklch(from var(--color-accent) l c h / 0.4);
      border-radius: var(--radius-full);
      background: oklch(from var(--color-accent) l c h / 0.06);
      font-size: var(--text-3xs);
      font-weight: var(--font-weight-medium);
      letter-spacing: var(--tracking-widest);
      text-transform: uppercase;
      color: var(--color-accent);
      margin-bottom: var(--space-5);
    }

    .hero__headline {
      font-family: var(--font-display);
      font-size: var(--text-display);    /* clamp(2.5rem, 5vw + 0.5rem, 7rem) */
      font-weight: 700;
      line-height: var(--line-height-tight);   /* 1.1 */
      letter-spacing: var(--tracking-tight);   /* -0.03em */
      color: var(--color-text-primary);
      max-width: 14ch;
      margin-bottom: var(--space-6);
    }

    .hero__sub {
      font-size: var(--text-body);
      line-height: var(--line-height-relaxed);  /* 1.65 */
      color: var(--color-text-secondary);
      max-width: 42ch;
      margin-bottom: var(--space-8);
    }

    /* ── CTAs ── */
    .hero__actions {
      display: flex;
      gap: var(--space-3);
      align-items: center;
      flex-wrap: wrap;
    }

    .btn-primary {
      background: var(--color-accent);
      color: oklch(98% 0.005 258);
      padding: 0 var(--space-6);
      height: var(--btn-height-md);       /* 44px */
      border-radius: var(--radius-md);
      font-weight: var(--font-weight-semibold);
      font-size: var(--text-sm);
      cursor: pointer;
      border: none;
      transition:
        background   var(--duration-fast)   var(--ease-smooth),
        box-shadow   var(--duration-fast)   var(--ease-smooth),
        transform    var(--duration-fast)   var(--ease-snappy);
    }

    .btn-primary:hover {
      background: var(--color-accent-dark);
      box-shadow: var(--shadow-sm);
      transform: translateY(-1px);
    }

    .btn-ghost {
      background: transparent;
      color: var(--color-text-secondary);
      padding: 0 var(--space-5);
      height: var(--btn-height-md);
      border-radius: var(--radius-md);
      font-size: var(--text-sm);
      cursor: pointer;
      border: 1px solid var(--color-border);
      transition:
        border-color  var(--duration-fast) var(--ease-smooth),
        color         var(--duration-fast) var(--ease-smooth);
    }

    .btn-ghost:hover {
      border-color: var(--color-text-muted);
      color: var(--color-text-primary);
    }

    /* ── Product visual ── */
    .hero__visual {
      position: relative;
    }

    .hero__screenshot {
      width: 100%;
      height: auto;
      border-radius: var(--radius-xl);
      border: 1px solid var(--color-border);
      box-shadow: var(--shadow-xl);
    }

    /* ── Entry animations ── */
    .hero__content > * {
      opacity: 0;
      transform: translateY(16px);
      animation: hero-enter var(--duration-slow) var(--ease-spring) forwards;
    }

    .hero__content .hero__eyebrow   { animation-delay: 0ms;   }
    .hero__content .hero__headline  { animation-delay: 80ms;  }
    .hero__content .hero__sub       { animation-delay: 160ms; }
    .hero__content .hero__actions   { animation-delay: 240ms; }

    .hero__visual {
      opacity: 0;
      transform: translateX(24px);
      animation: hero-enter var(--duration-entrance) var(--ease-spring) forwards;
      animation-delay: 200ms;
    }

    @keyframes hero-enter {
      to { opacity: 1; transform: none; }
    }

    /* Reduce motion: keep fade, remove translate */
    @media (prefers-reduced-motion: reduce) {
      .hero__content > *,
      .hero__visual {
        transform: none;
        animation-duration: var(--duration-fast);
        animation-delay: 0ms !important;
      }
    }
  </style>
</head>

<body>
  <section class="hero">
    <div class="hero__content">
      <span class="hero__eyebrow">Now in beta</span>

      <h1 class="hero__headline">Ship faster without the late-night incidents</h1>

      <p class="hero__sub">
        Pipeline gives your team a single place to monitor deploys, catch failures
        before users do, and roll back in 30 seconds.
      </p>

      <div class="hero__actions">
        <button class="btn-primary">Start free — no card needed</button>
        <button class="btn-ghost">See a 4-minute demo</button>
      </div>
    </div>

    <div class="hero__visual">
      <!-- LCP image: eager + high priority + preload in <head> -->
      <img
        class="hero__screenshot"
        src="/product-dashboard.webp"
        alt="Pipeline dashboard showing 4 active deployments, 1 failed build highlighted in red with a 'Roll back' button"
        width="1200"
        height="800"
        loading="eager"
        fetchpriority="high"
        decoding="async"
      />
    </div>
  </section>
</body>
```

---

## What Changed and Why

**Layout: centered → split**
The centered hero with H1 + subtext + 2 buttons is the most overused layout in SaaS. The split layout (text left, product visual right) serves two purposes at once: it puts a real product screenshot as the LCP element (performance win) and breaks the symmetry immediately.

**Font: Inter → Fraunces + Instrument Sans**
Inter is banned as a primary display font — it signals "I used the default." Fraunces is a variable optical-size serif with character that holds at large sizes. Instrument Sans handles body and UI copy.

**`font-size: 48px` → `var(--text-display)`**
`clamp(2.5rem, 5vw + 0.5rem, 7rem)` scales from 40px on a 390px screen to 112px on a large monitor. No media queries needed.

**`line-height: 1.5` → `var(--line-height-tight)` (1.1)**
1.5 on a 48px headline creates balloon-like floating text. Tight line-height on display type looks professional and intentional.

**Purple gradient → token surface**
The purple-to-indigo gradient is explicitly banned. The dark base surface (`oklch(10% 0.015 258)`) has a subtle blue tint that reads as premium without announcing itself.

**`transition: all 0.3s ease-in-out` → explicit property list with cubic-bezier**
`transition: all` transitions hidden properties and prevents discrete transitions. `ease-in-out` signals no thought was given to timing. Each property gets its own duration and easing from the token scale.

**No entry animation → staggered entrance with @keyframes**
Content entering the page creates energy and a reading sequence. The 80ms stagger between elements (eyebrow → headline → subtext → CTAs) creates composition without feeling theatrical.

**"Get Started" → "Start free — no card needed"**
Specific CTAs convert better because they answer the implicit objection (do I need a credit card?) and state the value (free). "Get Started" means nothing.

**`rgba(255,255,255,0.8)` → `oklch(from var(--token) l c h / α)`**
Hardcoded alpha values break in dark mode and don't adapt to theme changes. Relative OKLCH syntax derives alpha from the current token value.

---

*Example 01 — `examples/01-hero-redesign.md`*
*Related: `recipes/improve-hero-section.md`, `rules/03-typography.md`, `rules/04-color.md`, `rules/05-animation.md`, `rules/08-performance.md`*
