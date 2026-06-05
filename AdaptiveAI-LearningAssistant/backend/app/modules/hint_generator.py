from app.modules.ollama_client import generate_text
from app.modules.fallback_library import get_fallback_hint_levels


def _parse_hint_response(response: str) -> dict:
    hints = {"hint1": None, "hint2": None, "hint3": None}
    lines = [line.strip() for line in response.splitlines() if line.strip()]
    for line in lines:
        lower = line.lower()
        if "hint 1" in lower or lower.startswith("1."):
            hints["hint1"] = line.split(":", 1)[1].strip() if ":" in line else line
        elif "hint 2" in lower or lower.startswith("2."):
            hints["hint2"] = line.split(":", 1)[1].strip() if ":" in line else line
        elif "hint 3" in lower or lower.startswith("3."):
            hints["hint3"] = line.split(":", 1)[1].strip() if ":" in line else line
    extracted = {k: v for k, v in hints.items() if v}
    if len(extracted) == 3:
        extracted["hint"] = extracted["hint3"]
        return extracted

    if len(lines) >= 3:
        return {
            "hint1": lines[0],
            "hint2": lines[1],
            "hint3": lines[2],
            "hint": lines[2],
        }

    if lines:
        text = " ".join(lines)
        return {
            "hint1": text,
            "hint2": text,
            "hint3": text,
            "hint": text,
        }

    return {"hint1": None, "hint2": None, "hint3": None, "hint": ""}


def generate_hint_levels(question_id: str, student_answer: str, confidence: str) -> dict:
    prompt = (
        f"Generate three progressively stronger hints for a student who answered '{student_answer}' to question {question_id}. "
        "Hint 1 should offer a small clue, Hint 2 should offer a stronger clue, and Hint 3 should offer near-complete guidance. "
        f"Use positive language and keep the hints aligned with a student confidence level of {confidence}."
    )
    response = generate_text(prompt, max_tokens=220, temperature=0.35)
    if response:
        parsed = _parse_hint_response(response)
        if parsed["hint"]:
            return parsed
    return get_fallback_hint_levels(confidence)


def generate_hint(question_id: str, student_answer: str, confidence: str) -> dict:
    return generate_hint_levels(question_id, student_answer, confidence)
