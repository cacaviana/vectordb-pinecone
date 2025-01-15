from fastapi import APIRouter, Form
from services.assistantService import assistant_question
from services.queryServices import query_filter, query_filter_itvaley
from services.embeddingsService import embedding_chunk_openAI


router = APIRouter()



@router.post('/openai/assistant')
async def assistant_searc(question:str, shortextract:str):
    result = assistant_question(question=question, shortextract=shortextract)

    return result

@router.post('/openai/assistant/complete')
async def assistant_search(question:str, metadone: dict[str, str], namespace: str = "MasterIADEV"):

    embedding_list = embedding_chunk_openAI(question)
    list_embedding = embedding_list["data"][0]["embedding"]

    result_query = query_filter(vetor=list_embedding, metadone=metadone, namespace=namespace)
    excerpt = f'the excerpt{result_query}'
    
    result = assistant_question(question=question, shortextract=excerpt)

    return result

@router.post('/openai/assistant/clientfinance')
async def assistant_search(question:str, namespace: str = "ClientFinance"):

    embedding_list = embedding_chunk_openAI(question)
    list_embedding = embedding_list["data"][0]["embedding"]

    result_query = query_filter_itvaley(vetor=list_embedding, namespace=namespace)
    excerpt = f'the excerpt{result_query}'
    
    result = assistant_question(question=question, shortextract=excerpt)

    return result

