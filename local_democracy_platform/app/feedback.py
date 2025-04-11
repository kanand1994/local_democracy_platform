# app/feedback.py
from fastapi import APIRouter, Request
from services.feedback_service import FeedbackService

router = APIRouter()
feedback_service = FeedbackService()

@router.post("/feedback/submit")
async def submit_feedback(request: Request):
    data = await request.json()
    fb = feedback_service.submit_feedback(data["user_id"], data["representative_id"], data["message"])
    return {"feedback_id": fb.id}

@router.get("/feedback/responses/{user_id}")
async def get_responses(user_id: int):
    responses = feedback_service.get_feedback_responses(user_id)
    return {"responses": responses}