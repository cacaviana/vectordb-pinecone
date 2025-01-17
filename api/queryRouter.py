from fastapi import APIRouter
from services.queryServices import query_simple, query_filter, query_filter_itvaley
from services.embeddingsService import embedding_chunk_openAI, embedding_chunk_openAI_client_finance
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
async def query_filter_router(seach:str, namespace: str = "MasterIADEV"):
    
    embedding_list = embedding_chunk_openAI(seach)
    list_embedding = embedding_list["data"][0]["embedding"]
    
    result_query = query_filter(vetor=list_embedding, namespace=namespace)

    print(result_query)
    
    return {f'Result: {result_query}'}

@router.post('/query/query-filter/client-finance')
async def query_filter_router_finance(seach:str, namespace: str = "ClientFinance"):
    
    embedding_list = embedding_chunk_openAI_client_finance(seach)
    list_embedding = embedding_list["data"][0]["embedding"]
    
    result_query = query_filter_itvaley(vetor=list_embedding, namespace=namespace)

    print(result_query)
    
    return {f'Result: {result_query}'}
