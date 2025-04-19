from services.authenticationService import authentication_Pinecone
import os
from dotenv import load_dotenv

load_dotenv()


pinecone_client = authentication_Pinecone()

def query_simple(vetor: list[float], namespace: str):

    index = pinecone_client.Index(host=os.getenv("HOST_PINECONE"))

    result_query = index.query(
        namespace=namespace,
        vector=vetor,
        top_k=4
    )

    return result_query

def query_filter(vetor: list[float], metadone: dict[str, str], namespace: str):

    index = pinecone_client.Index(host=os.getenv("HOST_PINECONE"))

    result_query = index.query(
        namespace=namespace,
        vector=vetor,
        top_k=1000,
        filter=metadone,
        include_metadata=True
    )

    return result_query

def query_filter_itvaley(vetor: list[float], namespace: str):

    index = pinecone_client.Index(host="https://client-finance-xb3w3p4.svc.aped-4627-b74a.pinecone.io")

    result_query = index.query(
        namespace=namespace,
        vector=vetor,
        top_k=30,
        include_metadata=True
    )

    return result_query