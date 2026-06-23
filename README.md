# 🩺 Medical Chatbot — RAG-Powered Clinical Q&A

> An intelligent medical assistant that answers clinical queries by retrieving context from a curated medical knowledge base using **Retrieval-Augmented Generation (RAG)**.

Built with **LangChain · Groq (Llama-3.3-70B) · Pinecone · Hugging Face Embeddings · Flask**

---

## Overview

This project implements a domain-specific chatbot that grounds every response in a real medical knowledge base rather than relying solely on a language model's parametric memory. A user asks a medical question; the system retrieves the most semantically relevant passages from a PDF knowledge base, injects them into the prompt, and returns a concise, evidence-backed answer via a clean web interface.

---

## Features

| Capability | Detail |
|---|---|
| 📄 **Knowledge base** | PDF-driven, easily swappable medical corpus |
| 🔍 **Semantic search** | Dense vector retrieval via Pinecone |
| 🤖 **LLM** | Groq-hosted `llama-3.3-70b-versatile` |
| 🧠 **Embeddings** | Hugging Face sentence transformers |
| ⚡ **RAG pipeline** | Low-latency retrieval + generation loop |
| 🌐 **Web interface** | Responsive Flask + HTML/CSS/JS chat UI |
| 📦 **Modular structure** | Clean separation of ingestion, retrieval, and serving layers |

---

## Tech Stack

- **Runtime:** Python 3.10
- **Web framework:** Flask
- **Orchestration:** LangChain
- **Vector store:** Pinecone
- **LLM provider:** Groq
- **Embeddings:** Hugging Face (`sentence-transformers`)
- **PDF parsing:** PyPDF
- **Frontend:** HTML · CSS · Vanilla JS

---

## Project Structure

```
Medical-Chatbot/
├── app.py                  # Flask application entry point
├── store_index.py          # One-time vector index builder
├── setup.py
├── requirements.txt
├── .env                    # API keys (not committed)
│
├── data/
│   └── Medical_Book.pdf    # Source knowledge base
│
├── src/
│   ├── helper.py           # PDF loading, chunking, embedding helpers
│   └── prompt.py           # Prompt templates
│
├── templates/
│   └── chat.html           # Chat UI template
│
├── static/
│   ├── style.css
│   └── script.js
│
└── research/
    └── trials.ipynb        # Experimentation notebook
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/Medical-Chatbot.git
cd Medical-Chatbot
```

### 2. Create and activate a virtual environment

```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
```

> You can obtain a Pinecone API key at [pinecone.io](https://www.pinecone.io) and a Groq API key at [console.groq.com](https://console.groq.com).

### 5. Build the vector index

Place your medical PDF inside the `data/` directory, then run:

```bash
python store_index.py
```

This will:
1. Load and parse the PDF
2. Split the text into overlapping chunks
3. Generate dense embeddings via Hugging Face
4. Upsert all vectors to your Pinecone index

### 6. Launch the application

```bash
python app.py
```

Navigate to `http://localhost:8080` in your browser.

---

## RAG Pipeline

```
Medical PDF
     │
     ▼
 PyPDFLoader
     │
     ▼
 RecursiveCharacterTextSplitter
     │
     ▼
 HuggingFace Embeddings
     │
     ▼
 Pinecone Vector Store  ◄──── User Query (embedded)
     │
     ▼
 Top-K Retriever
     │
     ▼
 Groq  Llama-3.3-70B  (context + query → answer)
     │
     ▼
 Response
```

---



## License

This project is released for **educational purposes**. No medical advice is implied or should be inferred from its outputs. Always consult a qualified healthcare professional for clinical decisions.

---

## Author

**Jayash**


---

> ⭐ If you find this project useful, consider giving it a star — it helps others discover it!
