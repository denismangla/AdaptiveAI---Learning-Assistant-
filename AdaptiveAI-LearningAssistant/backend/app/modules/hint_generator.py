from app.modules.ollama_client import generate_text
from app.modules.fallback_library import get_fallback_hint


def generate_hint(question_id: str, student_answer: str, confidence: str) -> str:
    prompt = (
        f"Generate a concise hint for a student who answered '{student_answer}' to question {question_id}. "
        "The hint should be supportive, help the learner build confidence, and guide them to the right concept. "
        f"The student selected confidence level {confidence}."
    )
    response = generate_text(prompt)
    if response:
        return response
    return get_fallback_hint(confidence)
