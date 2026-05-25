import json
import sys
import os
import pytest
from pathlib import Path

# Add mcp-server directory to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

FIXTURES = json.loads(
    (Path(__file__).parent / "fixtures" / "sample_queries.json").read_text()
)

# Import after path setup — will fail until sector_context.py is created
from tools.sector_context import classify_niche


@pytest.mark.parametrize("case", FIXTURES, ids=[c["query"][:40] for c in FIXTURES])
def test_classify_niche_accuracy(case):
    result = classify_niche(case["query"])
    assert isinstance(result, str), "classify_niche must return a JSON string"

    data = json.loads(result)
    assert "sector" in data, "Result must have 'sector' key"
    assert "confidence" in data, "Result must have 'confidence' key"
    assert data["sector"] == case["expected_sector"], (
        f"Expected {case['expected_sector']}, got {data['sector']} "
        f"for query: {case['query']}"
    )
    assert data["confidence"] >= case["min_confidence"], (
        f"Confidence {data['confidence']} below minimum {case['min_confidence']} "
        f"for query: {case['query']}"
    )


def test_classify_niche_unknown_returns_valid_json():
    result = classify_niche("completely unrelated gibberish xyzzy")
    data = json.loads(result)
    assert "sector" in data
    assert "confidence" in data
    assert data["confidence"] < 0.5


def test_overall_accuracy():
    correct = 0
    for case in FIXTURES:
        data = json.loads(classify_niche(case["query"]))
        if data["sector"] == case["expected_sector"]:
            correct += 1
    accuracy = correct / len(FIXTURES)
    assert accuracy >= 0.85, f"Overall accuracy {accuracy:.1%} below 85% threshold"
