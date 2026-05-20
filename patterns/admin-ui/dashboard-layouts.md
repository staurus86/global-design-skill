# Pattern — Dashboard Layouts

> A dashboard is a decision-support surface. Every element must help the operator answer one question or take one action. Decoration without information is noise.

---

## Dashboard Design Questions

Before layout:
```
Primary question this dashboard answers: [one specific question]
Primary action this dashboard enables:   [one specific action]
Update frequency:     [real-time / every N minutes / daily]
User expertise:       [daily operator / weekly reviewer / executive]
Data volume:          [3 KPIs / 10 metrics / 50+ data points]
Critical alerts:      [what must the user never miss?]
```

**High density is a feature for expert dashboards.** Every screen must show ≥ 3 visible differentiating data elements: actual numbers, status inferences, trends, comparisons. A dashboard with one big number and empty space is not a dashboard.

---

## Pattern A — KPI Header + Data Grid (standard analytics)

Best for: product analytics, sales dashboards, operational metrics.

```html
<div class="dashboard">
  <!-- Page header -->
  <div class="dashboard-header">
    <div class="dashboard-header__left">
      <h1>Overview</h1>
      <p class="dashboard-header__period">May 1 – May 20, 2026</p>
    </div>
    <div class="dashboard-header__right">
      <select class="dashboard-period-select" aria-label="Date range">
        <option>Last 7 days</option>
        <option selected>Last 30 days</option>
        <option>Last 90 days</option>
        <option>Custom range</option>
      </select>
      <button class="btn-ghost btn-sm">Export</button>
    </div>
  </div>

  <!-- KPI metric cards -->
  <div class="kpi-grid">
    <div class="kpi-card">
      <div class="kpi-card__header">
        <span class="kpi-label">Monthly revenue</span>
        <span class="kpi-trend kpi-trend--up" aria-label="Up 12% vs last period">
          ↑ 12%
        </span>
      </div>
      <div class="kpi-value">$84,210</div>
      <div class="kpi-secondary">vs $75,100 last month</div>
      <!-- Sparkline -->
      <svg class="kpi-sparkline" viewBox="0 0 120 32" aria-hidden="true">
        <polyline
          points="0,28 20,24 40,20 60,22 80,14 100,10 120,6"
          fill="none"
          stroke="var(--color-success)"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
      </svg>
    </div>

    <div class="kpi-card">
      <div class="kpi-card__header">
        <span class="kpi-label">Active users</span>
        <span class="kpi-trend kpi-trend--up" aria-label="Up 8%">↑ 8%</span>
      </div>
      <div class="kpi-value">10,427</div>
      <div class="kpi-secondary">847 new this month</div>
    </div>

    <div class="kpi-card kpi-card--alert">
      <div class="kpi-card__header">
        <span class="kpi-label">Churn rate</span>
        <span class="kpi-trend kpi-trend--down" aria-label="Down 2%, negative direction">↑ 2%</span>
      </div>
      <div class="kpi-value">3.8%</div>
      <div class="kpi-secondary">Above 3% threshold</div>
      <div class="kpi-alert-bar" aria-label="Alert: above threshold"></div>
    </div>

    <div class="kpi-card">
      <div class="kpi-card__header">
        <span class="kpi-label">Avg. response time</span>
        <span class="kpi-trend kpi-trend--neutral" aria-label="Unchanged">→ 0%</span>
      </div>
      <div class="kpi-value">142ms</div>
      <div class="kpi-secondary">p95: 380ms</div>
    </div>
  </div>

  <!-- Data content grid -->
  <div class="dashboard-grid">
    <!-- Large chart: main data view -->
    <div class="dashboard-card dashboard-card--wide">
      <div class="card-header">
        <h2>Revenue over time</h2>
        <div class="card-header__actions">
          <button class="tab-btn tab-btn--active">Daily</button>
          <button class="tab-btn">Weekly</button>
          <button class="tab-btn">Monthly</button>
        </div>
      </div>
      <div class="chart-container" aria-label="Revenue chart — see data table below for accessible version">
        <!-- Chart library renders here: Recharts / Nivo / D3 -->
        <!-- Always provide a data table alternative for accessibility -->
      </div>
    </div>

    <!-- Secondary panel -->
    <div class="dashboard-card">
      <div class="card-header">
        <h2>Top sources</h2>
        <a href="/analytics/sources" class="card-header__link">View all →</a>
      </div>
      <ul class="source-list">
        <li class="source-item">
          <span class="source-name">Direct</span>
          <div class="source-bar-wrap">
            <div class="source-bar" style="width: 64%" aria-label="64%"></div>
          </div>
          <span class="source-value">64%</span>
        </li>
        <li class="source-item">
          <span class="source-name">Search</span>
          <div class="source-bar-wrap">
            <div class="source-bar" style="width: 22%"></div>
          </div>
          <span class="source-value">22%</span>
        </li>
        <li class="source-item">
          <span class="source-name">Referral</span>
          <div class="source-bar-wrap">
            <div class="source-bar" style="width: 14%"></div>
          </div>
          <span class="source-value">14%</span>
        </li>
      </ul>
    </div>

    <!-- Activity feed -->
    <div class="dashboard-card">
      <div class="card-header">
        <h2>Recent activity</h2>
      </div>
      <ul class="activity-feed" aria-label="Recent activity">
        <li class="activity-item">
          <img src="/avatars/sarah.webp" alt="Sarah Chen" width="32" height="32" class="activity-item__avatar" />
          <div>
            <span><strong>Sarah Chen</strong> created project <a href="#">Alpha redesign</a></span>
            <time class="activity-item__time" datetime="2026-05-20T12:30:00">2 hours ago</time>
          </div>
        </li>
        <!-- More items… -->
      </ul>
    </div>
  </div>
</div>
```

```css
/* Dashboard layout */
.dashboard {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
  padding: var(--space-6) var(--space-8);
  max-width: 1440px;
}

/* Dashboard header */
.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: var(--space-4);
  flex-wrap: wrap;
}

.dashboard-header h1 { font-size: 1.5rem; }

.dashboard-header__period {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  margin-top: 2px;
}

.dashboard-header__right {
  display: flex;
  gap: var(--space-3);
  align-items: center;
}

.dashboard-period-select {
  height: 36px;
  padding-inline: var(--space-3);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-size: 0.875rem;
  color: var(--color-text-primary);
}

/* KPI grid */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-4);
}

.kpi-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-5) var(--space-6);
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  position: relative;
  overflow: hidden;
}

.kpi-card--alert {
  border-color: oklch(from var(--color-error) l c h / 0.4);
}

.kpi-alert-bar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--color-error);
}

.kpi-card__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.kpi-label {
  font-size: 0.8125rem;
  font-weight: 500;
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.kpi-trend {
  font-size: 0.8125rem;
  font-weight: 600;
  padding: 0.15em 0.5em;
  border-radius: 9999px;
}

.kpi-trend--up    { color: oklch(42% 0.18 145); background: oklch(94% 0.08 145); }
.kpi-trend--down  { color: oklch(38% 0.18 25);  background: oklch(94% 0.08 25); }
.kpi-trend--neutral { color: var(--color-text-muted); background: var(--color-surface-2); }

.kpi-value {
  font-size: clamp(1.5rem, 2.5vw, 2rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.2;
}

.kpi-secondary {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
}

.kpi-sparkline {
  width: 100%;
  height: 32px;
  margin-top: var(--space-2);
}

/* Dashboard content grid */
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-4);
}

.dashboard-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
  grid-column: span 4;
}

.dashboard-card--wide { grid-column: span 8; }

@media (max-width: 1024px) {
  .dashboard-card { grid-column: span 6; }
  .dashboard-card--wide { grid-column: span 12; }
}

@media (max-width: 640px) {
  .dashboard-card, .dashboard-card--wide { grid-column: span 12; }
}

/* Card header */
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-5);
}

.card-header h2 { font-size: 1rem; font-weight: 600; }

.card-header__link {
  font-size: 0.875rem;
  color: var(--color-accent);
  text-decoration: none;
}

.card-header__actions { display: flex; gap: var(--space-1); }

/* Tab buttons (in card header) */
.tab-btn {
  height: 28px;
  padding-inline: var(--space-3);
  border-radius: var(--radius-md);
  background: transparent;
  border: none;
  cursor: pointer;
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  transition: background 120ms, color 120ms;
}

.tab-btn--active {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
  font-weight: 500;
}

/* Chart container */
.chart-container { height: 240px; }

/* Source bars */
.source-list {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.source-item {
  display: grid;
  grid-template-columns: 80px 1fr 48px;
  align-items: center;
  gap: var(--space-3);
  font-size: 0.875rem;
}

.source-bar-wrap {
  height: 6px;
  background: var(--color-surface-2);
  border-radius: 9999px;
  overflow: hidden;
}

.source-bar {
  height: 100%;
  background: var(--color-accent);
  border-radius: 9999px;
}

.source-value {
  text-align: right;
  font-weight: 500;
  color: var(--color-text-muted);
}

/* Activity feed */
.activity-feed {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.activity-item {
  display: flex;
  gap: var(--space-3);
  align-items: flex-start;
  font-size: 0.875rem;
  line-height: 1.5;
}

.activity-item__avatar {
  border-radius: 50%;
  object-fit: cover;
  flex-shrink: 0;
}

.activity-item__time {
  display: block;
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  margin-top: 2px;
}
```

---

## Pattern B — Real-Time Operations Dashboard

Best for: server monitoring, incident response, live customer activity.

**Differences from analytics dashboard:**
- Data auto-refreshes every 30–60s (show last-updated timestamp)
- Critical alerts appear at the top as banners
- Status indicators use color + label + icon (never color alone)
- Dense layout: more data per screen, tighter spacing

```html
<!-- Alert banner: critical issues surface immediately -->
<div class="ops-alert" role="alert" aria-live="assertive">
  <span class="ops-alert__icon" aria-hidden="true">⚠</span>
  <strong>API p95 latency above threshold</strong>
  <span>380ms · Started 12 minutes ago</span>
  <a href="/incidents/481" class="ops-alert__link">View incident →</a>
</div>

<!-- Last updated indicator -->
<div class="dashboard-freshness" aria-live="polite" aria-atomic="true">
  Last updated: <time id="last-updated" datetime="2026-05-20T14:30:00">14:30:12</time>
  <button class="btn-ghost btn-xs" onclick="refreshData()">Refresh now</button>
</div>
```

```css
.ops-alert {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-3) var(--space-6);
  background: oklch(from var(--color-error) l c h / 0.1);
  border-bottom: 1px solid oklch(from var(--color-error) l c h / 0.3);
  font-size: 0.9375rem;
}

.ops-alert__icon { color: var(--color-error); }
.ops-alert__link {
  margin-left: auto;
  color: var(--color-accent);
  text-decoration: none;
  font-weight: 500;
  white-space: nowrap;
}

.dashboard-freshness {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  padding: var(--space-2) var(--space-6);
  border-bottom: 1px solid var(--color-border);
}
```

---

## Accessibility: Charts Must Have Data Table Alternatives

Every chart in a dashboard must have an accessible alternative for screen reader users.

```html
<div class="chart-wrapper">
  <div class="chart-canvas" aria-hidden="true">
    <!-- Chart renders here -->
  </div>

  <!-- Hidden from visual users; available to screen readers -->
  <details class="chart-data-table">
    <summary>View chart data as table</summary>
    <table>
      <caption>Revenue by month, May 2025 – May 2026</caption>
      <thead>
        <tr><th>Month</th><th>Revenue</th><th>Change</th></tr>
      </thead>
      <tbody>
        <tr><td>May 2025</td><td>$61,200</td><td>—</td></tr>
        <tr><td>Jun 2025</td><td>$64,800</td><td>+5.9%</td></tr>
        <!-- … -->
      </tbody>
    </table>
  </details>
</div>
```

---

## Anti-Patterns

- Decorative numbers with no trend or context ("10,427 users" with no comparison)
- Charts without labeled axes or data alternatives for screen readers
- Real-time dashboard without a "last updated" timestamp
- KPI cards where trend arrows mean different things per metric (↑ is good for revenue, bad for churn — label explicitly)
- Dashboard that requires scrolling to see the most critical metric
- Too many alerts: if everything is critical, nothing is critical

## Related Files

- `rules/12-admin-panels.md` — density principle, label-everything rule
- `patterns/admin-ui/data-tables.md` — tabular data below the dashboard
- `patterns/admin-ui/filters.md` — date range filtering for dashboard data
- `references/data-viz.md` — chart types, Recharts, accessible chart patterns
