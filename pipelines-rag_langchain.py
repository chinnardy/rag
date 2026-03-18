from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.schema import Document

class LangchainRAG:
    def __init__(self, documents):
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = self._init_store(documents)
        self.llm = ChatOpenAI(temperature=0.2)

    def _init_store(self, documents):
        docs = [Document(page_content=d) for d in documents]
        return FAISS.from_documents(docs, self.embeddings)

    def run(self, query: str):
        docs = self.vector_store.similarity_search(query, k=4)
        context = "\n".join([d.page_content for d in docs])

        prompt = f"""
        Answer strictly from context.
        Context: {context}
        Question: {query}
        """

        return self.llm.predict(prompt)