import json
from pathlib import Path
from typing import Dict, Optional

DEFAULT_SCORES = {
    "Recognition": 0.0,
    "Understanding": 0.0,
    "Application": 0.0,
    "Debugging": 0.0,
}

DEFAULT_COUNTERS = {
    "Recognition": 0,
    "Understanding": 0,
    "Application": 0,
    "Debugging": 0,
}


def create_student_profile(name: str) -> Dict:
    return {
        "name": name,
        "topics_attempted": [],
        "scores": DEFAULT_SCORES.copy(),
        "attempt_counters": DEFAULT_COUNTERS.copy(),
        "average_confidence": 0.0,
        "confidence_counts": {"Low": 0, "Medium": 0, "High": 0},
        "weak_topics": [],
        "recommended_topics": [],
        "learning_history": [],
    }


def load_profile(profile_path: Path, name: str) -> Optional[Dict]:
    if not profile_path.exists():
        return None
    with profile_path.open("r", encoding="utf-8") as f:
        profiles = json.load(f).get("profiles", [])
    for profile in profiles:
        if profile.get("name") == name:
            return profile
    return None


def save_profile(profile_path: Path, profile: Dict):
    if profile_path.exists():
        with profile_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"profiles": []}
    existing = [p for p in data.get("profiles", []) if p.get("name") != profile.get("name")]
    existing.append(profile)
    with profile_path.open("w", encoding="utf-8") as f:
        json.dump({"profiles": existing}, f, indent=2)
