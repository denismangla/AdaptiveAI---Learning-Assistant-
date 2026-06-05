import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from app.modules.adaptive_engine import evaluate_answer, update_student_profile, select_next_question


def test_evaluate_answer_true_on_matching_text():
    assert evaluate_answer("Stack", "stack")


def test_evaluate_answer_false_on_different_text():
    assert not evaluate_answer("Queue", "Stack")


def test_update_student_profile_changes_scores_and_history():
    profile = {
        "name": "Test",
        "topics_attempted": [],
        "scores": {"Recognition": 0.0, "Understanding": 0.0, "Application": 0.0, "Debugging": 0.0},
        "attempt_counters": {"Recognition": 0, "Understanding": 0, "Application": 0, "Debugging": 0},
        "average_confidence": 0.0,
        "confidence_counts": {"Low": 0, "Medium": 0, "High": 0},
        "weak_topics": [],
        "recommended_topics": [],
        "learning_history": [],
    }
    update_student_profile(profile, "Arrays", "Recognition", True, "Medium")
    assert profile["scores"]["Recognition"] > 0
    assert profile["attempt_counters"]["Recognition"] == 1
    assert profile["learning_history"]


def test_select_next_question_returns_question_dict():
    profile = {
        "name": "Test",
        "topics_attempted": ["Arrays"],
        "scores": {"Recognition": 20.0, "Understanding": 0.0, "Application": 0.0, "Debugging": 0.0},
        "attempt_counters": {"Recognition": 1, "Understanding": 0, "Application": 0, "Debugging": 0},
        "average_confidence": 2.0,
        "confidence_counts": {"Low": 0, "Medium": 1, "High": 0},
        "weak_topics": ["Recognition"],
        "recommended_topics": ["Stack"],
        "learning_history": [],
    }
    next_question = select_next_question(profile, "Arrays", "Recognition", True, "High")
    assert isinstance(next_question, dict)
    assert next_question["topic"] == "Arrays"
