from fastapi import FastAPI
from pydantic import BaseModel
from rag import answer_query

app = FastAPI(title="RAG-Based AI Assistant")

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query: Query):
    return {"answer": answer_query(query.question)}