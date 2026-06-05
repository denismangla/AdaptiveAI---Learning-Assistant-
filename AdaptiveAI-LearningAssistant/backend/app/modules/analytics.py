from typing import Dict


def build_analytics_summary(profile: Dict) -> Dict:
    scores = profile.get("scores", {})
    counters = profile.get("attempt_counters", {})
    total_attempts = sum(counters.values())
    average_confidence = profile.get("average_confidence", 0.0)
    weak_topics = profile.get("weak_topics", [])
    recommended_topics = profile.get("recommended_topics", [])
    mastery = calculate_overall_mastery(scores)
    return {
        "name": profile.get("name"),
        "total_attempts": total_attempts,
        "average_confidence": average_confidence,
        "mastery": mastery,
        "scores": scores,
        "attempt_counters": counters,
        "weak_topics": weak_topics,
        "recommended_topics": recommended_topics,
        "learning_history": profile.get("learning_history", []),
    }


def calculate_overall_mastery(scores: Dict[str, float]) -> float:
    if not scores:
        return 0.0
    total = sum(scores.values())
    return round(total / len(scores), 2)
