from app.modules.ollama_client import generate_text
from app.modules.fallback_library import get_fallback_wrong_answer_explanation


def generate_wrong_answer_explanation(question_id: str, student_answer: str) -> str:
    prompt = (
        f"A student answered '{student_answer}' to question {question_id} and got it wrong. "
        "Explain the most likely misconception and how to correct it in a friendly way."
    )
    response = generate_text(prompt)
    if response:
        return response
    return get_fallback_wrong_answer_explanation()
