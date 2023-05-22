import customtkinter as ctk
from customtkinter import CTkFont as Font
from tkinter import messagebox
import json

import quiz_frame
from ai_classes import Quizinator


subject_list = [
    "History",
    "Math",
    "Science",
    "Literature",
    "Philosophy",
    "Other",
]
ed_level_list = [
    "Elementary school",
    "Middle school",
    "Secondary school",
    "College/University",
]


class QuizGenerator(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root, border_width=2)
        self.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")

        self.settings_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.settings_frame.grid(row=0, column=0, padx=2, pady=2, sticky="ns")

        self.prequiz_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.prequiz_frame.grid(row=0, column=1, padx=2, pady=2, sticky="nswe")

        self.init_settings()
        self.init_prequiz()

    def init_settings(self):
        inner_border = ctk.CTkLabel(self.settings_frame, text=" ", font=Font(size=6), bg_color="grey70")
        inner_border.grid(row=0, column=1, rowspan=10, sticky="ns")

        title = ctk.CTkLabel(
            self.settings_frame, text="Quiz Settings", font=Font(size=20, weight="bold")
        )
        title.grid(row=0, column=0, padx=10, pady=20, sticky="nwe")

        self.subject_dropdown = ctk.CTkOptionMenu(
            self.settings_frame,
            width=200,
            font=Font(size=14),
            values=subject_list,
            variable=ctk.StringVar(),
            state="normal",
            command=lambda v: self.check_subject_value(),
        )
        self.subject_dropdown.set("Choose a subject:")
        self.subject_dropdown.grid(row=2, column=0, padx=10)

        self.other_subject = ctk.CTkEntry(
            self.settings_frame,
            width=200,
            placeholder_text="Enter a subject here:",
            state="normal",
            text_color="grey20",
            font=Font(size=14),
        )

        self.ed_level_dropdown = ctk.CTkOptionMenu(
            self.settings_frame,
            width=200,
            font=Font(size=14),
            values=ed_level_list,
            variable=ctk.StringVar(),
            state="normal",
        )
        self.ed_level_dropdown.set("Choose a study level:")
        self.ed_level_dropdown.grid(row=1, column=0, padx=10, pady=(10, 20))

        user_topic_label = ctk.CTkLabel(
            self.settings_frame, text="Topic:", font=Font(size=14), text_color="grey20"
        )
        user_topic_label.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")

        self.user_topic_entry = ctk.CTkEntry(
            self.settings_frame,
            width=200,
            placeholder_text="Enter a topic here (optional)",
            state="normal",
            text_color="grey20",
            font=Font(size=14),
        )
        self.user_topic_entry.grid(row=5, column=0, padx=10)

        self.gen_quiz_button = ctk.CTkButton(
            self.settings_frame,
            border_width=1,
            border_color="#36719F",
            width=200,
            height=50,
            font=Font(size=20, weight="bold"),
            text="Generate My Quiz",
            state="normal",
            command=self.validate_quiz,
        )
        self.gen_quiz_button.grid(row=6, column=0, padx=10, pady=(50, 85))

    def init_prequiz(self):
        prequiz_text = ctk.CTkLabel(
            self.prequiz_frame,
            font=Font(size=18),
            text="Your quiz will show up here once it has been generated.",
        )
        prequiz_text.grid(
            row=0, column=0, columnspan=2, padx=130, pady=(170, 0), sticky="nswe"
        )

        prequiz_text2 = ctk.CTkLabel(
            self.prequiz_frame,
            font=Font(size=18),
            text="Did you want to open a saved quiz? Click here: ",
        )
        prequiz_text2.grid(row=1, column=0, pady=(10, 170), sticky="nse")

        button_to_saves = ctk.CTkButton(
            self.prequiz_frame, font=Font(size=16), text="Saved Quizzes"
        )
        button_to_saves.grid(row=1, column=1, padx=10, pady=(10, 170), sticky="w")

    def check_subject_value(self):
        if self.subject_dropdown.get() == "Other":
            self.other_subject.grid(row=3, column=0, padx=10)
        else:
            self.other_subject.grid_forget()

    def validate_quiz(self):
        subject = self.subject_dropdown.get()
        ed_level = self.ed_level_dropdown.get()

        if ed_level not in ed_level_list:
            error_box = messagebox.showwarning(
                title="Quiz Settings Error",
                message="Al needs a study level to generate a quiz. Choose one from the dropdown menu.",
            )
            error_box
        elif subject not in subject_list:
            error_box = messagebox.showwarning(
                title="Quiz Settings Error",
                message='Al needs a subject to generate a quiz. Choose one from the dropdown menu or choose "Other" and enter a custom one',
            )
            error_box

        elif subject == "Other" and self.other_subject.get() == "":
            error_box = messagebox.showwarning(
                title="Quiz Settings Error",
                message="Please enter a subject or choose one from the dropdown menu",
            )
            error_box

        else:
            self.gen_quiz_button.configure(state="disabled")
            self.ed_level_dropdown.configure(state="disabled")
            self.subject_dropdown.configure(state="disabled")
            self.other_subject.configure(state="readonly", text_color="grey")
            self.user_topic_entry.configure(state="readonly", text_color="grey")

            self.generate_quiz(subject, ed_level)

    def generate_quiz(self, subject, ed_level):
        if subject == "Other":
            subject = self.other_subject.get()
        user_topic = self.user_topic_entry.get()

        al_response = Quizinator(subject, ed_level, user_topic).generate_quiz()
        al_response = " ".join(al_response.split())
        start = al_response.find("[")
        end = al_response.rfind("]")
        al_response = al_response[start : end + 1]

        quiz_data = json.loads(al_response)
        quiz = quiz_frame.Quiz(self)

        print(quiz_data)

        quiz.init_quiz(subject, ed_level, user_topic, quiz_data)
