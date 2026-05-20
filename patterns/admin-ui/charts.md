# Pattern — Charts

> Charts communicate data trends, comparisons, and distributions that would be invisible in a table. Choose the chart type for the data relationship, not for visual variety.

---

## Chart Type Selection

```
What you want to show              Best chart type
─────────────────────────────────────────────────────
Trend over time (1 series)         Line chart
Trend over time (2–5 series)       Multi-line chart
Comparison between categories      Bar chart (horizontal for long labels)
Part of a whole (2–5 slices)       Donut chart
Distribution of values             Histogram or box plot
Correlation between two variables  Scatter plot
Progress toward a target           Progress bar (not pie chart)
Single KPI vs. target              Stat card + sparkline
```

---

## Implementation Stack

| Use case | Library |
|---|---|
| Simple charts (line, bar, donut) | **Recharts** (React) or **Chart.js** |
| Complex, interactive dashboards | **Visx** or **Observable Plot** |
| High-performance large datasets | **uPlot** |
| Tiny inline sparklines | **CSS-only** or custom `<svg>` |

Never load a full charting library for sparklines — the bundle cost is not justified.

---

## Pattern 1 — Line Chart (Time Series)

```tsx
// Using Recharts (React)
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid,
  Tooltip, ResponsiveContainer, Legend
} from 'recharts'

interface DataPoint {
  date: string
  deployments: number
  failures?: number
}

interface DeployChartProps {
  data: DataPoint[]
}

function DeployChart ({ data }: DeployChartProps) {
  return (
    <div className="chart-wrap">
      <div className="chart-header">
        <h3 className="chart-title">Deployments</h3>
        <p className="chart-sub">Last 30 days</p>
      </div>
      <ResponsiveContainer width="100%" height={240}>
        <LineChart data={data} margin={{ top: 4, right: 4, bottom: 0, left: 0 }}>
          <CartesianGrid
            strokeDasharray="3 3"
            stroke="var(--color-border)"
            vertical={false}
          />
          <XAxis
            dataKey="date"
            axisLine={false}
            tickLine={false}
            tick={{ fill: 'var(--color-text-muted)', fontSize: 11 }}
            tickFormatter={d => d.slice(5)} /* MM-DD */
          />
          <YAxis
            axisLine={false}
            tickLine={false}
            tick={{ fill: 'var(--color-text-muted)', fontSize: 11 }}
            width={32}
          />
          <Tooltip content={<ChartTooltip />} />
          <Line
            type="monotone"
            dataKey="deployments"
            stroke="var(--color-accent)"
            strokeWidth={2}
            dot={false}
            activeDot={{ r: 4, fill: 'var(--color-accent)', strokeWidth: 0 }}
          />
          {data[0]?.failures !== undefined && (
            <Line
              type="monotone"
              dataKey="failures"
              stroke="var(--color-danger)"
              strokeWidth={2}
              dot={false}
              strokeDasharray="4 2"
              activeDot={{ r: 4, fill: 'var(--color-danger)', strokeWidth: 0 }}
            />
          )}
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}

function ChartTooltip ({ active, payload, label }: any) {
  if (!active || !payload?.length) return null
  return (
    <div className="chart-tooltip">
      <p className="chart-tooltip__label">{label}</p>
      {payload.map((entry: any) => (
        <div key={entry.dataKey} className="chart-tooltip__row">
          <span className="chart-tooltip__dot" style={{ background: entry.color }} />
          <span className="chart-tooltip__key">{entry.name}</span>
          <span className="chart-tooltip__val">{entry.value.toLocaleString()}</span>
        </div>
      ))}
    </div>
  )
}
```

---

## Pattern 2 — Bar Chart (Category Comparison)

```tsx
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from 'recharts'

interface RegionData {
  region: string
  requests: number
}

function RegionChart ({ data }: { data: RegionData[] }) {
  const max = Math.max(...data.map(d => d.requests))

  return (
    <div className="chart-wrap">
      <div className="chart-header">
        <h3 className="chart-title">Requests by region</h3>
        <p className="chart-sub">Last 24 hours</p>
      </div>
      <ResponsiveContainer width="100%" height={200}>
        <BarChart data={data} layout="vertical"
          margin={{ top: 0, right: 8, bottom: 0, left: 0 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="var(--color-border)" horizontal={false} />
          <XAxis type="number" axisLine={false} tickLine={false}
            tick={{ fill: 'var(--color-text-muted)', fontSize: 11 }}
            tickFormatter={v => v >= 1000 ? `${(v/1000).toFixed(0)}k` : v} />
          <YAxis type="category" dataKey="region" axisLine={false} tickLine={false}
            tick={{ fill: 'var(--color-text-secondary)', fontSize: 12 }} width={60} />
          <Tooltip content={<ChartTooltip />} />
          <Bar dataKey="requests" radius={[0, var(--radius-sm), var(--radius-sm), 0]} barSize={20}>
            {data.map((entry, i) => (
              <Cell
                key={i}
                fill={entry.requests === max
                  ? 'var(--color-accent)'
                  : 'oklch(from var(--color-accent) l c h / 0.35)'}
              />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}
```

---

## Pattern 3 — Donut Chart (Part-of-Whole)

Use only for 2–5 slices. More than 5 slices: use a horizontal bar chart instead.

```tsx
import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from 'recharts'

const STATUS_COLORS: Record<string, string> = {
  success:  'var(--color-success)',
  failed:   'var(--color-danger)',
  cancelled:'var(--color-warning)',
  skipped:  'var(--color-text-muted)',
}

function StatusDonut ({ data }: { data: { name: string; value: number }[] }) {
  const total = data.reduce((sum, d) => sum + d.value, 0)

  return (
    <div className="chart-wrap chart-wrap--donut">
      <div className="chart-header">
        <h3 className="chart-title">Build status</h3>
        <p className="chart-sub">Last 7 days</p>
      </div>
      <div className="donut-container">
        <ResponsiveContainer width={160} height={160}>
          <PieChart>
            <Pie
              data={data}
              cx="50%" cy="50%"
              innerRadius={52} outerRadius={72}
              dataKey="value"
              strokeWidth={2}
              stroke="var(--color-surface)"
            >
              {data.map((entry, i) => (
                <Cell key={i} fill={STATUS_COLORS[entry.name] || 'var(--color-border)'} />
              ))}
            </Pie>
            <Tooltip content={<ChartTooltip />} />
          </PieChart>
        </ResponsiveContainer>

        {/* Center label */}
        <div className="donut-center" aria-hidden="true">
          <span className="donut-center__value">{total.toLocaleString()}</span>
          <span className="donut-center__label">Total</span>
        </div>
      </div>

      {/* Legend */}
      <ul className="donut-legend">
        {data.map(d => (
          <li key={d.name} className="donut-legend__item">
            <span className="donut-legend__dot" style={{ background: STATUS_COLORS[d.name] }} />
            <span className="donut-legend__name">{d.name}</span>
            <span className="donut-legend__count">{d.value.toLocaleString()}</span>
            <span className="donut-legend__pct">{Math.round(d.value / total * 100)}%</span>
          </li>
        ))}
      </ul>
    </div>
  )
}
```

---

## Pattern 4 — Sparkline (Inline Trend)

For stat cards — a tiny trend line without axes. CSS-only or minimal SVG.

```tsx
function Sparkline ({ data, color = 'var(--color-accent)' }: { data: number[]; color?: string }) {
  const max = Math.max(...data)
  const min = Math.min(...data)
  const range = max - min || 1
  const h = 40; const w = 120
  const step = w / (data.length - 1)

  const points = data
    .map((v, i) => `${i * step},${h - ((v - min) / range) * h}`)
    .join(' ')

  return (
    <svg
      className="sparkline"
      width={w} height={h}
      viewBox={`0 0 ${w} ${h}`}
      aria-hidden="true"
      role="img"
    >
      <polyline
        points={points}
        fill="none"
        stroke={color}
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  )
}
```

---

## CSS for Chart Containers

```css
.chart-wrap {
  background: var(--color-surface-2);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
}

.chart-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: var(--space-4);
}

.chart-title {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-primary);
}

.chart-sub {
  font-size: 12px;
  color: var(--color-text-muted);
}

/* Custom tooltip */
.chart-tooltip {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
  padding: var(--space-3) var(--space-4);
  min-width: 140px;
}

.chart-tooltip__label {
  font-size: 11px;
  color: var(--color-text-muted);
  margin-bottom: var(--space-2);
  font-weight: var(--font-weight-medium);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.chart-tooltip__row {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
}

.chart-tooltip__dot {
  width: 8px; height: 8px;
  border-radius: var(--radius-full);
  flex-shrink: 0;
}

.chart-tooltip__key { color: var(--color-text-secondary); flex: 1; }
.chart-tooltip__val { color: var(--color-text-primary); font-weight: var(--font-weight-semibold); }

/* Donut */
.donut-container { position: relative; width: 160px; margin-inline: auto; }

.donut-center {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  pointer-events: none;
}

.donut-center__value {
  font-size: var(--text-h3);
  font-weight: 700;
  color: var(--color-text-primary);
  line-height: 1;
}

.donut-center__label {
  font-size: 11px;
  color: var(--color-text-muted);
}

.donut-legend {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  margin-top: var(--space-4);
  list-style: none;
  padding: 0;
}

.donut-legend__item {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
}

.donut-legend__dot {
  width: 8px; height: 8px;
  border-radius: var(--radius-full);
  flex-shrink: 0;
}

.donut-legend__name { flex: 1; color: var(--color-text-secondary); }
.donut-legend__count { color: var(--color-text-primary); font-weight: var(--font-weight-medium); }
.donut-legend__pct { color: var(--color-text-muted); }

.sparkline { display: block; }
```

---

## Accessibility

```
- Every chart must have a text alternative:
    <figure role="figure" aria-label="Deployments over the last 30 days">
      [chart component]
      <figcaption class="sr-only">
        Table showing daily deployment counts from [date] to [date].
      </figcaption>
    </figure>

- Provide data table behind a disclosure for screen reader users
- Never use color alone to distinguish chart series — add shape or label differences
- Ensure tooltip text color meets 4.5:1 contrast against tooltip background
- Reduced motion: disable animation on chart mount when prefers-reduced-motion: reduce
```

---

## Anti-Patterns

```
× Pie chart with more than 5 slices — use horizontal bar
× 3D charts — no information added, perspective distorts values
× Dual Y-axis charts — almost always misleading
× Animation that replays on every render — animate once on mount
× Missing units on axes (no "ms", "requests", "$") 
× Chart without a title — user cannot interpret data without context
× Truncating Y-axis to exaggerate small differences
× Using color palette that fails color-blind accessibility
```

---

*Pattern version: global-design-skill v1.0 — `patterns/admin-ui/charts.md`*  
*Related: `patterns/admin-ui/bulk-actions.md`, `rules/11-data-tables.md`, `rules/07-accessibility.md`*
