import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from app.modules.analytics import build_analytics_summary


def test_build_analytics_summary_contains_expected_fields():
    profile = {
        "name": "StudentA",
        "scores": {"Recognition": 50.0, "Understanding": 75.0, "Application": 80.0, "Debugging": 60.0},
        "attempt_counters": {"Recognition": 2, "Understanding": 3, "Application": 1, "Debugging": 0},
        "average_confidence": 2.2,
        "weak_topics": ["Debugging"],
        "recommended_topics": ["Queue"],
        "learning_history": [],
    }
    analytics = build_analytics_summary(profile)
    assert analytics["name"] == "StudentA"
    assert analytics["mastery"] == 66.25
    assert analytics["weak_topics"] == ["Debugging"]
