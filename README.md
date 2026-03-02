# 🧠 AI Document Question Answering System (RAG)

A **local, privacy-first AI system** that allows users to upload PDF documents and ask questions grounded strictly in the document content using **Retrieval-Augmented Generation (RAG)**.

This project was built to deeply understand how **modern AI document assistants work internally**, not just to consume APIs.

---

## 🚀 What This Project Does

- Upload any **PDF document**
- Automatically:
  - Extract text from the PDF
  - Split it into overlapping chunks
  - Convert chunks into vector embeddings
  - Store embeddings in a **FAISS vector database**
- Ask natural language questions
- Receive **accurate, context-grounded answers**
- Runs **fully locally** using lightweight LLMs via **Ollama**
- Uses **document-level caching** to avoid repeated computation

---

## 🧠 Why This Project Matters

This is **not just a chatbot**.

It is a **real Retrieval-Augmented Generation (RAG) system**, the same architecture used in:

- Enterprise document search
- Internal AI knowledge assistants
- AI copilots
- Research and legal document analysis tools

The project demonstrates:
- Understanding of **LLM limitations**
- How to **augment models with external knowledge**
- Efficient **vector search using FAISS**
- Performance optimization using **caching**
- Clean and modular system design

---

## 🏗️ Architecture Overview

PDF Upload
↓
PDF Loader
↓
Text Chunking (with overlap)
↓
Embedding Generation
↓
FAISS Vector Store (Similarity Search)
↓
Relevant Context Retrieval
↓
Prompt Construction
↓
Local LLM (Ollama)
↓
Final Answer (Grounded in Document)

---

## 📁 Project Structure

ai-doc-assistant/
│
├── app/
│ ├── pdf_loader.py # Extracts text from PDFs
│ ├── chunking.py # Splits text into overlapping chunks
│ ├── embeddings.py # Generates vector embeddings
│ ├── vector_store.py # FAISS indexing and retrieval
│ ├── llm.py # Local LLM interface (Ollama)
│ ├── evaluation.py # Optional answer evaluation
│ └── rag.py # Orchestrates the RAG pipeline
│
├── data/
│ ├── docs/ # Uploaded PDFs
│ └── cache/ # Cached FAISS indexes
│
├── ui.py # Streamlit UI
├── main.py # CLI testing entry point
├── README.md
└── requirements.txt

---

## 🧩 Key Design Decisions

### ✅ Chunking with Overlap
- Prevents loss of context
- Avoids broken sentences
- Improves embedding quality

### ✅ FAISS Vector Database
- Extremely fast similarity search
- Scales well to large documents
- Industry-standard vector search library

### ✅ Document-Based Caching
- Uses a hash of the PDF file
- Prevents re-chunking and re-embedding
- Makes repeated queries near-instant

### ✅ Local LLM Inference
- No API costs
- No data leakage
- Works offline
- Memory-aware model selection

### ✅ Grounded Answers Only
- If the answer is **not in the document**, the model responds:
  > "I don’t know"
- Prevents hallucinations

---

## 🖥️ User Interface

Built using **Streamlit**:
- PDF upload interface
- Question input field
- Answer display
- Expandable retrieved context section
- Optional evaluation/debug output

The UI is intentionally minimal and functional.

---

## ⚙️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt

terminal 1-
.\venv\Scripts\Activate
.\venv\Scripts\Activate.ps1
python api_bridge.py --no-reload[D  (or) python api_server.py
deactivate(when done)

terminal 2-
deactivate
cd app
npm run dev(click the link that opens here)
