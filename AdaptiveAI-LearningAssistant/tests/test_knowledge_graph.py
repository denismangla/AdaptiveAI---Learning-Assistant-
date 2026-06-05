import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from app.modules.knowledge_graph import get_prerequisite_chain, build_dependency_recommendations, build_learning_path


def test_prerequisite_chain_returns_arrays_for_stack():
    assert get_prerequisite_chain("Stack") == ["Arrays"]


def test_dependency_recommendations_for_stack():
    recommendations = build_dependency_recommendations(["Stack"])
    assert "Review Arrays" in recommendations
    assert "Reinforce Stack fundamentals" in recommendations


def test_learning_path_includes_core_steps_for_queue():
    profile = {"weak_topics": ["Queue"]}
    path = build_learning_path(profile)
    assert any("Review FIFO behavior" in step for step in path)
    assert any("Attempt Queue application questions" in step for step in path)
