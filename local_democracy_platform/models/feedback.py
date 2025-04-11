# models/feedback.py
from pydantic import BaseModel

class Feedback(BaseModel):
    id: int
    user_id: int
    representative_id: int
    message: str
    response: str = ""