from app.modules.ollama_client import generate_text
from app.modules.fallback_library import get_fallback_explanation


def generate_explanation(question_id: str, topic: str) -> str:
    prompt = (
        f"Provide a clear educational explanation for the answer to question {question_id} "
        f"about {topic}. Include why the correct choice works and how the concept fits into programming practice."
    )
    response = generate_text(prompt)
    if response:
        return response
    return get_fallback_explanation(question_id.split("-")[-1])
