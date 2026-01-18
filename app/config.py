"""Configurações da aplicação"""
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Configurações da aplicação"""
    
    # Ambiente
    environment: str = "development"
    
    # Segurança
    secret_key: str = "change-me-in-production-secret-key-not-secure"  # Valor padrão temporário
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Banco de dados
    database_url: str = "sqlite:///./autorizacao_medica.db"
    
    # CORS
    cors_origins: str = "http://localhost:8000,http://127.0.0.1:8000"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Retorna as configurações da aplicação (cacheado)"""
    return Settings()
