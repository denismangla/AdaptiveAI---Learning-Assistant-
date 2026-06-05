from typing import Dict

QUESTION_FALLBACKS = {
    "Arrays": {
        "Recognition": {
            "question": "Which of the following is a valid way to declare an array in Python?",
            "options": ["a = [1, 2, 3]", "a = (1, 2, 3)", "a = {1, 2, 3}", "a = 1, 2, 3"],
            "answer": "a = [1, 2, 3]",
        }
    }
}

DEFAULT_HINTS = {
    "recognition": "Review the basic syntax for the topic and choose the answer that matches the standard pattern.",
    "understanding": "Think about what the question is asking and express the concept in your own words.",
    "application": "Apply the rules from the topic to the scenario described in the question.",
    "debugging": "Look for syntax and logical errors step by step in the code snippet.",
}

DEFAULT_EXPLANATIONS = {
    "recognition": "This question checks whether you can identify the correct syntax or definition for the programming construct.",
    "understanding": "Understanding questions ask you to explain the concept rather than just recognize it.",
    "application": "Application questions require that you take a concept and use it in a practical situation.",
    "debugging": "Debugging questions ask you to analyze code and find the mistake or behavior causing the error.",
}

DEFAULT_EXAMPLES = {
    "Arrays": "Example: Use arrays when you need to store multiple values in a fixed ordering and access them by index.",
    "Stack": "Example: A stack follows last-in, first-out behavior; push items in and pop the most recent item out.",
}

WRONG_ANSWER_EXPLANATIONS = {
    "default": "The answer did not align with the core ideas of the question. Break the problem down and compare your result with the correct pattern.",
}


def get_fallback_question(topic: str, level: str) -> Dict:
    topic_data = QUESTION_FALLBACKS.get(topic, {})
    fallback = topic_data.get(level)
    if fallback:
        return {
            "id": f"fallback-{topic}-{level}",
            "topic": topic,
            "level": level,
            "difficulty": "easy",
            "question": fallback["question"],
            "options": fallback["options"],
            "answer": fallback["answer"],
        }
    return {
        "id": f"fallback-{topic}-{level}",
        "topic": topic,
        "level": level,
        "difficulty": "easy",
        "question": f"Provide one core fact about {topic} at the {level} level.",
        "options": [],
        "answer": "Core concept explanation",
    }


def get_fallback_hint(level: str) -> str:
    return DEFAULT_HINTS.get(level.lower(), "Take a moment to review the fundamentals and the question carefully.")


def get_fallback_explanation(level: str) -> str:
    return DEFAULT_EXPLANATIONS.get(level.lower(), "This explanation is meant to clarify the core concept behind the question.")


def get_fallback_example(topic: str) -> str:
    return DEFAULT_EXAMPLES.get(topic, f"Use a concrete example to explain the role of {topic} in programming.")


def get_fallback_wrong_answer_explanation() -> str:
    return WRONG_ANSWER_EXPLANATIONS["default"]
