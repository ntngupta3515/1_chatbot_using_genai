from client.genAI import GenAI
from constants import AI

'''
Purpose: Main Application
'''
class App:

    def __init__(self) -> None:
        self.genAi = GenAI(AI.CHAT_GPT)
        text = f"""This is a beautiful day. What is the world like?"""
        prompt = f"""Give a single word title to the text delimited by triple backticks
        ```{text}```
        """
        response = self.genAi.get_completion(prompt)
        print(response)
