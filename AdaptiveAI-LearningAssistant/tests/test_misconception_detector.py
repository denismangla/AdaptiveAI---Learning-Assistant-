import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from app.modules.misconception_detector import detect_misconception


def test_detects_stack_fifo_confusion():
    result = detect_misconception("Stack", "What is a stack?", "A stack is FIFO and uses enqueue.")
    assert result == "Confuses FIFO and LIFO"


def test_detects_queue_lifo_confusion():
    result = detect_misconception("Queue", "What is a queue?", "A queue is LIFO and behaves like a stack.")
    assert result == "Confuses FIFO and LIFO"


def test_detects_linked_list_array_confusion():
    result = detect_misconception("Linked List", "What is a linked list?", "It stores items in a fixed-size array.")
    assert result == "Confuses nodes with arrays"
