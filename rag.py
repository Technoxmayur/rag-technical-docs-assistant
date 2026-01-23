import faiss
import spacy
import nltk
from sentence_transformers import SentenceTransformer
import numpy as np

nlp = spacy.load("en_core_web_sm")
nltk.download("punkt")

documents = [
    "FastAPI is a modern Python web framework for building APIs.",
    "RAG combines retrieval with language generation.",
    "spaCy is used for NLP tasks like tokenization and NER.",
    "Embeddings convert text into numerical vectors."
]

model = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = model.encode(documents)
index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(np.array(doc_embeddings))

def answer_query(question: str):
    q_embedding = model.encode([question])
    D, I = index.search(np.array(q_embedding), k=1)
    return documents[I[0][0]]