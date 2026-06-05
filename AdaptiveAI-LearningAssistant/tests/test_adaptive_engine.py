import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from app.modules.adaptive_engine import evaluate_answer, update_student_profile, select_next_question


def test_evaluate_answer_true_on_matching_text():
    result = evaluate_answer("Stack", "stack", ["Stack", "Queue"], "What is a stack?", "Recognition")
    assert result["correct"]
    assert result["label"] == "Correct"
    assert result["confidence_score"] == 100


def test_evaluate_answer_false_on_different_text():
    result = evaluate_answer("Queue", "Stack", ["Stack", "Queue"], "What is a stack?", "Recognition")
    assert not result["correct"]
    assert result["label"] == "Incorrect"


def test_update_student_profile_changes_scores_and_history():
    profile = {
        "name": "Test",
        "topics_attempted": [],
        "scores": {"Recognition": 0.0, "Understanding": 0.0, "Application": 0.0, "Debugging": 0.0},
        "attempt_counters": {"Recognition": 0, "Understanding": 0, "Application": 0, "Debugging": 0},
        "average_confidence": 0.0,
        "average_confidence_score": 0.0,
        "confidence_score_total": 0,
        "confidence_score_count": 0,
        "confidence_counts": {"Low": 0, "Medium": 0, "High": 0},
        "weak_topics": [],
        "recommended_topics": [],
        "learning_history": [],
        "overall_mastery_score": 0.0,
    }
    update_student_profile(profile, "Arrays", "Recognition", True, "Medium", 92)
    assert profile["scores"]["Recognition"] == 100.0
    assert profile["attempt_counters"]["Recognition"] == 1
    assert profile["learning_history"]
    assert profile["average_confidence_score"] == 92.0
    assert profile["average_confidence"] == 66.0
    assert profile["overall_mastery_score"] == 25.0
    assert profile["learning_path"]


def test_update_student_profile_records_misconception():
    profile = {
        "name": "Test",
        "topics_attempted": [],
        "scores": {"Recognition": 0.0, "Understanding": 0.0, "Application": 0.0, "Debugging": 0.0},
        "attempt_counters": {"Recognition": 0, "Understanding": 0, "Application": 0, "Debugging": 0},
        "average_confidence": 0.0,
        "average_confidence_score": 0.0,
        "confidence_score_total": 0,
        "confidence_score_count": 0,
        "confidence_counts": {"Low": 0, "Medium": 0, "High": 0},
        "weak_topics": [],
        "recommended_topics": [],
        "learning_history": [],
        "overall_mastery_score": 0.0,
        "misconceptions": [],
        "learning_path": [],
        "recent_questions": [],
        "knowledge_dependencies": [],
    }
    update_student_profile(profile, "Stack", "Recognition", False, "High", 10, "Confuses FIFO and LIFO")
    assert "Confuses FIFO and LIFO" in profile["misconceptions"]
    assert profile["learning_history"][-1]["misconception"] == "Confuses FIFO and LIFO"


def test_select_next_question_returns_question_dict():
    profile = {
        "name": "Test",
        "topics_attempted": ["Arrays"],
        "scores": {"Recognition": 20.0, "Understanding": 0.0, "Application": 0.0, "Debugging": 0.0},
        "attempt_counters": {"Recognition": 1, "Understanding": 0, "Application": 0, "Debugging": 0},
        "average_confidence": 2.0,
        "average_confidence_score": 40.0,
        "confidence_score_total": 40,
        "confidence_score_count": 1,
        "confidence_counts": {"Low": 0, "Medium": 1, "High": 0},
        "weak_topics": ["Recognition"],
        "recommended_topics": ["Stack"],
        "learning_history": [],
        "overall_mastery_score": 5.0,
    }
    next_question = select_next_question(profile, "Arrays", "Recognition", True, "High")
    assert isinstance(next_question, dict)
    assert next_question["topic"] == "Arrays"
