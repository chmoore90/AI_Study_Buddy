import customtkinter as ctk
from customtkinter import CTkFont as Font

class LoadingFrame(ctk.CTkFrame):
    def __init__(self, root, state):
        super().__init__(root, fg_color="transparent")
        self.grid(row=0, column=1, padx=20, pady=2, sticky="nsew")

        self.init_loading_frame(state)

    def init_loading_frame(self, state):
        if state == "generating quiz":
            title = ctk.CTkLabel(self, text="Please be patient while we generate your quiz.", font=Font(size=18))
            title.grid(padx=120, pady=(170, 0), sticky="nswe")
