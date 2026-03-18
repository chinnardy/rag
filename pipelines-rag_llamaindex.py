from llama_index.core import VectorStoreIndex, Document

class LlamaIndexRAG:
    def __init__(self, documents):
        docs = [Document(text=d) for d in documents]
        self.index = VectorStoreIndex.from_documents(docs)

    def query(self, query: str):
        engine = self.index.as_query_engine()
        return engine.query(query).response