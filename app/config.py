import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    AZURE_OPENAI_KEY=os.getenv("AZURE_OPENAI_KEY")
    AZURE_OPENAI_ENDPOINT=os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_VERSION=os.getenv("AZURE_OPENAI_VERSION")
    
    EMBEDDING_MODEL=os.getenv("AZURE_OPENAI_EMBEDDING_MODEL")
    LLM_MODEL=os.getenv("AZURE_OPENAI_MODEL")

settings=Settings()