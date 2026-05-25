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
