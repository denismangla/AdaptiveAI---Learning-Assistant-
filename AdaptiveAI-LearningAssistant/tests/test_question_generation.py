import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from app.modules.question_generator import generate_question_for_topic


def test_generate_question_for_topic_returns_structure():
    result = generate_question_for_topic("Arrays", "Recognition", "easy")
    assert result["topic"] == "Arrays"
    assert result["level"] == "Recognition"
    assert "question" in result
    assert "answer" in result


def test_generate_question_for_topic_fallback_when_unknown_level():
    result = generate_question_for_topic("Arrays", "InvalidLevel", "easy")
    assert result["topic"] == "Arrays"
    assert result["level"] == "InvalidLevel"
    assert result["options"] == [] or isinstance(result["options"], list)
