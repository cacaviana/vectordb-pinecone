from fastapi import APIRouter, UploadFile, File, HTTPException
from services.miscellaneousServices import extract_text_from_pdf, split_text_into_chunks
from services.embeddingsService import embedding_chunk_openAI
from fastapi.responses import JSONResponse



router = APIRouter()

@router.post('/miscellaneous/pdf_to_text', summary="recebe um arquivo PDF e extrai o texto desse arquivo")
async def pdf_to_text(file: UploadFile = File(...)):
    try:
        text = extract_text_from_pdf(file)
        return JSONResponse(content={"text": text})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
    
  
@router.post('/miscellaneous/split_in_chuncks_oficial', 
             summary="Endpoint para dividir texto em chunks", 
             description= "text (str): Texto para dividir.  Returns: list: Lista de chunks gerados.")
async def split_in_chunck_oficial(text: str):

    try:
        # Tenta executar a função split_text_into_chunks
        response = split_text_into_chunks(text=text)
        for i, chunk in enumerate(response):
            embedding = embedding_chunk_openAI(chunk)  # Gerar embedding
        return JSONResponse(embedding)
    except Exception as e:
        # Trata qualquer erro e retorna uma exceção HTTP 400
        raise HTTPException(status_code=400, detail=f"Erro ao dividir texto em chunks: {str(e)}")
    


