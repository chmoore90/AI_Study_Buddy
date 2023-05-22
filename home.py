import customtkinter as ctk
from customtkinter import CTkFont as Font
from PIL import Image


class Home(ctk.CTkFrame):
    def __init__(self, root, ask_frame, quiz_gen_frame):
        super().__init__(root)
        self.ask_frame = ask_frame
        self.quiz_gen_frame = quiz_gen_frame
        self.home = ctk.CTkFrame(root, fg_color="transparent")
        self.home.grid(row=0, column=0)

        al_img = ctk.CTkImage(Image.open("Al.png").transpose(0), size=(225, 225))
        al_img_label = ctk.CTkLabel(self.home, text=None, image=al_img)
        al_img_label.grid(row=0, column=0, rowspan=3, padx=30, pady=15)

        title = ctk.CTkLabel(
            self.home,
            text="Hello learner! My name is Al.",
            font=Font(size=24, weight="bold"),
            justify="center",
        )
        title.grid(row=0, column=1, padx=30, pady=20, sticky="s")

        intro_text = """\
I'm here to help you study and learn.\n\n\
Ask Al:  Ask me anything. I can answer all your questions.\n\
Quiz Generator:  Ready to test yourself? I make customized quizzes.\n\
Saved Quizzes:  Revisit your saved quizzes.\n\n\
What would you like to do?
"""
        intro = ctk.CTkLabel(
            self.home,
            text=intro_text,
            font=Font(size=18),
            wraplength=550,
            justify="left",
        )
        intro.grid(row=1, column=1, padx=30, pady=10, sticky="nwe")

        button_frame = ctk.CTkFrame(self.home, fg_color="transparent")
        button_frame.grid(row=2, column=1, padx=15)

        self.go_ask_button = ctk.CTkButton(
            button_frame,
            text="Ask Al",
            font=Font(size=18),
            width=175,
            height=35,
            command=lambda: self.raise_frame(root, self.ask_frame),
        )
        self.go_ask_button.grid(row=0, column=0, padx=15, pady=5)

        self.go_quiz_button = ctk.CTkButton(
            button_frame,
            text="Quiz Generator",
            font=Font(size=18),
            width=175,
            height=35,
            command=lambda: self.raise_frame(root, self.quiz_gen_frame),
        )
        self.go_quiz_button.grid(row=0, column=1, padx=15, pady=5)

        self.go_history_button = ctk.CTkButton(
            button_frame, text="Saved Quizzes", font=Font(size=18), width=175, height=35
        )
        self.go_history_button.grid(row=0, column=2, padx=15, pady=5)

    def raise_frame(self, root, frame):
        if frame == self.ask_frame:
            root.title("Al the Study Buddy - Ask Al")
            self.go_ask_button.configure(
                fg_color="#36719F", font=Font(size=20, weight="bold")
            )
            self.go_quiz_button.configure(
                fg_color="#3B8ED0", font=Font(size=18, weight="normal")
            )
        elif frame == self.quiz_gen_frame:
            root.title("Al the Study Buddy - Quiz")
            self.go_ask_button.configure(
                fg_color="#3B8ED0", font=Font(size=18, weight="normal")
            )
            self.go_quiz_button.configure(
                fg_color="#36719F", font=Font(size=20, weight="bold")
            )
            frame.prequiz_frame.tkraise()
        else:
            root.title("Al the Study Buddy")
            self.go_ask_button.configure(
                fg_color="#3B8ED0", font=Font(size=18, weight="normal")
            )
            self.go_quiz_button.configure(
                fg_color="#3B8ED0", font=Font(size=18, weight="normal")
            )
        frame.tkraise()
