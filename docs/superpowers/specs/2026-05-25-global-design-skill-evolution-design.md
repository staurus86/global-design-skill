# Global Design Skill — Full Evolution Design
**Date:** 2026-05-25  
**Status:** Approved  
**Scope:** 4-phase evolution from static markdown skill to self-evolving design intelligence

---

## Problem Statement

Global Design Skill is domain-agnostic — it provides universal rules (typography, grid, states) but has no awareness of business niches. Given a request for an industrial equipment manufacturer vs. a bicycle shop vs. a tarot reader, it produces the same generic structure. The skill also lacks automated validation, has no learning capability, and requires manual file copying into context.

**Root cause:** The skill answers HOW to design, but not WHAT to design FOR WHOM.

**Goal:** Evolve the skill through 4 phases into a system that automatically detects the user's niche, retrieves or learns domain-specific rules, applies them, and improves over time based on feedback.

---

## Architecture Overview

```
Phase 1 — Content Layer         Static markdown files, works immediately
Phase 2 — MCP Static Server     Python tools, file-based sector context
Phase 3 — Learning Engine       Web scraping, pattern extraction, knowledge base
Phase 4 — SEDI Full             Perception → Cognition → Execution → Feedback → Evolution
```

Each phase is independently useful and non-breaking to the existing skill.

### Repository Structure (final state)

```
global-design-skill/
├── [all existing files — unchanged]
│
├── industries/                        Phase 1
│   ├── _index.md
│   ├── b2b-products.md
│   ├── b2c-products.md
│   ├── services.md
│   ├── content-media.md
│   ├── education.md
│   ├── health.md
│   ├── finance.md
│   ├── real-estate.md
│   ├── travel.md
│   ├── tech-saas.md
│   ├── non-profit.md
│   └── entertainment.md
│
├── patterns/states/                   Phase 1
│   ├── skeleton-states.md
│   ├── partial-error-states.md
│   ├── offline-states.md
│   ├── permission-states.md
│   └── rate-limit-states.md
│
├── validators/                        Phase 1
│   ├── lighthouse-ci.md
│   ├── axe-core.md
│   └── bundle-analyzer.md
│
├── feedback/                          Phase 1
│   ├── gate-8-tracker.md
│   └── iteration-log.md
│
├── mcp-server/                        Phase 2
│   ├── README.md
│   ├── pyproject.toml
│   ├── server.py
│   └── tools/
│       ├── sector_context.py
│       ├── industry_rules.py
│       └── design_audit.py
│
├── learning/                          Phase 3
│   ├── sector_classifier.py
│   ├── pattern_extractor.py
│   ├── ethical_scraper.py
│   ├── gap_detector.py
│   └── knowledge_base.py
│
└── sedi/                              Phase 4
    ├── perception.py
    ├── cognition.py
    ├── execution.py
    ├── feedback_engine.py
    ├── evolution.py
    └── local_store/
```

---

## Phase 1 — Content Layer

### industries/ (12 files)

Each file follows a uniform structure:

```markdown
# [Sector Name]
## Sector Profile
- Decision pattern, risk level, key users

## Required Elements
- Bulleted list of mandatory page elements

## Banned Patterns
- What to never do in this sector

## Trust Signals
- How to build trust for this audience

## Conversion Path
- Awareness → Consideration → Decision → Action flow

## Typical Page Structure
- Ordered sections

## Quick Diagnosis
- 5 questions that determine the design pattern
```

**Sectors:**

| File | Sector | Example niches |
|------|--------|---------------|
| `b2b-products.md` | B2B Products & Services | Industrial equipment, SaaS, logistics |
| `b2c-products.md` | B2C Physical Products | Bicycles, electronics, furniture |
| `services.md` | B2C Services | Tarot, cleaning, fitness, legal |
| `content-media.md` | Content & Media | Blog, podcast, news, magazine |
| `education.md` | Education & Training | Courses, academies, corporate training |
| `health.md` | Health & Medicine | Clinics, telemedicine, wellness |
| `finance.md` | Finance & Fintech | Banking, insurance, crypto |
| `real-estate.md` | Real Estate | Agencies, developers, rentals |
| `travel.md` | Travel & Hospitality | Hotels, tours, restaurants |
| `tech-saas.md` | Tech & Startups | AI, SaaS, hardware, IoT |
| `non-profit.md` | Non-profit & Government | NGOs, foundations, civic services |
| `entertainment.md` | Entertainment & Culture | Games, streaming, events, sports |

**Integration with existing skill:** `industries/_index.md` is referenced in `integrations/claude-code/CLAUDE.md` — AI reads the relevant sector file on any business-context request.

### patterns/states/ (5 files)

Extensions to existing 9-state system (idle/hover/active/focus/disabled/loading/empty/error/success):

- **skeleton-states.md** — shimmer, pulse, structural preview. When to use skeleton vs spinner.
- **partial-error-states.md** — table loaded but 2 rows failed, partial API response patterns.
- **offline-states.md** — PWA offline mode, sync queue indicators, reconnection UX.
- **permission-states.md** — no access, upgrade required, locked feature, role-based visibility.
- **rate-limit-states.md** — too many requests, cooldown timer, retry guidance.

### validators/ (3 files)

Documentation on integrating automated quality checks:

- **lighthouse-ci.md** — performance budgets (LCP < 2.5s, CLS < 0.1, FID < 100ms), CI configuration.
- **axe-core.md** — a11y testing thresholds, how to configure in Jest/Playwright.
- **bundle-analyzer.md** — size limits per component type, tree-shaking checklist.

### feedback/ (2 files)

Templates for measuring skill effectiveness:

- **gate-8-tracker.md** — log template for "developer asked a question after handoff" events.
- **iteration-log.md** — template for recording iteration count before design acceptance.

---

## Phase 2 — MCP Static Server

**Location:** `mcp-server/` in the repository  
**Tech:** Python 3.11+, `fastmcp`, `markdown-it-py`  
**Purpose:** Thin layer between `industries/` files and AI — no database, no state

### 5 MCP Tools

```python
list_sectors() -> str
# Returns all 12 sectors with one-line descriptions

classify_niche(query: str) -> str
# Detects sector from user query text
# "сайт для производителя насосов" → {"sector": "b2b-products", "confidence": 0.9}

get_sector_context(sector: str, niche: str = None) -> str
# Returns full context: required elements, banned patterns,
# trust signals, conversion path. Reads from industries/*.md

check_banned_patterns(sector: str, content: str) -> str
# Checks design description for sector-specific banned patterns

get_quick_diagnosis(who_pays: str, decision_type: str, risk_level: str,
                    choice_type: str, user_value: str) -> str
# Takes 5 diagnostic answers → returns recommended sector pattern
```

### Data Flow

```
AI request → classify_niche() → get_sector_context() → industries/b2b-products.md
                                                       ↑
                                              plain markdown file,
                                              editable by hand
```

### Integration Instructions

`mcp-server/README.md` covers setup for:
- Claude Code (`~/.claude/settings.json`)
- Cursor (`.cursor/mcp.json`)
- Windsurf (`.windsurf/mcp.json`)

### Dependencies

```toml
[project]
dependencies = [
    "mcp>=1.0",
    "fastmcp>=0.1",
    "markdown-it-py>=3.0",
]
```

---

## Phase 3 — Learning Engine

**Location:** `learning/`  
**Purpose:** When a niche is not in `industries/`, automatically find references, extract patterns, and save to local knowledge base

### 5 Modules

**`sector_classifier.py`**  
Keyword-weighted sector detection. Input: query string. Output: sector + confidence score. No ML — pure keyword matching against `SECTOR_KEYWORDS` dict (12 sectors × ~10 keywords each).

**`pattern_extractor.py`**  
Parses HTML/CSS and extracts:
- Layout structure (header type, hero type, grid, footer)
- Components (search, carousel, testimonials, pricing table, FAQ, multi-step form)
- Trust signals (certifications, client logos, reviews, guarantees, security badges)
- Conversion elements (CTA buttons, lead forms, pricing, demo requests, free trials)

**`ethical_scraper.py`**  
HTTP client with:
- `robots.txt` compliance check before every request
- Rate limiting: 10 requests/minute
- User-Agent: `GlobalDesignSkill-Bot/1.0 (Learning/Reference Collection)`
- Search integration for finding reference sites by sector/niche

**`gap_detector.py`**  
Compares extracted patterns against existing `industries/*.md` content. Returns list of missing elements, outdated patterns, and improvement suggestions.

**`knowledge_base.py`**  
JSON storage at `~/.global-design-skill/knowledge/`. Schema:

```json
{
  "sector": "b2b-products",
  "niche": "industrial-pumps",
  "confidence_score": 0.85,
  "usage_count": 0,
  "success_rate": 0.0,
  "learned_at": "2026-05-25T00:00:00Z",
  "last_updated": "2026-05-25T00:00:00Z",
  "patterns": {
    "layout": [],
    "components": [],
    "visual": [],
    "interaction": []
  },
  "rules": {
    "required_elements": [],
    "banned_patterns": [],
    "trust_signals": [],
    "conversion_elements": []
  },
  "references": [
    {"url": "...", "quality_score": 0.9}
  ]
}
```

### 2 New MCP Tools (extends Phase 2)

```python
learn_from_reference(url: str, sector: str = None, niche: str = None) -> str
# Scrapes site, extracts patterns, saves to knowledge_base
# Returns extracted patterns and gaps vs existing knowledge

get_or_learn_sector(sector: str, niche: str) -> str
# 1. Check industries/*.md
# 2. Check knowledge_base
# 3. If not found → auto-trigger learn_from_reference on top reference sites
# Guaranteed to return context
```

### Learning Workflow

```
Query: "сайт для производителя промышленных насосов"
  ↓
classify_niche()         → "b2b-products / industrial-pumps"
  ↓
knowledge_base.get()     → not found
  ↓
ethical_scraper.search() → 10 references (Grundfos, KSB, Sulzer...)
  ↓
pattern_extractor()      → [configurator, rfq-form, technical-specs, certifications]
  ↓
knowledge_base.save()    → ~/.global-design-skill/knowledge/b2b-products/industrial-pumps.json
  ↓
get_sector_context()     → returns niche-specific context
```

---

## Phase 4 — SEDI Full Architecture

**Location:** `sedi/`  
**Purpose:** Orchestrates all layers, adds personalization through pattern weights, feedback loop, and periodic evolution

### 6 Modules

**`perception.py` — Request Analysis**

```python
@dataclass
class RequestAnalysis:
    intent: Literal["create", "improve", "audit", "learn", "compare"]
    sector: str
    niche: str
    context: dict   # has_existing_design, has_reference, has_constraints
    emotions: dict  # urgent, frustrated, confused
    constraints: dict  # budget, timeline, tech_stack, style
```

**`cognition.py` — Decision Making**

Knowledge lookup priority:
1. Local knowledge base (personalized, user-specific)
2. `industries/*.md` (static, universal)
3. Learning Mode (auto-triggered)

Selects blueprint based on intent:
- `create` → `blueprints/landing-page-from-scratch.md` (or sector-appropriate)
- `improve` → `blueprints/redesign-existing-page.md`
- `audit` → relevant checklist

Applies pattern weights — patterns with high weight for this user/sector get prioritized.

**`execution.py` — Design Generation**

Applies blueprint + patterns + rules → structured design output.  
Runs Quality Gates validation before returning.  
Each decision includes source explanation: *"RFQ form required by b2b-products rules, confirmed by Grundfos.com reference"*

**`feedback_engine.py` — Learning from Interaction**

Explicit signals: rating 1-5, liked/disliked patterns, comments  
Implicit signals: `revision_count > 3` → pattern underperforming  
Effect: pattern weights adjusted ±10% per interaction, capped at [0.1, 2.0]

**`evolution.py` — Periodic Self-Improvement**

Weekly cycle:
1. Calculate `effectiveness_score = success_rate × confidence` per niche
2. Re-train niches with `effectiveness_score < 0.5`
3. Identify successful pattern combinations → generate composite patterns
4. Log all changes to `local_store/evolution_log/`

**`local_store/` — Personal Knowledge Base**

```
~/.global-design-skill/
├── knowledge/           learned niches (from Phase 3)
├── weights/             pattern weights per sector
│   └── b2b-products.json
├── feedback/            interaction history
│   └── 2026-05/
└── evolution_log/       what changed and why
```

### SEDI Principles

- **Local-only:** No data leaves the user's machine
- **Transparent:** Every decision cites its source
- **Controllable:** User can edit or delete any learned knowledge
- **Additive:** Each phase works without the next; SEDI enhances but doesn't replace

---

## Phase Dependencies

```
Phase 1 (content)  →  required by all phases
Phase 2 (MCP)      →  requires Phase 1 industries/ files
Phase 3 (learning) →  extends Phase 2 MCP with 2 new tools
Phase 4 (SEDI)     →  orchestrates Phase 2 + Phase 3 + adds weights/feedback
```

---

## Success Criteria per Phase

| Phase | Done when |
|-------|-----------|
| Phase 1 | 12 industry files + 5 state files present; CLAUDE.md updated to reference industries/ |
| Phase 2 | MCP server starts; all 5 tools return correct data; README covers 3 IDE integrations |
| Phase 3 | `get_or_learn_sector("b2b-products", "industrial-pumps")` returns context without manual input |
| Phase 4 | After 3 interactions with feedback, pattern weights change measurably |

---

## Out of Scope

- Multi-agent orchestration (design-director → design-critic pipeline) — existing agents handle this
- Figma plugin integration — separate project
- Community contributions / crowdsourced industries — post-launch
- A/B test result integration — requires external analytics hookup
