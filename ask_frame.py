import customtkinter as ctk
from customtkinter import CTkFont as Font

class AskFrame(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root, border_width=2)
        self.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")

        title = ctk.CTkLabel(self, text="heya")
        title.grid(row=0, column=0)
