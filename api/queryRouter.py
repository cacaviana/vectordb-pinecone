from fastapi import APIRouter
from services.queryServices import query_simple, query_filter
from services.embeddingsService import embedding_chunk_openAI
import json

router = APIRouter()


@router.post('/query/query-simple')
async def query_simples_router(seach:str, namespace: str = "MasterIADEV"):

    embedding_list = embedding_chunk_openAI(seach)
    list_embedding = embedding_list["data"][0]["embedding"]

    
    result_query = query_simple(namespace=namespace, vetor=list_embedding)
    print(result_query)
    print(type(result_query["matches"][0]))
    print(result_query["matches"])

    return  {f'Resulta:{result_query}'}

@router.post('/query/query-filter')
async def query_filter_router(seach:str, metadone: dict[str, str], namespace: str = "MasterIADEV"):
    
    embedding_list = embedding_chunk_openAI(seach)
    list_embedding = embedding_list["data"][0]["embedding"]
    
    result_query = query_filter(vetor=list_embedding, metadone=metadone, namespace=namespace)

    print(result_query)
    
    return {f'Result: {result_query}'}
