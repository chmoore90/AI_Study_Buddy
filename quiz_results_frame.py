import customtkinter as ctk
from customtkinter import CTkFont as Font


class QuizResults(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root, fg_color="transparent")
        self.grid(row=0, column=1, padx=2, pady=2, sticky="nsew")

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
        title.grid(row=0, padx=280 - len(title._text), pady=(20, 0), sticky="nswe")

        subtitle = ctk.CTkLabel(self, text=f"{ed_level} level", font=Font(size=14))
        subtitle.grid(row=1)
