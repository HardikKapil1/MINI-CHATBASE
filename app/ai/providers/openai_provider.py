from app.ai.providers.base_provider import AIProvider


class OpenAIProvider(AIProvider):
    def chat(self, message: str):

        return f"OpenAI says: {message}"
