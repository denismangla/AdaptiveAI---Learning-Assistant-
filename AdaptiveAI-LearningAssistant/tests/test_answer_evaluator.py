import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from app.modules.answer_evaluator import evaluate_answer


def test_mcq_exact_match():
    result = evaluate_answer("a = [1, 2, 3]", "a = [1, 2, 3]", ["a = [1, 2, 3]", "a = (1, 2, 3)"], "Which of the following is a valid array declaration?", "Recognition")
    assert result["correct"]
    assert result["confidence_score"] == 100
    assert result["label"] == "Correct"


def test_semantic_short_answer_fallback():
    result = evaluate_answer("An array stores ordered values and lets you access them by index.", "A data structure that keeps ordered elements accessible by index.", None, "Explain what an array is.", "Understanding")
    assert "confidence_score" in result
    assert result["label"] in {"Correct", "Incorrect"}
    assert isinstance(result["reason"], str)
