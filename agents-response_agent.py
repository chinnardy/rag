from openai import OpenAI
from config import MODEL_NAME

client = OpenAI()

class ResponseAgent:
    """
    Handles non-RAG general queries
    """

    def generate(self, query: str):
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": query}
            ],
            temperature=0.5
        )

        return response.choices[0].message.content