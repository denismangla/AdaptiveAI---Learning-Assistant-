from typing import Dict, List

QUESTION_FALLBACKS = {
    "Arrays": {
        "Recognition": {
            "question": "Which of the following is a valid way to declare an array in Python?",
            "options": ["a = [1, 2, 3]", "a = (1, 2, 3)", "a = {1, 2, 3}", "a = 1, 2, 3"],
            "answer": "a = [1, 2, 3]",
        }
    }
}

DEFAULT_HINT_LEVELS: Dict[str, List[str]] = {
    "recognition": [
        "Review the basic syntax for the topic and what the question is asking.",
        "Consider the core concept the question expects and focus on the simplest definition.",
        "The correct answer will match the standard behavior or form for the concept.",
    ],
    "understanding": [
        "Think about the main idea behind the concept rather than the exact wording.",
        "Break the concept down into smaller pieces and connect them to the question.",
        "Use the definition of the topic to guide your response and focus on the relationship between the parts.",
    ],
    "application": [
        "Review the rule or pattern that applies to the scenario in the question.",
        "Map the scenario to the concept and identify which part of the topic is being used.",
        "Apply the key operation or behavior step by step to solve the example.",
    ],
    "debugging": [
        "Check the program flow or the order of operations carefully.",
        "Identify where the behavior diverges from the expected result.",
        "Focus on the exact statement or line that causes the incorrect behavior.",
    ],
    "default": [
        "Review the idea behind the question before choosing an answer.",
        "Focus on one key concept that is most relevant to the problem.",
        "Use the strongest clue to nudge yourself toward the correct response.",
    ],
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
    hint_levels = get_fallback_hint_levels(level)
    return hint_levels.get("hint3", hint_levels["hint1"])


def get_fallback_hint_levels(level: str) -> Dict[str, str]:
    hint_set = DEFAULT_HINT_LEVELS.get(level.lower(), DEFAULT_HINT_LEVELS["default"])
    return {
        "hint1": hint_set[0],
        "hint2": hint_set[1],
        "hint3": hint_set[2],
        "hint": hint_set[2],
    }


def get_fallback_explanation(level: str) -> str:
    return DEFAULT_EXPLANATIONS.get(level.lower(), "This explanation is meant to clarify the core concept behind the question.")


def get_fallback_example(topic: str) -> str:
    return DEFAULT_EXAMPLES.get(topic, f"Use a concrete example to explain the role of {topic} in programming.")


def get_fallback_wrong_answer_explanation(misconception: str | None = None) -> str:
    if misconception:
        return (
            f"A common misconception is: {misconception}. "
            "Focus on the key difference and try to separate the two concepts clearly."
        )
    return WRONG_ANSWER_EXPLANATIONS["default"]
