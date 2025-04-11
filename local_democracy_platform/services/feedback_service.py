# services/feedback_service.py
from typing import List
from models.feedback import Feedback

class FeedbackService:
    def __init__(self):
        self._feedbacks: List[Feedback] = []
        self._counter = 1

    def submit_feedback(self, user_id: int, representative_id: int, message: str) -> Feedback:
        fb = Feedback(id=self._counter, user_id=user_id, representative_id=representative_id, message=message)
        self._feedbacks.append(fb)
        self._counter += 1
        return fb

    def get_feedback_responses(self, user_id: int) -> List[Feedback]:
        return [fb for fb in self._feedbacks if fb.user_id == user_id]