import os
from app.rag.embeddings import get_embedding
from app.rag.vector_store import FAISSVectorStore
from pypdf import PdfReader

CHUNKS_DIR = "data/chunks"
os.makedirs(CHUNKS_DIR, exist_ok=True)

def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks

vector_store = FAISSVectorStore(dimension=1536)  # text-embedding-3-small

def ingest_document(file_path):
    text = extract_text(file_path)

    chunks = chunk_text(text)

    embeddings = []
    for chunk in chunks:
        embeddings.append(get_embedding(chunk))

    vector_store.add(embeddings, chunks)
    vector_store.save()

    return {"status": "ingested", "chunks": len(chunks)}

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()