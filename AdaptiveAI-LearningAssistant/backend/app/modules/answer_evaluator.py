import json
import re
from difflib import SequenceMatcher
from typing import Dict, List, Optional
from app.modules.ollama_client import generate_text


def _parse_json_response(response: str) -> Optional[Dict]:
    try:
        return json.loads(response.strip())
    except Exception:
        match = re.search(r"\{.*\}", response, re.S)
        if match:
            try:
                return json.loads(match.group())
            except Exception:
                return None
    return None


def is_mcq(options: Optional[List[str]], expected_answer: str, answer: str) -> bool:
    if options:
        return True
    normalized_expected = expected_answer.strip().lower()
    normalized_answer = answer.strip().lower()
    if normalized_expected in {"true", "false"} and normalized_answer in {"true", "false"}:
        return True
    if normalized_expected in {"a", "b", "c", "d"} and normalized_answer in {"a", "b", "c", "d"}:
        return True
    return False


def _normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def evaluate_answer(
    student_answer: str,
    expected_answer: str,
    options: Optional[List[str]] = None,
    question_text: str = "",
    level: str = "",
) -> Dict:
    student_answer = _normalize_text(student_answer)
    expected_answer = _normalize_text(expected_answer)
    if not student_answer:
        return {
            "correct": False,
            "label": "Incorrect",
            "confidence_score": 0,
            "reason": "No answer was provided.",
        }
    if is_mcq(options, expected_answer, student_answer):
        correct = student_answer.strip().lower() == expected_answer.strip().lower()
        return {
            "correct": correct,
            "label": "Correct" if correct else "Incorrect",
            "confidence_score": 100 if correct else 0,
            "reason": "MCQ exact matching uses the selected option as the evaluation criterion.",
        }

    prompt = (
        "You are a programming education evaluator. Compare the student answer to the expected answer. "
        "For short answer, application, and debugging questions, assess whether the student response is semantically correct. "
        f"Question: {question_text}\n"
        f"Expected Answer: {expected_answer}\n"
        f"Student Answer: {student_answer}\n"
        f"Level: {level}\n"
        "Respond with JSON only and no extra text. Use these keys:\n"
        "correct: \"Correct\" or \"Incorrect\"\n"
        "confidence_score: integer 0-100\n"
        "reason: short statement explaining your judgment.\n"
    )
    response = generate_text(prompt, max_tokens=220, temperature=0.2)
    parsed = _parse_json_response(response or "") if response else None
    if parsed:
        correct_label = str(parsed.get("correct", "Incorrect")).strip()
        confidence_value = parsed.get("confidence_score", 0)
        reason = str(parsed.get("reason", "Evaluated using semantic comparison.")).strip()
        try:
            confidence = max(0, min(100, int(confidence_value)))
        except Exception:
            confidence = 0
        return {
            "correct": correct_label.lower() == "correct",
            "label": "Correct" if correct_label.lower() == "correct" else "Incorrect",
            "confidence_score": confidence,
            "reason": reason,
        }

    similarity = SequenceMatcher(None, student_answer.lower(), expected_answer.lower()).ratio()
    confidence = int(round(similarity * 100))
    correct = similarity >= 0.65
    reason = (
        "Semantic similarity indicates that the answer is likely correct."
        if correct
        else "The answer does not sufficiently match the expected concept."
    )
    return {
        "correct": correct,
        "label": "Correct" if correct else "Incorrect",
        "confidence_score": confidence,
        "reason": reason,
    }
