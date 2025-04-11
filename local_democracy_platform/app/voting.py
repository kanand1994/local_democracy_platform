# app/voting.py
from fastapi import APIRouter, Request, HTTPException
from services.voting_service import VotingService

router = APIRouter()
voting_service = VotingService()

@router.post("/voting/create")
async def create_poll(request: Request):
    data = await request.json()
    poll_id = voting_service.create_poll(data["question"], data["options"])
    return {"poll_id": poll_id}

@router.post("/voting/vote")
async def vote(request: Request):
    data = await request.json()
    try:
        vote = voting_service.submit_vote(data["user_id"], data["poll_id"], data["option"])
        return {"vote_id": vote.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/voting/results/{poll_id}")
async def results(poll_id: int):
    try:
        return voting_service.get_poll_results(poll_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))