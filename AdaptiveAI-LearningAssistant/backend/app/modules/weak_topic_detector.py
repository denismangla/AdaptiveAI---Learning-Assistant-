from collections import defaultdict
from typing import Dict, List


def detect_weak_topics(profile: Dict) -> List[str]:
    weak = set()
    history = profile.get("learning_history", [])
    incorrect_counts = defaultdict(int)
    low_confidence_counts = defaultdict(int)

    for entry in history:
        topic = entry.get("topic")
        if not topic:
            continue
        if not entry.get("correct"):
            incorrect_counts[topic] += 1
        if entry.get("confidence_score", 100) < 50:
            low_confidence_counts[topic] += 1

    for topic, count in incorrect_counts.items():
        if count >= 2:
            weak.add(topic)

    for topic, count in low_confidence_counts.items():
        if count >= 2:
            weak.add(topic)

    return sorted(weak)
