import requests

OLLAMA_URL = "http://127.0.0.1:11434/v1/generate"
MODEL_NAME = "gemma3:1b-it-qat"
TIMEOUT_SECONDS = 15


def generate_text(prompt: str, model: str = MODEL_NAME, max_tokens: int = 256, temperature: float = 0.2):
    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=TIMEOUT_SECONDS)
        response.raise_for_status()
        data = response.json()
        return data.get("text", "").strip()
    except Exception:
        return None
