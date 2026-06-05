from typing import Optional


RULE_TEXT = {
    (True, "High"): "Because you answered correctly with high confidence, the system will offer a more challenging follow-up question to stretch your understanding.",
    (True, "Medium"): "Your answer is correct and your confidence is steady, so the next item will stay at a similar level of challenge.",
    (True, "Low"): "You answered correctly but with low confidence, so the system provides an explanation and a similar practice question to reinforce the concept.",
    (False, "High"): "A wrong answer with high confidence usually indicates a misconception, so the system offers a focused explanation to correct the misunderstanding.",
    (False, "Low"): "A wrong answer with low confidence suggests you are still building the skill, so the assistant gives a hint and moves to a slightly easier follow-up.",
}


def generate_adaptive_explanation(correct: bool, confidence: str) -> str:
    return RULE_TEXT.get((correct, confidence), "The system adapts based on your response and confidence to keep learning effective.")
