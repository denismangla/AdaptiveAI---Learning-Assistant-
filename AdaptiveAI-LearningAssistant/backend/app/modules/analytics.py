from typing import Dict


def build_analytics_summary(profile: Dict) -> Dict:
    scores = profile.get("scores", {})
    counters = profile.get("attempt_counters", {})
    total_attempts = sum(counters.values())
    average_confidence_score = profile.get("average_confidence_score", 0.0)
    weak_topics = profile.get("weak_topics", [])
    recommended_topics = profile.get("recommended_topics", [])
    mastery = profile.get("overall_mastery_score", calculate_overall_mastery(scores))
    return {
        "name": profile.get("name"),
        "total_attempts": total_attempts,
        "average_confidence_score": average_confidence_score,
        "overall_mastery_score": mastery,
        "recognition_score": scores.get("Recognition", 0.0),
        "understanding_score": scores.get("Understanding", 0.0),
        "application_score": scores.get("Application", 0.0),
        "debugging_score": scores.get("Debugging", 0.0),
        "scores": scores,
        "attempt_counters": counters,
        "confidence_counts": profile.get("confidence_counts", {}),
        "weak_topics": weak_topics,
        "recommended_topics": recommended_topics,
        "learning_history": profile.get("learning_history", []),
    }


def calculate_overall_mastery(scores: Dict[str, float]) -> float:
    if not scores:
        return 0.0
    total = sum(scores.values())
    return round(total / len(scores), 2)
