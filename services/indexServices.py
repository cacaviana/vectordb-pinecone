from pinecone import ServerlessSpec
from services.authenticationService import authentication_Pinecone


pinecone_client = authentication_Pinecone()

def create_index(name: str):
    try:
        # Tentando criar o índice no Pinecone
        response = pinecone_client.create_index(
            name=name,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            deletion_protection="disabled"
        )
        print(f"Índice '{name}' criado com sucesso!")
        return {"message": f"Banco '{name}' criado com sucesso!", "response": response}

    except Exception as e:
        # Tratando erros e retornando uma mensagem clara
        error_message = f"Erro ao criar o banco '{name}': {str(e)}"
        print(error_message)
        return {"error": error_message}

def details_index(name: str):
    response = pinecone_client.describe_index(name=name)

    return response.to_dict()

def listall_index():
    response = pinecone_client.list_indexes()
   
    return response.to_dict()