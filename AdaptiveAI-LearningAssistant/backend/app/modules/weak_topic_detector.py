from typing import Dict, List

WEAK_THRESHOLD = 45


def detect_weak_topics(profile: Dict) -> List[str]:
    weak = []
    scores = profile.get("scores", {})
    for topic, value in scores.items():
        if value < WEAK_THRESHOLD:
            weak.append(topic)
    return weak
