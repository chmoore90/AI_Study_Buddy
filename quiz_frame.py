import customtkinter as ctk
from customtkinter import CTkFont as Font
from tkinter import messagebox
from textwrap import wrap

import quiz_results_frame


class Quiz(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root, fg_color="transparent")
        self.root = root
        self.grid(row=0, column=1, padx=20, pady=2, sticky="nsew")
        self.grid_propagate(False)

    def init_quiz(self, subject, ed_level, user_topic, quiz_data):
        self.quiz_data = quiz_data
        self.ed_level = ed_level
        self.subject = subject.title()
        self.user_topic = user_topic.title()

        if user_topic == "":
            title = ctk.CTkLabel(
                self,
                text=f"{self.subject} Quiz",
                font=Font(size=20, weight="bold"),
            )
        else:
            title = ctk.CTkLabel(
                self,
                text=f"{self.subject} Quiz: {self.user_topic}",
                font=Font(size=20, weight="bold"),
            )
        title.grid(pady=(20, 0), sticky="we")

        subtitle = ctk.CTkLabel(self, text=f"{self.ed_level} level", font=Font(size=14))
        subtitle.grid(sticky="we")

        self.question_frame = ctk.CTkScrollableFrame(self, width=610, height=250, fg_color="transparent")
        self.question_frame.grid(sticky="nswe")

        self.display_question(0)

    def display_question(self, count):
        radio_var = ctk.StringVar()
        self.question_label = ctk.CTkLabel(
            self.question_frame,
            text=f'Question {count+1}:\n{self.quiz_data[count]["text"]}',
            font=Font(size=18),
            wraplength=600,
            justify="left",
        )
        self.question_label.grid(pady=10, sticky="w")

        self.radio_a = ctk.CTkRadioButton(
            self.question_frame,
            font=Font(size=16),
            text=self.wrap_text(self.quiz_data[count]["choices"][0]),
            value=self.quiz_data[count]["choices"][0],
            variable=radio_var,
        )
        self.radio_b = ctk.CTkRadioButton(
            self.question_frame,
            font=Font(size=16),
            text=self.wrap_text(self.quiz_data[count]["choices"][1]),
            value=self.quiz_data[count]["choices"][1],
            variable=radio_var,
        )
        self.radio_c = ctk.CTkRadioButton(
            self.question_frame,
            font=Font(size=16),
            text=self.wrap_text(self.quiz_data[count]["choices"][2]),
            value=self.quiz_data[count]["choices"][2],
            variable=radio_var,
        )
        self.radio_d = ctk.CTkRadioButton(
            self.question_frame,
            font=Font(size=16),
            text=self.wrap_text(self.quiz_data[count]["choices"][3]),
            value=self.quiz_data[count]["choices"][3],
            variable=radio_var,
        )
        self.radio_a.grid(padx=50, pady=10, sticky="w")
        self.radio_b.grid(padx=50, pady=10, sticky="w")
        self.radio_c.grid(padx=50, pady=10, sticky="w")
        self.radio_d.grid(padx=50, pady=10, sticky="w")

        self.submit_button = ctk.CTkButton(
            self,
            border_width=1,
            border_color="#36719F",
            text="Submit",
            font=Font(size=16, weight="bold"),
            command=lambda: self.submit_answer(radio_var.get(), count),
        )
        self.submit_button.grid(padx=10, pady=10, sticky="e")

    def wrap_text(self, text):
        wrapped = "\n".join(wrap(text, 65))
        return wrapped

    def submit_answer(self, student_answer, count):
        if student_answer == "":
            error_box = messagebox.showwarning(
                "Input needed",
                "You haven't selected an answer. If you don't know the answer, make an educated guess.",
            )
            error_box
        else:
            self.quiz_data[count]["student_answer"] = student_answer
            count += 1
            self.question_label.destroy()
            self.radio_a.destroy()
            self.radio_b.destroy()
            self.radio_c.destroy()
            self.radio_d.destroy()
            self.submit_button.destroy()

            if count < len(self.quiz_data):
                self.display_question(count)
            else:
                results = quiz_results_frame.QuizResults(self.root)
                results.tkraise()
                results.init_results(self.ed_level, self.subject, self.user_topic, self.quiz_data)

                self.destroy()
