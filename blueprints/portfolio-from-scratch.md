# Blueprint — Portfolio From Scratch

> A complete reference implementation for a developer or designer portfolio. The goal: communicate expertise, show real work, and make it trivially easy to reach out.

---

## Page Structure

```
1. Nav (minimal, sticky)
2. Hero — identity + role + 1 standout claim
3. Work / Case studies (2–4 featured projects)
4. Skills or Process section (optional)
5. About (short, personal, specific)
6. Contact / CTA
7. Footer (links only)
```

---

## Design Decisions Before You Build

```
Answer these before choosing typography or layout:

Audience:      Who is this for? Recruiters? Clients? Founders?
Tone:          Technical precision, creative personality, or warm/approachable?
Primary goal:  Job applications, freelance clients, community recognition?
Featured work: What 2–3 projects best represent you? (Quality beats quantity)
Differentiator:What do you do better than most? Name it in the hero.
```

---

## Section 1 — Hero

The hero must answer three questions in under 3 seconds:
- Who are you?
- What do you do?
- Why should I care?

```html
<section class="portfolio-hero">
  <div class="container">
    <div class="portfolio-hero__inner">
      <div class="portfolio-hero__identity">
        <img
          class="portfolio-hero__avatar"
          src="/avatar.jpg"
          alt="Alex Kim"
          width="64" height="64"
          loading="eager"
          fetchpriority="high"
        />
        <div>
          <p class="portfolio-hero__name">Alex Kim</p>
          <p class="portfolio-hero__availability">
            <span class="availability-dot" aria-hidden="true"></span>
            Available for freelance — January 2026
          </p>
        </div>
      </div>

      <h1 class="portfolio-hero__heading">
        I build interfaces that feel <em>alive.</em>
      </h1>
      <p class="portfolio-hero__sub">
        Frontend engineer specializing in design systems and motion design.
        5 years at product companies — Vercel, Stripe, Loom.
      </p>

      <div class="portfolio-hero__actions">
        <a href="#work" class="btn btn--primary">View my work</a>
        <a href="mailto:alex@example.com" class="btn btn--ghost">Get in touch</a>
      </div>
    </div>
  </div>
</section>
```

```css
.portfolio-hero {
  padding-block: var(--space-24) var(--space-20);
  min-height: 70dvh;
  display: flex;
  align-items: center;
}

.portfolio-hero__inner {
  max-width: 620px;
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}

.portfolio-hero__identity {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.portfolio-hero__avatar {
  width: 56px; height: 56px;
  border-radius: var(--radius-full);
  object-fit: cover;
}

.portfolio-hero__name {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-primary);
}

.portfolio-hero__availability {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: 12px;
  color: var(--color-success);
}

.availability-dot {
  display: block;
  width: 6px; height: 6px;
  border-radius: var(--radius-full);
  background: var(--color-success);
  animation: pulse-dot 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes pulse-dot {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.4; }
}

@media (prefers-reduced-motion: reduce) {
  .availability-dot { animation: none; }
}

.portfolio-hero__heading {
  font-size: var(--text-h1);
  font-family: var(--font-display);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.1;
  color: var(--color-text-primary);
}

.portfolio-hero__heading em {
  font-style: italic;
  color: var(--color-accent);
}

.portfolio-hero__sub {
  font-size: var(--text-body);
  color: var(--color-text-secondary);
  line-height: 1.65;
  max-width: 52ch;
}

.portfolio-hero__actions {
  display: flex;
  gap: var(--space-3);
  flex-wrap: wrap;
}
```

---

## Section 2 — Featured Work

Show 2–4 projects max. Each needs: real outcome, not just tech stack.

```html
<section class="portfolio-work" id="work" aria-labelledby="work-heading">
  <div class="container">
    <h2 class="section-heading" id="work-heading">Selected work</h2>

    <div class="work-grid">

      <!-- Full-width featured project -->
      <article class="work-card work-card--featured">
        <a href="/work/design-system" class="work-card__media-link" tabindex="-1" aria-hidden="true">
          <div class="work-card__media">
            <img src="/work/ds-cover.jpg" alt="" width="1200" height="720"
              loading="lazy" class="work-card__img" />
          </div>
        </a>
        <div class="work-card__body">
          <div class="work-card__meta">
            <span class="work-card__type">Design system</span>
            <span class="work-card__year">2024</span>
          </div>
          <h3 class="work-card__title">
            <a href="/work/design-system" class="work-card__link">
              Replatforming Loom's component library
            </a>
          </h3>
          <p class="work-card__outcome">
            Reduced frontend build time by 40% and enabled dark mode across 80 components
            in a single token migration.
          </p>
          <div class="work-card__tags">
            <span class="tag">React</span>
            <span class="tag">CSS tokens</span>
            <span class="tag">Figma</span>
          </div>
        </div>
      </article>

      <!-- Two-column grid for secondary projects -->
      <article class="work-card">
        <a href="/work/motion-library" class="work-card__media-link" tabindex="-1" aria-hidden="true">
          <div class="work-card__media">
            <img src="/work/motion-cover.jpg" alt="" width="720" height="480"
              loading="lazy" class="work-card__img" />
          </div>
        </a>
        <div class="work-card__body">
          <div class="work-card__meta">
            <span class="work-card__type">Open source</span>
            <span class="work-card__year">2023</span>
          </div>
          <h3 class="work-card__title">
            <a href="/work/motion-library" class="work-card__link">Motion library for SaaS</a>
          </h3>
          <p class="work-card__outcome">
            Zero-config animation primitives. 2,400 GitHub stars in 3 months.
          </p>
        </div>
      </article>

      <article class="work-card">
        <!-- ... similar structure -->
      </article>

    </div>
  </div>
</section>
```

```css
.portfolio-work { padding-block: var(--space-24); }

.section-heading {
  font-size: var(--text-h2);
  font-family: var(--font-display);
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--color-text-primary);
  margin-bottom: var(--space-10);
}

.work-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--space-6);
}

.work-card--featured { grid-column: span 2; }

.work-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-5);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  overflow: hidden;
  background: var(--color-surface-2);
  transition:
    border-color var(--duration-normal) var(--ease-smooth),
    box-shadow   var(--duration-normal) var(--ease-smooth),
    transform    var(--duration-normal) var(--ease-spring);
}

.work-card:hover {
  border-color: var(--color-border-strong);
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

.work-card__media {
  overflow: hidden;
  aspect-ratio: 16/9;
  background: var(--color-surface-3);
}

.work-card--featured .work-card__media { aspect-ratio: 21/9; }

.work-card__img {
  width: 100%; height: 100%;
  object-fit: cover;
  transition: transform 500ms var(--ease-smooth);
}

.work-card:hover .work-card__img { transform: scale(1.02); }

.work-card__body {
  padding: var(--space-5) var(--space-5) var(--space-6);
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.work-card--featured .work-card__body { padding: var(--space-8); }

.work-card__meta {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.work-card__type {
  font-size: 11px;
  font-weight: var(--font-weight-semibold);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-accent);
}

.work-card__year {
  font-size: 11px;
  color: var(--color-text-muted);
}

.work-card__title {
  font-size: var(--text-h3);
  font-family: var(--font-display);
  font-weight: 700;
  line-height: 1.2;
}

.work-card__link {
  color: var(--color-text-primary);
  text-decoration: none;
}

.work-card__link:hover { color: var(--color-accent); }
.work-card__link:focus-visible {
  outline: 2px solid var(--color-border-focus);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}

.work-card__outcome {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  line-height: 1.65;
}

.work-card__tags {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}

.tag {
  padding: var(--space-1) var(--space-2);
  border-radius: var(--radius-sm);
  background: var(--color-surface-3);
  font-size: 11px;
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
}

@media (max-width: 768px) {
  .work-grid { grid-template-columns: 1fr; }
  .work-card--featured { grid-column: span 1; }
}
```

---

## Section 3 — About (Short)

```html
<section class="portfolio-about" aria-labelledby="about-heading">
  <div class="container portfolio-about__container">
    <div class="portfolio-about__text">
      <h2 id="about-heading" class="section-heading">About</h2>
      <p>
        Frontend engineer based in Berlin. I've spent the last 5 years making
        design systems that developers actually enjoy using — and animations that
        don't get shipped with 300ms ease-in-out.
      </p>
      <p>
        Previously at Vercel, Stripe, and Loom. Currently available for
        contract work through April 2026.
      </p>
      <div class="portfolio-about__links">
        <a href="https://github.com/alexkim" class="external-link">GitHub</a>
        <a href="https://linkedin.com/in/alexkim" class="external-link">LinkedIn</a>
        <a href="/resume.pdf" class="external-link">Resume (PDF)</a>
      </div>
    </div>
    <div class="portfolio-about__image" aria-hidden="true">
      <img src="/about-photo.jpg" alt="" width="400" height="500"
        loading="lazy" class="about-img" />
    </div>
  </div>
</section>
```

```css
.portfolio-about { padding-block: var(--space-24); background: var(--color-surface-2); }

.portfolio-about__container {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: var(--space-16);
  align-items: center;
}

.portfolio-about__text {
  display: flex;
  flex-direction: column;
  gap: var(--space-5);
}

.portfolio-about__text p {
  font-size: var(--text-body);
  color: var(--color-text-secondary);
  line-height: 1.65;
  max-width: 54ch;
}

.portfolio-about__links {
  display: flex;
  gap: var(--space-4);
}

.external-link {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-accent);
  text-decoration: none;
}

.external-link:hover { text-decoration: underline; }

.about-img {
  width: 100%; height: 100%;
  object-fit: cover;
  border-radius: var(--radius-xl);
}

@media (max-width: 768px) {
  .portfolio-about__container { grid-template-columns: 1fr; }
  .portfolio-about__image { display: none; }
}
```

---

## Section 4 — Contact CTA

```html
<section class="portfolio-cta" aria-labelledby="cta-heading">
  <div class="container portfolio-cta__inner">
    <h2 class="portfolio-cta__heading" id="cta-heading">
      Let's build something together.
    </h2>
    <p class="portfolio-cta__sub">
      I respond to all inquiries within 24 hours.
    </p>
    <a href="mailto:alex@example.com" class="btn btn--primary btn--lg">
      alex@example.com
    </a>
  </div>
</section>
```

```css
.portfolio-cta {
  padding-block: var(--space-24);
  text-align: center;
}

.portfolio-cta__inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-5);
}

.portfolio-cta__heading {
  font-size: var(--text-h1);
  font-family: var(--font-display);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.1;
  color: var(--color-text-primary);
  max-width: 14ch;
}

.portfolio-cta__sub {
  font-size: var(--text-body);
  color: var(--color-text-secondary);
}
```

---

## Portfolio Anti-Patterns

```
× "Passionate about clean code" — says nothing, everyone says this
× Tech stack list without outcomes — no one cares what you used; they care what you achieved
× 10+ projects shown — shows you can't edit yourself
× "Available for opportunities" with no contact method — forces extra work
× Work thumbnails without descriptions — user can't tell what they're looking at
× "Currently looking for my next adventure" — unprofessional
× Password-protected work without a reason — signals the work isn't that good
× No dark mode — shows you don't care about the details
× Footer with 10 social icons — pick 2–3 and commit
```

---

*Blueprint version: global-design-skill v1.0 — `blueprints/portfolio-from-scratch.md`*  
*Related: `blueprints/onboarding-flow-from-scratch.md`, `rules/03-typography.md`, `rules/02-layout-and-grid.md`*
