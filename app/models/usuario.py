"""Modelo de Usuário/Prefeitura"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Usuario(Base):
    """Modelo de Usuário (Prefeitura/Município)"""
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(200), nullable=False)
    cpf = Column(String(14), unique=True, nullable=True)
    telefone = Column(String(20), nullable=True)
    data_nascimento = Column(Date, nullable=True)
    
    # Dados do município
    nome_municipio = Column(String(200), nullable=False)
    cnpj = Column(String(18), unique=True, nullable=False)
    uf = Column(String(2), nullable=False)
    cidade = Column(String(100), nullable=False)
    
    # Dados de acesso
    email = Column(String(100), unique=True, nullable=False, index=True)
    senha_hash = Column(String(255), nullable=False)
    
    # Status e plano
    plano = Column(String(20), default="gratuito", nullable=False)  # gratuito, basico, premium
    ativo = Column(Boolean, default=True, nullable=False)
    
    # Timestamps
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relacionamentos
    autorizacoes = relationship("Autorizacao", back_populates="usuario")
    tratamentos = relationship("TratamentoForaDomicilio", back_populates="usuario")
