from typing import Optional


RULE_TEXT = {
    (True, "High"): "Great job! The next question will be a little more challenging to keep your understanding growing.",
    (True, "Medium"): "Nice work — the next question will stay at a similar challenge so you can build confidence.",
    (True, "Low"): "Correct answer! We'll reinforce the concept with another example so you feel more secure.",
    (False, "High"): "You had strong confidence, so this response helps correct a likely misunderstanding with a clear explanation.",
    (False, "Low"): "You're still building this skill, so we'll offer a helpful hint and a gentler follow-up question.",
}


def generate_adaptive_explanation(correct: bool, confidence: str) -> str:
    return RULE_TEXT.get((correct, confidence), "The system adapts based on your response and confidence to keep learning effective.")
