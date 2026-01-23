# RAG-Based AI Assistant for Technical Documentation

## Features
- Retrieval-Augmented Generation (RAG)
- spaCy + NLTK preprocessing
- Sentence Transformers embeddings
- FAISS vector search
- FastAPI backend

## How to Run (VS Code)

### 1. Extract ZIP
```bash
unzip RAG_AI_Assistant.zip
cd RAG_AI_Assistant
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Run Server
```bash
uvicorn main:app --reload
```

### 5. Test API
Open browser:
http://127.0.0.1:8000/docs

Use POST /ask