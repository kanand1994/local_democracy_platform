# services/voting_service.py
from typing import List, Dict
from models.vote import Vote

class VotingService:
    def __init__(self):
        self._polls: Dict[int, Dict] = {}
        self._votes: List[Vote] = []
        self._poll_counter = 1
        self._vote_counter = 1

    def create_poll(self, question: str, options: List[str]) -> int:
        poll_id = self._poll_counter
        self._polls[poll_id] = {"question": question, "options": options, "votes": {opt: 0 for opt in options}}
        self._poll_counter += 1
        return poll_id

    def submit_vote(self, user_id: int, poll_id: int, option: str) -> Vote:
        if poll_id not in self._polls or option not in self._polls[poll_id]["options"]:
            raise ValueError("Invalid poll or option")
        vote = Vote(id=self._vote_counter, user_id=user_id, poll_id=poll_id, option=option)
        self._votes.append(vote)
        self._polls[poll_id]["votes"][option] += 1
        self._vote_counter += 1
        return vote

    def get_poll_results(self, poll_id: int) -> Dict:
        if poll_id not in self._polls:
            raise ValueError("Poll not found")
        poll = self._polls[poll_id]
        return {"question": poll["question"], "results": poll["votes"]}