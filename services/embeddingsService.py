from services.authenticationService import authentication_Pinecone, authentication_OpenAI
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec



pinecone_client = authentication_Pinecone()
openai_client = authentication_OpenAI()




def embedding_chunk_openAI(chunk: str):

    
    embedding = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk
    )
  
    return embedding.to_dict()

def embedding_chunk_openAI_client_finance(chunk: str):

    
    embedding = openai_client.embeddings.create(
        model="text-embedding-ada-002",
        input=chunk
    )
  
    return embedding.to_dict()
