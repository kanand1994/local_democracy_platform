# app/legislation.py
from fastapi import APIRouter, Request
from services.legislation_service import LegislationService

router = APIRouter()
legislation_service = LegislationService()

@router.post("/legislation/summarize")
async def summarize_legislation(request: Request):
    data = await request.json()
    text = data.get("text", "")
    summary = legislation_service.summarize_legislation(text)
    return {"summary": summary}
