import customtkinter as ctk

from home import Home
from ask_frame import AskFrame
from quiz_gen_frame import QuizGenerator


root = ctk.CTk()
root.title("Al the Study Buddy")
root.minsize(height=700, width=800)
root.grid_anchor("n")
blank_frame = ctk.CTkFrame(root, border_width=2)
blank_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")
blank_frame.grid_propagate(False)

ask_frame = AskFrame(root)
quiz_gen_frame = QuizGenerator(root)
home = Home(root, ask_frame, quiz_gen_frame)

quiz_gen_frame.prequiz_frame.tkraise()
blank_frame.tkraise()

root.mainloop()
