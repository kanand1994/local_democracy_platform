# models/initiative.py
from pydantic import BaseModel

class Initiative(BaseModel):
    id: int
    name: str
    description: str
    neighborhood: str