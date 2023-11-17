import tkinter as tk
from tkinter import messagebox
import os
from typing import Iterator, List, Optional
from backend.flashcard import Flashcard
from backend.csvHandler import loadFlashcards, saveFlashcards
from backend.sessionProvider import SessionProvider


BACKGROUND_COLOR: str = "#B1DDC6"
CURRENT_DIRECTORY: str = os.path.dirname(__file__)
CSV_FILE: str = os.path.join(
    CURRENT_DIRECTORY, '..', 'data', 'periodicTablePractice.csv')


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title("Periodic Table Flashcards")
        self.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)
        self.frontTextId: Optional[int] = None
        self.backTextId: Optional[int] = None
        self.flashcards: List[Flashcard] = loadFlashcards(CSV_FILE)
        self.sessionProvider: SessionProvider = SessionProvider(self.flashcards)
        self.flashcardGenerator: Iterator[Flashcard] = self.sessionProvider.startSession()
        self.currentCard: Optional[Flashcard] = None
        self.createWidgets()
        self.nextFlashcard()

    def createWidgets(self) -> None:
        self.canvas = tk.Canvas(self, width=800, height=526)
        self.cardFrontImage = tk.PhotoImage(file=os.path.join(
            CURRENT_DIRECTORY, 'images', 'cardFront.png'))
        self.cardBackImage = tk.PhotoImage(file=os.path.join(
            CURRENT_DIRECTORY, 'images', 'cardBack.png'))
        self.canvasImage = self.canvas.create_image(400, 263, image=self.cardFrontImage)
        self.frontTextId = self.canvas.create_text(
            400, 140, text="", fill="black", font=("Arial", 60, "bold"))
        self.backTextId = self.canvas.create_text(
            400, 263, text="", fill="black", font=("Arial", 36, "normal"))
        self.canvas.configure(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.crossImage = tk.PhotoImage(file=os.path.join(
            CURRENT_DIRECTORY, 'images', 'wrong.png'))
        self.wrongButton = tk.Button(
            image=self.crossImage, highlightthickness=0, command=self.onWrong)
        self.wrongButton.grid(row=1, column=0)

        self.tickImage = tk.PhotoImage(file=os.path.join(
            CURRENT_DIRECTORY, 'images', 'right.png'))
        self.rightButton = tk.Button(
            image=self.tickImage, highlightthickness=0, command=self.onRight)
        self.rightButton.grid(row=1, column=1)

    def nextFlashcard(self):
        try:
            self.currentCard = next(self.flashcardGenerator)
            self.showFront()
        except StopIteration:
            self.endSession()

    def showFront(self):
        frontText = f"\n\nAtomic Number & Name?"
        self.canvas.itemconfig(self.frontTextId, text=self.currentCard.front)
        self.canvas.itemconfig(self.backTextId, text=frontText)
        self.canvas.itemconfig(self.canvasImage, image=self.cardFrontImage)
        self.wrongButton.config(state='disabled')
        self.rightButton.config(state='disabled')
        self.after(4000, self.showBack)

    def showBack(self):
        backFirst = self.currentCard.back.split('|')[0]
        backNext = self.currentCard.back.split('|')[1]
        backText = f"\n\nAtomic Number: {backFirst}\n\nName: {backNext}"
        self.canvas.itemconfig(self.backTextId, text=backText)
        self.canvas.itemconfig(self.canvasImage, image=self.cardBackImage)
        self.wrongButton.config(state='normal')
        self.rightButton.config(state='normal')

    def onRight(self):
        self.sessionProvider.processResponse(self.currentCard, 'right')
        self.nextFlashcard()

    def onWrong(self):
        self.sessionProvider.processResponse(self.currentCard, 'wrong')
        self.nextFlashcard()

    def endSession(self):
        self.sessionProvider.endSession()
        next_review_date = min(card.nextReviewDate for card in self.flashcards)
        messagebox.showinfo(
            "Session End", f"The next review date is: {next_review_date}")
        saveFlashcards(self.flashcards, CSV_FILE)
        self.destroy()
