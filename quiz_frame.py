import customtkinter as ctk
from customtkinter import CTkFont as Font
from tkinter import messagebox
from textwrap import wrap

import quiz_results_frame


class Quiz(ctk.CTkScrollableFrame):
    def __init__(self, root):
        super().__init__(root, fg_color="transparent")
        self.root = root
        self.grid(row=0, column=1, padx=20, pady=2, sticky="nsew")

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
                bg_color="white"
            )
        title.grid(row=0, pady=(20, 0), sticky="we")

        subtitle = ctk.CTkLabel(self, text=f"{self.ed_level} level", font=Font(size=14))
        subtitle.grid(row=1, sticky="we")

        self.display_question(0)

    def display_question(self, count):
        radio_var = ctk.StringVar()
        self.question_label = ctk.CTkLabel(
            self,
            text=f'Question {count+1}:\n{self.quiz_data[count]["text"]}',
            font=Font(size=18),
            wraplength=500,
            justify="left",
        )
        if len(self.question_label._text) < 180:
            self.question_label.grid(row=2, padx=(10, 200-len(self.question_label._text)), pady=10, sticky="we")
        else:
            self.question_label.grid(row=2, padx=10, pady=10, sticky="we")


        self.radio_a = ctk.CTkRadioButton(
            self,
            font=Font(size=16),
            text=self.wrap_text(self.quiz_data[count]["choices"][0]),
            value=self.quiz_data[count]["choices"][0],
            variable=radio_var,
        )
        self.radio_b = ctk.CTkRadioButton(
            self,
            font=Font(size=16),
            text=self.wrap_text(self.quiz_data[count]["choices"][1]),
            value=self.quiz_data[count]["choices"][1],
            variable=radio_var,
        )
        self.radio_c = ctk.CTkRadioButton(
            self,
            font=Font(size=16),
            text=self.wrap_text(self.quiz_data[count]["choices"][2]),
            value=self.quiz_data[count]["choices"][2],
            variable=radio_var,
        )
        self.radio_d = ctk.CTkRadioButton(
            self,
            font=Font(size=16),
            text=self.wrap_text(self.quiz_data[count]["choices"][3]),
            value=self.quiz_data[count]["choices"][3],
            variable=radio_var,
        )
        self.radio_a.grid(row=3, padx=50, pady=10, sticky="w")
        self.radio_b.grid(row=4, padx=50, pady=10, sticky="w")
        self.radio_c.grid(row=5, padx=50, pady=10, sticky="w")
        self.radio_d.grid(row=6, padx=50, pady=10, sticky="w")

        submit_button = ctk.CTkButton(
            self,
            border_width=1,
            border_color="#36719F",
            text="Submit",
            font=Font(size=16, weight="bold"),
            command=lambda: self.submit_answer(radio_var.get(), count),
        )
        submit_button.grid(row=7, padx=(0, 20), pady=(30, 10), sticky="e")

    def wrap_text(self, text):
        wrapped = "\n".join(wrap(text, 60))
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

            if count < len(self.quiz_data):
                self.display_question(count)
            else:
                results = quiz_results_frame.QuizResults(self.root)
                results.tkraise()
                results.init_results(self.ed_level, self.subject, self.user_topic, self.quiz_data)

                self.destroy()
