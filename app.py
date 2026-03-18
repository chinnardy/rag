from fastapi import FastAPI
from pydantic import BaseModel

from agents.router_agent import RouterAgent
from agents.retrieval_agent import RetrievalAgent
from agents.response_agent import ResponseAgent

app = FastAPI()

documents = [
    "Reset password via settings page.",
    "Supports AWS, Azure, GCP.",
    "API integration via REST.",
]

router = RouterAgent()
retriever = RetrievalAgent(documents)
responder = ResponseAgent()


class Query(BaseModel):
    question: str


@app.post("/chat")
def chat(query: Query):
    route = router.route(query.question)

    if route == "rag":
        answer = retriever.execute(query.question)
    else:
        answer = responder.generate(query.question)

    return {
        "route": route,
        "answer": answer
    }