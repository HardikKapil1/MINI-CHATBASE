from app.ai.providers.base_provider import AIProvider


class GeminiProvider(AIProvider):
    def chat(self, message: str):

        return f"Gemini says: {message}"
