from typing import Dict, List
from app.modules.knowledge_graph import (
    build_learning_path,
    get_dependency_edges,
    get_knowledge_dependency_summary,
)


def build_analytics_summary(profile: Dict) -> Dict:
    scores = profile.get("scores", {})
    counters = profile.get("attempt_counters", {})
    total_attempts = sum(counters.values())
    mastery = profile.get("overall_mastery_score", calculate_overall_mastery(scores))
    learning_path = profile.get("learning_path") or build_learning_path(profile)
    return {
        "name": profile.get("name"),
        "total_attempts": total_attempts,
        "average_confidence": profile.get("average_confidence", 0.0),
        "average_confidence_score": profile.get("average_confidence_score", 0.0),
        "overall_mastery_score": mastery,
        "mastery": mastery,
        "recognition_score": scores.get("Recognition", 0.0),
        "understanding_score": scores.get("Understanding", 0.0),
        "application_score": scores.get("Application", 0.0),
        "debugging_score": scores.get("Debugging", 0.0),
        "scores": scores,
        "attempt_counters": counters,
        "confidence_counts": profile.get("confidence_counts", {}),
        "confidence_trend": [
            {"level": "Low", "count": profile.get("confidence_counts", {}).get("Low", 0)},
            {"level": "Medium", "count": profile.get("confidence_counts", {}).get("Medium", 0)},
            {"level": "High", "count": profile.get("confidence_counts", {}).get("High", 0)},
        ],
        "weak_topics": profile.get("weak_topics", []),
        "recommended_topics": profile.get("recommended_topics", []),
        "misconceptions": profile.get("misconceptions", []),
        "learning_path": learning_path,
        "knowledge_dependencies": profile.get("knowledge_dependencies", get_dependency_edges()),
        "dependency_summary": get_knowledge_dependency_summary(profile),
        "learning_history": profile.get("learning_history", []),
    }


def calculate_overall_mastery(scores: Dict[str, float]) -> float:
    if not scores:
        return 0.0
    total = sum(scores.values())
    return round(total / len(scores), 2)
