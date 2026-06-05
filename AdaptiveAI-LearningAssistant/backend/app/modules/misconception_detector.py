from typing import Optional

COMMON_MISCONCEPTIONS = {
    "Stack": [
        ("fifo", "Confuses FIFO and LIFO"),
        ("first in first out", "Confuses FIFO and LIFO"),
        ("queue", "Confuses FIFO and LIFO"),
        ("enqueue", "Confuses FIFO and LIFO"),
        ("dequeue", "Confuses FIFO and LIFO"),
        ("confusing push", "Confusing Push and Pop"),
        ("confusing pop", "Confusing Push and Pop"),
    ],
    "Queue": [
        ("lifo", "Confuses FIFO and LIFO"),
        ("last in first out", "Confuses FIFO and LIFO"),
        ("stack", "Confuses FIFO and LIFO"),
        ("push", "Confuses Enqueue and Dequeue"),
        ("pop", "Confuses Enqueue and Dequeue"),
        ("top of stack", "Confuses FIFO and LIFO"),
    ],
    "Linked List": [
        ("array", "Confuses nodes with arrays"),
        ("index", "Confuses nodes with arrays"),
        ("continuous memory", "Confuses nodes with arrays"),
        ("fixed size", "Confuses nodes with arrays"),
    ],
}


def detect_misconception(topic: str, question_text: str, student_answer: str) -> Optional[str]:
    answer_text = (student_answer or "").lower()
    question_text = (question_text or "").lower()
    candidates = COMMON_MISCONCEPTIONS.get(topic, [])
    for keyword, misconception in candidates:
        if keyword in answer_text or keyword in question_text:
            return misconception
    return None
