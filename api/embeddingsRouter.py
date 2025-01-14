from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from services.embeddingsService import embedding_chunk_openAI



router = APIRouter()

@router.post('/embeddings/simple-embeddings', summary="Cria um embedding de um trecho de texto")
def embedding_chunk_openAI_router(chunk: str):

    
    embedding = embedding_chunk_openAI(chunk=chunk)
    print(len(embedding["data"][0]["embedding"]))
  
    return JSONResponse(embedding)