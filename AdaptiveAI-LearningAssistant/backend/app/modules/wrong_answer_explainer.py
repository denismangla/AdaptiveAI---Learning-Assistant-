from app.modules.ollama_client import generate_text
from app.modules.fallback_library import get_fallback_wrong_answer_explanation


def generate_wrong_answer_explanation(question_id: str, student_answer: str, misconception: str | None = None) -> str:
    prompt = (
        f"A student answered '{student_answer}' to question {question_id} and got it wrong. "
        "Explain the most likely misconception and how to correct it in a friendly way. "
    )
    if misconception:
        prompt += f"Use the identified misconception: {misconception}. "
    response = generate_text(prompt, max_tokens=220, temperature=0.35)
    if response:
        return response
    return get_fallback_wrong_answer_explanation(misconception)
