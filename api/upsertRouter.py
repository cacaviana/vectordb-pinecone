from services.upsertServices import upsert_document, upsert_document_semmetadados
from services.miscellaneousServices import extract_text_from_pdf, split_text_into_chunks, split_text_into_chunks_maiores
from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import JSONResponse
import json


router = APIRouter(tags=["Upserts"])


@router.post('/upsert/upsert-pdf', summary="Enviar um arquivo PDF para a VectorStore", 
             description="Envie um arquivo PDF, ele irar extrair o texto, criar os chunks, o embeddings e salva na VectorStore",
             response_description="Quantos Vectores foram salvos no Index (BD) da Vectore Store")

async def upsert_vectorstore(filepdf: UploadFile):
    
    TextFromPDF = extract_text_from_pdf(filepdf)
    chucklist = split_text_into_chunks(text=TextFromPDF)
    upsert_response = upsert_document(index_name="itvalleycourses", chunks=chucklist, namespace="MasterIADEV")
    
    return {"message": f"Upsert realizado com sucesso. Total de chunks inseridos: {upsert_response}"}


@router.post('/upsert/upsert-pdf/metadonnes', summary="Enviar um arquivo PDF para a VectorStore + Metadados", 
             description="Envie um arquivo PDF, ele irar extrair o texto, criar os chunks, o embeddings e salva na VectorStore",
             response_description="Quantos Vectores foram salvos no Index (BD) da Vectore Store")

async def upsert_vectorstore(filepdf: UploadFile, metadone: str = Form(...)):


    metadone_dict = json.loads(metadone)

    TextFromPDF = extract_text_from_pdf(filepdf)
    chucklist = split_text_into_chunks(text=TextFromPDF)
    upsert_response = upsert_document(index_name="itvalleycourses", chunks=chucklist, namespace="MasterIADEV", metadone=metadone_dict)

    return {"message": f"Upsert realizado com sucesso. Total de chunks inseridos: {upsert_response}"}


@router.post('/upsert/upsert-pdf/client-finance', summary="Enviar um arquivo PDF para a VectorStore", 
             description="Envie um arquivo PDF, ele irar extrair o texto, criar os chunks, o embeddings e salva na VectorStore",
             response_description="Quantos Vectores foram salvos no Index (BD) da Vectore Store")

async def upsert_vectorstore_clientfinance(filepdf: UploadFile):
    
    TextFromPDF = extract_text_from_pdf(filepdf)
    chucklist = split_text_into_chunks_maiores(text=TextFromPDF)
    upsert_response = upsert_document_semmetadados(index_name="client-finance", chunks=chucklist, namespace="ClientFinance")
    
    return {"message": f"Upsert realizado com sucesso. Total de chunks inseridos: {upsert_response}"}











@router.post('/api/upsert/pdf_metadata_dict', summary="Upsert a document PDF into the database")
async def upsert_metadata(filepdf: UploadFile = File(...), metadata: MetadataModel = Form(...)):  

    
    metadate_dict = json.load(metadata)
    # metadataJson = json.loads(metadata)
    #textfromPDF = extract_text_from_pdf(filepdf)
    #chunckslistEmbbedings = await split_in_chuncks_embeddings(text=textfromPDF)
    #response = upsertService(embeddings=chunckslistEmbbedings)
    print(metadate_dict["terra"])

    
    return metadate_dict


def upsertService_text(chukstextList: list, metadata: dict[str, str]):
    
    index = pc.Index(host="https://itvalleyschool-xb3w3p4.svc.aped-4627-b74a.pinecone.io")
    try:    
        vectors = []

        for chuck_unit in chukstextList:
            embeddings = embeddingsService(chunck=chuck_unit)

            metadatacomplete = { **metadata, "chuck": chuck_unit}

            vectors.append({"id": f"{uuid.uuid4()}", "values": embeddings, "metadata": metadatacomplete})
        
        
        response = index.upsert(vectors=vectors,namespace="master-ia-pos")
        return {"message": "Document upserted successfully"}
    
    except Exception as e:
        return {"error": str(e)}


# Modelo da requisição
class UpsertRequest(BaseModel):
    index_name: str
    chunks: List[str]  # Lista de chunks de texto
    namespace: str
    metadone: Dict[str, str]  # Metadados no formato dicionário


from pydantic import BaseModel
from typing import List, Dict
from services.emdeggingsService import embeddingsService


# Modelo Pydantic para Metadata
class MetadataModel(BaseModel):
    metadata: Dict[str, str]


