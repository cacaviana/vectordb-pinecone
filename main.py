from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

from api.indexRouter import router as api_index_router
from api.miscellaneousRouter import router as api_miscellaneous_router
from api.embeddingsRouter import router as api_embeddings_router
from api.upsertRouter import router as api_upsert_router
from api.queryRouter import router as api_query_router
from api.assistantRouter import router as api_openai_router

app = FastAPI()

# Configurações de CORS
def get_cors_origins():
    origins = os.getenv('CORS_ORIGINS')
    if origins:
        return [origin.strip() for origin in origins.split(',')]
    return []

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota básica de teste
@app.get("/")
def read_root():
    return {"message": "Servidor está rodando!"}

app.include_router(api_index_router)
app.include_router(api_miscellaneous_router)
app.include_router(api_embeddings_router)
app.include_router(api_upsert_router)
app.include_router(api_query_router)
app.include_router(api_openai_router)