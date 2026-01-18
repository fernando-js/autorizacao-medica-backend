"""Aplicação principal FastAPI"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
from app.database import engine, Base
from app.routes import auth, autorizacoes, tratamentos

# Importar todos os modelos para garantir que são registrados
from app.models import Usuario, Autorizacao, TratamentoForaDomicilio

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Criar aplicação FastAPI
app = FastAPI(
    title="Sistema de Autorização Médica",
    description="API REST para gestão de autorizações médicas e tratamentos fora de domicílio",
    version="1.0.0"
)

# Configurar CORS
settings = get_settings()
origins = [origin.strip() for origin in settings.cors_origins.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(auth.router, prefix="/api")
app.include_router(autorizacoes.router, prefix="/api")
app.include_router(tratamentos.router, prefix="/api")


@app.get("/")
def root():
    """Rota raiz da API"""
    return {
        "message": "API do Sistema de Autorização Médica",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    """Health check da API"""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
