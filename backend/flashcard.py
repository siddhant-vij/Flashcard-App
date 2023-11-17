from datetime import datetime, timedelta
from typing import Optional


class Flashcard:
    def __init__(self, front: str, back: str, box: int = 1, nextReviewDate: Optional[datetime.date] = None):
        self.front = front
        self.back = back
        self.box = box
        self.nextReviewDate = nextReviewDate or datetime.now().date()

    def promote(self) -> None:
        if self.box < 3:
            self.box += 1
        self.updateNextReviewDate()

    def demote(self) -> None:
        if self.box > 1:
            self.box -= 1
        self.updateNextReviewDate()

    def updateNextReviewDate(self) -> None:
        intervals = {1: 1, 2: 3, 3: 5}
        self.nextReviewDate = datetime.now().date() + \
            timedelta(days=intervals[self.box])

    def __repr__(self) -> str:
        return f'Flashcard(front="{self.front}", back="{self.back}", box={self.box}, nextReviewDate="{self.nextReviewDate}")'
