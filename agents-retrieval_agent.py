from pipelines.rag_langchain import LangchainRAG

class RetrievalAgent:
    def __init__(self, documents):
        self.rag = LangchainRAG(documents)

    def execute(self, query: str):
        return self.rag.run(query)