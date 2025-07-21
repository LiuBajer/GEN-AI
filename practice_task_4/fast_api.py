from fastapi import FastAPI, HTTPException, Query
from models import ApmokymoDuomenys
from typing import Optional
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import json

app =  FastAPI(
    title="Apmokytojas",
    description="Apmokytojas",
    version="1.0.0",
)

@app.post("/ingest")
async def ingest_data(data: str = Query(..., description="Main data string"),
    chunk_size: int = Query(500, description="Chunk size"),
    overlap: int = Query(50, description="Overlap"),
    metadata: Optional[str] = Query(None, description="Optional metadata as JSON string"),):
    try:
        print("Received data:", data)
        print(f"Chunk Size: {chunk_size}")
        print(f"Overlap: {overlap}")
        print(f"Metadata: {metadata}")

        metadata_dict = json.loads(metadata) if metadata else {}
        doc = Document(page_content=data, metadata=metadata_dict)
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap
        )
        chunks = splitter.split_documents([doc])

        chunk_contents = [chunk.page_content for chunk in chunks]

        return {
            "status": "success",
            "message": "Data ingested successfully.",
            "details": {
                "chunk_size": chunk_size,
                "overlap": overlap,
                "metadata_keys": list(metadata.keys()) if metadata else []
            },
            "chunks": chunk_contents,
            "chunk_count": len(chunks)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occured: {str(e)}")
    
@app.get("/")
def test():
    return {"message": "Connection is ok"}