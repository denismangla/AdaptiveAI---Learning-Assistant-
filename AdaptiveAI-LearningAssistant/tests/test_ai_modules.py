import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from app.modules.fallback_library import (
    get_fallback_question,
    get_fallback_hint,
    get_fallback_explanation,
    get_fallback_example,
    get_fallback_wrong_answer_explanation,
)


def test_fallback_question_returns_default_shape():
    result = get_fallback_question("Queue", "Recognition")
    assert "question" in result
    assert "answer" in result
    assert result["topic"] == "Queue"


def test_fallback_hint_returns_text():
    hint = get_fallback_hint("Low")
    assert isinstance(hint, str)
    assert hint


def test_fallback_explanation_returns_text():
    explanation = get_fallback_explanation("Understanding")
    assert isinstance(explanation, str)
    assert explanation


def test_fallback_example_returns_text():
    example = get_fallback_example("Stack")
    assert isinstance(example, str)
    assert example


def test_fallback_wrong_answer_explanation_returns_text():
    explanation = get_fallback_wrong_answer_explanation()
    assert isinstance(explanation, str)
    assert explanation
