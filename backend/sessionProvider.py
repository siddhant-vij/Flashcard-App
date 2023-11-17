import random
from collections import deque
from datetime import datetime
from typing import Deque, Dict, Iterable, List

from .flashcard import Flashcard


class SessionProvider:
    def __init__(self, flashcards: List[Flashcard]) -> None:
        self.flashcards: List[Flashcard] = flashcards
        self.reviewQueue: Deque[Flashcard] = deque(self.getCardsForReview())
        self.attemptTracker: Dict[Flashcard, int] = {}

    def getCardsForReview(self) -> List[Flashcard]:
        tempListCards = [card for card in self.flashcards if card.nextReviewDate <=
                datetime.now().date()]
        random.shuffle(tempListCards)
        return tempListCards

    def startSession(self) -> Iterable[Flashcard]:
        while self.reviewQueue:
            currentCard = self.reviewQueue.popleft()
            self.attemptTracker[currentCard] = self.attemptTracker.get(
                currentCard, 0) + 1
            yield currentCard

    def processResponse(self, card: Flashcard, response: str) -> None:
        first_attempt = self.attemptTracker.get(card, 0) == 1
        if response == 'right':
            if first_attempt:
                card.promote()
            else:
                card.updateNextReviewDate()
            self.attemptTracker.pop(card, None)
        elif response == 'wrong':
            if first_attempt:
                self.reviewQueue.append(card)
                self.attemptTracker[card] = 2
            else:
                card.demote()
                self.attemptTracker.pop(card, None)
                if card in self.reviewQueue:
                    self.reviewQueue.remove(card)

    def endSession(self) -> None:
        self.attemptTracker.clear()
