import random
from difflib import SequenceMatcher
from typing import Dict, List, Optional
from app.modules.ollama_client import generate_text
from app.modules.fallback_library import get_fallback_question

LEVEL_PROMPTS = {
    "Recognition": (
        "Generate a recognition-level question for {topic}. "
        "Use multiple choice, true/false, or fill-in-the-blank format only. "
        "Include an explicit Answer: line. "
        "If you provide multiple choice, include 3 or 4 labeled options. "
        "Do not generate an open-ended short-answer question for Recognition."
    ),
    "Understanding": (
        "Generate a short-answer or concept-explanation question for {topic}. "
        "Ask the student to explain a core idea or describe a concept in their own words."
    ),
    "Application": (
        "Generate a scenario-based question for {topic} that requires applying the concept to a realistic example or use case."
    ),
    "Debugging": (
        "Generate a code analysis or error-identification question for {topic}. "
        "Ask the student to explain the behavior, find the bug, or predict the output."
    ),
}


def _is_near_duplicate(candidate_question: str, recent_questions: List[Dict[str, str]]) -> bool:
    normalized_candidate = candidate_question.lower().strip()
    for entry in recent_questions:
        existing = entry.get("question", "").lower().strip()
        ratio = SequenceMatcher(None, normalized_candidate, existing).ratio()
        if ratio > 0.85 or normalized_candidate == existing:
            return True
    return False


def generate_question_for_topic(topic: str, level: str, difficulty: str = "medium", profile: Optional[Dict] = None) -> Dict:
    prompt_template = LEVEL_PROMPTS.get(level)
    if not prompt_template:
        return get_fallback_question(topic, level)

    recent_questions = profile.get("recent_questions", []) if profile else []
    question = None
    for attempt in range(3):
        prompt = prompt_template.format(topic=topic)
        prompt += " Use clear programming education language and include a correct answer and options if needed."
        if attempt > 0:
            prompt += " Do not repeat questions asked previously for this student."
        response = generate_text(prompt)
        if not response:
            continue
        candidate = parse_response_to_question(response, topic, level, difficulty)
        if candidate and not _is_near_duplicate(candidate.get("question", ""), recent_questions):
            question = candidate
            break

    if not question:
        question = get_fallback_question(topic, level)
    return question


def parse_response_to_question(response: str, topic: str, level: str, difficulty: str = "medium") -> Dict:
    lines = [line.strip() for line in response.splitlines() if line.strip()]
    if not lines:
        return get_fallback_question(topic, level)
    question = lines[0]
    options: List[str] = []
    answer = ""
    for line in lines[1:]:
        candidate = line.lstrip("- ").strip()
        lower_candidate = candidate.lower()
        if lower_candidate.startswith("answer:"):
            answer = candidate.split(":", 1)[1].strip()
        elif candidate and (candidate[0].isalpha() or candidate[0].isdigit()):
            options.append(candidate)
    if not answer and options:
        answer = options[0]

    normalized_question = question.lower()
    if level == "Recognition":
        if not options and "___" not in normalized_question and "true/false" not in normalized_question and "true or false" not in normalized_question:
            return get_fallback_question(topic, level)

    if not question or not answer:
        return get_fallback_question(topic, level)

    return {
        "id": f"q-{topic}-{level}-{random.randint(1000,9999)}",
        "topic": topic,
        "level": level,
        "difficulty": difficulty,
        "question": question,
        "options": options,
        "answer": answer,
    }
