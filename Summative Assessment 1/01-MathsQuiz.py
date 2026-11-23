import random
from tkinter import BOTH, BOTTOM, Button, Entry, Frame, Label, StringVar, Tk
from tkinter import messagebox
from tkinter import ttk


TOTAL_QUESTIONS = 10


def randomInt(difficulty):
    """Return a random intege
    r using the range defined by the difficulty level."""
    ranges = {
        "Easy": (0, 9),
        "Moderate": (10, 99),
        "Advanced": (1000, 9999),
    }
    minimum, maximum = ranges[difficulty]
    return random.randint(minimum, maximum)


def decideOperation():
    """Randomly return '+' for addition or '-' for subtraction."""
    return random.choice(("+", "-"))


def isCorrect(user_answer, correct_answer):
    """Check an answer and return a result flag."""
    return user_answer == correct_answer


class MathsQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Maths Quiz")
        self.root.geometry("760x560")
        self.root.minsize(650, 480)
        self.root.configure(bg="#eef3f8")

        self.score = 0
        self.question_number = 0
        self.attempt = 0
        self.difficulty = ""
        self.current_answer = 0
        self.answer_var = StringVar()
        self.container = Frame(root, bg="#eef3f8")
        self.container.pack(fill=BOTH, expand=True, padx=24, pady=24)

        self.displayMenu()

    def clearScreen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def displayMenu(self):
        """Display the starting menu and difficulty selections."""
        self.score = 0
        self.question_number = 0
        self.clearScreen()

        card = Frame(self.container, bg="white", padx=36, pady=30)
        card.pack(fill=BOTH, expand=True)

        Label(
            card,
            text="MATHS QUIZ",
            font=("Segoe UI", 28, "bold"),
            fg="#183b56",
            bg="white",
        ).pack(pady=(10, 4))

        Label(
            card,
            text="Choose your difficulty",
            font=("Segoe UI", 13),
            fg="#657786",
            bg="white",
        ).pack(pady=(0, 28))

        difficulties = (
            ("Easy", "1 digit numbers", "#38a169"),
            ("Moderate", "2 digit numbers", "#3182ce"),
            ("Advanced", "4 digit numbers", "#805ad5"),
        )

        for name, description, colour in difficulties:
            button_frame = Frame(card, bg="white")
            button_frame.pack(pady=7)
            Button(
                button_frame,
                text=name,
                command=lambda level=name: self.startQuiz(level),
                width=16,
                height=2,
                font=("Segoe UI", 13, "bold"),
                fg="white",
                bg=colour,
                activebackground=colour,
                activeforeground="white",
                relief="flat",
                cursor="hand2",
            ).pack(side="left")
            Label(
                button_frame,
                text=description,
                width=22,
                anchor="w",
                font=("Segoe UI", 11),
                fg="#4a5568",
                bg="white",
            ).pack(side="left", padx=(14, 0))

        Label(
            card,
            text="10 questions  •  10 points on attempt 1  •  5 points on attempt 2",
            font=("Segoe UI", 10),
            fg="#718096",
            bg="white",
        ).pack(side=BOTTOM, pady=(22, 4))

    def startQuiz(self, difficulty):
        self.difficulty = difficulty
        self.score = 0
        self.question_number = 0
        self.answer_var.set("")
        self.displayProblem()

    def displayProblem(self):
        """Display the current question and accept an answer."""
        self.attempt = 0
        self.answer_var.set("")
        self.clearScreen()

        card = Frame(self.container, bg="white", padx=32, pady=24)
        card.pack(fill=BOTH, expand=True)

        top = Frame(card, bg="white")
        top.pack(fill="x")

        Label(
            top,
            text=f"{self.difficulty} Level",
            font=("Segoe UI", 12, "bold"),
            fg="#3182ce",
            bg="white",
        ).pack(side="left")

        Label(
            top,
            text=f"Score: {self.score}",
            font=("Segoe UI", 12, "bold"),
            fg="#183b56",
            bg="white",
        ).pack(side="right")

        progress = ttk.Progressbar(
            card,
            length=600,
            mode="determinate",
            maximum=TOTAL_QUESTIONS,
            value=self.question_number,
        )
        progress.pack(pady=(18, 24))

        Label(
            card,
            text=f"Question {self.question_number + 1} of {TOTAL_QUESTIONS}",
            font=("Segoe UI", 11),
            fg="#718096",
            bg="white",
        ).pack()

        first_number = randomInt(self.difficulty)
        second_number = randomInt(self.difficulty)
        operation = decideOperation()

        if operation == "+":
            self.current_answer = first_number + second_number
        else:
            self.current_answer = first_number - second_number

        question = f"{first_number} {operation} {second_number} ="
        Label(
            card,
            text=question,
            font=("Segoe UI", 30, "bold"),
            fg="#183b56",
            bg="white",
        ).pack(pady=(18, 16))

        answer_entry = Entry(
            card,
            textvariable=self.answer_var,
            font=("Segoe UI", 18),
            justify="center",
            width=14,
        )
        answer_entry.pack(ipady=7)

        feedback = Label(
            card,
            text="Enter your answer",
            font=("Segoe UI", 11),
            fg="#718096",
            bg="white",
        )
        feedback.pack(pady=(12, 8))

        submit = Button(
            card,
            text="Submit Answer",
            command=lambda: self.checkAnswer(answer_entry, feedback),
            font=("Segoe UI", 12, "bold"),
            fg="white",
            bg="#183b56",
            activebackground="#102a43",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=18,
        )
        submit.pack(ipady=7)

        answer_entry.bind("<Return>", lambda event: self.checkAnswer(answer_entry, feedback))
        answer_entry.focus_set()

    def checkAnswer(self, answer_entry, feedback):
        try:
            user_answer = int(answer_entry.get().strip())
        except ValueError:
            feedback.config(text="Please enter a whole number.", fg="#c05621")
            answer_entry.focus_set()
            return

        if isCorrect(user_answer, self.current_answer):
            if self.attempt == 0:
                self.score += 10
                feedback.config(text="Correct! 10 points awarded.", fg="#2f855a")
            else:
                self.score += 5
                feedback.config(text="Correct on the second try! 5 points awarded.", fg="#2f855a")

            self.question_number += 1
            self.root.after(700, self.moveToNextQuestion)
            return

        if self.attempt == 0:
            self.attempt = 1
            feedback.config(text="Not quite — one more try!", fg="#c05621")
            self.answer_var.set("")
            answer_entry.focus_set()
        else:
            feedback.config(
                text=f"Incorrect again. The answer was {self.current_answer}.",
                fg="#c53030",
            )
            self.question_number += 1
            self.root.after(1100, self.moveToNextQuestion)

    def moveToNextQuestion(self):
        if self.question_number < TOTAL_QUESTIONS:
            self.displayProblem()
        else:
            self.displayResults()

    def displayResults(self):
        """Display the final score and a grade for the completed quiz."""
        self.clearScreen()

        card = Frame(self.container, bg="white", padx=36, pady=30)
        card.pack(fill=BOTH, expand=True)

        Label(
            card,
            text="Quiz Complete!",
            font=("Segoe UI", 25, "bold"),
            fg="#183b56",
            bg="white",
        ).pack(pady=(20, 8))

        Label(
            card,
            text=f"{self.score} / 100",
            font=("Segoe UI", 42, "bold"),
            fg="#3182ce",
            bg="white",
        ).pack()

        grade = self.getGrade(self.score)
        Label(
            card,
            text=f"Grade: {grade}",
            font=("Segoe UI", 20, "bold"),
            fg="#805ad5",
            bg="white",
        ).pack(pady=(4, 18))

        message = {
            "A+": "Outstanding work!",
            "A": "Excellent result!",
            "B": "Well done!",
            "C": "Good effort!",
            "D": "Keep practising!",
            "F": "Try again and improve!",
        }[grade]

        Label(
            card,
            text=message,
            font=("Segoe UI", 12),
            fg="#657786",
            bg="white",
        ).pack(pady=(0, 22))

        Button(
            card,
            text="Play Again",
            command=lambda: self.displayMenu(),
            font=("Segoe UI", 12, "bold"),
            fg="white",
            bg="#38a169",
            activebackground="#2f855a",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=18,
        ).pack(ipady=7)

        Button(
            card,
            text="Exit",
            command=self.root.destroy,
            font=("Segoe UI", 11),
            fg="#718096",
            bg="#edf2f7",
            activebackground="#e2e8f0",
            activeforeground="#4a5568",
            relief="flat",
            cursor="hand2",
            width=18,
        ).pack(pady=(10, 0), ipady=5)

    @staticmethod
    def getGrade(score):
        if score > 90:
            return "A+"
        if score >= 80:
            return "A"
        if score >= 70:
            return "B"
        if score >= 60:
            return "C"
        if score >= 50:
            return "D"
        return "F"


if __name__ == "__main__":
    root = Tk()
    MathsQuiz(root)
    root.mainloop()