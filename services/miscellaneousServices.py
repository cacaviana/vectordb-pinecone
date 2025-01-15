from PyPDF2 import PdfReader
from fastapi import UploadFile
from io import BytesIO

def extract_text_from_pdf(filepdf: UploadFile):
    """
    Extrai o texto de um arquivo PDF usando PyPDF2.

    Returns:
        str: Texto completo extraído do PDF.
    """
    pdf_byte = filepdf.file.read()
    pdf_stream = BytesIO(pdf_byte)

    reader = PdfReader(pdf_stream)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        #print(text)
    return text


def split_text_into_chunks(text: str, chunk_size=512, overlap=50) -> list:
    """
    Divide o texto em chunks menores com sobreposição.

    Args:
        text (str): Texto para dividir.
        chunk_size (int): Tamanho máximo de cada chunk.
        overlap (int): Número de caracteres sobrepostos entre chunks.

    Returns:
        list: Lista de chunks.
    """
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
        #print(i+chunk_size)
        #print(f"Total de chunks: {len(chunks)}")
        
    '''
    for chunk in chunks:
        print(f"Tipo de chunk: {type(chunk)}, Conteúdo: {chunk[:50]}...") 
    '''


    return chunks

def split_text_into_chunks_maiores(text: str, chunk_size=2048, overlap=200) -> list:
    """
    Divide o texto em chunks menores com sobreposição.

    Args:
        text (str): Texto para dividir.
        chunk_size (int): Tamanho máximo de cada chunk.
        overlap (int): Número de caracteres sobrepostos entre chunks.

    Returns:
        list: Lista de chunks.
    """
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
        #print(i+chunk_size)
        #print(f"Total de chunks: {len(chunks)}")
        
    '''
    for chunk in chunks:
        print(f"Tipo de chunk: {type(chunk)}, Conteúdo: {chunk[:50]}...") 
    '''


    return chunks

