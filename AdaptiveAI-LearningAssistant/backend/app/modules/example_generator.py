from app.modules.ollama_client import generate_text
from app.modules.fallback_library import get_fallback_example


def generate_example(topic: str, level: str) -> str:
    prompt = (
        f"Generate a simple programming example for {topic} at the {level} level. "
        "The example should illustrate how the concept is used in practice."
    )
    response = generate_text(prompt)
    if response:
        return response
    return get_fallback_example(topic)
