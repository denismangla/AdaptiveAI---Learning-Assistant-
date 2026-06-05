import random
from typing import Dict
from app.modules.ollama_client import generate_text
from app.modules.fallback_library import get_fallback_question

LEVEL_PROMPTS = {
    "Recognition": "Write a short multiple choice or true/false question that asks the student to recognize a basic fact about {topic}.",
    "Understanding": "Create a short answer question that asks the student to explain a core concept of {topic}.",
    "Application": "Write a scenario-based application question that requires using {topic} in a practical programming situation.",
    "Debugging": "Generate a code analysis or debugging question where the student must identify the issue or explain the behavior of {topic} code.",
}


def generate_question_for_topic(topic: str, level: str, difficulty: str = "medium") -> Dict:
    prompt_template = LEVEL_PROMPTS.get(level)
    if not prompt_template:
        return get_fallback_question(topic, level)
    prompt = prompt_template.format(topic=topic)
    prompt += " Use clear programming education language and include a correct answer and options if needed."
    response = generate_text(prompt)
    if not response:
        return get_fallback_question(topic, level)
    question_text = parse_response_to_question(response, topic, level)
    return question_text


def parse_response_to_question(response: str, topic: str, level: str) -> Dict:
    lines = [line.strip() for line in response.splitlines() if line.strip()]
    if not lines:
        return get_fallback_question(topic, level)
    question = lines[0]
    options = []
    answer = ""
    for line in lines[1:]:
        candidate = line.lstrip("- ").strip()
        if candidate.lower().startswith("answer:"):
            answer = candidate.split(":", 1)[1].strip()
        elif candidate and (candidate[0].isalpha() or candidate[0].isdigit()):
            options.append(candidate)
    if not answer and options:
        answer = options[0]
    return {
        "id": f"q-{topic}-{level}-{random.randint(1000,9999)}",
        "topic": topic,
        "level": level,
        "difficulty": difficulty,
        "question": question,
        "options": options,
        "answer": answer,
    }
