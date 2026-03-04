import chromadb
from openai import AzureOpenAI
from app.config import settings
from fastapi.responses import StreamingResponse
from app.rag.vector_store import FAISSVectorStore
from app.rag.embeddings import get_embedding

client=AzureOpenAI(
        api_key=settings.AZURE_OPENAI_KEY,
        api_version=settings.AZURE_OPENAI_VERSION,
        azure_endpoint=settings.AZURE_OPENAI_ENDPOINT
    )

vector_store = FAISSVectorStore(dimension=1536)

def retrieve_context(query: str, k: int = 5):
    query_embedding = get_embedding(query)
    results = vector_store.search(query_embedding, k)
    return results

def stream_answer(query: str, contexts: list[str]):

    context_text = "\n\n".join(contexts)

    prompt = f"""
        You are an enterprise AI assistant.
        Answer strictly based on the provided context.
        If answer is not in context, say you don't know.

        Context:
        {context_text}

        Question:
        {query}
    """

    stream = client.chat.completions.create(
        model=settings.LLM_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful enterprise assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        stream=True
    )

    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            yield f"data: {chunk.choices[0].delta.content}\n\n"