from services.authenticationService import authentication_Pinecone
from services.embeddingsService import embedding_chunk_openAI
from pydantic import BaseModel
from typing import List, Dict

# Modelo da requisição
class UpsertRequest(BaseModel):
    index_name: str
    chunks: List[str]  # Lista de chunks de texto
    namespace: str
    metadone: Dict[str, str]  # Metadados no formato dicionário





pinecone_client = authentication_Pinecone()


def upsert_document(index_name: str, chunks: list, namespace: str):
    """
    Gera embeddings para chunks e realiza o upsert no banco vetorial.

    Args:
        index_name (str): Nome do índice no Pinecone.
        chunks (list): Lista de chunks de texto.
        embedding_model: Modelo de embeddings.
        namespace (str): Namespace para organizar os dados.

    Returns:
        dict: Resposta da operação de upsert.
    """
    vectors = []
    for i, chunk in enumerate(chunks):
        embedding = embedding_chunk_openAI(chunk)  # Gerar embedding
        
        
        vectors.append({
            "id": f"chunk-{i}",
            "values": embedding["data"][0]["embedding"],
            "metadata": {"chunk_text": chunk}
        })


    # Conectar ao índice e realizar o upsert
    index = pinecone_client.Index(index_name)
    response = index.upsert(vectors=vectors, namespace=namespace)
    print(response)
    return response

def upsert_document(index_name: str, chunks: list, namespace: str, metadone: dict[str, str]):
    """
    Gera embeddings para chunks e realiza o upsert no banco vetorial.

    Args:
        index_name (str): Nome do índice no Pinecone.
        chunks (list): Lista de chunks de texto.
        embedding_model: Modelo de embeddings.
        namespace (str): Namespace para organizar os dados.

    Returns:
        dict: Resposta da operação de upsert.
    """
    vectors = []
    for i, chunk in enumerate(chunks):
        embedding = embedding_chunk_openAI(chunk)  # Gerar embedding
        
        chunk_metadata = {**metadone, "chunk": chunk}

        vectors.append({
            "id": f"chunk-{i}",
            "values": embedding["data"][0]["embedding"],
            "metadata": chunk_metadata
        })


    # Conectar ao índice e realizar o upsert
    index = pinecone_client.Index(index_name)
    response = index.upsert(vectors=vectors, namespace=namespace)
    print(response)
    return response








def upsert_chunks(index_name: str, chunks: list, namespace="default"):
    """
    Gera embeddings para chunks e realiza o upsert no banco vetorial.

    Args:
        index_name (str): Nome do índice no Pinecone.
        chunks (list): Lista de chunks de texto.
        embedding_model: Modelo de embeddings.
        namespace (str): Namespace para organizar os dados.

    Returns:
        dict: Resposta da operação de upsert.
    """
    vectors = []
    for i, chunk in enumerate(chunks):
        embedding = embedding_chunk_openAI(chunk)  # Gerar embedding
        vectors.append({
            "id": f"chunk-{i}",
            "values": embedding["data"][0]["embeddings"],
            "metadata": {"chunk_text": chunk}
        })

    # Conectar ao índice e realizar o upsert
    index = pinecone_client.Index(index_name)
    response = index.upsert(vectors=vectors, namespace=namespace)
    return response

