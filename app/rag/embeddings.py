from openai import AzureOpenAI
from app.config import settings

client=AzureOpenAI(
        api_key=settings.AZURE_OPENAI_KEY,
        api_version=settings.AZURE_OPENAI_VERSION,
        azure_endpoint=settings.AZURE_OPENAI_ENDPOINT
    )

def get_embedding(text: str):
    response=client.embeddings.create(
        model=settings.EMBEDDING_MODEL,
        input=text
    )
    return response.data[0].embedding