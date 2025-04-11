# app/organizing.py
from fastapi import APIRouter, Request
from services.organizing_service import OrganizingService

router = APIRouter()
organizing_service = OrganizingService()

@router.post("/organizing/create")
async def create_initiative(request: Request):
    data = await request.json()
    init = organizing_service.create_initiative(data["name"], data["description"], data["neighborhood"])
    return {"initiative_id": init.id}

@router.get("/organizing/list")
async def list_initiatives():
    return organizing_service.list_initiatives()