# Phase 3 — Learning Engine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a 5-module learning engine that automatically finds reference sites, scrapes them ethically, extracts design patterns, detects gaps versus static industry files, and saves findings to a local JSON knowledge base. Extend the Phase 2 MCP server with 2 new tools.

**Architecture:** Five focused Python modules in `learning/`. Each module has one responsibility. The MCP server in `mcp-server/` gains two new tools: `learn_from_reference` and `get_or_learn_sector`. Knowledge is stored as JSON at `~/.global-design-skill/knowledge/`. No external database.

**Tech Stack:** Python 3.11+, `requests`, `beautifulsoup4`, `PyYAML`, `pytest>=8.0`

**Prerequisite:** Phase 1 and Phase 2 complete.

---

## File Map

**Create:**
```
learning/
  __init__.py
  sector_classifier.py    — keyword-weighted sector detection
  pattern_extractor.py    — HTML/CSS pattern extraction
  ethical_scraper.py      — robots.txt-respecting HTTP client
  gap_detector.py         — compare extracted vs static rules
  knowledge_base.py       — JSON storage at ~/.global-design-skill/

mcp-server/tools/
  learning_tools.py       — learn_from_reference, get_or_learn_sector MCP tools

tests/learning/
  __init__.py
  test_sector_classifier.py
  test_knowledge_base.py
  test_gap_detector.py
  fixtures/
    sample_html.html      — minimal HTML for extractor tests
```

**Add dependency to:**
```
mcp-server/pyproject.toml  — add requests, beautifulsoup4
```

---

## Task 1: `sector_classifier.py`

**Files:**
- Create: `learning/__init__.py`
- Create: `learning/sector_classifier.py`
- Create: `tests/learning/__init__.py`
- Create: `tests/learning/test_sector_classifier.py`

- [ ] **Step 1: Write failing test**

```python
# tests/learning/test_sector_classifier.py
import pytest
from learning.sector_classifier import classify_sector

def test_classifies_b2b():
    result = classify_sector("industrial pump manufacturer B2B equipment")
    assert result["sector"] == "b2b-products"
    assert result["confidence"] >= 0.6

def test_classifies_services():
    result = classify_sector("tarot reader booking website")
    assert result["sector"] == "services"
    assert result["confidence"] >= 0.6

def test_unknown_returns_low_confidence():
    result = classify_sector("xyzzy frobble nonce")
    assert result["confidence"] < 0.5
    assert result["sector"] == "unknown"

def test_returns_required_keys():
    result = classify_sector("online shop")
    assert "sector" in result
    assert "confidence" in result
    assert "sub_niche" in result
    assert "alternatives" in result
```

- [ ] **Step 2: Run to confirm it fails**

```bash
python -m pytest tests/learning/test_sector_classifier.py -v 2>&1 | head -10
```
Expected: `ModuleNotFoundError: No module named 'learning'`

- [ ] **Step 3: Write `learning/sector_classifier.py`**

```python
# learning/sector_classifier.py
"""Keyword-weighted sector classification for niche detection."""

SECTOR_KEYWORDS: dict[str, list[str]] = {
    "b2b-products": [
        "manufacturer", "manufacturing", "industrial", "equipment", "machinery",
        "factory", "supplier", "wholesale", "oem", "b2b", "насос", "pump",
        "станок", "завод", "поставщик", "производитель", "оборудование",
        "cnc", "логистика", "logistics", "consulting", "rfq",
    ],
    "b2c-products": [
        "shop", "store", "buy", "cart", "retail", "ecommerce", "product",
        "fashion", "electronics", "furniture", "bicycle", "велосипед",
        "магазин", "интернет-магазин", "купить", "электроника", "мебель",
    ],
    "services": [
        "booking", "appointment", "therapy", "coaching", "session", "tarot",
        "таролог", "тренер", "trainer", "клининг", "cleaning", "fitness",
        "legal", "юридический", "психолог", "service provider",
    ],
    "content-media": [
        "blog", "news", "magazine", "podcast", "media", "article",
        "новости", "блог", "журнал", "портал", "editorial", "publication",
    ],
    "education": [
        "course", "learn", "training", "academy", "school", "university",
        "certification", "курс", "обучение", "академия", "bootcamp",
        "curriculum", "lesson", "syllabus",
    ],
    "health": [
        "clinic", "hospital", "medical", "doctor", "dental", "wellness",
        "клиника", "стоматолог", "врач", "медицин", "therapy", "healthcare",
    ],
    "finance": [
        "bank", "invest", "insurance", "crypto", "payment", "fintech",
        "банк", "инвестиц", "страховая", "финансов", "кредит",
    ],
    "real-estate": [
        "property", "real estate", "apartment", "house", "mortgage",
        "недвижимость", "квартира", "аренда", "застройщик", "новостройка",
    ],
    "travel": [
        "hotel", "tour", "restaurant", "vacation", "booking", "trip",
        "отель", "ресторан", "туризм", "путешествие", "food delivery",
    ],
    "tech-saas": [
        "saas", "software", "platform", "api", "cloud", "developer",
        "разработчик", "платформа", "аналитика", "analytics", "startup",
    ],
    "non-profit": [
        "charity", "nonprofit", "ngo", "foundation", "donate", "volunteer",
        "благотворительн", "фонд", "НКО", "ecological", "environmental",
    ],
    "government": [
        "government", "municipal", "portal", "citizen", "public service",
        "госуслуг", "государственн", "муниципальн", "администрация",
    ],
    "entertainment": [
        "game", "gaming", "stream", "streaming", "event", "concert",
        "игра", "стриминг", "кино", "музыка", "casual", "aaa", "esports",
    ],
}

SUB_NICHE_KEYWORDS: dict[str, dict[str, list[str]]] = {
    "entertainment": {
        "casual-games": ["casual", "mobile game", "hyper-casual", "казуальн"],
        "aaa-games": ["aaa", "console", "fps", "rpg", "шутер", "open world"],
        "streaming": ["stream", "subscription", "series", "стриминг", "подписка"],
        "live-events": ["concert", "festival", "ticket", "concert", "концерт", "фестиваль"],
    }
}


def classify_sector(query: str) -> dict:
    """Classify a query string into a sector.

    Returns dict: {sector, confidence, sub_niche, alternatives}
    """
    q = query.lower()
    scores: dict[str, float] = {}

    for sector, keywords in SECTOR_KEYWORDS.items():
        score = sum(1.0 for kw in keywords if kw.lower() in q)
        if score > 0:
            scores[sector] = score

    if not scores:
        return {"sector": "unknown", "confidence": 0.0, "sub_niche": None, "alternatives": []}

    total = sum(scores.values())
    sorted_sectors = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_sector, top_score = sorted_sectors[0]

    confidence = round(top_score / max(total, top_score + 1), 2)
    if len(sorted_sectors) > 1 and top_score >= sorted_sectors[1][1] * 2:
        confidence = min(round(confidence * 1.2, 2), 1.0)

    # Detect sub_niche
    sub_niche = None
    if top_sector in SUB_NICHE_KEYWORDS:
        for sn, sn_keywords in SUB_NICHE_KEYWORDS[top_sector].items():
            if any(kw.lower() in q for kw in sn_keywords):
                sub_niche = sn
                break

    alternatives = [
        {"sector": s, "score": sc}
        for s, sc in sorted_sectors[1:4]
    ]

    return {
        "sector": top_sector,
        "confidence": confidence,
        "sub_niche": sub_niche,
        "alternatives": alternatives,
    }
```

- [ ] **Step 4: Run tests**

```bash
python -m pytest tests/learning/test_sector_classifier.py -v
```
Expected: all 4 tests pass.

- [ ] **Step 5: Commit**

```bash
git add learning/ tests/learning/
git commit -m "feat(p3): implement sector_classifier with sub_niche detection"
```

---

## Task 2: `knowledge_base.py`

**Files:**
- Create: `learning/knowledge_base.py`
- Create: `tests/learning/test_knowledge_base.py`

- [ ] **Step 1: Write failing tests**

```python
# tests/learning/test_knowledge_base.py
import json
import pytest
from pathlib import Path
from learning.knowledge_base import KnowledgeBase

@pytest.fixture
def kb(tmp_path):
    return KnowledgeBase(base_dir=tmp_path / "knowledge")

def test_save_and_get(kb):
    data = {
        "sector": "b2b-products",
        "niche": "industrial-pumps",
        "sub_niche": None,
        "confidence_score": 0.85,
        "patterns": {"components": ["rfq-form"]},
        "rules": {"required_elements": ["Technical specs"]},
        "references": [],
    }
    kb.save("b2b-products", "industrial-pumps", data)
    result = kb.get("b2b-products", "industrial-pumps")
    assert result is not None
    assert result["niche"] == "industrial-pumps"
    assert result["confidence_score"] == 0.85

def test_get_missing_returns_none(kb):
    assert kb.get("b2b-products", "nonexistent") is None

def test_storage_limits_enforced(kb):
    # MAX_REFERENCES_PER_NICHE = 10
    data = {"sector": "b2b-products", "niche": "test", "references": [{"url": f"http://example{i}.com"} for i in range(15)]}
    kb.save("b2b-products", "test", data)
    result = kb.get("b2b-products", "test")
    assert len(result["references"]) <= 10

def test_list_niches(kb):
    kb.save("b2b-products", "pumps", {"sector": "b2b-products", "niche": "pumps"})
    kb.save("services", "tarot", {"sector": "services", "niche": "tarot"})
    niches = kb.list_niches()
    assert any(n["niche"] == "pumps" for n in niches)
    assert any(n["niche"] == "tarot" for n in niches)

def test_delete_niche(kb):
    kb.save("b2b-products", "pumps", {"sector": "b2b-products", "niche": "pumps"})
    kb.delete("b2b-products", "pumps")
    assert kb.get("b2b-products", "pumps") is None

def test_is_stale_returns_true_for_old_entry(kb):
    import datetime
    old_date = (datetime.datetime.now() - datetime.timedelta(days=100)).isoformat() + "Z"
    kb.save("b2b-products", "pumps", {
        "sector": "b2b-products", "niche": "pumps",
        "last_updated": old_date, "stale_after_days": 90,
    })
    assert kb.is_stale("b2b-products", "pumps") is True
```

- [ ] **Step 2: Run to confirm failure**

```bash
python -m pytest tests/learning/test_knowledge_base.py -v 2>&1 | head -10
```
Expected: `ImportError` — `knowledge_base` not found.

- [ ] **Step 3: Write `learning/knowledge_base.py`**

```python
# learning/knowledge_base.py
"""Local JSON knowledge store at ~/.global-design-skill/knowledge/."""
import datetime
import json
import os
import stat
from pathlib import Path
from typing import Any

MAX_REFERENCES_PER_NICHE = 10
CACHE_TTL_DAYS = 30
STALE_THRESHOLD_DAYS = 90
MAX_STORAGE_MB = 500


class KnowledgeBase:
    def __init__(self, base_dir: Path | None = None):
        if base_dir is None:
            base_dir = Path.home() / ".global-design-skill" / "knowledge"
        self.base_dir = Path(base_dir)
        self._ensure_dir()

    def _ensure_dir(self):
        self.base_dir.mkdir(parents=True, exist_ok=True)
        # Restrict permissions on Unix
        if os.name == "posix":
            try:
                os.chmod(self.base_dir.parent, stat.S_IRWXU)
            except PermissionError:
                pass

    def _path(self, sector: str, niche: str) -> Path:
        sector_dir = self.base_dir / sector
        sector_dir.mkdir(exist_ok=True)
        return sector_dir / f"{niche}.json"

    def save(self, sector: str, niche: str, data: dict[str, Any]) -> None:
        """Save knowledge entry, enforcing storage limits."""
        # Enforce reference cap
        if "references" in data:
            data["references"] = data["references"][:MAX_REFERENCES_PER_NICHE]

        # Add metadata if missing
        now = datetime.datetime.utcnow().isoformat() + "Z"
        data.setdefault("learned_at", now)
        data.setdefault("last_updated", now)
        data.setdefault("stale_after_days", STALE_THRESHOLD_DAYS)
        data.setdefault("usage_count", 0)
        data.setdefault("success_rate", 0.0)
        data.setdefault("suspicion_flag", False)
        data.setdefault("sensitive", False)
        data.setdefault("sub_niche", None)
        data.setdefault("composite_patterns", [])
        data["last_updated"] = now

        self._check_storage_limit()
        self._path(sector, niche).write_text(json.dumps(data, indent=2), encoding="utf-8")

    def get(self, sector: str, niche: str) -> dict | None:
        path = self._path(sector, niche)
        if not path.exists():
            return None
        return json.loads(path.read_text(encoding="utf-8"))

    def delete(self, sector: str, niche: str) -> None:
        path = self._path(sector, niche)
        if path.exists():
            path.unlink()

    def list_niches(self) -> list[dict]:
        niches = []
        for sector_dir in self.base_dir.iterdir():
            if not sector_dir.is_dir():
                continue
            for niche_file in sector_dir.glob("*.json"):
                try:
                    data = json.loads(niche_file.read_text(encoding="utf-8"))
                    niches.append({
                        "sector": sector_dir.name,
                        "niche": niche_file.stem,
                        "confidence_score": data.get("confidence_score", 0),
                        "last_updated": data.get("last_updated", ""),
                        "stale": self.is_stale(sector_dir.name, niche_file.stem),
                        "suspicion_flag": data.get("suspicion_flag", False),
                    })
                except (json.JSONDecodeError, KeyError):
                    continue
        return sorted(niches, key=lambda x: x["last_updated"], reverse=True)

    def is_stale(self, sector: str, niche: str) -> bool:
        entry = self.get(sector, niche)
        if not entry:
            return False
        last_updated_str = entry.get("last_updated", "")
        stale_after = entry.get("stale_after_days", STALE_THRESHOLD_DAYS)
        if not last_updated_str:
            return True
        try:
            last_updated = datetime.datetime.fromisoformat(last_updated_str.rstrip("Z"))
            return (datetime.datetime.utcnow() - last_updated).days > stale_after
        except ValueError:
            return True

    def _check_storage_limit(self):
        total_bytes = sum(
            f.stat().st_size
            for f in self.base_dir.rglob("*.json")
            if f.is_file()
        )
        total_mb = total_bytes / (1024 * 1024)
        if total_mb > MAX_STORAGE_MB:
            self._evict_lru()

    def _evict_lru(self):
        """Remove the least recently used niche entry."""
        niches = self.list_niches()
        if not niches:
            return
        # Sort by (usage_count + recency) — lowest first
        def lru_score(n):
            entry = self.get(n["sector"], n["niche"])
            usage = entry.get("usage_count", 0) if entry else 0
            return usage

        niches.sort(key=lru_score)
        victim = niches[0]
        self.delete(victim["sector"], victim["niche"])
```

- [ ] **Step 4: Run tests**

```bash
python -m pytest tests/learning/test_knowledge_base.py -v
```
Expected: all 6 tests pass.

- [ ] **Step 5: Commit**

```bash
git add learning/knowledge_base.py tests/learning/test_knowledge_base.py
git commit -m "feat(p3): implement knowledge_base with storage limits and staleness check"
```

---

## Task 3: `ethical_scraper.py` and `pattern_extractor.py`

**Files:**
- Create: `learning/ethical_scraper.py`
- Create: `learning/pattern_extractor.py`
- Create: `tests/learning/fixtures/sample_html.html`

- [ ] **Step 1: Update `mcp-server/pyproject.toml` dependencies**

Add to `dependencies`:
```toml
    "requests>=2.31",
    "beautifulsoup4>=4.12",
```

Install:
```bash
cd mcp-server && pip install -e ".[test]"
```

- [ ] **Step 2: Write test fixture HTML**

```html
<!-- tests/learning/fixtures/sample_html.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Industrial Pump Manufacturer</title>
  <meta name="description" content="Leading manufacturer of industrial pumps">
</head>
<body>
  <header>
    <nav>
      <a href="/">Home</a>
      <a href="/products">Products</a>
      <a href="/contact">Contact</a>
    </nav>
  </header>

  <main>
    <section class="hero">
      <h1>Industrial Pumps for Demanding Applications</h1>
      <a href="/rfq" class="btn">Request Quote</a>
      <a href="/catalog" class="btn">Download Catalog</a>
    </section>

    <section class="certifications">
      <img alt="ISO 9001 Certified" src="/iso.png">
      <img alt="CE Marking" src="/ce.png">
    </section>

    <section class="products">
      <div class="product-card">
        <h2>Centrifugal Pump Series X</h2>
        <a href="/spec-sheet.pdf">Download Spec Sheet</a>
      </div>
    </section>

    <section class="testimonials">
      <blockquote>
        <p>Reduced downtime by 40%</p>
        <cite>— John Smith, Plant Manager, Acme Corp</cite>
      </blockquote>
    </section>

    <form class="rfq-form">
      <input type="text" name="company" placeholder="Company name">
      <input type="file" name="drawing" accept=".pdf,.dwg">
      <button type="submit">Request Quote</button>
    </form>
  </main>
</body>
</html>
```

- [ ] **Step 3: Write `learning/ethical_scraper.py`**

```python
# learning/ethical_scraper.py
"""Ethical HTTP client with robots.txt compliance and rate limiting."""
import time
import urllib.robotparser
from urllib.parse import urlparse

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

USER_AGENT = "GlobalDesignSkill-Bot/1.0 (Learning/Reference Collection)"
RATE_LIMIT_SECONDS = 6  # 10 requests/minute = 1 per 6 seconds
_last_request_time: float = 0.0


class EthicalScraper:
    def __init__(self):
        self._robots_cache: dict[str, urllib.robotparser.RobotFileParser] = {}

    def can_fetch(self, url: str) -> bool:
        """Check robots.txt before fetching."""
        parsed = urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}"
        robots_url = f"{base}/robots.txt"

        if base not in self._robots_cache:
            rp = urllib.robotparser.RobotFileParser()
            rp.set_url(robots_url)
            try:
                rp.read()
            except Exception:
                rp = None
            self._robots_cache[base] = rp

        rp = self._robots_cache[base]
        if rp is None:
            return True  # Cannot read robots.txt — allow
        return rp.can_fetch(USER_AGENT, url)

    def fetch(self, url: str) -> dict:
        """Fetch a URL respecting robots.txt and rate limits.

        Returns: {"html": str, "url": str, "status": int} or {"error": str}
        """
        if not REQUESTS_AVAILABLE:
            return {"error": "requests library not installed. Run: pip install requests"}

        if not self.can_fetch(url):
            return {"error": f"Disallowed by robots.txt: {url}"}

        global _last_request_time
        elapsed = time.time() - _last_request_time
        if elapsed < RATE_LIMIT_SECONDS:
            time.sleep(RATE_LIMIT_SECONDS - elapsed)

        try:
            response = requests.get(
                url,
                headers={"User-Agent": USER_AGENT},
                timeout=10,
            )
            _last_request_time = time.time()
            return {
                "html": response.text,
                "url": url,
                "status": response.status_code,
            }
        except requests.RequestException as e:
            return {"error": str(e)}
```

- [ ] **Step 4: Write `learning/pattern_extractor.py`**

```python
# learning/pattern_extractor.py
"""Extract design patterns from HTML content."""
import re

try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False


def extract_patterns(html: str) -> dict:
    """Extract design patterns from HTML.

    Returns dict with layout, components, trust_signals, conversion_elements.
    """
    if not BS4_AVAILABLE:
        return {"error": "beautifulsoup4 not installed. Run: pip install beautifulsoup4"}

    soup = BeautifulSoup(html, "html.parser")
    text = html.lower()

    return {
        "layout": _extract_layout(soup),
        "components": _extract_components(soup, text),
        "trust_signals": _extract_trust_signals(soup, text),
        "conversion_elements": _extract_conversion_elements(soup, text),
    }


def _extract_layout(soup) -> dict:
    return {
        "has_header": bool(soup.find("header")),
        "has_footer": bool(soup.find("footer")),
        "has_hero": bool(soup.find(class_=re.compile(r"hero|banner|jumbotron", re.I))),
        "has_sidebar": bool(soup.find(["aside", "nav"]) and soup.find(class_=re.compile(r"sidebar", re.I))),
        "nav_link_count": len(soup.find_all("nav")),
    }


def _extract_components(soup, text: str) -> list[str]:
    components = []
    if soup.find(class_=re.compile(r"carousel|slider|swiper", re.I)) or soup.find("swiper-container"):
        components.append("carousel")
    if soup.find(class_=re.compile(r"testimonial|review|quote", re.I)) or soup.find("blockquote"):
        components.append("testimonials")
    if soup.find(class_=re.compile(r"pricing|plan|tier", re.I)):
        components.append("pricing-table")
    if soup.find(class_=re.compile(r"faq|accordion", re.I)):
        components.append("faq-accordion")
    if soup.find(["input", "textarea", "select"]):
        form = soup.find("form")
        if form and form.find("input", type="file"):
            components.append("file-upload-form")
        elif form:
            components.append("contact-form")
    if soup.find(class_=re.compile(r"search", re.I)) or soup.find("input", type="search"):
        components.append("search")
    if "rfq" in text or "request quote" in text or "request a quote" in text:
        components.append("rfq-form")
    if "configurator" in text or "configure" in text:
        components.append("product-configurator")
    return components


def _extract_trust_signals(soup, text: str) -> list[str]:
    signals = []
    # Certifications
    for img in soup.find_all("img"):
        alt = (img.get("alt") or "").lower()
        if any(cert in alt for cert in ["iso", "ce ", "certified", "certification"]):
            signals.append("certifications")
            break
    # Client logos
    if soup.find(class_=re.compile(r"logo|client|partner", re.I)):
        signals.append("client-logos")
    # Reviews / testimonials
    if soup.find(class_=re.compile(r"testimonial|review|rating", re.I)) or soup.find("blockquote"):
        signals.append("reviews-testimonials")
    # Guarantee
    if "guarantee" in text or "money back" in text or "гарантия" in text:
        signals.append("guarantee")
    # Security
    if any(s in text for s in ["ssl", "secure", "encrypted", "soc 2"]):
        signals.append("security-badge")
    return signals


def _extract_conversion_elements(soup, text: str) -> list[str]:
    elements = []
    buttons = soup.find_all(["button", "a"], class_=re.compile(r"btn|button|cta", re.I))
    btn_texts = [b.get_text(strip=True).lower() for b in buttons]

    if any("quote" in t or "rfq" in t for t in btn_texts):
        elements.append("request-quote-cta")
    if any("demo" in t for t in btn_texts):
        elements.append("demo-request")
    if any("trial" in t or "free" in t for t in btn_texts):
        elements.append("free-trial")
    if any("download" in t or "catalog" in t or "spec" in t for t in btn_texts):
        elements.append("document-download")
    if any("book" in t or "schedule" in t or "appointment" in t for t in btn_texts):
        elements.append("booking")
    if soup.find("form"):
        elements.append("lead-form")
    return elements
```

- [ ] **Step 5: Write test for pattern_extractor**

```python
# Add to tests/learning/test_knowledge_base.py or new file:
# tests/learning/test_pattern_extractor.py
from pathlib import Path
from learning.pattern_extractor import extract_patterns

FIXTURE = (Path(__file__).parent / "fixtures" / "sample_html.html").read_text()

def test_extracts_trust_signals():
    result = extract_patterns(FIXTURE)
    assert "certifications" in result["trust_signals"]

def test_extracts_rfq_form():
    result = extract_patterns(FIXTURE)
    assert "rfq-form" in result["components"]

def test_extracts_request_quote_cta():
    result = extract_patterns(FIXTURE)
    assert "request-quote-cta" in result["conversion_elements"]

def test_returns_required_keys():
    result = extract_patterns(FIXTURE)
    for key in ["layout", "components", "trust_signals", "conversion_elements"]:
        assert key in result
```

- [ ] **Step 6: Run tests**

```bash
python -m pytest tests/learning/ -v
```
Expected: all tests pass.

- [ ] **Step 7: Commit**

```bash
git add learning/ethical_scraper.py learning/pattern_extractor.py tests/learning/
git commit -m "feat(p3): implement ethical_scraper and pattern_extractor"
```

---

## Task 4: `gap_detector.py`

**Files:**
- Create: `learning/gap_detector.py`
- Create: `tests/learning/test_gap_detector.py`

- [ ] **Step 1: Write test**

```python
# tests/learning/test_gap_detector.py
from learning.gap_detector import detect_gaps

def test_detects_missing_component():
    extracted = {
        "components": ["rfq-form"],
        "trust_signals": [],
        "conversion_elements": ["request-quote-cta"],
    }
    # b2b-products requires certifications — we have none
    gaps = detect_gaps("b2b-products", extracted)
    assert "missing_trust_signals" in gaps
    # certifications not in extracted trust_signals
    assert any("certification" in g.lower() for g in gaps["missing_trust_signals"])

def test_no_gaps_when_all_present():
    extracted = {
        "components": ["rfq-form", "product-configurator"],
        "trust_signals": ["certifications", "client-logos", "reviews-testimonials"],
        "conversion_elements": ["request-quote-cta", "document-download", "demo-request"],
    }
    gaps = detect_gaps("b2b-products", extracted)
    assert len(gaps.get("missing_trust_signals", [])) == 0
```

- [ ] **Step 2: Write `learning/gap_detector.py`**

```python
# learning/gap_detector.py
"""Compare extracted patterns against static industry rules to detect gaps."""
import re
from pathlib import Path

INDUSTRIES_DIR = Path(__file__).parent.parent / "industries"

# Maps extracted signal categories to keywords to look for in Required Elements
SIGNAL_KEYWORDS = {
    "certifications": ["certification", "iso", "ce ", "compliance", "licence"],
    "client-logos":   ["client", "logo", "customer", "partner"],
    "reviews-testimonials": ["testimonial", "review", "case stud", "social proof"],
    "security-badge": ["security", "ssl", "encrypt", "secure"],
    "guarantee":      ["guarantee", "money-back", "refund"],
}

COMPONENT_KEYWORDS = {
    "rfq-form":             ["rfq", "request quote", "quote form"],
    "product-configurator": ["configurator", "configure", "3d preview"],
    "booking":              ["booking", "calendar", "schedule", "appointment"],
    "pricing-table":        ["pricing", "price", "plan", "tier"],
    "file-upload-form":     ["cad", "drawing", "spec", "upload"],
    "testimonials":         ["testimonial", "review", "quote"],
    "search":               ["search", "filter", "find"],
}


def detect_gaps(sector: str, extracted: dict) -> dict:
    """Detect what is missing from extracted patterns vs static sector rules.

    Args:
        sector:    Sector ID (e.g. "b2b-products")
        extracted: Output from pattern_extractor.extract_patterns()

    Returns dict: {missing_trust_signals, missing_components, missing_conversion,
                   suspicion_flag, notes}
    """
    sector_file = INDUSTRIES_DIR / f"{sector}.md"
    if not sector_file.exists():
        return {"error": f"Sector file not found: {sector}.md"}

    text = sector_file.read_text(encoding="utf-8").lower()

    # Extract what the static rules require
    required_section = _get_section(text, "required elements")
    banned_section   = _get_section(text, "banned patterns")
    trust_section    = _get_section(text, "trust signals")

    missing_trust    = _find_missing(extracted.get("trust_signals", []),
                                      SIGNAL_KEYWORDS, trust_section)
    missing_comps    = _find_missing(extracted.get("components", []),
                                      COMPONENT_KEYWORDS, required_section)

    # Suspicion flag: if > 40% of required components are absent
    total_required = len([kw for kw in COMPONENT_KEYWORDS if any(k in required_section for k in COMPONENT_KEYWORDS[kw])])
    missing_count  = len(missing_comps)
    suspicion_flag = total_required > 0 and (missing_count / max(total_required, 1)) > 0.4

    return {
        "missing_trust_signals": missing_trust,
        "missing_components":    missing_comps,
        "suspicion_flag":        suspicion_flag,
        "notes": f"Checked against {sector}.md static rules",
    }


def _get_section(text: str, heading: str) -> str:
    match = re.search(rf"## {re.escape(heading)}\n(.*?)(?=\n##|\Z)", text, re.DOTALL)
    return match.group(1) if match else ""


def _find_missing(extracted_list: list[str], keyword_map: dict, section_text: str) -> list[str]:
    missing = []
    for name, keywords in keyword_map.items():
        required_in_static = any(kw in section_text for kw in keywords)
        present_in_extracted = name in extracted_list
        if required_in_static and not present_in_extracted:
            missing.append(name)
    return missing
```

- [ ] **Step 3: Run tests**

```bash
python -m pytest tests/learning/test_gap_detector.py -v
```
Expected: both tests pass.

- [ ] **Step 4: Commit**

```bash
git add learning/gap_detector.py tests/learning/test_gap_detector.py
git commit -m "feat(p3): implement gap_detector with suspicion_flag"
```

---

## Task 5: New MCP Tools — `learn_from_reference` and `get_or_learn_sector`

**Files:**
- Create: `mcp-server/tools/learning_tools.py`
- Modify: `mcp-server/server.py` — register new tools

- [ ] **Step 1: Write `mcp-server/tools/learning_tools.py`**

```python
# mcp-server/tools/learning_tools.py
"""MCP tools for learning from references and retrieving/learning sector context."""
import json
import sys
from pathlib import Path

# Allow importing from learning/ directory
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from learning.sector_classifier import classify_sector
from learning.knowledge_base import KnowledgeBase
from learning.ethical_scraper import EthicalScraper
from learning.pattern_extractor import extract_patterns
from learning.gap_detector import detect_gaps
from tools.sector_context import get_sector_context

_kb = KnowledgeBase()
_scraper = EthicalScraper()


def learn_from_reference(url: str, sector: str = None, niche: str = None) -> str:
    """Scrape a reference site, extract patterns, save to knowledge base.

    Returns JSON: {sector, niche, patterns, gaps, suspicion_flag, references_count}
    """
    fetch_result = _scraper.fetch(url)
    if "error" in fetch_result:
        return json.dumps({"error": fetch_result["error"]})

    html = fetch_result["html"]

    # Auto-classify if sector not provided
    if not sector:
        classification = classify_sector(html[:2000])  # use first 2000 chars
        sector = classification["sector"]
        if not niche:
            niche = classification.get("sub_niche") or "general"

    niche = niche or "general"

    # Extract patterns
    patterns = extract_patterns(html)
    if "error" in patterns:
        return json.dumps({"error": patterns["error"]})

    # Detect gaps
    gaps = detect_gaps(sector, patterns)

    # Load existing entry or start fresh
    existing = _kb.get(sector, niche) or {}
    existing_refs = existing.get("references", [])
    existing_refs.append({"url": url, "quality_score": 0.7, "scraped_at": _now()})

    knowledge = {
        "sector": sector,
        "niche": niche,
        "sub_niche": None,
        "source": "learned",
        "confidence_score": round(min(0.5 + len(existing_refs) * 0.05, 0.95), 2),
        "patterns": patterns,
        "rules": {
            "required_elements": [],
            "banned_patterns": [],
            "trust_signals": patterns.get("trust_signals", []),
            "conversion_elements": patterns.get("conversion_elements", []),
        },
        "references": existing_refs,
        "suspicion_flag": gaps.get("suspicion_flag", False),
    }

    _kb.save(sector, niche, knowledge)

    return json.dumps({
        "sector": sector,
        "niche": niche,
        "patterns_found": {k: len(v) if isinstance(v, list) else v for k, v in patterns.items()},
        "gaps": gaps,
        "suspicion_flag": gaps.get("suspicion_flag", False),
        "references_count": len(existing_refs),
        "saved": True,
    })


def get_or_learn_sector(sector: str, niche: str) -> str:
    """Get sector context from static files or knowledge base.
    If not found, returns a message indicating learning is needed.

    Priority: industries/*.md → knowledge_base → "not found, run learn_from_reference"

    Returns JSON: {source, sector, niche, context}
    """
    # 1. Try static industries file
    static = json.loads(get_sector_context(sector))
    if "error" not in static:
        return json.dumps({
            "source": "static",
            "sector": sector,
            "niche": niche,
            "context": static,
        })

    # 2. Try knowledge base
    learned = _kb.get(sector, niche)
    if learned:
        stale = _kb.is_stale(sector, niche)
        return json.dumps({
            "source": "learned" + ("_stale" if stale else ""),
            "sector": sector,
            "niche": niche,
            "stale": stale,
            "context": learned,
        })

    # 3. Not found
    return json.dumps({
        "source": "not_found",
        "sector": sector,
        "niche": niche,
        "action": f"Call learn_from_reference(url=<reference_url>, sector='{sector}', niche='{niche}') to learn this niche.",
    })


def list_learned_niches() -> str:
    """List all niches in the knowledge base with metadata."""
    return json.dumps(_kb.list_niches())


def forget_niche(sector: str, niche: str) -> str:
    """Delete a learned niche from the knowledge base."""
    existing = _kb.get(sector, niche)
    if not existing:
        return json.dumps({"error": f"Niche '{sector}/{niche}' not found in knowledge base"})
    _kb.delete(sector, niche)
    return json.dumps({"deleted": True, "sector": sector, "niche": niche})


def reset_weights(sector: str = None) -> str:
    """Reset pattern weights to 1.0. Weights live in sedi/ (Phase 4).
    This stub returns a message until Phase 4 is implemented."""
    return json.dumps({
        "status": "weights_reset_pending",
        "note": "Weight reset is implemented in Phase 4 (sedi/feedback_engine.py). "
                "Complete Phase 4 to use this tool.",
        "sector": sector,
    })


def _now() -> str:
    import datetime
    return datetime.datetime.utcnow().isoformat() + "Z"
```

- [ ] **Step 2: Register new tools in `mcp-server/server.py`**

Add after the existing tool registrations in `server.py`:

```python
    from tools.learning_tools import (
        learn_from_reference as _learn_from_reference,
        get_or_learn_sector as _get_or_learn_sector,
        list_learned_niches as _list_learned_niches,
        forget_niche as _forget_niche,
        reset_weights as _reset_weights,
    )

    @mcp.tool()
    def learn_from_reference_tool(url: str, sector: str = None, niche: str = None) -> str:
        """Scrape a reference URL, extract design patterns, save to knowledge base."""
        return _learn_from_reference(url, sector, niche)

    @mcp.tool()
    def get_or_learn_sector_tool(sector: str, niche: str) -> str:
        """Get sector context from static files or knowledge base.
        Returns action hint if niche is unknown."""
        return _get_or_learn_sector(sector, niche)

    @mcp.tool()
    def list_learned_niches_tool() -> str:
        """List all niches in the local knowledge base."""
        return _list_learned_niches()

    @mcp.tool()
    def forget_niche_tool(sector: str, niche: str) -> str:
        """Delete a learned niche from the local knowledge base."""
        return _forget_niche(sector, niche)

    @mcp.tool()
    def reset_weights_tool(sector: str = None) -> str:
        """Reset pattern weights to neutral (Phase 4 feature)."""
        return _reset_weights(sector)
```

- [ ] **Step 3: Run full test suite**

```bash
python -m pytest tests/ -v --tb=short
```
Expected: all tests pass.

- [ ] **Step 4: Commit**

```bash
git add learning/ mcp-server/tools/learning_tools.py mcp-server/server.py
git commit -m "feat(p3): add learn_from_reference, get_or_learn_sector, forget_niche MCP tools"
```

---

## Self-Review Checklist

- [x] `sector_classifier.py` returns `sub_niche` field — matches spec schema
- [x] `knowledge_base.py` enforces `MAX_REFERENCES_PER_NICHE=10`, `MAX_STORAGE_MB=500`, LRU eviction
- [x] `is_stale()` uses `stale_after_days` from stored entry, defaults to 90
- [x] `ethical_scraper.py` checks `robots.txt` before every fetch
- [x] `gap_detector.py` sets `suspicion_flag` when > 40% of required components absent
- [x] `learn_from_reference` updates `confidence_score` based on reference count
- [x] `get_or_learn_sector` follows priority: static → learned → not_found message
- [x] `forget_niche` and `reset_weights` stubs are present (reset_weights defers to Phase 4)
- [x] All new MCP tools registered in `server.py`
- [x] Tests cover knowledge_base CRUD, staleness, storage limits, pattern extraction
