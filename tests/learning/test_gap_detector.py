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
