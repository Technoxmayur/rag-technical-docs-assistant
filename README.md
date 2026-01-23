# 🤖 RAG-Based AI Assistant for Technical Documentation  
### Retrieval-Augmented Generation (RAG) System using NLP & Vector Search

This project implements a **Retrieval-Augmented Generation (RAG) based AI assistant** designed to answer technical queries from documentation using **semantic search and NLP**.

It combines **vector embeddings, similarity search, and an API-based backend**, making it suitable for **AI/ML portfolios, internships, and academic evaluations**.

---

## 🎯 Project Objective

- Build an AI assistant that answers queries from technical documents  
- Use **RAG architecture** for accurate, context-aware responses  
- Apply NLP preprocessing and vector databases  
- Expose the system via a scalable REST API  

---

## ✨ Key Features

- 📚 Retrieval-Augmented Generation (RAG) architecture  
- 🧠 Semantic document understanding  
- 🔍 Fast similarity search using FAISS  
- 🧾 NLP preprocessing using spaCy & NLTK  
- ⚡ High-performance backend using FastAPI  
- 📡 Interactive API documentation via Swagger UI  

---

## 🛠️ Technology Stack

### Core AI & NLP
- **Python**
- **Sentence Transformers** – Text embeddings
- **spaCy** – Tokenization & linguistic processing
- **NLTK** – Text normalization

### Vector Search
- **FAISS** – Efficient similarity search

### Backend & API
- **FastAPI**
- **Uvicorn**

---

## 🧠 System Architecture (High Level)

1. Technical documents are preprocessed using NLP  
2. Text chunks are converted into embeddings  
3. Embeddings are stored in FAISS vector index  
4. User queries are embedded and matched semantically  
5. Most relevant document context is retrieved  
6. Context-aware answer is generated  

---

## 📦 Installation & Setup (VS Code)

### Step 1: Extract Project
```bash
unzip RAG_AI_Assistant.zip
cd RAG_AI_Assistant
Step 2: Create Virtual Environment
python -m venv venv

Step 3: Activate Environment
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

Step 4: Install Dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

▶️ Run the Application
uvicorn main:app --reload

🌐 Access API Documentation

Open in browser:

http://127.0.0.1:8000/docs


This opens Swagger UI for interactive testing.

🔗 API Usage
POST /ask

Input: User query related to documentation

Output: Context-aware AI-generated response

Use cases:

Technical documentation assistants

Internal knowledge bases

Developer support tools

🧪 Limitations

Depends on quality and size of documentation

Basic RAG pipeline (can be extended with LLM APIs)

No user authentication currently

🚀 Future Enhancements

 Integration with LLMs (OpenAI / Watsonx / LLaMA)

 Support for PDF & DOCX ingestion

 Chunk ranking optimization

 UI frontend (Streamlit / React)

 Cloud deployment (IBM Cloud)

🎓 Academic & Career Relevance

Demonstrates RAG architecture & vector databases

Strong example of NLP + backend integration

Ideal project for AI / ML Engineer roles

Suitable for IBM, internship & placement evaluations

👤 Author

Mayur Holkar
AI / ML Engineer Aspirant

📄 License

This project is licensed under the MIT License.

Built with ❤️ using NLP & Retrieval-Augmented Generation
