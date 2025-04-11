# models/issue.py
from pydantic import BaseModel

class Issue(BaseModel):
    id: int
    title: str
    description: str
    neighborhood: str
