from enum import Enum

OPENAI_API_KEY_ENV = "OPENAI_API_KEY"
CLAUDE_API_KEY_ENV = "CLAUDE_API_KEY"

class AI(Enum):
    CHAT_GPT = "gpt-3.5-turbo"
    CLAUDE = "claude-3-opus-20240229"
