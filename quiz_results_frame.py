import customtkinter as ctk
from customtkinter import CTkFont as Font

class QuizResults(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root, fg_color="transparent")
        self.grid(row=0, column=1, padx=20, pady=2, sticky="nsew")

        title = ctk.CTkLabel(self, text="results page")
        title.grid()
