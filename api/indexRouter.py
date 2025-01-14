from fastapi import APIRouter
from fastapi.responses import JSONResponse
from services.indexServices import create_index, details_index, listall_index



router = APIRouter()




@router.post('/index/create-index',
            description="Criar um index (novo BD) no Pinecone",
            summary="Criar um index (novo BD) no Pinecone",
            response_description="Null - Se tiver tudo ok.")

async def create_index_pinecone(name: str):
    response = create_index(name=name)
    
    return JSONResponse(content=response)




@router.post('/index/details-index', summary="Exibe detalhes do Index, como nome, , host, dimension etc..")
async def details_index_pinecone(name: str):
    response = details_index(name=name)
    
    return JSONResponse(content=response)

@router.post('/index/list-all', summary="Lista todos os Index do Pinecone")
async def listall_index_pinecone():
    response = listall_index()
    return JSONResponse(content=response)