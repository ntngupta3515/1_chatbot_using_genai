from client.genAI import GenAI
from prompt.context import Context
from app.gui import GUI
from constants import AI

'''
Purpose: Main Application
'''
class App:

    def __init__(self) -> None:

        # Get GenAI client
        self.genAi = GenAI(AI.CHAT_GPT)

        # Get the context builder
        self.contextBuilder = Context(self.genAi)

        # Generate a UI
        self.gui = GUI(self.contextBuilder)
