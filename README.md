🚀 AI Knowledge Retrieval System (Enterprise RAG with Azure OpenAI + FAISS)
📌 Overview

This project is a production-style Retrieval-Augmented Generation (RAG) system built using Azure OpenAI, FAISS, and FastAPI.

It enables users to upload PDF documents, perform semantic search using vector embeddings, and receive context-grounded AI-generated responses streamed in real time.

🏗 Architecture

Flow:

PDF Upload

Text Extraction (pypdf)

Text Chunking

Embedding Generation (Azure OpenAI)

FAISS Vector Indexing (Cosine Similarity)

Query Embedding

Top-K Retrieval

Context Injection into LLM

Token-Level Streaming Response (SSE)

🧠 Key Features

✅ PDF ingestion pipeline

✅ Azure OpenAI integration

✅ FAISS vector database

✅ Cosine similarity search

✅ Context-grounded prompt design

✅ Hallucination mitigation

✅ Persistent vector storage

✅ Token-level streaming (Server-Sent Events)

✅ FastAPI backend (async-ready)

🛠 Tech Stack

Backend: FastAPI

LLM: Azure OpenAI (gpt-4o-mini)

Embeddings: text-embedding-3-small

Vector Store: FAISS (IndexFlatIP)

PDF Processing: pypdf

Streaming: SSE via StreamingResponse

📂 Project Structure
ai-knowledge-os/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── rag/
│   │   ├── ingestion.py
│   │   ├── retrieval.py
│   │   ├── vector_store.py
│   │   └── embeddings.py
│
├── data/
├── faiss_index.index
├── faiss_metadata.pkl
├── requirements.txt
└── .env
⚙️ Setup Instructions
1️⃣ Clone Repository
git clone <repo-url>
cd ai-knowledge-os
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure Environment Variables

Create .env file:

OPENAI_API_KEY=your_key
AZURE_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_API_VERSION=2024-02-01
▶️ Run Server
uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000/docs
📤 Upload Document

Use /upload endpoint to upload PDF.

🔍 Query Document

Use /query-stream endpoint to send queries.

Streaming responses are delivered via Server-Sent Events (SSE).

🧪 Example Queries

Who is the Chairperson?

List all professors.

Who is associated with NCERT?

🛡 Hallucination Control Strategy

Strict context-grounded prompting

Temperature set to 0

Retrieval-based answer generation

Cosine similarity filtering

🚀 Future Improvements

Hybrid Retrieval (BM25 + FAISS)

Similarity threshold guard

Citation tagging

Multi-agent orchestration

Evaluation dashboard

Azure deployment

📈 Resume Description

Designed and implemented an enterprise-grade RAG system integrating Azure OpenAI with a custom FAISS vector store. Built a PDF ingestion pipeline, cosine similarity retrieval, and streaming FastAPI backend with hallucination-resistant prompting.
