from pinecone.grpc import PineconeGRPC as Pinecone
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

#instanciar
def authentication_Pinecone():
    pc = Pinecone(api_key=os.getenv("API_KEY_PINECONE"))
    
    return pc

def authentication_OpenAI():
    clientOpenAi = OpenAI(api_key=os.getenv("API_KEY_OPENAI"))
    return clientOpenAi
