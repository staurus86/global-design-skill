# Rule 13 — SaaS Products

> SaaS UI must work for Day 1 users and Day 365 power users simultaneously. Every screen answers: who is this for right now, and what do they need to do?

---

## The Dual User Problem

A SaaS product serves two radically different users of the same account:

**Day 1 user:** Confused, skeptical, looking for the promised value. Needs guidance, empty states that explain, onboarding that leads to the "aha moment."

**Day 365 user:** Expert, has learned patterns, needs efficiency. Hates tutorials, wants keyboard shortcuts, needs information density.

**Rule:** Design for Day 365 as the primary state. Design Day 1 as a layer on top — onboarding flows, empty states, guided prompts — that disappears as the user advances.

**Banned:** Designing for Day 1 throughout (creates a product that feels like it has training wheels forever). Designing for Day 365 only (causes churn before users ever reach that state).

---

## Rules

### R1 — The aha moment is the north star

Every SaaS product has a moment where the user first experiences the core value. Design every screen in the onboarding flow to reach that moment as fast as possible.

**Find it:**
```
Aha moment: [the first moment the user experiences the product's value]
Example for project tool: "First task created and assigned"
Example for analytics: "First dashboard showing real data"
Example for email tool: "First campaign sent to real contacts"
```

**Design implication:** Every step between signup and the aha moment is overhead. Remove or defer everything that isn't required to reach the aha moment.

---

### R2 — Empty states are product moments

The empty state is the first thing a new user sees. It is not a blank screen, a "no data" message, or a generic illustration.

**Empty state formula:**
```
[Visual: specific to this product — not generic]
[Why it's empty: honest, specific]
[What to do: one action, directly actionable]
```

**Good:**
```
[Screenshot preview of what populated looks like]
"Your analytics will appear here once your first visitor arrives."
[Copy tracking snippet]
```

**Bad:**
```
[Generic "empty box" illustration]
"No data yet"
[No action]
```

**Rules:**
- Visual shows what the populated state looks like (creates desire)
- Copy names the specific content that's missing (not "no data")
- One CTA goes directly to the creation action (not to settings or documentation)
- Never show a skeleton loader for a genuinely empty state

---

### R3 — Onboarding follows the Minimum Viable Steps principle

The number of steps between signup and aha moment should be the minimum required to deliver value — nothing else.

**Step evaluation:**
For each step, ask: "Can the user reach the aha moment without completing this step?"
- If yes: make it optional, or move it to post-activation
- If no: keep it

**Maximum onboarding steps to aha moment:** 3-4. More than 5 causes significant drop-off.

**Required per step:**
- Progress indicator (visible count: "Step 2 of 4")
- Skip option for non-critical steps
- One primary action per step
- Clear "Why this matters" if the step isn't self-evident

---

### R4 — Navigation for complex products

SaaS products grow. Plan the navigation for 2-year scale, not 3-month scope.

**Structure:**
- Primary nav (sidebar or top): top-level product areas, ≤ 7 items
- Secondary nav: context within the area (tabs, sub-navigation)
- Utility nav (top bar): search, notifications, user profile, help

**Navigation naming:**
- Use what the user does, not what the product contains
- "Projects" (noun) → "My projects" or "Create project" is clearer
- "Reporting" → keep as-is if that's the clear mental model

**Collapsible sidebar for power users:**
- Collapsed: icon-only, 64px width
- Expanded: icon + label, 240px width
- Preference persists to localStorage

---

### R5 — Real-time feedback on every action

The Doherty Threshold: any gap > 400ms between user action and system response causes the user to perceive the product as "slow" or "broken," even if the action completes correctly.

**Implementation:**
```tsx
// Pattern: optimistic update + server sync
const [optimisticItems, addOptimistic] = useOptimistic(items)

async function handleCreate(formData: FormData) {
  // 1. Update UI immediately (0ms delay)
  addOptimistic({ id: 'temp', ...formValues, status: 'creating' })

  // 2. Sync with server
  const result = await createItem(formData)

  // 3. Replace optimistic with real data (handled by React)
}
```

**Minimum feedback requirements:**
- Button click: visual state change within 16ms (one frame)
- Form submit: loading state on button within 100ms
- Network operation: progress indicator within 200ms
- Completion: success feedback within 400ms of operation completing

---

### R6 — Subscription and billing clarity

Billing confusion is a support burden and a churn driver.

**Rules:**
- Current plan always visible (in account settings, in sidebar, on billing page)
- Usage limits visible before they're hit (not only at 100%)
- Overage warning: notify at 80% of plan limit
- Trial status: always visible ("12 days remaining in trial")
- Upgrade prompt: appears when user hits a limit, never randomly
- Downgrade: possible, consequences clearly stated before confirmation

**Upgrade prompt anatomy:**
```
[Feature they tried to use]
"This feature requires the Growth plan."
[What they get with the upgrade — specific]
[Upgrade button]  [Learn more]  (never lock without explanation)
```

---

### R7 — Notification model must be designed before building

Notifications that appear randomly or too frequently become ignored or disabled.

**Define the notification matrix:**

| Event | Channel | Frequency limit | Can disable? |
|---|---|---|---|
| Item assigned to user | In-app + email | Immediate | Yes |
| Comment mentioning user | In-app + email | Immediate | Yes |
| Weekly digest | Email only | Weekly | Yes |
| Trial ending in 3 days | In-app + email | Once | No |
| Plan limit reached | In-app only | Once per period | No |
| Security event (new login) | Email only | Immediate | No |

**In-app notification center:**
- Badge count on bell icon
- Dropdown: last 10 notifications, grouped by type
- "Mark all as read"
- "See all notifications" → full notification history page

---

### R8 — Settings architecture

Settings must be findable. Settings must be organized by user mental model, not by product architecture.

**Standard structure:**
```
Profile          (name, email, avatar, timezone, language)
Account          (plan, billing, invoices, usage)
Notifications    (per-event toggles, per-channel toggles)
Workspace        (for multi-user: name, branding, members)
Integrations     (connected apps, API keys, webhooks)
Security         (password, 2FA, sessions, connected devices)
Danger zone      (delete account, export data)
```

**Rules:**
- Danger zone always last, visually separated with a red border or section divider
- Changes save immediately for toggles; require explicit Save for forms
- Saved confirmation: inline "Saved" badge near the changed field (not a page-level toast for every toggle)

---

### R9 — Error recovery is a product feature

Users encounter errors. How the product handles errors determines whether users trust it.

**Error hierarchy:**

| Type | Display | Auto-dismiss? | Recovery action |
|---|---|---|---|
| Field validation | Below field, immediate | No | User corrects |
| Form submission | Above submit button | No | User corrects |
| Network error (retry-able) | Toast + Retry button | No | Retry button |
| Server error (not retry-able) | Full-page or inline error state | No | Contact support |
| Session expired | Modal (blocking) | No | Re-login |

**Copy formula:** `[What failed] + [Why] + [How to recover]`

"Failed to save changes — your connection dropped. Check your network and try again."

---

### R10 — Performance is product quality

SaaS users pay monthly. Performance below expectation is a reason to cancel.

**Targets:**
- Time to first meaningful data: < 1.5s (after login)
- Dashboard load: < 2s with real data
- Action response (create, update, delete): < 200ms (optimistic) + < 2s (server)

**Implementation:**
```tsx
// Cache with Next.js 16 "use cache"
'use cache'
export async function getDashboardData(userId: string) {
  const data = await db.dashboard.get(userId)
  cacheLife('minutes')
  return data
}

// Instant feedback with useOptimistic
// Skeleton loaders that match the real layout
// Prefetch on hover for navigation links
```

---

## SaaS Product Checklist

```
[ ] Aha moment defined and documented
[ ] Empty state: product-specific visual + why + one direct action
[ ] Onboarding: ≤ 4 steps to aha moment
[ ] Navigation: ≤ 7 primary items, plannable for 2-year scale
[ ] Every action has visual feedback within 400ms (Doherty Threshold)
[ ] Billing: current plan + usage visible at all times
[ ] Upgrade prompt: contextual to limit hit, not random
[ ] Notification matrix defined before building
[ ] Settings: organized by user mental model, Danger Zone last
[ ] Error messages: what + why + how to recover
[ ] Performance: dashboard load < 2s with real data
```

## Related Files

- `blueprints/saas-app-from-scratch.md` — full build protocol
- `agents/ux-architect.md` — onboarding flow review
- `patterns/product-ui/onboarding.md` — onboarding implementation patterns
- `patterns/product-ui/empty-states.md` — empty state patterns
- `patterns/product-ui/error-states.md` — error recovery patterns
- `patterns/product-ui/settings-pages.md` — settings patterns
- `checklists/ui-review.md` — full UI review checklist
