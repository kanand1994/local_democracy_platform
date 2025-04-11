# models/vote.py
from pydantic import BaseModel

class Vote(BaseModel):
    id: int
    user_id: int
    poll_id: int
    option: str