class Context:
    def __init__(self, ai) -> None:
        self.context = [] # Collects the context for the AI
        self.lastResponse = ''
        self.ai = ai

    def add(self, prompt):
        self.context.append({'role':'user', 'content':f"{prompt}"})
        response = self.ai.runMessages(self.context) 
        self.context.append({'role':'assistant', 'content':f"{response}"})
        self.lastResponse = response
        return self.context

    def getLastResponse(self):
        return self.lastResponse