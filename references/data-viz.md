# Reference — Data Visualization

> Charts, KPI cards, tables, and dashboards. Color palettes for data, accessible chart patterns, and component specifications for every chart type.

---

## When to Use Which Chart Type

| Goal | Chart | Library |
|---|---|---|
| Compare values across categories | Bar / column chart | Recharts, Visx |
| Show trends over time | Line chart | Recharts |
| Show composition | Donut / pie | Recharts |
| Show distribution | Histogram | Visx |
| Show correlation | Scatter plot | Visx |
| Show progress | Radial progress, gauge | Custom CSS/SVG |
| Show hierarchy | Treemap | Visx |
| Show single key metric | KPI card | Custom |
| Compare many values | Table | TanStack Table |

**Rule: if a table works, use a table.** Charts add cognitive load. Use a chart only when the visual pattern communicates something a table cannot.

---

## Chart Color Palette

Chart series must be distinguishable by both hue AND lightness (for color-blind users).

```css
:root {
  /* 8-series accessible palette — verified in grayscale */
  --chart-1: oklch(55% 0.22 258);   /* blue-violet — L55 */
  --chart-2: oklch(62% 0.20 25);    /* red-orange  — L62 */
  --chart-3: oklch(68% 0.18 145);   /* green       — L68 */
  --chart-4: oklch(50% 0.22 300);   /* purple      — L50 */
  --chart-5: oklch(72% 0.16 75);    /* amber       — L72 */
  --chart-6: oklch(45% 0.20 195);   /* teal-dark   — L45 */
  --chart-7: oklch(78% 0.14 330);   /* pink-light  — L78 */
  --chart-8: oklch(40% 0.18 258);   /* navy        — L40 */

  /* Dark mode — increase lightness ~10% */
  /* --chart-1-dark: oklch(65% 0.22 258); */
}
```

**Grayscale test:** Convert all 8 to grayscale — each must be a distinct gray shade. If two look the same, adjust `L`.

**Deuteranopia test:** Avoid using red + green as the only differentiator (most common color blindness). Always pair with shape, pattern, or label.

---

## KPI Card

The most common data display unit. Shows one metric with context.

```html
<article class="kpi-card" aria-label="Monthly recurring revenue">
  <div class="kpi-header">
    <span class="kpi-label">Monthly Recurring Revenue</span>
    <span class="kpi-trend kpi-trend--up" aria-label="Up 12% from last month">
      ↑ 12%
    </span>
  </div>

  <div class="kpi-value">
    <span class="kpi-number" aria-live="polite">$48,291</span>
  </div>

  <p class="kpi-context">
    +$5,200 vs. last month
  </p>

  <!-- Sparkline (optional) -->
  <svg class="kpi-sparkline" aria-hidden="true" role="img">
    <!-- 7-day trend line -->
  </svg>
</article>
```

```css
.kpi-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.kpi-label {
  font-size: var(--text-xs);
  font-weight: 500;
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.kpi-number {
  font-size: clamp(1.5rem, 3vw + 0.5rem, 2.5rem);
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  color: var(--color-text);
  line-height: 1.1;
}

.kpi-trend--up   { color: var(--color-success); }
.kpi-trend--down { color: var(--color-error); }
.kpi-trend--flat { color: var(--color-text-muted); }

.kpi-context {
  font-size: var(--text-xs);
  color: var(--color-text-muted);
}
```

### Animated counter on scroll entry

```ts
function animateCounter(el: HTMLElement, target: number, duration = 1200) {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  if (reduced) { el.textContent = target.toLocaleString(); return }

  const start = performance.now()
  const startVal = 0
  const format = (n: number) => Math.round(n).toLocaleString()

  const tick = (now: number) => {
    const progress = Math.min((now - start) / duration, 1)
    const eased = 1 - Math.pow(1 - progress, 3)   // ease-out cubic
    el.textContent = format(startVal + (target - startVal) * eased)
    if (progress < 1) requestAnimationFrame(tick)
  }

  requestAnimationFrame(tick)
}

const observer = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      const target = Number((e.target as HTMLElement).dataset.target)
      animateCounter(e.target as HTMLElement, target)
      observer.unobserve(e.target)
    }
  })
}, { threshold: 0.5 })

document.querySelectorAll('[data-counter]').forEach(el => observer.observe(el))
```

---

## Line Chart (Recharts)

```tsx
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from 'recharts'

interface DataPoint {
  date: string
  revenue: number
  users: number
}

function RevenueChart({ data }: { data: DataPoint[] }) {
  return (
    <div role="figure" aria-label="Revenue and user growth over 12 months">
      <ResponsiveContainer width="100%" height={280}>
        <LineChart
          data={data}
          margin={{ top: 8, right: 16, bottom: 0, left: 0 }}
        >
          <CartesianGrid
            strokeDasharray="4 4"
            stroke="oklch(87% 0.010 258)"
            vertical={false}     /* horizontal lines only — cleaner */
          />
          <XAxis
            dataKey="date"
            tick={{ fontSize: 11, fill: 'oklch(55% 0.010 258)' }}
            axisLine={false}
            tickLine={false}
          />
          <YAxis
            tick={{ fontSize: 11, fill: 'oklch(55% 0.010 258)' }}
            axisLine={false}
            tickLine={false}
            tickFormatter={v => `$${(v / 1000).toFixed(0)}k`}
          />
          <Tooltip
            contentStyle={{
              background: 'oklch(15% 0.013 258)',
              border: '1px solid oklch(26% 0.012 258 / 0.7)',
              borderRadius: '8px',
              fontSize: '12px',
            }}
          />
          <Legend />
          <Line
            type="monotone"
            dataKey="revenue"
            stroke="oklch(55% 0.22 258)"
            strokeWidth={2}
            dot={false}
            activeDot={{ r: 4 }}
          />
          <Line
            type="monotone"
            dataKey="users"
            stroke="oklch(62% 0.20 25)"
            strokeWidth={2}
            dot={false}
            activeDot={{ r: 4 }}
          />
        </LineChart>
      </ResponsiveContainer>

      {/* Accessible data table alternative */}
      <details className="chart-data-table">
        <summary className="sr-only">View data as table</summary>
        <table>
          <thead>
            <tr><th>Date</th><th>Revenue</th><th>Users</th></tr>
          </thead>
          <tbody>
            {data.map(row => (
              <tr key={row.date}>
                <td>{row.date}</td>
                <td>${row.revenue.toLocaleString()}</td>
                <td>{row.users.toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </details>
    </div>
  )
}
```

---

## Donut Chart (Progress / Composition)

```tsx
import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from 'recharts'

function DonutChart({
  data,
  label,
}: {
  data: { name: string; value: number }[]
  label: string
}) {
  const chartColors = [
    'oklch(55% 0.22 258)',
    'oklch(62% 0.20 25)',
    'oklch(68% 0.18 145)',
    'oklch(50% 0.22 300)',
  ]

  const total = data.reduce((sum, d) => sum + d.value, 0)

  return (
    <div role="figure" aria-label={label}>
      <ResponsiveContainer width="100%" height={200}>
        <PieChart>
          <Pie
            data={data}
            cx="50%"
            cy="50%"
            innerRadius={60}
            outerRadius={85}
            paddingAngle={3}
            dataKey="value"
            startAngle={90}
            endAngle={-270}
          >
            {data.map((entry, index) => (
              <Cell
                key={entry.name}
                fill={chartColors[index % chartColors.length]}
              />
            ))}
          </Pie>
          <Tooltip
            formatter={(value: number) =>
              [`${((value / total) * 100).toFixed(1)}%`, '']}
          />
        </PieChart>
      </ResponsiveContainer>
    </div>
  )
}
```

---

## Radial Progress Bar

For single-metric gauges (storage used, quota consumed, completion rate).

```css
.radial-progress {
  --progress: 0;   /* set via JS: style.setProperty('--progress', '0.72') */
  --size: 80px;
  --stroke: 6px;
  --color: var(--color-accent);

  width: var(--size);
  height: var(--size);
  display: grid;
  place-items: center;
  position: relative;
}

.radial-progress svg {
  position: absolute;
  inset: 0;
  transform: rotate(-90deg);
}

.radial-progress circle {
  fill: none;
  stroke-width: var(--stroke);
  stroke-linecap: round;
  r: calc(var(--size) / 2 - var(--stroke));
  cx: calc(var(--size) / 2);
  cy: calc(var(--size) / 2);
}

.radial-progress .track  { stroke: var(--color-surface-2); }
.radial-progress .fill   {
  stroke: var(--color);
  stroke-dasharray: calc(2 * 3.14159 * (var(--size) / 2 - var(--stroke)));
  stroke-dashoffset: calc(
    (1 - var(--progress)) * 2 * 3.14159 * (var(--size) / 2 - var(--stroke))
  );
  transition: stroke-dashoffset 800ms cubic-bezier(0.16, 1, 0.3, 1);
}

@media (prefers-reduced-motion: reduce) {
  .radial-progress .fill { transition: none; }
}
```

---

## Chart Design Rules

1. **Remove all non-data ink** — no decorative borders, excessive grid lines, or axis spines
2. **Label directly** when possible — eliminate the need for a legend
3. **Align decimals** — use `font-variant-numeric: tabular-nums` on all numeric data
4. **Mobile: horizontal bars > vertical bars** — easier to read rotated labels
5. **Always provide a data table alternative** — required for accessibility
6. **Never use 3D charts** — they distort perception and add no information
7. **Never use pie charts with > 5 slices** — use a sorted bar chart instead
8. **Color is not the only differentiator** — add pattern, label, or shape

---

## Chart Accessibility Checklist

```
[ ] role="figure" + aria-label on chart container
[ ] Data table alternative present (details/summary pattern)
[ ] Chart colors pass grayscale test
[ ] No red + green as only differentiators (deuteranopia)
[ ] Tooltip content readable by keyboard (tab-accessible)
[ ] Animated counters respect prefers-reduced-motion
[ ] KPI values wrapped in aria-live="polite"
[ ] Chart titles present and descriptive
```

---

*Reference version: global-design-skill v1.0 — `references/data-viz.md`*
*Related: `rules/11-data-tables.md`, `patterns/admin-ui/data-tables.md`, `references/accessibility.md`*
