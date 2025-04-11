# models/legislation.py
from pydantic import BaseModel

class Legislation(BaseModel):
    id: int
    title: str
    text: str