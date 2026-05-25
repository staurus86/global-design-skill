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
    for img in soup.find_all("img"):
        alt = (img.get("alt") or "").lower()
        if any(cert in alt for cert in ["iso", "ce ", "certified", "certification"]):
            signals.append("certifications")
            break
    if soup.find(class_=re.compile(r"logo|client|partner", re.I)):
        signals.append("client-logos")
    if soup.find(class_=re.compile(r"testimonial|review|rating", re.I)) or soup.find("blockquote"):
        signals.append("reviews-testimonials")
    if "guarantee" in text or "money back" in text or "гарантия" in text:
        signals.append("guarantee")
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
