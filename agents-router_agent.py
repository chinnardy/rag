from typing import Literal

class RouterAgent:
    """
    Decides how to route the query:
    - retrieval (RAG)
    - general LLM
    """

    def route(self, query: str) -> Literal["rag", "llm"]:
        keywords = ["how", "what", "guide", "steps", "reset", "error"]

        if any(k in query.lower() for k in keywords):
            return "rag"
        return "llm"