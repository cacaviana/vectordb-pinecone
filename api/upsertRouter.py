from services.upsertServices import upsert_document
from services.miscellaneousServices import extract_text_from_pdf, split_text_into_chunks
from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import JSONResponse
import json


router = APIRouter()


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










