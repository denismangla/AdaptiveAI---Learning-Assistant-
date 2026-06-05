from typing import Dict


def update_confidence_counts(profile: Dict, confidence: str):
    counts = profile.setdefault("confidence_counts", {"Low": 0, "Medium": 0, "High": 0})
    if confidence in counts:
        counts[confidence] += 1
    total = sum(counts.values())
    profile["average_confidence"] = round(
        (counts.get("Low", 0) * 1 + counts.get("Medium", 0) * 2 + counts.get("High", 0) * 3) / max(total, 1),
        2,
    )
