# services/organizing_service.py
from typing import List
from models.initiative import Initiative

class OrganizingService:
    def __init__(self):
        self._initiatives: List[Initiative] = []
        self._counter = 1

    def create_initiative(self, name: str, description: str, neighborhood: str) -> Initiative:
        init = Initiative(id=self._counter, name=name, description=description, neighborhood=neighborhood)
        self._initiatives.append(init)
        self._counter += 1
        return init

    def list_initiatives(self) -> List[Initiative]:
        return self._initiatives