# Pattern — Feature Sections

> The feature section is the most-abused section on the internet. The 3-column icon grid is not a pattern — it is a failure of imagination. These patterns replace it with layouts that communicate what the product actually does, using real product visuals and specific copy.

---

## When to use this section

Feature sections answer the question: "How does this actually work?" They follow the hero and translate the headline promise into specific capabilities. Each feature section should demonstrate one of:

1. **The how** — step-by-step product workflow
2. **The what** — specific capabilities with evidence (screenshots, data)
3. **The proof** — results, before/after, or comparison

---

## Pattern 1 — Alternating Split (Screenshot + Text)

**Use for:** 3–4 core features, each shown with a real product screenshot.

```html
<section class="features-alternating">
  <div class="features-alternating__inner">

    <div class="features-alternating__header">
      <span class="eyebrow">How it works</span>
      <h2 class="features-alternating__title">From push to production in 30 seconds</h2>
    </div>

    <!-- Feature 1: text left, image right -->
    <div class="feature-split" data-reveal>
      <div class="feature-split__content">
        <span class="feature-split__step" aria-hidden="true">01</span>
        <h3 class="feature-split__title">Push to any branch</h3>
        <p class="feature-split__desc">
          Connect your GitHub, GitLab, or Bitbucket repository.
          Pipeline watches every branch — not just main.
          Every commit triggers a build automatically.
        </p>
        <ul class="feature-split__list">
          <li>GitHub, GitLab, Bitbucket support</li>
          <li>Automatic preview URLs per branch</li>
          <li>Build status directly in pull requests</li>
        </ul>
      </div>
      <div class="feature-split__visual">
        <img
          src="/features/git-connect.webp"
          alt="GitHub integration showing Pipeline checking 4 open pull requests, each with a green build status indicator"
          width="640" height="420"
          loading="lazy"
          class="feature-split__img"
        />
      </div>
    </div>

    <!-- Feature 2: image left, text right (reversed) -->
    <div class="feature-split feature-split--reversed" data-reveal>
      <div class="feature-split__content">
        <span class="feature-split__step" aria-hidden="true">02</span>
        <h3 class="feature-split__title">Monitor every deploy in real time</h3>
        <p class="feature-split__desc">
          Watch logs stream live as your build runs. Get notified the moment
          something fails — with the exact test or command that failed,
          not a generic error code.
        </p>
        <ul class="feature-split__list">
          <li>Real-time log streaming</li>
          <li>Slack and PagerDuty alerts on failure</li>
          <li>Build time trends over 30 days</li>
        </ul>
      </div>
      <div class="feature-split__visual">
        <img
          src="/features/live-logs.webp"
          alt="Live deployment logs showing 47 lines of output, with a red error at line 43: 'Test failed: auth.spec.ts line 112'"
          width="640" height="420"
          loading="lazy"
          class="feature-split__img"
        />
      </div>
    </div>

    <!-- Feature 3 -->
    <div class="feature-split" data-reveal>
      <div class="feature-split__content">
        <span class="feature-split__step" aria-hidden="true">03</span>
        <h3 class="feature-split__title">Roll back in one click</h3>
        <p class="feature-split__desc">
          Every deploy is stored. If something breaks in production,
          click the previous deploy and it's live again in 11 seconds.
          No Git revert, no support ticket, no 3am incident.
        </p>
        <ul class="feature-split__list">
          <li>Full deploy history — unlimited retention</li>
          <li>11-second rollback average</li>
          <li>Automatic rollback on health check failure</li>
        </ul>
      </div>
      <div class="feature-split__visual">
        <img
          src="/features/rollback.webp"
          alt="Deploy history panel showing 5 previous deploys, with a 'Roll back to this version' button highlighted on the second entry"
          width="640" height="420"
          loading="lazy"
          class="feature-split__img"
        />
      </div>
    </div>

  </div>
</section>
```

```css
.features-alternating {
  padding-block: var(--space-24);
  background: var(--color-base);
}

.features-alternating__inner {
  max-width: var(--container-xl);
  margin-inline: auto;
  padding-inline: var(--space-8);
}

.features-alternating__header {
  text-align: center;
  max-width: 640px;
  margin-inline: auto;
  margin-bottom: var(--space-20);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-4);
}

.features-alternating__title {
  font-family: var(--font-display);
  font-size: var(--text-h1);
  font-weight: 700;
  line-height: var(--line-height-tight);
  color: var(--color-text-primary);
}

/* ── Feature split ── */
.feature-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  gap: var(--space-16);
  padding-block: var(--space-16);
  border-top: 1px solid var(--color-border);
}

.feature-split--reversed { direction: rtl; }
.feature-split--reversed > * { direction: ltr; }

@media (max-width: 768px) {
  .feature-split,
  .feature-split--reversed { grid-template-columns: 1fr; direction: ltr; gap: var(--space-8); }
}

.feature-split__step {
  display: block;
  font-family: var(--font-display);
  font-size: var(--text-display);
  font-weight: 700;
  line-height: 1;
  color: oklch(from var(--color-accent) l c h / 0.15);
  letter-spacing: var(--tracking-tighter);
  margin-bottom: var(--space-3);
}

.feature-split__title {
  font-family: var(--font-display);
  font-size: var(--text-h2);
  font-weight: 700;
  line-height: var(--line-height-snug);
  color: var(--color-text-primary);
  margin-bottom: var(--space-4);
}

.feature-split__desc {
  font-size: var(--text-body);
  line-height: var(--line-height-relaxed);
  color: var(--color-text-secondary);
  margin-bottom: var(--space-5);
}

.feature-split__list {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.feature-split__list li {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
}

.feature-split__list li::before {
  content: '';
  width: 6px; height: 6px;
  border-radius: var(--radius-full);
  background: var(--color-accent);
  flex-shrink: 0;
}

.feature-split__img {
  width: 100%;
  height: auto;
  border-radius: var(--radius-xl);
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-xl);
}
```

---

## Pattern 2 — Asymmetric Bento Grid

**Use for:** 4–6 features of unequal importance. One hero feature, supporting features below.

```html
<section class="features-bento">
  <div class="features-bento__inner">

    <div class="features-bento__header">
      <span class="eyebrow">What you get</span>
      <h2 class="features-bento__title">Built for teams who ship continuously</h2>
    </div>

    <div class="bento-grid" role="list">

      <!-- Hero cell: spans 2 columns, 2 rows -->
      <article class="bento-cell bento-cell--hero" role="listitem" data-reveal>
        <div class="bento-cell__content">
          <h3 class="bento-cell__title">Zero-config deployment from any git host</h3>
          <p class="bento-cell__desc">
            Connect your repository once. Pipeline detects your framework,
            sets up the build pipeline, and deploys in under 2 minutes.
            No YAML. No config files.
          </p>
        </div>
        <div class="bento-cell__visual">
          <img src="/features/zero-config.webp" alt="Setup wizard showing GitHub connected, framework detected as Next.js 15, and first deploy completed in 1m 47s" width="600" height="380" loading="lazy" />
        </div>
      </article>

      <!-- Stat cell -->
      <article class="bento-cell bento-cell--stat" role="listitem" data-reveal>
        <p class="bento-cell__stat">11s</p>
        <h3 class="bento-cell__title">Average rollback time</h3>
        <p class="bento-cell__desc">Measured across 1M+ deploys in 2025.</p>
      </article>

      <!-- Stat cell -->
      <article class="bento-cell bento-cell--stat" role="listitem" data-reveal>
        <p class="bento-cell__stat">40+</p>
        <h3 class="bento-cell__title">Integrations</h3>
        <p class="bento-cell__desc">Slack, PagerDuty, Datadog, Grafana, and more.</p>
      </article>

      <!-- Wide feature cell -->
      <article class="bento-cell bento-cell--wide" role="listitem" data-reveal>
        <div class="bento-cell__content">
          <h3 class="bento-cell__title">Preview every branch before it ships</h3>
          <p class="bento-cell__desc">Every pull request gets its own URL — shareable with your team, linked in the PR, deleted automatically on merge.</p>
        </div>
        <div class="bento-cell__tags">
          <span class="tag">preview.yourapp.com/pr-142</span>
          <span class="tag">preview.yourapp.com/pr-139</span>
          <span class="tag">preview.yourapp.com/main</span>
        </div>
      </article>

    </div>
  </div>
</section>
```

```css
.features-bento { padding-block: var(--space-24); }
.features-bento__inner { max-width: var(--container-xl); margin-inline: auto; padding-inline: var(--space-8); }

.features-bento__header {
  max-width: 640px;
  margin-bottom: var(--space-12);
  display: flex; flex-direction: column; gap: var(--space-4);
}
.features-bento__title {
  font-family: var(--font-display);
  font-size: var(--text-h1); font-weight: 700;
  line-height: var(--line-height-tight);
}

.bento-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-4);
}

.bento-cell {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  overflow: hidden;
}

.bento-cell--hero { grid-column: span 8; grid-row: span 2; display: flex; flex-direction: column; }
.bento-cell--stat { grid-column: span 4; padding: var(--space-8); }
.bento-cell--wide { grid-column: span 12; padding: var(--space-8); display: flex; align-items: center; justify-content: space-between; gap: var(--space-8); flex-wrap: wrap; }

.bento-cell--hero .bento-cell__content { padding: var(--space-8); }
.bento-cell--hero img { width: 100%; height: auto; border-top: 1px solid var(--color-border); }

.bento-cell__stat {
  font-family: var(--font-display);
  font-size: var(--text-display); font-weight: 700; line-height: 1;
  color: var(--color-accent); letter-spacing: var(--tracking-tighter);
  margin-bottom: var(--space-3);
}
.bento-cell__title { font-size: var(--text-lg); font-weight: var(--font-weight-semibold); color: var(--color-text-primary); margin-bottom: var(--space-2); }
.bento-cell__desc  { font-size: var(--text-sm); color: var(--color-text-secondary); line-height: var(--line-height-relaxed); }

.bento-cell__tags { display: flex; flex-wrap: wrap; gap: var(--space-2); }
.tag {
  padding: var(--space-1) var(--space-3);
  background: var(--color-surface-2);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-size: var(--text-sm); font-family: var(--font-mono);
  color: var(--color-text-secondary);
}

@media (max-width: 1024px) {
  .bento-cell--hero,
  .bento-cell--stat,
  .bento-cell--wide { grid-column: span 12; }
}
```

---

## Pattern 3 — How It Works (Numbered Steps)

**Use for:** Process-oriented products. Shows the workflow as 3–4 sequential steps.

```html
<section class="how-it-works">
  <div class="how-it-works__inner">
    <div class="how-it-works__header">
      <span class="eyebrow">Setup in minutes</span>
      <h2>Three steps from signup to first deploy</h2>
    </div>

    <div class="steps-grid">
      <div class="step" data-reveal>
        <div class="step__number" aria-hidden="true">1</div>
        <div class="step__content">
          <h3 class="step__title">Connect your repository</h3>
          <p class="step__desc">Authorize Pipeline to access your GitHub, GitLab, or Bitbucket account. Takes 45 seconds.</p>
        </div>
      </div>
      <div class="step-arrow" aria-hidden="true">→</div>
      <div class="step" data-reveal>
        <div class="step__number" aria-hidden="true">2</div>
        <div class="step__content">
          <h3 class="step__title">Select a repository</h3>
          <p class="step__desc">Pick any repo. Pipeline detects your framework and pre-fills the build settings. Edit anything you need.</p>
        </div>
      </div>
      <div class="step-arrow" aria-hidden="true">→</div>
      <div class="step" data-reveal>
        <div class="step__number" aria-hidden="true">3</div>
        <div class="step__content">
          <h3 class="step__title">Push and it deploys</h3>
          <p class="step__desc">Your next commit triggers a build. You get a deploy URL in under 2 minutes.</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

```css
.how-it-works { padding-block: var(--space-24); background: var(--color-surface); }
.how-it-works__inner { max-width: var(--container-xl); margin-inline: auto; padding-inline: var(--space-8); }
.how-it-works__header { text-align: center; max-width: 560px; margin-inline: auto; margin-bottom: var(--space-16); }

.steps-grid {
  display: grid;
  grid-template-columns: 1fr auto 1fr auto 1fr;
  align-items: start;
  gap: var(--space-4);
}
@media (max-width: 768px) {
  .steps-grid { grid-template-columns: 1fr; }
  .step-arrow { display: none; }
}

.step {
  background: var(--color-base);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-8);
}
.step__number {
  width: 40px; height: 40px;
  border-radius: var(--radius-full);
  background: var(--color-accent-bg);
  border: 1px solid var(--color-accent-border);
  display: flex; align-items: center; justify-content: center;
  font-weight: var(--font-weight-bold);
  font-size: var(--text-sm);
  color: var(--color-accent);
  margin-bottom: var(--space-5);
}
.step__title { font-size: var(--text-lg); font-weight: var(--font-weight-semibold); margin-bottom: var(--space-3); }
.step__desc  { font-size: var(--text-body); color: var(--color-text-secondary); line-height: var(--line-height-relaxed); }

.step-arrow {
  font-size: var(--text-h2);
  color: var(--color-text-muted);
  align-self: center;
  padding-top: var(--space-6);
}
```

---

## Anti-patterns

```
✗ 3-column equal-size icon grid with heading + 1-line description
✗ Icons as the primary visual element (use product screenshots)
✗ Feature names that are marketing adjectives ("Powerful Analytics")
✗ Same visual treatment for all features (no hierarchy)
✗ Bullet points listing product attributes without evidence
✗ "Feature" naming without showing what the feature actually does
```

---

*Pattern version: global-design-skill v1.0 — `patterns/marketing-blocks/feature-sections.md`*
*Related: `rules/03-typography.md`, `rules/05-animation.md`, `examples/04-card-grid-cleanup.md`, `blueprints/landing-page-from-scratch.md`*
