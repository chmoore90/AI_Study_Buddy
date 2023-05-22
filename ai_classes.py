import os
import openai
from textwrap import dedent

openai.api_key = os.getenv("OPEN_API_KEY")


class Quizinator:
    def __init__(self, subject, ed_level, user_topic):
        self.subject = subject
        self.study_level = ed_level
        self.user_topic = user_topic

        quiz_prompt = dedent(
            f"""\
            Create a {subject} quiz focusing on {user_topic} for a {ed_level} student.
            Make the quiz 5 questions long, with four options each.
            Make the quiz in JSON format, as a list of dictionaries, where one dictionary represents one question in the quiz.
            Put the dictionaries into the following format:
            {{
                "text": "text for the question goes here",
                "answer": "text for the correct answer goes here",
                "choices": [
                    "text for option A",
                    "text for option B",
                    "text for option C",
                    "text for option D",
                    ]
            }}
            Enclose the list in 3 backticks (```).
            Include the correct answer in the list of choices.
            """
        )

        self.system_prompt = (
            "You create multiple choices quizzes to help students test their knowledge."
        )
        self.user_prompt = quiz_prompt
        self.messages = [
            {"role": "system", "content": self.system_prompt},
        ]

    def generate_quiz(self):
        message = {"role": "user", "content": self.user_prompt}
        self.messages.append(message)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages, temperature=0.8
        )
        self.messages.append(response["choices"][0]["message"]["content"])

        return response["choices"][0]["message"]["content"]

    def clear(self):
        self.messages.clear()
        self.messages = [
            {"role": "system", "content": self.system_prompt},
        ]


class KnowItAll:
    def __init__(self, user_question):
        self.system_prompt = "You are a teacher and provide students with clear, concise answers to their questions."
        self.user_prompt = f"This is my question: {user_question}"
        self.messages = [
            {"role": "system", "content": self.system_prompt},
        ]

    def complete(self):
        message = {"role": "user", "content": self.user_prompt}
        self.messages.append(message)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages, temperature=0.8
        )
        self.messages.append(response["choices"][0]["message"]["content"])

        return response["choices"][0]["message"]["content"]

    def clear(self):
        self.messages.clear()
        self.messages = [
            {"role": "system", "content": self.system_prompt},
        ]
