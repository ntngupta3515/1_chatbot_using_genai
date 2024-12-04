from openai import OpenAI
from anthropic import Anthropic
from constants import OPENAI_API_KEY_ENV, CLAUDE_API_KEY_ENV, AI
import os

class GenAI:

    def __init__(self, ai) -> None:
        self.ai = ai
        match ai:
            case AI.CLAUDE:
                # TODO: This is not fully supported yet
                self.client = Anthropic(api_key=os.getenv(CLAUDE_API_KEY_ENV)).messages
            case AI.CHAT_GPT:
                self.client = OpenAI(api_key=os.getenv(OPENAI_API_KEY_ENV)).chat.completions
            case _:
                raise Exception(f"Unsupported AI: {ai}")

    def runPrompt(self, prompt):
        messages = [{
            "role": "user", 
            "content": prompt
        }]
        response = self.client.create(
            model=self.ai.value,
            messages=messages,
            temperature=0, # this is the degree of randomness of the model's output
        )
        return response.choices[0].message.content

    def runMessages(self, messages):
        response = self.client.create(
            model=self.ai.value,
            messages=messages,
            temperature=0, # this is the degree of randomness of the model's output
        )
        return response.choices[0].message.content