import csv
from datetime import datetime
from typing import List
from .flashcard import Flashcard


def loadFlashcards(filename: str) -> List[Flashcard]:
    flashcards: List[Flashcard] = []
    with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            flashcards.append(Flashcard(
                front=row['Front'],
                back=row['Back'],
                box=int(row['Box']),
                nextReviewDate=datetime.strptime(
                    row['NextReviewDate'], '%Y-%m-%d').date()
            ))
    return flashcards


def saveFlashcards(flashcards: List[Flashcard], filename: str) -> None:
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Front', 'Back', 'Box', 'NextReviewDate']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for card in flashcards:
            writer.writerow({
                'Front': card.front,
                'Back': card.back,
                'Box': card.box,
                'NextReviewDate': card.nextReviewDate.strftime('%Y-%m-%d')
            })
