import customtkinter as ctk
from customtkinter import CTkFont as Font

from ai_classes import Feedback


class QuizResults(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root, fg_color="transparent")
        self.grid(row=0, column=1, padx=20, pady=2, sticky="nsew")

    def init_results(self, ed_level, subject, user_topic, quiz_data):
        if user_topic == "":
            title = ctk.CTkLabel(
                self,
                text=f"{subject} Quiz Results",
                font=Font(size=20, weight="bold"),
            )
        else:
            title = ctk.CTkLabel(
                self,
                text=f"{subject} Quiz: {user_topic} Results",
                font=Font(size=20, weight="bold"),
            )
        title.grid(row=0, column=0, columnspan=2, pady=(20, 0), sticky="we")

        subtitle = ctk.CTkLabel(self, text=f"{ed_level} level", font=Font(size=14))
        subtitle.grid(row=1, column=0, columnspan=2, sticky="we")

        self.questions_frame = ctk.CTkScrollableFrame(self, width=610, height=250, fg_color="transparent")
        self.questions_frame.grid(row=2, column=0, columnspan=2, padx=10, sticky="nsew")

        question_count = 1
        row_count = 0
        for question in quiz_data:
            self.get_question(question_count, row_count, question)
            question_count += 1
            row_count +=3

        save_button = ctk.CTkButton(self, border_width=1, border_color="#36719F", text="Save Quiz", font=Font(size=16))
        save_button.grid(row=3, column =1, padx=10, pady=10, sticky="e")

        reset_button = ctk.CTkButton(self, border_width=1, border_color="#36719F", text="Reset Quiz Generator", font=Font(size=16))
        reset_button.grid(row=3, column=0, padx=(300, 10), pady=10, sticky="e")

    def get_question(self, question_count, row_count, question):
        spacer = ctk.CTkFrame(
            self.questions_frame,
            height=2,
            fg_color="#979DA2",
        )
        spacer.grid(row=row_count+1, columnspan=2, sticky="we"
)

        question_label = ctk.CTkLabel(
            self.questions_frame,
            text=f"Question {question_count}:",
            font=Font(size=18, weight="bold"),
            wraplength=225,
            justify="left",
        )
        question_label.grid(row=row_count, column=0, padx=(0, 10), sticky="nw")

        question_text = ctk.CTkLabel(
            self.questions_frame,
            text=f"{question['text']}\n\nCorrect answer:\n{question['answer']}\n\nYour answer:\n{question['student_answer']}\n\n",
            font=Font(size=18),
            wraplength=225,
            justify="left",
        )
        question_text.grid(row=row_count+2, column=0, padx=(0, 10), sticky="nw")

        feedback_label = ctk.CTkLabel(
            self.questions_frame,
            text=f"Al's feedback:",
            font=Font(size=18, weight="bold"),
            wraplength=350,
            justify="left"
        )
        feedback_label.grid(row=row_count, column=1, padx=(5, 0), sticky="nw")

        feedback_text = ctk.CTkLabel(
            self.questions_frame,
            text=f"{self.get_feedback(question['text'], question['answer'], question['student_answer'])}\n\n",
            font=Font(size=18),
            wraplength=350,
            justify="left"
        )
        feedback_text.grid(row=row_count+2, column=1, padx=(5, 0), sticky="nw")

        question_count += 1
        row_count += 3

    def get_feedback(self, question, answer, student_answer):
        feedback = Feedback(question, answer, student_answer).generate_feedback()
        feedback = " ".join(feedback.split())
        return feedback
