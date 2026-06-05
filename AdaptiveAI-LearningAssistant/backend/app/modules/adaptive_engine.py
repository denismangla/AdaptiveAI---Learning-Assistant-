import json
import random
from pathlib import Path
from typing import Dict, Optional
from app.modules.confidence_tracker import update_confidence_counts
from app.modules.weak_topic_detector import detect_weak_topics

LEVEL_WEIGHT = {
    "Recognition": 1,
    "Understanding": 2,
    "Application": 3,
    "Debugging": 4,
}

RULES = {
    (True, "High"): "harder",
    (True, "Medium"): "similar",
    (True, "Low"): "similar_explanation",
    (False, "High"): "misconception",
    (False, "Low"): "easier_hint",
}


def evaluate_answer(answer: str, expected_answer: str) -> bool:
    return answer.strip().lower() == expected_answer.strip().lower()


def calculate_mastery(profile: Dict) -> float:
    scores = profile.get("scores", {})
    if not scores:
        return 0.0
    return round(sum(scores.values()) / len(scores), 2)


def detect_weak_topics(profile: Dict) -> Dict:
    weak = detect_weak_topics(profile)
    profile["weak_topics"] = weak
    return {"weak_topics": weak}


def update_student_profile(profile: Dict, topic: str, level: str, correct: bool, confidence: str):
    if topic not in profile["topics_attempted"]:
        profile["topics_attempted"].append(topic)
    counters = profile.setdefault("attempt_counters", {
        "Recognition": 0,
        "Understanding": 0,
        "Application": 0,
        "Debugging": 0,
    })
    scores = profile.setdefault("scores", {
        "Recognition": 0.0,
        "Understanding": 0.0,
        "Application": 0.0,
        "Debugging": 0.0,
    })
    level_name = level
    counters[level_name] += 1
    current = scores.get(level_name, 0.0)
    score_delta = 25 if correct else -10
    new_score = max(0, min(100, current + score_delta))
    scores[level_name] = round((current + new_score) / 2, 2) if current else new_score
    update_confidence_counts(profile, confidence)
    profile["learning_history"].append({
        "topic": topic,
        "level": level,
        "correct": correct,
        "confidence": confidence,
    })
    profile["recommended_topics"] = recommend_topics(profile)
    profile["weak_topics"] = detect_weak_topics(profile)


def select_next_question(profile: Dict, topic: str, previous_level: str, correct: bool, confidence: str) -> Dict:
    rule = RULES.get((correct, confidence), "similar")
    levels = ["Recognition", "Understanding", "Application", "Debugging"]
    current_index = levels.index(previous_level)
    if rule == "harder" and current_index < len(levels) - 1:
        next_level = levels[current_index + 1]
    elif rule == "easier_hint" and current_index > 0:
        next_level = levels[current_index - 1]
    elif rule == "similar_explanation" or rule == "similar" or rule == "misconception":
        next_level = previous_level
    else:
        next_level = previous_level
    question = load_question_sample(topic, next_level)
    return question


def recommend_topics(profile: Dict) -> list:
    weak = profile.get("weak_topics", [])
    if weak:
        return weak[:3]
    attempts = profile.get("topics_attempted", [])
    candidates = [topic for topic in ["Arrays", "Stack", "Queue", "Linked List"] if topic not in attempts]
    return candidates[:3] if candidates else ["Arrays", "Stack"]


def load_question_sample(topic: str, level: str) -> Dict:
    data_dir = Path(__file__).resolve().parents[1] / "data"
    fallback = {
        "id": f"sample-{topic}-{level}",
        "topic": topic,
        "level": level,
        "difficulty": "medium",
        "question": f"Describe a core concept for {topic} at the {level} level.",
        "options": [],
        "answer": "Core concept explanation",
    }
    try:
        with (data_dir / "topic_hierarchy.json").open("r", encoding="utf-8") as f:
            topics = json.load(f).get("topics", [])
            for item in topics:
                if item.get("name") == topic and level in item.get("levels", []):
                    return fallback
    except Exception:
        return fallback
    return fallback
