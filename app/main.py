import shutil
import os
from fastapi import FastAPI, UploadFile, File
from app.rag.ingestion import ingest_document
from app.rag.retrieval import retrieve_context, stream_answer
from app.schemas import Query_Request
from fastapi.responses import StreamingResponse

app = FastAPI()

UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = ingest_document(file_path)
    return result

@app.post("/query-stream")
async def query_stream(request: Query_Request):
    contexts=retrieve_context(request.query)
    
    return StreamingResponse(
        stream_answer(request.query, contexts),
        media_type="text/event-stream"
    )

