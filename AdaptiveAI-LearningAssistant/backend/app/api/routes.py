import json
from pathlib import Path
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.modules.question_generator import generate_question_for_topic
from app.modules.adaptive_engine import (
    evaluate_answer,
    select_next_question,
    update_student_profile,
)
from app.modules.analytics import build_analytics_summary
from app.modules.student_profile import load_profile, save_profile, create_student_profile
from app.modules.hint_generator import generate_hint
from app.modules.explanation_generator import generate_explanation
from app.modules.wrong_answer_explainer import generate_wrong_answer_explanation
from app.modules.adaptive_explanation_generator import generate_adaptive_explanation

router = APIRouter()
DATA_DIR = Path(__file__).resolve().parents[2] / "data"
PROFILE_FILE = DATA_DIR / "student_profiles.json"

class LoginRequest(BaseModel):
    name: str

class QuestionRequest(BaseModel):
    name: str
    topic: str
    level: str
    difficulty: str = "medium"

class AnswerRequest(BaseModel):
    name: str
    topic: str
    level: str
    question_id: str
    question_text: str = ""
    options: list[str] = []
    answer: str
    confidence: str
    expected_answer: str

@router.post("/login")
def login(data: LoginRequest):
    profile = load_profile(PROFILE_FILE, data.name)
    if profile is None:
        profile = create_student_profile(data.name)
        save_profile(PROFILE_FILE, profile)
    return profile

@router.get("/topics")
def get_topics():
    topic_file = DATA_DIR / "topic_hierarchy.json"
    with topic_file.open("r", encoding="utf-8") as f:
        return json.load(f)

@router.post("/question")
def question(data: QuestionRequest):
    profile = load_profile(PROFILE_FILE, data.name)
    if not profile:
        raise HTTPException(status_code=404, detail="Student profile not found")
    question_data = generate_question_for_topic(data.topic, data.level, data.difficulty)
    return question_data

@router.post("/answer")
def answer(data: AnswerRequest):
    profile = load_profile(PROFILE_FILE, data.name)
    if not profile:
        raise HTTPException(status_code=404, detail="Student profile not found")

    evaluation = evaluate_answer(
        data.answer,
        data.expected_answer,
        data.options,
        data.question_text,
        data.level,
    )
    correctness = evaluation["correct"]
    response = {
        "correct": correctness,
        "evaluation": evaluation,
        "hint": None,
        "explanation": None,
        "next_question": None,
        "adaptive_explanation": None,
    }
    if correctness:
        response["explanation"] = generate_explanation(data.question_id, data.topic)
        response["adaptive_explanation"] = generate_adaptive_explanation(True, data.confidence)
    else:
        response["hint"] = generate_hint(data.question_id, data.answer, data.confidence)
        response["explanation"] = generate_wrong_answer_explanation(data.question_id, data.answer)
        response["adaptive_explanation"] = generate_adaptive_explanation(False, data.confidence)

    update_student_profile(
        profile,
        data.topic,
        data.level,
        correctness,
        data.confidence,
        evaluation.get("confidence_score", 0),
    )
    save_profile(PROFILE_FILE, profile)
    next_question = select_next_question(profile, data.topic, data.level, correctness, data.confidence)
    response["next_question"] = next_question
    return response

@router.get("/analytics/{name}")
def analytics(name: str):
    profile = load_profile(PROFILE_FILE, name)
    if not profile:
        raise HTTPException(status_code=404, detail="Student profile not found")
    summary = build_analytics_summary(profile)
    return summary

@router.get("/profile/{name}")
def profile_route(name: str):
    profile = load_profile(PROFILE_FILE, name)
    if not profile:
        raise HTTPException(status_code=404, detail="Student profile not found")
    return profile
